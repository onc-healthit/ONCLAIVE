#import packages
import os
import logging
from typing import List, Dict, Union, Optional, Any
import time
from datetime import datetime
import re
import pandas as pd
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from anthropic import Anthropic, RateLimitError
import google.generativeai as gemini
from openai import OpenAI
from pathlib import Path
import prompt_utils
from llm_utils import SafetyFilterException

# Get the current working directory and set up paths
PROJECT_ROOT = Path.cwd().parent  # Go up one level from reqs_extraction to onclaive root

SYSTEM_PROMPTS = {
    "claude": """You are a seasoned Healthcare Integration Test Engineer with expertise in INCOSE Systems Engineering standards, 
    analyzing a FHIR Implementation Guide to extract precise testable requirements in INCOSE format.""",
    "gemini": """You are a Healthcare Integration Test Engineer with expertise in INCOSE Systems Engineering standards, analyzing FHIR 
    Implementation Guide content to identify and format testable requirements following INCOSE specifications.""",
    "gpt": """As a Healthcare Integration Test Engineer with INCOSE Systems Engineering expertise, analyze this FHIR 
    Implementation Guide content to extract specific testable requirements in INCOSE-compliant format.""",
    "aip": """As a Healthcare Integration Test Engineer with INCOSE Systems Engineering expertise, analyze this FHIR 
    Implementation Guide content to extract specific testable requirements in INCOSE-compliant format."""
}

# Basic setup
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))

# Setup the prompt environment
prompt_env = prompt_utils.setup_prompt_environment(PROJECT_ROOT)
PROMPT_DIR = prompt_env["prompt_dir"]
REQUIREMENTS_EXTRACTION_PATH = prompt_env["requirements_extraction_path"]

# Setup logging
logging.basicConfig(level=logging.INFO)


def list_markdown_files(markdown_dir: str, verbose: bool = False) -> List[str]:
    """
    List all markdown files in a directory.
    
    Args:
        markdown_dir: Path to directory containing markdown files
        verbose: If True, log each filename found
        
    Returns:
        List of markdown filenames
        
    Raises:
        FileNotFoundError: If directory doesn't exist
    """
    if not os.path.exists(markdown_dir):
        raise FileNotFoundError(f"Directory does not exist: {markdown_dir}")
    
    files = [f for f in os.listdir(markdown_dir) if f.endswith('.md')]
    logging.info(f"Found {len(files)} markdown files")
    if verbose:
        for file in files:
            logging.info(f"  - {file}")
    return files


def calculate_optimal_chunk_size(config: Dict, api_type: str, markdown_content: str) -> int:
    """
    Calculate the optimal chunk size based on API type and content characteristics.
    
    Args:
        config: Configuration dictionary for the API
        api_type: Type of API ('claude', 'gemini', 'gpt', 'aip')
        markdown_content: The content to be chunked
        
    Returns:
        Optimal chunk size in characters
    """
    # Base chunk sizes based on API token limits
    base_chunk_sizes = {
        "claude": 25000,  # Claude has higher token limits
        "gemini": 20000,  # Gemini is also capable of handling larger chunks
        "gpt": 12000,     # GPT-4 with smaller context
        "aip": 8000
    }
    
    # Start with the base size for the API
    optimal_size = base_chunk_sizes[api_type]
    
    # For small content, don't chunk at all
    content_length = len(markdown_content)
    if content_length <= optimal_size:
        return content_length
    
    return optimal_size


def clean_markdown(text: str) -> str:
    """
    Clean markdown content by removing excessive whitespace, comments, and formatting artifacts.
    
    Args:
        text: Raw markdown text to clean
        
    Returns:
        Cleaned markdown text
    """
    text = re.sub(r'\n\s*\n', '\n\n', text)  # Normalize multiple newlines
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)  # Remove HTML comments
    text = re.sub(r'\.{2,}', '.', text)  # Replace multiple dots with single
    text = re.sub(r'\\(.)', r'\1', text)  # Remove escape characters
    text = re.sub(r'\|', ' ', text)  # Replace pipes with spaces
    text = re.sub(r'[-\s]*\n[-\s]*', '\n', text)  # Clean up dashes and whitespace
    return text.strip()


