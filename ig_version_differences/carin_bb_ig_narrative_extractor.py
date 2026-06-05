import os
import sys
from collections.abc import Callable
from pathlib import Path
import re
import tempfile
import zipfile

pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline'))
sys.path.append(pipeline_path)

import path_helpers
import requests

from ig_narrative_extractor import (
    _convert_local_html_to_markdown,
    _is_url,
    _strip_numbered_html_prefix,
)


CARIN_SKIP_FILES = frozenset({
    "artifacts.html",
    "capability-statements.html",
    "changes-between-versions.html",
    "changes.html",
    "change_notes.html",
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
    "vitals-write.html",
})

CARIN_NARRATIVE_FILES = frozenset({
    "Background.html",
    "Common_Payer_Consumer_Data_Set.html",
    "Conformance_Requirements.html",
    "General_Guidance.html",
    "Security_And_Privacy_Considerations.html",
    "Terminology_Licensure.html",
})

CARIN_RESOURCE_PREFIXES = ("StructureDefinition", "CapabilityStatement")

CARIN_SKIP_PATTERNS = tuple(
    re.compile(pattern)
    for pattern in [
        r"-definitions\.html$",
        r"-examples\.html$",
        r"-mappings\.html$",
        r"-testing\.html$",
        r"\.profile\.history\.html$",
        r"\.profile\.json\.html$",
        r"\.profile\.ttl\.html$",
        r"\.profile\.xml\.html$",
        r"^ipa-comparison-",
        r"^ips-comparison-",
        r"^comparison-",
        r"^us-core-comparisons",
        r"^qa",
    ]
)


def convert_local_html_to_markdown(
    artifacts_dir: str = str(path_helpers.DEMO_ARTIFACTS_ROOT),
    exclude_patterns: list[str] | None = None,
    verbose: bool = True,
) -> dict:
    """
    Convert CARIN HTML files from the flat extraction directories to markdown.

    CARIN zip extraction normalizes selected narrative pages into top-level old/new
    folders, so nested directories are intentionally ignored during conversion.
    """
    return _convert_local_html_to_markdown(
        artifacts_dir=artifacts_dir,
        exclude_patterns=exclude_patterns,
        verbose=verbose,
        recursive=False,
    )


def _normalized_zip_parts(zip_member: str) -> list[str]:
    """Split a zip member path into normalized, non-empty path parts."""
    return [
        part
        for part in zip_member.replace('\\', '/').split('/')
        if part and part != '.'
    ]


def _carin_output_filename(
    zip_member: str,
    allow_top_level_site: bool = False,
) -> str | None:
    """
    Return the normalized output filename for a CARIN narrative page.

    CARIN packages are expected to use site/en/*.html or en/*.html when present.
    Flat site/*.html files are accepted only when those en directories are empty.
    """
    path_parts = _normalized_zip_parts(zip_member)
    has_site_prefix = bool(path_parts and path_parts[0].lower() == 'site')
    if has_site_prefix:
        path_parts = path_parts[1:]

    if len(path_parts) == 2 and path_parts[0].lower() == 'en':
        filename = path_parts[1]
    elif allow_top_level_site and has_site_prefix and len(path_parts) == 1:
        filename = path_parts[0]
    else:
        return None

    if not filename.lower().endswith('.html'):
        return None
    return _strip_numbered_html_prefix(filename)


