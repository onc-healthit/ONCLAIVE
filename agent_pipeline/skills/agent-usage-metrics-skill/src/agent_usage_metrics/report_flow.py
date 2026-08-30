"""Coordinate collection, metric calculation, enrichment, and Markdown export."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .ccusage_adapter import load_ccusage_data
from .claude_code_source_adapter import load_raw_claude_code_data, normalize_claude_code_events
from .codex_source_adapter import load_raw_codex_data
from .event_normalizer import normalize_codex_events
from .metrics_builder import build_basic_metrics
from .models import CcusageResult, MetricResult, NormalizedEventData, ReportFlowResult, ResolvedInput, SessionBreakdownRow
from .report_builder import (
    DEFAULT_MARKDOWN_REPORT_FILENAME,
    DEFAULT_SESSION_BREAKDOWN_FILENAME,
    build_agent_usage_report,
    export_report_markdown,
    export_session_breakdown_markdown,
)


CCUSAGE_PERMISSION_QUESTION = (
    "ccusage is needed to calculate input tokens, output tokens, and estimated cost. "
    "It is not currently available locally, but it can be downloaded or cached using bunx/npx/pnpm. "
    "Do you approve? yes/no"
)
CCUSAGE_PERMISSION_DECLINED_WARNING = (
    "ccusage permission was declined; token/cost metrics are missing."
)
_AGGREGATED_BASIC_METRICS = {
    "wall_clock_time_seconds",
    "api_request_count",
    "human_prompts_required",
    "tool_calls",
    "file_edits",
    "session_count",
    "assistant_messages",
    "shell_commands",
    "file_reads",
    "file_write_edit_candidates",
    "tool_results",
    "tool_failures",
}
_AGGREGATED_METRIC_ORDER = (
    "wall_clock_time_seconds",
    "api_request_count",
    "human_prompts_required",
    "tool_calls",
    "file_edits",
    "session_count",
    "assistant_messages",
    "shell_commands",
    "file_reads",
    "file_write_edit_candidates",
    "tool_results",
    "tool_failures",
)


@dataclass(frozen=True)
class _SessionMetricBundle:
    rollout_file: Path
    metrics: list[MetricResult]
    normalized_data: NormalizedEventData
    conversation_title: str | None = None


def run_report_flow(
    resolved_input: ResolvedInput,
    *,
    skip_ccusage: bool = False,
    allow_download: bool = False,
    decline_download: bool = False,
    json_filename: str | None = None,
    md_filename: str | None = None,
) -> ReportFlowResult:
    """Generate a report, pausing only when ccusage download permission is needed."""
    del json_filename

    session_metric_bundles = _compute_session_metric_bundles(resolved_input)
    if _uses_session_aggregation(resolved_input):
        basic_metrics = _aggregate_session_metrics(session_metric_bundles)
    else:
        basic_metrics = session_metric_bundles[0].metrics

    ccusage_result: CcusageResult | None = None
    if not skip_ccusage:
        ccusage_result = load_ccusage_data(resolved_input, allow_download=allow_download)
        if ccusage_result.status == "requires_permission":
            if not decline_download:
                return ReportFlowResult(
                    status="requires_permission",
                    resolved_input=resolved_input,
                    ccusage_result=ccusage_result,
                    report=None,
                    permission_question=CCUSAGE_PERMISSION_QUESTION,
                )
            ccusage_result = _permission_declined_result(ccusage_result)

    breakdown_filename = _session_breakdown_filename(md_filename) if _should_export_session_breakdown(resolved_input) else None
    report = build_agent_usage_report(
        resolved_input,
        basic_metrics,
        ccusage_result,
        session_breakdown_path=breakdown_filename,
    )
    markdown_path = export_report_markdown(report, resolved_input.output_dir, md_filename)
    breakdown_path = None
    if breakdown_filename:
        breakdown_rows = _session_breakdown_rows(session_metric_bundles, ccusage_result)
        breakdown_path = export_session_breakdown_markdown(
            report,
            breakdown_rows,
            resolved_input.output_dir,
            breakdown_filename,
        )
    return ReportFlowResult(
        status="completed",
        resolved_input=resolved_input,
        ccusage_result=ccusage_result,
        report=report,
        markdown_path=markdown_path,
        breakdown_path=breakdown_path,
        json_path=None,
    )


def _compute_session_metric_bundles(resolved_input: ResolvedInput) -> list[_SessionMetricBundle]:
    """Analyze each session independently before aggregating a broader scope."""
    bundles: list[_SessionMetricBundle] = []
    for rollout_file in resolved_input.rollout_files:
        session_input = _single_session_resolved_input(resolved_input, rollout_file)
        if session_input.agent == "claude_code":
            raw_data = load_raw_claude_code_data(session_input)
            normalized_data = normalize_claude_code_events(raw_data)
        else:
            raw_data = load_raw_codex_data(session_input)
            normalized_data = normalize_codex_events(raw_data)
        bundles.append(
            _SessionMetricBundle(
                rollout_file=rollout_file,
                metrics=build_basic_metrics(normalized_data),
                normalized_data=normalized_data,
                conversation_title=session_input.thread_title,
            )
        )
    return bundles


def _single_session_resolved_input(resolved_input: ResolvedInput, rollout_file: Path) -> ResolvedInput:
    conversation_title = resolved_input.session_titles.get(
        rollout_file.name,
        resolved_input.thread_title,
    )
    return ResolvedInput(
        agent=resolved_input.agent,
        scope_type="session",
        rollout_files=[rollout_file],
        codex_home=resolved_input.codex_home,
        logs_db=resolved_input.logs_db,
        state_db=resolved_input.state_db,
        workspace=resolved_input.workspace,
        thread_title=conversation_title,
        date_range=resolved_input.date_range,
        output_dir=resolved_input.output_dir,
        warnings=list(resolved_input.warnings),
        resolution_status=resolved_input.resolution_status,
        claude_home=resolved_input.claude_home,
        source_metadata=dict(resolved_input.source_metadata),
        session_titles={rollout_file.name: conversation_title},
    )


def _uses_session_aggregation(resolved_input: ResolvedInput) -> bool:
    return resolved_input.scope_type in {"conversation", "workspace"}


def _aggregate_session_metrics(session_metric_bundles: list[_SessionMetricBundle]) -> list[MetricResult]:
    """Sum session metrics so gaps between sessions are not treated as active duration."""
    metrics_by_name: dict[str, list[MetricResult]] = {}
    for bundle in session_metric_bundles:
        for metric in bundle.metrics:
            if metric.name in _AGGREGATED_BASIC_METRICS:
                metrics_by_name.setdefault(metric.name, []).append(metric)

    aggregated: list[MetricResult] = []
    for metric_name in _AGGREGATED_METRIC_ORDER:
        metrics = metrics_by_name.get(metric_name, [])
        if not metrics:
            continue
        aggregated.append(_sum_metric(metric_name, metrics, len(session_metric_bundles)))
    return aggregated


def _sum_metric(metric_name: str, metrics: list[MetricResult], session_count: int) -> MetricResult:
    warnings = _dedupe([warning for metric in metrics for warning in metric.warnings])
    notes = _dedupe([note for metric in metrics for note in metric.notes])
    notes.append(f"Aggregated by summing independently computed metrics from {session_count} session(s).")
    if metric_name == "wall_clock_time_seconds":
        notes.append("For broader scopes, wall-clock time is the sum of session wall-clock durations, not the elapsed span.")

    numeric_values = [metric.value for metric in metrics if isinstance(metric.value, int | float)]
    if not numeric_values:
        return MetricResult(
            name=metric_name,
            value=None,
            status="missing",
            source="normalized_events",
            warnings=warnings,
            notes=_dedupe(notes),
        )

    total = sum(float(value) for value in numeric_values)
    if metric_name == "wall_clock_time_seconds":
        value: Any = round(total, 3)
    elif all(isinstance(value, int) for value in numeric_values):
        value = int(total)
    else:
        value = total

    statuses = {metric.status for metric in metrics}
    status = "computed"
    if len(numeric_values) < session_count or "missing" in statuses or "partial" in statuses:
        status = "partial"

    return MetricResult(
        name=metric_name,
        value=value,
        status=status,
        source="normalized_events",
        warnings=warnings,
        notes=_dedupe(notes),
    )


def _should_export_session_breakdown(resolved_input: ResolvedInput) -> bool:
    """Create a breakdown only for multi-session conversation or workspace reports."""
    return resolved_input.scope_type in {"conversation", "workspace"} and len(resolved_input.rollout_files) > 1


def _session_breakdown_filename(md_filename: str | None) -> str:
    main_name = Path(md_filename or DEFAULT_MARKDOWN_REPORT_FILENAME).name
    if main_name == DEFAULT_MARKDOWN_REPORT_FILENAME:
        return DEFAULT_SESSION_BREAKDOWN_FILENAME
    return f"{Path(main_name).stem}_session_breakdown.md"


def _session_breakdown_rows(
    session_metric_bundles: list[_SessionMetricBundle],
    ccusage_result: CcusageResult | None,
) -> list[SessionBreakdownRow]:
    ccusage_status = ccusage_result.status if ccusage_result else "not_requested"
    ccusage_precision = ccusage_result.precision if ccusage_result else "unavailable"
    ccusage_reason = ccusage_result.reason if ccusage_result else "ccusage_not_requested"
    ccusage_session_details = _ccusage_session_details_by_rollout(ccusage_result)
    rows: list[SessionBreakdownRow] = []
    for bundle in session_metric_bundles:
        metrics = {metric.name: metric for metric in bundle.metrics}
        start_time, end_time = _event_time_bounds(bundle.normalized_data)
        ccusage_detail = ccusage_session_details.get(bundle.rollout_file.name, {})
        rows.append(
            SessionBreakdownRow(
                rollout_file=bundle.rollout_file.name,
                start_time=start_time,
                end_time=end_time,
                wall_clock_time_seconds=_metric_value(metrics, "wall_clock_time_seconds"),
                api_request_count=_metric_value(metrics, "api_request_count"),
                human_prompts_required=_metric_value(metrics, "human_prompts_required"),
                tool_calls=_metric_value(metrics, "tool_calls"),
                file_edits=_metric_value(metrics, "file_edits"),
                ccusage_status=ccusage_detail.get("status", ccusage_status),
                ccusage_precision=ccusage_detail.get("precision", ccusage_precision),
                ccusage_reason=ccusage_detail.get("reason", ccusage_reason),
                input_tokens=ccusage_detail.get("input_tokens"),
                output_tokens=ccusage_detail.get("output_tokens"),
                estimated_cost=ccusage_detail.get("estimated_cost"),
                conversation_title=bundle.conversation_title,
            )
        )
    return rows


def _ccusage_session_details_by_rollout(ccusage_result: CcusageResult | None) -> dict[str, dict[str, Any]]:
    if ccusage_result is None or not isinstance(ccusage_result.session_match, dict):
        return {}
    sessions = ccusage_result.session_match.get("sessions")
    if not isinstance(sessions, list):
        return {}
    details: dict[str, dict[str, Any]] = {}
    for session in sessions:
        if not isinstance(session, dict):
            continue
        rollout_file = session.get("rollout_file")
        if not rollout_file:
            continue
        details[Path(str(rollout_file)).name] = session
    return details


def _metric_value(metrics: dict[str, MetricResult], metric_name: str) -> Any:
    metric = metrics.get(metric_name)
    return metric.value if metric else None


def _event_time_bounds(normalized_data: NormalizedEventData) -> tuple[str | None, str | None]:
    parsed_times = [
        (parsed, event.timestamp)
        for event in normalized_data.events
        if event.timestamp and (parsed := _parse_timestamp(event.timestamp)) is not None
    ]
    if not parsed_times:
        return None, None
    start = min(parsed_times, key=lambda item: item[0])[1]
    end = max(parsed_times, key=lambda item: item[0])[1]
    return start, end


def _parse_timestamp(value: str) -> datetime | None:
    normalized = value.strip()
    if not normalized:
        return None
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _permission_declined_result(result: CcusageResult) -> CcusageResult:
    warnings = [CCUSAGE_PERMISSION_DECLINED_WARNING, *result.warnings]
    return CcusageResult(
        status="permission_declined",
        command=result.command,
        scope_requested=result.scope_requested,
        scope_returned=result.scope_returned,
        input_tokens=None,
        cached_input_tokens=None,
        output_tokens=None,
        reasoning_output_tokens=None,
        total_tokens=None,
        estimated_cost=None,
        currency=None,
        model_breakdown=None,
        raw_summary=None,
        warnings=_dedupe(warnings),
        errors=list(result.errors),
        precision="unavailable",
        reason="permission_denied",
        mode_attempted=result.mode_attempted,
        command_attempts=list(result.command_attempts),
        session_match=result.session_match,
    )


def _dedupe(values: list[str]) -> list[str]:
    deduped: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        deduped.append(value)
    return deduped
