#!/usr/bin/env python3
"""
diff_to_change_ledger.py  (v2)

Converts a FHIR IG markdown diff file into a raw structured YAML change ledger.
Each atomic change becomes one YAML record.

Supports two diff input types — both produce the same output schema:

  reqs-to-narrative   (reqs_difference_output_*.md)
    Old requirements come from the XLSX; structured tags in the diff will
    have real integer IDs. old_requirement_ids is always authoritative.

  narrative-to-narrative   (differences_*.md)
    Both sides are IG narrative text. If --reqs-xlsx is also provided the
    diff prompt embeds the XLSX as context, so tags may have real IDs.
    If no XLSX was provided, tags will have ID=none but still carry
    Conformance/Actor inferred from the old narrative text.

In all cases the script extracts whatever structured metadata is present in
the tags and only falls back to LLM inference for fields it cannot determine
directly. It does not add Inferno test-kit inventory matches; run
inventory_change_enricher.py as a separate step when you want test-kit context.

Usage:
    python diff_to_change_ledger_v2.py \\
        --diff-file carin-bb-comparison/ig/reqs_difference_output_20240101_120000.md \\
        [--output-dir carin-bb-comparison/ig] \\
        [--reqs-xlsx carin-bb-comparison/ig/hl7.fhir.us.carin-bb_2.0.0_reqs.xlsx] \\
        [--provider claude|openai]

Environment variables:
    ANTHROPIC_API_KEY   — required when --provider claude (default)
    OPENAI_API_KEY      — required when --provider openai
"""

import argparse
import json
import os
import re
import sys
import textwrap
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


# ---------------------------------------------------------------------------
# LLM provider abstraction
# ---------------------------------------------------------------------------

def _call_claude(prompt: str, system: str, api_key: str) -> str:
    try:
        import anthropic
    except ImportError:
        sys.exit("anthropic package not installed. Run: pip install anthropic")
    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def _call_openai(prompt: str, system: str, api_key: str) -> str:
    try:
        import openai
    except ImportError:
        sys.exit("openai package not installed. Run: pip install openai")
    client = openai.OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-5.5",
        instructions=system,
        input=prompt,
    )
    for item in response.output:
        if item.type == "message":
            for block in item.content:
                if block.type == "output_text":
                    return block.text
    return ""


def call_llm(prompt: str, system: str, provider: str) -> str:
    if provider == "claude":
        api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            sys.exit("ANTHROPIC_API_KEY environment variable not set.")
        return _call_claude(prompt, system, api_key)
    elif provider == "openai":
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            sys.exit("OPENAI_API_KEY environment variable not set.")
        return _call_openai(prompt, system, api_key)
    else:
        sys.exit(f"Unknown provider: {provider}")


# ---------------------------------------------------------------------------
# Metadata tag parser
# ---------------------------------------------------------------------------

# Matches: [ID=122, Conformance=SHOULD NOT, Actor=Consumer, Scope=AUTOMATION, Planning To Test=Yes]
# or:      [ID=none, Conformance=SHALL, Actor=Health Plan, Scope=unknown, Planning To Test=unknown]
# or just: [ID=none]
_META_TAG_RE = re.compile(
    r'\[ID=(?P<id>[^\],]+?)'
    r'(?:,\s*Conformance=(?P<conformance>[^\],]+?))?'
    r'(?:,\s*Actor=(?P<actor>[^\],]+?))?'
    r'(?:,\s*Scope=(?P<scope>[^\],]+?))?'
    r'(?:,\s*Planning\s+To\s+Test=(?P<planning>[^\]]+?))?\s*\]',
    re.IGNORECASE,
)


def parse_metadata_tags(text: str) -> list[dict]:
    """
    Extract all [ID=..., ...] metadata tag lines from a diff subsection.
    Returns a list of dicts, one per tag found. Works for both real IDs
    (reqs-to-narrative) and ID=none with inferred fields (narrative-to-narrative).
    """
    results = []
    for m in _META_TAG_RE.finditer(text):
        raw_id = m.group("id").strip()
        results.append({
            "raw_id": raw_id,
            "id": None if raw_id.lower() == "none" else _safe_int(raw_id),
            "conformance": (m.group("conformance") or "").strip() or None,
            "actor": (m.group("actor") or "").strip() or None,
            "scope": (m.group("scope") or "").strip() or None,
            "planning_to_test": (m.group("planning") or "").strip() or None,
        })
    return results


def _safe_int(val: str) -> int | None:
    try:
        return int(val)
    except (ValueError, TypeError):
        return None


