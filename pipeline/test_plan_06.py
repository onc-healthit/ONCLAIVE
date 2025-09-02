"""
FHIR Test Plan Generation with RAG

This module generates comprehensive test plans from FHIR Implementation Guide requirements
using Retrieval-Augmented Generation (RAG) with capability statements.

Features:
- Parse requirements from markdown or JSON files
- Use ChromaDB for semantic search of capability statements
- Generate contextually-aware test specifications
- Group requirements by functional categories
- Output consolidated test plans with navigation

Usage:
    from req_to_testplan_rag import generate_consolidated_test_plan, clear_capability_collection
    
    # Generate test plan
    result = generate_consolidated_test_plan(
        client_instance=client,
        api_type="claude", 
        requirements_file="requirements.md",
        capability_statement_file="capability.md"
    )
"""

import re
import logging
import time
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from collections import defaultdict

import chromadb
from chromadb.utils import embedding_functions

import llm_utils
import prompt_utils

# Constants
PROJECT_ROOT = Path.cwd().parent
CURRENT_DIR = Path.cwd()

# System prompt for test plan generation
SYSTEM_PROMPT = """You are a specialized FHIR testing engineer with expertise in healthcare interoperability.
Your task is to analyze FHIR Implementation Guide requirements and generate practical, implementable test specifications."""

# Setup the prompt environment
prompt_env = prompt_utils.setup_prompt_environment(PROJECT_ROOT)
PROMPT_DIR = prompt_env["prompt_dir"]
TEST_PLAN_PATH = prompt_env["test_plan_gen_path"]
REQUIREMENT_GROUPING_PATH = prompt_env["requirement_grouping_path"]

# Setup logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def chunk_capability_statement(capability_statement_file: str) -> List[str]:
    """
    Split capability statement into semantic chunks for RAG retrieval.
    
    Args:
        capability_statement_file: Path to capability statement markdown file
        
    Returns:
        List of capability statement chunks with context labels
        
    Note:
        Splits by markdown headings and adds context type labels for better retrieval
    """
    with open(capability_statement_file, 'r', encoding='utf-8') as f:
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
    Create or retrieve ChromaDB collection from capability statement chunks.
    
    Args:
        capability_statement_file: Path to capability statement file
        collection_name: Name for the ChromaDB collection
        
    Returns:
        ChromaDB collection instance
    """
    chroma_client = chromadb.Client()
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-mpnet-base-v2"
    )
    
    # Check if collection already exists
    existing_collections = [c.name for c in chroma_client.list_collections()]
    if collection_name in existing_collections:
        collection = chroma_client.get_collection(collection_name, embedding_function=sentence_transformer_ef)
        logging.info(f"Using existing ChromaDB collection: {collection_name}")
    else:
        # Create new collection
        chunks = chunk_capability_statement(capability_statement_file)
        logging.info(f"Created {len(chunks)} capability chunks from {capability_statement_file}")
        
        collection = chroma_client.create_collection(name=collection_name, embedding_function=sentence_transformer_ef)
        
        # Add chunks to collection
        collection.add(
            documents=chunks,
            ids=[str(x) for x in range(len(chunks))]
        )
        logging.info(f"Created new ChromaDB collection: {collection_name} with {len(chunks)} documents")
    
    return collection


def retrieve_relevant_capability_info(requirement: Dict[str, str], collection, n_examples: int = 2, verbose: bool = False) -> str:
    """
    Retrieve most relevant capability information for a requirement using ChromaDB.
    
    Args:
        requirement: Requirement dictionary with parsed fields
        collection: ChromaDB collection instance
        n_examples: Number of relevant chunks to retrieve
        verbose: Whether to print detailed retrieval information
        
    Returns:
        Formatted string containing relevant capability information
    """
    # Create query from requirement
    query_parts = [
        requirement.get('summary', ''),
        requirement.get('text', ''),
        requirement.get('context', ''),
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
    """
    Load the test plan prompt from file and format it with requirement and capability info.
    
    Args:
        requirement: Formatted requirement string
        capability_info: Retrieved capability information
        
    Returns:
        Formatted prompt for test plan generation
    """
    return prompt_utils.load_prompt(
        TEST_PLAN_PATH,
        requirement=requirement,
        capability_info=capability_info
    )


def get_requirement_grouping_prompt(requirement: str) -> str:
    """
    Load the requirement grouping prompt from file and format it with requirement info.
    
    Args:
        requirement: Formatted requirement string
        
    Returns:
        Formatted prompt for requirement grouping
    """
    return prompt_utils.load_prompt(
        REQUIREMENT_GROUPING_PATH,
        requirement=requirement
    )


def format_requirement_for_prompt(requirement: Dict[str, str]) -> str:
    """
    Format a requirement dictionary into markdown for inclusion in prompts.
    
    Args:
        requirement: Requirement dictionary with parsed fields
        
    Returns:
        Formatted markdown string ready for prompt inclusion
    """
    formatted = f"# {requirement.get('id', 'UNKNOWN-ID')}\n"
    formatted += f"**Summary**: {requirement.get('summary', '')}\n"
    formatted += f"**Text**: {requirement.get('text', '')}\n"
    formatted += f"**Context**: {requirement.get('context', '')}\n"
    formatted += f"**Verification**: {requirement.get('verification', '')}\n"
    formatted += f"**Actor**: {requirement.get('actor', '')}\n"
    formatted += f"**Conformance**: {requirement.get('conformance', '')}\n"
    formatted += f"**Conditional**: {requirement.get('conditional', '')}\n"
    formatted += f"**Source**: {requirement.get('source', '')}\n"
    
    return formatted


def parse_requirements_file(file_path: str) -> List[Dict[str, str]]:
    """
    Parse an INCOSE requirements markdown file into a structured list of requirements.
    
    Args:
        file_path: Path to the requirements markdown file
        
    Returns:
        List of dictionaries containing structured requirement information
        
    Note:
        Expects requirements separated by --- with fields like **Summary**, **Text**, etc.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
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
        for field in ['Summary', 'Text', 'Context', 'Verification', 'Actor', 'Conformance', 'Conditional', 'Source']:
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


