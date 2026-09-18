"""Validation rules for uploaded Agent Usage Metrics reports."""

from __future__ import annotations

from dataclasses import dataclass
from numbers import Real
from typing import Any

from .loader import AgentReport, decode_report
from .schema import (
    ALLOWED_SCOPE_TYPES,
    ALLOWED_STATUSES,
    INTEGER_METRIC_NAMES,
    REQUIRED_METRIC_NAMES,
    REQUIRED_RUN_METADATA_FIELDS,
)


@dataclass(frozen=True)
class ValidatedUpload:
    filename: str
    payload: dict[str, Any] | None
    report: AgentReport | None
    error: str | None = None

    @property
    def valid(self) -> bool:
        return self.error is None and self.report is not None


@dataclass(frozen=True)
class UploadDecision:
    """UI-ready result for a mode-specific upload selection."""

    valid_items: tuple[ValidatedUpload, ...]
    errors: tuple[str, ...]
    mode: str | None
    cta_label: str

    @property
    def ready(self) -> bool:
        return self.mode in {"single", "multiple", "workspace", "comparison"}


def _is_number(value: Any) -> bool:
    return isinstance(value, Real) and not isinstance(value, bool)


def _contract_errors(payload: dict[str, Any], report: AgentReport) -> list[str]:
    errors = _metadata_errors(report.run_metadata)

    metric_items = payload.get("metrics", [])
    names = [str(item.get("name", "")).strip() for item in metric_items if isinstance(item, dict)]
    if len(names) != len(set(names)):
        errors.append("metric names must be unique")

    required = set(REQUIRED_METRIC_NAMES)
    present = set(names)
    missing = sorted(required - present)
    unsupported = sorted(present - required)
    if missing:
        errors.append(f"missing required metrics: {', '.join(missing)}")
    if unsupported:
        errors.append(f"unsupported metrics: {', '.join(unsupported)}")

    for name in sorted(required & present):
        metric = report.metrics[name]
        if metric.status not in ALLOWED_STATUSES:
            errors.append(f"{name} has unsupported status '{metric.status}'")
        value = metric.value
        if value is None:
            if metric.status != "missing":
                errors.append(f"{name} must use status 'missing' when value is null")
            continue
        if not _is_number(value) or float(value) < 0:
            errors.append(f"{name} must be a non-negative number or null")
        elif name in INTEGER_METRIC_NAMES and not float(value).is_integer():
            errors.append(f"{name} must be an integer count")
        if metric.status == "missing":
            errors.append(f"{name} cannot have a value when status is 'missing'")
        if name == "estimated_cost" and metric.unit != "USD":
            errors.append("estimated_cost must use unit 'USD'")
    return errors


def _metadata_errors(metadata: Any) -> list[str]:
    errors: list[str] = []
    missing = [field for field in REQUIRED_RUN_METADATA_FIELDS if field not in metadata]
    if missing:
        errors.append(f"missing required run_metadata fields: {', '.join(missing)}")

    session_files = metadata.get("session_files")
    if "session_files" in metadata:
        if not isinstance(session_files, list):
            errors.append("run_metadata.session_files must be a JSON array")
        elif not session_files:
            errors.append("run_metadata.session_files must contain at least one filename")
        elif any(not isinstance(item, str) for item in session_files):
            errors.append("run_metadata.session_files entries must be strings")

    for field in ("conversation_name", "workspace_name"):
        value = metadata.get(field)
        if field in metadata and value is not None and not isinstance(value, str):
            errors.append(f"run_metadata.{field} must be a string or null")

    scope_type = metadata.get("scope_type")
    if "scope_type" in metadata and scope_type not in ALLOWED_SCOPE_TYPES:
        allowed = ", ".join(sorted(ALLOWED_SCOPE_TYPES))
        errors.append(f"run_metadata.scope_type must be one of: {allowed}")

    model = metadata.get("model")
    if "model" in metadata and model is not None and not isinstance(model, str):
        errors.append("run_metadata.model must be a string or null")

    generated_at = metadata.get("generated_at")
    if "generated_at" in metadata and (
        not isinstance(generated_at, str) or not generated_at.strip()
    ):
        errors.append("run_metadata.generated_at must be a non-empty string")
    return errors


