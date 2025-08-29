"""
FHIR Requirements Refinement Module

This module processes a raw list of FHIR Implementation Guide requirements and uses an LLM 
to produce a refined, concise list of only the testable requirements.

Features:
- Takes a markdown file containing FHIR requirements (generated from an IG)
- Applies filtering to identify only testable requirements
- Consolidates duplicate requirements and merges related ones
- Formats each requirement with consistent structure
- Outputs a clean, testable requirements list
- Enhanced token management to handle large requirement lists

Usage:
    from reqs_reviewer import refine_requirements, run_interactive_refinement
    
    # Direct usage
    result = refine_requirements("input_file.md", "claude", "output_dir")
    
    # Interactive mode
    result = run_interactive_refinement()
"""

import os
import logging
import time
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime, timedelta
import re
import tiktoken
import importlib.util
from dotenv import load_dotenv
import sys


logging.basicConfig(level=logging.INFO, 
                       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def setup_environment(project_root: str = None):
    """
    Set up the environment for requirements refinement
    
    Args:
        project_root: Path to project root directory. If None, auto-detected.
        
    Returns:
        Dict containing paths and utilities
    """
    if project_root is None:
        project_root = Path.cwd().parent
    else:
        project_root = Path(project_root)
    
    # Load environment variables (MISSING from original)
    load_dotenv()
    
    # Default paths
    default_input_dir = project_root / "pipeline" / "checkpoints" / "requirements_extraction" / "markdown"
    default_output_dir = project_root / "pipeline" / "checkpoints" / "revised_reqs_extraction"
    
    # Create output directory if it doesn't exist (MISSING from original)
    default_output_dir.mkdir(parents=True, exist_ok=True)
    
    # Add project root to sys.path for imports (IMPROVEMENT)
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    
    # Import LLM utils with better error handling
    llm_utils_path = project_root / 'pipeline' /'llm_utils.py'
    if not llm_utils_path.exists():
        raise FileNotFoundError(f"llm_utils.py not found at {llm_utils_path}")
    
    spec = importlib.util.spec_from_file_location("llm_utils", llm_utils_path)
    llm_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(llm_utils)
    
    # Import prompt utilities with better error handling
    prompt_utils_path = project_root / 'prompt_utils.py'
    if not prompt_utils_path.exists():
        raise FileNotFoundError(f"prompt_utils.py not found at {prompt_utils_path}")
    
    spec = importlib.util.spec_from_file_location("prompt_utils", prompt_utils_path)
    prompt_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prompt_utils)
    
    # Setup the prompt environment
    try:
        prompt_env = prompt_utils.setup_prompt_environment(project_root)
    except Exception as e:
        raise RuntimeError(f"Failed to setup prompt environment: {e}")
    
    # System prompts
    system_prompts = {
        "claude": "You are a Healthcare Standards Expert tasked with analyzing and refining FHIR Implementation Guide requirements.",
        "gemini": "Your role is to analyze and refine FHIR Implementation Guide requirements, focusing on making them concise, testable, and conformance-oriented.",
        "gpt": "As a Healthcare Standards Expert, analyze and refine FHIR Implementation Guide requirements to produce a concise, testable requirements list."
    }
    
    return {
        "project_root": project_root,
        "default_input_dir": str(default_input_dir),
        "default_output_dir": str(default_output_dir),
        "llm_utils": llm_utils,
        "prompt_utils": prompt_utils,
        "prompt_env": prompt_env,
        "system_prompts": system_prompts
    }

def get_requirements_refinement_prompt(requirements_list: str, prompt_utils, requirements_refinement_path: str) -> str:
    """
    Create the prompt for refining requirements list using external prompt file
    
    Args:
        requirements_list: The original list of requirements
        prompt_utils: Prompt utilities module
        requirements_refinement_path: Path to requirements refinement prompt
        
    Returns:
        str: The prompt for the LLM loaded from external file
    """
    return prompt_utils.load_prompt(
        requirements_refinement_path,
        requirements_list=requirements_list
    )