def _merge_tags(tags: list[dict]) -> dict:
    """
    Collapse a list of tag dicts into a single metadata dict.
    For narrative-to-narrative diffs, IDs may all be None but
    conformance/actor/scope are still worth carrying through.
    """
    ids = [t["id"] for t in tags if t["id"] is not None]
    first = next((t for t in tags if t.get("conformance")), tags[0] if tags else {})
    return {
        "old_requirement_ids": ids,
        "old_conformance": first.get("conformance") or "unknown",
        "actor": first.get("actor") or "unknown",
        "scope": first.get("scope") or "unknown",
        "planning_to_test": first.get("planning_to_test") or "unknown",
        # Track whether IDs came from a real table or were inferred from narrative
        "ids_source": "table" if ids else "inferred",
    }


def _no_tags_metadata() -> dict:
    """Fallback metadata when no tags were found at all (old prompt format)."""
    return {
        "old_requirement_ids": [],
        "old_conformance": "unknown",
        "actor": "unknown",
        "scope": "unknown",
        "planning_to_test": "unknown",
        "ids_source": "none",
    }


# ---------------------------------------------------------------------------
# Markdown diff parser
# ---------------------------------------------------------------------------

SKIP_PATTERNS = [
    re.compile(r"no\s+substantive\s+differences?\s+found", re.IGNORECASE),
    re.compile(r"cannot\s+(perform|be\s+compared?|compare)", re.IGNORECASE),
    re.compile(r"no\s+changes?\s+detected", re.IGNORECASE),
    re.compile(r"files?\s+(are\s+)?identical", re.IGNORECASE),
    re.compile(r"unable\s+to\s+compare", re.IGNORECASE),
    re.compile(r"old[_\s]ig[_\s]requirements.*?is\s+empty", re.IGNORECASE),
]


def _is_skippable(text: str) -> tuple[bool, str]:
    for pat in SKIP_PATTERNS:
        if pat.search(text):
            tag = "cannot_compare" if any(
                kw in pat.pattern for kw in ("cannot", "unable", "empty")
            ) else "no_change"
            return True, tag
    return False, ""


def parse_diff_file(path: Path) -> tuple[list[dict], list[dict]]:
    """
    Split the diff markdown on top-level `#` headings.

    Returns:
        artifacts — list of {"filename": str, "content": str}
        skipped   — list of {"filename": str, "reason": str}
    """
    text = path.read_text(encoding="utf-8")
    sections = re.split(r"(?m)^(?=#[^#])", text)
    artifacts: list[dict] = []
    skipped: list[dict] = []

    for section in sections:
        section = section.strip()
        if not section:
            continue
        first_line, _, body = section.partition("\n")
        filename = first_line.lstrip("#").strip()
        if not filename:
            continue
        skippable, reason = _is_skippable(body)
        if skippable:
            skipped.append({"filename": filename, "reason": reason})
        else:
            artifacts.append({"filename": filename, "content": section})

    return artifacts, skipped


# ---------------------------------------------------------------------------
# Subsection splitter
# ---------------------------------------------------------------------------

def split_into_subsections(artifact_content: str) -> dict[str, str]:
    """
    Split one artifact section (under a single # heading) into its ##
    subsections. Returns {heading_text: full_subsection_text}.
    Heading text has any leading "N. " or "N) " numbering stripped.
    """
    parts = re.split(r"(?m)^(?=##[^#])", artifact_content)
    result = {}
    for part in parts:
        part = part.strip()
        if not part or part.startswith("# "):
            continue
        first_line, _, _ = part.partition("\n")
        heading = first_line.lstrip("#").strip()
        heading = re.sub(r"^\d+[\.\)]\s*", "", heading)
        result[heading] = part
    return result


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = textwrap.dedent("""\
    You are a seasoned Healthcare Integration Test Engineer specialising in FHIR
    Implementation Guides and the Inferno test framework. Your task is to classify
    structured change records from IG diff narratives so that another engineer can
    update the test kit correctly.
""")

