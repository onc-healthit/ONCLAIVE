from pathlib import Path
import pandas as pd


def _markdown_filename_from_requirement_url(raw_url) -> str | None:
    """Return the markdown filename referenced by a requirements URL cell."""
    if pd.isna(raw_url) or not str(raw_url).strip():
        return None

    filename = str(raw_url).strip().split("/")[-1].split("#")[0]
    if not filename:
        return None

    return filename.removesuffix(".html") + ".md"


def row_to_markdown(row) -> str:
    """
    Converts an Excel spreadsheet row into formatted markdown.
    """
    lines = ["## Entry\n"]
    for col, val in row.items():
        lines.append(f"- **{col}**: {val}")
    lines.append("")
    return "\n".join(lines)


def load_and_extract_ig_requirements(
    old_requirements_path: str,
    artifacts_dir: str,
    verbose: bool = False
) -> None:
    """
    Loads and extracts IG requirements from an Excel spreadsheet and saves the
    contents of each row in the spreadsheet to a markdown file corresponding to the
    HTML filename in the URL* column of the spreadsheet.

    Args:
        old_requirements_path: Local path of the first (old) IG requirements source
        artifacts_dir: Path to the base artifacts directory
        verbose: Whether to print progress messages
    """
    artifacts_path = Path(artifacts_dir)
    old_ig_requirements_markdown_output = artifacts_path / "ig" / "converted_markdown" / "old"
    old_ig_requirements_markdown_output.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"Created directory: {old_ig_requirements_markdown_output}")

    # Read the requirements Excel spreadsheet.
    df = pd.read_excel(Path(old_requirements_path), sheet_name='Requirements')

    # Store existing markdown file names from the URL* column of the spreadsheet in a set
    markdown_files = set()

    for _, row in df.iterrows():
        md_filename = _markdown_filename_from_requirement_url(row['URL*'])
        if md_filename is None:
            if verbose:
                print(f"Skipping row with empty or invalid URL*: {row['URL*']}")
            continue

        md_path = old_ig_requirements_markdown_output / md_filename
        content = row_to_markdown(row)

        if md_filename in markdown_files:
            with md_path.open("a", encoding="utf-8") as f:
                f.write(content)
        else:
            with md_path.open("w", encoding="utf-8") as f:
                f.write(f"# {md_filename.replace('.md', '').replace('-', ' ').title()}\n\n")
                f.write(content)

            markdown_files.add(md_filename)
