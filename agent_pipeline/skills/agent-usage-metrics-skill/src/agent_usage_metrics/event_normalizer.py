"""Convert raw Codex records into the common metric event format."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from .models import NormalizedEvent, NormalizedEventData, RawCodexData, RawCodexRecord


_EVENT_TYPE_MAP = {
    "task_started": "task_started",
    "task_complete": "task_completed",
    "task_completed": "task_completed",
    "user_message": "user_message",
    "patch_apply_end": "file_edit_candidate",
}
_API_REQUEST_TYPES = {"codex.api_request", "codex.websocket_request"}
_STREAM_REQUEST_TYPES = {"stream_request"}
_PROMPT_LIKE_KEYS = {"content", "message", "messages", "prompt", "text", "input", "output"}
_TIMESTAMP_KEYS = ("timestamp", "created_at", "started_at", "time", "ts")
_TURN_ID_KEYS = ("turn_id", "turnId", "turn", "conversation_id", "session_id")
_DURATION_KEYS = ("duration_ms", "durationMs", "elapsed_ms", "elapsedMs")
_ROLE_KEYS = ("role",)
_TOOL_NAME_KEYS = ("tool_name", "toolName", "tool", "name")
_COMMAND_KEYS = ("command", "cmd", "shell_command")
_SANDBOX_KEYS = ("sandbox_permissions", "sandboxPermissions")


def normalize_codex_events(raw_data: RawCodexData) -> NormalizedEventData:
    """Normalize raw Codex records while retaining only metric-relevant fields."""
    warnings = list(raw_data.warnings)
    events: list[NormalizedEvent] = []

    for record in raw_data.records:
        normalized = _normalize_record(record)
        events.extend(normalized)
        for event in normalized:
            warnings.extend(event.warnings)

    return NormalizedEventData(
        events=events,
        source_record_count=len(raw_data.records),
        normalized_event_count=len(events),
        warnings=warnings,
    )


def summarize_normalized_event_data(event_data: NormalizedEventData) -> dict[str, Any]:
    event_type_counts = Counter(event.event_type for event in event_data.events)
    return {
        "source_record_count": event_data.source_record_count,
        "normalized_event_count": event_data.normalized_event_count,
        "event_type_counts": dict(sorted(event_type_counts.items())),
        "warning_count": len(event_data.warnings),
        "warnings": list(event_data.warnings),
    }


def _normalize_record(record: RawCodexRecord) -> list[NormalizedEvent]:
    event_type, event_warnings = _event_type_for_record(record)
    payload = record.raw_payload if isinstance(record.raw_payload, dict) else {}

    return [
        NormalizedEvent(
            event_type=event_type,
            timestamp=record.timestamp or _extract_first_string(payload, _TIMESTAMP_KEYS),
            turn_id=record.turn_id or _extract_first_string(payload, _TURN_ID_KEYS),
            source_type=record.source_type,
            source_path=record.source_path,
            payload_type=record.payload_type or _payload_type(payload),
            role=_extract_first_string(payload, _ROLE_KEYS),
            tool_name=_extract_tool_name(record, payload),
            command=_extract_command(payload),
            file_paths=_extract_file_paths(payload),
            duration_ms=_extract_duration_ms(payload),
            request_type=_request_type(record),
            sandbox_permissions=_extract_first_string(payload, _SANDBOX_KEYS),
            metadata=_safe_metadata(record, payload, event_type),
            warnings=event_warnings,
        )
    ]


def _event_type_for_record(record: RawCodexRecord) -> tuple[str, list[str]]:
    """Classify known record shapes and leave unsupported shapes visible as warnings."""
    payload_type = record.payload_type or _payload_type(record.raw_payload)
    if record.record_kind == "telemetry_log" or record.source_type == "sqlite_logs":
        telemetry_type = _telemetry_type(record)
        if telemetry_type in _API_REQUEST_TYPES:
            return "api_request", []
        if telemetry_type in _STREAM_REQUEST_TYPES:
            return "stream_request", []
        return "unknown", [f"Unknown telemetry record type: {telemetry_type or 'missing'}"]

    payload = record.raw_payload if isinstance(record.raw_payload, dict) else {}
    if payload_type in _EVENT_TYPE_MAP:
        return _EVENT_TYPE_MAP[payload_type], []
    if _is_shell_command(payload_type, payload):
        return "shell_command", []
    if _extract_tool_name(record, payload):
        return "tool_call", []

    return "unknown", [f"Unknown Codex payload type: {payload_type or 'missing'}"]


def _payload_type(payload: Any) -> str | None:
    if not isinstance(payload, dict):
        return None
    nested_payload = payload.get("payload")
    if isinstance(nested_payload, dict) and isinstance(nested_payload.get("type"), str):
        return nested_payload["type"]
    if isinstance(payload.get("type"), str):
        return payload["type"]
    return None


def _telemetry_type(record: RawCodexRecord) -> str | None:
    if record.payload_type:
        return record.payload_type
    text = _safe_value_text(record.raw_payload)
    for request_type in (*_API_REQUEST_TYPES, *_STREAM_REQUEST_TYPES):
        if request_type in text:
            return request_type
    return None


def _is_shell_command(payload_type: str | None, payload: dict[str, Any]) -> bool:
    tool_name = _extract_first_string(payload, _TOOL_NAME_KEYS)
    if payload_type in {"shell_command", "exec_command", "command"}:
        return True
    if tool_name and tool_name.casefold() in {"shell", "shell_command", "exec_command", "run_shell_command"}:
        return True
    return bool(_extract_command(payload) and tool_name and "shell" in tool_name.casefold())


def _extract_tool_name(record: RawCodexRecord, payload: dict[str, Any]) -> str | None:
    tool_name = _extract_first_string(payload, _TOOL_NAME_KEYS)
    if tool_name:
        return tool_name
    if record.payload_type == "tool_call":
        return "tool_call"
    return None


def _extract_command(payload: dict[str, Any]) -> str | None:
    return _extract_first_string(payload, _COMMAND_KEYS)


def _extract_duration_ms(payload: dict[str, Any]) -> int | None:
    value = _extract_first_value(payload, _DURATION_KEYS)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        try:
            return int(float(value))
        except ValueError:
            return None
    return None


def _request_type(record: RawCodexRecord) -> str | None:
    if record.record_kind != "telemetry_log" and record.source_type != "sqlite_logs":
        return None
    return record.payload_type


def _extract_file_paths(payload: dict[str, Any]) -> list[str]:
    """Find explicit edit paths; commands are intentionally not treated as file edits."""
    paths: list[str] = []
    changes = _find_first_dict(payload, ("changes",))
    if changes:
        paths.extend(str(path) for path in changes.keys())

    for key in ("file_path", "filePath", "path"):
        value = _extract_first_value(payload, (key,))
        if isinstance(value, str) and value:
            paths.append(value)

    files = _extract_first_value(payload, ("files", "file_paths", "filePaths"))
    if isinstance(files, list):
        paths.extend(str(path) for path in files if isinstance(path, str))

    return sorted(set(paths))


def _safe_metadata(record: RawCodexRecord, payload: dict[str, Any], event_type: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "record_kind": record.record_kind,
        "raw_payload_keys": sorted(str(key) for key in payload.keys()),
    }
    if event_type == "user_message":
        metadata["content_present"] = _contains_prompt_like_value(payload)
    if event_type == "file_edit_candidate":
        metadata["file_path_count"] = len(_extract_file_paths(payload))

    text_blob = _safe_value_text(payload)
    if "approval" in text_blob:
        metadata["approval_related"] = True
    if "wait" in text_blob or "blocked" in text_blob:
        metadata["wait_related"] = True

    return metadata


def _extract_first_string(payload: dict[str, Any], keys: tuple[str, ...]) -> str | None:
    value = _extract_first_value(payload, keys)
    if isinstance(value, str) and value.strip():
        return value.strip()
    if isinstance(value, int | float):
        return str(value)
    return None


def _extract_first_value(payload: Any, keys: tuple[str, ...]) -> Any:
    if not isinstance(payload, dict):
        return None
    normalized_keys = {_normalize_key(key) for key in keys}
    for key, value in payload.items():
        if _normalize_key(str(key)) in normalized_keys:
            return value
    for value in payload.values():
        if isinstance(value, dict):
            nested = _extract_first_value(value, keys)
            if nested is not None:
                return nested
    return None


def _find_first_dict(payload: Any, keys: tuple[str, ...]) -> dict[str, Any] | None:
    value = _extract_first_value(payload, keys)
    return value if isinstance(value, dict) else None


def _contains_prompt_like_value(payload: dict[str, Any]) -> bool:
    for key, value in _walk_key_values(payload):
        if _normalize_key(key) in {_normalize_key(item) for item in _PROMPT_LIKE_KEYS}:
            if isinstance(value, str) and value:
                return True
            if isinstance(value, list | dict) and value:
                return True
    return False


def _safe_value_text(value: Any) -> str:
    if isinstance(value, dict):
        pieces = []
        for key, item in value.items():
            if _normalize_key(str(key)) in {_normalize_key(prompt_key) for prompt_key in _PROMPT_LIKE_KEYS}:
                continue
            pieces.append(_safe_value_text(item))
        return " ".join(pieces).casefold()
    if isinstance(value, list):
        return " ".join(_safe_value_text(item) for item in value).casefold()
    if value is None:
        return ""
    return str(value).casefold()


def _walk_key_values(payload: Any) -> list[tuple[str, Any]]:
    values: list[tuple[str, Any]] = []
    if isinstance(payload, dict):
        for key, value in payload.items():
            values.append((str(key), value))
            values.extend(_walk_key_values(value))
    elif isinstance(payload, list):
        for item in payload:
            values.extend(_walk_key_values(item))
    return values


def _normalize_key(key: str) -> str:
    return key.replace("_", "").replace("-", "").casefold()
