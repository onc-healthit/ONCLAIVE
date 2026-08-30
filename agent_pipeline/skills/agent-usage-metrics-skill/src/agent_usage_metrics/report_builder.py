"""Build agent usage report models and render their Markdown outputs."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .models import AgentUsageReport, CcusageResult, MetricResult, ResolvedInput, RunMetadata, SessionBreakdownRow


DEFAULT_MARKDOWN_REPORT_FILENAME = "agent_usage_metrics_report.md"
DEFAULT_SESSION_BREAKDOWN_FILENAME = "agent_usage_metrics_session_breakdown.md"
MISSING_DISPLAY_VALUE = "\u2014"
METADATA_UNAVAILABLE_DISPLAY_VALUE = "Not available in selected Codex metadata"
SESSION_TITLE_UNAVAILABLE_DISPLAY_VALUE = "Unavailable"

_BASIC_METRIC_ORDER = [
    "wall_clock_time_seconds",
    "api_request_count",
    "human_prompts_required",
    "tool_calls",
    "file_edits",
]
_CLAUDE_BASIC_METRIC_ORDER = [
    "session_count",
    "assistant_messages",
    "shell_commands",
    "file_reads",
    "file_write_edit_candidates",
    "tool_results",
    "tool_failures",
]
_CCUSAGE_METRIC_ORDER = [
    "input_tokens",
    "output_tokens",
    "estimated_cost",
]
_CLAUDE_CCUSAGE_METRIC_ORDER = ["cached_input_tokens", "total_tokens", "model_name"]
_BASIC_REPORT_SOURCES = {
    "wall_clock_time_seconds": "codex_logs",
    "api_request_count": "codex_telemetry",
    "human_prompts_required": "codex_logs",
    "tool_calls": "codex_logs",
    "file_edits": "codex_patch_events",
}
_CLAUDE_BASIC_REPORT_SOURCES = {
    name: "claude_code_transcript"
    for name in [*_BASIC_METRIC_ORDER, *_CLAUDE_BASIC_METRIC_ORDER]
}
_CCUSAGE_STATUSES_WITH_DATA = {
    "available",
    "available_via_bunx",
    "available_via_npx",
    "available_via_pnpm",
    "scope_mismatch",
    "success",
    "partial",
}
_CCUSAGE_DATA_PRECISIONS = {
    "exact_session",
    "exact_conversation",
    "partial_conversation",
    "exact_workspace",
    "partial_workspace",
    "date_range",
    "day_level",
    "week_level",
    "month_level",
}
_FILE_EDITS_PARTIAL_NOTE = (
    "File edits is partial because only explicit patch/file edit events are counted. "
    "Shell-based edits or script-generated edits may not be captured, so this value may undercount total edits."
)
_API_REQUEST_COUNT_NOTE = "API request count is a workflow intensity signal, not a quality metric."
def build_agent_usage_report(
    resolved_input: ResolvedInput,
    basic_metrics: list[MetricResult],
    ccusage_result: CcusageResult | None = None,
    *,
    generated_at: str | None = None,
    session_breakdown_path: str | None = None,
) -> AgentUsageReport:
    """Combine workflow metrics and optional ccusage enrichment into a report model."""
    generated = generated_at or _utc_now()
    report_metrics = [
        *_basic_report_metrics(basic_metrics, resolved_input.agent),
        *_ccusage_report_metrics(ccusage_result, resolved_input.agent),
    ]

    warnings = _report_warnings(resolved_input, report_metrics, ccusage_result)
    notes = _report_notes(report_metrics)

    return AgentUsageReport(
        run_metadata=_run_metadata(resolved_input, generated),
        metrics=report_metrics,
        warnings=warnings,
        notes=notes,
        generated_at=generated,
        sources_used=_sources_used(resolved_input, ccusage_result),
        ccusage=_ccusage_metadata(ccusage_result),
        session_breakdown_path=session_breakdown_path,
    )


def export_report_markdown(
    report: AgentUsageReport,
    output_dir: str | Path,
    filename: str | None = None,
) -> Path:
    """Write the main human-readable Markdown report."""
    destination_dir = Path(output_dir).expanduser()
    destination_dir.mkdir(parents=True, exist_ok=True)
    safe_filename = Path(filename or DEFAULT_MARKDOWN_REPORT_FILENAME).name
    output_path = destination_dir / safe_filename
    output_path.write_text(format_report_markdown(report) + "\n", encoding="utf-8")
    return output_path.resolve()


def export_session_breakdown_markdown(
    report: AgentUsageReport,
    rows: list[SessionBreakdownRow],
    output_dir: str | Path,
    filename: str | None = None,
) -> Path:
    """Write the per-session details referenced by a multi-session main report."""
    destination_dir = Path(output_dir).expanduser()
    destination_dir.mkdir(parents=True, exist_ok=True)
    safe_filename = Path(filename or DEFAULT_SESSION_BREAKDOWN_FILENAME).name
    output_path = destination_dir / safe_filename
    output_path.write_text(format_session_breakdown_markdown(report, rows) + "\n", encoding="utf-8")
    return output_path.resolve()


def format_report_table(report: AgentUsageReport) -> str:
    metadata = report.run_metadata
    lines = [
        "Agent Usage Metrics Report",
        "",
        "Run Summary:",
        f"- Agent: {_display(metadata.agent)}",
        f"- Target type: {_display(metadata.scope_type)}",
        f"- Workspace: {_display(metadata.workspace)}",
        f"- Sources used: {_display(', '.join(report.sources_used))}",
        f"- ccusage status: {_display(report.ccusage.get('status'))}",
    ]
    if metadata.scope_type == "workspace":
        lines.insert(5, f"- Conversation titles discovered: {_conversation_titles_discovered(metadata)}")
    else:
        lines.insert(5, f"- Conversation: {_display(metadata.thread_title)}")
    if report.session_breakdown_path:
        lines.append(f"- Per-session breakdown: {report.session_breakdown_path}")
    if metadata.agent == "claude_code":
        lines.extend([
            f"- Session ID: {_display(metadata.source_session_id)}",
            f"- Git branch: {_display(metadata.git_branch)}",
            f"- Start timestamp: {_display(metadata.start_timestamp)}",
            f"- End timestamp: {_display(metadata.end_timestamp)}",
        ])
    if metadata.scope_type == "workspace":
        lines.extend([
            "",
            "Workspace Sessions:",
            "| Conversation/thread title | Rollout/session file |",
            "|---|---|",
            *(
                f"| {_display_session_title(metadata.session_titles.get(rollout_file))} | {rollout_file} |"
                for rollout_file in metadata.rollout_files
            ),
        ])
    lines.extend([
        "",
        "Metrics:",
        "| Metric | Value | Status | Source |",
        "|---|---:|---|---|",
    ])
    lines.extend(
        f"| {metric.name} | {_format_metric_display(metric)} | {metric.status} | {metric.source} |"
        for metric in report.metrics
    )
    lines.append("")
    if report.warnings:
        lines.append("Warnings:")
        lines.extend(f"- {warning}" for warning in report.warnings)
    else:
        lines.append("Warnings: None")

    return "\n".join(lines)


def format_report_markdown(report: AgentUsageReport) -> str:
    metadata = report.run_metadata
    lines = [
        "# Agent Usage Metrics Report",
        "",
        "## Run Summary",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Agent | {_markdown_cell(_display_or_dash(metadata.agent))} |",
        f"| Target type | {_markdown_cell(_display_or_dash(metadata.scope_type))} |",
        f"| Workspace | {_markdown_cell(_display_metadata(metadata.workspace))} |",
        f"| Date range | {_markdown_cell(_format_date_range(metadata.date_range))} |",
        f"| Rollout/session files | {_markdown_cell(_display_or_dash(', '.join(metadata.rollout_files)))} |",
        f"| ccusage status | {_markdown_cell(_display_or_dash(report.ccusage.get('status')))} |",
        f"| Generated at | {_markdown_cell(_display_or_dash(metadata.generated_at))} |",
        f"| Sources used | {_markdown_cell(_display_or_dash(', '.join(report.sources_used)))} |",
    ]
    if metadata.scope_type == "workspace":
        lines.insert(8, f"| Conversation titles discovered | {_conversation_titles_discovered(metadata)} |")
    else:
        lines.insert(8, f"| Conversation title | {_markdown_cell(_display_metadata(metadata.thread_title))} |")
    if report.session_breakdown_path:
        lines.append(f"| Per-session breakdown | {_markdown_cell(_markdown_link(report.session_breakdown_path))} |")
    if metadata.agent == "claude_code":
        lines.extend([
            f"| Session ID | {_markdown_cell(_display_or_dash(metadata.source_session_id))} |",
            f"| Git branch | {_markdown_cell(_display_or_dash(metadata.git_branch))} |",
            f"| Start timestamp | {_markdown_cell(_display_or_dash(metadata.start_timestamp))} |",
            f"| End timestamp | {_markdown_cell(_display_or_dash(metadata.end_timestamp))} |",
        ])
    if metadata.scope_type == "workspace":
        lines.extend([
            "",
            "## Workspace Sessions",
            "",
            "| Conversation/thread title | Rollout/session file |",
            "|---|---|",
            *(
                "| "
                f"{_markdown_cell(_display_session_title(metadata.session_titles.get(rollout_file)))} | "
                f"{_markdown_cell(rollout_file)} |"
                for rollout_file in metadata.rollout_files
            ),
        ])
    lines.extend([
        "",
        "## Metrics Summary",
        "",
        "| Metric | Value | Status | Source |",
        "|---|---:|---|---|",
    ])
    lines.extend(
        "| "
        f"{_markdown_cell(metric.name)} | "
        f"{_markdown_cell(_format_metric_display(metric))} | "
        f"{_markdown_cell(metric.status)} | "
        f"{_markdown_cell(metric.source)} |"
        for metric in report.metrics
    )

    lines.extend(["", "## Warnings", ""])
    if report.warnings:
        lines.append("Warnings:")
        lines.extend(f"- {_markdown_text(warning)}" for warning in report.warnings)
    else:
        lines.append("Warnings: None")

    return "\n".join(lines)


def format_session_breakdown_markdown(report: AgentUsageReport, rows: list[SessionBreakdownRow]) -> str:
    metadata = report.run_metadata
    lines = [
        "# Agent Usage Metrics Per-Session Breakdown",
        "",
        "## Scope",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Target type | {_markdown_cell(_display_or_dash(metadata.scope_type))} |",
        f"| Workspace | {_markdown_cell(_display_metadata(metadata.workspace))} |",
        f"| Date range | {_markdown_cell(_format_date_range(metadata.date_range))} |",
        f"| Generated at | {_markdown_cell(_display_or_dash(metadata.generated_at))} |",
        "",
        "## Sessions",
        "",
        "| Conversation/thread title | Rollout/session file | Start time | End time | Wall-clock time | API request count | Human prompts required | Tool calls | File edits | ccusage status | ccusage precision | ccusage reason | Input tokens | Output tokens | Estimated cost |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---:|---:|---:|",
    ]
    if metadata.scope_type == "workspace":
        lines.insert(9, f"| Conversation titles discovered | {_conversation_titles_discovered(metadata)} |")
    else:
        lines.insert(9, f"| Conversation title | {_markdown_cell(_display_metadata(metadata.thread_title))} |")
    if rows:
        lines.extend(_session_breakdown_row_markdown(row) for row in rows)
    else:
        lines.append("| None | None | - | - | - | - | - | - | - | - | - | - | - | - | - |")
    lines.extend([
        "",
        "## Warnings",
        "",
    ])
    if report.warnings:
        lines.append("Warnings:")
        lines.extend(f"- {_markdown_text(warning)}" for warning in report.warnings)
    else:
        lines.append("Warnings: None")
    lines.extend([
        "",
        "## Privacy",
        "",
        "- This breakdown includes safe metadata and aggregate metrics only.",
    ])
    return "\n".join(lines)


def report_to_dict(report: AgentUsageReport) -> dict[str, Any]:
    return report.to_dict()


def _basic_report_metrics(basic_metrics: list[MetricResult], agent: str = "codex") -> list[MetricResult]:
    metrics_by_name = {metric.name: metric for metric in basic_metrics}
    report_metrics: list[MetricResult] = []
    metric_order = list(_BASIC_METRIC_ORDER)
    sources = _BASIC_REPORT_SOURCES
    if agent == "claude_code":
        metric_order.extend(_CLAUDE_BASIC_METRIC_ORDER)
        sources = _CLAUDE_BASIC_REPORT_SOURCES
    for metric_name in metric_order:
        metric = metrics_by_name.get(metric_name)
        if metric is None:
            report_metrics.append(
                MetricResult(
                    name=metric_name,
                    value=None,
                    status="missing",
                    source=sources[metric_name],
                    warnings=[f"{metric_name} was not produced by the Basic Metrics Builder."],
                    notes=["Expected beta metric was absent from normalized event metrics."],
                )
            )
            continue
        report_metrics.append(_with_report_source(metric, sources[metric_name]))
    return report_metrics


def _with_report_source(metric: MetricResult, source: str) -> MetricResult:
    notes = list(metric.notes)
    if metric.name == "file_edits" and _FILE_EDITS_PARTIAL_NOTE not in notes:
        notes.append(_FILE_EDITS_PARTIAL_NOTE)
    if metric.name == "api_request_count" and _API_REQUEST_COUNT_NOTE not in notes:
        notes.append(_API_REQUEST_COUNT_NOTE)
    return MetricResult(
        name=metric.name,
        value=metric.value,
        status=metric.status,
        source=source,
        warnings=list(metric.warnings),
        notes=notes,
    )


def _ccusage_report_metrics(ccusage_result: CcusageResult | None, agent: str = "codex") -> list[MetricResult]:
    values = {
        "input_tokens": ccusage_result.input_tokens if ccusage_result else None,
        "output_tokens": ccusage_result.output_tokens if ccusage_result else None,
        "estimated_cost": ccusage_result.estimated_cost if ccusage_result else None,
        "cached_input_tokens": ccusage_result.cached_input_tokens if ccusage_result else None,
        "total_tokens": ccusage_result.total_tokens if ccusage_result else None,
        "model_name": _model_name(ccusage_result.model_breakdown if ccusage_result else None),
    }

    metric_order = list(_CCUSAGE_METRIC_ORDER)
    if agent == "claude_code":
        metric_order.extend(_CLAUDE_CCUSAGE_METRIC_ORDER)
    return [
        _ccusage_metric(metric_name, values[metric_name], ccusage_result)
        for metric_name in metric_order
    ]


def _ccusage_metric(
    name: str,
    value: Any,
    ccusage_result: CcusageResult | None,
) -> MetricResult:
    """Represent unavailable or ambiguous enrichment explicitly instead of estimating it."""
    warnings = _ccusage_warnings(ccusage_result)
    if ccusage_result is None:
        return MetricResult(
            name=name,
            value=None,
            status="missing",
            source="ccusage",
            warnings=warnings,
            notes=["ccusage was not requested, so token/cost data is missing."],
        )

    has_data = (
        ccusage_result.status in _CCUSAGE_STATUSES_WITH_DATA
        and ccusage_result.precision in _CCUSAGE_DATA_PRECISIONS
        and value is not None
    )
    if has_data:
        if ccusage_result.status == "partial" or ccusage_result.precision.startswith("partial_"):
            status = "partial"
        else:
            status = "estimated" if name == "estimated_cost" else "computed"
        return MetricResult(
            name=name,
            value=value,
            status=status,
            source="ccusage",
            warnings=list(ccusage_result.warnings),
            notes=[f"Loaded from ccusage with {ccusage_result.precision} precision."],
        )

    reason_note = f" Reason: {ccusage_result.reason}." if ccusage_result.reason else ""
    return MetricResult(
        name=name,
        value=None,
        status="missing",
        source="ccusage",
        warnings=warnings,
        notes=[f"ccusage did not provide {name} for this scope.{reason_note}"],
    )


def _run_metadata(resolved_input: ResolvedInput, generated_at: str) -> RunMetadata:
    source_metadata = resolved_input.source_metadata
    return RunMetadata(
        agent=resolved_input.agent,
        scope_type=resolved_input.scope_type,
        workspace=_safe_path_label(resolved_input.workspace),
        thread_title=resolved_input.thread_title,
        date_range=resolved_input.date_range,
        rollout_files=[path.name for path in resolved_input.rollout_files],
        resolution_status=resolved_input.resolution_status,
        codex_home_present=resolved_input.codex_home is not None,
        logs_db_present=resolved_input.logs_db is not None,
        state_db_present=resolved_input.state_db is not None,
        output_dir=_safe_path_label(resolved_input.output_dir) or "",
        generated_at=generated_at,
        session_titles=dict(resolved_input.session_titles),
        source_session_id=source_metadata.get("session_id"),
        git_branch=source_metadata.get("git_branch"),
        start_timestamp=source_metadata.get("start_timestamp"),
        end_timestamp=source_metadata.get("end_timestamp"),
    )


def _sources_used(
    resolved_input: ResolvedInput,
    ccusage_result: CcusageResult | None,
) -> list[str]:
    sources: list[str] = []
    if resolved_input.rollout_files:
        sources.append("claude_code_jsonl" if resolved_input.agent == "claude_code" else "jsonl_session")
    if resolved_input.logs_db:
        sources.append("logs_2.sqlite")
    if resolved_input.state_db:
        sources.append("state_5.sqlite")
    if ccusage_result is not None:
        sources.append("ccusage")
    return _dedupe(sources)


def _ccusage_metadata(ccusage_result: CcusageResult | None) -> dict[str, Any]:
    if ccusage_result is None:
        return {
            "status": "not_requested",
            "precision": "unavailable",
            "reason": "ccusage_not_requested",
        }
    return {
        "status": ccusage_result.status,
        "precision": ccusage_result.precision,
        "reason": ccusage_result.reason,
        "mode_attempted": ccusage_result.mode_attempted,
        "command_shape": _command_shape(ccusage_result.command),
        "command_attempt_shapes": [
            _command_shape(command)
            for command in ccusage_result.command_attempts
        ],
        "scope_requested": ccusage_result.scope_requested,
        "scope_returned": ccusage_result.scope_returned,
        "session_match": ccusage_result.session_match,
    }


def _report_warnings(
    resolved_input: ResolvedInput,
    metrics: list[MetricResult],
    ccusage_result: CcusageResult | None,
) -> list[str]:
    warnings = list(resolved_input.warnings)
    if resolved_input.scope_type == "workspace" and any(
        not title for title in resolved_input.session_titles.values()
    ):
        warnings.append(
            "Conversation/thread titles were unavailable for some sessions because no supported Codex title metadata was found."
        )
    warnings.extend(_ccusage_status_warnings(ccusage_result))
    for metric in metrics:
        warnings.extend(metric.warnings)
    return _dedupe(warnings)


def _report_notes(metrics: list[MetricResult]) -> list[str]:
    """Collect metric limitations so partial values are clear in the rendered report."""
    notes: list[str] = []
    for metric in metrics:
        notes.extend(metric.notes)
    return _dedupe(notes)


def _ccusage_warnings(ccusage_result: CcusageResult | None) -> list[str]:
    if ccusage_result is None:
        return ["ccusage was not requested; token/cost metrics are missing."]
    warnings = [*ccusage_result.warnings]
    warnings.extend(f"ccusage error: {error}" for error in ccusage_result.errors)
    if ccusage_result.status not in _CCUSAGE_STATUSES_WITH_DATA:
        warnings.insert(0, f"ccusage status: {ccusage_result.status}")
    return _dedupe(warnings)


def _ccusage_status_warnings(ccusage_result: CcusageResult | None) -> list[str]:
    if ccusage_result is None:
        return ["ccusage was not requested; token/cost metrics are missing."]
    if ccusage_result.status in _CCUSAGE_STATUSES_WITH_DATA:
        return [*ccusage_result.warnings, *(f"ccusage error: {error}" for error in ccusage_result.errors)]
    return [
        f"ccusage status: {ccusage_result.status}",
        *ccusage_result.warnings,
        *(f"ccusage error: {error}" for error in ccusage_result.errors),
    ]


def _safe_path_label(path: Path | None) -> str | None:
    if path is None:
        return None
    cleaned = str(path).strip().rstrip("\\/")
    if not cleaned:
        return None
    return Path(cleaned).name


def _model_name(model_breakdown: dict[str, Any] | None) -> str | None:
    if not model_breakdown:
        return None
    names = sorted(str(name) for name in model_breakdown if str(name).strip())
    return ", ".join(names) if names else None


def _display(value: Any) -> str:
    if value is None or value == "":
        return "unknown"
    return str(value)


def _display_or_dash(value: Any) -> str:
    if value is None:
        return MISSING_DISPLAY_VALUE
    text = str(value)
    if not text:
        return MISSING_DISPLAY_VALUE
    return text


def _display_metadata(value: Any) -> str:
    if value is None:
        return METADATA_UNAVAILABLE_DISPLAY_VALUE
    text = str(value)
    if not text:
        return METADATA_UNAVAILABLE_DISPLAY_VALUE
    return text


def _format_metric_display(metric: MetricResult) -> str:
    if metric.value is None:
        return MISSING_DISPLAY_VALUE
    if metric.name == "wall_clock_time_seconds":
        return _format_wall_clock_time(metric.value)
    return _format_metric_value(metric.value)


def _format_metric_value(value: Any) -> str:
    if value is None:
        return MISSING_DISPLAY_VALUE
    if isinstance(value, float):
        return f"{value:g}"
    return str(value)


def _format_wall_clock_time(value: Any) -> str:
    if not isinstance(value, int | float):
        return str(value)
    total_seconds = float(value)
    minutes = int(total_seconds // 60)
    remaining_seconds = round(total_seconds - (minutes * 60), 3)
    if remaining_seconds.is_integer():
        seconds_text = str(int(remaining_seconds))
    else:
        seconds_text = f"{remaining_seconds:g}"
    return f"{minutes} min {seconds_text} sec"


def _session_breakdown_row_markdown(row: SessionBreakdownRow) -> str:
    return (
        f"| {_markdown_cell(_display_session_title(row.conversation_title))} | "
        f"{_markdown_cell(row.rollout_file)} | "
        f"{_markdown_cell(_display_or_dash(row.start_time))} | "
        f"{_markdown_cell(_display_or_dash(row.end_time))} | "
        f"{_markdown_cell(_format_breakdown_metric('wall_clock_time_seconds', row.wall_clock_time_seconds))} | "
        f"{_markdown_cell(_format_breakdown_metric('api_request_count', row.api_request_count))} | "
        f"{_markdown_cell(_format_breakdown_metric('human_prompts_required', row.human_prompts_required))} | "
        f"{_markdown_cell(_format_breakdown_metric('tool_calls', row.tool_calls))} | "
        f"{_markdown_cell(_format_breakdown_metric('file_edits', row.file_edits))} | "
        f"{_markdown_cell(_display_or_dash(row.ccusage_status))} | "
        f"{_markdown_cell(_display_or_dash(row.ccusage_precision))} | "
        f"{_markdown_cell(_display_or_dash(row.ccusage_reason))} | "
        f"{_markdown_cell(_format_metric_value(row.input_tokens))} | "
        f"{_markdown_cell(_format_metric_value(row.output_tokens))} | "
        f"{_markdown_cell(_format_metric_value(row.estimated_cost))} |"
    )


def _format_breakdown_metric(name: str, value: Any) -> str:
    if value is None:
        return MISSING_DISPLAY_VALUE
    if name == "wall_clock_time_seconds":
        return _format_wall_clock_time(value)
    return _format_metric_value(value)


def _format_date_range(date_range: tuple[str, str] | None) -> str:
    if not date_range:
        return METADATA_UNAVAILABLE_DISPLAY_VALUE
    start, end = date_range
    if start == end:
        return start
    return f"{start} to {end}"


def _display_session_title(value: Any) -> str:
    if value is None:
        return SESSION_TITLE_UNAVAILABLE_DISPLAY_VALUE
    text = str(value).strip()
    return text or SESSION_TITLE_UNAVAILABLE_DISPLAY_VALUE


def _conversation_titles_discovered(metadata: RunMetadata) -> int:
    """Count distinct safe titles attached to workspace rollout sessions."""
    return len(
        {
            title.strip()
            for title in metadata.session_titles.values()
            if isinstance(title, str) and title.strip()
        }
    )


def _markdown_cell(value: Any) -> str:
    return _markdown_text(value).replace("|", "\\|")


def _markdown_text(value: Any) -> str:
    return str(value).replace("\r", " ").replace("\n", " ").strip()


def _markdown_link(path_text: str) -> str:
    safe_label = Path(path_text).name
    safe_target = safe_label.replace(" ", "%20")
    return f"[{safe_label}]({safe_target})"


def _command_shape(command: list[str] | None) -> str | None:
    if not command:
        return None
    shaped_parts: list[str] = []
    for index, part in enumerate(command):
        text = str(part)
        if index == 0:
            text = Path(text).name
            for suffix in (".cmd", ".exe", ".ps1", ".bat"):
                if text.casefold().endswith(suffix):
                    text = text[: -len(suffix)]
                    break
        shaped_parts.append(text)
    return " ".join(shaped_parts)


def _dedupe(values: list[str]) -> list[str]:
    deduped: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not value:
            continue
        if value in seen:
            continue
        seen.add(value)
        deduped.append(value)
    return deduped


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