def load_requirements(req_file: str) -> List[Dict[str, Any]]:
    """
    Load requirements from either JSON or markdown file.
    
    Args:
        req_file: Path to requirements file (.json or .md)
        
    Returns:
        List of requirement dictionaries
        
    Raises:
        ValueError: If file format is unsupported
    """
    if req_file.endswith('.json'):
        with open(req_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    elif req_file.endswith('.md'):
        return parse_requirements_file(req_file)
    else:
        raise ValueError(f"Unsupported file format: {req_file}. Must be .json or .md")


def identify_requirement_group(client_instance, api_type: str, req: Dict[str, Any]) -> str:
    """
    Identify the appropriate group for a requirement using LLM analysis.
    
    Args:
        client_instance: LLM client instance
        api_type: Type of API to use ('claude', 'gemini', 'gpt')
        req: Requirement dictionary
        
    Returns:
        Group name for the requirement
    """
    requirement = req['parsed']
    req_id = req.get('id', 'unknown')
    logging.info(f"Identifying group for requirement {req_id} using {api_type}")
    
    # Format requirement as markdown
    formatted_req = format_requirement_for_prompt(requirement)
    
    # Retrieve prompt with the requirement using external file
    prompt = get_requirement_grouping_prompt(formatted_req)
    
    # Make the API request with simplified system prompt
    group_system_prompt = "You are a FHIR expert who categorizes requirements by their functional or resource type."
    group_name = client_instance.make_llm_request(api_type, prompt, group_system_prompt).strip()
    
    # Clean up response (in case model returns extra text)
    if '\n' in group_name:
        group_name = group_name.split('\n')[0].strip()
    
    return group_name


def generate_test_specification_with_capability(api_type: str, client_instance, requirement: Dict[str, str],
                                               capability_collection, verbose: bool = False) -> str:
    """
    Generate a comprehensive test specification using capability info from ChromaDB.
    
    Args:
        api_type: Type of API to use for generation
        client_instance: LLM client instance
        requirement: Requirement dictionary
        capability_collection: ChromaDB collection for capability statements
        verbose: Whether to print detailed processing information
        
    Returns:
        Generated test specification text
    """
    req_id = requirement.get('id', 'unknown')
    req_parsed = requirement.get('parsed', {})
    logging.info(f"Generating test specification for {req_id} using {api_type}")
    
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
    result = client_instance.make_llm_request(api_type, prompt, SYSTEM_PROMPT)
    
    if verbose:
        print(f"Completed test specification for {req_id}")
    
    return result


def generate_consolidated_test_plan(client_instance, api_type: str, requirements_file: str,
                                   capability_statement_file: str, ig_name: str = "FHIR Implementation Guide",
                                   output_dir: str = None, verbose: bool = True) -> Dict[str, Any]:
    """
    Process requirements and generate a consolidated test plan using ChromaDB RAG.
    
    This is the main function that orchestrates the entire test plan generation process:
    1. Load and parse requirements
    2. Initialize ChromaDB with capability statements
    3. Group requirements by functional category
    4. Generate test specifications for each requirement
    5. Create consolidated test plan document
    
    Args:
        client_instance: LLM client instance
        api_type: Type of API to use ('claude', 'gemini', 'gpt')
        requirements_file: Path to requirements file (.md or .json)
        capability_statement_file: Path to capability statement file
        ig_name: Name of the implementation guide
        output_dir: Output directory (uses default if None)
        verbose: Whether to show detailed progress information
        
    Returns:
        Dictionary containing:
            - requirements_count: Number of requirements processed
            - group_count: Number of requirement groups created
            - test_plan_path: Path to generated test plan file
            
    Raises:
        Exception: For various processing errors
    """
    # Set up output directory
    if output_dir is None:
        output_dir = Path(CURRENT_DIR, 'test_plan_output')
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print(f"\n{'='*80}")
    print(f"FHIR TEST PLAN GENERATION")
    print(f"{'='*80}")
    print(f"Implementation Guide: {ig_name}")
    print(f"Requirements file: {requirements_file}")
    print(f"Capability file: {capability_statement_file}")
    print(f"API: {api_type}")
    print(f"Output directory: {output_dir}")
    print()
    
    try:
        # Parse requirements from file
        print("Loading requirements...")
        requirements = load_requirements(requirements_file)
        print(f"Loaded {len(requirements)} requirements")
        logging.info(f"Parsed {len(requirements)} requirements from {requirements_file}")
        
        # Initialize ChromaDB collection for capability statements
        print("Setting up capability knowledge base...")
        capability_collection = instantiate_capability_vectordb(capability_statement_file)
        print("Capability knowledge base ready")
        
        # Identify groups for each requirement
        print(f"\nGrouping requirements...")
        req_groups = {}
        for i, req in enumerate(requirements, 1):
            req_id = req.get('id', 'UNKNOWN-ID')
            print(f"  Analyzing requirement {i}/{len(requirements)}: {req_id}", end='\r')
            req_groups[req_id] = identify_requirement_group(client_instance, api_type, req)
        
        print(f"  Completed grouping {len(requirements)} requirements                    ")
        
        # Group requirements by identified category
        grouped_requirements = defaultdict(list)
        for req in requirements:
            req_id = req.get('id', 'UNKNOWN-ID')
            group = req_groups.get(req_id, 'Uncategorized')
            grouped_requirements[group].append(req)
            
        # Log the grouping results
        print(f"\nRequirements organized into {len(grouped_requirements)} groups:")
        for group, reqs in grouped_requirements.items():
            print(f"  • {group}: {len(reqs)} requirements")
        
        # Generate test plan file
        #test_plan_path = output_dir / f"{api_type}_test_plan_{timestamp}.md"
        test_plan_path = output_dir / "test_plan.md"
        
        print(f"\nGenerating test specifications...")
        
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
        
        total_reqs = sum(len(reqs) for reqs in grouped_requirements.values())
        processed_count = 0
        
        for group in sorted(grouped_requirements.keys()):
            # Add group header with anchor for TOC linking
            test_plan += f"<a id='{group.lower().replace(' ', '-')}'></a>\n\n"
            test_plan += f"## {group}\n\n"
            
            print(f"\n[{group}] Processing {len(grouped_requirements[group])} requirements...")
            
            # Process each requirement in the group
            for req in grouped_requirements[group]:
                processed_count += 1
                req_id = req.get('id', 'UNKNOWN-ID')
                
                print(f"  [{processed_count}/{total_reqs}] {req_id}", end='\r')
                
                test_spec = generate_test_specification_with_capability(
                    api_type, client_instance, req, capability_collection, verbose=verbose
                )
                
                # Add to test plan content with proper anchor for TOC linking
                test_plan += f"<a id='{req_id.lower()}'></a>\n\n"
                test_plan += f"### {req_id}: {req['parsed'].get('summary', 'No summary')}\n\n"
                test_plan += f"**Text**: {req['parsed'].get('text', '')}\n\n"
                test_plan += f"**Context**: {req['parsed'].get('context', '')}\n\n"
                test_plan += f"**Actor**: {req['parsed'].get('actor', '')}\n\n"
                test_plan += f"**Conformance**: {req['parsed'].get('conformance', '')}\n\n"
                test_plan += f"{test_spec}\n\n"
                test_plan += "---\n\n"
                
                # Add delay between requests
                time.sleep(client_instance.config[api_type]["delay_between_chunks"])
            
            print(f"  Completed {len(grouped_requirements[group])} requirements                    ")
            test_plan += "\n\n"
        
        # Save consolidated test plan
        with open(test_plan_path, 'w', encoding='utf-8') as f:
            f.write(test_plan)
        
        print(f"\n{'='*80}")
        print("TEST PLAN GENERATION COMPLETE!")
        print(f"Output file: {test_plan_path}")
        print(f"Total requirements: {len(requirements)}")
        print(f"Requirement groups: {len(grouped_requirements)}")
        print(f"{'='*80}")
        
        logging.info(f"Consolidated test plan saved to {test_plan_path}")
        
        return {
            "requirements_count": len(requirements),
            "group_count": len(grouped_requirements),
            "test_plan_path": str(test_plan_path)
        }
        
    except Exception as e:
        logging.error(f"Error processing requirements: {str(e)}")
        print(f"\nError occurred during test plan generation: {str(e)}")
        raise


def clear_capability_collection(collection_name: str = "capability_statements") -> None:
    """
    Delete the existing ChromaDB collection so it can be recreated with new chunking.
    
    Args:
        collection_name: Name of the collection to delete
        
    Note:
        Useful when you want to recreate the collection with different chunking strategy
    """
    chroma_client = chromadb.Client()
    
    try:
        # Check if collection exists and delete it
        existing_collections = [c.name for c in chroma_client.list_collections()]
        if collection_name in existing_collections:
            chroma_client.delete_collection(collection_name)
            print(f"Deleted existing collection: {collection_name}")
            logging.info(f"Cleared ChromaDB collection: {collection_name}")
        else:
            print(f"No existing collection found: {collection_name}")
    except Exception as e:
        logging.error(f"Error clearing collection: {e}")
        print(f"Error clearing collection: {e}")