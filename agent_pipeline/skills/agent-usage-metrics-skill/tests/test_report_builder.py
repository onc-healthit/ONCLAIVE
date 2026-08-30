"""Tests for report models, status labels, and Markdown formatting."""

from __future__ import annotations

import io
import json
import sys
import tempfile
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

from agent_usage_metrics.models import CcusageResult, MetricResult, ResolvedInput, SessionBreakdownRow
from agent_usage_metrics.report_builder import (
    DEFAULT_SESSION_BREAKDOWN_FILENAME,
    build_agent_usage_report,
    export_report_markdown,
    export_session_breakdown_markdown,
    format_report_markdown,
    format_session_breakdown_markdown,
    format_report_table,
)

import run_metrics


EXPECTED_REPORT_METRICS = [
    "wall_clock_time_seconds",
    "api_request_count",
    "human_prompts_required",
    "tool_calls",
    "file_edits",
    "input_tokens",
    "output_tokens",
    "estimated_cost",
]
REMOVED_REPORT_METRICS = {
    "active_agent_time",
    "human_intervention_minutes",
    "destructive_action_attempts",
}


def make_metric(
    name: str,
    value: object,
    *,
    status: str = "computed",
    source: str = "normalized_events",
    warnings: list[str] | None = None,
    notes: list[str] | None = None,
) -> MetricResult:
    return MetricResult(
        name=name,
        value=value,
        status=status,
        source=source,
        warnings=list(warnings or []),
        notes=list(notes or []),
    )


def make_basic_metrics() -> list[MetricResult]:
    return [
        make_metric("wall_clock_time_seconds", 12.5),
        make_metric("api_request_count", 3),
        make_metric("human_prompts_required", 2),
        make_metric("tool_calls", 4),
        make_metric(
            "file_edits",
            1,
            status="partial",
            warnings=["File edits are partial because shell-based edits may not be captured."],
        ),
    ]


def make_resolved_input(
    root: Path,
    *,
    scope_type: str = "session",
    rollout_count: int = 1,
    thread_title: str | None = "Example Thread",
    session_titles: dict[str, str | None] | None = None,
) -> ResolvedInput:
    codex_home = root / ".codex"
    logs_db = codex_home / "logs_2.sqlite"
    state_db = codex_home / "state_5.sqlite"
    rollout_dir = codex_home / "sessions" / "2026" / "07" / "01"
    rollouts = [
        rollout_dir / f"rollout-test-{index}.jsonl"
        for index in range(1, rollout_count + 1)
    ]
    output_dir = root / "out"
    return ResolvedInput(
        agent="codex",
        scope_type=scope_type,
        rollout_files=rollouts,
        codex_home=codex_home,
        logs_db=logs_db,
        state_db=state_db,
        workspace=root / "example-workspace",
        thread_title=thread_title,
        date_range=("2026-07-01", "2026-07-01"),
        output_dir=output_dir,
        warnings=[],
        session_titles=dict(session_titles or {}),
    )


def make_resolved_input_without_optional_metadata(root: Path) -> ResolvedInput:
    codex_home = root / ".codex"
    rollout = codex_home / "sessions" / "rollout-test.jsonl"
    return ResolvedInput(
        agent="codex",
        scope_type="session",
        rollout_files=[rollout],
        codex_home=codex_home,
        logs_db=None,
        state_db=None,
        workspace=None,
        thread_title=None,
        date_range=None,
        output_dir=root / "out",
        warnings=[],
    )


def make_ccusage_result(
    *,
    status: str = "available",
    input_tokens: int | None = 100,
    output_tokens: int | None = 25,
    estimated_cost: float | None = 0.12,
    warnings: list[str] | None = None,
    errors: list[str] | None = None,
) -> CcusageResult:
    return CcusageResult(
        status=status,
        command=["ccusage", "codex", "session", "--json", "--offline"],
        scope_requested={"scope_type": "session"},
        scope_returned={"mode": "session", "sessions": ["rollout-test"]},
        input_tokens=input_tokens,
        cached_input_tokens=None,
        output_tokens=output_tokens,
        reasoning_output_tokens=None,
        total_tokens=None,
        estimated_cost=estimated_cost,
        currency="USD",
        model_breakdown=None,
        raw_summary={"top_level_keys": ["summary"], "record_count": 1},
        warnings=list(warnings or []),
        errors=list(errors or []),
        precision="exact_session" if input_tokens is not None or output_tokens is not None or estimated_cost is not None else "unavailable",
        reason=None,
        mode_attempted="session",
        command_attempts=[["ccusage", "codex", "session", "--json", "--offline"]],
        session_match={"confidence": "exact"},
    )


