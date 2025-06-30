# FHIR Inferno Test Generator
import re
import os
import logging
import time
import json
import httpx
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from collections import defaultdict

import pandas as pd
from dotenv import load_dotenv


import prompt_utils


# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Constants
CURRENT_DIR = Path.cwd()  # Current working directory
#OUTPUT_DIR = os.path.join(CURRENT_DIR, 'test_output')
PROJECT_ROOT = CURRENT_DIR.parent  # Go up one level to project root
TEST_GEN_PATH = PROJECT_ROOT / "prompts" / "test_gen.md"

# System prompts for test generation
INFERNO_TEST_SYSTEM_PROMPT = """You are a specialized FHIR testing engineer with expertise in healthcare interoperability.
Your task is to convert test specifications from a test plan into executable Ruby tests using the Inferno testing framework.
You will generate valid, working Ruby code that follows Inferno test patterns and best practices, and uses the Inferno domain specific language."""

def get_inferno_test_generation_prompt(test_specification: str, requirement_id: str, module_name: str, inferno_guidance: str, dsl_guidance: str) -> str:
    """
    Load the Inferno test generation prompt from file and format it with test details
    
    Args:
        test_specification: The test specification content
        requirement_id: The ID of the requirement
        module_name: The name of the module
        inferno_guidance: The Inferno guidance
        
    Returns:
        str: The formatted prompt for the LLM
    """
    return prompt_utils.load_prompt(
        TEST_GEN_PATH,
        test_specification=test_specification,
        requirement_id=requirement_id,
        module_name=module_name,
        inferno_guidance=inferno_guidance, 
        dsl_guidance=dsl_guidance
    )

