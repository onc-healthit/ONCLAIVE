import argparse
import llm_utils
import os
import reqs_downselect_05
import reqs_extraction_03
import reqs_reviewer_04

llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

demo_artifacts_path = "demo-artifacts"

parser = argparse.ArgumentParser(
    description="Extract requirements from IG markdown files"
)

parser.add_argument(
    'artifacts_dir',
    nargs="?",
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
    '-m', '--max-files',
    type=int,
    help="Maximum number of files to process"
)

parser.add_argument(
    '-b', '--batch-size',
    type=int,
    default=25,
    help="Number of requirements per batch"
)

parser.add_argument(
    '-t', '--threshold',
    type=float,
    default=0.98,
    help="Similarity threshold for duplicate detection (0.0-1.0)"
)

parser.add_argument(
    '-f', '--output-format',
    default="markdown",
    choices=['markdown', 'json', 'csv', 'all'],
    help="Output format"
)

args = parser.parse_args()

relative_artifacts_dir = args.artifacts_dir
api_type = args.api_type
max_files = args.max_files
batch_size = args.batch_size
threshold = args.threshold
output_format = args.output_format

final_artifacts_dir = os.path.abspath(os.path.join(working_directory, relative_artifacts_dir))

reqs_extraction_03.run_requirements_extractor(
    artifacts_dir=final_artifacts_dir,
    api_type=api_type,
    client_instance=llm_clients,
    max_files=max_files,
    output_format=output_format
)

reqs_reviewer_04.run_batch_requirements_refinement(
    artifacts_dir=final_artifacts_dir,
    client_instance=llm_clients,
    batch_size=batch_size,
    api_type=api_type,
    output_format=output_format
)

reqs_downselect_05.full_pass(
    artifacts_dir=final_artifacts_dir,
    threshold=threshold,
    output_format=output_format
)