EXTRACTION_PROMPT_TEMPLATE = textwrap.dedent("""\
    ## Task
    For each numbered change subsection in the IG diff below, return one JSON object.

    Some fields have already been extracted from structured metadata tags in the diff
    and are provided in the PRE-FILLED METADATA block. Copy them verbatim — do not
    override or re-infer them.

    Your job is to determine the remaining fields that require reasoning:
      - artifact_type, artifact_id, affected_resource
      - element_paths
      - change_type  (from vocabulary below)
      - new_conformance
      - summary
      - test_action  (from vocabulary below)
      - confidence

    Note on ids_source:
      "table"    — old_requirement_ids came from a requirements spreadsheet; trust them completely.
      "inferred" — IDs are empty but old_conformance/actor were inferred from the old narrative text;
                   still copy them exactly.
      "none"     — no structured tags found; you may infer old_conformance and actor from the diff text.

    ## Change type vocabulary (use ONLY these values)
    conformance_escalation, conformance_demotion, new_requirement_added,
    requirement_removed, actor_change, new_element_or_extension,
    scope_conditionality_change, terminology_valueset_change,
    deprecated_reinstated, external_dependency_versioned, suite_level_config_change

    ## Test action vocabulary (use ONLY these values)
    add_required_assertion, delete_or_make_optional, author_new_test,
    delete_test_block, move_between_suites, add_to_must_support,
    update_preconditions, update_fixture_or_assertion, reenable_test,
    pin_version_in_config, update_suite_config, manual_review

    ## Output schema — return a JSON array, one object per change subsection
    {{
      "source_artifact": "<filename>",
      "source_section": "<## heading text, without leading number>",
      "artifact_type": "<StructureDefinition|ValueSet|CapabilityStatement|...>",
      "artifact_id": "<local artifact id>",
      "affected_resource": "<FHIR resource type>",
      "element_paths": ["<dot-notation path>"],
      "change_type": "<from vocab>",
      "old_conformance": "<PRE-FILLED — copy exactly>",
      "new_conformance": "<SHALL|SHOULD|MAY|SHOULD NOT|SHALL NOT|guidance_only|none|unknown>",
      "actor": "<PRE-FILLED — copy exactly>",
      "summary": "<one sentence plain-English summary>",
      "old_text": "<verbatim old text from diff>",
      "new_text": "<verbatim new text from diff>",
      "test_action": "<from vocab>",
      "confidence": "<high|medium|low>",
      "old_requirement_ids": [<PRE-FILLED — copy exactly>],
      "planning_to_test": "<PRE-FILLED — copy exactly>",
      "scope": "<PRE-FILLED — copy exactly>",
      "ids_source": "<PRE-FILLED — copy exactly>",
      "source_of_truth_status": "unverified"
    }}

    Rules:
    - Return ONLY a JSON array, no prose, no markdown fences.
    - Fields marked PRE-FILLED must be copied verbatim from the metadata block.
    - If ids_source is "none", you may infer old_conformance and actor from the diff text.
    - If element_paths cannot be determined, return [].
    - Use "unknown" for artifact fields you cannot determine.
    - If a subsection describes two truly independent changes to different elements, emit two records.

    ## Pre-filled metadata per change (keyed by subsection heading)
    {metadata_block}

    ## IG Diff Section
    {diff_section}
""")


def build_prompt(diff_section: str, tags_by_section: dict[str, dict]) -> str:
    metadata_lines = []
    for heading, merged in tags_by_section.items():
        metadata_lines.append(f"### {heading}")
        for key in ("old_requirement_ids", "old_conformance", "actor",
                    "scope", "planning_to_test", "ids_source"):
            metadata_lines.append(f"  {key}: {merged.get(key)}")
    metadata_block = "\n".join(metadata_lines) if metadata_lines else "(none)"
    return EXTRACTION_PROMPT_TEMPLATE.format(
        diff_section=diff_section,
        metadata_block=metadata_block,
    )


# ---------------------------------------------------------------------------
# JSON parsing & schema validation
# ---------------------------------------------------------------------------

CHANGE_TYPES = {
    "conformance_escalation", "conformance_demotion", "new_requirement_added",
    "requirement_removed", "actor_change", "new_element_or_extension",
    "scope_conditionality_change", "terminology_valueset_change",
    "deprecated_reinstated", "external_dependency_versioned",
    "suite_level_config_change",
}

TEST_ACTIONS = {
    "add_required_assertion", "delete_or_make_optional", "author_new_test",
    "delete_test_block", "move_between_suites", "add_to_must_support",
    "update_preconditions", "update_fixture_or_assertion", "reenable_test",
    "pin_version_in_config", "update_suite_config", "manual_review",
}


def _coerce_ids(raw: Any) -> list[int]:
    if not raw:
        return []
    if isinstance(raw, list):
        result = []
        for x in raw:
            try:
                result.append(int(x))
            except (ValueError, TypeError):
                pass
        return result
    try:
        return [int(raw)]
    except (ValueError, TypeError):
        return []