def validate_content(filename: str, content: bytes | str) -> ValidatedUpload:
    if not filename.lower().endswith(".json"):
        return ValidatedUpload(filename, None, None, "Only .json files are supported")
    try:
        payload, report = decode_report(content)
    except ValueError as exc:
        return ValidatedUpload(filename, None, None, str(exc))
    errors = _contract_errors(payload, report)
    if errors:
        return ValidatedUpload(filename, payload, report, "; ".join(errors))
    return ValidatedUpload(filename, payload, report)


def validate_upload(uploaded_file: Any) -> ValidatedUpload:
    filename = str(getattr(uploaded_file, "name", "report.json"))
    try:
        content = uploaded_file.getvalue()
    except AttributeError as exc:
        return ValidatedUpload(filename, None, None, str(exc))
    return validate_content(filename, content)


def validate_pair(items: list[ValidatedUpload]) -> list[str]:
    errors: list[str] = []
    if len(items) != 2:
        errors.append("Upload exactly two JSON reports.")
        return errors
    for item in items:
        if not item.valid:
            errors.append(f"{item.filename}: {item.error}")
    if errors:
        return errors
    agent_keys = {item.report.agent_key for item in items if item.report}
    if agent_keys != {"codex", "claude_code"}:
        errors.append(
            "Comparison requires one Codex report and one Claude Code report. "
            "Two reports from the same agent cannot be compared."
        )
    return errors


def evaluate_uploads(
    items: list[ValidatedUpload], requested_mode: str
) -> UploadDecision:
    """Evaluate uploaded files against the user's explicit workflow choice."""
    if requested_mode not in {
        "visualize",
        "single_conversation",
        "multiple_conversations",
        "workspace",
        "compare",
    }:
        raise ValueError("unsupported upload mode")

    valid_items = tuple(item for item in items if item.valid)
    errors = [f"{item.filename}: {item.error}" for item in items if not item.valid]

    if requested_mode in {"visualize", "single_conversation"}:
        scope_errors = [
            f"{item.filename}: Single Conversation requires a conversation-level report."
            for item in valid_items
            if item.report and item.report.run_metadata.get("scope_type") != "conversation"
        ]
        errors.extend(scope_errors)
        ready = len(items) == 1 and len(valid_items) == 1 and not scope_errors
        cta_label = "Visualize Report" if requested_mode == "visualize" else "View Results"
        return UploadDecision(
            valid_items,
            tuple(errors),
            "single" if ready else None,
            cta_label,
        )

    if requested_mode == "workspace":
        scope_errors = [
            f"{item.filename}: Workspace requires a workspace-level report."
            for item in valid_items
            if item.report and item.report.run_metadata.get("scope_type") != "workspace"
        ]
        errors.extend(scope_errors)
        ready = len(items) == 1 and len(valid_items) == 1 and not scope_errors
        return UploadDecision(
            valid_items,
            tuple(errors),
            "workspace" if ready else None,
            "View Workspace",
        )

    if requested_mode == "multiple_conversations":
        scope_errors = [
            f"{item.filename}: Multiple Conversations accepts conversation-level reports only."
            for item in valid_items
            if item.report and item.report.run_metadata.get("scope_type") != "conversation"
        ]
        errors.extend(scope_errors)
        agents = {item.report.agent_key for item in valid_items if item.report}
        if len(agents) > 1:
            errors.append("Multiple Conversations requires reports from the same agent.")
        ready = (
            len(items) >= 2
            and len(valid_items) == len(items)
            and not scope_errors
            and len(agents) == 1
        )
        return UploadDecision(
            valid_items,
            tuple(errors),
            "multiple" if ready else None,
            "View Conversations",
        )

    if len(items) == 2 and len(valid_items) == 2:
        agent_keys = {item.report.agent_key for item in valid_items if item.report}
        if agent_keys == {"codex", "claude_code"}:
            return UploadDecision(valid_items, tuple(errors), "comparison", "Compare Reports")
        errors.append(
            "Comparison requires one Codex report and one Claude Code report. "
            "Remove one of the same-agent reports to continue."
        )
        return UploadDecision(valid_items, tuple(errors), None, "Compare Reports")

    return UploadDecision(valid_items, tuple(errors), None, "Compare Reports")