def estimate_tokens(text: str, api_type: str = "claude", llm_utils=None) -> int:
    """
    Estimate token count for different models using existing count_tokens method
    """
    if llm_utils:
        try:
            temp_client = llm_utils.LLMApiClient()
            return temp_client.count_tokens(text, api_type)
        except:
            pass
    
    # Fallback estimation if client creation fails
    if api_type == "gpt":
        try:
            encoding = tiktoken.encoding_for_model("gpt-4o")
            return len(encoding.encode(text))
        except:
            return len(text) // 4
    else:
        # Claude and Gemini fallback
        return len(text) // 4

def get_token_limits(api_type: str, llm_utils=None) -> Tuple[int, int]:
    """
    Get input and output token limits for different APIs
    """
    # Input limits (conservative estimates for context windows)
    input_limits = {
        "claude": 180000,    # Claude 3.5 Sonnet has 200K, leave buffer
        "gemini": 900000,    # Gemini 2.5 Pro has 1M, leave buffer  
        "gpt": 120000        # GPT-4o has 128K, leave buffer
    }
    
    # Output limits from config
    if llm_utils and hasattr(llm_utils, 'API_CONFIGS'):
        output_limits = {
            "claude": llm_utils.API_CONFIGS["claude"]["max_tokens"],
            "gemini": llm_utils.API_CONFIGS["gemini"]["max_tokens"], 
            "gpt": llm_utils.API_CONFIGS["gpt"]["max_tokens"]
        }
    else:
        output_limits = {
            "claude": 8192,
            "gemini": 8192,
            "gpt": 8192
        }
    
    return input_limits.get(api_type, 100000), output_limits.get(api_type, 4000)

def split_requirements_by_tokens(requirements_text: str, max_input_tokens: int, 
                                prompt_template: str, api_type: str, 
                                prompt_utils, requirements_refinement_path: str,
                                llm_utils=None) -> List[str]:
    """
    Split requirements into chunks that fit within token limits
    """
    # For prompt overhead calculation, use existing prompt loading function
    sample_prompt = prompt_utils.load_prompt(requirements_refinement_path, requirements_list="PLACEHOLDER")
    prompt_overhead = estimate_tokens(sample_prompt, api_type, llm_utils) - estimate_tokens("PLACEHOLDER", api_type, llm_utils)
    
    # Available tokens for requirements (with safety buffer)
    available_tokens = max_input_tokens - prompt_overhead - 2000  # Larger safety buffer
    
    logging.info(f"Prompt overhead: {prompt_overhead} tokens")
    logging.info(f"Available tokens for requirements: {available_tokens}")
    
    # Split by individual requirements first
    #req_pattern = r'(?=^---\s*\n#\s*REQ-\d+)'
    req_pattern = r'(?=^#+\s+REQ-\d+)'
    requirements = re.split(req_pattern, requirements_text, flags=re.MULTILINE)
    requirements = [req.strip() for req in requirements if req.strip()]
    
    logging.info(f"Found {len(requirements)} individual requirements to process")
    
    chunks = []
    current_chunk = ""
    current_tokens = 0
    
    for i, req in enumerate(requirements):
        req_tokens = estimate_tokens(req, api_type, llm_utils)
        
        # If single requirement exceeds limit, it needs special handling
        if req_tokens > available_tokens:
            logging.warning(f"Requirement {i+1} exceeds token limit ({req_tokens} > {available_tokens})")
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = ""
                current_tokens = 0
            
            # Try to split the large requirement (this is tricky and may not work perfectly)
            chunks.append(req)  # Add it anyway, let API handle it
            continue
        
        # Check if adding this requirement would exceed limit
        if current_tokens + req_tokens > available_tokens:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = req
            current_tokens = req_tokens
        else:
            current_chunk += "\n\n" + req if current_chunk else req
            current_tokens += req_tokens
    
    if current_chunk:
        chunks.append(current_chunk)
    
    logging.info(f"Split into {len(chunks)} chunks")
    return chunks

