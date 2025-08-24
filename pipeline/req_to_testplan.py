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

def parse_capability_statement_by_chunks(file_path: str) -> Dict[str, Any]:
    """
    Parse a FHIR Capability Statement markdown file into resource chunks
    
    Args:
        file_path: Path to the Capability Statement markdown file
        
    Returns:
        Dictionary containing:
        - 'general_capabilities': General server capabilities text
        - 'resource_chunks': Dict mapping resource names to their full sections
        - 'resource_list': List of all resource names found
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract general capabilities section
    general_capabilities = ""
    general_section_match = re.search(
        r'### FHIR RESTful Capabilities(.*?)(?=####|### |$)', 
        content, 
        re.DOTALL
    )
    if general_section_match:
        general_capabilities = general_section_match.group(1).strip()
    
    # Find all resource sections (#### ResourceName)
    resource_chunks = {}
    resource_list = []
    
    # Pattern to match resource headers and capture the resource name
    resource_pattern = r'#### ([A-Za-z][A-Za-z0-9]*)\s*\n'
    resource_matches = list(re.finditer(resource_pattern, content))
    
    for i, match in enumerate(resource_matches):
        resource_name = match.group(1)
        resource_list.append(resource_name)
        
        # Get the start position of this resource section
        start_pos = match.start()
        
        # Find the end position (start of next resource section or end of document)
        if i + 1 < len(resource_matches):
            end_pos = resource_matches[i + 1].start()
        else:
            # This is the last resource, go to end of document
            end_pos = len(content)
        
        # Extract the full resource section
        resource_section = content[start_pos:end_pos].strip()
        
        # Clean up any trailing separators
        resource_section = re.sub(r'\n---\s*$', '', resource_section)
        
        resource_chunks[resource_name] = resource_section
    
    return {
        'general_capabilities': general_capabilities,
        'resource_chunks': resource_chunks,
        'resource_list': resource_list
    }

def extract_relevant_capability_chunks(
    requirement: Dict[str, str], 
    capability_statement: Dict[str, Any]
) -> str:
    """
    Extract relevant capability statement chunks for a specific requirement
    
    Args:
        requirement: Requirement dictionary
        capability_statement: Parsed capability statement with chunks
        
    Returns:
        Formatted string with relevant capability information
    """
    # Get the full text of the requirement for analysis
    requirement_text = " ".join([
        requirement.get('summary', ''),
        requirement.get('description', ''),
        requirement.get('verification', ''),
        requirement.get('actor', '')
    ]).lower()
    
    relevant_info = "### Applicable Capability Statement Information\n\n"
    
    # Always include general capabilities for server-related requirements
    if ('server' in requirement_text or 
        'shall' in requirement_text or 
        'should' in requirement_text):
        
        if capability_statement.get('general_capabilities'):
            relevant_info += "#### General Server Capabilities\n\n"
            relevant_info += capability_statement['general_capabilities']
            relevant_info += "\n\n"
    
    # Find relevant resource chunks
    resource_chunks = capability_statement.get('resource_chunks', {})
    resource_list = capability_statement.get('resource_list', [])
    
    matched_resources = []
    
    # Direct resource name matching (case insensitive)
    for resource_name in resource_list:
        if resource_name.lower() in requirement_text:
            matched_resources.append(resource_name)
    
    # If no direct matches, try partial matching for common variations
    if not matched_resources:
        # Check for plural forms and common variations
        resource_variations = {
            'practitioner': ['Practitioner'],
            'practitioners': ['Practitioner'],
            'organization': ['Organization'],
            'organizations': ['Organization'],
            'location': ['Location'],
            'locations': ['Location'],
            'endpoint': ['Endpoint'],
            'endpoints': ['Endpoint'],
            'healthcare service': ['HealthcareService'],
            'healthcareservice': ['HealthcareService'],
            'practitioner role': ['PractitionerRole'],
            'practitionerrole': ['PractitionerRole'],
            'organization affiliation': ['OrganizationAffiliation'],
            'organizationaffiliation': ['OrganizationAffiliation'],
            'insurance plan': ['InsurancePlan'],
            'insuranceplan': ['InsurancePlan'],
            'network': ['Organization'],  # Networks are a type of Organization
        }
        
        for variation, resource_names in resource_variations.items():
            if variation in requirement_text:
                for resource_name in resource_names:
                    if resource_name in resource_list and resource_name not in matched_resources:
                        matched_resources.append(resource_name)
    
    # Add matched resource chunks
    if matched_resources:
        relevant_info += "#### Relevant Resource Capabilities\n\n"
        for resource_name in matched_resources:
            if resource_name in resource_chunks:
                relevant_info += f"{resource_chunks[resource_name]}\n\n"
                relevant_info += "---\n\n"
    else:
        # If no specific resources matched, this might be a general requirement
        relevant_info += "#### Note\n\n"
        relevant_info += "No specific FHIR resources were identified in this requirement. "
        relevant_info += "This appears to be a general implementation requirement.\n\n"
    
    return relevant_info

def identify_mentioned_resources(requirement: Dict[str, str]) -> List[str]:
    """
    Identify FHIR resources mentioned in a requirement
    
    Args:
        requirement: Requirement dictionary
        
    Returns:
        List of identified resource names
    """
    # Get the full text of the requirement
    requirement_text = " ".join([
        requirement.get('summary', ''),
        requirement.get('description', ''),
        requirement.get('verification', ''),
    ]).lower()
    
    # FHIR resources in Plan-Net
    fhir_resources = [
        'Practitioner', 'Organization', 'Location', 'Endpoint', 
        'HealthcareService', 'PractitionerRole', 'OrganizationAffiliation',
        'InsurancePlan', 'Patient'
    ]
    
    mentioned_resources = []
    
    # Direct matching
    for resource in fhir_resources:
        if resource.lower() in requirement_text:
            mentioned_resources.append(resource)
    
    # Pattern matching for common variations
    patterns = {
        r'\bpractitioner\b': 'Practitioner',
        r'\borganization\b': 'Organization',
        r'\blocation\b': 'Location',
        r'\bendpoint\b': 'Endpoint',
        r'\bhealthcare\s*service\b': 'HealthcareService',
        r'\bpractitioner\s*role\b': 'PractitionerRole',
        r'\borganization\s*affiliation\b': 'OrganizationAffiliation',
        r'\binsurance\s*plan\b': 'InsurancePlan',
        r'\bnetwork\b': 'Organization',  # Networks are Organizations in Plan-Net
        r'\bprovider\b': 'Practitioner',  # Providers are often Practitioners
    }
    
    for pattern, resource in patterns.items():
        if re.search(pattern, requirement_text) and resource not in mentioned_resources:
            mentioned_resources.append(resource)
    
    return mentioned_resources

def parse_requirements_file(file_path: str) -> List[Dict[str, str]]:
    """
    Parse an INCOSE requirements markdown file into a structured list of requirements
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
    capability_info = extract_relevant_capability_chunks(requirement, capability_statement)
    
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
            capability_statement = parse_capability_statement_by_chunks(capability_statement_file)
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
