"""Tests for mapping raw Codex records to normalized events."""

from __future__ import annotations

import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
SCRIPTS_ROOT = REPO_ROOT / "scripts"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from agent_usage_metrics.event_normalizer import (
    normalize_codex_events,
    summarize_normalized_event_data,
)
from agent_usage_metrics.models import RawCodexData, RawCodexRecord, ResolvedInput

import verify_normalization


def make_record(
    payload: dict[str, object],
    *,
    payload_type: str | None = None,
    record_kind: str = "rollout_event",
    source_type: str = "jsonl_session",
) -> RawCodexRecord:
    inferred_payload_type = payload_type
    if inferred_payload_type is None and isinstance(payload.get("type"), str):
        inferred_payload_type = str(payload["type"])

    return RawCodexRecord(
        source_type=source_type,
        source_path=Path("rollout-test.jsonl"),
        record_kind=record_kind,
        timestamp=payload.get("timestamp") if isinstance(payload.get("timestamp"), str) else None,
        turn_id=payload.get("turn_id") if isinstance(payload.get("turn_id"), str) else None,
        payload_type=inferred_payload_type,
        raw_payload=payload,
        warnings=[],
    )


def make_raw_data(records: list[RawCodexRecord]) -> RawCodexData:
    return RawCodexData(
        records=records,
        source_files=[Path("rollout-test.jsonl")],
        warnings=[],
    )


def make_resolved_input() -> ResolvedInput:
    return ResolvedInput(
        agent="codex",
        scope_type="session",
        rollout_files=[Path("rollout-test.jsonl")],
        codex_home=Path(".codex"),
        logs_db=None,
        state_db=None,
        workspace=None,
        thread_title=None,
        date_range=None,
        output_dir=Path("out"),
        warnings=[],
    )


