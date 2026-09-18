"""Tests for source-backed workflow metric calculations."""

from __future__ import annotations

import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
SCRIPTS_ROOT = REPO_ROOT / "scripts"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from agent_usage_metrics.metrics_builder import build_basic_metrics, summarize_metric_results
from agent_usage_metrics.models import NormalizedEvent, NormalizedEventData, RawCodexData, ResolvedInput

import verify_metrics


def make_event(
    event_type: str,
    *,
    timestamp: str | None = None,
    turn_id: str | None = None,
    source_type: str = "jsonl_session",
    payload_type: str | None = None,
    tool_name: str | None = None,
    command: str | None = None,
    file_paths: list[str] | None = None,
    duration_ms: int | None = None,
    request_type: str | None = None,
) -> NormalizedEvent:
    return NormalizedEvent(
        event_type=event_type,
        timestamp=timestamp,
        turn_id=turn_id,
        source_type=source_type,
        source_path=Path("source.jsonl"),
        payload_type=payload_type,
        tool_name=tool_name,
        command=command,
        file_paths=list(file_paths or []),
        duration_ms=duration_ms,
        request_type=request_type,
    )


def make_data(events: list[NormalizedEvent], warnings: list[str] | None = None) -> NormalizedEventData:
    return NormalizedEventData(
        events=events,
        source_record_count=len(events),
        normalized_event_count=len(events),
        warnings=list(warnings or []),
    )


def metrics_by_name(data: NormalizedEventData):
    return {metric.name: metric for metric in build_basic_metrics(data)}


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