class ReportBuilderTests(unittest.TestCase):
    def test_report_includes_all_expected_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(
                make_resolved_input(Path(tmp)),
                make_basic_metrics(),
                generated_at="2026-07-01T12:00:00Z",
            )

        self.assertEqual([metric.name for metric in report.metrics], EXPECTED_REPORT_METRICS)

    def test_report_excludes_shell_commands_and_quality_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(make_resolved_input(Path(tmp)), make_basic_metrics())

        metric_names = {metric.name for metric in report.metrics}
        excluded = {
            "shell_commands",
            "file_reads_searches",
            "test_runs",
            "edit_test_cycles",
            "requirement_identification_recall",
            "requirement_identification_precision",
            "correct_implementation_rate",
            "acceptance_test_pass",
            "missed_requirement_count",
            "correct_test_matches",
            "incorrect_irrelevant_test_matches",
        }
        self.assertFalse(metric_names.intersection(excluded))

    def test_removed_metrics_are_not_in_report_model_or_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(make_resolved_input(Path(tmp)), make_basic_metrics())

        metric_names = {metric.name for metric in report.metrics}
        markdown = format_report_markdown(report)
        table = format_report_table(report)
        self.assertFalse(metric_names.intersection(REMOVED_REPORT_METRICS))
        for metric_name in REMOVED_REPORT_METRICS:
            self.assertNotIn(metric_name, markdown)
            self.assertNotIn(metric_name, table)

    def test_ccusage_metrics_are_included_when_data_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(
                make_resolved_input(Path(tmp)),
                make_basic_metrics(),
                make_ccusage_result(),
            )

        metrics = {metric.name: metric for metric in report.metrics}
        self.assertEqual(metrics["input_tokens"].value, 100)
        self.assertEqual(metrics["input_tokens"].status, "computed")
        self.assertEqual(metrics["output_tokens"].value, 25)
        self.assertEqual(metrics["estimated_cost"].value, 0.12)
        self.assertEqual(metrics["estimated_cost"].status, "estimated")

    def test_ccusage_metrics_are_missing_when_ccusage_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(
                make_resolved_input(Path(tmp)),
                make_basic_metrics(),
                make_ccusage_result(
                    status="failed",
                    input_tokens=None,
                    output_tokens=None,
                    estimated_cost=None,
                    errors=["ccusage exited with code 1"],
                ),
            )

        metrics = {metric.name: metric for metric in report.metrics}
        self.assertIsNone(metrics["input_tokens"].value)
        self.assertEqual(metrics["input_tokens"].status, "missing")
        self.assertIn("ccusage status: failed", report.warnings)
        self.assertIn("ccusage error: ccusage exited with code 1", report.warnings)

    def test_file_edits_partial_note_appears(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(make_resolved_input(Path(tmp)), make_basic_metrics())

        file_edits = {metric.name: metric for metric in report.metrics}["file_edits"]
        self.assertEqual(file_edits.status, "partial")
        self.assertTrue(any("Shell-based edits or script-generated edits" in note for note in file_edits.notes))

    def test_main_markdown_links_per_session_breakdown_when_present(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = build_agent_usage_report(
                make_resolved_input(root, scope_type="conversation", rollout_count=2),
                make_basic_metrics(),
                make_ccusage_result(),
                generated_at="2026-07-01T12:00:00Z",
                session_breakdown_path=DEFAULT_SESSION_BREAKDOWN_FILENAME,
            )
            markdown = format_report_markdown(report)

        self.assertIn("| Per-session breakdown | [agent_usage_metrics_session_breakdown.md](agent_usage_metrics_session_breakdown.md) |", markdown)
        self.assertEqual(report.session_breakdown_path, DEFAULT_SESSION_BREAKDOWN_FILENAME)

    def test_markdown_export_writes_expected_sections_and_metric_states(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = build_agent_usage_report(
                make_resolved_input(root),
                make_basic_metrics(),
                make_ccusage_result(),
                generated_at="2026-07-01T12:00:00Z",
            )
            output_path = export_report_markdown(report, root / "out", "report.md")
            markdown = output_path.read_text(encoding="utf-8")

        self.assertIn("# Agent Usage Metrics Report", markdown)
        self.assertIn("## Run Summary", markdown)
        self.assertIn("## Metrics Summary", markdown)
        self.assertNotIn("Detailed Notes", markdown)
        self.assertIn("## Warnings", markdown)
        self.assertNotIn("| Resolution status |", markdown)
        self.assertNotIn("| ccusage precision |", markdown)
        self.assertNotIn("| ccusage reason |", markdown)
        self.assertIn("| wall_clock_time_seconds | 0 min 12.5 sec | computed | codex_logs |", markdown)
        self.assertIn("| file_edits | 1 | partial | codex_patch_events |", markdown)
        self.assertIn("| input_tokens | 100 | computed | ccusage |", markdown)
        for metric_name in REMOVED_REPORT_METRICS:
            self.assertNotIn(metric_name, markdown)

    def test_session_breakdown_markdown_writes_safe_per_session_rows(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = build_agent_usage_report(
                make_resolved_input(root, scope_type="workspace", rollout_count=2, thread_title=None),
                make_basic_metrics(),
                generated_at="2026-07-01T12:00:00Z",
            )
            rows = [
                SessionBreakdownRow(
                    rollout_file="rollout-test-1.jsonl",
                    conversation_title="Workspace Thread",
                    start_time="2026-07-01T12:00:00Z",
                    end_time="2026-07-01T12:00:10Z",
                    wall_clock_time_seconds=10,
                    api_request_count=3,
                    human_prompts_required=2,
                    tool_calls=4,
                    file_edits=1,
                    ccusage_status="success",
                    ccusage_precision="exact_session",
                    ccusage_reason=None,
                    input_tokens=100,
                    output_tokens=25,
                    estimated_cost=0.12,
                )
            ]
            output_path = export_session_breakdown_markdown(report, rows, root / "out", "breakdown.md")
            markdown = output_path.read_text(encoding="utf-8")

        self.assertIn("# Agent Usage Metrics Per-Session Breakdown", markdown)
        self.assertIn(
            "| Workspace Thread | rollout-test-1.jsonl | 2026-07-01T12:00:00Z | 2026-07-01T12:00:10Z | 0 min 10 sec | 3 | 2 | 4 | 1 | success | exact_session | \u2014 | 100 | 25 | 0.12 |",
            markdown,
        )
        self.assertIn("safe metadata and aggregate metrics only", markdown)

    def test_workspace_markdown_lists_available_and_unavailable_session_titles(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            session_titles = {
                "rollout-test-1.jsonl": "Inventory workspace review",
                "rollout-test-2.jsonl": None,
            }
            report = build_agent_usage_report(
                make_resolved_input(
                    root,
                    scope_type="workspace",
                    rollout_count=2,
                    thread_title=None,
                    session_titles=session_titles,
                ),
                make_basic_metrics(),
                make_ccusage_result(),
            )
            markdown = format_report_markdown(report)

        self.assertIn("## Workspace Sessions", markdown)
        self.assertIn("| Conversation titles discovered | 1 |", markdown)
        self.assertNotIn("| Conversation title |", markdown)
        self.assertIn("| Inventory workspace review | rollout-test-1.jsonl |", markdown)
        self.assertIn("| Unavailable | rollout-test-2.jsonl |", markdown)
        self.assertIn(
            "Conversation/thread titles were unavailable for some sessions because no supported Codex title metadata was found.",
            markdown,
        )

    def test_workspace_markdown_displays_long_prompt_like_state_title_without_exclusion_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state_title = "TRANSCRIPT START user: " + ("Codex authoritative state title detail " * 8)
            report = build_agent_usage_report(
                make_resolved_input(
                    root,
                    scope_type="workspace",
                    rollout_count=1,
                    thread_title=None,
                    session_titles={"rollout-test-1.jsonl": state_title},
                ),
                make_basic_metrics(),
                make_ccusage_result(),
            )
            markdown = format_report_markdown(report)

        self.assertIn(f"| {state_title.strip()} | rollout-test-1.jsonl |", markdown)
        self.assertNotIn("| Unavailable | rollout-test-1.jsonl |", markdown)
        self.assertNotIn(
            "Conversation titles were excluded because the available metadata contained raw conversation content.",
            markdown,
        )
        self.assertNotIn(
            "Conversation/thread titles were unavailable for some sessions because no supported Codex title metadata was found.",
            markdown,
        )

    def test_session_breakdown_uses_unavailable_when_title_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = build_agent_usage_report(
                make_resolved_input(root, scope_type="workspace", thread_title=None),
                make_basic_metrics(),
                make_ccusage_result(),
            )
            markdown = format_session_breakdown_markdown(
                report,
                [
                    SessionBreakdownRow(
                        rollout_file="rollout-test-1.jsonl",
                        start_time=None,
                        end_time=None,
                        wall_clock_time_seconds=None,
                        api_request_count=None,
                        human_prompts_required=None,
                        tool_calls=None,
                        file_edits=None,
                        ccusage_status=None,
                        ccusage_precision=None,
                    )
                ],
            )

        self.assertIn("| Unavailable | rollout-test-1.jsonl |", markdown)
        self.assertIn("| Conversation titles discovered | 0 |", markdown)
        self.assertNotIn("| Conversation title |", markdown)

    def test_report_metadata_uses_session_conversation_workspace_terminology(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            session_report = build_agent_usage_report(make_resolved_input(root, scope_type="session"), make_basic_metrics())
            conversation_report = build_agent_usage_report(
                make_resolved_input(root, scope_type="conversation", rollout_count=2),
                make_basic_metrics(),
            )
            workspace_report = build_agent_usage_report(
                make_resolved_input(root, scope_type="workspace", rollout_count=2, thread_title=None),
                make_basic_metrics(),
            )

        self.assertEqual(session_report.run_metadata.scope_type, "session")
        self.assertEqual(conversation_report.run_metadata.scope_type, "conversation")
        self.assertEqual(workspace_report.run_metadata.scope_type, "workspace")
        self.assertEqual(len(conversation_report.run_metadata.rollout_files), 2)
        conversation_markdown = format_report_markdown(conversation_report)
        self.assertIn("| Target type | conversation |", conversation_markdown)
        self.assertIn("| Conversation title | Example Thread |", conversation_markdown)
        self.assertIn("| Rollout/session files | rollout-test-1.jsonl, rollout-test-2.jsonl |", conversation_markdown)

    def test_markdown_report_includes_ccusage_missing_warnings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(
                make_resolved_input(Path(tmp)),
                make_basic_metrics(),
                make_ccusage_result(
                    status="permission_declined",
                    input_tokens=None,
                    output_tokens=None,
                    estimated_cost=None,
                    warnings=["ccusage permission was declined; token/cost metrics are missing."],
                ),
            )

        markdown = format_report_markdown(report)

        self.assertIn("| input_tokens | \u2014 | missing | ccusage |", markdown)
        self.assertIn("ccusage status: permission_declined", markdown)
        self.assertIn("ccusage permission was declined; token/cost metrics are missing.", markdown)

    def test_warnings_section_says_none_when_no_warnings_exist(self) -> None:
        clean_metrics = [
            make_metric("wall_clock_time_seconds", 12.5),
            make_metric("api_request_count", 3),
            make_metric("human_prompts_required", 2),
            make_metric("tool_calls", 4),
            make_metric("file_edits", 1, status="partial"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(
                make_resolved_input(Path(tmp)),
                clean_metrics,
                make_ccusage_result(),
            )

        markdown = format_report_markdown(report)
        table = format_report_table(report)
        self.assertIn("## Warnings", markdown)
        self.assertIn("Warnings: None", markdown)
        self.assertIn("Warnings: None", table)

    def test_warnings_section_lists_specific_warning_text(self) -> None:
        warning = "File edit count is partial because shell commands may modify files without explicit edit events."
        metrics = make_basic_metrics()
        metrics[-1] = make_metric("file_edits", 1, status="partial", warnings=[warning])
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(
                make_resolved_input(Path(tmp)),
                metrics,
                make_ccusage_result(),
            )

        markdown = format_report_markdown(report)
        self.assertIn("Warnings:", markdown)
        self.assertIn(f"- {warning}", markdown)

    def test_markdown_report_handles_empty_optional_metadata_clearly(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(
                make_resolved_input_without_optional_metadata(Path(tmp)),
                make_basic_metrics(),
                make_ccusage_result(
                    status="node_runtime_missing",
                    input_tokens=None,
                    output_tokens=None,
                    estimated_cost=None,
                ),
            )

        markdown = format_report_markdown(report)

        self.assertIn("| Workspace | Not available in selected Codex metadata |", markdown)
        self.assertIn("| Conversation title | Not available in selected Codex metadata |", markdown)
        self.assertIn("| Date range | Not available in selected Codex metadata |", markdown)

    def test_console_table_includes_computed_partial_and_missing_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(
                make_resolved_input(Path(tmp)),
                make_basic_metrics(),
                make_ccusage_result(),
            )

        table = format_report_table(report)

        self.assertIn("Agent Usage Metrics Report", table)
        self.assertIn("| wall_clock_time_seconds | 0 min 12.5 sec | computed | codex_logs |", table)
        self.assertIn("| file_edits | 1 | partial | codex_patch_events |", table)
        for metric_name in REMOVED_REPORT_METRICS:
            self.assertNotIn(metric_name, table)

    def test_wall_clock_display_uses_minutes_and_remaining_seconds(self) -> None:
        basic_metrics = [
            make_metric("wall_clock_time_seconds", 5329.7),
            make_metric("api_request_count", 3),
            make_metric("human_prompts_required", 2),
            make_metric("tool_calls", 4),
            make_metric("file_edits", 1, status="partial"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(make_resolved_input(Path(tmp)), basic_metrics)

        self.assertIn("| wall_clock_time_seconds | 88 min 49.7 sec |", format_report_table(report))
        self.assertIn("| wall_clock_time_seconds | 88 min 49.7 sec |", format_report_markdown(report))

    def test_run_metrics_demo_executes_against_fake_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = root / ".codex" / "sessions" / "2026" / "07" / "01" / "rollout-test.jsonl"
            rollout.parent.mkdir(parents=True)
            rollout.write_text(
                "\n".join(
                    [
                        json.dumps({"timestamp": "2026-07-01T12:00:00Z", "payload": {"type": "task_started", "turn_id": "turn-1"}}),
                        json.dumps({"timestamp": "2026-07-01T12:00:01Z", "payload": {"type": "user_message", "content": "private prompt must not print"}}),
                        json.dumps({"timestamp": "2026-07-01T12:00:02Z", "payload": {"type": "patch_apply_end", "changes": {"src/a.py": {"status": "modified"}}}}),
                        json.dumps({"timestamp": "2026-07-01T12:00:03Z", "payload": {"type": "task_complete", "turn_id": "turn-1", "duration_ms": 3000}}),
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            output_dir = root / "out"

            ccusage_result = make_ccusage_result(
                status="node_runtime_missing",
                input_tokens=None,
                output_tokens=None,
                estimated_cost=None,
                warnings=["No ccusage runtime found."],
            )
            with patch("agent_usage_metrics.report_flow.load_ccusage_data", return_value=ccusage_result) as ccusage_mock:
                with patch.object(
                    sys,
                    "argv",
                    [
                        "run_metrics.py",
                        "--rollout-file",
                        str(rollout),
                        "--output-dir",
                        str(output_dir),
                        "--md-filename",
                        "demo.md",
                    ],
                ):
                    output = io.StringIO()
                    with patch("sys.stdout", output):
                        exit_code = run_metrics.main()

            md_path = output_dir / "demo.md"
            md_exists = md_path.exists()
            json_exists = (output_dir / "agent_usage_metrics_report.json").exists()
            report_markdown = md_path.read_text(encoding="utf-8")

        self.assertEqual(exit_code, 0)
        ccusage_mock.assert_called_once()
        self.assertTrue(md_exists)
        self.assertFalse(json_exists)
        self.assertIn("Agent Usage Metrics Report", output.getvalue())
        self.assertIn("Markdown report written to:", output.getvalue())
        self.assertNotIn("JSON report written to:", output.getvalue())
        self.assertNotIn("private prompt", output.getvalue())
        self.assertNotIn("private prompt", report_markdown)

    def test_run_metrics_skip_ccusage_suppresses_default_enrichment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = root / ".codex" / "sessions" / "2026" / "07" / "01" / "rollout-test.jsonl"
            rollout.parent.mkdir(parents=True)
            rollout.write_text("", encoding="utf-8")
            output_dir = root / "out"

            with patch("agent_usage_metrics.report_flow.load_ccusage_data") as ccusage_mock:
                with patch.object(
                    sys,
                    "argv",
                    [
                        "run_metrics.py",
                        "--rollout-file",
                        str(rollout),
                        "--output-dir",
                        str(output_dir),
                        "--skip-ccusage",
                    ],
                ):
                    output = io.StringIO()
                    with patch("sys.stdout", output):
                        exit_code = run_metrics.main()
            markdown = (output_dir / "agent_usage_metrics_report.md").read_text(encoding="utf-8")
            json_exists = (output_dir / "agent_usage_metrics_report.json").exists()

        self.assertEqual(exit_code, 0)
        ccusage_mock.assert_not_called()
        self.assertFalse(json_exists)
        self.assertIn("| input_tokens | \u2014 | missing | ccusage |", markdown)

    def test_removed_metrics_do_not_reappear_for_long_sessions(self) -> None:
        basic_metrics = [
            make_metric("wall_clock_time_seconds", 7200),
            make_metric("api_request_count", None, status="missing"),
            make_metric("human_prompts_required", 1),
            make_metric("tool_calls", 0),
            make_metric("file_edits", 0, status="partial"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            report = build_agent_usage_report(make_resolved_input(Path(tmp)), basic_metrics)

        metric_names = {metric.name for metric in report.metrics}
        self.assertFalse(metric_names.intersection(REMOVED_REPORT_METRICS))


if __name__ == "__main__":
    unittest.main()
