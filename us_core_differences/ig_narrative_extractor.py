import sys
import os

pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline'))
sys.path.append(pipeline_path)

from bs4 import BeautifulSoup
import os
from pathlib import Path
import path_helpers
from langchain_community.document_transformers import MarkdownifyTransformer
from langchain.schema import Document
import re
import requests
import zipfile
import tempfile

# Default patterns to exclude from conversion
DEFAULT_EXCLUDE_PATTERNS = [
    r'\.ttl\.html$',      # Exclude files ending with .ttl.html
    r'\.xml\.html$',      # Exclude files ending with .xml.html
    r'\.json\.html$',     # Exclude files ending with .json.html
    r'\.change\.history\.html$',    # Exclude change history files
    r'\.profile\.history\.html$',
    r'(?i)example'
]

def convert_local_html_to_markdown(
    artifacts_dir: str = str(path_helpers.DEMO_ARTIFACTS_ROOT),
    exclude_patterns: list = None,
    verbose: bool = True
) -> dict:
    """
    Convert HTML files from a local directory to markdown, excluding files matching specific patterns.

    This function recursively processes all HTML files in the input directory,
    applies header numbering based on CSS styles, and converts them to Markdown format
    while preserving the directory structure.

    Args:
        artifacts_dir: Path to the base artifacts directory
        exclude_patterns: List of regex patterns to exclude. If None, uses DEFAULT_EXCLUDE_PATTERNS
        verbose: Whether to print progress messages

    Returns:
        Dictionary containing conversion summary:
            - total_files: Total HTML files found
            - processed: Number of files successfully processed
            - errors: Number of files that encountered errors
            - error_files: List of files that had errors

    Raises:
        FileNotFoundError: If input directory doesn't exist
        PermissionError: If unable to create output directory or write files

    Example:
        >>> result = convert_local_html_to_markdown('input/html', 'output/md')
        >>> print(f"Processed {result['processed']} files")
    """
    for ig_version in ['old', 'new']:
        # Validate input directory
        input_path = Path(artifacts_dir) / "ig" / "site" / ig_version
        if not input_path.exists():
            raise FileNotFoundError(f"IG files in artifacts directory not found: {input_path}")

        output_dir= Path(artifacts_dir) / "ig" / "converted_markdown" / ig_version

        os.makedirs(output_dir, exist_ok=True)

        # Use default patterns if none provided
        if exclude_patterns is None:
            exclude_patterns = DEFAULT_EXCLUDE_PATTERNS

        # Compile regex patterns for exclusion
        compiled_patterns = [re.compile(pattern) for pattern in exclude_patterns]

        # Get all HTML files in the directory
        html_files = []
        for file in input_path.glob('**/*.html'):
            file_str = str(file)

            # Check if the file should be excluded
            exclude = any(pattern.search(file_str) for pattern in compiled_patterns)
            if not exclude:
                html_files.append(file)

        if verbose:
            print(f"Found {len(html_files)} HTML files to process")

        # Initialize counters and transformer
        processed = 0
        errors = 0
        error_files = []
        md_transformer = MarkdownifyTransformer()

        # Process each HTML file
        for i, html_file in enumerate(html_files):
            try:
                # Create relative path to preserve directory structure
                rel_path = html_file.relative_to(input_path)
                output_path = Path(output_dir) / rel_path.with_suffix('.md')

                # Create parent directories if they don't exist
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Load and process HTML content
                with open(html_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()

                # Process headers with numbering
                processed_content = _process_html_headers(html_content, html_file, verbose)

                # Create a LangChain Document object with the processed HTML content
                doc = Document(page_content=processed_content)

                # Transform to Markdown
                converted_docs = md_transformer.transform_documents([doc])

                # Write to output file
                if converted_docs and len(converted_docs) > 0:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(converted_docs[0].page_content)
                    processed += 1
                else:
                    raise ValueError("No content generated from markdown transformer")

                # Print progress
                if verbose and ((i + 1) % 10 == 0 or i == len(html_files) - 1):
                    print(f"Processed {i + 1}/{len(html_files)} files")

            except Exception as e:
                if verbose:
                    print(f"Error processing {html_file}: {str(e)}")
                errors += 1
                error_files.append(str(html_file))

        # Print summary
        if verbose:
            print(f"Conversion complete. Successfully processed {processed} files. Encountered {errors} errors.")

    return {
        'total_files': len(html_files),
        'processed': processed,
        'errors': errors,
        'error_files': error_files
    }


def _process_html_headers(html_content: str, html_file: Path, verbose: bool = True) -> str:
    """
    Process HTML headers to add hierarchical numbering based on CSS styles.

    This function extracts header numbering patterns from CSS --heading-prefix variables
    and applies hierarchical numbering to all h1-h6 elements in the document.

    Args:
        html_content: The HTML content to process
        html_file: Path to the HTML file (used for error reporting)
        verbose: Whether to print warning messages for processing failures

    Returns:
        Processed HTML content with numbered headers, or original content if processing fails

    Note:
        The function looks for CSS variables in the format:
        h{level} { --heading-prefix: "1.2.3"; }
        and uses this to establish the starting numbering hierarchy.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the style tag with CSS heading prefix information
        style_tag = soup.find("style", attrs={'type': 'text/css'})

        if not (style_tag and style_tag.text):
            return html_content

        # Look for heading prefix pattern in CSS
        h_prefix_match = re.search(
            r'(h[0-9])\s*\{\s*--heading-prefix\s*:\s*"([0-9]+(?:\.[0-9]+)*)"',
            style_tag.text
        )

        # We also want to check if the CSS styling is present in the HTML file and if not then we need to add a digit to the first header present
        css_style_tag = None
        for tag in soup.find_all("style", attrs={'type': 'text/css'}):
            if 'h2:before{color:silver;counter-increment:section;content:var(--heading-prefix) " ";}' in tag.text:
                css_style_tag = tag.text
                break

        if not h_prefix_match:
            return html_content

        # Extract the starting header level and numbering
        starting_header_level = int(h_prefix_match.group(1)[1:])
        prev_level = starting_header_level - 1
        header_list = [int(x) for x in h_prefix_match.group(2).split('.')]

        # If the CSS styling is not present, we want to add a 1 as a digit (see 14.2.1 in US Core IG)
        if css_style_tag == None:
            header_list.append(1)

        # Process all headers in the document
        for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            header_level = int(header.name[1:])

            # Adjust header numbering based on level changes
            header_list = _update_header_numbering(header_list, header_level, prev_level, starting_header_level)

            # Create the numbered header text
            header_number = ".".join(str(x) for x in header_list)
            markdown_header = " ".join([
                "#" * header_level,
                header_number,
                header.get_text(strip=True)
            ])

            # Replace the original header with numbered version
            header.replace_with(markdown_header)
            prev_level = header_level

        return str(soup)

    except Exception as header_error:
        if verbose:
            print(f"Warning: Header processing failed for {html_file}: {str(header_error)}")
            print("Falling back to original HTML content...")
        return html_content

def _update_header_numbering(header_list: list, current_level: int, prev_level: int, starting_header_level: int) -> list:
    """
    Update the header numbering list based on the current and previous header levels.

    Args:
        header_list: Current list of header numbers at each level
        current_level: The level of the current header (1-6)
        prev_level: The level of the previous header
        starting_header_level: The level of the header prefix

    Returns:
        Updated header numbering list
    """
    # Base base - if the header level is the same as the starting level, then nothing changes
    if current_level != starting_header_level:
        if prev_level == current_level:
            header_list[-1] += 1
        elif prev_level > current_level:
            # Chop off the last digit and increment the new last digit
            header_list = header_list[:-1] # or try .pop if this doesn't work
            header_list[-1] += 1
        elif prev_level < current_level:
            # Add a 1 to the end
            header_list.append(1)
    return header_list


def _is_url(path_or_url: str) -> bool:
    return path_or_url.startswith(('http://', 'https://'))

def download_and_extract_ig_html(
    old_ig_location: str,
    new_ig_location: str,
    artifacts_dir: str,
    verbose: bool = False
) -> dict:
    """
    Download or load two specified IG sources and extract all html files to separate folders.

    This function handles both URLs and local file paths. For URLs, it downloads zip files
    and extracts HTML files. For local paths, it handles both zip files and directories
    containing HTML files directly.

    Args:
        old_ig_location: URL or local path of the first (old) IG source
        new_ig_location: URL or local path of the second (new) IG source
        artifacts_dir: Path to the base artifacts directory
        verbose: Whether to print progress messages

    Raises:
        requests.RequestException: If download fails (for URLs)
        zipfile.BadZipFile: If zip file is corrupted
        FileNotFoundError: If local path doesn't exist
        PermissionError: If unable to create directories or write files
    """
    artifacts_path = Path(artifacts_dir)
    old_ig_dir = artifacts_path / "ig" / "site" / "old"
    new_ig_dir = artifacts_path / "ig" / "site" / "new"

    # Create directories
    old_ig_dir.mkdir(parents=True, exist_ok=True)
    new_ig_dir.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"Created directories: {old_ig_dir} and {new_ig_dir}")

    # Process both IG sources (URLs or local zip files)
    ig_configs = [
        {"source": old_ig_location, "target_dir": old_ig_dir, "name": "old"},
        {"source": new_ig_location, "target_dir": new_ig_dir, "name": "new"}
    ]

    for config in ig_configs:
        try:
            if _is_url(config['source']):
                # Handle URL - download zip file
                if verbose:
                    print(f"Downloading {config['name']} zip file from: {config['source']}")

                response = requests.get(config['source'], stream=True, timeout=30)
                response.raise_for_status()

                zip_size = int(response.headers.get('content-length', 0))

                if verbose:
                    print(f"Downloaded {config['name']} zip file ({zip_size} bytes)")

                with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_zip:
                    # Write zip content
                    for chunk in response.iter_content(chunk_size=8192):
                        temp_zip.write(chunk)
                    temp_zip_path = temp_zip.name

                try:
                    html_count = _extract_html_files(
                        temp_zip_path,
                        config['target_dir'],
                        verbose
                    )

                    if verbose:
                        print(f"Extracted {html_count} html files from {config['name']} zip")

                finally:
                    os.unlink(temp_zip_path)

            else:
                # Handle local zip file
                local_path = Path(os.path.abspath(os.path.join(os.getcwd(), config['source'])))

                if not local_path.exists():
                    raise FileNotFoundError(f"Local zip file does not exist: {local_path}")

                if not local_path.is_file() or local_path.suffix.lower() != '.zip':
                    raise ValueError(f"Local path must be a zip file, got: {local_path}")

                if verbose:
                    print(f"Extracting {config['name']} from local zip file: {local_path}")

                html_count = _extract_html_files(
                    str(local_path),
                    config['target_dir'],
                    verbose
                )

                if verbose:
                    print(f"Extracted {html_count} html files from {config['name']} local zip")

        except requests.RequestException as e:
            error_msg = f"Failed to download {config['name']} from {config['source']}: {str(e)}"
            if verbose:
                print(f"Error: {error_msg}")

        except zipfile.BadZipFile as e:
            error_msg = f"Invalid zip file for {config['name']}: {str(e)}"
            if verbose:
                print(f"Error: {error_msg}")

        except FileNotFoundError as e:
            error_msg = f"Local file not found for {config['name']}: {str(e)}"
            if verbose:
                print(f"Error: {error_msg}")

        except Exception as e:
            error_msg = f"Unexpected error processing {config['name']} from {config['source']}: {str(e)}"
            if verbose:
                print(f"Error: {error_msg}")

def _extract_html_files(zip_path: str, target_dir: Path, verbose: bool = True) -> int:
    """
    Extract all html files from a zip archive to the target directory.

    Args:
        zip_path: Path to the zip file
        target_dir: Directory to extract html files to
        verbose: Whether to print progress messages

    Returns:
        Number of html files extracted

    Raises:
        zipfile.BadZipFile: If zip file is corrupted
        PermissionError: If unable to write files
    """
    html_count = 0

    files_to_skip = [
        "artifacts.html",
        "capability-statements.html",
        "changes-between-versions.html",
        "changes.html",
        "conformance.html",
        "downloads.html",
        "examples.html",
        "fsh-link-references.html",
        "future-of-US-core.html",
        "guidance.html",
        "index.html",
        "looking-ahead.html",
        "observation-summary.html",
        "patient-data-feed-additional-resources.html",
        "patient-data-feed.html",
        "profiles-and-extensions.html",
        "README.html",
        "relationship-with-other-igs.html",
        "search-parameters-and-operations.html",
        "searchform.html",
        "terminology.html",
        "toc.html",
        "us-core-roadmap.html",
        "uscdi.html",
        "vsacname-fhiruri-map.html",
        "vitals-write.html"
    ]

    patterns_to_skip = [
        re.compile(r"-definitions\.html$"),
        re.compile(r"-examples\.html$"),
        re.compile(r"-mappings\.html$"),
        re.compile(r"-testing\.html$"),
        re.compile(r"\.profile\.history\.html$"),
        re.compile(r"\.profile\.json\.html$"),
        re.compile(r"\.profile\.ttl\.html$"),
        re.compile(r"\.profile\.xml\.html$"),
        re.compile(r"^ipa-comparison-"),
        re.compile(r"^comparison-"),
        re.compile(r"^qa*")
    ]

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        all_files = zip_ref.namelist()

        html_files = [f for f in all_files if f.lower().endswith(('.html'))]

        if verbose and len(html_files) > 0:
            print(f"Found {len(html_files)} html files in zip")

        for html_file in html_files:
            try:
                with zip_ref.open(html_file) as source:
                    content = source.read()

                safe_filename = html_file.removeprefix('site/').replace('/', '_').replace('\\', '_')

                if safe_filename in files_to_skip:
                    continue

                # Skip documentation for resources which aren't StructureDefinitions (terminology and examples)
                if safe_filename[0].isupper() and not safe_filename.startswith('StructureDefinition'):
                    continue

                pattern_to_skip = False
                for pattern in patterns_to_skip:
                    if pattern.search(safe_filename):
                        pattern_to_skip = True
                        break

                if pattern_to_skip:
                    continue

                target_file = target_dir / safe_filename
                with open(target_file, 'wb') as dest:
                    dest.write(content)

                html_count += 1

                if verbose and html_count % 10 == 0:
                    print(f"Extracted {html_count} html files...")

            except Exception as e:
                print(f"Error extracting {html_file}: {str(e)}")

                continue

    return html_count