def parse_test_plan(file_path: str) -> Dict[str, Any]:
    """
    Parse a consolidated test plan into sections and requirements
    focusing on the main requirements
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Initialize empty sections dictionary
    sections = {}
    
    # First try to extract sections from the TOC
    toc_pattern = r'## Table of Contents\n(.*?)(?:\n## |\n# |\Z)'
    toc_match = re.search(toc_pattern, content, re.DOTALL)
    
    if toc_match:
        toc_content = toc_match.group(1)
        # Extract section names from the TOC
        section_pattern = r'- \[(.*?)\]'
        section_matches = re.findall(section_pattern, toc_content)
        
        # Only use top-level sections (not the REQ items)
        top_level_sections = [s for s in section_matches if not s.startswith('REQ-')]
        
        # Create section entries for each section found
        for section_name in top_level_sections:
            clean_section_name = section_name.strip()
            section_id = clean_section_name.lower().replace(' ', '-')
            sections[clean_section_name] = {
                'id': section_id,
                'name': clean_section_name,
                'content': "",
                'requirements': []
            }
    
    # If no sections found in TOC, try to find sections from the document headings
    if not sections:
        # Look for section headers (##) that are not part of the TOC
        section_pattern = r'## ([^\n#]+)(?=\n(?!## Table of Contents))'
        section_matches = re.findall(section_pattern, content)
        
        for section_name in section_matches:
            clean_section_name = section_name.strip()
            # Skip if this is a "Test Specification" section
            if "Test Specification" in clean_section_name:
                continue
                
            section_id = clean_section_name.lower().replace(' ', '-')
            sections[clean_section_name] = {
                'id': section_id,
                'name': clean_section_name,
                'content': "",
                'requirements': []
            }
    
    # Find all requirement headers in the document
    req_pattern = r'### (REQ-\d+): (.*?)\n\n\*\*Description\*\*: "(.*?)"\n\n\*\*Actor\*\*: (.*?)\n\n\*\*Conformance\*\*: (.*?)(?:\n\n|$)'
    req_matches = re.findall(req_pattern, content, re.DOTALL)
    
    print(f"Found {len(req_matches)} potential requirements")
    
    # Process each requirement
    for req_id, req_title, req_desc, req_actor, req_conf in req_matches:
        print(f"Processing requirement: {req_id}")
        
        # Find the full test specification for this requirement
        test_spec_pattern = f"# Test Specification for {req_id}(.*?)(?:---|\\n## |$)"
        test_spec_match = re.search(test_spec_pattern, content, re.DOTALL)
        test_spec = test_spec_match.group(1).strip() if test_spec_match else ""
        
        # Try to determine which section this requirement belongs to
        assigned_to_section = False
        
        # First try to find the requirement in one of the identified sections
        for section_name, section in sections.items():
            section_start = content.find(f"## {section_name}")
            if section_start == -1:
                continue
                
            # Find the next section to determine where this section ends
            next_section_start = len(content)
            for other_section in sections.keys():
                if other_section != section_name:
                    other_start = content.find(f"## {other_section}", section_start + len(section_name))
                    if other_start > section_start and other_start < next_section_start:
                        next_section_start = other_start
            
            # Extract the content of this section
            section_content = content[section_start:next_section_start]
            
            if f"### {req_id}" in section_content:
                # This requirement belongs to this section
                requirement = {
                    'id': req_id,
                    'title': req_title.strip(),
                    'description': req_desc.strip(),
                    'actor': req_actor.strip(),
                    'conformance': req_conf.strip(),
                    'full_content': f"### {req_id}: {req_title}\n\n**Description**: \"{req_desc}\"\n\n**Actor**: {req_actor}\n\n**Conformance**: {req_conf}",
                    'full_spec': test_spec,
                    'section': section_name,
                    'testability': 'Automatic'  # Default value
                }
                
                sections[section_name]['requirements'].append(requirement)
                print(f"Added requirement {req_id} to section {section_name}")
                assigned_to_section = True
                break
        
        # If can't find the requirement in any sections,
        # create a section based on the actor if it doesn't exist already
        if not assigned_to_section:
            actor = req_actor.strip()
            if not actor:
                actor = "Unknown Actor"
                
            if actor not in sections:
                section_id = actor.lower().replace(' ', '-')
                sections[actor] = {
                    'id': section_id,
                    'name': actor,
                    'content': "",
                    'requirements': []
                }
            
            requirement = {
                'id': req_id,
                'title': req_title.strip(),
                'description': req_desc.strip(),
                'actor': actor,
                'conformance': req_conf.strip(),
                'full_content': f"### {req_id}: {req_title}\n\n**Description**: \"{req_desc}\"\n\n**Actor**: {req_actor}\n\n**Conformance**: {req_conf}",
                'full_spec': test_spec,
                'section': actor,
                'testability': 'Automatic'  # Default value
            }
            
            sections[actor]['requirements'].append(requirement)
            print(f"Added requirement {req_id} to actor-based section {actor}")
    
    # Remove empty sections
    sections = {k: v for k, v in sections.items() if v['requirements']}
    
    return sections

def get_inferno_guidance() -> str:
    """
    Load the Inferno test writing guidance document
    
    Returns:
        String containing Inferno test development guidance
    """
    guidance_path = PROJECT_ROOT / "test_kit_dev" / "inferno-guidance.md"
    
    with open(guidance_path, 'r') as f:
        return f.read()
    

def get_dsl_guidance() -> str:
    """
    Load the Inferno dsl guidance document
    
    Returns:
        String containing Inferno dsl guidance
    """
    guidance_path = PROJECT_ROOT / "test_kit_dev" / "dsl-guidance.md"
    
    with open(guidance_path, 'r') as f:
        return f.read()
    

def determine_test_groups(sections: Dict[str, Dict[str, Any]], expected_actors: List[str]) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    """
    Group test specifications based on the sections and actors from the test plan
    
    Args:
        sections: Dictionary of sections from the parsed test plan
        expected_actors: List of expected actors from user input
        
    Returns:
        Nested dictionary of grouped test specifications
    """
    # First, group by actor
    actor_groups = defaultdict(list)
    
    # Create a mapping from normalized actor names to expected actor names
    actor_mapping = {actor.lower().replace(' ', '_'): actor for actor in expected_actors}
    
    # Collect all requirements across all sections
    for section_name, section in sections.items():
        for req in section['requirements']:
            # Use the exact actor name from the requirement
            actor = req['actor'].strip()
            if not actor:
                actor = "Unknown Actor"
            else:
                # Try to match with expected actors (case-insensitive)
                actor_lower = actor.lower().replace(' ', '_')
                if actor_lower in actor_mapping:
                    actor = actor_mapping[actor_lower]
            
            # Store the requirement with its section information
            req_with_section = req.copy()
            req_with_section['section_name'] = section_name
            req_with_section['section_id'] = section['id']
            
            actor_groups[actor].append(req_with_section)
    
    # Only include actors that have requirements
    result_groups = {}
    for actor, reqs in actor_groups.items():
        if reqs:  # Only include non-empty actor groups
            if actor not in result_groups:
                result_groups[actor] = {}
            
            # Group by original section
            section_groups = defaultdict(list)
            for req in reqs:
                section_groups[req['section_name']].append(req)
            
            # Add the section groups to the result
            result_groups[actor] = dict(section_groups)
    
    return result_groups


def validate_test_with_llm(llm_clients, api_type, test_code, inferno_guidance, dsl_guidance):
    """Use LLM to check and correct common issues in generated test code."""
    
    validation_prompt = f"""
    Review this Inferno test code for common issues and fix them:
    
    Property usage:
       - The 'links' property can ONLY be used in a TestSuite, not in TestGroups or individual Tests
       - Check proper use of 'test from:' vs 'group from:':
         * Use 'test from:' only for individual Test objects
         * Use 'group from:' for TestGroup objects
         
    Input declarations:
       - Ensure each test explicitly declares all inputs it uses with the `input` method
       - Don't use server_url or access_token without declaring them as inputs
       - Use valid input types (see guidance below; e.g., text, textarea, radio, checkbox, oauth_credentials)     
   
   FHIR client usage:
       - Never create FHIR clients manually with 'FHIR::Client.new()' 
       - Always use the Inferno DSL's 'fhir_client' block
       - Do not use non-existent methods like 'use_additional_headers='
    
    HTTP and FHIR requests:
       - Never use direct HTTP methods like 'get', 'post', etc. - use the Inferno DSL methods instead
       - Use proper FHIR client methods - 'fhir_get_capability_statement' instead of 'get capability_statement_url'
       - NEVER redefine the 'response' variable which is automatically created by Inferno
       
    ID references:
    - Ensure test/group IDs match those in the referenced files
    - Don't reference filename-based IDs, but use the actual defined ID in the referenced file
    - Example: If 'req_XX_test.rb' contains a group with ID `:example_text`, 
        reference that ID, not `:req_XX_test`

    Response handling:
       - Use hash syntax for response access: response[:code], response[:body], etc.
       - Don't use dot notation like response.code or response.body
       - For headers, use response[:headers] and iterate through the array of headers
       - Fix patterns like 'response.headers['www-authenticate']' to use proper header access
    
    Assertion patterns:
       - Use assertions instead of exceptions for failures
       - Do not use rescue blocks for error handling in tests
       - Never rescue StandardError in test implementations
    
    Request management:
        - When using 'uses_request', ensure a previous test has declared 'makes_request' with the same name
        - Ensure proper request naming and reference
        
    Resources: 
        - Only test resources specified in the test plan - don't add tests for resources not mentioned
    
    Here's the test code:
    ```ruby
    {test_code}
    ```
    Please ensure the code is valid Ruby and follows the below Inferno best practices, using the Inferno domain specific language.
    {dsl_guidance}
    
    Return ONLY the corrected code without explanations.
    """
    # Add token counting
    actual_tokens = llm_clients.count_tokens(validation_prompt, api_type)
    logger.info(f"Validation for test: Sending {actual_tokens} tokens to {api_type} API")
    
    # Check if need to truncate the guidance to fit within token limits
    if actual_tokens > 70000:  # Assuming a high limit
        logger.warning(f"Validation prompt exceeds token limit ({actual_tokens})")
        
    
    corrected_code = llm_clients.make_llm_request(
        api_type, 
        validation_prompt, 
        "You are an expert Ruby developer specialized in FHIR Inferno testing.", 
    )
    
    # Clean up any markdown formatting
    if corrected_code.startswith('```ruby'):
        corrected_code = re.sub(r'^```ruby\n', '', corrected_code)
        corrected_code = re.sub(r'\n```$', '', corrected_code)
    elif corrected_code.startswith('```'):
        corrected_code = re.sub(r'^```\n', '', corrected_code)
        corrected_code = re.sub(r'\n```$', '', corrected_code)
    
    return corrected_code

def generate_tests_for_section(
    llm_clients, 
    api_type: str,
    section: Dict[str, Any],
    inferno_guidance: str,
    dsl_guidance: str,
    module_name: str,
    max_input_token_limit: int = 16000
):
    """
    Generate tests for an entire section or individual requirements based on token limits
    
    Args:
        client: The API client
        api_type: API type (claude, gemini, gpt)
        section: Section dictionary containing requirements
        dsl_guidance: Inferno test development guidance
        module_name: Name of the module for the test
        rate_limit_func: Function to check rate limits
        max_input_token_limit: Maximum tokens for the model
        
    Returns:
        Dictionary mapping requirement IDs to generated tests
    """
    logger.info(f"Generating tests for section: {section['name']}")

    # First, try to generate tests for the entire section
    if len(section['requirements']) > 1:
        # Construct a prompt for the entire section
        section_prompt = f"""
        Generate Inferno tests for the following section of requirements from a FHIR implementation guide.
        
        Section: {section['name']}
        
        Requirements:
        {section['content']}
        
        For each requirement, create a separate Inferno test class following the naming convention:
        - Class name: {module_name}[Actor][Resource][REQ-ID]Test
        - File name: req_[id]_test.rb
        
        Module Name: {module_name}
        
        Follow this Inferno development guidance:
        {dsl_guidance}
        
        Return the Ruby code for each test implementation, separated by clear markers indicating the requirement ID.
        """
        
        # Estimate token count (rough approximation)
        estimated_tokens = len(section_prompt) / 4  # Approximate 4 chars per token
        actual_tokens = llm_clients.count_tokens(section_prompt, api_type)
        logger.info(f"Sending {actual_tokens} tokens to {api_type} API (limit: {max_input_token_limit})")
        
        if estimated_tokens < max_input_token_limit:
            try:
                logger.info(f"Attempting to generate tests for entire section: {section['name']}")
                response = llm_clients.make_llm_request( 
                    api_type, 
                    section_prompt, 
                    sys_prompt=INFERNO_TEST_SYSTEM_PROMPT 
                )
                
                # Parse the response to extract individual tests
                tests = {}
                current_req = None
                current_test = []
                
                for line in response.split('\n'):
                    # Look for markers indicating requirement boundaries
                    req_marker = re.search(r'(REQ-\d+)', line)
                    if req_marker and ("Test for" in line or "Implementation for" in line or "# Requirement" in line):
                        if current_req and current_test:
                            tests[current_req] = '\n'.join(current_test)
                            current_test = []
                        
                        current_req = req_marker.group(1)
                    
                    if current_req:
                        current_test.append(line)
                
                if current_req and current_test:
                    tests[current_req] = '\n'.join(current_test)
                
                # If successfully parsed tests for all requirements, return them
                if len(tests) == len(section['requirements']):
                    logger.info(f"Successfully generated tests for all requirements in section: {section['name']}")
                    return tests
                
                logger.warning(f"Generated tests for only {len(tests)} of {len(section['requirements'])} requirements in section: {section['name']}")
                # Continue to individual requirement processing
            
            except Exception as e:
                logger.warning(f"Failed to generate tests for entire section: {str(e)}")
                # Continue to individual requirement processing
    
    # If section-level generation failed or wasn't attempted, generate tests for individual requirements
    tests = {}
    for requirement in section['requirements']:
        try:
            logger.info(f"Generating test for requirement: {requirement['id']}")
            
            # Prepare the prompt for this requirement with full context
            req_prompt = get_inferno_test_generation_prompt(
                test_specification=requirement['full_content'],
                requirement_id=requirement['id'],
                module_name=module_name,
                inferno_guidance=inferno_guidance,
                dsl_guidance=dsl_guidance
            )
            actual_tokens = llm_clients.count_tokens(req_prompt, api_type)
            logger.info(f"Requirement {requirement['id']}: Sending {actual_tokens} tokens to {api_type} API (limit: {max_input_token_limit})")
        
            # Generate the test
            test_code = llm_clients.make_llm_request(
                api_type, 
                req_prompt, 
                INFERNO_TEST_SYSTEM_PROMPT, 
            )
            
            # Clean up any markdown formatting
            if test_code.startswith('```ruby'):
                test_code = re.sub(r'^```ruby\n', '', test_code)
                test_code = re.sub(r'\n```$', '', test_code)
            elif test_code.startswith('```'):
                test_code = re.sub(r'^```\n', '', test_code)
                test_code = re.sub(r'\n```$', '', test_code)
            
            tests[requirement['id']] = test_code
            logger.info(f"Successfully generated test for requirement: {requirement['id']}")
            
        except Exception as e:
            logger.error(f"Error generating test for requirement {requirement['id']}: {str(e)}")
    
    validated_tests = {}
    for req_id, test_code in tests.items():
        try:
            logger.info(f"Validating test for requirement: {req_id}")
            validated_code = validate_test_with_llm(
                llm_clients, 
                api_type, 
                test_code, 
                inferno_guidance,
                dsl_guidance
            )
            validated_tests[req_id] = validated_code
            logger.info(f"Successfully validated test for requirement: {req_id}")
        except Exception as e:
            logger.warning(f"Error validating test for {req_id}: {str(e)}")
            # Fall back to original if validation fails
            validated_tests[req_id] = test_code
    
    return validated_tests

def create_file_structure(grouped_tests: Dict[str, Dict[str, List[Dict[str, Any]]]], module_name: str, output_dir: str):
    """
    Create the file structure for the Inferno tests
    
    Args:
        grouped_tests: Nested dictionary of grouped test specs
        module_name: Name of the module for the tests
        output_dir: Directory for output files
        
    Returns:
        Dictionary mapping test specs to file paths
    """
    # Create base directories
    module_dir = os.path.join(output_dir, module_name.lower())
    os.makedirs(module_dir, exist_ok=True)
    
    # Create test group directories
    test_file_map = {}
    
    for actor, resource_groups in grouped_tests.items():
        actor_dir = os.path.join(module_dir, actor.lower())
        os.makedirs(actor_dir, exist_ok=True)
        
        for resource, test_specs in resource_groups.items():
            resource_dir = os.path.join(actor_dir, resource.lower().replace('-', '_').replace(' ', '_'))
            os.makedirs(resource_dir, exist_ok=True)
            
            for spec in test_specs:
                # Create a file name based on the requirement ID
                req_id = spec['id'].lower().replace('-', '_')
                file_name = f"{req_id}_test.rb"
                file_path = os.path.join(resource_dir, file_name)
                
                test_file_map[spec['id']] = file_path
    
    return test_file_map

def extract_test_id_from_file(file_path: str) -> str:
    """
    Extract the actual ID defined in a test file using the 'id :xyz' pattern.
    
    Args:
        file_path: Path to the Ruby test file
        
    Returns:
        The extracted ID or None if not found
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            # Look for 'id :some_id' or 'id:some_id' pattern
            id_match = re.search(r'id\s*:([a-zA-Z0-9_]+)', content)
            if id_match:
                return id_match.group(1)
    except Exception as e:
        logger.warning(f"Error extracting ID from {file_path}: {str(e)}")
    return None


