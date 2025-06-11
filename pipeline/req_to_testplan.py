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

def parse_capability_statement(file_path: str) -> Dict[str, Any]:
    """
    Parse a FHIR Capability Statement markdown file into a structured dictionary
    
    Args:
        file_path: Path to the Capability Statement markdown file
        
    Returns:
        Dictionary containing structured Capability Statement information
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract resource capabilities
    resource_sections = {}
    
    # Find resource sections - they typically start with "#### ResourceName"
    resource_matches = re.finditer(r'#### ([A-Za-z]+)\n', content)
    
    for match in resource_matches:
        resource_name = match.group(1)
        start_pos = match.start()
        
        # Find the next resource section or end of document
        next_match = re.search(r'#### ([A-Za-z]+)\n', content[start_pos + len(match.group(0)):])
        if next_match:
            end_pos = start_pos + len(match.group(0)) + next_match.start()
            resource_section = content[start_pos:end_pos]
        else:
            resource_section = content[start_pos:]
        
        # Extract specific capabilities
        search_params = []
        search_param_section = re.search(r'Search Parameter Summary:.*?\| Conformance \| Parameter \| Type \| Example \|\n\| --- \| --- \| --- \| --- \|(.*?)(?:\n\n---|\Z)', 
                                       resource_section, re.DOTALL)
        
        if search_param_section:
            param_lines = search_param_section.group(1).strip().split('\n')
            for line in param_lines:
                if '|' in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 5 and parts[1] and parts[2]:
                        conformance = parts[1].replace('**', '')
                        param_name = parts[2]
                        param_type = parts[3]
                        search_params.append({
                            'name': param_name,
                            'type': param_type,
                            'conformance': conformance
                        })
        
        # Extract supported operations
        operations = []
        operations_section = re.search(r'Supported Operations:(.*?)(?:\n\n|\Z)', resource_section, re.DOTALL)
        if operations_section:
            op_lines = operations_section.group(1).strip().split('\n')
            for line in op_lines:
                if line.strip():
                    operations.append(line.strip())
        
        # Extract includes and revincludes
        includes = []
        includes_section = re.search(r'A Server \*\*SHALL\*\* be capable of supporting the following \_includes:(.*?)(?:\n\n|\Z)', 
                                   resource_section, re.DOTALL)
        if includes_section:
            include_lines = includes_section.group(1).strip().split('\n')
            for line in include_lines:
                if line.strip():
                    include_match = re.search(r'([A-Za-z]+):([A-Za-z\-]+)', line)
                    if include_match:
                        includes.append(f"{include_match.group(1)}:{include_match.group(2)}")
        
        revincludes = []
        revincludes_section = re.search(r'A Server \*\*SHALL\*\* be capable of supporting the following \_revincludes:(.*?)(?:\n\n|\Z)', 
                                      resource_section, re.DOTALL)
        if revincludes_section:
            revinclude_lines = revincludes_section.group(1).strip().split('\n')
            for line in revinclude_lines:
                if line.strip():
                    revinclude_match = re.search(r'([A-Za-z]+):([A-Za-z\-]+)', line)
                    if revinclude_match:
                        revincludes.append(f"{revinclude_match.group(1)}:{revinclude_match.group(2)}")
        
        resource_sections[resource_name] = {
            'search_parameters': search_params,
            'operations': operations,
            'includes': includes,
            'revincludes': revincludes
        }
    
    # Extract general capabilities
    general_capabilities = {}
    general_section = re.search(r'### FHIR RESTful Capabilities(.*?)(?:###|$)', content, re.DOTALL)
    if general_section:
        shall_match = re.search(r'The Plan-Net Server \*\*SHALL\*\*:(.*?)(?:The Plan-Net Server \*\*SHOULD\*\*:|\n\n\*\*Security:\*\*|\Z)', 
                              general_section.group(1), re.DOTALL)
        should_match = re.search(r'The Plan-Net Server \*\*SHOULD\*\*:(.*?)(?:\n\n\*\*Security:\*\*|\Z)', 
                               general_section.group(1), re.DOTALL)
        
        if shall_match:
            shall_items = re.findall(r'\d+\.\s*(.*?)(?:\n\d+\.|\Z)', shall_match.group(1), re.DOTALL)
            general_capabilities['SHALL'] = [item.strip() for item in shall_items]
        
        if should_match:
            should_items = re.findall(r'\d+\.\s*(.*?)(?:\n\d+\.|\Z)', should_match.group(1), re.DOTALL)
            general_capabilities['SHOULD'] = [item.strip() for item in should_items]
    
    return {
        'resources': resource_sections,
        'general_capabilities': general_capabilities
    }

def extract_relevant_capability_info(requirement: Dict[str, str], capability_statement: Dict[str, Any]) -> str:
    """
    Extract relevant capability statement information for a specific requirement
    
    Args:
        requirement: Requirement dictionary
        capability_statement: Parsed capability statement
        
    Returns:
        Formatted string with relevant capability information
    TODO: This is rules-based and ultimately pretty brittle. Maybe introduce more modern NLP techniques?
    """
    # Determine which resource types are relevant to this requirement
    requirement_text = f"{requirement.get('description', '')} {requirement.get('summary', '')}"
    resource_types = []
    
    # plan net resource types
    fhir_resources = [
        "Patient", "Practitioner", "Organization", "Location", "Endpoint", 
        "HealthcareService", "PractitionerRole", "OrganizationAffiliation",
        "InsurancePlan", "Network"
    ]
    
    # Check if requirement mentions specific resources
    for resource in fhir_resources:
        if resource.lower() in requirement_text.lower():
            resource_types.append(resource)
    
    # If no specific resources found, check for general requirements
    if not resource_types:
        # If it's a server requirement
        if "Server" in requirement.get('actor', ''):
            resource_types = ["General Server Capabilities"]
        # If it's a client requirement
        elif "Client" in requirement.get('actor', '') or "Application" in requirement.get('actor', ''):
            resource_types = ["General Client Capabilities"]
    
    # Build relevant capability information
    relevant_info = "### Applicable Capability Statement Information\n\n"
    
    # Add general capabilities
    relevant_info += "#### General Capabilities\n"
    if "general_capabilities" in capability_statement:
        for level in ["SHALL", "SHOULD"]:
            if level in capability_statement["general_capabilities"]:
                relevant_info += f"\n**{level}**:\n"
                for item in capability_statement["general_capabilities"][level]:
                    relevant_info += f"- {item}\n"
    
    # Add resource-specific capabilities
    for resource_type in resource_types:
        if resource_type in capability_statement.get("resources", {}):
            resource_info = capability_statement["resources"][resource_type]
            
            relevant_info += f"\n#### {resource_type} Resource Capabilities\n"
            
            # Add search parameters
            if resource_info.get("search_parameters"):
                relevant_info += "\n**Supported Search Parameters**:\n"
                for param in resource_info["search_parameters"]:
                    relevant_info += f"- {param['name']} ({param['type']}): {param['conformance']}\n"
            
            # Add operations
            if resource_info.get("operations"):
                relevant_info += "\n**Supported Operations**:\n"
                for op in resource_info["operations"]:
                    relevant_info += f"- {op}\n"
            
            # Add includes
            if resource_info.get("includes"):
                relevant_info += "\n**Supported _includes**:\n"
                for include in resource_info["includes"]:
                    relevant_info += f"- {include}\n"
            
            # Add revincludes
            if resource_info.get("revincludes"):
                relevant_info += "\n**Supported _revincludes**:\n"
                for revinclude in resource_info["revincludes"]:
                    relevant_info += f"- {revinclude}\n"
    
    return relevant_info

def load_requirements(req_file):
    with open(req_file) as f:
        data = json.load(f)
    return data

def identify_requirement_group(
    logger,
    llm_clients,
    api_type,
    req,
) -> str:
    """
    Identify the appropriate group for a requirement using LLM only
    
    Args:
        client: The API client
        api_type: API type (claude, gemini, gpt)
        requirement: Requirement dictionary
        rate_limit_func: Function to check rate limits
        
    Returns:
        Identified group name from LLM
    """
    requirement = req['parsed']
    # use LLM to identify group based on prompt
    logger.info(f"Identifying group for requirement {req.get('id', 'unknown')} using {api_type}...")
    
    # Format requirement as markdown
    formatted_req = format_requirement_for_prompt(requirement)
    
    # Retrieve prompt with the requirement using external file
    prompt = get_requirement_grouping_prompt(formatted_req)
    
    # Make the API request with simplified system prompt
    group_system_prompt = "You are a FHIR expert who categorizes requirements by their functional or resource type."
    group_name = llm_clients.make_llm_request(api_type, prompt, sys_prompt=group_system_prompt).strip()
    
    # Clean up response (in case model returns extra text)
    if '\n' in group_name:
        group_name = group_name.split('\n')[0].strip()
    
    return group_name

def generate_test_specification_with_capability(
    logger,
    api_type,
    client, 
    req,
    capability_statement: Dict[str, Any],
) -> str:
    """
    Generate a comprehensive test specification for a single requirement, considering capability statement
    
    Args:
        client: The API client
        api_type: API type (claude, gemini, gpt)
        requirement: Requirement dictionary
        capability_statement: Parsed capability statement
        rate_limit_func: Function to check rate limits
        
    Returns:
        Test specification for the requirement
    """
    requirement = req['parsed']
    logger.info(f"Generating test specification for {req.get('id', 'unknown')} using {api_type}...")
    
    # Format requirement as markdown
    formatted_req = format_requirement_for_prompt(requirement)
    
    # Extract relevant capability information
    capability_info = extract_relevant_capability_info(requirement, capability_statement)
    
    # Create prompt with the requirement and capability information using external file
    prompt = get_test_plan_prompt(formatted_req, capability_info)
    
    # Make the API request
    return client.make_llm_request(api_type, prompt, sys_prompt='You are a FHIR expert')


def generate_test_specification(req, llm_completion):
    formatted_req = format_requirement_for_prompt(req['parsed'])
    prompt = f"""
    Create a test specification for this FHIR Implementation Guide requirement:
    
    {formatted_req}
    
    Include these sections:
    1. Testability Assessment
    2. Complexity
    3. Prerequisites
    4. Required inputs and outputs
    5. Required FHIR Operations
    6. Validation Criteria
    
    Format as markdown with clear headers.
    """
    return llm_completion(prompt)


def generate_consolidated_test_plan(
    llm_clients,
    api_type,
    logger: any,
    requirements_file: str,
    capability_statement_file: str = None,
    ig_name: str = "FHIR Implementation Guide",
    output_dir: str = None
) -> Dict[str, Any]:
    """
    Process requirements and generate a consolidated test plan
    
    Args:
        api_type: API type (claude, gemini, gpt)
        requirements_file: Path to requirements markdown file
        capability_statement_file: Path to capability statement markdown file (optional)
        ig_name: Name of the Implementation Guide
        output_dir: Directory for output files
        
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
        
        # Parse capability statement if provided
        capability_statement = None
        if capability_statement_file and os.path.exists(capability_statement_file):
            capability_statement = parse_capability_statement(capability_statement_file)
            logger.info(f"Parsed capability statement from {capability_statement_file}")
        
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
            
            # Process each requirement in the group
            for i, req in enumerate(grouped_requirements[group]):
                req_id = req.get('id', 'UNKNOWN-ID')
                logger.info(f"Processing requirement for group '{group}': {req_id}")
                
                # Generate test specification with capability statement if available
                if capability_statement:
                    test_spec = generate_test_specification_with_capability(
                        logger, api_type, llm_clients, req, capability_statement
                    )
                else:
                    logger.info(f"Generating basic test specification for {req.get('id', 'unknown')} using {api_type}...")
                    test_spec = generate_test_specification(llm_clients, api_type, req)
                
                # Add to test plan content with proper anchor for TOC linking
                test_plan += f"<a id='{req_id.lower()}'></a>\n\n"
                test_plan += f"### {req_id}: {req.get('summary', 'No summary')}\n\n"
                test_plan += f"**Description**: {req.get('description', '')}\n\n"
                test_plan += f"**Actor**: {req.get('actor', '')}\n\n"
                test_plan += f"**Conformance**: {req.get('conformance', '')}\n\n"
                test_plan += f"{test_spec}\n\n"
                test_plan += "---\n\n"
                
                # Add delay between requests
                if i < len(grouped_requirements[group]) - 1:  # No need to delay after the last request
                    time.sleep(config["delay_between_chunks"])
            
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
