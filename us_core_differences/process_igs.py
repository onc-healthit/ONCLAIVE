import argparse
import ig_narrative_extractor
import markdown_cleaner
import os

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
    '-o', '--old-ig-location',
    required=True,
    help="URL or relative file path of full IG package for old IG version"
)

parser.add_argument(
    '-n', '--new-ig-location',
    required=True,
    help="URL or relative file path of full IG package for new IG version"
)

parser.add_argument(
    '-v', '--verbose',
    default=False,
    action='store_true',
    help="Enable verbose logging"
)

parser.add_argument(
    '-e', '--exclude-pattern',
    action='append',
    help="Files matching regular expressions in this argument will be ignored"
)

args = parser.parse_args()

relative_artifacts_dir = args.artifacts_dir
old_ig_location = args.old_ig_location
new_ig_location = args.new_ig_location
verbose = args.verbose
exclude_patterns = args.exclude_pattern

final_artifacts_dir = os.path.abspath(os.path.join(working_directory, relative_artifacts_dir))

ig_narrative_extractor.download_and_extract_ig_html(
    artifacts_dir=final_artifacts_dir,
    old_ig_location=old_ig_location,
    new_ig_location=new_ig_location,
    verbose=verbose
)

result = ig_narrative_extractor.convert_local_html_to_markdown(
    artifacts_dir=final_artifacts_dir,
    verbose=verbose,
    exclude_patterns=exclude_patterns
)

markdown_cleaner.process_directory(
    artifacts_dir=final_artifacts_dir
)
