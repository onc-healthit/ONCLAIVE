import sys
import os

pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline'))
sys.path.append(pipeline_path)

import argparse
import difference_finder_v2 as difference_finder
import llm_utils

llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

demo_artifacts_path = "demo-artifacts"

parser = argparse.ArgumentParser(
    description="Convert html IG files into cleaned markdown files"
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

parser.add_argument(
    '-r', '--reqs-xlsx',
    default=None,
    help="Optional path to old requirements XLSX for context"
)

args = parser.parse_args()

api_type = args.api_type
relative_artifacts_dir = args.artifacts_dir

final_artifacts_dir = os.path.abspath(os.path.join(working_directory, relative_artifacts_dir))

from pathlib import Path
difference_finder.compare_narrative(
    llm_clients, final_artifacts_dir, api_type,
    reqs_xlsx=Path(args.reqs_xlsx) if args.reqs_xlsx else None
)
