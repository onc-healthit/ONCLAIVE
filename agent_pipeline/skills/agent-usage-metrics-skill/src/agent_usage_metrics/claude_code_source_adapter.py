"""Load Claude Code transcripts and normalize their workflow events."""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from .models import NormalizedEvent, NormalizedEventData, RawCodexData, RawCodexRecord, ResolvedInput


_SHELL_TOOLS = {"bash", "powershell", "shell", "shellcommand", "run_shell_command"}
_WRITE_TOOLS = {"edit", "multiedit", "notebookedit", "write"}
_READ_TOOLS = {"read"}


def load_raw_claude_code_data(resolved_input: ResolvedInput) -> RawCodexData:
    """Load Claude Code transcript JSONL without interpreting usage or cost data."""
    warnings = list(resolved_input.warnings)
    records: list[RawCodexRecord] = []
    source_files: list[Path] = []

    for transcript_file in resolved_input.rollout_files:
        path = Path(transcript_file).expanduser()
        if not path.exists() or not path.is_file():
            warnings.append(f"Claude Code transcript not found: {path.name}")
            continue

        source_files.append(path.resolve())
        try:
            with path.open("r", encoding="utf-8-sig") as handle:
                for line_number, line in enumerate(handle, start=1):
                    stripped = line.strip()
                    if not stripped:
                        continue
                    try:
                        payload = json.loads(stripped)
                    except json.JSONDecodeError:
                        warnings.append(
                            f"Malformed Claude Code JSONL skipped in {path.name} at line {line_number}"
                        )
                        continue
                    if not isinstance(payload, dict):
                        warnings.append(
                            f"Non-object Claude Code JSONL skipped in {path.name} at line {line_number}"
                        )
                        continue
                    records.append(
                        RawCodexRecord(
                            source_type="claude_code_jsonl",
                            source_path=path.resolve(),
                            record_kind="claude_transcript_event",
                            timestamp=_string(payload.get("timestamp")),
                            turn_id=_string(payload.get("sessionId")),
                            payload_type=_string(payload.get("type")),
                            raw_payload=payload,
                        )
                    )
        except OSError:
            warnings.append(f"Claude Code transcript is not readable: {path.name}")

    return RawCodexData(records=records, source_files=_dedupe_paths(source_files), warnings=warnings)


def normalize_claude_code_events(raw_data: RawCodexData) -> NormalizedEventData:
    """Map Claude transcript records into the shared event representation."""
    warnings = list(raw_data.warnings)
    events: list[NormalizedEvent] = []

    records_by_source: dict[Path, list[RawCodexRecord]] = {}
    for record in raw_data.records:
        records_by_source.setdefault(record.source_path, []).append(record)
        events.extend(_normalize_record(record))

    for source_path, records in records_by_source.items():
        events.extend(_session_boundary_events(source_path, records))

    return NormalizedEventData(
        events=events,
        source_record_count=len(raw_data.records),
        normalized_event_count=len(events),
        warnings=warnings,
    )


def summarize_raw_claude_code_data(raw_data: RawCodexData) -> dict[str, Any]:
    return {
        "raw_record_count": len(raw_data.records),
        "source_file_count": len(raw_data.source_files),
        "payload_type_counts": dict(
            sorted(Counter(record.payload_type or "unknown" for record in raw_data.records).items())
        ),
        "warnings": list(raw_data.warnings),
    }


def _normalize_record(record: RawCodexRecord) -> list[NormalizedEvent]:
    payload = record.raw_payload if isinstance(record.raw_payload, dict) else {}
    message = payload.get("message")
    if not isinstance(message, dict):
        return []

    role = _string(message.get("role"))
    content = message.get("content")
    base_metadata = _safe_metadata(payload, message)
    events: list[NormalizedEvent] = []

    if role == "user" and isinstance(content, str) and content.strip():
        events.append(_event(record, "user_message", role=role, metadata=base_metadata))

    if not isinstance(content, list):
        return events

    if role == "assistant" and any(
        isinstance(block, dict) and block.get("type") == "text" and _string(block.get("text"))
        for block in content
    ):
        events.append(_event(record, "assistant_message", role=role, metadata=base_metadata))

    for block in content:
        if not isinstance(block, dict):
            continue
        block_type = _string(block.get("type"))
        if block_type == "tool_use":
            events.extend(_tool_use_events(record, block, base_metadata))
        elif block_type == "tool_result":
            events.extend(_tool_result_events(record, block, base_metadata))
    return events


