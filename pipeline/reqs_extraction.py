#import packages
import os
import logging
from typing import List, Dict, Union, Optional, Any
import time
import json
from datetime import datetime
import re
import pandas as pd
from dotenv import load_dotenv
import httpx
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from anthropic import Anthropic, RateLimitError
import google.generativeai as gemini
from openai import OpenAI
from pathlib import Path
import sys
import prompt_utils

# Get the current working directory and set up paths
PROJECT_ROOT = Path.cwd().parent  # Go up one level from reqs_extraction to onclaive root
#DEFAULT_MARKDOWN_DIR = os.path.join(PROJECT_ROOT, 'full-ig', 'markdown7_cleaned')
#DEFAULT_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'reqs_extraction', 'initial_reqs_output')

SYSTEM_PROMPTS = {
    "claude": """You are a seasoned Healthcare Integration Test Engineer with expertise in INCOSE Systems Engineering standards, 
    analyzing a FHIR Implementation Guide to extract precise testable requirements in INCOSE format.""",
    "gemini": """You are a Healthcare Integration Test Engineer with expertise in INCOSE Systems Engineering standards, analyzing FHIR 
    Implementation Guide content to identify and format testable requirements following INCOSE specifications.""",
    "gpt": """As a Healthcare Integration Test Engineer with INCOSE Systems Engineering expertise, analyze this FHIR 
    Implementation Guide content to extract specific testable requirements in INCOSE-compliant format."""
}

# Add debug logging
logging.basicConfig(level=logging.INFO)
logging.info(f"Current working directory: {Path.cwd()}")
logging.info(f"Project root: {PROJECT_ROOT}")
#logging.info(f"Default markdown directory: {DEFAULT_MARKDOWN_DIR}")
#logging.info(f"Default output directory: {DEFAULT_OUTPUT_DIR}")

# Basic setup
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))

# Import prompt utilities
prompt_utils_path = os.path.join(PROJECT_ROOT, 'prompt_utils.py')
    
# Setup the prompt environment
prompt_env = prompt_utils.setup_prompt_environment(PROJECT_ROOT)
PROMPT_DIR = prompt_env["prompt_dir"]
REQUIREMENTS_EXTRACTION_PATH = prompt_env["requirements_extraction_path"]

logging.info(f"Using prompts directory: {PROMPT_DIR}")
logging.info(f"Requirements extraction prompt: {REQUIREMENTS_EXTRACTION_PATH}")

def list_markdown_files(markdown_dir):
    """Debug function to list all markdown files"""
    if not os.path.exists(markdown_dir):
        logging.error(f"Directory does not exist: {markdown_dir}")
        return
    
    files = [f for f in os.listdir(markdown_dir) if f.endswith('.md')]
    logging.info(f"Found {len(files)} markdown files:")
    for file in files:
        logging.info(f"  - {file}")
    return files

def calculate_optimal_chunk_size(config, api_type: str, markdown_content: str) -> int:
    """
    Calculate the optimal chunk size based on API type and content characteristics.
    """
    
    # Base chunk sizes based on API token limits
    base_chunk_sizes = {
        "claude": 8000,  # Claude has higher token limits
        "gemini": 7000,  # Gemini is also capable of handling larger chunks
        "gpt": 3000      # GPT-4 with smaller context
    }
    
    # Start with the base size for the API
    optimal_size = base_chunk_sizes[api_type]
    
    # Adjust based on content characteristics
    content_length = len(markdown_content)
    
    # For very small content, don't chunk at all
    if content_length <= optimal_size / 2:
        return content_length
    
    # For medium content, use the base size
    if content_length <= optimal_size * 1.5:
        return optimal_size
    
    # For larger content, adjust based on complexity 
    code_blocks = markdown_content.count("```")
    tables = markdown_content.count("|")
    
    # Adjust down if content has complex structures
    complexity_factor = 1.0
    if code_blocks > 5:
        complexity_factor *= 0.9
    if tables > 10:
        complexity_factor *= 0.9
    
    # Avoid exceeding API token limits
    return min(int(optimal_size * complexity_factor), base_chunk_sizes[api_type])

# Markdown Processing Functions
def clean_markdown(text: str) -> str:
    """Clean markdown content"""
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'\.{2,}', '.', text)
    text = re.sub(r'\\(.)', r'\1', text)
    text = re.sub(r'\|', ' ', text)
    text = re.sub(r'[-\s]*\n[-\s]*', '\n', text)
    return text.strip()