class EventNormalizerTests(unittest.TestCase):
    def test_task_started_becomes_normalized_task_started(self) -> None:
        raw_data = make_raw_data([
            make_record({"type": "task_started", "timestamp": "2026-07-01T12:00:00Z", "turn_id": "turn-1"})
        ])

        event_data = normalize_codex_events(raw_data)

        self.assertEqual(event_data.events[0].event_type, "task_started")
        self.assertEqual(event_data.events[0].timestamp, "2026-07-01T12:00:00Z")
        self.assertEqual(event_data.events[0].turn_id, "turn-1")

    def test_task_complete_becomes_normalized_task_completed(self) -> None:
        raw_data = make_raw_data([
            make_record({"type": "task_complete", "duration_ms": 1200})
        ])

        event_data = normalize_codex_events(raw_data)

        self.assertEqual(event_data.events[0].event_type, "task_completed")
        self.assertEqual(event_data.events[0].duration_ms, 1200)

    def test_user_message_does_not_expose_full_message_text_in_summary(self) -> None:
        raw_data = make_raw_data([
            make_record(
                {
                    "type": "user_message",
                    "role": "user",
                    "payload": {"content": "private prompt text should not be printed"},
                }
            )
        ])

        event_data = normalize_codex_events(raw_data)
        summary_text = json.dumps(summarize_normalized_event_data(event_data))

        self.assertEqual(event_data.events[0].event_type, "user_message")
        self.assertEqual(event_data.events[0].role, "user")
        self.assertTrue(event_data.events[0].metadata["content_present"])
        self.assertNotIn("private prompt text", summary_text)

    def test_patch_apply_end_becomes_file_edit_candidate_and_extracts_file_paths(self) -> None:
        raw_data = make_raw_data([
            make_record(
                {
                    "type": "patch_apply_end",
                    "changes": {
                        "src/example.py": {"status": "modified"},
                        "tests/test_example.py": {"status": "added"},
                    },
                }
            )
        ])

        event_data = normalize_codex_events(raw_data)

        self.assertEqual(event_data.events[0].event_type, "file_edit_candidate")
        self.assertEqual(
            event_data.events[0].file_paths,
            ["src/example.py", "tests/test_example.py"],
        )

    def test_codex_api_request_telemetry_becomes_api_request(self) -> None:
        raw_data = make_raw_data([
            make_record(
                {"event_name": "codex.api_request", "timestamp": "2026-07-01T12:00:00Z"},
                payload_type="codex.api_request",
                record_kind="telemetry_log",
                source_type="sqlite_logs",
            )
        ])

        event_data = normalize_codex_events(raw_data)

        self.assertEqual(event_data.events[0].event_type, "api_request")
        self.assertEqual(event_data.events[0].request_type, "codex.api_request")

    def test_codex_websocket_request_telemetry_becomes_api_request(self) -> None:
        raw_data = make_raw_data([
            make_record(
                {"event_name": "codex.websocket_request"},
                payload_type="codex.websocket_request",
                record_kind="telemetry_log",
                source_type="sqlite_logs",
            )
        ])

        event_data = normalize_codex_events(raw_data)

        self.assertEqual(event_data.events[0].event_type, "api_request")
        self.assertEqual(event_data.events[0].request_type, "codex.websocket_request")

    def test_stream_request_telemetry_becomes_stream_request(self) -> None:
        raw_data = make_raw_data([
            make_record(
                {"message": "stream_request completed"},
                payload_type="stream_request",
                record_kind="telemetry_log",
                source_type="sqlite_logs",
            )
        ])

        event_data = normalize_codex_events(raw_data)

        self.assertEqual(event_data.events[0].event_type, "stream_request")
        self.assertEqual(event_data.events[0].request_type, "stream_request")

    def test_shell_command_extracts_command_and_sandbox_permissions(self) -> None:
        raw_data = make_raw_data([
            make_record(
                {
                    "type": "shell_command",
                    "command": "python -m pytest",
                    "sandbox_permissions": "use_default",
                    "tool_name": "shell",
                }
            )
        ])

        event_data = normalize_codex_events(raw_data)

        self.assertEqual(event_data.events[0].event_type, "shell_command")
        self.assertEqual(event_data.events[0].tool_name, "shell")
        self.assertEqual(event_data.events[0].command, "python -m pytest")
        self.assertEqual(event_data.events[0].sandbox_permissions, "use_default")

    def test_unknown_payload_types_become_unknown_events_with_warnings(self) -> None:
        raw_data = make_raw_data([make_record({"type": "new_codex_event"})])

        event_data = normalize_codex_events(raw_data)

        self.assertEqual(event_data.events[0].event_type, "unknown")
        self.assertIn("Unknown Codex payload type: new_codex_event", event_data.warnings)

    def test_source_metadata_is_preserved(self) -> None:
        source_path = Path("rollout-test.jsonl")
        raw_data = make_raw_data([make_record({"type": "task_started"})])

        event_data = normalize_codex_events(raw_data)
        event = event_data.events[0]

        self.assertEqual(event.source_type, "jsonl_session")
        self.assertEqual(event.source_path, source_path)
        self.assertEqual(event.payload_type, "task_started")

    def test_normalization_does_not_calculate_final_metrics(self) -> None:
        raw_data = make_raw_data([
            make_record({"type": "task_started"}),
            make_record({"type": "task_complete"}),
        ])

        event_data = normalize_codex_events(raw_data)
        summary = summarize_normalized_event_data(event_data)

        self.assertFalse(hasattr(event_data, "metrics"))
        self.assertNotIn("wall_clock_time", summary)
        self.assertNotIn("api_request_count", summary)

    def test_verification_script_output_is_privacy_safe(self) -> None:
        raw_data = make_raw_data([
            make_record(
                {
                    "type": "user_message",
                    "payload": {"content": "private user prompt must not print"},
                }
            )
        ])

        with patch("verify_normalization.resolve_input", return_value=make_resolved_input()):
            with patch("verify_normalization.load_raw_codex_data", return_value=raw_data):
                with patch.object(sys, "argv", ["verify_normalization.py", "--rollout-file", "fake.jsonl"]):
                    output = io.StringIO()
                    with patch("sys.stdout", output):
                        exit_code = verify_normalization.main()

        self.assertEqual(exit_code, 0)
        self.assertIn('"user_message": 1', output.getvalue())
        self.assertNotIn("private user prompt", output.getvalue())


if __name__ == "__main__":
    unittest.main()