def _tool_use_events(
    record: RawCodexRecord,
    block: dict[str, Any],
    base_metadata: dict[str, Any],
) -> list[NormalizedEvent]:
    """Turn Claude tool-use records into workflow events with safe metadata."""
    tool_name = _string(block.get("name")) or "unknown"
    normalized_name = _normalize_name(tool_name)
    tool_input = block.get("input") if isinstance(block.get("input"), dict) else {}
    metadata = {
        **base_metadata,
        "tool_use_id": _string(block.get("id")),
        "tool_operation": normalized_name,
    }
    file_paths = _file_paths(tool_input)

    if normalized_name in _SHELL_TOOLS:
        return [
            _event(
                record,
                "shell_command",
                role="assistant",
                tool_name=tool_name,
                command=_string(tool_input.get("command")),
                metadata=metadata,
            )
        ]

    tool_event = _event(
        record,
        "tool_call",
        role="assistant",
        tool_name=tool_name,
        file_paths=file_paths,
        metadata=metadata,
    )
    events = [tool_event]
    if normalized_name in _WRITE_TOOLS:
        events.append(
            _event(
                record,
                "file_edit_candidate",
                role="assistant",
                tool_name=tool_name,
                file_paths=file_paths,
                metadata={**metadata, "file_path_count": len(file_paths)},
            )
        )
    return events


def _tool_result_events(
    record: RawCodexRecord,
    block: dict[str, Any],
    base_metadata: dict[str, Any],
) -> list[NormalizedEvent]:
    is_error = block.get("is_error") is True
    metadata = {
        **base_metadata,
        "tool_use_id": _string(block.get("tool_use_id")),
        "is_error": is_error,
    }
    events = [_event(record, "tool_result", role="user", metadata=metadata)]
    if is_error:
        events.append(_event(record, "tool_failure", role="user", metadata=metadata))
    return events


def _session_boundary_events(source_path: Path, records: list[RawCodexRecord]) -> list[NormalizedEvent]:
    timestamped = [record for record in records if _parse_timestamp(record.timestamp) is not None]
    if not timestamped:
        return []
    first = min(timestamped, key=lambda record: _parse_timestamp(record.timestamp) or datetime.max)
    last = max(timestamped, key=lambda record: _parse_timestamp(record.timestamp) or datetime.min)
    turn_id = next((record.turn_id for record in records if record.turn_id), None)
    common = {
        "duration_kind": "transcript_span",
        "session_id": turn_id,
        "source_file": source_path.name,
    }
    return [
        NormalizedEvent(
            event_type="task_started",
            timestamp=first.timestamp,
            turn_id=turn_id,
            source_type="claude_code_jsonl",
            source_path=source_path,
            payload_type="session_boundary",
            metadata={**common, "boundary": "start"},
        ),
        NormalizedEvent(
            event_type="task_completed",
            timestamp=last.timestamp,
            turn_id=turn_id,
            source_type="claude_code_jsonl",
            source_path=source_path,
            payload_type="session_boundary",
            metadata={**common, "boundary": "end"},
        ),
    ]


def _event(
    record: RawCodexRecord,
    event_type: str,
    *,
    role: str | None = None,
    tool_name: str | None = None,
    command: str | None = None,
    file_paths: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
) -> NormalizedEvent:
    return NormalizedEvent(
        event_type=event_type,
        timestamp=record.timestamp,
        turn_id=record.turn_id,
        source_type=record.source_type,
        source_path=record.source_path,
        payload_type=record.payload_type,
        role=role,
        tool_name=tool_name,
        command=command,
        file_paths=list(file_paths or []),
        metadata=dict(metadata or {}),
    )


def _safe_metadata(payload: dict[str, Any], message: dict[str, Any]) -> dict[str, Any]:
    return {
        "session_id": _string(payload.get("sessionId")),
        "record_uuid": _string(payload.get("uuid")),
        "parent_uuid": _string(payload.get("parentUuid")),
        "workspace": _string(payload.get("cwd")),
        "git_branch": _string(payload.get("gitBranch")),
        "model": _string(message.get("model")),
        "stop_reason": _string(message.get("stop_reason")) or _string(payload.get("stopReason")),
    }


def _file_paths(tool_input: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for key in ("file_path", "filePath", "path", "notebook_path"):
        value = _string(tool_input.get(key))
        if value:
            paths.append(value)
    return sorted(set(paths))


def _normalize_name(value: str) -> str:
    return value.replace("_", "").replace("-", "").casefold()


def _string(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _parse_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        return None


def _dedupe_paths(paths: list[Path]) -> list[Path]:
    return list(dict.fromkeys(paths))
