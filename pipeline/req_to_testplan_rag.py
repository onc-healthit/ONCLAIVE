import re
import os
import logging
import time
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Union
from collections import defaultdict
import llm_utils
import prompt_utils

import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
from copy import deepcopy

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a specialized FHIR testing engineer with expertise in healthcare interoperability.
Your task is to analyze FHIR Implementation Guide requirements and generate practical, implementable test specifications."""

# Constants
PROJECT_ROOT = Path.cwd().parent  # Go up one level to project root
CURRENT_DIR = Path.cwd()  # Current working directory (test_kit_dev)
DEFAULT_INPUT_DIR = Path(PROJECT_ROOT, 'reqs_extraction', 'revised_reqs_output')  # Default input directory
DEFAULT_OUTPUT_DIR = Path(CURRENT_DIR, 'test_plan_output')  # Default output directory
DEFAULT_CAPABILITY_DIR = Path(PROJECT_ROOT, 'full-ig', 'markdown7_cleaned')  # Default capability statement directory

# Create output directory if it doesn't exist
DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# # Function to find capability statement files
# def find_capability_statement_files(directory=DEFAULT_CAPABILITY_DIR):
#     """Find files containing 'CapabilityStatement' in the filename"""
#     if not directory.exists():
#         logger.warning(f"Capability statement directory {directory} does not exist")
#         return []
    
#     capability_files = list(directory.glob("*CapabilityStatement*.md"))
#     capability_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
#     return capability_files

def chunk_capability_statement(capability_statement_file: str) -> List[str]:
    """
    Simpler version: Just split by headings, keep tables with their sections
    """
    with open(capability_statement_file, 'r') as f:
        content = f.read()
    
    chunks = []
    
    # Split by markdown headings (# through ####)
    heading_pattern = r'\n(?=#{1,4}\s)'
    sections = re.split(heading_pattern, content)
    
    for section in sections:
        section = section.strip()
        
        # Skip very small sections
        if len(section) < 50:
            continue
        
        # Determine the context type
        heading_match = re.match(r'(#{1,4})\s+(.+?)(?:\n|$)', section)
        if heading_match:
            heading_level = len(heading_match.group(1))
            heading_title = heading_match.group(2).strip()
            
            # Categorize by heading level and content
            if heading_level == 1:
                context_type = "Document Title"
            elif heading_level == 2:
                context_type = "Major Section"
            elif heading_level == 3:
                context_type = "Resource/Component"
            elif heading_level == 4:
                context_type = "Resource Detail"
            else:
                context_type = "Section"
        else:
            context_type = "Document Header"
        
        # Clean up the section content
        clean_section = re.sub(r'\n\s*\n', '\n\n', section)
        clean_section = clean_section.strip()
        
        # Add with appropriate context
        chunks.append(f"FHIR {context_type}: {clean_section}")
    
    return chunks

def instantiate_capability_vectordb(capability_statement_file: str, collection_name: str = "capability_statements"):
    """
    Create ChromaDB collection from capability statement chunks
    """
    chroma_client = chromadb.Client()
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-mpnet-base-v2"
    )
    
    # Check if collection already exists
    if collection_name in [c.name for c in chroma_client.list_collections()]:
        collection = chroma_client.get_collection(collection_name, embedding_function=sentence_transformer_ef)
        logger.info(f"Using existing collection: {collection_name}")
    else:
        # Create new collection
        chunks = chunk_capability_statement(capability_statement_file)
        logger.info(f"Created {len(chunks)} capability chunks")
        
        collection = chroma_client.create_collection(name=collection_name, embedding_function=sentence_transformer_ef)
        
        # Add chunks to collection
        collection.add(
            documents=chunks,
            ids=[str(x) for x in range(len(chunks))]
        )
        logger.info(f"Created new collection: {collection_name} with {len(chunks)} documents")
    
    return collection


def retrieve_relevant_capability_info(requirement: Dict[str, str], collection, n_examples: int = 5, verbose: bool = False) -> str:
    """
    Retrieve most relevant capability information for a requirement using ChromaDB
    """
    # Create query from requirement
    query_parts = [
        requirement.get('summary', ''),
        requirement.get('description', ''),
        requirement.get('actor', ''),
        f"FHIR {requirement.get('conformance', '')}"
    ]
    query = " ".join(filter(None, query_parts))
    
    if verbose:
        req_id = requirement.get('id', 'UNKNOWN-ID')
        print(f"\n{'='*80}")
        print(f"RAG RETRIEVAL FOR {req_id}")
        print(f"{'='*80}")
        print(f"Query: {query}")
        print(f"Searching for {n_examples} most relevant capability chunks...")
    
    # Query the collection
    results = collection.query(
        query_texts=[query],
        n_results=n_examples
    )
    
    if verbose:
        print(f"\nFound {len(results['documents'][0])} matching chunks:")
        for i, doc in enumerate(results['documents'][0]):
            distance = results.get('distances', [[]])[0][i] if results.get('distances') else 'N/A'
            print(f"\n  Match {i+1} (distance: {distance}):")
            print(f"  Length: {len(doc)} chars")
            print(f"  Preview: {doc[:100]}...")
            if len(doc) > 100:
                print(f"  ...{doc[-50:]}")
        print(f"{'='*80}\n")
    
    # Format results
    capability_info = "### Relevant Capability Statement Information\n\n"
    
    for i, doc in enumerate(results['documents'][0]):
        capability_info += f"**Relevant Capability {i+1}**:\n"
        capability_info += f"{doc}\n\n"
    
    return capability_info



def get_test_plan_prompt(requirement: str, capability_info: str) -> str:
    """Load the test plan prompt from file and format it with requirement and capability info"""
    return prompt_utils.load_prompt(
        TEST_PLAN_PATH,
        requirement=requirement,
        capability_info=capability_info
    )

# Setup the prompt environment
prompt_env = prompt_utils.setup_prompt_environment(PROJECT_ROOT)
PROMPT_DIR = prompt_env["prompt_dir"]
TEST_PLAN_PATH = prompt_env["test_plan_gen_path"]
REQUIREMENT_GROUPING_PATH = prompt_env["requirement_grouping_path"]

def format_requirement_for_prompt(requirement: Dict[str, str]) -> str:
    """
    Format a requirement dictionary into markdown for inclusion in prompts
    
    Args:
        requirement: Requirement dictionary
        
    Returns:
        Formatted markdown string
    """
    formatted = f"# {requirement.get('id', 'UNKNOWN-ID')}\n"
    formatted += f"**Summary**: {requirement.get('summary', '')}\n"
    formatted += f"**Description**: {requirement.get('description', '')}\n"
    formatted += f"**Verification**: {requirement.get('verification', '')}\n"
    formatted += f"**Actor**: {requirement.get('actor', '')}\n"
    formatted += f"**Conformance**: {requirement.get('conformance', '')}\n"
    formatted += f"**Conditional**: {requirement.get('conditional', '')}\n"
    formatted += f"**Source**: {requirement.get('source', '')}\n"
    
    return formatted


def get_test_plan_prompt(requirement: str, capability_info: str) -> str:
    """Load the test plan prompt from file and format it with requirement and capability info"""
    return prompt_utils.load_prompt(
        TEST_PLAN_PATH,
        requirement=requirement,
        capability_info=capability_info
    )

def get_requirement_grouping_prompt(requirement: str) -> str:
    """Load the requirement grouping prompt from file and format it with requirement info"""
    return prompt_utils.load_prompt(
        REQUIREMENT_GROUPING_PATH,
        requirement=requirement
    )



# def extract_relevant_capability_info_rag(
#     requirement: Dict[str, str], 
#     rag_system: SimpleFHIRRAG, 
#     verbose: bool = False
# ) -> str:
#     """
#     Extract relevant capability information using RAG instead of keyword matching
#     """
#     return rag_system.retrieve_relevant_info(requirement, top_k=5, verbose=verbose)


