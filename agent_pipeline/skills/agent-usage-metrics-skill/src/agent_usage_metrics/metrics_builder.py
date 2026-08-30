"""Build source-backed workflow metrics from normalized agent events."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from .models import MetricResult, NormalizedEvent, NormalizedEventData


_SOURCE = "normalized_events"


def build_basic_metrics(normalized_data: NormalizedEventData) -> list[MetricResult]:
    """Build the metrics available for the normalized agent source."""
    metrics = [
        _wall_clock_time(normalized_data.events),
        _api_request_count(normalized_data),
        _human_prompts_required(normalized_data.events),
        _tool_calls(normalized_data.events),
        _file_edits(normalized_data.events),
    ]
    if _is_claude_code(normalized_data.events):
        metrics.extend(_claude_code_metrics(normalized_data.events))
    return metrics


def summarize_metric_results(metrics: list[MetricResult]) -> list[dict[str, Any]]:
    return [
        {
            "name": metric.name,
            "value": metric.value,
            "status": metric.status,
            "source": metric.source,
            "warnings": list(metric.warnings),
            "notes": list(metric.notes),
        }
        for metric in metrics
    ]


def _wall_clock_time(events: list[NormalizedEvent]) -> MetricResult:
    """Use recorded completion durations first, then matching event timestamps."""
    starts_by_turn = _task_starts_by_turn(events)
    completed_events = [event for event in events if event.event_type == "task_completed"]
    total_seconds = 0.0
    computed_count = 0
    missing_count = 0
    warnings: list[str] = []

    for event in completed_events:
        if event.duration_ms is not None:
            total_seconds += event.duration_ms / 1000
            computed_count += 1
            continue

        elapsed_seconds = _elapsed_seconds_from_matching_start(event, starts_by_turn)
        if elapsed_seconds is None:
            missing_count += 1
            warnings.append("Missing task timing data for a task_completed event.")
            continue

        total_seconds += elapsed_seconds
        computed_count += 1

    if computed_count == 0:
        return MetricResult(
            name="wall_clock_time_seconds",
            value=None,
            status="missing",
            source=_SOURCE,
            warnings=["No usable task_started/task_completed timing data found."],
            notes=["Uses task_completed.duration_ms first, then matching task_started/task_completed timestamps."],
        )

    status = "partial" if missing_count else "computed"
    if missing_count:
        warnings.append("Some task_completed events could not be matched to timing data.")

    notes = ["Uses task_completed.duration_ms first, then matching task_started/task_completed timestamps."]
    if _is_claude_code(events):
        notes = [
            "For Claude Code, this is transcript/session duration: the span from the first to last transcript timestamp.",
            "It is elapsed session span, not active agent time.",
        ]
    return MetricResult(
        name="wall_clock_time_seconds",
        value=round(total_seconds, 3),
        status=status,
        source=_SOURCE,
        warnings=warnings,
        notes=notes,
    )


def _api_request_count(normalized_data: NormalizedEventData) -> MetricResult:
    """Count only telemetry-backed API request events; never infer them."""
    api_count = sum(1 for event in normalized_data.events if event.event_type == "api_request")
    telemetry_loaded = any(event.source_type == "sqlite_logs" for event in normalized_data.events)
    telemetry_unavailable = _telemetry_unavailable(normalized_data.warnings)

    if api_count > 0 or telemetry_loaded:
        return MetricResult(
            name="api_request_count",
            value=api_count,
            status="computed",
            source=_SOURCE,
            notes=[
                "Counts normalized api_request events from telemetry records.",
                "API request count is a workflow intensity signal, not a quality metric.",
            ],
        )

    warnings = []
    notes = [
        "0 is only reported when telemetry source evidence is present.",
        "API request count is a workflow intensity signal, not a quality metric.",
    ]
    is_claude_code = _is_claude_code(normalized_data.events)
    if is_claude_code:
        warnings.append("API request count is unavailable for Claude Code because transcripts do not provide reliable request telemetry.")
        notes = ["Claude Code API request count is not inferred from assistant messages or tool activity."]
    elif telemetry_unavailable:
        warnings.append("API telemetry was unavailable, so API request count is missing.")
    else:
        warnings.append("No telemetry evidence was available for API request counting.")

    return MetricResult(
        name="api_request_count",
        value=None,
        status="missing",
        source=_SOURCE,
        warnings=warnings,
        notes=notes,
    )


def _human_prompts_required(events: list[NormalizedEvent]) -> MetricResult:
    return MetricResult(
        name="human_prompts_required",
        value=sum(1 for event in events if event.event_type == "user_message"),
        status="computed",
        source=_SOURCE,
        notes=["Counts all user_message events, including the first human prompt."],
    )


def _tool_calls(events: list[NormalizedEvent]) -> MetricResult:
    """Count distinct tool activity while avoiding duplicate source representations."""
    seen: set[tuple[str, str, str | None, str | None, str | None, str | None, str | None]] = set()
    count = 0

    for event in events:
        if event.event_type not in {"tool_call", "shell_command"}:
            continue
        key = (
            event.source_type,
            _path_key(event.source_path),
            event.timestamp,
            event.turn_id,
            event.payload_type,
            event.tool_name,
            event.command,
        )
        if key in seen:
            continue
        seen.add(key)
        count += 1

    return MetricResult(
        name="tool_calls",
        value=count,
        status="computed",
        source=_SOURCE,
        notes=["Counts tool_call and shell_command events; shell commands are included only as tool calls."],
    )


def _file_edits(events: list[NormalizedEvent]) -> MetricResult:
    """Count explicit edit candidates and mark them partial because shell edits are invisible."""
    edit_events = [event for event in events if event.event_type == "file_edit_candidate"]
    unique_paths: set[str] = set()
    pathless_event_count = 0

    for event in edit_events:
        if event.file_paths:
            unique_paths.update(event.file_paths)
        else:
            pathless_event_count += 1

    return MetricResult(
        name="file_edits",
        value=len(unique_paths) + pathless_event_count,
        status="partial",
        source=_SOURCE,
        warnings=["File edits are partial because shell-based edits may not be captured."],
        notes=["Counts unique file paths from file_edit_candidate events, falling back to event count when paths are missing."],
    )


def _claude_code_metrics(events: list[NormalizedEvent]) -> list[MetricResult]:
    session_ids = {
        str(event.metadata.get("session_id"))
        for event in events
        if event.metadata.get("session_id")
    }
    source_paths = {event.source_path for event in events if event.source_type == "claude_code_jsonl"}
    return [
        MetricResult(
            name="session_count",
            value=len(session_ids) or len(source_paths),
            status="computed",
            source=_SOURCE,
            notes=["Counts distinct Claude Code session IDs, falling back to transcript files."],
        ),
        _count_event_metric("assistant_messages", events, "assistant_message", "Counts Claude assistant records containing text."),
        _count_event_metric("shell_commands", events, "shell_command", "Counts PowerShell, Bash, and shell tool calls."),
        MetricResult(
            name="file_reads",
            value=sum(
                1
                for event in events
                if event.event_type == "tool_call"
                and str(event.metadata.get("tool_operation", "")).casefold() == "read"
            ),
            status="computed",
            source=_SOURCE,
            notes=["Counts explicit Claude Code Read tool calls."],
        ),
        _count_event_metric(
            "file_write_edit_candidates",
            events,
            "file_edit_candidate",
            "Counts explicit Claude Code Write/Edit candidates; shell-based edits are not included.",
            status="partial",
            warnings=["File write/edit candidates are partial because shell commands can modify files."],
        ),
        _count_event_metric("tool_results", events, "tool_result", "Counts Claude Code tool_result blocks."),
        _count_event_metric("tool_failures", events, "tool_failure", "Counts tool_result blocks where is_error=true."),
    ]


def _count_event_metric(
    name: str,
    events: list[NormalizedEvent],
    event_type: str,
    note: str,
    *,
    status: str = "computed",
    warnings: list[str] | None = None,
) -> MetricResult:
    return MetricResult(
        name=name,
        value=sum(1 for event in events if event.event_type == event_type),
        status=status,
        source=_SOURCE,
        warnings=list(warnings or []),
        notes=[note],
    )


def _is_claude_code(events: list[NormalizedEvent]) -> bool:
    return any(event.source_type == "claude_code_jsonl" for event in events)


def _task_starts_by_turn(events: list[NormalizedEvent]) -> dict[str, list[NormalizedEvent]]:
    starts_by_turn: dict[str, list[NormalizedEvent]] = {}
    for event in events:
        if event.event_type != "task_started" or not event.turn_id:
            continue
        starts_by_turn.setdefault(event.turn_id, []).append(event)
    return starts_by_turn


def _elapsed_seconds_from_matching_start(
    completed_event: NormalizedEvent,
    starts_by_turn: dict[str, list[NormalizedEvent]],
) -> float | None:
    if not completed_event.turn_id or not completed_event.timestamp:
        return None

    completed_at = _parse_timestamp(completed_event.timestamp)
    if completed_at is None:
        return None

    starts = starts_by_turn.get(completed_event.turn_id, [])
    start_times = [
        parsed
        for parsed in (_parse_timestamp(start.timestamp) for start in starts if start.timestamp)
        if parsed is not None and parsed <= completed_at
    ]
    if not start_times:
        return None

    started_at = max(start_times)
    return (completed_at - started_at).total_seconds()


def _parse_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        return None


def _telemetry_unavailable(warnings: list[str]) -> bool:
    telemetry_markers = (
        "logs_db not provided",
        "logs_db not found",
        "logs_db unreadable",
        "logs table not found",
        "skipped telemetry logs",
        "logs_2.sqlite not found",
    )
    warning_text = " ".join(warnings).casefold()
    return any(marker in warning_text for marker in telemetry_markers)


def _path_key(path: Path) -> str:
    return str(path)