def extract_test_data(module_dir: str) -> Dict[str, Dict[str, Any]]:
    """
    Scan all test files in the module directory and extract their actual IDs and metadata.
    
    Args:
        module_dir: Path to the module directory
        
    Returns:
        Dictionary mapping file paths to metadata about the test files
    """
    test_data = {}
    
    # Walk through all directories in the module
    for root, dirs, files in os.walk(module_dir):
        for file in files:
            if file.endswith('_test.rb'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, module_dir)
                
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        
                        # Extract class type (TestGroup or Test)
                        class_type_match = re.search(r'class\s+\w+\s+<\s+Inferno::(\w+)', content)
                        class_type = class_type_match.group(1) if class_type_match else 'Unknown'
                        
                        # Extract ID
                        id_match = re.search(r'id\s*:([a-zA-Z0-9_]+)', content)
                        actual_id = id_match.group(1) if id_match else None
                        
                        # Extract title
                        title_match = re.search(r'title\s+[\'"]([^\'"]+)[\'"]', content)
                        title = title_match.group(1) if title_match else 'Unknown Test'
                        
                        # Store the data
                        test_data[relative_path] = {
                            'id': actual_id,
                            'type': class_type,
                            'title': title,
                            'file_path': relative_path
                        }
                except Exception as e:
                    logger.warning(f"Error processing file {file_path}: {str(e)}")
    
    return test_data