def merge_and_renumber_requirements(results: List[str]) -> str:
    """
    Merge multiple result chunks and renumber requirements sequentially
    """
    all_requirements = []
    
    for result in results:
        # Skip safety filter blocked content
        if "[CONTENT BLOCKED BY SAFETY FILTER - SKIPPED]" in result:
            logging.warning("Skipping chunk blocked by safety filter")
            continue
            
        # Extract individual requirements from each result
        req_pattern = r'---\s*\n(#\s*REQ-\d+.*?)(?=---|\Z)'
        matches = re.findall(req_pattern, result, re.DOTALL)
        all_requirements.extend(matches)
    
    # Renumber requirements
    final_output = ""
    for i, req in enumerate(all_requirements, 1):
        # Replace the REQ-XX number
        req_renumbered = re.sub(r'#\s*REQ-\d+', f'# REQ-{i:02d}', req)
        final_output += f"---\n{req_renumbered}\n"
    
    return final_output

def validate_output_completeness(input_count: int, output_count: int, 
                               estimated_output_tokens: int, max_output_tokens: int):
    """
    Validate that output wasn't truncated
    """
    warnings = []
    
    # Check if output might be truncated
    if estimated_output_tokens > max_output_tokens * 0.95:
        warnings.append(f"Output may be truncated. Estimated tokens: {estimated_output_tokens}, Limit: {max_output_tokens}")
    
    # Check if significant requirements were lost (more than 70% reduction might indicate issues)
    if output_count < input_count * 0.3:
        warnings.append(f"Large reduction in requirements count (from {input_count} to {output_count}). Verify this is expected.")
    
    return warnings

def make_api_request_with_limits(client_instance, api_type: str, content: str, 
                               prompt_utils, requirements_refinement_path: str,
                               system_prompts: dict, llm_utils=None) -> str:
    """Enhanced API request with token limit checking using LLMApiClient"""
    
    # Validate inputs (MISSING from original)
    if not content.strip():
        raise ValueError("Content cannot be empty")
    
    if api_type not in system_prompts:
        raise ValueError(f"Unsupported API type: {api_type}")
    
    # Get token limits for this API
    max_input_tokens, max_output_tokens = get_token_limits(api_type, llm_utils)
    
    # Get the full prompt using existing function
    try:
        full_prompt = get_requirements_refinement_prompt(content, prompt_utils, requirements_refinement_path)
    except Exception as e:
        raise RuntimeError(f"Failed to generate prompt: {e}")
    
    estimated_tokens = estimate_tokens(full_prompt, api_type, llm_utils)
    
    logging.info(f"Estimated input tokens: {estimated_tokens}")
    logging.info(f"API input limit: {max_input_tokens}")
    logging.info(f"API output limit: {max_output_tokens}")
    
    if estimated_tokens > max_input_tokens * 0.9:  # 90% threshold
        logging.warning("Input may exceed token limits. Splitting into chunks...")
        
        # Load the prompt template from external file with error handling
        try:
            with open(requirements_refinement_path, 'r', encoding='utf-8') as f:
                prompt_template = f.read()
        except Exception as e:
            raise RuntimeError(f"Failed to read prompt template from {requirements_refinement_path}: {e}")
        
        # Split requirements into manageable chunks
        chunks = split_requirements_by_tokens(content, max_input_tokens, prompt_template, api_type, 
                                            prompt_utils, requirements_refinement_path, llm_utils)
        logging.info(f"Split into {len(chunks)} chunks")
        
        if not chunks:
            raise RuntimeError("Failed to split content into processable chunks")
        
        all_results = []
        for i, chunk in enumerate(chunks):
            logging.info(f"Processing chunk {i+1}/{len(chunks)}")
            
            # Use existing prompt loading function for each chunk
            try:
                chunk_prompt = get_requirements_refinement_prompt(chunk, prompt_utils, requirements_refinement_path)
            except Exception as e:
                logging.error(f"Failed to generate prompt for chunk {i+1}: {e}")
                all_results.append(f"[ERROR GENERATING PROMPT FOR CHUNK {i+1}: {str(e)}]")
                continue
            
            # Use existing LLMApiClient method
            try:
                response = client_instance.make_llm_request(
                    api_type=api_type,
                    prompt=chunk_prompt,
                    sys_prompt=system_prompts[api_type],
                    reformat=False  # We're already providing the formatted prompt
                )
                all_results.append(response)
                
                # Add small delay between chunks
                time.sleep(1)
                
            except Exception as e:
                logging.error(f"Error processing chunk {i+1}: {str(e)}")
                all_results.append(f"[ERROR PROCESSING CHUNK {i+1}: {str(e)}]")
        
        # Merge results and renumber requirements
        try:
            return merge_and_renumber_requirements(all_results)
        except Exception as e:
            raise RuntimeError(f"Failed to merge chunk results: {e}")
    
    else:
        # Single API call - use existing method
        try:
            return client_instance.make_llm_request(
                api_type=api_type,
                prompt=full_prompt,
                sys_prompt=system_prompts[api_type],
                reformat=False  # We're already providing the formatted prompt
            )
        except Exception as e:
            raise RuntimeError(f"Failed to process single API request: {e}")