def parse_llm_response(text: str) -> list[dict]:
    clean = re.sub(r"```(?:json)?\s*", "", text).strip().rstrip("`").strip()
    try:
        data = json.loads(clean)
    except json.JSONDecodeError:
        m = re.search(r"\[.*\]", clean, re.DOTALL)
        if m:
            try:
                data = json.loads(m.group(0))
            except json.JSONDecodeError:
                print("  WARNING: Could not parse LLM response as JSON. Skipping.")
                return []
        else:
            print("  WARNING: No JSON array found in LLM response. Skipping.")
            return []

    if not isinstance(data, list):
        data = [data]

    records = []
    for item in data:
        if not isinstance(item, dict):
            continue
        if item.get("change_type") not in CHANGE_TYPES:
            item["change_type"] = "manual_review"
        if item.get("test_action") not in TEST_ACTIONS:
            item["test_action"] = "manual_review"
        item["old_requirement_ids"] = _coerce_ids(item.get("old_requirement_ids"))
        item.setdefault("source_of_truth_status", "unverified")
        item.setdefault("element_paths", [])
        item.setdefault("confidence", "low")
        item.setdefault("ids_source", "none")
        records.append(item)
    return records


# ---------------------------------------------------------------------------
# Apply pre-filled metadata (always wins over LLM output)
# ---------------------------------------------------------------------------

def apply_prefilled_metadata(records: list[dict], tags_by_section: dict[str, dict]) -> list[dict]:
    """
    Overwrite metadata fields in each record with the pre-parsed tag values.
    For ids_source="none" sections the LLM may have filled these in from the
    diff text, which is fine — we still let the structured tags win if present.
    """
    for rec in records:
        section = re.sub(r"^\d+[\.\)]\s*", "", rec.get("source_section", ""))
        merged = tags_by_section.get(section) or tags_by_section.get(rec.get("source_section", ""))
        if not merged:
            continue
        # Always overwrite these from tags regardless of ids_source
        rec["old_requirement_ids"] = merged["old_requirement_ids"]
        rec["ids_source"] = merged["ids_source"]
        # Only overwrite conformance/actor/scope/planning if tags had real values
        if merged["ids_source"] in ("table", "inferred"):
            rec["old_conformance"] = merged["old_conformance"]
            rec["actor"] = merged["actor"]
            rec["scope"] = merged["scope"]
            rec["planning_to_test"] = merged["planning_to_test"]
    return records


# ---------------------------------------------------------------------------
# change_id generation
# ---------------------------------------------------------------------------

def _artifact_slug(filename: str) -> str:
    name = Path(filename).stem
    name = re.sub(
        r"^(StructureDefinition|ValueSet|CapabilityStatement|CodeSystem"
        r"|SearchParameter|OperationDefinition|Extension)-",
        "", name, flags=re.IGNORECASE,
    )
    abbrevs = {
        "ExplanationOfBenefit": "eob",
        "Coverage": "cov",
        "Organization": "org",
        "Patient": "pat",
        "Practitioner": "prac",
        "RelatedPerson": "rp",
    }
    for long, short in abbrevs.items():
        name = name.replace(long, short)
    return name.lower()


