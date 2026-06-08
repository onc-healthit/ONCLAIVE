from pathlib import Path
import re


def _remove_no_differences_sections(markdown_content: str) -> tuple[str, int, int]:
    """
    Remove per-file sections that report no substantive differences.

    Returns:
        The filtered markdown, kept section count, and removed section count
    """
    lines = markdown_content.split('\n')
    result_lines = []

    target_phrase = "no substantive differences found"
    file_header_pattern = re.compile(r"^\s*#\s+")

    current_section = []
    has_no_differences = False
    kept_count = 0
    removed_count = 0

    for line in lines:
        if file_header_pattern.match(line):
            if current_section:
                if has_no_differences:
                    removed_count += 1
                else:
                    result_lines.extend(current_section)
                    kept_count += 1
            current_section = [line]
            has_no_differences = False
        else:
            current_section.append(line)

        if target_phrase in line.lower():
            has_no_differences = True

    if current_section:
        if has_no_differences:
            removed_count += 1
        else:
            result_lines.extend(current_section)
            kept_count += 1

    return "\n".join(result_lines), kept_count, removed_count


def clean_differences_markdown_file(file_path: Path) -> None:
    """Remove no-difference sections and normalize generated report whitespace."""
    content = file_path.read_text(encoding='utf-8')
    content, kept_count, removed_count = _remove_no_differences_sections(content)
    content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)
    content = re.sub(r"\n{3,}", "\n\n", content).strip()

    file_path.write_text(f"{content}\n" if content else "", encoding='utf-8')

    print(f"Cleaned differences file: {file_path}")
    print(
        f"Kept {kept_count} sections with substantive differences; "
        f"removed {removed_count} sections with no substantive differences."
    )