def create_module_structure(test_data: Dict[str, Dict[str, Any]]) -> str:
    """
    Create a structured representation of the module for the LLM to use.
    
    Args:
        test_data: Dictionary of test file data
        
    Returns:
        String describing the module structure
    """
    structure = "Module Structure:\n"
    
    # Group by directories
    dir_structure = defaultdict(list)
    for file_path, data in test_data.items():
        dir_name = os.path.dirname(file_path)
        dir_structure[dir_name].append((file_path, data))
    
    # Create a hierarchical description
    for dir_name, files in sorted(dir_structure.items()):
        structure += f"- Directory: {dir_name}\n"
        for file_path, data in sorted(files):
            structure += f"  - File: {os.path.basename(file_path)}\n"
            structure += f"    - Type: {data['type']}\n"
            structure += f"    - ID: {data['id'] or 'None'}\n"
            structure += f"    - Title: {data['title']}\n"
    
    return structure


def generate_landing_file_with_llm(
    llm_clients,
    api_type: str,
    module_name_camel: str,
    module_name_snake: str,
    test_data: Dict[str, Dict[str, Any]],
    structure: str,
) -> str:
    """
    Use an LLM to generate the main module file with proper ID references.
    
    Args:
        client: The API client
        api_type: API type (claude, gemini, gpt)
        module_name_camel: CamelCase module name
        module_name_snake: snake_case module name
        test_data: Dictionary of test file data
        structure: String describing the module structure
        rate_limit_func: Function to check rate limits
        
    Returns:
        Generated module file content
    """
    # Define a system prompt for the LLM
    system_prompt = """You are an expert Ruby developer specializing in FHIR Inferno test development.
Your task is to create a main module file for an Inferno test suite that correctly references all test groups."""
    
    # Create the user prompt
    user_prompt = f"""
Generate a main module file for an Inferno test suite called '{module_name_camel}' with a snake_case name of '{module_name_snake}'.

The test suite should have:
1. A proper module definition with a TestSuite class
2. Configuration for a FHIR client with a URL input
3. All required imports for the test files
4. A properly structured hierarchy of groups that reflects the directory structure
5. Correct references to test groups using their actual IDs, not their filenames

Here is the structure of the test files:
{structure}

CRITICAL REQUIREMENTS:
1. Each 'require_relative' statement should reference the actual file path
2. When using 'group from:', ALWAYS use the actual ID from the file (what follows 'id :'), NOT the filename
3. Organize the groups to match the directory structure
4. Configure the FHIR client at the TestSuite level
5. Do not require 'inferno/dsl/test_suite' or other non-existent libraries
6. The main module file should be named '{module_name_snake}.rb'

Return ONLY the Ruby code for the main module file, with no explanations.
"""
    
    # Call the LLM
    landing_file_content = llm_clients.make_llm_request(
        api_type,
        user_prompt,
        sys_prompt=system_prompt
    )
    
    # Clean up any markdown formatting
    if landing_file_content.startswith('```ruby'):
        landing_file_content = re.sub(r'^```ruby\n', '', landing_file_content)
        landing_file_content = re.sub(r'\n```$', '', landing_file_content)
    elif landing_file_content.startswith('```'):
        landing_file_content = re.sub(r'^```\n', '', landing_file_content)
        landing_file_content = re.sub(r'\n```$', '', landing_file_content)
    
    return landing_file_content