def assign_change_ids(records: list[dict], artifact_filename: str) -> list[dict]:
    slug = _artifact_slug(artifact_filename)
    for i, rec in enumerate(records, start=1):
        rec["change_id"] = f"{slug}-{i:03d}"
    return records


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run(
    diff_file: Path,
    output_dir: Path,
    reqs_xlsx: Path | None,
    provider: str,
) -> None:
    ts = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"change_ledger_raw_{ts}.yaml"

    print(f"\n{'='*60}")
    print(f"FHIR IG Diff → Change Ledger  (v2)")
    print(f"  diff file  : {diff_file}")
    print(f"  output     : {output_file}")
    print(f"  reqs xlsx  : {reqs_xlsx or 'not provided'}")
    print(f"  provider   : {provider}")
    print(f"  stage      : raw IG change ledger only")
    print(f"{'='*60}\n")

    artifacts, skipped = parse_diff_file(diff_file)
    print(f"Parsed {len(artifacts)} artifact sections with changes, "
          f"{len(skipped)} skipped (no-change / cannot-compare).")

    all_records: list[dict] = []
    skipped_records = [{"source_artifact": e["filename"], "status": e["reason"]} for e in skipped]
    stats_by_type: dict[str, int] = {}
    total_changes = 0

    for idx, artifact in enumerate(artifacts, start=1):
        filename = artifact["filename"]
        content = artifact["content"]
        print(f"[{idx}/{len(artifacts)}] Processing: {filename}")

        # Extract structured metadata tags from each subsection
        subsections = split_into_subsections(content)
        tags_by_section: dict[str, dict] = {}
        for heading, body in subsections.items():
            tags = parse_metadata_tags(body)
            tags_by_section[heading] = _merge_tags(tags) if tags else _no_tags_metadata()

        ids_found = sum(1 for v in tags_by_section.values() if v["old_requirement_ids"])
        inferred = sum(1 for v in tags_by_section.values() if v["ids_source"] == "inferred")
        no_tags = sum(1 for v in tags_by_section.values() if v["ids_source"] == "none")
        print(f"  {len(subsections)} subsection(s) — "
              f"{ids_found} with table IDs, {inferred} with inferred metadata, {no_tags} with no tags.")

        prompt = build_prompt(content, tags_by_section)
        try:
            raw_response = call_llm(prompt, SYSTEM_PROMPT, provider)
        except Exception as exc:
            print(f"  ERROR calling LLM: {exc}")
            all_records.append({
                "change_id": None,
                "source_artifact": filename,
                "status": "llm_error",
                "error": str(exc),
            })
            continue

        records = parse_llm_response(raw_response)
        records = apply_prefilled_metadata(records, tags_by_section)
        records = assign_change_ids(records, filename)

        for rec in records:
            ct = rec.get("change_type", "unknown")
            stats_by_type[ct] = stats_by_type.get(ct, 0) + 1

        total_changes += len(records)
        all_records.extend(records)
        print(f"  → {len(records)} change(s) extracted.")

    output_dir.mkdir(parents=True, exist_ok=True)
    output_data = {
        "meta": {
            "ledger_stage": "raw_ig_change_ledger",
            "inventory_enriched": False,
            "diff_file": str(diff_file),
            "reqs_xlsx": str(reqs_xlsx) if reqs_xlsx else None,
            "provider": provider,
            "generated_at": ts,
            "total_artifacts_processed": len(artifacts),
            "total_skipped": len(skipped),
            "total_changes_extracted": total_changes,
        },
        "changes": all_records,
        "skipped": skipped_records,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump(output_data, f, Dumper=NoAliasDumper, allow_unicode=True,
                  sort_keys=False, default_flow_style=False, width=120)

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"  Artifacts processed : {len(artifacts)}")
    print(f"  Artifacts skipped   : {len(skipped)}")
    print(f"  Total changes       : {total_changes}")
    print(f"\n  Changes by type:")
    for ctype, count in sorted(stats_by_type.items(), key=lambda x: -x[1]):
        print(f"    {ctype:<40} {count}")
    print(f"\n  Output: {output_file}")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a FHIR IG markdown diff into a raw structured YAML change ledger (v2).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              # Reqs-to-narrative diff, with XLSX (recommended)
              python diff_to_change_ledger_v2.py \\
                  --diff-file carin-bb-comparison/ig/reqs_difference_output_20240101_120000.md \\
                  --reqs-xlsx carin-bb-comparison/ig/hl7.fhir.us.carin-bb_2.0.0_reqs.xlsx

              # Narrative-to-narrative diff, XLSX as optional context
              python diff_to_change_ledger_v2.py \\
                  --diff-file carin-bb-comparison/ig/differences_20240101_120000.md \\
                  --reqs-xlsx carin-bb-comparison/ig/hl7.fhir.us.carin-bb_2.0.0_reqs.xlsx

              # Narrative-to-narrative diff, no XLSX
              python diff_to_change_ledger_v2.py \\
                  --diff-file carin-bb-comparison/ig/differences_20240101_120000.md

              # Add deterministic Inferno inventory matches in a separate step:
              python inventory_change_enricher.py \\
                  carin-bb-comparison/ig/change_ledger_raw_20240101_120000.yaml \\
                  --inventory-dir inferno-test-kits/inventory/carin-for-blue-button-test-kit-v110
        """),
    )
    parser.add_argument("--diff-file", "-d", required=True, type=Path,
                        help="Path to the markdown diff file")
    parser.add_argument("--output-dir", "-o", type=Path, default=None,
                        help="Directory for YAML output (default: same dir as diff file)")
    parser.add_argument("--reqs-xlsx", "-r", type=Path, default=None,
                        help="Optional path to the old-version requirements XLSX")
    parser.add_argument("--provider", choices=["claude", "openai"], default="claude",
                        help="LLM provider (default: claude)")

    args = parser.parse_args()

    if not args.diff_file.exists():
        sys.exit(f"Diff file not found: {args.diff_file}")
    if args.reqs_xlsx and not args.reqs_xlsx.exists():
        sys.exit(f"Requirements XLSX not found: {args.reqs_xlsx}")

    run(
        diff_file=args.diff_file,
        output_dir=args.output_dir or args.diff_file.parent,
        reqs_xlsx=args.reqs_xlsx,
        provider=args.provider,
    )


if __name__ == "__main__":
    main()
