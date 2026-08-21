"""
Create a file-based searchable inventory for Inferno test kits.

This first pass is intentionally deterministic: it scans Ruby DSL files,
requirements CSVs, and generated coverage CSVs, then writes JSONL records that
can later be enriched with LLM labels or embeddings.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable


FHIR_RESOURCE_TYPES = {
    "Account",
    "AllergyIntolerance",
    "Bundle",
    "CapabilityStatement",
    "CarePlan",
    "CareTeam",
    "Claim",
    "ClaimResponse",
    "Condition",
    "Coverage",
    "Device",
    "DiagnosticReport",
    "DocumentReference",
    "Encounter",
    "ExplanationOfBenefit",
    "Goal",
    "Immunization",
    "Location",
    "Medication",
    "MedicationRequest",
    "Observation",
    "OperationOutcome",
    "Organization",
    "Patient",
    "Practitioner",
    "PractitionerRole",
    "Procedure",
    "Provenance",
    "RelatedPerson",
}

DEFAULT_RUBY_GLOBS = ("*.rb",)
DEFAULT_SUITE_HINTS = {
    "c4bb_v110": "v1.1.0",
    "c4bb_v200": "v2.0.0",
    "c4bb_v200_client": "client/v2.0.0",
    "c4bb_v200devnonfinancial": "v2.0.0-dev-nonfinancial",
}


@dataclass
class RunnableRecord:
    record_type: str
    repo_name: str
    repo_url: str | None
    commit: str | None
    kit_id: str | None
    suite_hint: str | None
    runnable_type: str
    ruby_class: str | None
    id: str | None
    title: str | None
    description: str | None
    source_file: str
    line: int
    requirement_ids: list[str] = field(default_factory=list)
    requirement_sets: list[str] = field(default_factory=list)
    resource_types: list[str] = field(default_factory=list)
    profile_urls: list[str] = field(default_factory=list)
    search_parameters: list[str] = field(default_factory=list)
    must_support_elements: list[str] = field(default_factory=list)
    include_modules: list[str] = field(default_factory=list)
    group_refs: list[str] = field(default_factory=list)
    code_hash: str | None = None


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as output:
        for record in records:
            output.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            count += 1
    return count


def run_git(repo_path: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_path), *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def normalize_symbol(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    if value.startswith(":"):
        value = value[1:]
    return value.strip("\"'")


def unique(values: Iterable[str | None]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        if not value:
            continue
        clean = value.strip()
        if clean and clean not in seen:
            seen.add(clean)
            output.append(clean)
    return output


def relpath(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def find_balanced_percent_string(lines: list[str], start_idx: int, marker: str) -> str | None:
    first = lines[start_idx]
    marker_idx = first.find(marker)
    if marker_idx == -1:
        return None

    text_parts: list[str] = []
    depth = 0
    started = False
    for line in lines[start_idx:]:
        scan_start = 0
        if not started:
            scan_start = line.find(marker) + len(marker)
            started = True
            depth = 1

        chars: list[str] = []
        for char in line[scan_start:]:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return "\n".join(text_parts + ["".join(chars)]).strip()
            chars.append(char)
        text_parts.append("".join(chars).rstrip())

    return "\n".join(text_parts).strip() if text_parts else None


def find_heredoc(lines: list[str], start_idx: int) -> str | None:
    match = re.search(r"<<[-~]?['\"]?([A-Z_][A-Z0-9_]*)['\"]?", lines[start_idx])
    if not match:
        return None
    terminator = match.group(1)
    collected: list[str] = []
    for line in lines[start_idx + 1 :]:
        if line.strip() == terminator:
            return "\n".join(collected).strip()
        collected.append(line.rstrip())
    return None


def extract_call_text(lines: list[str], start_idx: int, name: str) -> str | None:
    line = lines[start_idx].strip()
    if not re.match(rf"{name}\b", line):
        return None

    single = re.search(rf"{name}\s+['\"]([^'\"]+)['\"]", line)
    if single:
        return single.group(1).strip()

    if "%(" in line:
        return find_balanced_percent_string(lines, start_idx, "%(")

    if "%Q(" in line:
        return find_balanced_percent_string(lines, start_idx, "%Q(")

    heredoc = find_heredoc(lines, start_idx)
    if heredoc:
        return heredoc

    return None


def extract_first_call(lines: list[str], name: str) -> str | None:
    for idx, line in enumerate(lines):
        if re.match(rf"\s*{name}\b", line):
            value = extract_call_text(lines, idx, name)
            if value:
                return value
    return None


def extract_first_id(block: str) -> str | None:
    match = re.search(r"^\s*id\s+(:[A-Za-z0-9_?!]+|['\"][^'\"]+['\"])", block, re.MULTILINE)
    return normalize_symbol(match.group(1)) if match else None


def extract_requirement_ids(block: str) -> list[str]:
    requirement_ids = re.findall(r"['\"]([A-Za-z0-9_.-]+@[A-Za-z0-9_.:-]+)['\"]", block)
    return unique(requirement_ids)


def extract_requirement_sets(block: str) -> list[str]:
    identifiers = re.findall(r"identifier:\s*['\"]([^'\"]+)['\"]", block)
    return unique(identifiers)


def extract_profile_urls(block: str) -> list[str]:
    urls = re.findall(r"https?://[^\s'\"),]+/StructureDefinition/[A-Za-z0-9_.:-]+", block)
    return unique(urls)


def extract_resource_types(block: str) -> list[str]:
    found = []
    for resource_type in sorted(FHIR_RESOURCE_TYPES):
        if re.search(rf"\b{re.escape(resource_type)}\b", block):
            found.append(resource_type)
    return found


def extract_include_modules(block: str) -> list[str]:
    modules = re.findall(r"^\s*include\s+([A-Za-z0-9_:]+)", block, re.MULTILINE)
    return unique(modules)


def extract_group_refs(block: str) -> list[str]:
    refs = re.findall(r"^\s*group\s+from:\s+(:[A-Za-z0-9_?!]+|['\"][^'\"]+['\"])", block, re.MULTILINE)
    return unique(normalize_symbol(ref) for ref in refs)


def extract_search_parameters(block: str) -> list[str]:
    candidates: list[str] = []
    searchy_lines = [
        line
        for line in block.splitlines()
        if re.search(r"search|params?|_include|_revinclude", line, re.IGNORECASE)
    ]
    for line in searchy_lines:
        candidates.extend(re.findall(r"['\"]([A-Za-z_][A-Za-z0-9_.:-]*)['\"]", line))
        bullet = re.match(r"\s*\*\s+`?([A-Za-z_][A-Za-z0-9_.:-]*)`?\s*$", line)
        if bullet:
            candidates.append(bullet.group(1))

    if re.search(r"search(?:ing)? (?:by|parameters?)", block, re.IGNORECASE):
        for line in block.splitlines():
            bullet = re.match(r"\s*\*\s+`?([A-Za-z_][A-Za-z0-9_.:-]*)`?\s*$", line)
            if bullet:
                candidates.append(bullet.group(1))

    candidates.extend(
        match.group(1)
        for match in re.finditer(r"search by\s+`?([A-Za-z_][A-Za-z0-9_.:-]*)`?", block, re.IGNORECASE)
    )

    ignored = FHIR_RESOURCE_TYPES | {
        "DELETE",
        "GET",
        "PATCH",
        "POST",
        "PUT",
        "all",
        "code",
        "fhirUser",
        "json",
        "launch",
        "openid",
        "post",
        "search",
        "system",
        "url",
    }
    normalized = (value.rstrip(":") for value in candidates)
    return unique(value for value in normalized if value not in ignored and len(value) <= 64)


def extract_must_support_elements(description: str | None) -> list[str]:
    if not description:
        return []
    elements = []
    for line in description.splitlines():
        match = re.match(r"\s*\*\s+([A-Za-z][A-Za-z0-9.:[\]x-]+)\s*$", line)
        if match and "." in match.group(1):
            elements.append(match.group(1))
    return unique(elements)


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def infer_suite_hint(path: Path) -> str | None:
    parts = path.parts
    if "generated" in parts:
        idx = parts.index("generated")
        if idx + 1 < len(parts):
            return parts[idx + 1]
    if "client" in parts:
        idx = parts.index("client")
        if idx + 1 < len(parts):
            return f"client/{parts[idx + 1]}"
    return None


def class_blocks(lines: list[str]) -> list[tuple[int, str, str, str]]:
    starts: list[tuple[int, str, str]] = []
    pattern = re.compile(r"^\s*class\s+([A-Za-z0-9_:]+)\s+<\s+Inferno::(TestSuite|TestGroup|Test)\b")
    for idx, line in enumerate(lines):
        match = pattern.match(line)
        if match:
            starts.append((idx, match.group(1), match.group(2)))

    blocks: list[tuple[int, str, str, str]] = []
    for index, (start_idx, ruby_class, superclass) in enumerate(starts):
        end_idx = starts[index + 1][0] if index + 1 < len(starts) else len(lines)
        blocks.append((start_idx + 1, ruby_class, superclass, "\n".join(lines[start_idx:end_idx])))
    return blocks


def inline_group_blocks(lines: list[str]) -> list[tuple[int, str]]:
    blocks: list[tuple[int, str]] = []
    for idx, line in enumerate(lines):
        if not re.match(r"^\s*(group|test)\s+do\b", line):
            continue

        depth = 0
        collected: list[str] = []
        for inner in lines[idx:]:
            depth += len(re.findall(r"\bdo\b", inner))
            depth -= len(re.findall(r"^\s*end\b", inner))
            collected.append(inner)
            if depth <= 0 and len(collected) > 1:
                break
        blocks.append((idx + 1, "\n".join(collected)))
    return blocks


def build_runnable_record(
    *,
    repo_root: Path,
    repo_name: str,
    repo_url: str | None,
    commit: str | None,
    kit_id: str | None,
    source_path: Path,
    line: int,
    runnable_type: str,
    ruby_class: str | None,
    block: str,
) -> RunnableRecord:
    block_lines = block.splitlines()
    title = extract_first_call(block_lines, "title")
    description = extract_first_call(block_lines, "description")

    return RunnableRecord(
        record_type="runnable",
        repo_name=repo_name,
        repo_url=repo_url,
        commit=commit,
        kit_id=kit_id,
        suite_hint=infer_suite_hint(source_path.relative_to(repo_root)),
        runnable_type=runnable_type,
        ruby_class=ruby_class,
        id=extract_first_id(block),
        title=title,
        description=description,
        source_file=relpath(source_path, repo_root),
        line=line,
        requirement_ids=extract_requirement_ids(block),
        requirement_sets=extract_requirement_sets(block),
        resource_types=extract_resource_types(block),
        profile_urls=extract_profile_urls(block),
        search_parameters=extract_search_parameters(block),
        must_support_elements=extract_must_support_elements(description),
        include_modules=extract_include_modules(block),
        group_refs=extract_group_refs(block),
        code_hash=hash_text(block),
    )


def extract_runnables(repo_root: Path, repo_name: str, repo_url: str | None, commit: str | None) -> list[dict[str, Any]]:
    metadata_file = repo_root / "lib" / "carin_for_blue_button_test_kit" / "metadata.rb"
    kit_id = None
    if metadata_file.exists():
        kit_id = extract_first_id(read_text(metadata_file))

    records: list[RunnableRecord] = []
    for path in sorted((repo_root / "lib").rglob("*.rb")):
        text = read_text(path)
        lines = text.splitlines()

        for line, ruby_class, superclass, block in class_blocks(lines):
            records.append(
                build_runnable_record(
                    repo_root=repo_root,
                    repo_name=repo_name,
                    repo_url=repo_url,
                    commit=commit,
                    kit_id=kit_id,
                    source_path=path,
                    line=line,
                    runnable_type=superclass,
                    ruby_class=ruby_class,
                    block=block,
                )
            )

        for line, block in inline_group_blocks(lines):
            runnable_id = extract_first_id(block)
            if not runnable_id and not extract_first_call(block.splitlines(), "title"):
                continue
            records.append(
                build_runnable_record(
                    repo_root=repo_root,
                    repo_name=repo_name,
                    repo_url=repo_url,
                    commit=commit,
                    kit_id=kit_id,
                    source_path=path,
                    line=line,
                    runnable_type="inline_group",
                    ruby_class=None,
                    block=block,
                )
            )

    return [asdict(record) for record in records]


def extract_kit_metadata(repo_root: Path, repo_name: str, repo_url: str | None, commit: str | None) -> dict[str, Any]:
    metadata_candidates = sorted((repo_root / "lib").rglob("metadata.rb"))
    metadata_text = read_text(metadata_candidates[0]) if metadata_candidates else ""
    metadata_lines = metadata_text.splitlines()

    suite_ids_match = re.search(r"suite_ids\s+\[([^\]]*)\]", metadata_text, re.DOTALL)
    suite_ids = []
    if suite_ids_match:
        suite_ids = unique(normalize_symbol(value) for value in re.findall(r":[A-Za-z0-9_?!]+|['\"][^'\"]+['\"]", suite_ids_match.group(1)))

    return {
        "record_type": "repo",
        "repo_name": repo_name,
        "repo_url": repo_url,
        "commit": commit,
        "kit_id": extract_first_id(metadata_text),
        "title": extract_first_call(metadata_lines, "title"),
        "description": extract_first_call(metadata_lines, "description"),
        "suite_ids": suite_ids,
        "version": extract_constant(repo_root / "lib" / "carin_for_blue_button_test_kit" / "version.rb", "VERSION"),
        "last_updated": extract_constant(repo_root / "lib" / "carin_for_blue_button_test_kit" / "version.rb", "LAST_UPDATED"),
        "source_file": relpath(metadata_candidates[0], repo_root) if metadata_candidates else None,
    }


def extract_constant(path: Path, name: str) -> str | None:
    if not path.exists():
        return None
    match = re.search(rf"\b{name}\s*=\s*['\"]([^'\"]+)['\"]", read_text(path))
    return match.group(1) if match else None


def read_csv_records(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def extract_requirements(repo_root: Path, repo_name: str, repo_url: str | None, commit: str | None) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted((repo_root / "lib").rglob("*requirements.csv")):
        if "/generated/" in path.as_posix():
            continue
        for row in read_csv_records(path):
            req_set = row.get("Req Set")
            req_id = row.get("ID")
            records.append(
                {
                    "record_type": "requirement",
                    "repo_name": repo_name,
                    "repo_url": repo_url,
                    "commit": commit,
                    "requirement_id": f"{req_set}@{req_id}" if req_set and req_id else req_id,
                    "req_set": req_set,
                    "id": req_id,
                    "url": row.get("URL"),
                    "requirement": row.get("Requirement"),
                    "conformance": row.get("Conformance"),
                    "actors": split_csvish(row.get("Actors")),
                    "conditionality": row.get("Conditionality"),
                    "not_tested_reason": row.get("Not Tested Reason"),
                    "not_tested_details": row.get("Not Tested Details"),
                    "source_file": relpath(path, repo_root),
                }
            )
    return records


def split_csvish(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def extract_coverage(repo_root: Path, repo_name: str, repo_url: str | None, commit: str | None) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted((repo_root / "lib").rglob("*requirements_coverage.csv")):
        suite_id = path.name.removesuffix("_requirements_coverage.csv")
        for row in read_csv_records(path):
            req_set = row.get("Req Set")
            req_id = row.get("ID")
            short_ids_key = next((key for key in row if key.endswith("Short ID(s)")), None)
            full_ids_key = next((key for key in row if key.endswith("Full ID(s)")), None)
            records.append(
                {
                    "record_type": "coverage",
                    "repo_name": repo_name,
                    "repo_url": repo_url,
                    "commit": commit,
                    "suite_id": suite_id,
                    "requirement_id": f"{req_set}@{req_id}" if req_set and req_id else req_id,
                    "req_set": req_set,
                    "id": req_id,
                    "url": row.get("URL"),
                    "conformance": row.get("Conformance"),
                    "actors": split_csvish(row.get("Actors")),
                    "conditionality": row.get("Conditionality"),
                    "not_tested_reason": row.get("Not Tested Reason"),
                    "short_ids": split_csvish(row.get(short_ids_key) if short_ids_key else None),
                    "full_ids": split_csvish(row.get(full_ids_key) if full_ids_key else None),
                    "source_file": relpath(path, repo_root),
                }
            )
    return records


def split_arg_values(values: list[str] | None) -> list[str]:
    if not values:
        return []
    return unique(part.strip() for value in values for part in value.split(","))


def suite_hints_for(suite_ids: list[str], explicit_hints: list[str]) -> list[str]:
    inferred = [DEFAULT_SUITE_HINTS[suite_id] for suite_id in suite_ids if suite_id in DEFAULT_SUITE_HINTS]
    return unique([*explicit_hints, *inferred])


def runnable_matches_suite(record: dict[str, Any], suite_ids: list[str], suite_hints: list[str]) -> bool:
    record_id = record.get("id") or ""
    source_file = record.get("source_file") or ""
    suite_hint = record.get("suite_hint") or ""

    if any(record_id == suite_id or record_id.startswith(f"{suite_id}_") for suite_id in suite_ids):
        return True
    if suite_hint in suite_hints:
        return True
    return any(f"/{hint}/" in f"/{source_file}" for hint in suite_hints)


def filter_runnables_by_suite(
    runnables: list[dict[str, Any]],
    suite_ids: list[str],
    suite_hints: list[str],
) -> list[dict[str, Any]]:
    if not suite_ids and not suite_hints:
        return runnables

    by_id = {
        record["id"]: record
        for record in runnables
        if record.get("id")
    }
    selected_ids = [
        record["id"]
        for record in runnables
        if record.get("id") and runnable_matches_suite(record, suite_ids, suite_hints)
    ]
    selected_id_set: set[str] = set()
    queue = list(selected_ids)

    while queue:
        record_id = queue.pop(0)
        if record_id in selected_id_set:
            continue
        selected_id_set.add(record_id)
        for ref in by_id.get(record_id, {}).get("group_refs") or []:
            if ref in by_id and ref not in selected_id_set:
                queue.append(ref)

    filtered: list[dict[str, Any]] = []
    seen: set[int] = set()
    for index, record in enumerate(runnables):
        record_id = record.get("id")
        include_record = (
            bool(record_id and record_id in selected_id_set)
            or runnable_matches_suite(record, suite_ids, suite_hints)
        )
        if include_record and index not in seen:
            seen.add(index)
            filtered.append(record)
    return filtered


def filter_coverage_by_suite(coverage: list[dict[str, Any]], suite_ids: list[str]) -> list[dict[str, Any]]:
    if not suite_ids:
        return coverage
    suite_id_set = set(suite_ids)
    return [record for record in coverage if record.get("suite_id") in suite_id_set]


def filter_requirements_by_references(
    requirements: list[dict[str, Any]],
    coverage: list[dict[str, Any]],
    runnables: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    referenced_ids = set()
    for record in coverage:
        requirement_id = record.get("requirement_id")
        if requirement_id:
            referenced_ids.add(requirement_id)
    for record in runnables:
        referenced_ids.update(record.get("requirement_ids") or [])

    if not referenced_ids:
        return []
    return [record for record in requirements if record.get("requirement_id") in referenced_ids]


def filter_repo_metadata(repo_metadata: dict[str, Any], suite_ids: list[str]) -> dict[str, Any]:
    if not suite_ids:
        return repo_metadata
    filtered = dict(repo_metadata)
    wanted = set(suite_ids)
    filtered["suite_ids"] = [suite_id for suite_id in repo_metadata.get("suite_ids", []) if suite_id in wanted]
    filtered["inventory_scope"] = {
        "suite_ids": suite_ids,
    }
    return filtered


def inventory_repo(
    repo_root: Path,
    output_dir: Path,
    suite_ids: list[str] | None = None,
    suite_hints: list[str] | None = None,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    output_dir = output_dir.resolve()
    repo_name = repo_root.name
    repo_url = run_git(repo_root, "config", "--get", "remote.origin.url")
    commit = run_git(repo_root, "rev-parse", "HEAD")
    suite_ids = suite_ids or []
    suite_hints = suite_hints or []

    repo_metadata = extract_kit_metadata(repo_root, repo_name, repo_url, commit)
    runnables = extract_runnables(repo_root, repo_name, repo_url, commit)
    requirements = extract_requirements(repo_root, repo_name, repo_url, commit)
    coverage = extract_coverage(repo_root, repo_name, repo_url, commit)

    if suite_ids or suite_hints:
        runnables = filter_runnables_by_suite(runnables, suite_ids, suite_hints)
        coverage = filter_coverage_by_suite(coverage, suite_ids)
        requirements = filter_requirements_by_references(requirements, coverage, runnables)
        repo_metadata = filter_repo_metadata(repo_metadata, suite_ids)

    counts = {
        "repos": write_jsonl(output_dir / "repos.jsonl", [repo_metadata]),
        "runnables": write_jsonl(output_dir / "runnables.jsonl", runnables),
        "requirements": write_jsonl(output_dir / "requirements.jsonl", requirements),
        "coverage": write_jsonl(output_dir / "coverage.jsonl", coverage),
    }

    summary = {
        "repo_root": str(repo_root),
        "output_dir": str(output_dir),
        "repo_name": repo_name,
        "repo_url": repo_url,
        "commit": commit,
        "filters": {
            "suite_ids": suite_ids,
            "suite_hints": suite_hints,
        },
        "counts": counts,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inventory an Inferno test kit into JSONL files.")
    parser.add_argument("repo", type=Path, help="Path to a cloned Inferno test kit repository")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("inferno-test-kits/inventory"),
        help="Directory where JSONL inventory files will be written",
    )
    parser.add_argument(
        "--suite-id",
        action="append",
        default=None,
        help="Limit inventory to suite ID(s), e.g. --suite-id c4bb_v110. Can be repeated or comma-separated.",
    )
    parser.add_argument(
        "--suite-hint",
        action="append",
        default=None,
        help="Limit inventory to suite path hint(s), e.g. --suite-hint v1.1.0. Can be repeated or comma-separated.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    suite_ids = split_arg_values(args.suite_id)
    suite_hints = suite_hints_for(suite_ids, split_arg_values(args.suite_hint))
    summary = inventory_repo(args.repo, args.output_dir, suite_ids=suite_ids, suite_hints=suite_hints)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
