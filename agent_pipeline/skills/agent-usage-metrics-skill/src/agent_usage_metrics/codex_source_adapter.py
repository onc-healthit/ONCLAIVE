"""Load Codex rollout and telemetry records for later normalization."""

from __future__ import annotations

import json
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Any

from .models import RawCodexData, RawCodexRecord, ResolvedInput


_TELEMETRY_NEEDLES = (
    "codex.api_request",
    "codex.websocket_request",
    "stream_request",
)
_TIMESTAMP_KEYS = ("timestamp", "created_at", "started_at", "time", "ts")
_TURN_ID_KEYS = ("turn_id", "turnId", "turn", "conversation_id", "session_id")


def load_raw_codex_data(resolved_input: ResolvedInput) -> RawCodexData:
    """Collect rollout events and optional telemetry without changing their payloads."""
    warnings = list(resolved_input.warnings)
    records: list[RawCodexRecord] = []
    source_files: list[Path] = []

    for rollout_file in resolved_input.rollout_files:
        jsonl_records, jsonl_source_files, jsonl_warnings = _load_rollout_jsonl(rollout_file)
        records.extend(jsonl_records)
        source_files.extend(jsonl_source_files)
        warnings.extend(jsonl_warnings)

    logs_records, logs_source_files, logs_warnings = _load_logs_db(resolved_input.logs_db)
    records.extend(logs_records)
    source_files.extend(logs_source_files)
    warnings.extend(logs_warnings)

    # TODO: Add state_5.sqlite metadata support after the normalizer contract is clearer.
    if resolved_input.state_db and resolved_input.state_db.exists():
        source_files.append(resolved_input.state_db.resolve())

    return RawCodexData(
        records=records,
        source_files=_dedupe_paths(source_files),
        warnings=warnings,
    )


def summarize_raw_codex_data(raw_data: RawCodexData) -> dict[str, Any]:
    payload_type_counts = Counter(record.payload_type or "unknown" for record in raw_data.records)
    telemetry_records = sum(1 for record in raw_data.records if record.record_kind == "telemetry_log")

    return {
        "raw_record_count": len(raw_data.records),
        "source_file_count": len(raw_data.source_files),
        "payload_type_counts": dict(sorted(payload_type_counts.items())),
        "telemetry_record_count": telemetry_records,
        "warnings": list(raw_data.warnings),
    }


def _load_rollout_jsonl(rollout_file: Path) -> tuple[list[RawCodexRecord], list[Path], list[str]]:
    path = Path(rollout_file).expanduser()
    warnings: list[str] = []
    records: list[RawCodexRecord] = []

    if not path.exists():
        warnings.append(f"Rollout file not found: {path.name}")
        return records, [], warnings
    if not path.is_file():
        warnings.append(f"Rollout path is not a file: {path.name}")
        return records, [], warnings

    try:
        with path.open("r", encoding="utf-8-sig") as handle:
            for line_number, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    payload = json.loads(stripped)
                except json.JSONDecodeError:
                    warnings.append(f"Malformed JSONL skipped in {path.name} at line {line_number}")
                    continue

                records.append(
                    RawCodexRecord(
                        source_type="jsonl_session",
                        source_path=path.resolve(),
                        record_kind="rollout_event",
                        timestamp=_extract_timestamp(payload),
                        turn_id=_extract_turn_id(payload),
                        payload_type=_extract_payload_type(payload),
                        raw_payload=payload,
                    )
                )
    except OSError:
        warnings.append(f"Rollout file is not readable: {path.name}")
        return records, [], warnings

    return records, [path.resolve()], warnings


def _load_logs_db(logs_db: Path | None) -> tuple[list[RawCodexRecord], list[Path], list[str]]:
    """Load telemetry rows when the optional logs database is present and readable."""
    if logs_db is None:
        return [], [], ["logs_db not provided; skipped telemetry logs"]

    path = Path(logs_db).expanduser()
    if not path.exists():
        return [], [], [f"logs_db not found: {path.name}"]
    if not path.is_file():
        return [], [], [f"logs_db path is not a file: {path.name}"]

    records: list[RawCodexRecord] = []
    warnings: list[str] = []
    connection: sqlite3.Connection | None = None

    try:
        connection = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True)
        connection.row_factory = sqlite3.Row
        if not _logs_table_exists(connection):
            return [], [path.resolve()], ["logs table not found in logs_db"]

        columns = _logs_table_columns(connection)
        if not columns:
            return [], [path.resolve()], ["logs table has no readable columns"]

        column_sql = ", ".join(_quote_identifier(column) for column in columns)
        cursor = connection.execute(f"SELECT {column_sql} FROM logs")
        for row in cursor:
            row_payload = {column: row[column] for column in columns}
            if not _row_mentions_telemetry(row_payload):
                continue
            records.append(
                RawCodexRecord(
                    source_type="sqlite_logs",
                    source_path=path.resolve(),
                    record_kind="telemetry_log",
                    timestamp=_extract_timestamp(row_payload),
                    turn_id=_extract_turn_id(row_payload),
                    payload_type=_extract_telemetry_payload_type(row_payload),
                    raw_payload=row_payload,
                )
            )
    except sqlite3.Error as exc:
        warnings.append(f"logs_db unreadable or unsupported: {exc.__class__.__name__}")
    finally:
        if connection is not None:
            connection.close()

    return records, [path.resolve()], warnings


def _logs_table_exists(connection: sqlite3.Connection) -> bool:
    cursor = connection.execute(
        "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'logs' LIMIT 1"
    )
    return cursor.fetchone() is not None


def _logs_table_columns(connection: sqlite3.Connection) -> list[str]:
    cursor = connection.execute("PRAGMA table_info(logs)")
    return [str(row["name"]) for row in cursor.fetchall()]


def _row_mentions_telemetry(row_payload: dict[str, Any]) -> bool:
    return any(needle in _value_text(row_payload) for needle in _TELEMETRY_NEEDLES)


def _extract_payload_type(payload: Any) -> str | None:
    if isinstance(payload, dict):
        nested_payload = payload.get("payload")
        if isinstance(nested_payload, dict) and isinstance(nested_payload.get("type"), str):
            return nested_payload["type"]
        if isinstance(payload.get("type"), str):
            return payload["type"]
    return None


def _extract_telemetry_payload_type(row_payload: dict[str, Any]) -> str | None:
    for value in row_payload.values():
        text = _value_text(value)
        for needle in _TELEMETRY_NEEDLES:
            if needle in text:
                return needle
    return None


def _extract_timestamp(payload: Any) -> str | None:
    return _extract_first_string_value(payload, _TIMESTAMP_KEYS)


def _extract_turn_id(payload: Any) -> str | None:
    value = _extract_first_string_value(payload, _TURN_ID_KEYS)
    if value is not None:
        return value
    if isinstance(payload, dict):
        for key in _TURN_ID_KEYS:
            raw_value = payload.get(key)
            if isinstance(raw_value, int):
                return str(raw_value)
    return None


def _extract_first_string_value(payload: Any, keys: tuple[str, ...]) -> str | None:
    if not isinstance(payload, dict):
        return None

    for key in keys:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, int | float):
            return str(value)

    for value in payload.values():
        if isinstance(value, dict):
            nested_value = _extract_first_string_value(value, keys)
            if nested_value is not None:
                return nested_value

    return None


def _value_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="ignore")
    if isinstance(value, dict):
        return " ".join(_value_text(item) for item in value.values())
    return str(value)


def _quote_identifier(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def _dedupe_paths(paths: list[Path]) -> list[Path]:
    deduped: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        deduped.append(resolved)
    return deduped
