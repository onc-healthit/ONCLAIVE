"""Tests for the end-to-end report generation flow."""

from __future__ import annotations

import json
import io
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

from agent_usage_metrics.models import CcusageResult, RawCodexData, RawCodexRecord, ResolvedInput
from agent_usage_metrics.report_flow import CCUSAGE_PERMISSION_QUESTION, run_report_flow

import run_metrics


def make_resolved_input(root: Path) -> ResolvedInput:
    rollout = root / ".codex" / "sessions" / "2026" / "07" / "01" / "rollout-test.jsonl"
    rollout.parent.mkdir(parents=True)
    rollout.write_text(
        "\n".join(
            [
                json.dumps({"timestamp": "2026-07-01T12:00:00Z", "payload": {"type": "task_started", "turn_id": "turn-1"}}),
                json.dumps({"timestamp": "2026-07-01T12:00:01Z", "payload": {"type": "tool_call", "name": "apply_patch"}}),
                json.dumps({"timestamp": "2026-07-01T12:01:15.5Z", "payload": {"type": "task_complete", "turn_id": "turn-1", "duration_ms": 75500}}),
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    codex_home = root / ".codex"
    return ResolvedInput(
        agent="codex",
        scope_type="session",
        rollout_files=[rollout],
        codex_home=codex_home,
        logs_db=None,
        state_db=None,
        workspace=root / "workspace",
        thread_title="Example",
        date_range=("2026-07-01", "2026-07-01"),
        output_dir=root / "out",
        warnings=[],
    )


def make_conversation_resolved_input(root: Path) -> ResolvedInput:
    resolved = make_resolved_input(root)
    second = root / ".codex" / "sessions" / "2026" / "07" / "01" / "rollout-test-2.jsonl"
    second.write_text("", encoding="utf-8")
    return ResolvedInput(
        agent=resolved.agent,
        scope_type="conversation",
        rollout_files=[*resolved.rollout_files, second],
        codex_home=resolved.codex_home,
        logs_db=resolved.logs_db,
        state_db=resolved.state_db,
        workspace=resolved.workspace,
        thread_title=resolved.thread_title,
        date_range=resolved.date_range,
        output_dir=resolved.output_dir,
        warnings=list(resolved.warnings),
        resolution_status="exact",
    )


def make_ccusage_result(
    status: str,
    *,
    input_tokens: int | None = None,
    output_tokens: int | None = None,
    estimated_cost: float | None = None,
    warnings: list[str] | None = None,
    precision: str | None = None,
    reason: str | None = None,
    session_match: dict[str, object] | None = None,
) -> CcusageResult:
    has_values = input_tokens is not None or output_tokens is not None or estimated_cost is not None
    return CcusageResult(
        status=status,
        command=["bunx", "ccusage", "codex", "session", "--json", "--offline"],
        scope_requested={"scope_type": "session"},
        scope_returned={"mode": "session"} if has_values else None,
        input_tokens=input_tokens,
        cached_input_tokens=None,
        output_tokens=output_tokens,
        reasoning_output_tokens=None,
        total_tokens=None,
        estimated_cost=estimated_cost,
        currency=None,
        model_breakdown=None,
        raw_summary=None,
        warnings=list(warnings or []),
        errors=[],
        precision=precision or ("exact_session" if has_values else "unavailable"),
        reason=reason,
        mode_attempted="session",
        command_attempts=[["bunx", "ccusage", "codex", "session", "--json", "--offline"]],
        session_match=session_match if session_match is not None else ({"confidence": "exact"} if has_values else None),
    )


def make_raw_record(
    rollout: Path,
    payload: dict[str, object],
    *,
    source_type: str = "jsonl_session",
    record_kind: str = "rollout_event",
    payload_type: str | None = None,
) -> RawCodexRecord:
    resolved_payload_type = payload_type
    if resolved_payload_type is None and payload.get("type"):
        resolved_payload_type = str(payload.get("type"))
    return RawCodexRecord(
        source_type=source_type,
        source_path=rollout,
        record_kind=record_kind,
        timestamp=str(payload.get("timestamp")) if payload.get("timestamp") else None,
        turn_id=str(payload.get("turn_id")) if payload.get("turn_id") else None,
        payload_type=resolved_payload_type,
        raw_payload=payload,
    )


def make_session_raw_data(
    rollout: Path,
    *,
    start: str,
    end: str,
    duration_ms: int,
    api_requests: int,
    human_prompts: int,
    tool_calls: int,
    file_edits: int,
) -> RawCodexData:
    records: list[RawCodexRecord] = [
        make_raw_record(rollout, {"timestamp": start, "type": "task_started", "turn_id": rollout.stem}),
    ]
    for index in range(api_requests):
        records.append(
            make_raw_record(
                rollout,
                {"timestamp": start, "message": f"codex.api_request {index}"},
                source_type="sqlite_logs",
                record_kind="telemetry_log",
                payload_type="codex.api_request",
            )
        )
    for index in range(human_prompts):
        records.append(
            make_raw_record(
                rollout,
                {"timestamp": start, "type": "user_message", "content": f"prompt {index}"},
            )
        )
    for index in range(tool_calls):
        records.append(
            make_raw_record(
                rollout,
                {"timestamp": start, "type": "tool_call", "name": f"tool-{index}"},
            )
        )
    for index in range(file_edits):
        records.append(
            make_raw_record(
                rollout,
                {
                    "timestamp": start,
                    "type": "patch_apply_end",
                    "changes": {f"src/file_{rollout.stem}_{index}.py": {"status": "modified"}},
                },
            )
        )
    records.append(
        make_raw_record(
            rollout,
            {"timestamp": end, "type": "task_complete", "turn_id": rollout.stem, "duration_ms": duration_ms},
        )
    )
    return RawCodexData(records=records, source_files=[rollout], warnings=[])


def metrics_by_name(result):
    return {metric.name: metric for metric in result.report.metrics}


class ReportFlowTests(unittest.TestCase):
    def test_requires_permission_is_returned_before_finalizing_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_resolved_input(root)
            ccusage_result = make_ccusage_result(
                "requires_permission",
                warnings=["ccusage may need to be downloaded or cached by bunx/npx/pnpm."],
            )

            with patch("agent_usage_metrics.report_flow.load_ccusage_data", return_value=ccusage_result):
                result = run_report_flow(resolved)

            self.assertEqual(result.status, "requires_permission")
            self.assertEqual(result.permission_question, CCUSAGE_PERMISSION_QUESTION)
            self.assertIsNone(result.report)
            self.assertFalse((root / "out" / "agent_usage_metrics_report.md").exists())
            self.assertFalse((root / "out" / "agent_usage_metrics_report.json").exists())

    def test_declined_permission_generates_report_with_missing_ccusage_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_resolved_input(root)
            ccusage_result = make_ccusage_result(
                "requires_permission",
                warnings=["ccusage may need to be downloaded or cached by bunx/npx/pnpm."],
            )

            with patch("agent_usage_metrics.report_flow.load_ccusage_data", return_value=ccusage_result):
                result = run_report_flow(resolved, decline_download=True)

            markdown = (root / "out" / "agent_usage_metrics_report.md").read_text(encoding="utf-8")

        self.assertEqual(result.status, "completed")
        self.assertEqual(result.ccusage_result.status, "permission_declined")
        self.assertIsNone(result.json_path)
        self.assertFalse((root / "out" / "agent_usage_metrics_report.json").exists())
        metrics = metrics_by_name(result)
        for metric_name in ("input_tokens", "output_tokens", "estimated_cost"):
            self.assertIsNone(metrics[metric_name].value)
            self.assertEqual(metrics[metric_name].status, "missing")
            self.assertEqual(metrics[metric_name].source, "ccusage")
        self.assertIn("ccusage permission was declined", markdown)

    def test_allow_download_treats_permission_as_approved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_resolved_input(root)
            ccusage_result = make_ccusage_result(
                "available_via_bunx",
                input_tokens=10,
                output_tokens=4,
                estimated_cost=0.02,
            )

            with patch("agent_usage_metrics.report_flow.load_ccusage_data", return_value=ccusage_result) as ccusage_mock:
                result = run_report_flow(resolved, allow_download=True)

        self.assertEqual(result.status, "completed")
        ccusage_mock.assert_called_once()
        self.assertTrue(ccusage_mock.call_args.kwargs["allow_download"])
        metrics = {metric.name: metric for metric in result.report.metrics}
        self.assertEqual(metrics["input_tokens"].value, 10)
        self.assertEqual(metrics["estimated_cost"].status, "estimated")

    def test_skip_ccusage_does_not_ask_or_load_ccusage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_resolved_input(root)

            with patch("agent_usage_metrics.report_flow.load_ccusage_data") as ccusage_mock:
                result = run_report_flow(resolved, skip_ccusage=True)

        self.assertEqual(result.status, "completed")
        self.assertIsNone(result.ccusage_result)
        ccusage_mock.assert_not_called()
        metrics = {metric.name: metric for metric in result.report.metrics}
        self.assertIsNone(metrics["input_tokens"].value)
        self.assertEqual(metrics["input_tokens"].status, "missing")

    def test_ccusage_receives_resolved_target_type_and_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_conversation_resolved_input(root)
            ccusage_result = make_ccusage_result(
                "unsupported_scope",
                warnings=["conversation ccusage unsupported"],
            )

            with patch("agent_usage_metrics.report_flow.load_ccusage_data", return_value=ccusage_result) as ccusage_mock:
                result = run_report_flow(resolved)

        passed_resolved = ccusage_mock.call_args.args[0]
        self.assertEqual(passed_resolved.scope_type, "conversation")
        self.assertEqual(passed_resolved.thread_title, "Example")
        self.assertEqual(len(passed_resolved.rollout_files), 2)
        self.assertEqual(result.report.run_metadata.scope_type, "conversation")

    def test_session_breakdown_uses_per_session_ccusage_details(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_conversation_resolved_input(root)
            first, second = resolved.rollout_files
            ccusage_result = make_ccusage_result(
                "partial",
                input_tokens=100,
                output_tokens=25,
                estimated_cost=0.12,
                precision="partial_conversation",
                reason="partial_session_matches",
                warnings=["ccusage matched 1 of 2 conversation sessions; token/cost metrics are partial."],
                session_match={
                    "requested_session_count": 2,
                    "matched_session_count": 1,
                    "unmatched_session_count": 1,
                    "scope_type": "conversation",
                    "sessions": [
                        {
                            "rollout_file": first.name,
                            "status": "success",
                            "precision": "exact_session",
                            "reason": None,
                            "input_tokens": 100,
                            "output_tokens": 25,
                            "estimated_cost": 0.12,
                        },
                        {
                            "rollout_file": second.name,
                            "status": "no_confident_match",
                            "precision": "no_confident_match",
                            "reason": "no_confident_session_match",
                            "input_tokens": None,
                            "output_tokens": None,
                            "estimated_cost": None,
                        },
                    ],
                },
            )

            with patch("agent_usage_metrics.report_flow.load_ccusage_data", return_value=ccusage_result):
                result = run_report_flow(resolved)
            breakdown = result.breakdown_path.read_text(encoding="utf-8")

        self.assertIn(f"| {first.name} |", breakdown)
        self.assertIn("| success | exact_session | \u2014 | 100 | 25 | 0.12 |", breakdown)
        self.assertIn(f"| {second.name} |", breakdown)
        self.assertIn("| no_confident_match | no_confident_match | no_confident_session_match | \u2014 | \u2014 | \u2014 |", breakdown)

    def test_single_session_report_behavior_is_unchanged_and_has_no_breakdown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_resolved_input(root)

            result = run_report_flow(resolved, skip_ccusage=True)

        metrics = metrics_by_name(result)
        self.assertEqual(result.status, "completed")
        self.assertEqual(metrics["wall_clock_time_seconds"].value, 75.5)
        self.assertEqual(metrics["tool_calls"].value, 1)
        self.assertIsNone(result.breakdown_path)
        self.assertFalse((root / "out" / "agent_usage_metrics_session_breakdown.md").exists())

    def test_conversation_metrics_sum_independent_session_metrics_and_writes_breakdown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_conversation_resolved_input(root)
            first, second = resolved.rollout_files
            raw_by_name = {
                first.name: make_session_raw_data(
                    first,
                    start="2026-07-01T10:00:00Z",
                    end="2026-07-01T10:00:10Z",
                    duration_ms=10_000,
                    api_requests=11,
                    human_prompts=3,
                    tool_calls=4,
                    file_edits=1,
                ),
                second.name: make_session_raw_data(
                    second,
                    start="2026-07-01T12:00:00Z",
                    end="2026-07-01T12:00:20Z",
                    duration_ms=20_000,
                    api_requests=14,
                    human_prompts=5,
                    tool_calls=6,
                    file_edits=2,
                ),
            }

            def load_for_session(session_input: ResolvedInput) -> RawCodexData:
                self.assertEqual(session_input.scope_type, "session")
                self.assertEqual(len(session_input.rollout_files), 1)
                return raw_by_name[session_input.rollout_files[0].name]

            with patch("agent_usage_metrics.report_flow.load_raw_codex_data", side_effect=load_for_session) as load_mock:
                result = run_report_flow(resolved, skip_ccusage=True)

            markdown = (root / "out" / "agent_usage_metrics_report.md").read_text(encoding="utf-8")
            breakdown = result.breakdown_path.read_text(encoding="utf-8")

        metrics = metrics_by_name(result)
        self.assertEqual(load_mock.call_count, 2)
        self.assertEqual(metrics["wall_clock_time_seconds"].value, 30.0)
        self.assertNotEqual(metrics["wall_clock_time_seconds"].value, 7220.0)
        self.assertEqual(metrics["api_request_count"].value, 25)
        self.assertEqual(metrics["human_prompts_required"].value, 8)
        self.assertEqual(metrics["tool_calls"].value, 10)
        self.assertEqual(metrics["file_edits"].value, 3)
        self.assertIn("agent_usage_metrics_session_breakdown.md", markdown)
        self.assertIn(first.name, breakdown)
        self.assertIn(second.name, breakdown)
        self.assertIn("| 0 min 10 sec | 11 | 3 | 4 | 1 |", breakdown)
        self.assertIn("| 0 min 20 sec | 14 | 5 | 6 | 2 |", breakdown)

    def test_ccusage_enrichment_does_not_change_codex_derived_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_conversation_resolved_input(root)
            first, second = resolved.rollout_files
            raw_by_name = {
                first.name: make_session_raw_data(
                    first,
                    start="2026-07-01T10:00:00Z",
                    end="2026-07-01T10:00:10Z",
                    duration_ms=10_000,
                    api_requests=11,
                    human_prompts=3,
                    tool_calls=4,
                    file_edits=1,
                ),
                second.name: make_session_raw_data(
                    second,
                    start="2026-07-01T12:00:00Z",
                    end="2026-07-01T12:00:20Z",
                    duration_ms=20_000,
                    api_requests=14,
                    human_prompts=5,
                    tool_calls=6,
                    file_edits=2,
                ),
            }
            ccusage_result = make_ccusage_result(
                "success",
                input_tokens=300,
                output_tokens=40,
                estimated_cost=None,
                precision="exact_conversation",
                reason="estimated_cost_not_provided",
                warnings=["ccusage did not provide estimated_cost for matched session row(s)."],
                session_match={
                    "requested_session_count": 2,
                    "matched_session_count": 2,
                    "unmatched_session_count": 0,
                    "scope_type": "conversation",
                    "sessions": [],
                },
            )

            with patch(
                "agent_usage_metrics.report_flow.load_raw_codex_data",
                side_effect=lambda session_input: raw_by_name[session_input.rollout_files[0].name],
            ):
                with patch("agent_usage_metrics.report_flow.load_ccusage_data", return_value=ccusage_result):
                    result = run_report_flow(resolved)

        metrics = metrics_by_name(result)
        self.assertEqual(metrics["wall_clock_time_seconds"].value, 30.0)
        self.assertEqual(metrics["api_request_count"].value, 25)
        self.assertEqual(metrics["human_prompts_required"].value, 8)
        self.assertEqual(metrics["tool_calls"].value, 10)
        self.assertEqual(metrics["file_edits"].value, 3)
        self.assertEqual(metrics["input_tokens"].value, 300)
        self.assertEqual(metrics["output_tokens"].value, 40)
        self.assertIsNone(metrics["estimated_cost"].value)
        self.assertEqual(metrics["estimated_cost"].status, "missing")

    def test_workspace_metrics_sum_independent_session_metrics_and_writes_breakdown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_conversation_resolved_input(root)
            first, second = resolved.rollout_files
            resolved = ResolvedInput(
                agent=resolved.agent,
                scope_type="workspace",
                rollout_files=resolved.rollout_files,
                codex_home=resolved.codex_home,
                logs_db=resolved.logs_db,
                state_db=resolved.state_db,
                workspace=resolved.workspace,
                thread_title=None,
                date_range=resolved.date_range,
                output_dir=resolved.output_dir,
                warnings=[],
                resolution_status="exact",
                session_titles={
                    first.name: "Workspace inventory review",
                    second.name: None,
                },
            )
            raw_by_name = {
                first.name: make_session_raw_data(
                    first,
                    start="2026-07-01T10:00:00Z",
                    end="2026-07-01T10:00:05Z",
                    duration_ms=5_000,
                    api_requests=2,
                    human_prompts=1,
                    tool_calls=2,
                    file_edits=1,
                ),
                second.name: make_session_raw_data(
                    second,
                    start="2026-07-01T11:00:00Z",
                    end="2026-07-01T11:00:07Z",
                    duration_ms=7_000,
                    api_requests=3,
                    human_prompts=4,
                    tool_calls=5,
                    file_edits=2,
                ),
            }

            with patch(
                "agent_usage_metrics.report_flow.load_raw_codex_data",
                side_effect=lambda session_input: raw_by_name[session_input.rollout_files[0].name],
            ):
                result = run_report_flow(resolved, skip_ccusage=True)
            breakdown_exists = result.breakdown_path.exists()
            main_markdown = result.markdown_path.read_text(encoding="utf-8")
            breakdown_markdown = result.breakdown_path.read_text(encoding="utf-8")

        metrics = metrics_by_name(result)
        self.assertEqual(metrics["wall_clock_time_seconds"].value, 12.0)
        self.assertEqual(metrics["api_request_count"].value, 5)
        self.assertEqual(metrics["human_prompts_required"].value, 5)
        self.assertEqual(metrics["tool_calls"].value, 7)
        self.assertEqual(metrics["file_edits"].value, 3)
        self.assertIsNotNone(result.breakdown_path)
        self.assertTrue(breakdown_exists)
        self.assertIn("| Conversation titles discovered | 1 |", main_markdown)
        self.assertIn("| Workspace inventory review |", main_markdown)
        self.assertIn(f"| Workspace inventory review | {first.name} |", breakdown_markdown)
        self.assertIn(f"| Unavailable | {second.name} |", breakdown_markdown)

    def test_cli_surfaces_requires_permission_without_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resolved = make_resolved_input(root)
            ccusage_result = make_ccusage_result(
                "requires_permission",
                warnings=["ccusage may need to be downloaded or cached by bunx/npx/pnpm."],
            )

            with patch("agent_usage_metrics.report_flow.load_ccusage_data", return_value=ccusage_result):
                with patch.object(
                    sys,
                    "argv",
                    [
                        "run_metrics.py",
                        "--rollout-file",
                        str(resolved.rollout_files[0]),
                        "--output-dir",
                        str(resolved.output_dir),
                    ],
                ):
                    output = io.StringIO()
                    with patch("sys.stdout", output):
                        exit_code = run_metrics.main()

            stdout = output.getvalue()

        self.assertEqual(exit_code, run_metrics.REQUIRES_PERMISSION_EXIT_CODE)
        self.assertIn("ccusage status: requires_permission", stdout)
        self.assertIn(CCUSAGE_PERMISSION_QUESTION, stdout)
        self.assertFalse((root / "out" / "agent_usage_metrics_report.md").exists())
        self.assertFalse((root / "out" / "agent_usage_metrics_report.json").exists())


if __name__ == "__main__":
    unittest.main()