def _has_carin_en_html(zip_path: str) -> bool:
    """Return whether the zip contains CARIN HTML under site/en/ or en/."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        return any(
            _carin_output_filename(member) is not None
            for member in zip_ref.namelist()
        )


def _should_extract_carin_html(filename: str, skip_files: frozenset[str]) -> bool:
    """Return whether a CARIN HTML file contains narrative worth comparing."""
    if not filename or filename in skip_files:
        return False

    if any(pattern.search(filename) for pattern in CARIN_SKIP_PATTERNS):
        return False

    # Uppercase filenames are generally artifact detail pages in these packages.
    if filename[0].isupper():
        return filename.startswith(CARIN_RESOURCE_PREFIXES) or filename in CARIN_NARRATIVE_FILES

    return True


def _extract_carin_html_files(
    zip_path: str,
    target_dir: Path,
    output_filename_for_member: Callable[[str], str | None],
    skip_files: frozenset[str],
    source_label: str,
    verbose: bool = True,
) -> int:
    """Extract selected CARIN HTML files from one zip archive."""
    html_count = 0
    target_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        html_members = []
        for member in zip_ref.namelist():
            output_filename = output_filename_for_member(member)
            if output_filename and _should_extract_carin_html(output_filename, skip_files):
                html_members.append((member, output_filename))

        if verbose and html_members:
            print(f"Found {len(html_members)} {source_label} html files in zip")

        for html_member, output_filename in html_members:
            try:
                target_file = target_dir / output_filename
                with zip_ref.open(html_member) as source:
                    with open(target_file, 'wb') as dest:
                        dest.write(source.read())

                html_count += 1
                if verbose and html_count % 10 == 0:
                    print(f"Extracted {html_count} html files...")

            except Exception as e:
                print(f"Error extracting {html_member}: {str(e)}")

    return html_count


def _extract_html_files(zip_path: str, target_dir: Path, verbose: bool = True) -> int:
    """Extract narrative HTML from a CARIN package using the preferred layout."""
    allow_top_level_site = not _has_carin_en_html(zip_path)

    if verbose and allow_top_level_site:
        print("No en-directory CARIN HTML files found; falling back to top-level site/*.html files")

    def output_filename_for_member(zip_member: str) -> str | None:
        return _carin_output_filename(
            zip_member,
            allow_top_level_site=allow_top_level_site,
        )

    return _extract_carin_html_files(
        zip_path=zip_path,
        target_dir=target_dir,
        output_filename_for_member=output_filename_for_member,
        skip_files=CARIN_SKIP_FILES,
        source_label="CARIN",
        verbose=verbose,
    )


def _extract_zip_file(
    zip_path: str,
    target_dir: Path,
    verbose: bool,
) -> int:
    """Extract one CARIN zip using the package's available narrative layout."""
    return _extract_html_files(zip_path, target_dir, verbose)


def _download_zip_to_temp_file(source: str, source_name: str, verbose: bool) -> str:
    """Download a zip URL and return the temporary file path containing it."""
    if verbose:
        print(f"Downloading {source_name} zip file from: {source}")

    response = requests.get(source, stream=True, timeout=30)
    response.raise_for_status()

    zip_size = int(response.headers.get('content-length', 0))
    if verbose:
        print(f"Downloaded {source_name} zip file ({zip_size} bytes)")

    with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_zip:
        for chunk in response.iter_content(chunk_size=8192):
            temp_zip.write(chunk)
        return temp_zip.name


def _resolve_local_zip_path(source: str) -> Path:
    """Resolve and validate a local CARIN zip source path."""
    local_path = Path(os.path.abspath(os.path.join(os.getcwd(), source)))

    if not local_path.exists():
        raise FileNotFoundError(f"Local zip file does not exist: {local_path}")

    if not local_path.is_file() or local_path.suffix.lower() != '.zip':
        raise ValueError(f"Local path must be a zip file, got: {local_path}")

    return local_path


def download_and_extract_ig_html(
    new_ig_location: str,
    artifacts_dir: str,
    verbose: bool = False,
    old_ig_location: str | None = None,
) -> dict[str, int]:
    """
    Download or load CARIN IG zip sources and extract selected narrative HTML.

    Args:
        old_ig_location: URL or local path for the old CARIN IG zip, when present
        new_ig_location: URL or local path for the new CARIN IG zip
        artifacts_dir: Path to the base artifacts directory
        verbose: Whether to print progress messages

    Returns:
        Mapping of processed version labels to extracted HTML file counts
    """
    artifacts_path = Path(artifacts_dir)
    old_ig_dir = artifacts_path / "ig" / "site" / "old"
    new_ig_dir = artifacts_path / "ig" / "site" / "new"

    old_ig_dir.mkdir(parents=True, exist_ok=True)
    new_ig_dir.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"Created directories: {old_ig_dir} and {new_ig_dir}")

    ig_configs = [
        {"source": old_ig_location, "target_dir": old_ig_dir, "name": "old"},
        {"source": new_ig_location, "target_dir": new_ig_dir, "name": "new"},
    ]
    extracted_counts = {}

    for config in ig_configs:
        source = config["source"]
        if source is None:
            continue

        try:
            if _is_url(source):
                temp_zip_path = _download_zip_to_temp_file(source, config["name"], verbose)
                try:
                    html_count = _extract_zip_file(
                        temp_zip_path,
                        config["target_dir"],
                        verbose,
                    )
                finally:
                    os.unlink(temp_zip_path)
            else:
                local_path = _resolve_local_zip_path(source)
                if verbose:
                    print(f"Extracting {config['name']} from local zip file: {local_path}")

                html_count = _extract_zip_file(
                    str(local_path),
                    config["target_dir"],
                    verbose,
                )

            extracted_counts[config["name"]] = html_count
            if verbose:
                print(f"Extracted {html_count} html files from {config['name']} zip")

        except requests.RequestException as e:
            error_msg = f"Failed to download {config['name']} from {source}: {str(e)}"
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
            error_msg = f"Unexpected error processing {config['name']} from {source}: {str(e)}"
            if verbose:
                print(f"Error: {error_msg}")

    return extracted_counts