def count_requirements_in_markdown(markdown_text):
    """
    Count the number of requirements in a markdown file that follow the REQ-XX format.
    
    Handles both formats:
    # REQ-01
    or
    ## REQ-01
    """
    # Pattern for both formats: either # REQ-XX or ## REQ-XX
    req_pattern = r"^\s*(#|##)\s+REQ-\d+"
    
    # Count the occurrences
    lines = markdown_text.split('\n')
    count = 0
    
    for line in lines:
        if re.match(req_pattern, line):
            count += 1
    
    return count

def refine_requirements(input_file: str, api_type: str = "claude", 
                       output_dir: str = None, project_root: str = None,
                       llm_client_instance=None) -> Dict[str, Any]:
    """
    Refine requirements using the specified API with token limit handling
    
    Args:
        input_file: Path to the input requirements list markdown file
        api_type: The API to use ("claude", "gemini", or "gpt")
        output_dir: Directory to save the output (optional)
        project_root: Path to project root (optional, auto-detected if None)
        llm_client_instance: Pre-initialized LLM client instance (optional)
        
    Returns:
        Dict containing processing results and path to refined requirements
    """
    # Setup environment
    try:
        env = setup_environment(project_root)
    except Exception as e:
        raise RuntimeError(f"Failed to setup environment: {e}")
    
    logging.info(f"Starting requirements refinement with {api_type}")
    
    # Use provided output directory or default
    if output_dir is None:
        output_dir = env["default_output_dir"]
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Validate input file
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    if not input_path.is_file():
        raise ValueError(f"Input path is not a file: {input_file}")
    
    # Read input requirements with proper encoding
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            requirements_content = f.read()
    except Exception as e:
        raise RuntimeError(f"Failed to read input file {input_file}: {e}")
    
    if not requirements_content.strip():
        raise ValueError("Input file is empty or contains only whitespace")
    
    # Count original requirements
    original_req_count = count_requirements_in_markdown(requirements_content)
    logging.info(f"Original requirements count: {original_req_count}")
    
    # Check input size
    input_tokens = estimate_tokens(requirements_content, api_type, env["llm_utils"])
    logging.info(f"Input size: {len(requirements_content)} characters, ~{input_tokens} tokens")
    
    # Initialize LLMApiClient
    if llm_client_instance is None:
        try:
            client_instance = env["llm_utils"].LLMApiClient()
            if api_type not in client_instance.clients or client_instance.clients[api_type] is None:
                raise ValueError(f"API client for {api_type} is not available")
        except Exception as e:
            logging.error(f"Error initializing LLMApiClient: {str(e)}")
            raise
    else:
        client_instance = llm_client_instance
        # Validate that the provided client has the required API
        if hasattr(client_instance, 'clients') and api_type not in client_instance.clients:
            raise ValueError(f"Provided client instance does not support {api_type}")
    
    try:
        # Process the requirements with enhanced token handling
        logging.info(f"Sending requirements to {api_type} for refinement...")
        refined_requirements = make_api_request_with_limits(
            client_instance, api_type, requirements_content,
            env["prompt_utils"], env["prompt_env"]["requirements_refinement_path"],
            env["system_prompts"], env["llm_utils"]
        )
        
        if not refined_requirements or not refined_requirements.strip():
            raise RuntimeError("API returned empty or whitespace-only response")
        
        # Validate output
        refined_req_count = count_requirements_in_markdown(refined_requirements)
        output_tokens = estimate_tokens(refined_requirements, api_type, env["llm_utils"])
        max_input_tokens, max_output_tokens = get_token_limits(api_type, env["llm_utils"])
        
        # Check for potential issues
        warnings = validate_output_completeness(
            original_req_count, refined_req_count, output_tokens, max_output_tokens
        )
        
        if warnings:
            for warning in warnings:
                logging.warning(warning)
                print(f"WARNING: {warning}")
        
        # Generate output filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{api_type}_reqs_list_v2_{timestamp}.md"
        #output_filename = f"reqs_list_v2.md"
        output_file_path = output_dir / output_filename
        
        # Save refined requirements with proper encoding
        try:
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(refined_requirements)
        except Exception as e:
            raise RuntimeError(f"Failed to save output file {output_file_path}: {e}")
        
        logging.info(f"Requirements refinement complete. Output saved to: {output_file_path}")
        logging.info(f"Refined {original_req_count} -> {refined_req_count} requirements")
        logging.info(f"Output size: {len(refined_requirements)} characters, ~{output_tokens} tokens")
        
        return {
            "input_file": str(input_path),
            "output_file": str(output_file_path),
            "api_used": api_type,
            "timestamp": timestamp,
            "original_requirements_count": original_req_count,
            "requirements_count": refined_req_count,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "warnings": warnings
        }
        
    except Exception as e:
        logging.error(f"Error refining requirements: {str(e)}")
        raise




