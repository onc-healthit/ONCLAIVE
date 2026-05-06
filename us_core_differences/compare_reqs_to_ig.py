import sys
import os
from pathlib import Path
import re

pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline'))
sys.path.append(pipeline_path)

import argparse
import difference_finder
import llm_utils

llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

demo_artifacts_path = "demo_artifacts"
OUTPUT_FILENAME = "reqs_difference_output.md"


def _remove_no_differences_files(markdown_content: str):
    """
    Remove file sections that report no substantive differences.

    Args:
        markdown_content: The input markdown content as a string

    Returns:
        The cleaned markdown content and the number of remaining sections
    """
    lines = markdown_content.split('\n')
    result_lines = []

    target_phrase = "no substantive differences found"
    header_pattern = re.compile(r"^\s*#\s+")

    current_section = []
    has_target = False
    differences_count = 0

    for line in lines:
        if header_pattern.match(line):
            if current_section and not has_target:
                result_lines.extend(current_section)
                differences_count += 1
            current_section = [line]
            has_target = False
        else:
            current_section.append(line)

        if target_phrase in line.lower():
            has_target = True

    if current_section and not has_target:
        result_lines.extend(current_section)
        differences_count += 1

    return "\n".join(result_lines), differences_count


def clean_differences_markdown_file(file_path: Path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content, differences_count = _remove_no_differences_files(content)
    content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)
    content = re.sub(r"\n{3,}", "\n\n", content).strip()

    with open(file_path, 'w', encoding='utf-8') as out_file:
        out_file.write(f"{content}\n" if content else "")

    print(f"Cleaned differences file: {file_path}")
    print(f"{differences_count} substantive differences found between IG versions.")

parser = argparse.ArgumentParser(
    description="Compare IG versions"
)

parser.add_argument(
    'artifacts_dir',
    default=demo_artifacts_path,
    help="Relative path to the base artifacts directory"
)

parser.add_argument(
    '-a', '--api-type',
    default='claude',
    choices=['claude', 'gemini', 'gpt'],
    help="Which llm api to use"
)

args = parser.parse_args()

api_type = args.api_type
relative_artifacts_dir = args.artifacts_dir

final_artifacts_dir = os.path.abspath(os.path.join(working_directory, relative_artifacts_dir))

difference_finder.compare_requirements_to_narrative(llm_clients, final_artifacts_dir, api_type)
clean_differences_markdown_file(Path(final_artifacts_dir) / 'ig' / OUTPUT_FILENAME)
