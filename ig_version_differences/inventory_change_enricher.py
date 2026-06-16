#!/usr/bin/env python3
"""
Enrich IG change ledgers with deterministic Inferno test-kit inventory context.

The LLM-generated change ledger explains what changed in the IG. This module
adds the "where should I look in the test kit?" layer by matching each change
against the JSONL inventory produced by pipeline/inferno_inventory.py.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable

import yaml


DEFAULT_REQ_SET = None
GENERIC_ARTIFACT_IDS = {"carin bb", "c4bb", "implementationguide", "unknown", "none"}
GENERIC_QUERY_TERMS = {"unknown", "none", "implementationguide"}
FHIR_INTERACTIONS = {
    "batch",
    "capabilities",
    "create",
    "delete",
    "history-instance",
    "history-system",
    "history-type",
    "patch",
    "read",
    "search-system",
    "search-type",
    "transaction",
    "update",
    "vread",
}
CONFORMANCE_STRENGTHS = {
    "MAY": "optional",
    "SHOULD": "recommended",
    "SHALL": "required",
    "SHALL NOT": "required_prohibition",
    "MUST": "required",
    "MUST NOT": "required_prohibition",
    "GUIDANCE_ONLY": "guidance_only",
    "UNKNOWN": "unknown",
}
OPTIONAL_OR_RECOMMENDED_CONFORMANCE = {"MAY", "SHOULD"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def unique(values: Iterable[Any]) -> list[Any]:
    output: list[Any] = []
    seen: set[str] = set()
    for value in values:
        if value is None or value == "":
            continue
        marker = json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else str(value)
        if marker not in seen:
            seen.add(marker)
            output.append(value)
    return output


def sorted_unique_text(values: Iterable[Any]) -> list[str]:
    return sorted(str(value) for value in unique(values) if value not in (None, ""))


def split_cli_values(values: list[str] | None) -> list[str]:
    if not values:
        return []
    return [str(value) for value in unique(part.strip() for value in values for part in value.split(","))]


def normalize_text(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def normalize_path(value: str) -> str:
    value = value.strip()
    value = value.replace("[x]", "")
    value = re.sub(r"\[[^\]]+\]", "", value)
    return value


def artifact_slug(value: str | None) -> str:
    if not value:
        return ""
    name = Path(value).stem
    name = re.sub(
        r"^(StructureDefinition|ValueSet|CapabilityStatement|CodeSystem|SearchParameter|OperationDefinition|Extension)-",
        "",
        name,
        flags=re.IGNORECASE,
    )
    return normalize_text(name)


def source_artifact_type(value: str | None) -> str:
    name = Path(value or "").name
    match = re.match(r"([A-Za-z]+)-", name)
    if match:
        return match.group(1)
    if name:
        return Path(name).stem
    return "unknown"


def profile_local_id(value: str) -> str:
    """Return the local StructureDefinition id from a profile id or canonical URL."""
    match = re.search(r"/StructureDefinition/([^/#?]+)", value)
    if match:
        return match.group(1)
    return Path(value).stem


def profile_source_token(value: str) -> str:
    """
    Convert a profile id into the generated-test source token used by Inferno.

    Example:
      C4BB-ExplanationOfBenefit-Inpatient-Institutional -> eob_inpatient_institutional
      C4BB-Coverage -> coverage
    """
    local_id = profile_local_id(value)
    name = Path(local_id).stem
    name = re.sub(
        r"^(StructureDefinition|ValueSet|CapabilityStatement|CodeSystem|SearchParameter|OperationDefinition|Extension)-",
        "",
        name,
        flags=re.IGNORECASE,
    )
    name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
    words = [word for word in normalize_text(name).split() if word and word != "c4bb"]

    source_words: list[str] = []
    idx = 0
    while idx < len(words):
        if words[idx] == "c4bb":
            idx += 1
            continue
        if words[idx : idx + 2] == ["c4", "bb"]:
            idx += 2
            continue
        if words[idx : idx + 3] == ["explanation", "of", "benefit"]:
            source_words.append("eob")
            idx += 3
            continue
        source_words.append(words[idx])
        idx += 1

    return "_".join(source_words)


def profile_filter_match_reasons(runnable: dict[str, Any], profile_filters: list[str]) -> list[str]:
    """
    Return deterministic reasons a runnable appears to belong to a requested profile.

    This uses deterministic hints in the inventory: profile URLs, generated source
    paths, runnable IDs, and group file names. It intentionally does not use the
    generic FHIR resource type alone, because a resource can have multiple profiles.
    """
    if not profile_filters:
        return []

    profile_urls = [str(url) for url in runnable.get("profile_urls") or []]
    source_file = str(runnable.get("source_file") or "")
    search_blob = f"/{source_file.lower()}|"
    reasons: list[str] = []

    for profile_filter in profile_filters:
        local_id = profile_local_id(profile_filter)
        source_token = profile_source_token(profile_filter)
        if not source_token:
            continue

        normalized_local_id = normalize_text(local_id)
        if any(normalized_local_id == normalize_text(profile_local_id(url)) for url in profile_urls):
            if len(profile_urls) == 1:
                reasons.append(f"profile URL match: {local_id}")
            else:
                reasons.append(f"broad profile URL match: {local_id}")

        source_patterns = [
            f"/{source_token}/",
            f"/{source_token}_group.rb",
        ]
        if any(pattern in search_blob for pattern in source_patterns):
            reasons.append(f"profile source path match: {local_id}")

    return unique(reasons)


def runnable_matches_profile_filter(runnable: dict[str, Any], profile_filters: list[str]) -> bool:
    if not profile_filters:
        return True
    return bool(profile_filter_match_reasons(runnable, profile_filters))


def profile_match_score(reasons: list[str]) -> int:
    score = 0
    for reason in reasons:
        if reason.startswith("profile source path match:"):
            score += 22
        elif reason.startswith("profile URL match:"):
            score += 16
        elif reason.startswith("broad profile URL match:"):
            score += 6
    return min(score, 32)


def infer_change_profile_filters(change: dict[str, Any]) -> list[str]:
    """Infer precise StructureDefinition profile filters directly named by a change."""
    text_values: list[str] = []
    for key in ("artifact_id", "source_artifact", "source_section", "summary", "old_text", "new_text"):
        value = change.get(key)
        if value:
            text_values.append(str(value))
    text_values.extend(str(value) for value in change.get("element_paths") or [])

    profiles: list[str] = []
    for text in text_values:
        profiles.extend(
            match.group(1)
            for match in re.finditer(r"/StructureDefinition/([A-Za-z0-9_.:-]+)", text)
        )
        profiles.extend(
            match.group(1)
            for match in re.finditer(
                r"\bStructureDefinition-([A-Za-z][A-Za-z0-9_:-]+)(?=\.(?:html|md|json|xml|ttl)|\b)",
                text,
            )
        )
        profiles.extend(match.group(1) for match in re.finditer(r"\b(C4BB-[A-Za-z0-9_.:-]+)\b", text))

    affected_resource = normalize_text(change.get("affected_resource"))
    filtered_profiles: list[str] = []
    for profile in unique(profiles):
        local_id = profile_local_id(str(profile))
        normalized_local_id = normalize_text(local_id)
        if affected_resource and affected_resource not in {"unknown", "none"}:
            if affected_resource not in normalized_local_id:
                continue
        filtered_profiles.append(local_id)

    return filtered_profiles


def normalize_conformance(value: Any) -> str:
    text = normalize_text(value).upper().replace(" ", "_")
    if text in {"GUIDANCE", "GUIDANCE_ONLY"}:
        return "GUIDANCE_ONLY"
    return text.replace("_", " ")


def conformance_impact(change: dict[str, Any]) -> dict[str, Any]:
    new_conformance = normalize_conformance(change.get("new_conformance"))
    strength = CONFORMANCE_STRENGTHS.get(new_conformance, "unknown")
    optional_or_recommended = new_conformance in OPTIONAL_OR_RECOMMENDED_CONFORMANCE
    required_for_conformance = strength in {"required", "required_prohibition"}

    if new_conformance == "MAY":
        filter_category = "optional_conformance"
    elif new_conformance == "SHOULD":
        filter_category = "recommended_conformance"
    elif required_for_conformance:
        filter_category = "required_conformance"
    elif strength == "guidance_only":
        filter_category = "guidance_only"
    else:
        filter_category = "unknown_conformance"

    if optional_or_recommended:
        likely_test_kit_coverage = "low"
    elif required_for_conformance:
        likely_test_kit_coverage = "high"
    elif strength == "guidance_only":
        likely_test_kit_coverage = "low"
    else:
        likely_test_kit_coverage = "unknown"

    return {
        "strength": strength,
        "required_for_conformance": required_for_conformance,
        "optional_or_recommended": optional_or_recommended,
        "likely_test_kit_coverage": likely_test_kit_coverage,
        "filter_category": filter_category,
    }


def requirement_full_ids(raw_ids: Iterable[Any], req_set: str | None) -> list[str]:
    full_ids: list[str] = []
    for raw_id in raw_ids or []:
        text = str(raw_id).strip()
        if not text:
            continue
        if "@" in text:
            full_ids.append(text)
        elif req_set:
            full_ids.append(f"{req_set}@{text}")
        else:
            full_ids.append(text)
    return unique(full_ids)


def has_unqualified_requirement_ids(ledger: dict[str, Any]) -> bool:
    """Return True when a ledger has numeric/table IDs without a req_set prefix."""
    for change in ledger.get("changes", []) or []:
        for raw_id in change.get("old_requirement_ids") or []:
            text = str(raw_id).strip()
            if text and "@" not in text:
                return True
    return False


def concise_requirement(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "requirement_id": record.get("requirement_id"),
        "url": record.get("url"),
        "conformance": record.get("conformance"),
        "actors": list(record.get("actors") or []),
        "requirement": record.get("requirement"),
        "source_file": record.get("source_file"),
    }


def concise_coverage(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "requirement_id": record.get("requirement_id"),
        "suite_id": record.get("suite_id"),
        "short_ids": list(record.get("short_ids") or []),
        "full_ids": list(record.get("full_ids") or []),
        "not_tested_reason": record.get("not_tested_reason"),
        "source_file": record.get("source_file"),
    }


def concise_runnable(record: dict[str, Any], score: int, reasons: list[str]) -> dict[str, Any]:
    return {
        "id": record.get("id"),
        "title": record.get("title"),
        "runnable_type": record.get("runnable_type"),
        "suite_hint": record.get("suite_hint"),
        "source_file": record.get("source_file"),
        "line": record.get("line"),
        "score": score,
        "match_reasons": unique(reasons),
        "requirement_ids": list(record.get("requirement_ids") or []),
        "resource_types": list(record.get("resource_types") or []),
        "search_parameters": list(record.get("search_parameters") or []),
        "matched_must_support_elements": list(record.get("_matched_must_support_elements") or []),
    }


@dataclass
class InventoryIndex:
    inventory_dir: Path
    requirements: list[dict[str, Any]]
    coverage: list[dict[str, Any]]
    runnables: list[dict[str, Any]]

    @classmethod
    def load(cls, inventory_dir: Path) -> "InventoryIndex":
        inventory_dir = inventory_dir.resolve()
        return cls(
            inventory_dir=inventory_dir,
            requirements=load_jsonl(inventory_dir / "requirements.jsonl"),
            coverage=load_jsonl(inventory_dir / "coverage.jsonl"),
            runnables=load_jsonl(inventory_dir / "runnables.jsonl"),
        )

    @property
    def counts(self) -> dict[str, int]:
        return {
            "requirements": len(self.requirements),
            "coverage": len(self.coverage),
            "runnables": len(self.runnables),
        }

    def requirements_for(self, full_ids: list[str]) -> list[dict[str, Any]]:
        wanted = set(full_ids)
        return [record for record in self.requirements if record.get("requirement_id") in wanted]

    def coverage_for(self, full_ids: list[str]) -> list[dict[str, Any]]:
        wanted = set(full_ids)
        return [record for record in self.coverage if record.get("requirement_id") in wanted]

    @property
    def req_sets(self) -> list[str]:
        return sorted_unique_text(
            record.get("req_set")
            for record in [*self.requirements, *self.coverage]
        )


def change_search_terms(change: dict[str, Any], full_requirement_ids: list[str]) -> list[str]:
    terms: list[str] = []
    affected_resource = change.get("affected_resource")
    artifact_id = change.get("artifact_id")
    source_artifact = change.get("source_artifact")
    section = change.get("source_section")

    for element_path in change.get("element_paths") or []:
        path = normalize_path(str(element_path))
        if affected_resource and "." not in path:
            terms.append(f"{affected_resource}.{path}")
        terms.append(path)

    for value in (artifact_id, source_artifact, affected_resource, section):
        if value and str(value).lower() not in {"unknown", "none"}:
            terms.append(str(value))

    terms.extend(full_requirement_ids)
    summary = change.get("summary")
    if affected_resource and normalize_text(affected_resource) not in GENERIC_QUERY_TERMS and summary:
        terms.append(f"{affected_resource} {summary}")

    return unique(terms)


def search_parameters_from_change(change: dict[str, Any]) -> list[str]:
    text = " ".join(
        str(value or "")
        for value in [
            change.get("source_artifact"),
            change.get("artifact_id"),
            change.get("source_section"),
            change.get("summary"),
            change.get("old_text"),
            change.get("new_text"),
            " ".join(change.get("element_paths") or []),
        ]
    )
    params: list[str] = []
    for match in re.finditer(r"SearchParameter-[A-Za-z]+-([A-Za-z0-9-]+)", text):
        params.append(match.group(1))
    for match in re.finditer(r"`([A-Za-z_][A-Za-z0-9_.:-]*(?:-[A-Za-z0-9_.:-]+)*)`", text):
        value = match.group(1)
        if "-" in value or value.startswith("_"):
            params.append(value)
    return unique(params)


def interactions_from_change(change: dict[str, Any]) -> list[str]:
    text = " ".join(
        str(value or "")
        for value in [
            change.get("source_section"),
            change.get("summary"),
            change.get("old_text"),
            change.get("new_text"),
            " ".join(change.get("element_paths") or []),
        ]
    )
    interactions: list[str] = []
    for match in re.finditer(r"`([A-Za-z][A-Za-z0-9-]*)`", text):
        value = match.group(1)
        if value in FHIR_INTERACTIONS:
            interactions.append(value)
    return unique(interactions)


def path_variants(change: dict[str, Any]) -> list[str]:
    affected_resource = change.get("affected_resource")
    variants: list[str] = []
    for raw_path in change.get("element_paths") or []:
        path = normalize_path(str(raw_path))
        variants.append(path)
        if affected_resource and "." not in path:
            variants.append(f"{affected_resource}.{path}")
        if affected_resource and path.startswith(f"{affected_resource}."):
            variants.append(path.split(".", 1)[1])
    return unique(variants)


def score_runnable(
    runnable: dict[str, Any],
    change: dict[str, Any],
    full_requirement_ids: list[str],
    coverage_full_ids: list[str],
) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    matched_elements: list[str] = []

    runnable_id = runnable.get("id") or ""
    runnable_req_ids = set(runnable.get("requirement_ids") or [])
    overlapping_req_ids = sorted(runnable_req_ids.intersection(full_requirement_ids))
    if overlapping_req_ids:
        score += 70
        reasons.append(f"direct requirement id match: {', '.join(overlapping_req_ids)}")

    for full_id in coverage_full_ids:
        segments = [segment for segment in full_id.split("-") if segment]
        if runnable_id and (runnable_id == segments[-1] or runnable_id in segments or full_id.endswith(runnable_id)):
            score += 60
            reasons.append(f"covered test id from requirements coverage: {full_id}")
            break

    affected_resource = change.get("affected_resource")
    if affected_resource and affected_resource in (runnable.get("resource_types") or []):
        score += 12
        reasons.append(f"resource match: {affected_resource}")

    variants = path_variants(change)
    must_support = runnable.get("must_support_elements") or []
    for variant in variants:
        normalized_variant = normalize_path(variant)
        for element in must_support:
            normalized_element = normalize_path(element)
            if normalized_variant == normalized_element or normalized_element.endswith(f".{normalized_variant}"):
                matched_elements.append(element)
    if matched_elements:
        score += min(40, 18 + 5 * len(set(matched_elements)))
        reasons.append("must support element match")

    search_params = set(search_parameters_from_change(change))
    runnable_params = set(runnable.get("search_parameters") or [])
    matched_params = sorted(search_params.intersection(runnable_params))
    if matched_params:
        score += 25
        reasons.append(f"search parameter match: {', '.join(matched_params)}")

    artifact_id = normalize_text(change.get("artifact_id") or artifact_slug(change.get("source_artifact")))
    if artifact_id and artifact_id not in GENERIC_ARTIFACT_IDS:
        profile_blob = normalize_text(" ".join(runnable.get("profile_urls") or []))
        source_blob = normalize_text(runnable.get("source_file"))
        if artifact_id in profile_blob or artifact_id in source_blob:
            score += 15
            reasons.append("profile/artifact id match")

    title_description = normalize_text(
        " ".join([str(runnable.get("title") or ""), str(runnable.get("description") or "")])
    )
    source_file = str(runnable.get("source_file") or "").lower()
    runnable_resource_types = set(runnable.get("resource_types") or [])
    single_resource_match = bool(affected_resource and runnable_resource_types == {affected_resource})
    interactions = set(interactions_from_change(change))
    if single_resource_match and "read" in interactions and (
        "read_test" in source_file or "read interaction" in title_description
    ):
        score += 15
        reasons.append("interaction match: read")

    for token in search_params:
        if normalize_text(token) and normalize_text(token) in title_description:
            score += 8
            reasons.append(f"text mention: {token}")
            break

    runnable["_matched_must_support_elements"] = unique(matched_elements)
    return score, unique(reasons)


def is_broad_resource_only_match(
    runnable: dict[str, Any],
    change: dict[str, Any],
    reasons: list[str],
) -> bool:
    affected_resource = change.get("affected_resource")
    if not affected_resource:
        return False

    resource_types = set(runnable.get("resource_types") or [])
    if len(resource_types) <= 1:
        return False

    resource_reason = f"resource match: {affected_resource}"
    reason_set = set(reasons)
    broad_profile_reasons = {reason for reason in reason_set if reason.startswith("broad profile URL match:")}
    if broad_profile_reasons:
        return reason_set - broad_profile_reasons <= {resource_reason}

    return reason_set == {resource_reason}


def candidate_tests(
    index: InventoryIndex,
    change: dict[str, Any],
    full_requirement_ids: list[str],
    coverage_rows: list[dict[str, Any]],
    limit: int,
    profile_filters: list[str] | None = None,
) -> list[dict[str, Any]]:
    coverage_full_ids = unique(
        full_id
        for row in coverage_rows
        for full_id in (row.get("full_ids") or [])
    )
    candidates: list[dict[str, Any]] = []
    active_profile_filters = profile_filters or []
    for runnable in index.runnables:
        profile_reasons = profile_filter_match_reasons(runnable, active_profile_filters)
        if active_profile_filters and not profile_reasons:
            continue
        score, reasons = score_runnable(runnable, change, full_requirement_ids, coverage_full_ids)
        if profile_reasons:
            score += profile_match_score(profile_reasons)
            reasons = unique([*reasons, *profile_reasons])
        if is_broad_resource_only_match(runnable, change, reasons):
            continue
        if score > 0:
            candidates.append(concise_runnable(runnable, score, reasons))

    candidates.sort(key=lambda item: (-int(item["score"]), item.get("source_file") or "", item.get("id") or ""))
    return candidates[:limit]


def match_status(change: dict[str, Any], candidates: list[dict[str, Any]], coverage_rows: list[dict[str, Any]]) -> tuple[str, str]:
    if not candidates:
        action = change.get("test_action")
        if action in {"author_new_test", "add_required_assertion", "add_to_must_support"}:
            return "no_candidate_found", "low"
        return "manual_review", "low"

    top_score = int(candidates[0]["score"])
    if top_score >= 70:
        if coverage_rows:
            return "covered_by_existing_test", "high"
        return "strong_candidate_found", "high"
    if top_score >= 35:
        return "candidate_found_review_needed", "medium"
    return "weak_candidate_found", "low"


def repobase_queries(change: dict[str, Any], full_requirement_ids: list[str]) -> list[str]:
    affected_resource = change.get("affected_resource")
    useful_resource = bool(affected_resource and normalize_text(affected_resource) not in GENERIC_QUERY_TERMS)
    queries: list[str] = []
    for requirement_id in full_requirement_ids:
        queries.append(requirement_id)

    for term in change_search_terms(change, []):
        if normalize_text(term) in GENERIC_QUERY_TERMS:
            continue
        if useful_resource and term != affected_resource:
            queries.append(f"{affected_resource} {term}")
        else:
            queries.append(term)

    for param in search_parameters_from_change(change):
        if useful_resource:
            queries.append(f"{affected_resource} search parameter {param}")
        else:
            queries.append(f"search parameter {param}")

    summary = change.get("summary")
    if summary:
        queries.append(str(summary))

    return unique(queries)[:8]


def enrich_change(
    index: InventoryIndex,
    change: dict[str, Any],
    req_set: str | None,
    candidate_limit: int,
    profile_filters: list[str] | None = None,
    auto_profile_filter: bool = True,
) -> dict[str, Any]:
    old_requirement_ids = change.get("old_requirement_ids") or []
    full_ids = requirement_full_ids(old_requirement_ids, req_set)
    requirement_rows = index.requirements_for(full_ids)
    coverage_rows = index.coverage_for(full_ids)
    explicit_profile_filters = profile_filters or []
    inferred_profile_filters = infer_change_profile_filters(change) if auto_profile_filter else []
    effective_profile_filters = explicit_profile_filters or inferred_profile_filters
    candidates = candidate_tests(index, change, full_ids, coverage_rows, candidate_limit, effective_profile_filters)
    status, confidence = match_status(change, candidates, coverage_rows)

    enriched = dict(change)
    enriched["old_requirement_full_ids"] = full_ids
    enriched["requirement_context"] = [concise_requirement(record) for record in requirement_rows]
    enriched["conformance_impact"] = conformance_impact(change)
    enriched["inventory_match"] = {
        "status": status,
        "confidence": confidence,
        "candidate_tests": candidates,
        "candidate_coverage": [concise_coverage(record) for record in coverage_rows],
        "repobase_queries": repobase_queries(change, full_ids),
    }
    if inferred_profile_filters:
        enriched["inventory_match"]["inferred_profile_filters"] = inferred_profile_filters
    if effective_profile_filters:
        enriched["inventory_match"]["profile_filters"] = effective_profile_filters
        enriched["inventory_match"]["profile_filter_source"] = "explicit" if explicit_profile_filters else "inferred_from_change"
    return enriched


def enrich_ledger(
    ledger: dict[str, Any],
    index: InventoryIndex,
    req_set: str | None = DEFAULT_REQ_SET,
    candidate_limit: int = 8,
    baseline_ig_version: str | None = None,
    target_ig_version: str | None = None,
    baseline_suite_ids: list[str] | None = None,
    inventory_label: str | None = None,
    profile_filters: list[str] | None = None,
    auto_profile_filter: bool = True,
) -> dict[str, Any]:
    enriched = dict(ledger)
    meta = dict(enriched.get("meta") or {})
    meta.update(
        {
            "ledger_stage": "inventory_enriched_change_ledger",
            "inventory_enriched": True,
            "inventory_dir": str(index.inventory_dir),
            "inventory_counts": index.counts,
            "inventory_req_sets": index.req_sets,
            "numeric_requirement_id_req_set": req_set,
            "numeric_requirement_ids_qualified": bool(req_set),
            "profile_filters": profile_filters or [],
            "auto_profile_filter": auto_profile_filter,
            "inventory_enriched_at": datetime.now(UTC).strftime("%Y%m%d_%H%M%S"),
        }
    )
    if inventory_label or baseline_ig_version or baseline_suite_ids:
        meta["baseline_test_inventory"] = {
            "label": inventory_label,
            "ig_version": baseline_ig_version,
            "suite_ids": baseline_suite_ids or [],
        }
    if target_ig_version:
        meta["target_ig_version"] = target_ig_version
    enriched["meta"] = meta
    enriched["changes"] = [
        enrich_change(index, change, req_set, candidate_limit, profile_filters, auto_profile_filter)
        for change in ledger.get("changes", [])
    ]
    return enriched


def write_jsonl(path: Path, changes: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for change in changes:
            handle.write(json.dumps(change, ensure_ascii=False, sort_keys=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Enrich a YAML IG change ledger with Inferno inventory matches."
    )
    parser.add_argument("ledger", type=Path, help="Path to changes.yaml or change_ledger_*.yaml")
    parser.add_argument("--inventory-dir", required=True, type=Path, help="Directory containing inventory JSONL files")
    parser.add_argument("--output", "-o", type=Path, default=None, help="Output YAML path")
    parser.add_argument("--jsonl-output", type=Path, default=None, help="Optional JSONL output path for changes only")
    parser.add_argument(
        "--req-set",
        default=DEFAULT_REQ_SET,
        help=(
            "Optional requirement set prefix for numeric old_requirement_ids, "
            "for example hl7.fhir.us.carin-bb_1.1.0. If omitted, numeric IDs "
            "remain unqualified."
        ),
    )
    parser.add_argument("--candidate-limit", type=int, default=8, help="Maximum candidate tests per change")
    parser.add_argument("--baseline-ig-version", default=None, help="IG version represented by the baseline test inventory")
    parser.add_argument("--target-ig-version", default=None, help="IG version represented by the changed/new IG narrative")
    parser.add_argument(
        "--baseline-suite-id",
        action="append",
        default=None,
        help="Baseline test suite ID(s), e.g. --baseline-suite-id c4bb_v110. Can be repeated or comma-separated.",
    )
    parser.add_argument(
        "--profile-filter",
        action="append",
        default=None,
        help=(
            "Limit candidate tests to one or more profile ids/canonical URLs, "
            "e.g. --profile-filter C4BB-ExplanationOfBenefit-Inpatient-Institutional. "
            "Can be repeated or comma-separated."
        ),
    )
    parser.add_argument(
        "--no-auto-profile-filter",
        dest="auto_profile_filter",
        action="store_false",
        default=True,
        help="Disable per-change profile filters inferred from Supported Profiles and StructureDefinition references.",
    )
    parser.add_argument("--inventory-label", default=None, help="Human-readable label for the inventory used")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ledger = yaml.safe_load(args.ledger.read_text(encoding="utf-8"))
    if not isinstance(ledger, dict):
        raise SystemExit(f"Ledger is not a YAML mapping: {args.ledger}")

    index = InventoryIndex.load(args.inventory_dir)
    if args.req_set is None and has_unqualified_requirement_ids(ledger):
        print(
            "WARNING: Ledger contains unqualified numeric old_requirement_ids, "
            "but --req-set was not provided. Requirement/coverage ID matches "
            "will only work for IDs already written with a req_set prefix."
        )
    enriched = enrich_ledger(
        ledger,
        index,
        req_set=args.req_set,
        candidate_limit=args.candidate_limit,
        baseline_ig_version=args.baseline_ig_version,
        target_ig_version=args.target_ig_version,
        baseline_suite_ids=split_cli_values(args.baseline_suite_id),
        inventory_label=args.inventory_label,
        profile_filters=split_cli_values(args.profile_filter),
        auto_profile_filter=args.auto_profile_filter,
    )

    output_path = args.output or args.ledger.with_name(f"{args.ledger.stem}_inventory_enriched.yaml")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        yaml.dump(
            enriched,
            handle,
            Dumper=NoAliasDumper,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
            width=120,
        )

    if args.jsonl_output:
        args.jsonl_output.parent.mkdir(parents=True, exist_ok=True)
        write_jsonl(args.jsonl_output, enriched.get("changes", []))

    print(f"Wrote enriched change ledger: {output_path}")
    print(f"Inventory counts: {index.counts}")
    print(f"Changes enriched: {len(enriched.get('changes', []))}")


if __name__ == "__main__":
    main()