def generate_inferno_test_kit(
    llm_clients,
    api_type: str,
    test_plan_file: str,
    module_name: str = "PlanNet",
    output_dir: str = OUTPUT_DIR,
    expected_actors: List[str] = None
) -> Dict[str, Any]:
    """
    Process a test plan and generate an Inferno test kit
    
    Args:
        api_type: API type (claude, gemini, gpt)
        test_plan_file: Path to test plan markdown file
        guidance_file: Path to Inferno guidance file (optional)
        module_name: Name of the module for the tests
        output_dir: Directory for output files
        expected_actors: List of expected actors in the test plan
        
    Returns:
        Dictionary containing statistics and paths
    """
    logger.info(f"Starting Inferno test generation with {api_type} for {module_name}")
    
    # Initialize API clients and rate limiters
    #config = clients.config[api_type]
  
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Standardize module name for Ruby
    module_name_snake = module_name.lower().replace('-', '_').replace(' ', '_')
    module_name_camel = ''.join(word.capitalize() for word in module_name.split())
    
    # Create module subdirectory
    module_subdir = os.path.join(output_dir, module_name_snake)
    os.makedirs(module_subdir, exist_ok=True)
    
    # Set default actors if none provided
    if not expected_actors:
        expected_actors = ["Health Plan API Actor", "Application Actor"]
    
    try:
        # Parse test plan into sections
        sections = parse_test_plan(test_plan_file)
        logger.info(f"Parsed test plan into {len(sections)} sections")
        
        # Count total requirements
        total_requirements = sum(len(section['requirements']) for section in sections.values())
        logger.info(f"Found {total_requirements} total requirements")
        
        # Get Inferno test writing guidance
        #if guidance_file and os.path.exists(guidance_file):
            #with open(guidance_file, 'r') as f:
                #inferno_guidance = f.read()
            #logger.info(f"Loaded Inferno guidance from {guidance_file}")
        #else:
        #inferno_guidance = get_inferno_guidance()
        #logger.info("Using default Inferno guidance")
        #guidance_tokens = llm_clients.count_tokens(inferno_guidance, api_type)
        #logger.info(f"Inferno guidance size: {guidance_tokens} tokens")
        
        # Get DSL guidance
        dsl_guidance = get_dsl_guidance()
        logger.info("Loaded Inferno DSL guidance")
        dsl_tokens = llm_clients.count_tokens(dsl_guidance, api_type)
        

        # Generate tests by section
        all_tests = {}
        for section_name, section in sections.items():
            logger.info(f"Processing section: {section_name} with {len(section['requirements'])} requirements")
            
            # Skip empty sections
            if not section['requirements']:
                continue
                
            # Generate tests for this section
            section_tests = generate_tests_for_section(
                llm_clients, 
                api_type, 
                section, 
                #inferno_guidance, 
                dsl_guidance,
                module_name_camel, 
                70000
            )
            
            # Add to our collection
            all_tests.update(section_tests)
            
            # Add delay between sections
            time.sleep(llm_clients.config[api_type]["delay_between_batches"])
            
        logger.info(f"Generated tests for {len(all_tests)} requirements")
        
        # Group requirements by actor and section (original groups from test plan)
        grouped_reqs = determine_test_groups(sections, expected_actors)
        
        # Write test files to the module subdirectory
        file_paths = {}
        for actor, section_groups in grouped_reqs.items():
            # Skip actors with no tests
            if not section_groups:
                continue
                
            actor_safe = re.sub(r'[^a-zA-Z0-9_]', '_', actor.lower())
            actor_dir = os.path.join(module_subdir, actor_safe)
            
            # Only create actor directory if it has at least one test
            has_tests = False
            for section_name, reqs in section_groups.items():
                for req in reqs:
                    if req['id'] in all_tests:
                        has_tests = True
                        break
                if has_tests:
                    break
            
            if not has_tests:
                continue
                
            os.makedirs(actor_dir, exist_ok=True)
            
            for section_name, reqs in section_groups.items():
                # Skip empty sections or sections with no generated tests
                has_section_tests = False
                for req in reqs:
                    if req['id'] in all_tests:
                        has_section_tests = True
                        break
                
                if not has_section_tests:
                    continue
                    
                section_safe = re.sub(r'[^a-zA-Z0-9_]', '_', section_name.lower())
                section_dir = os.path.join(actor_dir, section_safe)
                os.makedirs(section_dir, exist_ok=True)
                
                for req in reqs:
                    # Skip requirements we couldn't generate tests for
                    if req['id'] not in all_tests:
                        continue
                        
                    file_name = f"{req['id'].lower().replace('-', '_')}_test.rb"
                    file_path = os.path.join(section_dir, file_name)
                    
                    with open(file_path, 'w') as f:
                        f.write(all_tests[req['id']])
                    
                    file_paths[req['id']] = file_path
                    logger.info(f"Wrote test for {req['id']} to {file_path}")
        
        # Extract data from all test files for LLM-based module file generation
        logger.info("Collecting test data for module file generation")
        test_data = extract_test_data(module_subdir)
        
        # Create structured representation for the LLM
        structure = create_module_structure(test_data)
        logger.info("Created structure representation of test files")
        
        # Generate the module file using an LLM
        logger.info("Generating module file with LLM")
        module_content = generate_landing_file_with_llm(
            llm_clients,
            api_type,
            module_name_camel,
            module_name_snake,
            test_data,
            structure
        )
        
        # Write the module file
        module_file_path = os.path.join(output_dir, f"{module_name_snake}.rb")
        with open(module_file_path, 'w') as f:
            f.write(module_content)
        logger.info(f"Wrote module file to {module_file_path}")
        
        return {
            "total_sections": len(sections),
            "total_requirements": total_requirements,
            "generated_tests": len(all_tests),
            "module_dir": module_subdir,
            "module_file": module_file_path
        }
        
    except Exception as e:
        logger.error(f"Error generating Inferno tests: {str(e)}")
        raise