def run_interactive_refinement(project_root: str = None) -> Optional[Dict[str, Any]]:
    """
    Run the refinement process with user input (interactive mode)
    
    Args:
        project_root: Path to project root (optional, auto-detected if None)
        
    Returns:
        Dict containing processing results or None if error occurred
    """
    # Setup environment
    env = setup_environment(project_root)
    
    print("\n" + "="*80)
    print("FHIR Requirements Refinement Tool")
    print("="*80)
    
    # Start timing the entire function execution
    start_time = time.time()
    
    # Get input directory or use default
    input_dir = input(f"Enter input directory path or accept default (default '{env['default_input_dir']}'): ") or env["default_input_dir"]
    input_dir_path = Path(input_dir)
    
    if not input_dir_path.exists():
        print(f"Warning: Input directory {input_dir} does not exist.")
        input_file = input("Enter full path to requirements markdown file: ")
    else:
        # List all markdown files in the input directory
        md_files = list(input_dir_path.glob("*.md"))
        
        if md_files:
            # Sort files by modification time (newest first)
            md_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            
            # Show only the 10 most recent files
            recent_files = md_files[:10]
            
            print("\nMost recent files:")
            for idx, file in enumerate(recent_files, 1):
                # Format the modification time as part of the display
                mod_time = datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
                print(f"{idx}. {file.name} ({mod_time})")
            
            # Let user select from the list, see more files, or enter a custom path
            print("\nOptions:")
            print("- Select a number (1-10) to choose one of the following most recently generated files")
            print("- Enter 'all' to see all files")
            print("- Enter a full path to use a specific file")
            
            selection = input("\nReview the printed options for choosing a requirements file and enter applicable selection: ")
            
            if selection.lower() == 'all':
                # Show all files with pagination
                all_files = md_files
                page_size = 20
                total_pages = (len(all_files) + page_size - 1) // page_size
                
                current_page = 1
                while current_page <= total_pages:
                    start_idx = (current_page - 1) * page_size
                    end_idx = min(start_idx + page_size, len(all_files))
                    
                    print(f"\nAll files (page {current_page}/{total_pages}):")
                    for idx, file in enumerate(all_files[start_idx:end_idx], start_idx + 1):
                        mod_time = datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
                        print(f"{idx}. {file.name} ({mod_time})")
                    
                    if current_page < total_pages:
                        next_action = input("\nPress Enter for next page, 'q' to select, or enter a number to choose a file: ")
                        if next_action.lower() == 'q':
                            break
                        elif next_action.isdigit() and 1 <= int(next_action) <= len(all_files):
                            input_file = str(all_files[int(next_action) - 1])
                            break
                        else:
                            current_page += 1
                    else:
                        break
                
                if 'input_file' not in locals():
                    # If we went through all pages without selection
                    file_number = input("\nEnter the file number to process: ")
                    if file_number.isdigit() and 1 <= int(file_number) <= len(all_files):
                        input_file = str(all_files[int(file_number) - 1])
                    else:
                        input_file = file_number  # Treat as a custom path
            
            elif selection.isdigit() and 1 <= int(selection) <= len(recent_files):
                input_file = str(recent_files[int(selection) - 1])
            else:
                input_file = selection  # Treat as a custom path
        else:
            print(f"No markdown files found in {input_dir}")
            input_file = input("Enter full path to requirements markdown file: ")
    
    # Get output directory or use default
    output_dir = input(f"Enter output directory path or accept default (default '{env['default_output_dir']}'): ") or env["default_output_dir"]
    output_dir_path = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_dir_path.mkdir(parents=True, exist_ok=True)
    
    # Select the API to use
    print("\nSelect the API to use:")
    print("1. Claude")
    print("2. Gemini")
    print("3. GPT-4")
    api_choice = input("Enter your choice of API to use, based on the printed listing (1-3, default 1): ") or "1"
    
    api_mapping = {
        "1": "claude",
        "2": "gemini",
        "3": "gpt"
    }
    
    api_type = api_mapping.get(api_choice, "claude")
    
    try:
        # Run the refinement
        print(f"\nProcessing requirements with {api_type.capitalize()}...")
        result = refine_requirements(input_file, api_type, str(output_dir_path), env["project_root"])
        
        # Calculate total execution time
        total_elapsed_time = time.time() - start_time
        total_elapsed_formatted = str(timedelta(seconds=int(total_elapsed_time)))
        
        print("\n" + "="*80)
        print("Requirements Refinement Complete!")
        print(f"Input file: {result['input_file']}")
        print(f"Refined requirements saved to: {result['output_file']}")
        print(f"API used: {result['api_used']}")
        
        # Handle both old and new result formats
        if 'original_requirements_count' in result:
            print(f"Original requirements: {result['original_requirements_count']}")
            print(f"Refined requirements: {result['requirements_count']}")
            print(f"Input tokens: ~{result['input_tokens']}")
            print(f"Output tokens: ~{result['output_tokens']}")
            if result.get('warnings'):
                print("Warnings:")
                for warning in result['warnings']:
                    print(f"  - {warning}")
        else:
            print(f"Number of requirements identified: {result['requirements_count']}")
        
        print(f"Total execution time: {total_elapsed_formatted}")
        print("="*80)
        
        return result
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        print(f"\nError occurred during refinement: {str(e)}")
        print("Check the log for more details.")
        return None