def load_requirements(req_file):
    if req_file.endswith('.json'):
        with open(req_file) as f:
            data = json.load(f)
        return data
    elif req_file.endswith('.md'):
        # Use the markdown parser
        return parse_requirements_file(req_file)
    else:
        raise ValueError(f"Unsupported file format: {req_file}. Must be .json or .md")
    
    

def parse_requirements_file(file_path: str) -> List[Dict[str, str]]:
    """
    Parse an INCOSE requirements markdown file into a structured list of requirements
    
    Args:
        file_path: Path to the requirements markdown file
        
    Returns:
        List of dictionaries containing structured requirement information
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split by requirement sections (separated by ---)
    req_sections = content.split('---')
    
    requirements = []
    for section in req_sections:
        if not section.strip():
            continue
            
        # Parse requirement data
        req_data = {}
        
        # Extract ID from format "# REQ-XX"
        id_match = re.search(r'#\s+([A-Z0-9\-]+)', section)
        if id_match:
            req_data['id'] = id_match.group(1)
        
        # Extract other fields
        for field in ['Summary', 'Description', 'Verification', 'Actor', 'Conformance', 'Conditional', 'Source']:
            pattern = rf'\*\*{field}\*\*:\s*(.*?)(?:\n\*\*|\n---|\Z)'
            field_match = re.search(pattern, section, re.DOTALL)
            if field_match:
                req_data[field.lower()] = field_match.group(1).strip()
        
        if req_data:
            # Format to match expected structure (same as JSON format)
            formatted_req = {
                'id': req_data.get('id', 'UNKNOWN'),
                'parsed': req_data
            }
            requirements.append(formatted_req)
    
    return requirements

def identify_requirement_group(
    logger,
    llm_clients,
    api_type,
    req,
) -> str:
    """
    Identify the appropriate group for a requirement using LLM only
    """
    requirement = req['parsed']
    logger.info(f"Identifying group for requirement {req.get('id', 'unknown')} using {api_type}...")
    
    # Format requirement as markdown
    formatted_req = format_requirement_for_prompt(requirement)
    
    # Retrieve prompt with the requirement using external file
    prompt = get_requirement_grouping_prompt(formatted_req)
    
    # Make the API request with simplified system prompt
    group_system_prompt = "You are a FHIR expert who categorizes requirements by their functional or resource type."
    # Use consistent method name
    group_name = llm_clients.make_llm_request(api_type, prompt, group_system_prompt).strip()
    
    # Clean up response (in case model returns extra text)
    if '\n' in group_name:
        group_name = group_name.split('\n')[0].strip()
    
    return group_name


def generate_test_specification_with_capability(
    logger,
    api_type: str,
    llm_clients,
    requirement: Dict[str, str],
    capability_collection,
    verbose: bool = False
) -> str:
    """
    Generate a comprehensive test specification using capability info from ChromaDB
    """
    req_id = requirement.get('id', 'unknown')
    req_parsed = requirement.get('parsed', {})
    logger.info(f"Generating test specification for {req_id} using {api_type}...")
    
    if verbose:
        print(f"\nProcessing {req_id}: {req_parsed.get('summary', 'No summary')}")
    
    # Format requirement as markdown
    formatted_req = format_requirement_for_prompt(req_parsed)
    
    # Extract relevant capability information using ChromaDB
    capability_info = retrieve_relevant_capability_info(req_parsed, capability_collection, verbose=verbose)

    # Create prompt with the requirement and capability information
    prompt = get_test_plan_prompt(formatted_req, capability_info)
    
    if verbose:
        print(f"Sending request to {api_type.upper()} API...")
    
    # Make the API request
    result = llm_clients.make_llm_request(api_type, prompt, SYSTEM_PROMPT)
    
    if verbose:
        print(f"Completed test specification for {req_id}")
    
    return result



def generate_consolidated_test_plan(
    llm_clients,
    api_type,
    logger: any,
    requirements_file: str,
    capability_statement_file: str = None,
    ig_name: str = "FHIR Implementation Guide",
    output_dir: str = None,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    Process requirements and generate a consolidated test plan using ChromaDB
    """
    # Use default output directory if none provided
    if output_dir is None:
        output_dir = DEFAULT_OUTPUT_DIR
    else:
        if not isinstance(output_dir, Path):
            output_dir = Path(output_dir)
    
    logger.info(f"Starting test plan generation with {api_type} for {ig_name}")

    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        # Parse requirements from file
        requirements = load_requirements(requirements_file)
        logger.info(f"Parsed {len(requirements)} requirements from {requirements_file}")
        
        # Initialize ChromaDB collection for capability statements
        capability_collection = instantiate_capability_vectordb(capability_statement_file)
        logger.info(f"Initialized capability collection from {capability_statement_file}")
        
        # Identify groups for each requirement
        req_groups = {}
        for req in requirements:
            req_id = req.get('id', 'UNKNOWN-ID')
            req_groups[req_id] = identify_requirement_group(logger, llm_clients, api_type, req)
        
        # Group requirements by identified category
        grouped_requirements = defaultdict(list)
        for req in requirements:
            req_id = req.get('id', 'UNKNOWN-ID')
            group = req_groups.get(req_id, 'Uncategorized')
            grouped_requirements[group].append(req)
            
        # Log the grouping results
        logger.info(f"Requirements grouped into {len(grouped_requirements)} categories")
        for group, reqs in grouped_requirements.items():
            logger.info(f"Group '{group}': {len(reqs)} requirements")
        
        # Update output file path to use Path object
        test_plan_path = output_dir / f"{api_type}_test_plan_{timestamp}.md"
        
        # Initialize test plan content
        test_plan = f"# Consolidated Test Plan for {ig_name}\n\n"
        test_plan += f"## Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        test_plan += f"## API Type: {api_type}\n\n"
        
        test_plan += "## Table of Contents\n\n"
        
        # Add group headers to TOC
        for group in sorted(grouped_requirements.keys()):
            test_plan += f"- [{group}](#{group.lower().replace(' ', '-')})\n"
            for req in grouped_requirements[group]:
                req_id = req.get('id', 'UNKNOWN-ID')
                req_summary = req['parsed'].get('summary', 'No summary')
                test_plan += f"  - [{req_id}: {req_summary}](#{req_id.lower()})\n"
        
        # Process each group and its requirements
        test_plan += "\n## Test Specifications\n\n"
        
        for group in sorted(grouped_requirements.keys()):
            # Add group header with anchor for TOC linking
            test_plan += f"<a id='{group.lower().replace(' ', '-')}'></a>\n\n"
            test_plan += f"## {group}\n\n"
            
            if verbose:
                print(f"\nProcessing Group: {group} ({len(grouped_requirements[group])} requirements)")
            
            # Process each requirement in the group
            for i, req in enumerate(grouped_requirements[group]):
                req_id = req.get('id', 'UNKNOWN-ID')
                logger.info(f"Processing requirement for group '{group}': {req_id}")
                
                test_spec = generate_test_specification_with_capability(
                    logger, api_type, llm_clients, req, capability_collection, verbose=verbose
                )
                
                # Add to test plan content with proper anchor for TOC linking
                test_plan += f"<a id='{req_id.lower()}'></a>\n\n"
                test_plan += f"### {req_id}: {req['parsed'].get('summary', 'No summary')}\n\n"
                test_plan += f"**Description**: {req['parsed'].get('description', '')}\n\n"
                test_plan += f"**Actor**: {req['parsed'].get('actor', '')}\n\n"
                test_plan += f"**Conformance**: {req['parsed'].get('conformance', '')}\n\n"
                test_plan += f"{test_spec}\n\n"
                test_plan += "---\n\n"
                
                # Add delay between requests
                if i < len(grouped_requirements[group]) - 1:  # No need to delay after the last request
                    time.sleep(llm_clients.config[api_type]["delay_between_chunks"])
            
            # Add spacing between groups
            test_plan += "\n\n"
        
        # Save consolidated test plan
        with open(test_plan_path, 'w') as f:
            f.write(test_plan)
        logger.info(f"Consolidated test plan saved to {test_plan_path}")
        
        return {
            "requirements_count": len(requirements),
            "group_count": len(grouped_requirements),
            "test_plan_path": str(test_plan_path)
        }
        
    except Exception as e:
        logger.error(f"Error processing requirements: {str(e)}")
        raise


def clear_capability_collection(collection_name: str = "capability_statements"):
    """
    Delete the existing ChromaDB collection so it can be recreated with new chunking
    """
    chroma_client = chromadb.Client()
    
    try:
        # Check if collection exists and delete it
        existing_collections = [c.name for c in chroma_client.list_collections()]
        if collection_name in existing_collections:
            chroma_client.delete_collection(collection_name)
            print(f"Deleted existing collection: {collection_name}")
        else:
            print(f"No existing collection found: {collection_name}")
    except Exception as e:
        print(f"Error clearing collection: {e}")