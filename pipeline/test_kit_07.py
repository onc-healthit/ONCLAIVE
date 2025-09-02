"""
FHIR Inferno Test Generator

This module converts FHIR Implementation Guide test plans into executable Ruby tests 
using the Inferno testing framework.

Features:
- Parse consolidated test plans into structured requirements
- Generate Ruby test code using LLM analysis
- Optional validation and fixing of generated tests
- Create proper Inferno module structure
- Organize tests by functional sections
- Generate main module files with correct references
- Handle large test suites without truncation

Usage:
    from plan_to_tests import generate_inferno_test_kit
    
    # Generate test kit with validation
    result = generate_inferno_test_kit(
        client_instance=client,
        api_type="claude",
        test_plan_file="test_plan.md",
        ig_name="US Core",
        enable_validation=True  # Optional LLM review
    )
"""

import re
import os
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from collections import defaultdict

import prompt_utils

# Constants
CURRENT_DIR = Path.cwd()
OUTPUT_DIR = os.path.join(CURRENT_DIR, 'test_output')
PROJECT_ROOT = CURRENT_DIR.parent
TEST_GEN_PATH = PROJECT_ROOT / "prompts" / "test_gen.md"

# System prompts for test generation
INFERNO_TEST_SYSTEM_PROMPT = """You are a specialized FHIR testing engineer with expertise in healthcare interoperability.
Your task is to convert test specifications from a test plan into executable Ruby tests using the Inferno testing framework.
You will generate valid, working Ruby code that follows Inferno test patterns and best practices, and uses the Inferno domain specific language."""

# Setup logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def parse_test_plan(file_path: str) -> Dict[str, Any]:
    """
    Parse a consolidated test plan into sections and requirements.
    
    Args:
        file_path: Path to the test plan markdown file
        
    Returns:
        Dictionary mapping section names to their requirements and metadata
        
    Note:
        Expects test plan format with Table of Contents, sections marked with ##,
        and requirements in format ### REQ-XXX: Title followed by structured fields
    """
    with open(file_path, 'r', encoding='utf-8') as f:
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
    
    # Extract requirements with updated regex pattern
    req_pattern = r'### (REQ-\d+): (.*?)\n\n\*\*Text\*\*: "(.*?)"\n\n\*\*Context\*\*: (.*?)\n\n\*\*Actor\*\*: (.*?)\n\n\*\*Conformance\*\*: (.*?)(?:\n\n|# Test Specification|\Z)'
    req_matches = re.findall(req_pattern, content, re.DOTALL)
    
    print(f"Found {len(req_matches)} requirements in test plan")
    
    # Process each requirement
    for req_id, req_title, req_text, req_context, req_actor, req_conf in req_matches:
        print(f"Processing requirement: {req_id}")
        
        # Find the full test specification for this requirement
        test_spec_pattern = f"# Test Specification for {req_id}(.*?)(?=### REQ-|\\Z)"
        test_spec_match = re.search(test_spec_pattern, content, re.DOTALL)
        test_spec = test_spec_match.group(1).strip() if test_spec_match else ""
        
        # Try to determine which section this requirement belongs to
        assigned_to_section = False
        
        # First try to find the requirement in one of the identified sections
        for section_name, section in sections.items():
            # Look for section headers that might contain this requirement
            section_pattern = f"<a id='{section['id']}'></a>\n\n## {section_name}"
            section_start = content.find(section_pattern)
            
            # If we can't find the exact pattern, try simpler approach
            if section_start == -1:
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
                    'text': req_text.strip(),
                    'context': req_context.strip(),
                    'actor': req_actor.strip(),
                    'conformance': req_conf.strip(),
                    'full_content': f"### {req_id}: {req_title}\n\n**Text**: \"{req_text}\"\n\n**Context**: {req_context}\n\n**Actor**: {req_actor}\n\n**Conformance**: {req_conf}",
                    'full_spec': test_spec,
                    'section': section_name,
                    'testability': 'Automatic'
                }
                
                sections[section_name]['requirements'].append(requirement)
                print(f"Added requirement {req_id} to section {section_name}")
                assigned_to_section = True
                break
        
        # If can't find the requirement in any sections, create actor-based section
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
                'text': req_text.strip(),
                'context': req_context.strip(),
                'actor': actor,
                'conformance': req_conf.strip(),
                'full_content': f"### {req_id}: {req_title}\n\n**Text**: \"{req_text}\"\n\n**Context**: {req_context}\n\n**Actor**: {req_actor}\n\n**Conformance**: {req_conf}",
                'full_spec': test_spec,
                'section': actor,
                'testability': 'Automatic'
            }
            
            sections[actor]['requirements'].append(requirement)
            print(f"Added requirement {req_id} to actor-based section {actor}")
    
    # Remove empty sections
    sections = {k: v for k, v in sections.items() if v['requirements']}
    
    print(f"Final sections: {list(sections.keys())}")
    for section_name, section in sections.items():
        print(f"  {section_name}: {len(section['requirements'])} requirements")
    
    return sections


