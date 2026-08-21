import sys
import os

pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline'))
sys.path.append(pipeline_path)

from datetime import UTC, datetime
from pathlib import Path
import pandas as pd
import prompt_utils
from llm_utils import SafetyFilterException

SYSTEM_PROMPTS = {
    "claude": """You are a seasoned Healthcare Integration Test Engineer with expertise determining the requirements present in FHIR Implementation Guides.""",
    "gemini": """You are a Healthcare Integration Test Engineer with expertise determining the requirements present in FHIR Implementation Guides.""",
    "gpt": """As a Healthcare Integration Test Engineer with expertise determining the requirements present in FHIR Implementation Guides, analyze these IG narratives for differences in requirements."""
}


def _timestamp() -> str:
    """Return a compact UTC timestamp string suitable for filenames."""
    return datetime.now(UTC).strftime("%Y%m%d_%H%M%S")


def _cached_response_path(cache_dir: Path, filename: str) -> Path:
    return cache_dir / f"{filename}.txt"


def _load_cached_response(cache_dir: Path, filename: str) -> str | None:
    cache_path = _cached_response_path(cache_dir, filename)
    if cache_path.exists() and cache_path.stat().st_size > 0:
        print(f"  [skip] cached comparison found for {filename}")
        return cache_path.read_text()
    return None


def _save_cached_response(cache_dir: Path, filename: str, response: str) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = _cached_response_path(cache_dir, filename)
    temp_path = cache_path.with_suffix(cache_path.suffix + ".tmp")
    temp_path.write_text(response)
    temp_path.replace(cache_path)


def _write_combined_differences(
    artifacts_path: Path,
    output_prefix: str,
    all_changes: dict[str, str],
) -> Path:
    final_content = ""
    for filename, differences in all_changes.items():
        final_content += f"# {filename}\n\n{differences}\n\n"

    ts = _timestamp()
    output_path = artifacts_path / "ig" / f"{output_prefix}_{ts}.md"
    output_path.write_text(final_content)
    return output_path


def _cleaned_markdown_exists(artifacts_path: Path, version: str) -> bool:
    """
    Return True if cleaned_markdown/<version>/ already exists and contains
    at least one .md file, meaning the cleaning step can be skipped.
    """
    md_dir = artifacts_path / "ig" / "cleaned_markdown" / version
    if not md_dir.exists():
        return False
    files = list(md_dir.glob("*.md"))
    if not files:
        return False
    print(f"  [skip] cleaned_markdown/{version}/ already has {len(files)} file(s) — reusing existing files.")
    return True


def should_run_cleaning(artifacts_path: Path, version: str) -> bool:
    """
    Call this from your pipeline before running any cleaning/scraping step
    for 'old' or 'new'. Returns False if cleaned markdown already exists.

    Example:
        if difference_finder.should_run_cleaning(artifacts_path, 'new'):
            scraper.clean_and_save(...)
    """
    return not _cleaned_markdown_exists(artifacts_path, version)


def _load_requirements_block(reqs_xlsx: Path | None) -> str:
    """
    Load the requirements spreadsheet and format it as a compact text block
    suitable for embedding in a prompt as an <old_ig_requirements> section.
    Returns an empty string if no path is provided or the file cannot be read.
    """
    if reqs_xlsx is None:
        return ""

    try:
        df = pd.read_excel(reqs_xlsx, sheet_name="Requirements", dtype=str)
    except Exception as e:
        print(f"  WARNING: Could not load requirements XLSX ({e}) — continuing without it.")
        return ""

    df.columns = [c.rstrip("*").strip() for c in df.columns]
    keep = ["ID", "URL", "Requirement", "Conformance", "Actors",
            "Conditionality", "Verifiable?", "Planning To Test?",
            "Scope", "Test Plan", "Section"]
    keep = [c for c in keep if c in df.columns]
    df = df[keep].dropna(subset=["ID", "Requirement"])

    lines = []
    for _, r in df.iterrows():
        rid = r.get("ID", "?")
        url = r.get("URL", "")
        conf = r.get("Conformance", "")
        actor = r.get("Actors", "")
        plan = r.get("Planning To Test?", "")
        scope = r.get("Scope", "")
        req_text = str(r.get("Requirement", ""))[:300]
        lines.append(
            f"[{rid}] ({conf}, {actor}, tested={plan}, scope={scope}) URL={url}\n  {req_text}"
        )

    block = "\n".join(lines)
    return f"<old_ig_requirements>\n{block}\n</old_ig_requirements>\n"