def split_markdown_dynamic(config: Dict, content: str, api_type: str) -> List[str]:
    """
    Split markdown content into optimal chunks for API processing.
    
    Args:
        config: Configuration dictionary for the API
        content: Markdown content to split
        api_type: Type of API being used
        
    Returns:
        List of content chunks
    """
    # Don't split small files at all
    if len(content) < 5000:
        return [content]
    
    max_size = calculate_optimal_chunk_size(config, api_type, content)
    
    # Try to split on major sections first (headers)
    sections = re.split(r'\n(?=# )', content)
    
    chunks = []
    current_chunk = ""
    
    for section in sections:
        if len(current_chunk) + len(section) <= max_size:
            current_chunk += section + "\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = section + "\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks if len(chunks) > 1 else [content]


def should_combine_files(config: Dict, files: List[str], markdown_dir: str, api_type: str) -> List[List[str]]:
    """
    Determine if small files should be combined for more efficient processing.
    
    Args:
        config: Configuration dictionary for the API
        files: List of markdown filenames
        markdown_dir: Directory containing the files
        api_type: Type of API being used
        
    Returns:
        List of file groups, where each group should be processed together
    """
    file_sizes = {}
    
    # Get the size of each file
    for file in files:
        file_path = os.path.join(markdown_dir, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            file_sizes[file] = len(content)
    
    # Estimate the optimal size based on API
    optimal_sizes = {
        "claude": 12000,
        "gemini": 10000,
        "gpt": 6000,
        "aip": 6000,
    }
    
    optimal_size = optimal_sizes[api_type]
    combined_files = []
    current_group = []
    current_size = 0
    
    # Sort files by size (ascending) to try combining smaller files first
    sorted_files = sorted(files, key=lambda f: file_sizes[f])
    
    for file in sorted_files:
        size = file_sizes[file]
        
        # If this file is already big, process it individually
        if size > optimal_size * 0.8:
            if current_group:
                combined_files.append(current_group)
                current_group = []
                current_size = 0
            combined_files.append([file])
            continue
        
        # If adding this file would exceed optimal size, start a new group
        if current_size + size > optimal_size:
            if current_group:
                combined_files.append(current_group)
            current_group = [file]
            current_size = size
        else:
            current_group.append(file)
            current_size += size
    
    # Add the last group if there's anything left
    if current_group:
        combined_files.append(current_group)
    
    return combined_files


def create_incose_requirements_extraction_prompt(content: str, chunk_index: int, total_chunks: int) -> str:
    """
    Create a prompt for extracting requirements in INCOSE format using external prompt file.
    
    Args:
        content: The content to analyze
        chunk_index: Index of this chunk in the total content (1-based)
        total_chunks: Total number of chunks being processed
        
    Returns:
        The formatted prompt for the LLM
    """
    prompt = prompt_utils.load_prompt(
        REQUIREMENTS_EXTRACTION_PATH,
        FHIR_TEXT=content,
        chunk_index=chunk_index,
        total_chunks=total_chunks
    )
    
    return prompt


def format_content_for_api(content: str, api_type: str, chunk_index: int, total_chunks: int) -> Union[str, List[dict], dict]:
    """
    Format content appropriately for each API's expected input format.
    
    Args:
        content: The content to format
        api_type: Type of API ('claude', 'gemini', 'gpt', 'aip')
        chunk_index: Index of this chunk
        total_chunks: Total number of chunks
        
    Returns:
        Formatted content ready for API consumption
    """
    base_prompt = create_incose_requirements_extraction_prompt(content, chunk_index, total_chunks)
    
    if api_type == "claude":
        return [{
            "type": "text",
            "text": base_prompt
        }]
    elif api_type == "gemini":
        return [{  
            "parts": [{
                "text": base_prompt
            }]
        }]
    return base_prompt


def process_markdown_content_for_incose_srs(
    client_instance, 
    api_type: str, 
    markdown_dir: str, 
    output_dir: str = None, 
    max_files: int = None
) -> Dict[str, Any]:
    """
    Process markdown content and generate document directly from LLM outputs.
    
    Args:
        client_instance: LLM client manager object
        api_type: The API to use for processing ('claude', 'gemini', 'gpt', 'aip')
        markdown_dir: Directory containing markdown files
        output_directory: Directory to save output files (optional, uses default if None)
        max_files: Maximum number of files to process (optional, processes all if None)
        
    Returns:
        Dictionary containing:
            - processed_files: List of files that were processed
            - srs_document: The complete INCOSE SRS document text
            - output_file: Path to the saved output file
            
    Raises:
        FileNotFoundError: If markdown directory doesn't exist
        Exception: For various processing errors
    """
    logging.info(f"Starting processing with {api_type} on directory: {markdown_dir}")
    config = client_instance.config[api_type]
    
    # Use default output directory if none provided
    if output_dir is None:
        output_dir = os.path.join(PROJECT_ROOT, 'reqs_extraction', 'initial_reqs_output')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # List files before processing
    markdown_files = list_markdown_files(markdown_dir)
    if not markdown_files:
        logging.error("No markdown files found to process")
        return {"processed_files": [], "srs_document": "", "output_file": None}
    
    try:
        all_requirements = []
        processed_files = []
        
        # Group files for potential combination
        file_groups = should_combine_files(config, markdown_files[:max_files], markdown_dir, api_type)
        logging.info(f"Organized {len(markdown_files)} files into {len(file_groups)} processing groups")
        
        for group_idx, group in enumerate(file_groups, 1):
            # Process single file
            if len(group) == 1:
                file_path = os.path.join(markdown_dir, group[0])
                print(f"\n[{group_idx}/{len(file_groups)}] Processing single file: {group[0]}")
                logging.info(f"Processing single file: {group[0]}")
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = clean_markdown(f.read())
                
                chunks = split_markdown_dynamic(config, content, api_type)
                logging.info(f"Split {group[0]} into {len(chunks)} chunks using dynamic sizing")
                
                for chunk_idx, chunk in enumerate(chunks, 1):
                    print(f"    Processing chunk {chunk_idx}/{len(chunks)}", end='\r')
                    logging.info(f"Processing chunk {chunk_idx}/{len(chunks)} of {group[0]}")
                    
                    formatted_content = format_content_for_api(chunk, api_type, chunk_idx, len(chunks))
                    
                    # Extract proper text based on API type
                    if api_type == "claude":
                        prompt_text = formatted_content[0]["text"]
                    elif api_type == "gemini":
                        prompt_text = formatted_content[0]["parts"][0]["text"]
                    else:
                        prompt_text = formatted_content
                    
                    try:
                        response = client_instance.make_llm_request(api_type, prompt_text, sys_prompt=SYSTEM_PROMPTS[api_type])
                        all_requirements.append(response)
                    except SafetyFilterException as e:
                        client_instance.safety_blocked_count += 1
                        print(f"\nSAFETY FILTER BLOCKED CONTENT #{client_instance.safety_blocked_count}")
                        print(f"File: {group[0]} - Chunk {chunk_idx}/{len(chunks)}")
                        print("=" * 60)
                        print("BLOCKED CONTENT SAMPLE:")
                        print(e.blocked_content)
                        print("=" * 60)
                        print("Skipping this chunk and continuing...\n")
                        all_requirements.append("## CHUNK SKIPPED DUE TO SAFETY FILTER\n[Content blocked by safety filters]\n\n")
                    
                    time.sleep(config["delay_between_chunks"])
                
                print(f"    Completed {len(chunks)} chunks                    ")
                processed_files.append(group[0])
                
            # Process multiple combined files
            else:
                print(f"\n[{group_idx}/{len(file_groups)}] Processing combined group of {len(group)} files: {', '.join(group[:3])}{'...' if len(group) > 3 else ''}")
                logging.info(f"Processing combined group of {len(group)} files")
                combined_content = []
                
                # Prepare combined content with clear file boundaries
                for file in group:
                    file_path = os.path.join(markdown_dir, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = clean_markdown(f.read())
                        combined_content.append(f"## FILE: {file}\n\n{file_content}\n\n")
                
                combined_text = "".join(combined_content)
                chunks = split_markdown_dynamic(config, combined_text, api_type)
                logging.info(f"Split combined content into {len(chunks)} chunks")
                
                for chunk_idx, chunk in enumerate(chunks, 1):
                    print(f"    Processing chunk {chunk_idx}/{len(chunks)}", end='\r')
                    logging.info(f"Processing chunk {chunk_idx}/{len(chunks)} of combined files")
                    
                    formatted_content = format_content_for_api(chunk, api_type, chunk_idx, len(chunks))
                    
                    # Extract proper text based on API type
                    if api_type == "claude":
                        prompt_text = formatted_content[0]["text"]
                    elif api_type == "gemini":
                        prompt_text = formatted_content[0]["parts"][0]["text"]
                    else:
                        prompt_text = formatted_content
                    
                    try:
                        response = client_instance.make_llm_request(api_type, prompt_text, SYSTEM_PROMPTS[api_type])
                        all_requirements.append(response)
                    except SafetyFilterException as e:
                        client_instance.safety_blocked_count += 1
                        print(f"\nSAFETY FILTER BLOCKED CONTENT #{client_instance.safety_blocked_count}")
                        print(f"Combined files: {', '.join(group)} - Chunk {chunk_idx}/{len(chunks)}")
                        print("=" * 60)
                        print("BLOCKED CONTENT SAMPLE:")
                        print(e.blocked_content)
                        print("=" * 60)
                        print("Skipping this chunk and continuing...\n")
                        all_requirements.append("## CHUNK SKIPPED DUE TO SAFETY FILTER\n[Content blocked by safety filters]\n\n")
                    
                    time.sleep(config["delay_between_chunks"])
                
                print(f"    Completed {len(chunks)} chunks                    ")
                processed_files.extend(group)
            
            # Add delay between file groups
            time.sleep(config["delay_between_batches"])
        
        # Combine all requirements into single list
        reqs_document = ""
        for req_section in all_requirements:
            # Skip the intro text if it's present to avoid duplication
            if "## REQ-" in req_section:
                # Find the index of the first requirement
                req_start_idx = req_section.find("## REQ-")
                if req_start_idx > 0:
                    # Only add the requirements part, not any introductory text
                    reqs_document += req_section[req_start_idx:]
                else:
                    reqs_document += req_section
            else:
                # Add any content that doesn't contain requirements
                reqs_document += req_section
        
        # Save requirements list to markdown file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        #output_file = os.path.join(output_dir, f"{api_type}_reqs_list_v1_{timestamp}.md")
        output_file = os.path.join(output_dir, "reqs_list_v1.md")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(reqs_document)
        
        logging.info(f"Completed processing {len(processed_files)} files")
        logging.info(f"Generated requirements document saved to {output_file}")
        
        return {
            "processed_files": processed_files,
            "srs_document": reqs_document,
            "output_file": output_file
        }
        
    except Exception as e:
        logging.error(f"Error processing content: {str(e)}")
        raise


def run_requirements_extractor(
    markdown_dir: str, 
    output_dir: str, 
    api_type: str, 
    client_instance, 
    max_files: int = None
) -> None:
    """
    Main function to run the requirements extraction process.
    
    This function handles the complete workflow of processing FHIR Implementation Guide
    markdown files and generating INCOSE-formatted requirements documents.
    
    Args:
        markdown_dir: Path to directory containing markdown files to process
        output_dir: Path to directory where output files should be saved
        api_type: Type of LLM API to use ('claude', 'gemini', 'gpt', 'aip')
        client_instance: LLM client manager object with configured API clients
        max_files: Maximum number of files to process (optional, processes all if None)
        
    Raises:
        FileNotFoundError: If markdown directory doesn't exist
        Exception: For various processing errors
        
    Example:
        >>> run_requirements_extractor(
        ...     'input/markdown_files',
        ...     'output/requirements', 
        ...     'claude',
        ...     llm_clients,
        ...     max_files=10
        ... )
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Verify the markdown directory exists
    if not os.path.exists(markdown_dir):
        raise FileNotFoundError(f"Markdown directory not found at {markdown_dir}")
    
    logging.info(f"Found markdown directory at {markdown_dir}")
    markdown_files = [f for f in os.listdir(markdown_dir) if f.endswith('.md')]
    logging.info(f"Found {len(markdown_files)} markdown files")

    # Initialize safety filter counter
    client_instance.safety_blocked_count = 0

    logging.info(f"Processing with {api_type}...")
    print(f"\nProcessing Implementation Guide with {api_type.capitalize()}...")
    print("This may take several minutes depending on the size of the Implementation Guide.")
    
    # Process the markdown files and generate direct INCOSE SRS document
    api_results = process_markdown_content_for_incose_srs(
        client_instance=client_instance,
        api_type=api_type, 
        markdown_dir=markdown_dir,
        output_dir=output_dir,
        max_files=max_files
    )
    
    # Output the results to the user
    print("\n" + "="*80)
    print("Processing complete!")
    print(f"Generated requirements document: {api_results['output_file']}")
    print(f"Processed {len(api_results['processed_files'])} files")
    if hasattr(client_instance, 'safety_blocked_count') and client_instance.safety_blocked_count > 0:
        print(f"Safety filter blocked {client_instance.safety_blocked_count} chunks")
    print("="*80)