def split_markdown_dynamic(config, content: str, api_type: str) -> List[str]:
    """
    Split markdown into dynamically sized chunks based on API type and content.
    """
    # If content is very small, don't split it
    if len(content) < 1000:
        return [content]
    
    # Calculate optimal chunk size
    max_size = calculate_optimal_chunk_size(config, api_type, content)
    
    chunks = []
    lines = content.split('\n')
    current_chunk = []
    current_size = 0
    
    # Try to split at meaningful boundaries like headers or blank lines
    for i, line in enumerate(lines):
        line_size = len(line)
        
        if current_size + line_size > max_size:
            # Look back for a good splitting point (blank line or header)
            split_index = find_good_split_point(current_chunk)
            
            if split_index > 0:
                # Split at the good point
                first_part = current_chunk[:split_index]
                second_part = current_chunk[split_index:]
                chunks.append('\n'.join(first_part))
                current_chunk = second_part
                current_size = sum(len(l) for l in second_part)
            else:
                # If no good splitting point, use the current chunk
                chunks.append('\n'.join(current_chunk))
                current_chunk = []
                current_size = 0
            
            # Add the current line to the new chunk
            current_chunk.append(line)
            current_size += line_size
        else:
            current_chunk.append(line)
            current_size += line_size
    
    # Add the last chunk if there's anything left
    if current_chunk:
        chunks.append('\n'.join(current_chunk))
    
    return chunks

def find_good_split_point(lines: List[str]) -> int:
    """
    Find a good place to split a chunk, preferring blank lines or headers.
    """
    # Go backwards from the end to find a natural splitting point
    for i in range(len(lines) - 1, 0, -1):
        # Prefer blank lines
        if lines[i].strip() == '':
            return i + 1
        
        # Or headers
        if lines[i].startswith('#') or lines[i].startswith('==') or lines[i].startswith('--'):
            return i
    
    # If we're more than halfway through, just use the current point
    return len(lines) // 2