# Main execution functions for backwards compatibility
def main():
    """Main function for standalone execution"""
    # Set up logging
    logging.basicConfig(level=logging.INFO, 
                       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    return run_interactive_refinement()

if __name__ == "__main__":
    main()


def create_batch_refinement_prompt(batch_content: str, batch_num: int, total_batches: int, 
                                  prompt_utils, requirements_refinement_path: str) -> str:
    """Create the refinement prompt for a batch using your existing prompt file"""
    
    # Use existing prompt loading function - this will load requirements_refinement.md
    return get_requirements_refinement_prompt(batch_content, prompt_utils, requirements_refinement_path)



def batch_process_requirements(input_file: str, output_dir: str, llm_client_instance, 
                             batch_size: int = 100, api_type: str = "claude", 
                             project_root: str = None) -> Dict[str, Any]:
    """
    Process requirements in batches of specified size
    
    Args:
        input_file: Path to input requirements file
        output_dir: Directory to save output
        llm_client_instance: Your LLM client instance
        batch_size: Number of requirements per batch (default: 100)
        api_type: API to use (claude/gemini/gpt)
        project_root: Project root path (optional)
    
    Returns:
        Dict with processing results
    """
    
    print("STARTING BATCH PROCESSING")
    print("=" * 50)
    print(f"Input: {input_file}")
    print(f"Output: {output_dir}")
    print(f"Batch size: {batch_size} requirements")
    print(f"API: {api_type}")
    print()
    
    # Setup environment to get prompt utilities
    try:
        env = setup_environment(project_root)
    except Exception as e:
        raise RuntimeError(f"Failed to setup environment: {e}")
    
    # Read input file
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"File size: {len(content):,} characters")
    
    # Split into individual requirements
    print("Splitting requirements...")
    req_pattern = r'(?=^#+\s+REQ-\d+)'
    requirements = re.split(req_pattern, content, flags=re.MULTILINE)
    requirements = [req.strip() for req in requirements if req.strip()]
    
    print(f"Found {len(requirements)} total requirements")
    
    # Calculate batches
    total_batches = (len(requirements) + batch_size - 1) // batch_size
    print(f"Will process in {total_batches} batches")
    print()
    
    # Process each batch
    all_results = []
    successful_batches = 0
    failed_batches = 0
    start_time = time.time()
    
    for batch_num in range(total_batches):
        batch_start_idx = batch_num * batch_size
        batch_end_idx = min(batch_start_idx + batch_size, len(requirements))
        batch_reqs = requirements[batch_start_idx:batch_end_idx]
        
        print(f"BATCH {batch_num + 1}/{total_batches}")
        print(f"   Requirements: {len(batch_reqs)} (#{batch_start_idx + 1}-#{batch_end_idx})")
        
        # Create batch content
        batch_content = "\n\n".join(batch_reqs)
        batch_tokens = len(batch_content) // 4
        print(f"   Size: {len(batch_content):,} chars (~{batch_tokens:,} tokens)")
        
        # Process this batch
        batch_start_time = time.time()
        
        try:
            # Create the prompt using your existing prompt file
            batch_prompt = create_batch_refinement_prompt(
                batch_content, batch_num + 1, total_batches,
                env["prompt_utils"], env["prompt_env"]["requirements_refinement_path"]
            )
            
            # Make API request with timeout
            result = make_batch_request_with_timeout(
                llm_client_instance, api_type, batch_prompt,
                env["system_prompts"][api_type],  # Use your system prompts
                timeout_minutes=8  # 8 minute timeout per batch
            )
            
            batch_elapsed = time.time() - batch_start_time
            print(f"   Completed in {batch_elapsed:.1f}s")
            
            all_results.append(result)
            successful_batches += 1
            
            # Brief pause between batches
            if batch_num < total_batches - 1:  # Don't pause after last batch
                print("   Pausing 2s...")
                time.sleep(2)
        
        except Exception as e:
            batch_elapsed = time.time() - batch_start_time
            print(f"   Failed after {batch_elapsed:.1f}s: {str(e)}")
            
            # Add error placeholder
            error_result = f"""
---
# ERROR IN BATCH {batch_num + 1}

**Error**: {str(e)}
**Requirements**: {batch_start_idx + 1} to {batch_end_idx}
**Time**: {batch_elapsed:.1f} seconds

---
"""
            all_results.append(error_result)
            failed_batches += 1
        
        # Progress update
        total_elapsed = time.time() - start_time
        avg_time_per_batch = total_elapsed / (batch_num + 1)
        remaining_batches = total_batches - (batch_num + 1)
        eta_minutes = (remaining_batches * avg_time_per_batch) / 60
        
        print(f"   Progress: {batch_num + 1}/{total_batches} ({((batch_num + 1)/total_batches)*100:.1f}%)")
        print(f"   ETA: {eta_minutes:.1f} minutes remaining")
        print()
    
    # Combine all results
    print("COMBINING RESULTS")
    print("-" * 20)
    
    final_output = combine_batch_results(all_results)
    final_req_count = count_requirements_in_output(final_output)
    
    # Save output
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{api_type}_refined_requirements_{timestamp}.md"
    #output_filename = f"refined_requirements.md"
    output_path = output_dir_path / output_filename
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
    
    # Final summary
    total_time = time.time() - start_time
    
    print("BATCH PROCESSING COMPLETE!")
    print("=" * 40)
    print(f"Output saved: {output_path}")
    print(f"Original requirements: {len(requirements)}")
    print(f"Final requirements: {final_req_count}")
    print(f"Successful batches: {successful_batches}/{total_batches}")
    print(f"Failed batches: {failed_batches}/{total_batches}")
    print(f"Total time: {total_time/60:.1f} minutes")
    print(f"Average per batch: {total_time/total_batches:.1f} seconds")
    
    return {
        "input_file": str(input_path),
        "output_file": str(output_path),
        "api_used": api_type,
        "timestamp": timestamp,
        "original_requirements_count": len(requirements),
        "final_requirements_count": final_req_count,
        "total_batches": total_batches,
        "successful_batches": successful_batches,
        "failed_batches": failed_batches,
        "total_time_minutes": total_time / 60,
        "average_time_per_batch_seconds": total_time / total_batches
    }