def create_requirements_ig_difference_prompt(
    new_ig_content: str,
    old_ig_requirements_content: str,
    artifacts_dir: str,
) -> str:
    """
    Prompt for reqs-to-narrative comparison. The old requirements spreadsheet
    content is passed in directly as old_ig_requirements_content.
    """
    prompt = prompt_utils.load_prompt(
        artifacts_dir,
        'reqs_ig_content_difference_structured.md',
        NEW_IG_NARRATIVE=new_ig_content,
        OLD_IG_REQUIREMENTS=old_ig_requirements_content
    )
    return prompt


def create_difference_prompt(
    new_ig_content: str,
    old_ig_content: str,
    artifacts_dir: str,
    reqs_xlsx: Path | None = None,
) -> str:
    """
    Prompt for narrative-to-narrative comparison. If reqs_xlsx is provided,
    its contents are embedded as an <old_ig_requirements> context block so
    the LLM can cross-reference requirement IDs, conformance levels, and
    test planning status even though the primary comparison is narrative-based.
    """
    reqs_block = _load_requirements_block(reqs_xlsx)
    prompt = prompt_utils.load_prompt(
        artifacts_dir,
        'reqs_difference_structured.md',
        NEW_IG_NARRATIVE=new_ig_content,
        OLD_IG_NARRATIVE=old_ig_content,
        OLD_IG_REQUIREMENTS_BLOCK=reqs_block,
    )
    return prompt


def compare_narrative(
    client_instance,
    artifacts_dir: str,
    api_type: str,
    reqs_xlsx: Path | None = None,
):
    """
    Narrative-to-narrative comparison. Optionally accepts a requirements XLSX
    path to embed as reference context in each prompt.
    """
    artifacts_path = Path(artifacts_dir)
    old_ig_dir = artifacts_path / "ig" / "cleaned_markdown" / "old"
    new_ig_dir = artifacts_path / "ig" / "cleaned_markdown" / "new"

    for label, d in [("old", old_ig_dir), ("new", new_ig_dir)]:
        if not d.exists():
            print(f"WARNING: cleaned_markdown/{label}/ not found at {d}")

    if reqs_xlsx:
        print(f"  Using requirements XLSX as context: {reqs_xlsx}")

    new_ig_files = sorted(new_ig_dir.glob('*.md'))
    cache_dir = artifacts_path / "ig" / "difference_chunks"
    all_changes = {}
    client_instance.safety_blocked_count = 0

    for new_ig_file_path in new_ig_files:
        cached_response = _load_cached_response(cache_dir, new_ig_file_path.name)
        if cached_response is not None:
            all_changes[new_ig_file_path.name] = cached_response
            continue

        old_ig_file_path = old_ig_dir / new_ig_file_path.name

        try:
            with open(new_ig_file_path) as f:
                new_file_content = f.read()
        except FileNotFoundError:
            print(f"Error: {new_ig_file_path} not found")
            continue
        try:
            with open(old_ig_file_path) as f:
                old_file_content = f.read()
        except FileNotFoundError:
            old_file_content = ""

        prompt_text = create_difference_prompt(
            new_file_content, old_file_content, artifacts_dir, reqs_xlsx=reqs_xlsx
        )

        try:
            print(f"Comparing: {new_ig_file_path.name}")
            response = client_instance.make_llm_request(
                api_type, prompt_text, sys_prompt=SYSTEM_PROMPTS[api_type]
            )
            all_changes[new_ig_file_path.name] = response
            _save_cached_response(cache_dir, new_ig_file_path.name, response)
        except SafetyFilterException as e:
            client_instance.safety_blocked_count += 1
            print(f"\nSAFETY FILTER BLOCKED CONTENT #{client_instance.safety_blocked_count}")
            print(f"File: {new_ig_file_path.name}")
            print("=" * 60)
            print("BLOCKED CONTENT SAMPLE:")
            print(e.blocked_content)
            print("=" * 60)
            print("Skipping this chunk and continuing...\n")
            response = "## CHUNK SKIPPED DUE TO SAFETY FILTER\n[Content blocked by safety filters]\n\n"
            all_changes[new_ig_file_path.name] = response
            _save_cached_response(cache_dir, new_ig_file_path.name, response)

    output_path = _write_combined_differences(artifacts_path, "differences", all_changes)

    print(f"\nDifferences written to: {output_path}")
    return output_path


