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
    result = refine_requirements("../us-core", "claude", "output_dir")
"""

import os
import logging
import time
from pathlib import Path
import path_helpers
import prompt_utils
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime, timedelta
import re
import importlib.util
from dotenv import load_dotenv
import sys
import json
import csv

# Setup logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def setup_environment() -> Dict[str, Any]:
    """
    Set up the environment for requirements refinement.
    
    Returns:
        Dictionary containing paths and utilities needed for processing
        
    Raises:
        FileNotFoundError: If required files (llm_utils.py, prompt_utils.py) are not found
        RuntimeError: If prompt environment setup fails
    """
    # Load environment variables
    load_dotenv()
    
    # Add project root to sys.path for imports
    if str(path_helpers.PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(path_helpers.PROJECT_ROOT))
    
    # Import LLM utils with better error handling
    llm_utils_path = path_helpers.PROJECT_ROOT / 'pipeline' / 'llm_utils.py'
    if not llm_utils_path.exists():
        raise FileNotFoundError(f"llm_utils.py not found at {llm_utils_path}")
    
    spec = importlib.util.spec_from_file_location("llm_utils", llm_utils_path)
    llm_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(llm_utils)
    
    # System prompts
    system_prompts = {
        "claude": "You are a Healthcare Standards Expert tasked with analyzing and refining FHIR Implementation Guide requirements.",
        "gemini": "Your role is to analyze and refine FHIR Implementation Guide requirements, focusing on making them concise, testable, and conformance-oriented.",
        "gpt": "As a Healthcare Standards Expert, analyze and refine FHIR Implementation Guide requirements to produce a concise, testable requirements list."
    }
    
    return {
        "llm_utils": llm_utils,
        "system_prompts": system_prompts
    }


def get_requirements_refinement_prompt(requirements_list: str, artifacts_dir: str) -> str:
    """
    Create the prompt for refining requirements list using external prompt file.
    
    Args:
        requirements_list: The original list of requirements to refine
        prompt_utils: Prompt utilities module
        requirements_refinement_path: Path to requirements refinement prompt file
        
    Returns:
        The formatted prompt for the LLM loaded from external file
    """
    return prompt_utils.load_prompt(
        artifacts_dir,
        "reqs_refinement.md",
        requirements_list=requirements_list
    )

# Batch Processing Functions

def make_batch_request_with_timeout(client_instance, api_type: str, prompt: str, 
                                   system_prompt: str, timeout_minutes: int = 12) -> str:
    """
    Make API request with timeout monitoring using threading.
    
    Args:
        client_instance: LLM client instance
        api_type: Type of API ('claude', 'gemini', 'gpt')
        prompt: The prompt to send
        system_prompt: System prompt for the API
        timeout_minutes: Timeout in minutes (default 12)
        
    Returns:
        API response text
        
    Raises:
        TimeoutError: If request takes too long
        RuntimeError: If API call fails or returns no result
    """
    import threading
    
    result = [None]
    exception = [None]
    
    def api_call():
        try:
            result[0] = client_instance.make_llm_request(
                api_type=api_type,
                prompt=prompt,
                sys_prompt=system_prompt,
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


def parse_requirements_from_markdown(markdown_text: str) -> List[Dict[str, str]]:
    """
    Parse requirements from markdown format into structured data.
    
    Args:
        markdown_text: The markdown document containing requirements
        
    Returns:
        List of requirement dictionaries
    """
    requirements = []
    
    # Split by requirement headers (# REQ-)
    req_blocks = re.split(r'# (REQ-[^\n]+)', markdown_text)
    
    # Process pairs of (ID, content)
    for i in range(1, len(req_blocks), 2):
        if i + 1 < len(req_blocks):
            req_id = req_blocks[i].strip()
            content = req_blocks[i + 1].strip()
            
            req_dict = {'ID': req_id}
            
            # Extract fields using regex
            fields = {
                'Summary': r'\*\*Summary\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Requirement': r'\*\*Requirement\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Context': r'\*\*Context\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Conformance': r'\*\*Conformance\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Actor': r'\*\*Actor\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Sub-Requirement(s)': r'\*\*Sub-Requirement\(s\)\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Conditionality': r'\*\*Conditionality\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Conditionality Details': r'\*\*Conditionality Details\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Verifiable?': r'\*\*Verifiable\?\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Verifiability Details': r'\*\*Verifiability Details\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Section': r'\*\*Section\*\*:\s*(.+?)(?=\n\*\*|\n---|$)',
                'Grouping': r'\*\*Grouping\*\*:\s*(.+?)(?=\n\*\*|\n---|$)'
            }
            
            for field, pattern in fields.items():
                match = re.search(pattern, content, re.DOTALL)
                req_dict[field] = match.group(1).strip() if match else ''
            
            requirements.append(req_dict)
    
    return requirements


def group_requirements(requirements: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """
    Group requirements by their Group field.
    
    Args:
        requirements: List of requirement dictionaries
        
    Returns:
        Dictionary mapping group names to lists of requirements
    """
    grouped = {}
    for req in requirements:
        group = req.get('Group', 'Ungrouped')
        if group not in grouped:
            grouped[group] = []
        grouped[group].append(req)
    return grouped



def save_requirements_json(requirements: List[Dict[str, str]], output_path: str):
    """Save requirements as JSON."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(requirements, f, indent=2, ensure_ascii=False)
    logging.info(f"Saved JSON output to {output_path}")


