import argparse
import ig_narrative_extractor
import carin_bb_ig_narrative_extractor
import markdown_cleaner
import os


def _get_narrative_extractor(c4bb_ig: bool):
    """Return the narrative extractor module for the selected IG family."""
    return carin_bb_ig_narrative_extractor if c4bb_ig else ig_narrative_extractor


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

parser.add_argument(
    '--c4bb-ig',
    action='store_true',
    help="Process Carin for Blue Button"
)

args = parser.parse_args()

relative_artifacts_dir = args.artifacts_dir
old_ig_location = args.old_ig_location
new_ig_location = args.new_ig_location
verbose = args.verbose
exclude_patterns = args.exclude_pattern
c4bb_ig = args.c4bb_ig

final_artifacts_dir = os.path.abspath(os.path.join(working_directory, relative_artifacts_dir))

narrative_extractor = _get_narrative_extractor(c4bb_ig)
narrative_extractor.download_and_extract_ig_html(
    artifacts_dir=final_artifacts_dir,
    old_ig_location=old_ig_location,
    new_ig_location=new_ig_location,
    verbose=verbose
)

narrative_extractor.convert_local_html_to_markdown(
    artifacts_dir=final_artifacts_dir,
    verbose=verbose,
    exclude_patterns=exclude_patterns
)

markdown_cleaner.process_directory(
    artifacts_dir=final_artifacts_dir
)