def get_dsl_guidance() -> str:
    """
    Load the Inferno DSL guidance document.
    
    Returns:
        String containing Inferno DSL guidance for test development
    """
    guidance_path = PROJECT_ROOT / "pipeline" / "dsl-guidance.md"
    
    with open(guidance_path, 'r', encoding='utf-8') as f:
        return f.read()


def validate_test_with_llm(client_instance, api_type: str, test_code: str, dsl_guidance: str) -> str:
    """
    Use LLM to check and correct common issues in generated test code.
    
    Args:
        client_instance: LLM client instance
        api_type: Type of API to use
        test_code: Generated test code to validate
        dsl_guidance: Inferno DSL guidance document
        
    Returns:
        Corrected test code
    """
    validation_prompt = f"""
    Review this Inferno test code for common issues and fix them:
    
    FHIR Client Inheritance (CRITICAL):
       - TestGroups should NOT define their own fhir_client unless they need different authentication
       - TestGroups should NOT declare URL inputs - they inherit from the parent TestSuite
       - Only declare inputs that are specific to the test group (patient_id, specialty_code, etc.)
       - Remove any duplicate fhir_client blocks in TestGroups
       - Remove any duplicate URL input declarations in TestGroups
    
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

    SPECIFIC FIXES REQUIRED:
    1. Remove any fhir_client blocks from TestGroups unless they need different authentication
    2. Remove any URL input declarations from TestGroups
    3. Ensure TestGroups only declare inputs specific to their testing needs

    Please ensure the code is valid Ruby and follows the below Inferno best practices, using the Inferno domain specific language.
    {dsl_guidance}
    
    Return ONLY the corrected code without explanations.
    """
    
    # Add token counting for monitoring
    actual_tokens = client_instance.count_tokens(validation_prompt, api_type)
    logging.info(f"Validation request: {actual_tokens} tokens to {api_type} API")
    
    # Check if need to truncate the guidance to fit within token limits
    if actual_tokens > 70000:  # Conservative limit
        logging.warning(f"Validation prompt exceeds token limit ({actual_tokens}), truncating guidance")
        # Truncate guidance if needed
        truncated_guidance = dsl_guidance[:10000]  # Keep first 10k chars
        validation_prompt = validation_prompt.replace(dsl_guidance, truncated_guidance)
    
    corrected_code = client_instance.make_llm_request(
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


def generate_tests_for_section(client_instance, api_type: str, section: Dict[str, Any], dsl_guidance: str,
                              ig_name: str, max_input_token_limit: int = 16000, enable_validation: bool = True) -> Dict[str, str]:
    """
    Generate tests for an entire section or individual requirements.
    
    Args:
        client_instance: LLM client instance
        api_type: API type (claude, gemini, gpt)
        section: Section dictionary containing requirements
        dsl_guidance: Inferno test development guidance
        ig_name: Name of the module for the test
        max_input_token_limit: Maximum tokens for the model
        enable_validation: Whether to perform LLM validation of generated tests
        
    Returns:
        Dictionary mapping requirement IDs to generated test code
    """
    logging.info(f"Generating tests for section: {section['name']}")

    # First, try to generate tests for the entire section
    if len(section['requirements']) > 1:
        # Construct a prompt for the entire section
        section_prompt = f"""
        Generate Inferno tests for the following section of requirements from a FHIR implementation guide.
        
        Section: {section['name']}
        
        Requirements:
        {section['content']}
        
        For each requirement, create a separate Inferno test class following the naming convention:
        - Class name: {ig_name}[Actor][Resource][REQ-ID]Test
        - File name: req_[id]_test.rb
        
        Module Name: {ig_name}
        
        Follow this Inferno development guidance:
        {dsl_guidance}
        
        Return the Ruby code for each test implementation, separated by clear markers indicating the requirement ID.
        """
        
        # Estimate token count
        actual_tokens = client_instance.count_tokens(section_prompt, api_type)
        logging.info(f"Section-level generation: {actual_tokens} tokens to {api_type} API (limit: {max_input_token_limit})")
        
        if actual_tokens < max_input_token_limit:
            try:
                logging.info(f"Attempting to generate tests for entire section: {section['name']}")
                response = client_instance.make_llm_request( 
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
                    logging.info(f"Successfully generated tests for all requirements in section: {section['name']}")
                    return tests
                
                logging.warning(f"Generated tests for only {len(tests)} of {len(section['requirements'])} requirements in section: {section['name']}")
                # Continue to individual requirement processing
            
            except Exception as e:
                logging.warning(f"Failed to generate tests for entire section: {str(e)}")
                # Continue to individual requirement processing
    
    # Generate tests for individual requirements
    tests = {}
    for requirement in section['requirements']:
        try:
            logging.info(f"Generating test for requirement: {requirement['id']}")
            
            # Prepare the prompt for this requirement with full context
            req_prompt = prompt_utils.load_prompt(
                str(TEST_GEN_PATH),
                test_specification=requirement['full_content'],
                requirement_id=requirement['id'],
                ig_name=ig_name,
                dsl_guidance=dsl_guidance
            )
            actual_tokens = client_instance.count_tokens(req_prompt, api_type)
            logging.info(f"Requirement {requirement['id']}: {actual_tokens} tokens to {api_type} API")
        
            # Generate the test
            test_code = client_instance.make_llm_request(
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
            logging.info(f"Successfully generated test for requirement: {requirement['id']}")
            
        except Exception as e:
            logging.error(f"Error generating test for requirement {requirement['id']}: {str(e)}")
    
    # Optional validation step
    if enable_validation:
        logging.info("Starting LLM validation phase...")
        validated_tests = {}
        for req_id, test_code in tests.items():
            try:
                logging.info(f"Validating test for requirement: {req_id}")
                validated_code = validate_test_with_llm(
                    client_instance, 
                    api_type, 
                    test_code, 
                    dsl_guidance
                )
                validated_tests[req_id] = validated_code
                logging.info(f"Successfully validated test for requirement: {req_id}")
            except Exception as e:
                logging.warning(f"Error validating test for {req_id}: {str(e)}")
                # Fall back to original if validation fails
                validated_tests[req_id] = test_code
        return validated_tests
    else:
        logging.info("Skipping LLM validation phase (disabled)")
        return tests


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
                    with open(file_path, 'r', encoding='utf-8') as f:
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
                    logging.warning(f"Error processing file {file_path}: {str(e)}")
    
    return test_data


def create_module_structure(test_data: Dict[str, Dict[str, Any]], ig_name_snake: str) -> str:
    """
    Create a structured representation of the module for the LLM to use.
    
    Args:
        test_data: Dictionary of test file data
        ig_name_snake: The snake_case module name (e.g., 'plannet')
        
    Returns:
        String describing the module structure with correct require_relative paths
    """
    structure = "Module Structure:\n"
    
    # Group by directories
    dir_structure = defaultdict(list)
    for file_path, data in test_data.items():
        dir_name = os.path.dirname(file_path)
        dir_structure[dir_name].append((file_path, data))
    
    # Create a hierarchical description with corrected require_relative paths
    for dir_name, files in sorted(dir_structure.items()):
        structure += f"- Directory: {dir_name}\n"
        for file_path, data in sorted(files):
            # Create the correct require_relative path (include module folder)
            # Remove .rb extension for require_relative
            require_path = f"{ig_name_snake}/{file_path}".replace('.rb', '')
            
            structure += f"  - File: {os.path.basename(file_path)}\n"
            structure += f"    - Type: {data['type']}\n"
            structure += f"    - ID: {data['id'] or 'None'}\n"
            structure += f"    - Title: {data['title']}\n"
            structure += f"    - require_relative: '{require_path}'\n"
    
    return structure


def generate_landing_file_with_llm(client_instance, api_type: str, ig_name_camel: str, ig_name_snake: str,
                                  test_data: Dict[str, Dict[str, Any]], structure: str) -> str:
    """
    Use an LLM to generate the main module file with proper ID references.
    
    This addresses the truncation issue by using a more targeted approach for large test suites.
    """
    # For large test suites, break into chunks to avoid truncation
    total_tests = len(test_data)
    
    if total_tests > 50:  # If more than 50 tests, use chunked approach
        logging.info(f"Large test suite detected ({total_tests} tests), using chunked generation")
        return generate_large_module_file(client_instance, api_type, ig_name_camel, ig_name_snake, test_data, structure)
    
    # Standard approach for smaller test suites
    system_prompt = """You are an expert Ruby developer specializing in FHIR Inferno test development.
Your task is to create a main module file for an Inferno test suite that correctly references all test groups.
CRITICAL: The TestSuite should declare inputs ONCE and all TestGroups will inherit them automatically.
CRITICAL: require_relative paths must include the module folder name."""
    
    user_prompt = f"""
Generate a main module file for an Inferno test suite called '{ig_name_camel}' with a snake_case name of '{ig_name_snake}'.

The test suite should have:
1. A proper module definition with a TestSuite class
2. A mandatory ID declaration as the first property
3. ONE declaration of the FHIR server URL input (all groups will inherit this)
4. ONE FHIR client configuration (all groups will inherit this)
5. Optional OAuth credentials input for authenticated endpoints
6. All required imports for the test files
7. A properly structured hierarchy of groups that reflects the directory structure
8. Correct references to test groups using their actual IDs, not their filenames

CRITICAL REQUIREMENTS FOR INPUT MANAGEMENT:
- Declare the URL input ONLY in the TestSuite
- Declare OAuth credentials ONLY in the TestSuite
- All TestGroups will automatically inherit these inputs
- Do not repeat input declarations in the referenced test groups

CRITICAL REQUIREMENTS FOR FILE REFERENCES:
- ONLY include require_relative statements for files that actually exist
- ONLY include group from: statements for IDs that exist in the referenced files
- Each require_relative must include the module folder: require_relative '{ig_name_snake}/path/to/file'
- Each group from: must reference an actual ID defined in a test file

Here is the structure of the test files with correct require_relative paths:
{structure}

Return ONLY the Ruby code for the main module file, with no explanations.
"""
    
    # Call the LLM
    landing_file_content = client_instance.make_llm_request(
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


def generate_large_module_file(client_instance, api_type: str, ig_name_camel: str, ig_name_snake: str,
                              test_data: Dict[str, Dict[str, Any]], structure: str) -> str:
    """
    Generate module file for large test suites using chunked approach to avoid truncation.
    
    This method generates the module file in parts and combines them to ensure all tests are included.
    """
    logging.info("Using chunked approach for large module file generation")
    
    # First, generate the module header
    header_prompt = f"""
Generate the header and configuration section for an Inferno test suite called '{ig_name_camel}' with snake_case name '{ig_name_snake}'.

Include:
1. Module definition with TestSuite class
2. ID declaration
3. Title and description
4. FHIR server URL input declaration
5. OAuth credentials input (optional)
6. FHIR client configuration
7. FHIR resource validator configuration if needed

Return ONLY the Ruby code for the header section (module definition through fhir_resource_validator), ending with a comment "# Test groups will be added below".
"""
    
    module_header = client_instance.make_llm_request(
        api_type,
        header_prompt,
        "You are an expert Ruby developer specializing in FHIR Inferno test development."
    )
    
    # Clean up markdown formatting
    module_header = clean_markdown_formatting(module_header)
    
    # Generate require statements and group references
    require_statements = []
    group_references = []
    
    for file_path, data in test_data.items():
        if data['id']:  # Only include if ID exists
            require_path = f"{ig_name_snake}/{file_path}".replace('.rb', '')
            require_statements.append(f"require_relative '{require_path}'")
            group_references.append(f"    group from: :{data['id']}")
    
    # Combine all parts
    full_module = f"""{module_header}

    # Require all test files
{chr(10).join(f"    {req}" for req in require_statements)}

    # Reference all test groups
{chr(10).join(group_references)}
  end
end"""
    
    logging.info(f"Generated large module file with {len(require_statements)} requires and {len(group_references)} group references")
    
    return full_module


def clean_markdown_formatting(text: str) -> str:
    """Clean up markdown code block formatting from LLM responses."""
    if text.startswith('```ruby'):
        text = re.sub(r'^```ruby\n', '', text)
        text = re.sub(r'\n```', '', text)
    elif text.startswith('```'):
        text = re.sub(r'^```\n', '', text)
        text = re.sub(r'\n```', '', text)
    return text


def collect_alignment_data(module_file_path: str, module_dir: str, ig_name_snake: str) -> Dict[str, Any]:
    """
    Collect all alignment data for LLM review.
    
    Args:
        module_file_path: Path to the main module file
        module_dir: Directory containing test files
        ig_name_snake: Snake case module name
        
    Returns:
        Dictionary containing alignment analysis data
    """
    alignment_data = {
        'module_file_content': '',
        'module_file_path': module_file_path,
        'test_files': {},
        'require_statements': [],
        'group_references': [],
        'actual_files': [],
        'actual_group_ids': {},
        'ig_name': ig_name_snake
    }
    
    # Read module file
    try:
        with open(module_file_path, 'r', encoding='utf-8') as f:
            alignment_data['module_file_content'] = f.read()
    except Exception as e:
        alignment_data['error'] = f"Cannot read module file: {str(e)}"
        return alignment_data
    
    # Extract require_relative and group from: statements
    alignment_data['require_statements'] = re.findall(
        r"require_relative\s+['\"]([^'\"]+)['\"]", 
        alignment_data['module_file_content']
    )
    alignment_data['group_references'] = re.findall(
        r"group\s+from:\s*:([a-zA-Z0-9_]+)", 
        alignment_data['module_file_content']
    )
    
    # Collect all actual test files and their content
    for root, dirs, files in os.walk(module_dir):
        for file in files:
            if file.endswith('.rb'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, module_dir)
                
                # Create the expected require_relative path format
                expected_require_path = f"{ig_name_snake}/{relative_path}".replace('.rb', '')
                
                alignment_data['actual_files'].append({
                    'relative_path': relative_path,
                    'expected_require_path': expected_require_path
                })
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        alignment_data['test_files'][relative_path] = content
                        
                        # Extract group IDs from this file
                        group_ids = re.findall(r'id\s+:([a-zA-Z0-9_]+)', content)
                        if group_ids:
                            alignment_data['actual_group_ids'][relative_path] = group_ids
                            
                except Exception as e:
                    alignment_data['test_files'][relative_path] = f"ERROR: {str(e)}"
    
    return alignment_data


def llm_validate_alignment(client_instance, api_type: str, alignment_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Use LLM to validate and fix alignment issues.
    
    Args:
        client_instance: LLM client instance
        api_type: Type of API to use
        alignment_data: Collected alignment data
        
    Returns:
        Dictionary with validation results and corrected content
    """
    # Prepare alignment summary for LLM
    alignment_summary = f"""
MODULE FILE: {alignment_data['module_file_path']}
REQUIRE_RELATIVE STATEMENTS: {alignment_data['require_statements']}
GROUP FROM REFERENCES: {alignment_data['group_references']}

ACTUAL TEST FILES:
{chr(10).join(f"- {file['relative_path']}" for file in alignment_data['actual_files'])}

ACTUAL GROUP IDs FOUND:
{chr(10).join(f"- {file}: {ids}" for file, ids in alignment_data['actual_group_ids'].items())}
"""
    
    system_prompt = """You are an expert Ruby developer specializing in Inferno FHIR test suites. 
You need to analyze alignment between a main module file and its test files, then fix any issues."""
    
    user_prompt = f"""
Analyze this Inferno test suite for alignment issues between the main module file and test files:

{alignment_summary}

MAIN MODULE FILE CONTENT:
```ruby
{alignment_data['module_file_content']}
```

Check for these issues:
1. require_relative statements pointing to non-existent files
2. group from: references to non-existent group IDs  
3. test files that exist but aren't required
4. group IDs that exist but aren't referenced

Provide a corrected version of the main module file that:
- Only includes require_relative for files that actually exist
- Only includes group from: for group IDs that actually exist in the test files
- Adds any missing require_relative statements for existing test files
- Adds any missing group from: statements for existing group IDs
- Maintains proper Ruby syntax and structure
- Preserves the existing TestSuite structure and configuration

Return ONLY the corrected Ruby code for the main module file, with no explanations.
"""
    
    try:
        corrected_module_content = client_instance.make_llm_request(
            api_type,
            user_prompt,
            sys_prompt=system_prompt
        )
        
        # Clean up any markdown formatting
        corrected_module_content = clean_markdown_formatting(corrected_module_content)
        
        return {
            'success': True,
            'corrected_content': corrected_module_content,
            'original_content': alignment_data['module_file_content']
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'original_content': alignment_data['module_file_content']
        }


def detailed_llm_alignment_report(client_instance, api_type: str, alignment_data: Dict[str, Any]) -> str:
    """
    Generate a detailed alignment report using LLM analysis.
    
    Args:
        client_instance: LLM client instance
        api_type: Type of API to use
        alignment_data: Collected alignment data
        
    Returns:
        Detailed alignment report string
    """
    alignment_summary = f"""
REQUIRE_RELATIVE STATEMENTS: {alignment_data['require_statements']}
GROUP FROM REFERENCES: {alignment_data['group_references']}
ACTUAL TEST FILES: {[f['relative_path'] for f in alignment_data['actual_files']]}
ACTUAL GROUP IDs: {alignment_data['actual_group_ids']}
"""
    
    report_prompt = f"""
Analyze this Inferno test suite alignment data and create a detailed report:

{alignment_summary}

Provide a detailed analysis covering:
1. Missing files (required but don't exist)
2. Missing group IDs (referenced but don't exist)
3. Orphaned files (exist but not required)
4. Orphaned group IDs (exist but not referenced)
5. Overall alignment status
6. Recommendations for fixes

Format as a clear, structured report with sections and bullet points.
"""
    
    try:
        report = client_instance.make_llm_request(
            api_type,
            report_prompt,
            "You are an expert at analyzing software project structure and dependencies."
        )
        return report
    except Exception as e:
        return f"Error generating alignment report: {str(e)}"


def llm_validate_and_fix_alignment(client_instance, api_type: str, output_dir: str, ig_name: str) -> Dict[str, Any]:
    """
    Complete LLM-based alignment validation and fixing.
    
    Args:
        client_instance: LLM client instance
        api_type: Type of API to use
        output_dir: Output directory containing module file
        ig_name: Module name
        
    Returns:
        Dictionary with validation results and report
    """
    # Find the module file
    module_file = None
    for file in os.listdir(output_dir):
        if file.endswith('.rb') and ig_name.lower() in file.lower():
            module_file = os.path.join(output_dir, file)
            break
    
    if not module_file:
        return {
            'success': False,
            'error': 'Module file not found',
            'report': 'Could not locate main module file for alignment validation'
        }
    
    module_dir = os.path.join(output_dir, ig_name.lower())
    
    # Collect alignment data
    logging.info("Collecting alignment data for LLM analysis...")
    alignment_data = collect_alignment_data(module_file, module_dir, ig_name)
    
    if 'error' in alignment_data:
        return {
            'success': False,
            'error': alignment_data['error'],
            'report': f"Failed to collect alignment data: {alignment_data['error']}"
        }
    
    # Generate detailed report
    logging.info("Generating LLM alignment report...")
    detailed_report = detailed_llm_alignment_report(client_instance, api_type, alignment_data)
    
    # Get LLM fixes
    logging.info("Getting LLM alignment fixes...")
    fix_result = llm_validate_alignment(client_instance, api_type, alignment_data)
    
    if fix_result['success']:
        # Write the corrected module file
        try:
            with open(module_file, 'w', encoding='utf-8') as f:
                f.write(fix_result['corrected_content'])
            
            logging.info("LLM-corrected module file written successfully")
            
            return {
                'success': True,
                'fixed': True,
                'report': detailed_report,
                'original_content': fix_result['original_content'],
                'corrected_content': fix_result['corrected_content'],
                'module_file_path': module_file
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f"Failed to write corrected module file: {str(e)}",
                'report': detailed_report,
                'fix_content': fix_result['corrected_content']
            }
    else:
        return {
            'success': False,
            'error': f"LLM alignment fixing failed: {fix_result['error']}",
            'report': detailed_report
        }


def generate_inferno_test_kit(client_instance, api_type: str, test_plan_file: str, ig_name: str = "US Core",
                             output_dir: str = OUTPUT_DIR, expected_actors: List[str] = None,
                             enable_validation: bool = True) -> Dict[str, Any]:
    """
    Process a test plan and generate an Inferno test kit.
    
    This is the main function that orchestrates the entire test kit generation process.
    
    Args:
        client_instance: LLM client instance
        api_type: API type (claude, gemini, gpt)
        test_plan_file: Path to test plan markdown file
        ig_name: Name of the module for the tests
        output_dir: Directory for output files
        expected_actors: List of expected actors in the test plan
        enable_validation: Whether to enable optional LLM validation of generated tests
        
    Returns:
        Dictionary containing statistics and paths:
            - total_sections: Number of sections processed
            - total_requirements: Number of requirements found
            - generated_tests: Number of tests generated
            - module_dir: Path to module directory
            - module_file: Path to main module file
            - output_dir: Path to timestamped output directory
            - timestamp: Generation timestamp
            
    Raises:
        Exception: For various processing errors
    """
    print(f"\n{'='*80}")
    print("INFERNO TEST KIT GENERATION")
    print(f"{'='*80}")
    print(f"Module: {ig_name}")
    print(f"Test plan: {test_plan_file}")
    print(f"API: {api_type}")
    print(f"LLM Validation: {'Enabled' if enable_validation else 'Disabled'}")
    print()
    
    logging.info(f"Starting Inferno test generation with {api_type} for {ig_name}")
    
    # Create timestamped output directory with API name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    timestamped_output_dir = os.path.join(output_dir, f"{api_type}_testkit_{timestamp}")
    os.makedirs(timestamped_output_dir, exist_ok=True)
    
    # Standardize module name for Ruby
    ig_name_snake = ig_name.lower().replace('-', '_').replace(' ', '_')
    ig_name_camel = ''.join(word.capitalize() for word in ig_name.split())
    
    # Create module subdirectory
    module_subdir = os.path.join(timestamped_output_dir, ig_name_snake)
    os.makedirs(module_subdir, exist_ok=True)
    
    # Set default actors if none provided
    if not expected_actors:
        expected_actors = ["Health Plan API Actor", "Application Actor"]
    
    try:
        # Parse test plan into sections
        print("Parsing test plan...")
        sections = parse_test_plan(test_plan_file)
        
        # Count total requirements
        total_requirements = sum(len(section['requirements']) for section in sections.values())
        
        print(f"Found {len(sections)} sections with {total_requirements} total requirements")
        logging.info(f"Parsed test plan into {len(sections)} sections with {total_requirements} requirements")
        
        # Get DSL guidance
        print("Loading Inferno DSL guidance...")
        dsl_guidance = get_dsl_guidance()
        dsl_tokens = client_instance.count_tokens(dsl_guidance, api_type)
        logging.info(f"Loaded DSL guidance: {dsl_tokens} tokens")

        # Generate tests by section
        print(f"\nGenerating tests...")
        all_tests = {}
        processed_sections = 0
        
        for section_name, section in sections.items():
            processed_sections += 1
            print(f"[{processed_sections}/{len(sections)}] Processing: {section_name}")
            logging.info(f"Processing section: {section_name} with {len(section['requirements'])} requirements")
            
            # Skip empty sections
            if not section['requirements']:
                print(f"  Skipping empty section")
                continue
                
            # Generate tests for this section
            section_tests = generate_tests_for_section(
                client_instance, 
                api_type, 
                section, 
                dsl_guidance,
                ig_name_camel, 
                70000,  # Higher token limit
                enable_validation
            )
            
            print(f"  Generated {len(section_tests)} tests")
            
            # Add to our collection
            all_tests.update(section_tests)
            
            # Add delay between sections
            time.sleep(client_instance.config[api_type]["delay_between_batches"])
            
        print(f"\nGenerated {len(all_tests)} total tests")
        logging.info(f"Generated tests for {len(all_tests)} requirements")

        # Write test files to the module subdirectory - SECTION-BASED ORGANIZATION
        print("Writing test files...")
        file_paths = {}
        
        # Group by sections instead of actors
        for section_name, section in sections.items():
            # Skip empty sections
            if not section['requirements']:
                continue
            
            # Create section directory
            section_safe = re.sub(r'[^a-zA-Z0-9_]', '_', section_name.lower())
            section_dir = os.path.join(module_subdir, section_safe)
            os.makedirs(section_dir, exist_ok=True)
            
            # Write tests for each requirement in this section
            section_has_tests = False
            for req in section['requirements']:
                # Skip requirements we couldn't generate tests for
                if req['id'] not in all_tests:
                    logging.warning(f"No test generated for {req['id']}")
                    continue
                
                file_name = f"{req['id'].lower().replace('-', '_')}_test.rb"
                file_path = os.path.join(section_dir, file_name)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(all_tests[req['id']])
                
                file_paths[req['id']] = file_path
                section_has_tests = True
                logging.info(f"Wrote test for {req['id']} to {file_path}")
            
            if section_has_tests:
                print(f"  Created section: {section_safe} with {len([r for r in section['requirements'] if r['id'] in all_tests])} tests")
                logging.info(f"Created section directory: {section_safe} with tests")
            else:
                # Remove empty directory
                try:
                    os.rmdir(section_dir)
                    logging.info(f"Removed empty section directory: {section_safe}")
                except:
                    pass
        
        # Extract data from all test files for module file generation
        print("Analyzing generated test files...")
        logging.info("Collecting test data for module file generation")
        test_data = extract_test_data(module_subdir)
        
        # Create structured representation for the LLM
        structure = create_module_structure(test_data, ig_name_snake)
        logging.info("Created structure representation of test files")
        
        # Generate the module file using an LLM
        print("Generating main module file...")
        logging.info("Generating module file with LLM")
        module_content = generate_landing_file_with_llm(
            client_instance,
            api_type,
            ig_name_camel,
            ig_name_snake,
            test_data,
            structure
        )
        
        # Write the module file with timestamped name
        module_file_name = f"{api_type}_{ig_name_snake}_{timestamp}.rb"
        module_file_path = os.path.join(timestamped_output_dir, module_file_name)
        with open(module_file_path, 'w', encoding='utf-8') as f:
            f.write(module_content)
        logging.info(f"Wrote module file to {module_file_path}")

        # Optional LLM-based alignment validation and fixing
        if enable_validation:
            print("Performing alignment validation...")
            logging.info("Starting LLM-based alignment validation...")
            alignment_result = llm_validate_and_fix_alignment(
                client_instance, 
                api_type, 
                timestamped_output_dir, 
                ig_name_snake
            )
            
            # Log the results
            if alignment_result['success']:
                print("  Alignment validation completed successfully")
                logging.info("LLM alignment validation completed successfully")
                if alignment_result.get('fixed'):
                    print("  Applied fixes to module file")
                    logging.info("LLM applied fixes to module file")
            else:
                print(f"  Alignment validation failed: {alignment_result['error']}")
                logging.warning(f"LLM alignment validation failed: {alignment_result['error']}")
            
            # Log the detailed report
            logging.info("=== LLM ALIGNMENT REPORT ===")
            for line in alignment_result['report'].split('\n'):
                if line.strip():
                    logging.info(line)
        else:
            print("Skipping alignment validation (disabled)")
            logging.info("Skipping LLM-based alignment validation (disabled)")

        print(f"\n{'='*80}")
        print("TEST KIT GENERATION COMPLETE!")
        print(f"Output directory: {timestamped_output_dir}")
        print(f"Module file: {module_file_name}")
        print(f"Total sections: {len(sections)}")
        print(f"Total requirements: {total_requirements}")
        print(f"Generated tests: {len(all_tests)}")
        print(f"LLM validation: {'Enabled' if enable_validation else 'Disabled'}")
        print(f"{'='*80}")

        return {
            "total_sections": len(sections),
            "total_requirements": total_requirements,
            "generated_tests": len(all_tests),
            "module_dir": module_subdir,
            "module_file": module_file_path,
            "output_dir": timestamped_output_dir,
            "timestamp": timestamp,
            "validation_enabled": enable_validation
        }
        
    except Exception as e:
        logging.error(f"Error generating Inferno tests: {str(e)}")
        print(f"\nError occurred during test kit generation: {str(e)}")
        raise