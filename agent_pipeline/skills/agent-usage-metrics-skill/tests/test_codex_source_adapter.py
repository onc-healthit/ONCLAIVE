"""Tests for loading Codex rollout and telemetry sources."""

from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from agent_usage_metrics.codex_source_adapter import (
    load_raw_codex_data,
    summarize_raw_codex_data,
)
from agent_usage_metrics.models import RawCodexRecord, ResolvedInput


def make_resolved_input(
    root: Path,
    rollout_files: list[Path],
    *,
    logs_db: Path | None = None,
    state_db: Path | None = None,
) -> ResolvedInput:
    return ResolvedInput(
        agent="codex",
        scope_type="session",
        rollout_files=rollout_files,
        codex_home=root / ".codex",
        logs_db=logs_db,
        state_db=state_db,
        workspace=None,
        thread_title=None,
        date_range=None,
        output_dir=root / "out",
        warnings=[],
    )


def make_rollout(root: Path, lines: list[str]) -> Path:
    rollout = root / ".codex" / "sessions" / "2026" / "06" / "30" / "rollout-test.jsonl"
    rollout.parent.mkdir(parents=True, exist_ok=True)
    rollout.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return rollout


def make_logs_db(root: Path) -> Path:
    logs_db = root / ".codex" / "logs_2.sqlite"
    logs_db.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(logs_db)
    try:
        connection.execute(
            "CREATE TABLE logs (timestamp TEXT, event_name TEXT, message TEXT, turn_id TEXT)"
        )
        connection.execute(
            "INSERT INTO logs VALUES (?, ?, ?, ?)",
            (
                "2026-06-30T12:00:00Z",
                "codex.api_request",
                "telemetry only",
                "turn-1",
            ),
        )
        connection.execute(
            "INSERT INTO logs VALUES (?, ?, ?, ?)",
            (
                "2026-06-30T12:01:00Z",
                "other.event",
                "not selected",
                "turn-2",
            ),
        )
        connection.execute(
            "INSERT INTO logs VALUES (?, ?, ?, ?)",
            (
                "2026-06-30T12:02:00Z",
                "other.event",
                "stream_request completed",
                "turn-3",
            ),
        )
        connection.commit()
    finally:
        connection.close()
    return logs_db


class CodexSourceAdapterTests(unittest.TestCase):
    def test_jsonl_rollout_events_are_wrapped_as_raw_records(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            payload = {
                "timestamp": "2026-06-30T12:00:00Z",
                "turn_id": "turn-1",
                "payload": {"type": "agent_message", "content": "internal raw payload"},
            }
            rollout = make_rollout(root, [json.dumps(payload)])

            raw_data = load_raw_codex_data(make_resolved_input(root, [rollout]))

            self.assertEqual(len(raw_data.records), 1)
            record = raw_data.records[0]
            self.assertIsInstance(record, RawCodexRecord)
            self.assertEqual(record.source_type, "jsonl_session")
            self.assertEqual(record.record_kind, "rollout_event")
            self.assertEqual(record.timestamp, "2026-06-30T12:00:00Z")
            self.assertEqual(record.turn_id, "turn-1")
            self.assertEqual(record.payload_type, "agent_message")
            self.assertEqual(record.raw_payload, payload)

    def test_malformed_jsonl_lines_warn_and_continue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            valid_payload = {"type": "valid_event"}
            rollout = make_rollout(root, ["not-json", json.dumps(valid_payload)])

            raw_data = load_raw_codex_data(make_resolved_input(root, [rollout]))

            self.assertEqual(len(raw_data.records), 1)
            self.assertEqual(raw_data.records[0].payload_type, "valid_event")
            self.assertIn("Malformed JSONL skipped in rollout-test.jsonl at line 1", raw_data.warnings)

    def test_missing_optional_logs_db_is_handled_safely(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root, [json.dumps({"type": "event"})])

            raw_data = load_raw_codex_data(make_resolved_input(root, [rollout], logs_db=None))

            self.assertEqual(len(raw_data.records), 1)
            self.assertIn("logs_db not provided; skipped telemetry logs", raw_data.warnings)

    def test_fake_sqlite_logs_telemetry_rows_are_wrapped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root, [])
            logs_db = make_logs_db(root)

            raw_data = load_raw_codex_data(make_resolved_input(root, [rollout], logs_db=logs_db))

            telemetry_records = [
                record for record in raw_data.records if record.record_kind == "telemetry_log"
            ]
            self.assertEqual(len(telemetry_records), 2)
            self.assertEqual(telemetry_records[0].source_type, "sqlite_logs")
            self.assertEqual(telemetry_records[0].payload_type, "codex.api_request")
            self.assertEqual(telemetry_records[0].turn_id, "turn-1")
            self.assertEqual(telemetry_records[1].payload_type, "stream_request")

    def test_state_db_is_recorded_but_not_queried(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root, [])
            state_db = root / ".codex" / "state_5.sqlite"
            state_db.write_text("not a sqlite database", encoding="utf-8")

            raw_data = load_raw_codex_data(make_resolved_input(root, [rollout], state_db=state_db))

            self.assertIn(state_db.resolve(), raw_data.source_files)
            self.assertFalse(any("state_5.sqlite" in warning for warning in raw_data.warnings))

    def test_adapter_does_not_calculate_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root, [json.dumps({"type": "api_request"})])

            raw_data = load_raw_codex_data(make_resolved_input(root, [rollout]))

            self.assertEqual(raw_data.records[0].record_kind, "rollout_event")
            self.assertFalse(hasattr(raw_data.records[0], "metric_type"))
            self.assertNotIn("api_request_count", summarize_raw_codex_data(raw_data))

    def test_privacy_safe_summary_excludes_payloads_and_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(
                root,
                [
                    json.dumps(
                        {
                            "type": "user_message",
                            "payload": {"content": "private prompt should stay internal"},
                        }
                    )
                ],
            )

            raw_data = load_raw_codex_data(make_resolved_input(root, [rollout]))
            summary = summarize_raw_codex_data(raw_data)
            summary_text = json.dumps(summary)

            self.assertEqual(summary["raw_record_count"], 1)
            self.assertEqual(summary["source_file_count"], 1)
            self.assertEqual(summary["payload_type_counts"], {"user_message": 1})
            self.assertNotIn("private prompt", summary_text)
            self.assertNotIn(str(root), summary_text)


if __name__ == "__main__":
    unittest.main()
