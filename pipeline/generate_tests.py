import argparse
import llm_utils
import os
import test_kit_07

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
    '--actor',
    action='append',
    help="Expected actor in the test plan"
)

parser.add_argument(
    '--validate',
    default=False,
    action='store_true',
    help="Whether to enable optional LLM validation of generated tests"
)

args = parser.parse_args()

relative_artifacts_dir = args.artifacts_dir
ig_name = args.ig_name
api_type = args.api_type
expected_actors = args.actor
enable_validation=args.validate

final_artifacts_dir = os.path.abspath(os.path.join(working_directory, relative_artifacts_dir))

test_kit_07.generate_inferno_test_kit(
    client_instance=llm_clients,
    api_type=api_type,
    artifacts_dir=final_artifacts_dir,
    ig_name=ig_name,
    expected_actors=expected_actors,
    enable_validation=enable_validation
)