def make_batch_request_with_timeout(llm_client_instance, api_type: str, prompt: str, 
                                   system_prompt: str, timeout_minutes: int = 12) -> str:
    """Make API request with timeout monitoring"""
    
    import threading
    
    result = [None]
    exception = [None]
    
    def api_call():
        try:
            result[0] = llm_client_instance.make_llm_request(
                api_type=api_type,
                prompt=prompt,
                sys_prompt=system_prompt,  # Use the passed system prompt
                reformat=False
            )
        except Exception as e:
            exception[0] = e
    
    # Start API call in separate thread
    thread = threading.Thread(target=api_call)
    thread.daemon = True
    thread.start()
    
    # Monitor with timeout
    timeout_seconds = timeout_minutes * 60
    start_time = time.time()
    
    while thread.is_alive():
        elapsed = time.time() - start_time
        
        if elapsed > timeout_seconds:
            print(f"      Request taking longer than {timeout_minutes} minutes...")
            # Give it a bit more time, but warn
            if elapsed > timeout_seconds * 1.5:  # 150% of timeout
                raise TimeoutError(f"Request timed out after {timeout_minutes * 1.5:.1f} minutes")
        
        time.sleep(1)
    
    if exception[0]:
        raise exception[0]
    
    if result[0] is None:
        raise RuntimeError("API call completed but no result received")
    
    return result[0]