class MetricsBuilderTests(unittest.TestCase):
    def test_wall_clock_time_uses_duration_ms_when_available(self) -> None:
        metrics = metrics_by_name(make_data([make_event("task_completed", duration_ms=2500)]))

        self.assertEqual(metrics["wall_clock_time_seconds"].value, 2.5)
        self.assertEqual(metrics["wall_clock_time_seconds"].status, "computed")

    def test_wall_clock_time_falls_back_to_timestamp_difference(self) -> None:
        metrics = metrics_by_name(
            make_data(
                [
                    make_event("task_started", timestamp="2026-07-01T12:00:00Z", turn_id="turn-1"),
                    make_event("task_completed", timestamp="2026-07-01T12:00:05Z", turn_id="turn-1"),
                ]
            )
        )

        self.assertEqual(metrics["wall_clock_time_seconds"].value, 5.0)
        self.assertEqual(metrics["wall_clock_time_seconds"].status, "computed")

    def test_wall_clock_time_returns_missing_without_timing_data(self) -> None:
        metrics = metrics_by_name(make_data([make_event("task_started", turn_id="turn-1")]))

        self.assertIsNone(metrics["wall_clock_time_seconds"].value)
        self.assertEqual(metrics["wall_clock_time_seconds"].status, "missing")

    def test_wall_clock_time_returns_partial_when_some_turns_are_missing(self) -> None:
        metrics = metrics_by_name(
            make_data(
                [
                    make_event("task_completed", duration_ms=1000),
                    make_event("task_completed", timestamp="2026-07-01T12:00:05Z", turn_id="missing"),
                ]
            )
        )

        self.assertEqual(metrics["wall_clock_time_seconds"].value, 1.0)
        self.assertEqual(metrics["wall_clock_time_seconds"].status, "partial")

    def test_api_request_count_counts_api_request_events(self) -> None:
        metrics = metrics_by_name(
            make_data(
                [
                    make_event("api_request", source_type="sqlite_logs", request_type="codex.api_request"),
                    make_event("api_request", source_type="sqlite_logs", request_type="codex.websocket_request"),
                ]
            )
        )

        self.assertEqual(metrics["api_request_count"].value, 2)
        self.assertEqual(metrics["api_request_count"].status, "computed")

    def test_api_request_count_reports_zero_when_telemetry_loaded(self) -> None:
        metrics = metrics_by_name(make_data([make_event("stream_request", source_type="sqlite_logs")]))

        self.assertEqual(metrics["api_request_count"].value, 0)
        self.assertEqual(metrics["api_request_count"].status, "computed")

    def test_api_request_count_missing_without_telemetry_evidence(self) -> None:
        metrics = metrics_by_name(make_data([make_event("user_message")]))

        self.assertIsNone(metrics["api_request_count"].value)
        self.assertEqual(metrics["api_request_count"].status, "missing")

    def test_human_prompts_required_counts_all_user_messages(self) -> None:
        metrics = metrics_by_name(make_data([make_event("user_message"), make_event("user_message")]))

        self.assertEqual(metrics["human_prompts_required"].value, 2)

    def test_tool_calls_counts_tool_call_and_shell_command_events(self) -> None:
        metrics = metrics_by_name(
            make_data(
                [
                    make_event("tool_call", tool_name="apply_patch"),
                    make_event("shell_command", tool_name="shell", command="python -m pytest"),
                ]
            )
        )

        self.assertEqual(metrics["tool_calls"].value, 2)

    def test_shell_commands_is_not_output_as_its_own_metric(self) -> None:
        metric_names = set(metrics_by_name(make_data([make_event("shell_command")])).keys())

        self.assertIn("tool_calls", metric_names)
        self.assertNotIn("shell_commands", metric_names)

    def test_file_edits_counts_unique_file_paths(self) -> None:
        metrics = metrics_by_name(
            make_data(
                [
                    make_event("file_edit_candidate", file_paths=["src/a.py", "src/b.py"]),
                    make_event("file_edit_candidate", file_paths=["src/a.py"]),
                ]
            )
        )

        self.assertEqual(metrics["file_edits"].value, 2)

    def test_file_edits_falls_back_to_event_count_when_paths_are_missing(self) -> None:
        metrics = metrics_by_name(
            make_data(
                [
                    make_event("file_edit_candidate"),
                    make_event("file_edit_candidate"),
                ]
            )
        )

        self.assertEqual(metrics["file_edits"].value, 2)

    def test_file_edits_status_is_partial(self) -> None:
        metrics = metrics_by_name(make_data([make_event("file_edit_candidate", file_paths=["src/a.py"])]))

        self.assertEqual(metrics["file_edits"].status, "partial")

    def test_excluded_metrics_are_not_returned(self) -> None:
        metric_names = set(metrics_by_name(make_data([])).keys())
        excluded = {
            "active_agent_time",
            "human_intervention_minutes",
            "file_reads",
            "test_runs",
            "edit_test_cycles",
            "destructive_action_attempts",
            "input_tokens",
            "cached_input_tokens",
            "output_tokens",
            "reasoning_output_tokens",
            "total_tokens",
            "estimated_cost",
            "requirement_identification_recall",
            "acceptance_test_pass",
        }

        self.assertFalse(metric_names.intersection(excluded))

    def test_builder_does_not_call_ccusage(self) -> None:
        load_mock = Mock()

        with patch("agent_usage_metrics.ccusage_adapter.load_ccusage_data", load_mock):
            build_basic_metrics(make_data([make_event("api_request")]))

        load_mock.assert_not_called()

    def test_builder_does_not_read_raw_files(self) -> None:
        with patch("builtins.open", side_effect=AssertionError("raw file read attempted")):
            metrics = build_basic_metrics(make_data([make_event("user_message")]))

        self.assertEqual(len(metrics), 5)

    def test_verification_script_output_is_privacy_safe(self) -> None:
        normalized_data = make_data(
            [
                make_event("user_message"),
                make_event("shell_command", command="private shell command should not print"),
            ]
        )

        with patch("verify_metrics.resolve_input", return_value=make_resolved_input()):
            with patch("verify_metrics.load_raw_codex_data", return_value=RawCodexData([], [], [])):
                with patch("verify_metrics.normalize_codex_events", return_value=normalized_data):
                    with patch.object(sys, "argv", ["verify_metrics.py", "--rollout-file", "fake.jsonl"]):
                        output = io.StringIO()
                        with patch("sys.stdout", output):
                            exit_code = verify_metrics.main()

        self.assertEqual(exit_code, 0)
        self.assertIn('"name": "tool_calls"', output.getvalue())
        self.assertNotIn("private shell command", output.getvalue())

    def test_metric_summary_is_safe_and_structured(self) -> None:
        metrics = build_basic_metrics(make_data([make_event("user_message")]))
        summary = summarize_metric_results(metrics)

        self.assertIsInstance(summary, list)
        self.assertIn("name", summary[0])
        self.assertIn("status", summary[0])


if __name__ == "__main__":
    unittest.main()
