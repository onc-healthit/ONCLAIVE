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

from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a specialized FHIR testing engineer with expertise in healthcare interoperability.
Your task is to analyze FHIR Implementation Guide requirements and generate practical, implementable test specifications."""


class SimpleFHIRRAG:
    """
    Simple RAG system for FHIR capability statements using sentence transformers
    No external dependencies like ChromaDB - just embeddings and cosine similarity
    """
    
    def __init__(self):
        # Use a lightweight, fast model that works well for technical text
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.documents = []
        self.embeddings = None
        
    def chunk_capability_statement(self, capability_statement_file: str) -> List[str]:
        """
        Read and chunk the capability statement markdown file into searchable pieces
        """
        with open(capability_statement_file, 'r') as f:
            content = f.read()
        
        chunks = []
        
        # Split by major sections and create contextual chunks
        sections = content.split('\n---\n')
        
        for section in sections:
            if not section.strip():
                continue
                
            # Extract resource name if this is a resource section
            resource_match = re.search(r'#### ([A-Za-z]+)', section)
            resource_name = resource_match.group(1) if resource_match else "General"
            
            # Split section into logical chunks
            paragraphs = section.split('\n\n')
            
            for paragraph in paragraphs:
                if len(paragraph.strip()) < 50:  # Skip very short chunks
                    continue
                    
                # Clean up the paragraph
                clean_paragraph = re.sub(r'\n\s*\n', ' ', paragraph)
                clean_paragraph = re.sub(r'\s+', ' ', clean_paragraph).strip()
                
                # Add context prefix for better retrieval
                if resource_name != "General":
                    contextual_chunk = f"FHIR {resource_name} Resource: {clean_paragraph}"
                else:
                    contextual_chunk = f"FHIR General Capability: {clean_paragraph}"
                
                chunks.append(contextual_chunk)
        
        # Add some FHIR-specific context chunks to help with semantic matching
        fhir_context = [
            "FHIR Must Support: Must Support data elements are required to be populated in profiles and indicated via meta.profile",
            "FHIR JSON Format: JSON format support is required for all FHIR REST API interactions and content negotiation",
            "FHIR Client Requirements: Client applications must process resources without errors and handle missing data indicators",
            "FHIR Security Privacy: Applications should not send PII and servers must implement proper authorization controls",
            "FHIR Profile Conformance: Resources must declare conformance to profiles via meta.profile element"
        ]
        
        chunks.extend(fhir_context)
        return chunks
    
    def create_embeddings(self, capability_statement_file: str):
        """
        Create embeddings for all capability statement chunks
        """
        logger.info("Creating RAG embeddings for capability statement...")
        
        # Chunk the capability statement
        self.documents = self.chunk_capability_statement(capability_statement_file)
        
        # Create embeddings
        self.embeddings = self.model.encode(self.documents)
        
        logger.info(f"Created embeddings for {len(self.documents)} capability chunks")
        
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("Sample chunks:")
            for i, chunk in enumerate(self.documents[:3]):
                logger.debug(f"  {i}: {chunk[:100]}...")
    
    def retrieve_relevant_info(self, requirement: Dict[str, str], top_k: int = 5, verbose: bool = False) -> str:
        """
        Retrieve most relevant capability information for a requirement
        """
        if self.embeddings is None:
            return "No capability statement information available."
        
        # Create query from requirement
        query_parts = [
            requirement.get('summary', ''),
            requirement.get('description', ''),
            requirement.get('actor', ''),
            f"FHIR {requirement.get('conformance', '')}"
        ]
        query = " ".join(filter(None, query_parts))
        
        # Get query embedding
        query_embedding = self.model.encode([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Get top-k most similar chunks
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        if verbose:
            req_id = requirement.get('id', 'UNKNOWN-ID')
            print(f"\n{'='*60}")
            print(f"RAG RETRIEVAL FOR {req_id}")
            print(f"{'='*60}")
            print(f"Query: {query[:100]}...")
            print(f"Retrieved {top_k} most relevant capability chunks:")
        
        # Format results
        result = "### Relevant Capability Statement Information (RAG Retrieved)\n\n"
        
        for i, idx in enumerate(top_indices):
            chunk = self.documents[idx]
            similarity_score = similarities[idx]
            
            # Only include chunks with reasonable similarity
            if similarity_score > 0.1:  # Threshold to filter noise
                result += f"**Relevant Capability {i+1}** (similarity: {similarity_score:.3f}):\n"
                result += f"{chunk}\n\n"
                
                if verbose:
                    print(f"  {i+1}. (score: {similarity_score:.3f}) {chunk[:80]}...")
        
        if verbose:
            print(f"{'='*60}\n")
        
        return result
    

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


def generate_test_specification_with_capability_rag(
    logger,
    api_type: str,
    llm_clients,
    requirement: Dict[str, str],
    rag_system: SimpleFHIRRAG,
    verbose: bool = False
) -> str:
    """
    Generate a comprehensive test specification using RAG-retrieved capability info
    """
    req_id = requirement.get('id', 'unknown')
    req_parsed = requirement.get('parsed', {})
    logger.info(f"Generating test specification for {req_id} using {api_type}...")
    
    if verbose:
        print(f"\nProcessing {req_id}: {req_parsed.get('summary', 'No summary')}")
    
    # Format requirement as markdown
    formatted_req = format_requirement_for_prompt(req_parsed)
    
    # Extract relevant capability information using RAG
    capability_info = rag_system.retrieve_relevant_info(req_parsed, verbose=verbose)
    
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
    Process requirements and generate a consolidated test plan using RAG
    
    Args:
        llm_clients: LLM client configuration
        api_type: API type (claude, gemini, gpt)
        logger: Logger instance
        requirements_file: Path to requirements markdown file
        capability_statement_file: Path to capability statement markdown file (optional)
        ig_name: Name of the Implementation Guide
        output_dir: Directory for output files
        verbose: Whether to show detailed capability extraction information
        
    Returns:
        Dictionary containing path to output file
    """
    # Use default output directory if none provided
    if output_dir is None:
        output_dir = DEFAULT_OUTPUT_DIR
    else:
        # Ensure output_dir is a Path object
        if not isinstance(output_dir, Path):
            output_dir = Path(output_dir)
    
    logger.info(f"Starting test plan generation with {api_type} for {ig_name}")

    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        # Parse requirements from file
        requirements = load_requirements(requirements_file)
        logger.info(f"Parsed {len(requirements)} requirements from {requirements_file}")
        
        # Initialize RAG system instead of parsing capability statement dictionary
        rag_system = SimpleFHIRRAG()
        rag_system.create_embeddings(capability_statement_file)
        logger.info(f"Initialized RAG system with capability statement from {capability_statement_file}")
        
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
                
                test_spec = generate_test_specification_with_capability_rag(
                    logger, api_type, llm_clients, req, rag_system, verbose=verbose
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