def combine_batch_results(batch_results: List[str]) -> str:
    """Combine all batch results and renumber requirements"""
    
    print("Merging batch results and renumbering...")
    
    final_output = """# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the US Core FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.

"""
    
    req_counter = 1
    
    for i, batch_result in enumerate(batch_results):
        if not batch_result or batch_result.strip() == "":
            continue
            
        print(f"   Processing batch {i+1} results...")
        
        # Skip error results  
        if "[ERROR" in batch_result and "BATCH" in batch_result:
            final_output += batch_result + "\n"
            continue
        
        # Process each line and renumber requirements
        lines = batch_result.split('\n')
        
        for line in lines:
            if re.match(r'^# REQ-\d+', line):
                # Renumber this requirement
                line = f"# REQ-{req_counter:03d}"
                req_counter += 1
            
            final_output += line + '\n'
    
    print(f"   Renumbered {req_counter - 1} requirements")
    
    return final_output

def count_requirements_in_output(output: str) -> int:
    """Count requirements in the final output"""
    return len(re.findall(r'^# REQ-\d+', output, re.MULTILINE))


def run_batch_requirements_refinement(input_file: str, llm_client_instance, 
                                     output_dir: str = "checkpoints/revised_reqs_extraction",
                                     batch_size: int = 100, api_type: str = "claude",
                                     project_root: str = None):
    """
    Convenience function to run batch processing with your existing setup
    
    Usage:
        result = run_batch_requirements_refinement(
            input_file="path/to/your/requirements.md",
            llm_client_instance=llm_clients,
            batch_size=100,
            api_type="claude"
        )
    """
    
    return batch_process_requirements(
        input_file=input_file,
        output_dir=output_dir,
        llm_client_instance=llm_client_instance,
        batch_size=batch_size,
        api_type=api_type,
        project_root=project_root
    )