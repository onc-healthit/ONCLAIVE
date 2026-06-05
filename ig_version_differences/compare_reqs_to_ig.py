import sys
import os
from pathlib import Path

pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline'))
sys.path.append(pipeline_path)

import argparse
import difference_finder
from difference_output_cleaner import clean_differences_markdown_file
import llm_utils

llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

demo_artifacts_path = "demo_artifacts"
OUTPUT_FILENAME = "reqs_difference_output.md"


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