def save_requirements_csv(requirements: List[Dict[str, str]], output_path: str):
    """Save requirements as CSV."""
    if not requirements:
        return
    
    fieldnames = ['ID', 'Summary', 'Requirement', 'Context', 'Conformance', 
                  'Actor', 'Sub-Requirement(s)', 'Conditionality', 'Conditionality Details', 
                  'Verifiable?', 'Verifiability Details', 'Section', 'Grouping']
    
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(requirements)
    logging.info(f"Saved CSV output to {output_path}")


def save_requirements_csv_inferno(requirements: List[Dict[str, str]], output_path: str):
    """
    Save requirements as CSV with additional Inferno columns in the specified order.
    """
    if not requirements:
        return
    
    # Define the complete column order for Inferno format
    inferno_fieldnames = [
        'ID', 'URL', 'Summary', 'Requirement', 'Context', 'Conformance', 
        'Actor', 'Sub-Requirement(s)', 'Conditionality', 'Conditionality Details',
        'Verifiable?', 'Verifiability Details', 'Planning To Test?', 
        'Planning To Test Details', 'Page', 'Section', 'Section #', 
        'Grouping', 'Priority', 'Test Plan', 'Questions', 'Notes', 
        'Target Draft Scope', 'Status'
    ]
    
    # Convert requirements to Inferno format
    inferno_requirements = []
    for req in requirements:
        inferno_req = {}
        
        # Copy existing fields directly (they already have the right names)
        for field in ['ID', 'Summary', 'Requirement', 'Context', 'Conformance', 
                      'Actor', 'Sub-Requirement(s)', 'Conditionality', 
                      'Conditionality Details', 'Verifiable?', 'Verifiability Details', 
                      'Section', 'Grouping']:
            inferno_req[field] = req.get(field, '')
        
        # Initialize new empty columns
        new_columns = ['URL', 'Planning To Test?', 'Planning To Test Details', 
                      'Page', 'Section #', 'Priority', 'Test Plan', 
                      'Questions', 'Notes', 'Target Draft Scope', 'Status']
        
        for col in new_columns:
            inferno_req[col] = ''
        
        inferno_requirements.append(inferno_req)
    
    # Write to CSV with all columns in the correct order
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=inferno_fieldnames)
        writer.writeheader()
        writer.writerows(inferno_requirements)
    
    logging.info(f"Saved Inferno CSV output to {output_path}")


