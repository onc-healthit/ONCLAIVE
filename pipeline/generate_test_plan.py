import argparse
import logging
import llm_utils
import os
import test_plan_06
import urllib3

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
    '-i', '--ig-name',
    required=True,
    help="Name of the implementation guide"
)

parser.add_argument(
    '-a', '--api-type',
    default='claude',
    choices=['claude', 'gemini', 'gpt'],
    help="Which llm api to use"
)

parser.add_argument(
    '-v', '--verbose',
    default=False,
    action='store_true',
    help="Enable verbose logging"
)

args = parser.parse_args()

relative_artifacts_dir = args.artifacts_dir
ig_name = args.ig_name
api_type = args.api_type
verbose = args.verbose

final_artifacts_dir = os.path.abspath(os.path.join(working_directory, relative_artifacts_dir))

llm_clients.logger.setLevel(logging.INFO)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)
logging.getLogger("backoff").setLevel(logging.ERROR)

# clear any existing capability statements from vector database
test_plan_06.clear_capability_collection("capability_statements")

test_plan_06.generate_consolidated_test_plan(
    client_instance=llm_clients,
    api_type=api_type,
    artifacts_dir=final_artifacts_dir,
    ig_name=ig_name,
    verbose=verbose
)
