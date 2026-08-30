"""Tests for Claude Code transcript support and ccusage enrichment."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from agent_usage_metrics.ccusage_adapter import (
    CcusageRuntime,
    build_ccusage_command,
    parse_ccusage_json,
)
from agent_usage_metrics.claude_code_source_adapter import (
    load_raw_claude_code_data,
    normalize_claude_code_events,
    summarize_raw_claude_code_data,
)
from agent_usage_metrics.input_resolver import resolve_input
from agent_usage_metrics.metrics_builder import build_basic_metrics
from agent_usage_metrics.models import ResolvedInput
from agent_usage_metrics.report_builder import build_agent_usage_report
from agent_usage_metrics.report_flow import run_report_flow


CLAUDE_FIXTURE = REPO_ROOT / "tests" / "fixtures" / "claude_code" / "sample_1.jsonl"
CCUSAGE_FIXTURE = REPO_ROOT / "tests" / "fixtures" / "ccusage" / "claude_session.json"
CCUSAGE_AMBIGUOUS_FIXTURE = (
    REPO_ROOT / "tests" / "fixtures" / "ccusage" / "claude_session_ambiguous.json"
)
SESSION_ID = "7f8c3ed2-3907-43fe-b9ed-db16df5b5302"


def make_resolved_input(root: Path, transcript: Path = CLAUDE_FIXTURE) -> ResolvedInput:
    return ResolvedInput(
        agent="claude_code",
        scope_type="session",
        rollout_files=[transcript],
        codex_home=None,
        logs_db=None,
        state_db=None,
        workspace=Path(r"C:\workspace\sample-project"),
        thread_title=None,
        date_range=("2026-07-21", "2026-07-21"),
        output_dir=root / "out",
        claude_home=root / ".claude",
        source_metadata={"session_id": SESSION_ID},
    )


class ClaudeCodeSourceAdapterTests(unittest.TestCase):
    def test_fixture_loads_and_normalizes_expected_workflow_events(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resolved = make_resolved_input(Path(tmp))
            raw_data = load_raw_claude_code_data(resolved)
            event_data = normalize_claude_code_events(raw_data)
            counts: dict[str, int] = {}
            for event in event_data.events:
                counts[event.event_type] = counts.get(event.event_type, 0) + 1

            self.assertEqual(summarize_raw_claude_code_data(raw_data)["raw_record_count"], 29)
            self.assertEqual(counts["user_message"], 2)
            self.assertEqual(counts["assistant_message"], 3)
            self.assertEqual(counts["shell_command"], 1)
            self.assertEqual(counts["tool_call"], 3)
            self.assertEqual(counts["file_edit_candidate"], 2)
            self.assertEqual(counts["tool_result"], 4)
            self.assertNotIn("tool_failure", counts)
            self.assertEqual(counts["task_started"], 1)
            self.assertEqual(counts["task_completed"], 1)

    def test_workflow_metrics_are_built_without_ccusage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resolved = make_resolved_input(Path(tmp))
            events = normalize_claude_code_events(load_raw_claude_code_data(resolved))
            metrics = {metric.name: metric for metric in build_basic_metrics(events)}

            self.assertEqual(metrics["session_count"].value, 1)
            self.assertEqual(metrics["human_prompts_required"].value, 2)
            self.assertEqual(metrics["assistant_messages"].value, 3)
            self.assertEqual(metrics["tool_calls"].value, 4)
            self.assertEqual(metrics["shell_commands"].value, 1)
            self.assertEqual(metrics["file_reads"].value, 1)
            self.assertEqual(metrics["file_write_edit_candidates"].value, 2)
            self.assertEqual(metrics["tool_results"].value, 4)
            self.assertEqual(metrics["tool_failures"].value, 0)
            self.assertEqual(metrics["wall_clock_time_seconds"].value, 44.132)
            self.assertEqual(metrics["api_request_count"].status, "missing")
            self.assertTrue(any("unavailable for Claude Code" in warning for warning in metrics["api_request_count"].warnings))

    def test_error_tool_result_emits_result_and_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            transcript = root / "failed.jsonl"
            transcript.write_text(
                json.dumps(
                    {
                        "type": "user",
                        "sessionId": "failed-session",
                        "timestamp": "2026-07-21T10:00:00Z",
                        "message": {
                            "role": "user",
                            "content": [{"type": "tool_result", "tool_use_id": "tool-1", "is_error": True}],
                        },
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            resolved = make_resolved_input(root, transcript)
            events = normalize_claude_code_events(load_raw_claude_code_data(resolved)).events
            self.assertEqual(sum(event.event_type == "tool_result" for event in events), 1)
            self.assertEqual(sum(event.event_type == "tool_failure" for event in events), 1)

    def test_explicit_transcript_resolution_captures_safe_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resolved = resolve_input(
                rollout_file=CLAUDE_FIXTURE,
                agent="claude_code",
                output_dir=Path(tmp) / "out",
            )
            self.assertEqual(resolved.agent, "claude_code")
            self.assertEqual(resolved.source_metadata["session_id"], SESSION_ID)
            self.assertEqual(resolved.workspace.name, "sample-project")
            self.assertEqual(resolved.thread_title, "Claude Code logs sample generation")
            self.assertEqual(
                resolved.session_titles[CLAUDE_FIXTURE.name],
                "Claude Code logs sample generation",
            )
            self.assertEqual(resolved.source_metadata["start_timestamp"], "2026-07-21T14:41:08.967000Z")
            self.assertEqual(resolved.source_metadata["end_timestamp"], "2026-07-21T14:41:53.099000Z")

    def test_report_flow_skips_ccusage_without_losing_workflow_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resolved = make_resolved_input(Path(tmp))
            result = run_report_flow(resolved, skip_ccusage=True)
            metrics = {metric.name: metric for metric in result.report.metrics}
            self.assertEqual(result.status, "completed")
            self.assertEqual(metrics["human_prompts_required"].value, 2)
            self.assertEqual(metrics["input_tokens"].status, "missing")
            self.assertIn("claude_code_jsonl", result.report.sources_used)

    def test_latest_claude_query_discovers_transcripts_under_projects(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            transcript = root / ".claude" / "projects" / "sample-project" / "session.jsonl"
            transcript.parent.mkdir(parents=True)
            transcript.write_text(
                json.dumps(
                    {
                        "type": "user",
                        "sessionId": "discovered-session",
                        "timestamp": "2026-07-21T10:00:00Z",
                        "cwd": r"C:\workspace\sample-project",
                        "gitBranch": "main",
                        "message": {"role": "user", "content": "safe test prompt"},
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            resolved = resolve_input(
                query="Create a report for the latest Claude Code session.",
                claude_home=root / ".claude",
                output_dir=root / "out",
            )
            self.assertEqual(resolved.agent, "claude_code")
            self.assertEqual(resolved.rollout_files, [transcript.resolve()])
            self.assertEqual(resolved.source_metadata["session_id"], "discovered-session")


class ClaudeCodeCcusageTests(unittest.TestCase):
    def test_claude_uses_unified_ccusage_session_command(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resolved = make_resolved_input(Path(tmp))
            runtime = CcusageRuntime("ccusage", ["ccusage"], "available", False)
            self.assertEqual(
                build_ccusage_command(resolved, runtime),
                ["ccusage", "session", "--all", "--json", "--offline"],
            )

    def test_mocked_ccusage_json_matches_exact_claude_session(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resolved = make_resolved_input(Path(tmp))
            data = json.loads(CCUSAGE_FIXTURE.read_text(encoding="utf-8"))
            result = parse_ccusage_json(
                data,
                resolved,
                ["ccusage", "session", "--all", "--json", "--offline"],
            )
            self.assertEqual(result.status, "available")
            self.assertEqual(result.precision, "exact_session")
            self.assertEqual(result.input_tokens, 1200)
            self.assertEqual(result.cached_input_tokens, 300)
            self.assertEqual(result.output_tokens, 450)
            self.assertEqual(result.total_tokens, 1950)
            self.assertEqual(result.estimated_cost, 0.0123)
            self.assertIn("claude-sonnet-test", result.model_breakdown)

            events = normalize_claude_code_events(load_raw_claude_code_data(resolved))
            report = build_agent_usage_report(resolved, build_basic_metrics(events), result)
            metrics = {metric.name: metric for metric in report.metrics}
            self.assertEqual(metrics["cached_input_tokens"].value, 300)
            self.assertEqual(metrics["total_tokens"].value, 1950)
            self.assertEqual(metrics["model_name"].value, "claude-sonnet-test")

    def test_ambiguous_ccusage_rows_are_not_guessed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resolved = make_resolved_input(Path(tmp))
            data = json.loads(CCUSAGE_AMBIGUOUS_FIXTURE.read_text(encoding="utf-8"))
            result = parse_ccusage_json(
                data,
                resolved,
                ["ccusage", "session", "--all", "--json", "--offline"],
            )
            self.assertEqual(result.status, "ambiguous_match")
            self.assertIsNone(result.input_tokens)
            self.assertIsNone(result.estimated_cost)


if __name__ == "__main__":
    unittest.main()