def combine_batch_results(batch_results: List[str]) -> str:
    """
    Combine all batch results and renumber requirements sequentially.
    
    Args:
        batch_results: List of result strings from different batches
        
    Returns:
        Combined document with renumbered requirements
    """
    print("Merging batch results and renumbering...")
    
    final_output = """# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

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
    """
    Count requirements in the final output using standard REQ-XX format.
    
    Args:
        output: Output text to count requirements in
        
    Returns:
        Number of requirements found
    """
    return len(re.findall(r'^# REQ-\d+', output, re.MULTILINE))


def batch_process_requirements(input_file: str, output_dir: str, client_instance, artifacts_dir: str,
                             batch_size: int = 100, api_type: str = "claude",
                             output_format: str = "markdown"
                             ) -> Dict[str, Any]:
    """
    Process requirements in batches of specified size for handling large requirement sets.
    
    Args:
        input_file: Path to input requirements file
        output_dir: Directory to save output
        client_instance: LLM client instance
        batch_size: Number of requirements per batch (default: 100)
        api_type: API to use ('claude', 'gemini', 'gpt')

    Returns:
        Dictionary containing processing results including timing and success metrics
        
    Raises:
        FileNotFoundError: If input file doesn't exist
        RuntimeError: If environment setup fails
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
        env = setup_environment()
    except Exception as e:
        raise RuntimeError(f"Failed to setup environment: {e}")
    
    # Read input file
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"File size: {len(content):,} characters")
    
    # Detect format and parse accordingly
    if input_path.suffix == '.json':
        print("Detected JSON format with groups...")
        requirements_data = json.loads(content)
        grouped_reqs = group_requirements(requirements_data)
        total_reqs = len(requirements_data)
        print(f"Found {total_reqs} total requirements in {len(grouped_reqs)} groups")
        use_groups = True
    else:
        print("Detected markdown format...")
        req_pattern = r'(?=^#+\s+REQ-\d+)'
        requirements = re.split(req_pattern, content, flags=re.MULTILINE)
        requirements = [req.strip() for req in requirements if req.strip()]
        total_reqs = len(requirements)
        print(f"Found {total_reqs} total requirements")
        use_groups = False
    
    # Calculate batches
    if use_groups:
        # Count total sub-batches across all groups
        total_batches = 0
        for group_reqs in grouped_reqs.values():
            group_batch_count = (len(group_reqs) + batch_size - 1) // batch_size
            total_batches += group_batch_count
        print(f"Will process in {total_batches} batches across {len(grouped_reqs)} groups")
    else:
        total_batches = (len(requirements) + batch_size - 1) // batch_size
        print(f"Will process in {total_batches} batches")
    print()
    
    # Process each batch
    all_results = []
    successful_batches = 0
    failed_batches = 0
    start_time = time.time()
    
    batch_counter = 0  # Track overall batch number
    
    if use_groups:
        # Process by groups
        for group_name, group_reqs in grouped_reqs.items():
            print(f"\n{'='*60}")
            print(f"PROCESSING GROUP: {group_name}")
            print(f"{'='*60}")
            print(f"Requirements in group: {len(group_reqs)}")

            # Split large groups into sub-batches
            group_batches = []
            for i in range(0, len(group_reqs), batch_size):
                sub_batch = group_reqs[i:i + batch_size]
                group_batches.append(sub_batch)
            
            if len(group_batches) > 1:
                print(f"Group split into {len(group_batches)} sub-batches")
            print()
            
            # Process each sub-batch within the group
            for sub_batch_num, sub_batch_reqs in enumerate(group_batches, 1):
                batch_counter += 1
                
                print(f"BATCH {batch_counter}/{total_batches} (Group: {group_name}, Sub-batch {sub_batch_num}/{len(group_batches)})")
                print(f"   Requirements: {len(sub_batch_reqs)}")
                
                # Convert JSON requirements to markdown format
                batch_content = "\n\n".join([
                    f"# {req['ID']}: {req.get('Summary', '')}\n\n" +
                    "\n\n".join([f"**{k}**: {v}" for k, v in req.items() if k not in ['ID', 'Group'] and v]) +
                    f"\n\n**Group**: {group_name}"  # Add group back to markdown
                    for req in sub_batch_reqs
                ])
                
                batch_tokens = len(batch_content) // 4
                print(f"   Size: {len(batch_content):,} chars (~{batch_tokens:,} tokens)")
                
                # Process this batch
                batch_start_time = time.time()
                
                try:
                    # Create the prompt using existing prompt file
                    batch_prompt = get_requirements_refinement_prompt(batch_content, artifacts_dir)
                    
                    # Make API request with timeout
                    result = make_batch_request_with_timeout(
                        client_instance, api_type, batch_prompt,
                        env["system_prompts"][api_type],
                        timeout_minutes=8
                    )
                    
                    batch_elapsed = time.time() - batch_start_time
                    print(f"   Completed in {batch_elapsed:.1f}s")
                    
                    # Add group header for first sub-batch
                    if sub_batch_num == 1:
                        all_results.append(f"\n\n---\n# GROUP: {group_name}\n---\n\n{result}")
                    else:
                        all_results.append(result)
                    
                    successful_batches += 1
                    
                    # Brief pause between batches
                    if batch_counter < total_batches:
                        print("   Pausing 2s...")
                        time.sleep(2)
                
                except Exception as e:
                    batch_elapsed = time.time() - batch_start_time
                    print(f"   Failed after {batch_elapsed:.1f}s: {str(e)}")
                    
                    # Add error placeholder
                    error_result = f"""
---
# ERROR IN BATCH {batch_counter} (Group: {group_name})

**Error**: {str(e)}
**Time**: {batch_elapsed:.1f} seconds

---
"""
                    all_results.append(error_result)
                    failed_batches += 1
                
                # Progress update
                total_elapsed = time.time() - start_time
                avg_time_per_batch = total_elapsed / batch_counter
                remaining_batches = total_batches - batch_counter
                eta_minutes = (remaining_batches * avg_time_per_batch) / 60
                
                print(f"   Overall Progress: {batch_counter}/{total_batches} ({(batch_counter/total_batches)*100:.1f}%)")
                print(f"   ETA: {eta_minutes:.1f} minutes remaining")
                print()
    
    else:
        # Original markdown processing (unchanged)
        for batch_num in range(total_batches):
            batch_counter += 1
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
                # Create the prompt using existing prompt file
                batch_prompt = get_requirements_refinement_prompt(batch_content, artifacts_dir)
                
                # Make API request with timeout
                result = make_batch_request_with_timeout(
                    client_instance, api_type, batch_prompt,
                    env["system_prompts"][api_type],
                    timeout_minutes=8
                )
                
                batch_elapsed = time.time() - batch_start_time
                print(f"   Completed in {batch_elapsed:.1f}s")
                
                all_results.append(result)
                successful_batches += 1
                
                # Brief pause between batches
                if batch_num < total_batches - 1:
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
    base_filename = f"{api_type}_refined_requirements_{timestamp}"
    
    # Always save markdown
    md_output_path = output_dir_path / f"{base_filename}.md"
    with open(md_output_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
    
    output_files = {"markdown": str(md_output_path)}
    
    # Parse and save in additional formats if requested
    if output_format in ["json", "csv", "inferno", "all"]:
        parsed_reqs = parse_requirements_from_markdown(final_output)
        
        if use_groups:
            # Create a mapping of req_id to group from original data
            req_to_group = {}
            for group_name, group_reqs in grouped_reqs.items():
                for req in group_reqs:
                    req_to_group[req.get('ID', req.get('id', ''))] = group_name
            
            # Add Group field back to parsed requirements
            for req in parsed_reqs:
                req_id = req.get('ID', req.get('id', ''))
                req['Group'] = req_to_group.get(req_id, 'Ungrouped')

        if output_format in ["json", "all"]:
            json_output_path = output_dir_path / f"{base_filename}.json"
            save_requirements_json(parsed_reqs, str(json_output_path))
            output_files["json"] = str(json_output_path)
        
        if output_format in ["csv", "all"]:
            csv_output_path = output_dir_path / f"{base_filename}.csv"
            save_requirements_csv(parsed_reqs, str(csv_output_path))
            output_files["csv"] = str(csv_output_path)

        if output_format in ["inferno", "all"]:
            inferno_output_path = output_dir_path / f"{base_filename}_inferno.csv"
            save_requirements_csv_inferno(parsed_reqs, str(inferno_output_path))
            output_files["inferno"] = str(inferno_output_path)

    # Final summary
    total_time = time.time() - start_time
    
    print("BATCH PROCESSING COMPLETE!")
    print("=" * 40)
    print("Output saved:")
    for fmt, path in output_files.items():
        print(f"  {fmt.upper()}: {path}")
    print(f"Original requirements: {total_reqs}")
    print(f"Final requirements: {final_req_count}")
    if use_groups:
        print(f"Groups processed: {len(grouped_reqs)}")
    print(f"Successful batches: {successful_batches}/{total_batches}")
    print(f"Failed batches: {failed_batches}/{total_batches}")
    print(f"Total time: {total_time/60:.1f} minutes")
    print(f"Average per batch: {total_time/total_batches:.1f} seconds")
    
    return {
        "input_file": str(input_path),
        "output_file": str(output_files),
        "api_used": api_type,
        "timestamp": timestamp,
        "original_requirements_count": total_reqs,
        "final_requirements_count": final_req_count,
        "groups_processed": len(grouped_reqs) if use_groups else None,
        "total_batches": total_batches,
        "successful_batches": successful_batches,
        "failed_batches": failed_batches,
        "total_time_minutes": total_time / 60,
        "average_time_per_batch_seconds": total_time / total_batches
    }


def run_batch_requirements_refinement(client_instance,
                                      artifacts_dir: str = str(path_helpers.DEMO_ARTIFACTS_ROOT),
                                      batch_size: int = 100, api_type: str = "claude",
                                      output_format: str = "markdown"
                                      ) -> Dict[str, Any]:
    """
    Convenience function to run batch processing with existing setup.
    
    Args:
        artifacts_dir: Path to base artifacts directory
        client_instance: Your LLM client instance
        batch_size: Requirements per batch (default: 100)
        api_type: API to use (default: "claude")
        output_format: Format for output ('markdown', 'json', 'csv', 'inferno', or 'all')


    Returns:
        Dictionary containing processing results
        
    Usage:
        >>> result = run_batch_requirements_refinement(
        ...     artifacts_dir="../us-core",
        ...     client_instance=llm_clients,
        ...     batch_size=50,
        ...     api_type="gpt"
        ... )
    """
    input_file = os.path.join(artifacts_dir, "requirements", "grouped", "HealthcareService.json")
    output_dir = os.path.join(artifacts_dir, "requirements", "revised")
    return batch_process_requirements(
        input_file=input_file,
        output_dir=output_dir,
        client_instance=client_instance,
        artifacts_dir=artifacts_dir,
        batch_size=batch_size,
        api_type=api_type,
        output_format=output_format
    )
