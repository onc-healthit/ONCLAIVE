import sys
import os

pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline'))
sys.path.append(pipeline_path)

from pathlib import Path
import prompt_utils
from llm_utils import SafetyFilterException

SYSTEM_PROMPTS = {
    "claude": """You are a seasoned Healthcare Integration Test Engineer with expertise determining the requirements present in FHIR Implementation Guides.""",
    "gemini": """You are a Healthcare Integration Test Engineer with expertise determining the requirements present in FHIR Implementation Guides.""",
    "gpt": """As a Healthcare Integration Test Engineer with expertise determining the requirements present in FHIR Implementation Guides, analyze these IG narratives for differences in requirements.""",
    "aip": """As a Healthcare Integration Test Engineer with expertise determining the requirements present in FHIR Implementation Guides, analyze these IG narratives for differences in requirements."""
}

def create_requirements_ig_difference_prompt(new_ig_content: str, old_ig_requirements_content: str, artifacts_dir: str) -> str:
    """
    Create a prompt for finding differences between the Inferno requirements of one IG version and the narrative 
    content of another IG version.

    Args:
        new_ig_content: The content from the new version of the IG to analyze
        old_ig_requirements: The requirements form the old version of the IG to analyze
        artifacts_dir: Path to the base artifacts directory

    Returns:
        The formatted prompt for the LLM
    """

    prompt = prompt_utils.load_prompt(
        artifacts_dir,
        'reqs_ig_content_difference.md',
        NEW_IG_NARRATIVE=new_ig_content,
        OLD_IG_REQUIREMENTS=old_ig_requirements_content
    )

    return prompt

def create_difference_prompt(new_ig_content: str, old_ig_content: str, artifacts_dir: str) -> str:
    """
    Create a prompt for finding differences between IG versions.

    Args:
        new_ig_content: The content from the new version of the IG to analyze
        old_ig_content: The content from the old version of the IG to analyze
        artifacts_dir: Path to the base artifacts directory

    Returns:
        The formatted prompt for the LLM
    """

    prompt = prompt_utils.load_prompt(
        artifacts_dir,
        'reqs_difference.md',
        NEW_IG_NARRATIVE=new_ig_content,
        OLD_IG_NARRATIVE=old_ig_content
    )

    return prompt

def compare_narrative(client_instance, artifacts_dir: str, api_type: str):
    artifacts_path = Path(artifacts_dir)
    old_ig_dir = artifacts_path / "ig" / "cleaned_markdown" / "old"
    new_ig_dir = artifacts_path / "ig" / "cleaned_markdown" / "new"

    new_ig_files = new_ig_dir.glob('*.md')

    all_changes = {}

    client_instance.safety_blocked_count = 0

    for new_ig_file_path in new_ig_files:
        old_ig_file_path = old_ig_dir / new_ig_file_path.name

        try:
            with open(new_ig_file_path) as new_file:
                new_file_content = new_file.read()
        except FileNotFoundError:
            print(f"Error: {new_ig_file_path} not found")
            continue
        try:
            with open(old_ig_file_path) as old_file:
                old_file_content = old_file.read()
        except FileNotFoundError:
            old_file_content = ""

        prompt_text = create_difference_prompt(new_file_content, old_file_content, artifacts_dir)

        try:
            print(f"Comparing: {new_ig_file_path.name}")
            response = client_instance.make_llm_request(api_type, prompt_text, sys_prompt=SYSTEM_PROMPTS[api_type])
            all_changes[new_ig_file_path.name] = response
        except SafetyFilterException as e:
            client_instance.safety_blocked_count += 1
            print(f"\nSAFETY FILTER BLOCKED CONTENT #{client_instance.safety_blocked_count}")
            print(f"File: {new_ig_file_path.name}")
            print("=" * 60)
            print("BLOCKED CONTENT SAMPLE:")
            print(e.blocked_content)
            print("=" * 60)
            print("Skipping this chunk and continuing...\n")
            all_changes[new_ig_file_path.name] = "## CHUNK SKIPPED DUE TO SAFETY FILTER\n[Content blocked by safety filters]\n\n"

    final_content = ""
    for filename, differences in all_changes.items():
        content = f"# {filename}\n\n{differences}\n\n"
        final_content = final_content + content

    output_path = artifacts_path / 'ig' / 'differences.md'

    with open(output_path, 'w') as f:
        f.write(final_content)

def compare_requirements_to_narrative(client_instance, artifacts_dir: str, api_type: str):
    artifacts_path = Path(artifacts_dir)
    old_ig_dir = artifacts_path / "ig" / "cleaned_markdown" / "old"
    new_ig_dir = artifacts_path / "ig" / "cleaned_markdown" / "new"

    new_ig_files = new_ig_dir.glob('*.md')

    all_changes = {}

    client_instance.safety_blocked_count = 0

    for new_ig_file_path in new_ig_files:
        old_ig_file_path = old_ig_dir / new_ig_file_path.name

        try:
            with open(new_ig_file_path) as new_file:
                new_file_content = new_file.read()
        except FileNotFoundError:
            print(f"Error: {new_ig_file_path} not found")
            continue
        try:
            with open(old_ig_file_path) as old_file:
                old_file_content = old_file.read()
        except FileNotFoundError:
            old_file_content = ""

        prompt_text = create_requirements_ig_difference_prompt(new_file_content, old_file_content, artifacts_dir)

        try:
            print(f"Comparing: {new_ig_file_path.name}")
            response = client_instance.make_llm_request(api_type, prompt_text, sys_prompt=SYSTEM_PROMPTS[api_type])
            all_changes[new_ig_file_path.name] = response
        except SafetyFilterException as e:
            client_instance.safety_blocked_count += 1
            print(f"\nSAFETY FILTER BLOCKED CONTENT #{client_instance.safety_blocked_count}")
            print(f"File: {new_ig_file_path.name}")
            print("=" * 60)
            print("BLOCKED CONTENT SAMPLE:")
            print(e.blocked_content)
            print("=" * 60)
            print("Skipping this chunk and continuing...\n")
            all_changes[new_ig_file_path.name] = "## CHUNK SKIPPED DUE TO SAFETY FILTER\n[Content blocked by safety filters]\n\n"

    final_content = ""
    for filename, differences in all_changes.items():
        content = f"# {filename}\n\n{differences}\n\n"
        final_content = final_content + content

    output_path = artifacts_path / 'ig' / 'reqs_difference_output.md'
    
    with open(output_path, 'w') as f:
        f.write(final_content)