def compare_requirements_to_narrative(
    client_instance,
    artifacts_dir: str,
    api_type: str,
):
    """
    Requirements-to-narrative comparison. Reads old requirements from the
    cleaned_markdown/old/ directory (pre-formatted as text by the pipeline).
    """
    artifacts_path = Path(artifacts_dir)
    old_ig_dir = artifacts_path / "ig" / "cleaned_markdown" / "old"
    new_ig_dir = artifacts_path / "ig" / "cleaned_markdown" / "new"

    for label, d in [("old", old_ig_dir), ("new", new_ig_dir)]:
        if not d.exists():
            print(f"WARNING: cleaned_markdown/{label}/ not found at {d}")

    new_ig_files = sorted(new_ig_dir.glob('*.md'))
    cache_dir = artifacts_path / "ig" / "reqs_difference_chunks"
    all_changes = {}
    client_instance.safety_blocked_count = 0

    for new_ig_file_path in new_ig_files:
        cached_response = _load_cached_response(cache_dir, new_ig_file_path.name)
        if cached_response is not None:
            all_changes[new_ig_file_path.name] = cached_response
            continue

        old_ig_file_path = old_ig_dir / new_ig_file_path.name

        try:
            with open(new_ig_file_path) as f:
                new_file_content = f.read()
        except FileNotFoundError:
            print(f"Error: {new_ig_file_path} not found")
            continue
        try:
            with open(old_ig_file_path) as f:
                old_file_content = f.read()
        except FileNotFoundError:
            old_file_content = ""

        prompt_text = create_requirements_ig_difference_prompt(
            new_file_content, old_file_content, artifacts_dir
        )

        try:
            print(f"Comparing: {new_ig_file_path.name}")
            response = client_instance.make_llm_request(
                api_type, prompt_text, sys_prompt=SYSTEM_PROMPTS[api_type]
            )
            all_changes[new_ig_file_path.name] = response
            _save_cached_response(cache_dir, new_ig_file_path.name, response)
        except SafetyFilterException as e:
            client_instance.safety_blocked_count += 1
            print(f"\nSAFETY FILTER BLOCKED CONTENT #{client_instance.safety_blocked_count}")
            print(f"File: {new_ig_file_path.name}")
            print("=" * 60)
            print("BLOCKED CONTENT SAMPLE:")
            print(e.blocked_content)
            print("=" * 60)
            print("Skipping this chunk and continuing...\n")
            response = "## CHUNK SKIPPED DUE TO SAFETY FILTER\n[Content blocked by safety filters]\n\n"
            all_changes[new_ig_file_path.name] = response
            _save_cached_response(cache_dir, new_ig_file_path.name, response)

    output_path = _write_combined_differences(artifacts_path, "reqs_difference_output", all_changes)

    print(f"\nRequirements difference written to: {output_path}")
    return output_path