def should_combine_files(config, files: List[str], markdown_dir: str, api_type: str) -> List[List[str]]:
    """
    Determine if small files should be combined for processing.
    """
    file_sizes = {}
    
    # Get the size of each file
    for file in files:
        file_path = os.path.join(markdown_dir, file)
        with open(file_path, 'r') as f:
            content = f.read()
            file_sizes[file] = len(content)
    
    # Estimate the optimal size based on API
    optimal_sizes = {
        "claude": 12000,
        "gemini": 10000,
        "gpt": 6000
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
    Create a prompt for extracting requirements in INCOSE format using external prompt file
    
    Args:
        content: The content to analyze
        chunk_index: Index of this chunk in the total content
        total_chunks: Total number of chunks being processed
        
    Returns:
        str: The prompt for the LLM loaded from external file
    """
    return prompt_utils.load_prompt(
        REQUIREMENTS_EXTRACTION_PATH,
        content=content,
        chunk_index=chunk_index,
        total_chunks=total_chunks
    )

def format_content_for_api(content: Union[str, dict, list], api_type: str, chunk_index: int, total_chunks: int) -> Union[str, List[dict], dict]:
    """Format content appropriately for each API"""
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

def process_markdown_content_for_incose_srs(clients, api_type: str, markdown_dir: str, 
                                           output_directory: str = None) -> Dict[str, Any]:
    """
    Process markdown content and generate INCOSE SRS document directly from LLM outputs.
    
    Args:
        api_type: The API to use for processing
        markdown_dir: Directory containing markdown files
        output_directory: Directory to save output files (optional)
        
    Returns:
        Dict containing processing results and SRS document
    """
    logging.info(f"Starting processing with {api_type} on directory: {markdown_dir}")
    config = clients.config[api_type]
    # Use default output directory if none provided
    if output_directory is None:
        output_directory = os.path.join(PROJECT_ROOT, 'reqs_extraction', 'initial_reqs_output')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # List files before processing
    markdown_files = list_markdown_files(markdown_dir)
    if not markdown_files:
        logging.error("No markdown files found to process")
        return {"processed_files": [], "srs_document": "", "output_file": None}
    
    try:
        all_incose_requirements = []
        processed_files = []
        
        # Group files for potential combination
        file_groups = should_combine_files(config, markdown_files, markdown_dir, api_type)
        logging.info(f"Organized {len(markdown_files)} files into {len(file_groups)} processing groups")
        
        for group in file_groups:
            # For a single file
            if len(group) == 1:
                file_path = os.path.join(markdown_dir, group[0])
                logging.info(f"Processing single file: {group[0]}")
                
                with open(file_path, 'r') as f:
                    content = clean_markdown(f.read())
                
                # Use dynamic chunk sizing
                chunks = split_markdown_dynamic(config, content, api_type)
                logging.info(f"Split {group[0]} into {len(chunks)} chunks using dynamic sizing")
                
                for chunk_idx, chunk in enumerate(chunks, 1):
                    logging.info(f"Processing chunk {chunk_idx}/{len(chunks)} of {group[0]}")
                    
                    # Format the content for the API
                    formatted_content = format_content_for_api(content, api_type, chunk_idx, len(chunks))
                    
                    # Extract proper text based on API type
                    if api_type == "claude":
                        prompt_text = formatted_content[0]["text"]
                    elif api_type == "gemini":
                        prompt_text = formatted_content[0]["parts"][0]["text"]
                    else:
                        prompt_text = formatted_content
                    
                    # Use the utility function for API request
                    response = clients.make_llm_request(api_type, prompt_text, sys_prompt=SYSTEM_PROMPTS[api_type])
                    
                    all_incose_requirements.append(response)
                    time.sleep(config["delay_between_chunks"])
                
                processed_files.append(group[0])
                
            # For multiple combined files
            else:
                logging.info(f"Processing combined group of {len(group)} files")
                combined_content = []
                
                # Prepare combined content with clear file boundaries
                for file in group:
                    file_path = os.path.join(markdown_dir, file)
                    with open(file_path, 'r') as f:
                        file_content = clean_markdown(f.read())
                        combined_content.append(f"## FILE: {file}\n\n{file_content}\n\n")
                
                combined_text = "".join(combined_content)
                chunks = split_markdown_dynamic(config, combined_text, api_type)
                logging.info(f"Split combined content into {len(chunks)} chunks")
                
                for chunk_idx, chunk in enumerate(chunks, 1):
                    logging.info(f"Processing chunk {chunk_idx}/{len(chunks)} of combined files")
                    
                    # Format the content for the API
                    formatted_content = format_content_for_api(chunk, api_type, chunk_idx, len(chunks))
                    
                    # Extract proper text based on API type
                    if api_type == "claude":
                        prompt_text = formatted_content[0]["text"]
                    elif api_type == "gemini":
                        prompt_text = formatted_content[0]["parts"][0]["text"]
                    else:
                        prompt_text = formatted_content
                    
                    # Use the utility function for API request
                    response = clients.make_llm_request(api_type, prompt_text, SYSTEM_PROMPTS[api_type])
                    
                    all_incose_requirements.append(response)
                    time.sleep(config["delay_between_chunks"])
                
                processed_files.extend(group)
            
            # Add delay between file groups
            time.sleep(config["delay_between_batches"])
        
        # Combine all requirements into a full INCOSE SRS document
        srs_document = ""
        for req_section in all_incose_requirements:
            # Skip the intro text if it's present to avoid duplication
            # Look for the first requirement section
            if "## REQ-" in req_section:
                # Find the index of the first requirement
                req_start_idx = req_section.find("## REQ-")
                if req_start_idx > 0:
                    # Only add the requirements part, not any introductory text
                    srs_document += req_section[req_start_idx:]
                else:
                    srs_document += req_section
            else:
                # Add any content that doesn't contain requirements
                # (this could be informational text related to requirements)
                srs_document += req_section
        
        # Save INCOSE SRS document to markdown file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        srs_output_file = os.path.join(output_directory, f"{api_type}_reqs_list_v1_{timestamp}.md")
        
        with open(srs_output_file, 'w') as f:
            f.write(srs_document)
        
        logging.info(f"Completed processing {len(processed_files)} files")
        logging.info(f"Generated requirements document saved to {srs_output_file}")
        
        return {
            "processed_files": processed_files,
            "srs_document": srs_document,
            "output_file": srs_output_file
        }
        
    except Exception as e:
        logging.error(f"Error processing content: {str(e)}")
        raise

def run_requirements_extractor(markdown_dir, output_directory, api_type, clients):
    """
    Main function to run the requirements extraction process.
    Handles user input, processes markdown files, and generates INCOSE-formatted requirements.
    """
   
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Verify the markdown directory exists
    if os.path.exists(markdown_dir):
        logging.info(f"Found markdown directory at {markdown_dir}")
        markdown_files = [f for f in os.listdir(markdown_dir) if f.endswith('.md')]
        logging.info(f"Found {len(markdown_files)} markdown files")
    else:
        logging.error(f"Markdown directory not found at {markdown_dir}")
        print(f"Error: Directory not found at {markdown_dir}")
        return  # Exit the function if directory doesn't exist


    try:
        logging.info(f"Processing with {api_type}...")
        print(f"\nProcessing Implementation Guide with {api_type.capitalize()}...")
        print(f"This may take several minutes depending on the size of the Implementation Guide.")
        
        # Process the markdown files and generate direct INCOSE SRS document
        api_results = process_markdown_content_for_incose_srs(
            clients=clients,
            api_type=api_type, 
            markdown_dir=markdown_dir,
            output_directory=output_directory
        )
        
        # Output the results to the user
        print("\n" + "="*80)
        print(f"Processing complete!")
        print(f"Generated requirements document: {api_results['output_file']}")
        print(f"Processed {len(api_results['processed_files'])} files")
        print("="*80)
        
    except Exception as e:
        logging.error(f"Error processing {api_type}: {str(e)}")
        print(f"\nError occurred during processing: {str(e)}")
        print("Check the log file for more details.")