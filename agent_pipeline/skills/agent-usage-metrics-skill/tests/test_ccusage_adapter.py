"""Tests for ccusage discovery, parsing, and conservative session matching."""

from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
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

from agent_usage_metrics.ccusage_adapter import (
    load_ccusage_data,
    parse_ccusage_json,
    summarize_ccusage_match_diagnostics,
    summarize_ccusage_result,
)
from agent_usage_metrics.models import CcusageResult, ResolvedInput

import verify_ccusage


ROOT_HELP = "Usage: ccusage [command]\nCommands: daily weekly monthly session codex\n"
CODEX_HELP = "Usage: ccusage codex [command]\nCommands: daily weekly monthly session\n"
CODEX_HELP_NO_SESSION = "Usage: ccusage codex [command]\nCommands: daily weekly monthly\n"
SESSION_HELP = "Usage: ccusage session [options]\nOptions: --all --json --offline\n"


def make_resolved_input(
    *,
    scope_type: str = "session",
    date_range: tuple[str, str] | None = ("2026-06-30", "2026-06-30"),
    rollout_file: Path | None = None,
    rollout_files: list[Path] | None = None,
    workspace: Path | None = None,
    thread_title: str | None = None,
) -> ResolvedInput:
    return ResolvedInput(
        agent="codex",
        scope_type=scope_type,
        rollout_files=list(rollout_files or [rollout_file or Path("rollout-test.jsonl")]),
        codex_home=Path(".codex"),
        logs_db=None,
        state_db=None,
        workspace=workspace,
        thread_title=thread_title,
        date_range=date_range,
        output_dir=Path("out"),
        warnings=[],
    )


def make_rollout(root: Path, lines: list[dict[str, object]] | None = None, name: str = "rollout-test.jsonl") -> Path:
    rollout = root / ".codex" / "sessions" / "2026" / "06" / "30" / name
    rollout.parent.mkdir(parents=True)
    rollout.write_text(
        "\n".join(json.dumps(line) for line in (lines or [])) + "\n",
        encoding="utf-8",
    )
    return rollout


def which_from(mapping: dict[str, str | None]):
    def fake_which(name: str) -> str | None:
        return mapping.get(name)

    return fake_which


def completed(stdout: object, returncode: int = 0, stderr: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(
        args=["ccusage"],
        returncode=returncode,
        stdout=json.dumps(stdout) if not isinstance(stdout, str) else stdout,
        stderr=stderr,
    )


def command_shape(command: list[str]) -> str:
    return " ".join(command)


def runner_for(responses: dict[str, subprocess.CompletedProcess[str]]) -> Mock:
    def fake_run(command: list[str], **_: object) -> subprocess.CompletedProcess[str]:
        shape = command_shape(command)
        if shape not in responses:
            raise AssertionError(f"unexpected command: {shape}")
        return responses[shape]

    return Mock(side_effect=fake_run)


def discovery_responses(prefix: str, actual_args: str, actual_stdout: object) -> dict[str, subprocess.CompletedProcess[str]]:
    return {
        f"{prefix} --help": completed(ROOT_HELP),
        f"{prefix} codex --help": completed(CODEX_HELP),
        f"{prefix} session --help": completed(SESSION_HELP),
        f"{prefix} {actual_args}": completed(actual_stdout),
    }


class CcusageAdapterTests(unittest.TestCase):
    def test_global_ccusage_available_returns_direct_daily_command_path(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "ccusage",
                "codex daily --json --offline",
                {"inputTokens": 10, "totalTokens": 20},
            )
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(scope_type="daily"))

        self.assertEqual(result.status, "available")
        self.assertEqual(result.command, ["ccusage", "codex", "daily", "--json", "--offline"])
        self.assertEqual(result.precision, "day_level")
        self.assertEqual(result.input_tokens, 10)
        self.assertEqual(result.total_tokens, 20)
        self.assertIn(["ccusage", "--help"], result.command_attempts)

    def test_session_scope_attempts_session_level_before_daily_mode(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "ccusage",
                "codex session --json --offline",
                {
                    "sessions": [
                        {
                            "sessionId": "rollout-test",
                            "inputTokens": 100,
                            "outputTokens": 25,
                            "totalCost": 0.12,
                        }
                    ]
                },
            )
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input())

        shapes = [command_shape(call.args[0]) for call in run_mock.call_args_list]
        self.assertIn("ccusage codex session --json --offline", shapes)
        self.assertNotIn("ccusage codex daily --json --offline", shapes)
        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.input_tokens, 100)
        self.assertEqual(result.estimated_cost, 0.12)

    def test_bunx_available_without_download_permission_requires_permission(self) -> None:
        run_mock = Mock()

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"bunx": "bunx"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(), allow_download=False)

        self.assertEqual(result.status, "requires_permission")
        self.assertEqual(result.reason, "permission_required")
        self.assertEqual(result.command, ["bunx", "ccusage", "codex", "session", "--json", "--offline"])
        self.assertIn("ccusage may need to be downloaded or cached", " ".join(result.warnings))
        run_mock.assert_not_called()

    def test_bunx_available_with_download_permission_builds_bunx_command(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "bunx ccusage",
                "codex daily --json --offline",
                {"output_tokens": 33},
            )
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"bunx": "bunx"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(scope_type="daily"), allow_download=True)

        self.assertEqual(result.status, "available_via_bunx")
        self.assertEqual(result.command, ["bunx", "ccusage", "codex", "daily", "--json", "--offline"])
        self.assertEqual(result.output_tokens, 33)

    def test_allow_download_still_prefers_installed_ccusage(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "ccusage",
                "codex daily --json --offline",
                {"inputTokens": 8},
            )
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage", "bunx": "bunx"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(scope_type="daily"), allow_download=True)

        self.assertEqual(result.status, "available")
        self.assertEqual(result.command, ["ccusage", "codex", "daily", "--json", "--offline"])
        self.assertEqual(result.input_tokens, 8)

    def test_npx_fallback_works_when_bunx_is_missing(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "npx ccusage@latest",
                "codex daily --json --offline",
                {"totalCost": 0.12},
            )
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"npx": "npx"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(scope_type="daily"), allow_download=True)

        self.assertEqual(result.status, "available_via_npx")
        self.assertEqual(result.command, ["npx", "ccusage@latest", "codex", "daily", "--json", "--offline"])
        self.assertEqual(result.estimated_cost, 0.12)

    def test_pnpm_fallback_works_when_bunx_and_npx_are_missing(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "pnpm dlx ccusage",
                "codex daily --json --offline",
                {"cachedInputTokens": 7},
            )
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"pnpm": "pnpm"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(scope_type="daily"), allow_download=True)

        self.assertEqual(result.status, "available_via_pnpm")
        self.assertEqual(result.command, ["pnpm", "dlx", "ccusage", "codex", "daily", "--json", "--offline"])
        self.assertEqual(result.cached_input_tokens, 7)

    def test_no_runtime_returns_node_runtime_missing_with_specific_reason(self) -> None:
        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({})):
            result = load_ccusage_data(make_resolved_input())

        self.assertEqual(result.status, "node_runtime_missing")
        self.assertEqual(result.reason, "ccusage_unavailable")
        self.assertEqual(result.precision, "unavailable")
        self.assertIn("No ccusage runtime found", " ".join(result.warnings))

    def test_invalid_json_returns_parser_failure_reason(self) -> None:
        run_mock = runner_for(
            {
                "ccusage --help": completed(ROOT_HELP),
                "ccusage codex --help": completed(CODEX_HELP),
                "ccusage session --help": completed(SESSION_HELP),
                "ccusage codex session --json --offline": completed("not-json"),
                "ccusage session --all --json --offline": completed("still-not-json"),
            }
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input())

        self.assertEqual(result.status, "invalid_json")
        self.assertEqual(result.reason, "parser_unsupported_output_shape")
        self.assertIn("ccusage did not return valid JSON", result.errors)

    def test_unsupported_codex_session_falls_back_to_unified_session_all(self) -> None:
        responses = {
            "ccusage --help": completed(ROOT_HELP),
            "ccusage codex --help": completed(CODEX_HELP),
            "ccusage session --help": completed(SESSION_HELP),
            "ccusage codex session --json --offline": completed({}, returncode=1, stderr="unknown command session"),
            "ccusage session --all --json --offline": completed(
                {
                    "sessions": [
                        {
                            "sessionId": "rollout-test",
                            "inputTokens": 11,
                            "outputTokens": 5,
                            "totalCost": 0.04,
                        }
                    ]
                }
            ),
        }
        run_mock = runner_for(responses)

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input())

        self.assertEqual(result.command, ["ccusage", "session", "--all", "--json", "--offline"])
        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.input_tokens, 11)

    def test_exact_session_match_populates_token_and_cost_metrics(self) -> None:
        result = parse_ccusage_json(
            {
                "sessions": [
                    {
                        "sessionId": "rollout-test",
                        "inputTokens": 100,
                        "outputTokens": 50,
                        "totalCost": 0.42,
                    }
                ]
            },
            make_resolved_input(),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.input_tokens, 100)
        self.assertEqual(result.output_tokens, 50)
        self.assertEqual(result.estimated_cost, 0.42)
        self.assertEqual(result.session_match["confidence"], "exact")

    def test_codex_session_cost_usd_populates_estimated_cost(self) -> None:
        result = parse_ccusage_json(
            {
                "sessions": [
                    {
                        "sessionId": "rollout-test",
                        "inputTokens": 100,
                        "outputTokens": 50,
                        "costUSD": 0.42,
                        "models": {
                            "gpt-5.5": {
                                "inputTokens": 100,
                                "outputTokens": 50,
                            }
                        },
                    }
                ]
            },
            make_resolved_input(),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.input_tokens, 100)
        self.assertEqual(result.output_tokens, 50)
        self.assertEqual(result.estimated_cost, 0.42)
        self.assertIsNone(result.reason)

    def test_total_cost_usd_alias_populates_estimated_cost(self) -> None:
        result = parse_ccusage_json(
            {
                "sessions": [
                    {
                        "sessionId": "rollout-test",
                        "inputTokens": 100,
                        "outputTokens": 50,
                        "totalCostUSD": 0.55,
                    }
                ]
            },
            make_resolved_input(),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.estimated_cost, 0.55)

    def test_null_codex_cost_usd_keeps_estimated_cost_missing(self) -> None:
        result = parse_ccusage_json(
            {
                "sessions": [
                    {
                        "sessionId": "rollout-test",
                        "inputTokens": 100,
                        "outputTokens": 50,
                        "costUSD": None,
                    }
                ]
            },
            make_resolved_input(),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.input_tokens, 100)
        self.assertEqual(result.output_tokens, 50)
        self.assertIsNone(result.estimated_cost)
        self.assertEqual(result.reason, "estimated_cost_not_provided")
        self.assertIn("estimated_cost", " ".join(result.warnings))

    def test_path_like_ccusage_session_id_exact_matches_rollout_stem(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rollout = make_rollout(
                Path(tmp),
                [{"timestamp": "2026-07-13T13:31:45Z"}],
                name="rollout-2026-07-13T09-31-38-019f5bad-0326-7f83-8b4f-ebd9b1b18b11.jsonl",
            )
            result = parse_ccusage_json(
                {
                    "sessions": [
                        {
                            "sessionId": "2026/07/13/rollout-2026-07-13t09-31-38-019f5bad-0326-7f83-8b4f-ebd9b1b18b11",
                            "date": "2026-07-13",
                            "inputTokens": 158304,
                            "outputTokens": 24984,
                        }
                    ]
                },
                make_resolved_input(rollout_file=rollout),
                ["ccusage", "codex", "session", "--json", "--offline"],
            )

        self.assertEqual(result.status, "available")
        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.session_match["confidence"], "exact")
        self.assertEqual(result.input_tokens, 158304)
        self.assertEqual(result.output_tokens, 24984)
        self.assertIsNone(result.estimated_cost)
        self.assertEqual(result.reason, "estimated_cost_not_provided")
        self.assertIn("estimated_cost", " ".join(result.warnings))

    def test_rollout_id_matching_is_case_insensitive(self) -> None:
        result = parse_ccusage_json(
            {"sessions": [{"sessionId": "2026/07/13/rollout-alpha", "inputTokens": 10}]},
            make_resolved_input(rollout_file=Path("ROLLOUT-ALPHA.jsonl")),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.session_match["confidence"], "exact")
        self.assertEqual(result.input_tokens, 10)

    def test_jsonl_extension_difference_does_not_prevent_exact_match(self) -> None:
        result = parse_ccusage_json(
            {"sessions": [{"sessionId": "2026/07/13/rollout-alpha.jsonl", "inputTokens": 12}]},
            make_resolved_input(rollout_file=Path("rollout-alpha.jsonl")),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.session_match["confidence"], "exact")
        self.assertEqual(result.input_tokens, 12)

    def test_path_like_bare_uuid_is_not_promoted_to_exact_alias(self) -> None:
        uuid = "019f5bad-0326-7f83-8b4f-ebd9b1b18b11"
        with tempfile.TemporaryDirectory() as tmp:
            rollout = make_rollout(
                Path(tmp),
                [{"timestamp": "2026-07-13T13:31:45Z"}],
                name=f"rollout-2026-07-13T09-31-38-{uuid}.jsonl",
            )
            result = parse_ccusage_json(
                {
                    "sessions": [
                        {
                            "sessionId": f"2026/07/13/{uuid}",
                            "date": "2026-07-13",
                            "inputTokens": 99,
                        }
                    ]
                },
                make_resolved_input(rollout_file=rollout),
                ["ccusage", "codex", "session", "--json", "--offline"],
            )

        self.assertEqual(result.status, "no_confident_match")
        self.assertEqual(result.reason, "weak_session_match")
        self.assertIsNone(result.input_tokens)
        self.assertEqual(result.session_match["confidence"], "weakest")

    def test_thread_and_parent_ids_do_not_cause_false_exact_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rollout = make_rollout(
                Path(tmp),
                [
                    {
                        "timestamp": "2026-07-13T13:31:45Z",
                        "threadId": "msg_parent_thread",
                        "parentThreadId": "019f5bad-0326-7f83-8b4f-ebd9b1b18b11",
                    }
                ],
                name="rollout-2026-07-13T09-31-38-019f5bad-0326-7f83-8b4f-ebd9b1b18b11.jsonl",
            )
            result = parse_ccusage_json(
                {
                    "sessions": [
                        {
                            "sessionId": "msg_parent_thread",
                            "date": "2026-07-13",
                            "inputTokens": 99,
                        }
                    ]
                },
                make_resolved_input(rollout_file=rollout),
                ["ccusage", "codex", "session", "--json", "--offline"],
            )

        self.assertEqual(result.status, "no_confident_match")
        self.assertNotEqual(result.session_match.get("confidence"), "exact")
        self.assertIsNone(result.input_tokens)

    def test_strong_workspace_and_time_match_populates_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(
                root,
                [
                    {
                        "timestamp": "2026-06-30T12:00:00Z",
                        "workspace": str(root / "workspace"),
                    }
                ],
            )
            resolved = make_resolved_input(rollout_file=rollout, workspace=root / "workspace")
            result = parse_ccusage_json(
                {
                    "sessions": [
                        {
                            "workspace": str(root / "workspace"),
                            "firstActivity": "2026-06-30T11:59:59Z",
                            "lastActivity": "2026-06-30T12:01:00Z",
                            "inputTokens": 90,
                            "outputTokens": 30,
                            "totalCost": 0.2,
                        }
                    ]
                },
                resolved,
                ["ccusage", "codex", "session", "--json", "--offline"],
            )

        self.assertEqual(result.precision, "exact_session")
        self.assertEqual(result.session_match["confidence"], "strong")
        self.assertEqual(result.input_tokens, 90)

    def test_same_day_only_ties_remain_ambiguous(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rollout = make_rollout(Path(tmp), [{"timestamp": "2026-07-13T13:31:45Z"}])
            result = parse_ccusage_json(
                {
                    "sessions": [
                        {"sessionId": "unrelated-a", "date": "2026-07-13", "inputTokens": 1},
                        {"sessionId": "unrelated-b", "date": "2026-07-13", "inputTokens": 2},
                    ]
                },
                make_resolved_input(rollout_file=rollout),
                ["ccusage", "codex", "session", "--json", "--offline"],
            )

        self.assertEqual(result.status, "ambiguous_match")
        self.assertEqual(result.reason, "multiple_ambiguous_session_matches")
        self.assertEqual(result.session_match["candidate_confidences"], ["weakest"])
        self.assertIsNone(result.input_tokens)

    def test_weak_session_match_does_not_populate_exact_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root, [{"timestamp": "2026-06-30T12:00:00Z"}])
            result = parse_ccusage_json(
                {
                    "sessions": [
                        {
                            "firstActivity": "2026-06-30T11:59:59Z",
                            "lastActivity": "2026-06-30T12:01:00Z",
                            "inputTokens": 90,
                            "outputTokens": 30,
                            "totalCost": 0.2,
                        }
                    ]
                },
                make_resolved_input(rollout_file=rollout),
                ["ccusage", "codex", "session", "--json", "--offline"],
            )

        self.assertEqual(result.status, "no_confident_match")
        self.assertEqual(result.reason, "weak_session_match")
        self.assertEqual(result.precision, "no_confident_match")
        self.assertIsNone(result.input_tokens)
        self.assertIn("Best ccusage session match was weak", " ".join(result.warnings))

    def test_multiple_ambiguous_session_matches_do_not_populate_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(
                root,
                [
                    {
                        "timestamp": "2026-06-30T12:00:00Z",
                        "workspace": str(root / "workspace"),
                    }
                ],
            )
            resolved = make_resolved_input(rollout_file=rollout, workspace=root / "workspace")
            result = parse_ccusage_json(
                {
                    "sessions": [
                        {
                            "workspace": str(root / "workspace"),
                            "firstActivity": "2026-06-30T12:00:00Z",
                            "inputTokens": 1,
                        },
                        {
                            "workspace": str(root / "workspace"),
                            "firstActivity": "2026-06-30T12:00:01Z",
                            "inputTokens": 2,
                        },
                    ]
                },
                resolved,
                ["ccusage", "codex", "session", "--json", "--offline"],
            )

        self.assertEqual(result.status, "ambiguous_match")
        self.assertEqual(result.reason, "multiple_ambiguous_session_matches")
        self.assertIsNone(result.input_tokens)
        self.assertIn("Multiple ccusage session rows matched", " ".join(result.warnings))
        plain_summary = summarize_ccusage_result(result)
        diagnostic_summary = summarize_ccusage_match_diagnostics(result)
        self.assertNotIn("diagnostics", plain_summary["session_match"])
        diagnostics = diagnostic_summary["match_diagnostics"]
        self.assertEqual(diagnostics["decision"]["top_row_indexes"], [0, 1])
        self.assertEqual(diagnostics["candidate_matches"][0]["confidence"], "strong")
        self.assertEqual(diagnostics["ccusage_rows_considered"][0]["usage"]["input_tokens"], 1)
        self.assertNotIn(Path.home().name, " ".join(diagnostics["target"]["workspace_labels"]))

    def test_no_confident_session_match_leaves_metrics_missing_with_actionable_reason(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rollout = make_rollout(Path(tmp), [{"timestamp": "2026-06-30T12:00:00Z"}])
            result = parse_ccusage_json(
                {
                    "sessions": [
                        {
                            "sessionId": "different-session",
                            "firstActivity": "2026-07-01T12:00:00Z",
                            "inputTokens": 90,
                        }
                    ]
                },
                make_resolved_input(rollout_file=rollout),
                ["ccusage", "codex", "session", "--json", "--offline"],
            )

        self.assertEqual(result.status, "no_confident_match")
        self.assertEqual(result.reason, "no_confident_session_match")
        self.assertIsNone(result.input_tokens)
        self.assertIn("No ccusage session row confidently matched", " ".join(result.warnings))

    def test_sample_json_parses_token_and_cost_fields(self) -> None:
        data = {
            "daily": [{"date": "2026-06-30"}],
            "summary": {
                "input_tokens": 100,
                "cachedInputTokens": 25,
                "outputTokens": 50,
                "reasoning_output_tokens": 5,
                "totalTokens": 180,
                "estimatedCost": 0.42,
                "currency": "USD",
                "models": {
                    "claude-sonnet": {
                        "inputTokens": 100,
                        "outputTokens": 50,
                    }
                },
            },
        }

        result = parse_ccusage_json(data, make_resolved_input(scope_type="daily"), ["ccusage"])

        self.assertEqual(result.input_tokens, 100)
        self.assertEqual(result.cached_input_tokens, 25)
        self.assertEqual(result.output_tokens, 50)
        self.assertEqual(result.reasoning_output_tokens, 5)
        self.assertEqual(result.total_tokens, 180)
        self.assertEqual(result.estimated_cost, 0.42)
        self.assertEqual(result.currency, "USD")
        self.assertEqual(result.model_breakdown["claude-sonnet"]["inputTokens"], 100)
        self.assertIn("2026-06-30", result.scope_returned["dates"])

    def test_current_ccusage_totals_json_parses_token_and_cost_fields(self) -> None:
        data = {
            "daily": [
                {
                    "date": "2026-06-30",
                    "inputTokens": 1,
                    "outputTokens": 2,
                    "totalCost": 0.01,
                }
            ],
            "totals": {
                "inputTokens": 100,
                "outputTokens": 50,
                "cacheReadTokens": 25,
                "totalTokens": 175,
                "totalCost": 0.42,
                "modelBreakdowns": {
                    "gpt-5.2-codex": {
                        "inputTokens": 100,
                        "outputTokens": 50,
                    }
                },
            },
        }

        result = parse_ccusage_json(data, make_resolved_input(scope_type="daily"), ["ccusage", "codex", "daily"])

        self.assertEqual(result.input_tokens, 100)
        self.assertEqual(result.output_tokens, 50)
        self.assertEqual(result.cached_input_tokens, 25)
        self.assertEqual(result.total_tokens, 175)
        self.assertEqual(result.estimated_cost, 0.42)
        self.assertEqual(result.model_breakdown["gpt-5.2-codex"]["outputTokens"], 50)

    def test_session_daily_output_is_not_used_as_exact_metrics(self) -> None:
        result = parse_ccusage_json(
            {"totals": {"inputTokens": 100, "outputTokens": 50, "totalCost": 0.42}},
            make_resolved_input(),
            ["ccusage", "codex", "daily", "--json", "--offline"],
        )

        self.assertEqual(result.status, "only_day_level_available")
        self.assertEqual(result.precision, "day_level")
        self.assertEqual(result.reason, "only_day_level_output_available")
        self.assertIsNone(result.input_tokens)
        self.assertIsNone(result.output_tokens)
        self.assertIsNone(result.estimated_cost)
        self.assertIn("cannot be safely attributed", " ".join(result.warnings))

    def test_conversation_scope_aggregates_confident_session_ccusage_matches(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "ccusage",
                "codex session --json --offline",
                {
                    "sessions": [
                        {"sessionId": "rollout-alpha", "inputTokens": 10, "outputTokens": 3, "costUSD": 0.01},
                        {"sessionId": "rollout-beta", "inputTokens": 20, "outputTokens": 7, "costUSD": 0.03},
                    ]
                },
            )
        )
        resolved = make_resolved_input(
            scope_type="conversation",
            rollout_files=[Path("rollout-alpha.jsonl"), Path("rollout-beta.jsonl")],
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(resolved)

        shapes = [command_shape(call.args[0]) for call in run_mock.call_args_list]
        self.assertIn("ccusage codex session --json --offline", shapes)
        self.assertNotIn("ccusage codex daily --json --offline", shapes)
        self.assertEqual(result.status, "success")
        self.assertEqual(result.precision, "exact_conversation")
        self.assertEqual(result.input_tokens, 30)
        self.assertEqual(result.output_tokens, 10)
        self.assertEqual(result.estimated_cost, 0.04)
        self.assertEqual(result.session_match["matched_session_count"], 2)

    def test_workspace_scope_aggregates_confident_session_ccusage_matches(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "ccusage",
                "codex session --json --offline",
                {
                    "sessions": [
                        {"sessionId": "rollout-alpha", "inputTokens": 4, "outputTokens": 1, "costUSD": 0.01},
                        {"sessionId": "rollout-beta", "inputTokens": 6, "outputTokens": 2, "costUSD": 0.02},
                    ]
                },
            )
        )
        resolved = make_resolved_input(
            scope_type="workspace",
            rollout_files=[Path("rollout-alpha.jsonl"), Path("rollout-beta.jsonl")],
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(resolved)

        self.assertEqual(result.command, ["ccusage", "codex", "session", "--json", "--offline"])
        self.assertEqual(result.status, "success")
        self.assertEqual(result.precision, "exact_workspace")
        self.assertEqual(result.input_tokens, 10)
        self.assertEqual(result.output_tokens, 3)
        self.assertEqual(result.estimated_cost, 0.03)

    def test_partial_conversation_ccusage_is_marked_partial(self) -> None:
        result = parse_ccusage_json(
            {
                "sessions": [
                    {"sessionId": "rollout-alpha", "inputTokens": 10, "outputTokens": 2, "totalCost": 0.01},
                ]
            },
            make_resolved_input(
                scope_type="conversation",
                rollout_files=[Path("rollout-alpha.jsonl"), Path("rollout-beta.jsonl")],
            ),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        self.assertEqual(result.status, "partial")
        self.assertEqual(result.precision, "partial_conversation")
        self.assertEqual(result.reason, "partial_session_matches")
        self.assertEqual(result.input_tokens, 10)
        self.assertEqual(result.session_match["matched_session_count"], 1)
        self.assertIn("ccusage matched 1 of 2 conversation sessions", " ".join(result.warnings))

    def test_no_confident_conversation_ccusage_matches_leaves_metrics_missing(self) -> None:
        result = parse_ccusage_json(
            {
                "sessions": [
                    {"sessionId": "different-session", "inputTokens": 10, "outputTokens": 2, "totalCost": 0.01},
                ]
            },
            make_resolved_input(
                scope_type="conversation",
                rollout_files=[Path("rollout-alpha.jsonl"), Path("rollout-beta.jsonl")],
            ),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        self.assertEqual(result.status, "no_confident_match")
        self.assertEqual(result.reason, "no_confident_session_matches")
        self.assertEqual(result.precision, "no_confident_match")
        self.assertIsNone(result.input_tokens)
        self.assertEqual(result.session_match["matched_session_count"], 0)

    def test_ambiguous_conversation_session_match_is_not_attributed(self) -> None:
        result = parse_ccusage_json(
            {
                "sessions": [
                    {"sessionId": "rollout-alpha", "inputTokens": 10},
                    {"sessionId": "rollout-alpha", "inputTokens": 20},
                    {"sessionId": "rollout-beta", "inputTokens": 30},
                ]
            },
            make_resolved_input(
                scope_type="conversation",
                rollout_files=[Path("rollout-alpha.jsonl"), Path("rollout-beta.jsonl")],
            ),
            ["ccusage", "codex", "session", "--json", "--offline"],
        )

        details = {detail["rollout_file"]: detail for detail in result.session_match["sessions"]}
        self.assertEqual(result.status, "partial")
        self.assertEqual(result.input_tokens, 30)
        self.assertEqual(details["rollout-alpha.jsonl"]["status"], "ambiguous_match")
        self.assertIsNone(details["rollout-alpha.jsonl"]["input_tokens"])
        self.assertIn("Multiple ccusage session rows matched", " ".join(result.warnings))

    def test_conversation_daily_output_is_not_used_as_exact_metrics(self) -> None:
        result = parse_ccusage_json(
            {"totals": {"inputTokens": 100, "outputTokens": 50, "totalCost": 0.42}},
            make_resolved_input(scope_type="conversation", rollout_files=[Path("rollout-alpha.jsonl")]),
            ["ccusage", "codex", "daily", "--json", "--offline"],
        )

        self.assertEqual(result.status, "only_day_level_available")
        self.assertEqual(result.precision, "day_level")
        self.assertEqual(result.reason, "only_day_level_output_available")
        self.assertIsNone(result.input_tokens)
        self.assertIsNone(result.output_tokens)
        self.assertIsNone(result.estimated_cost)
        self.assertIn("cannot be safely attributed", " ".join(result.warnings))

    def test_weekly_scope_invokes_weekly_ccusage_mode(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "ccusage",
                "codex weekly --json --offline",
                {"totals": {"inputTokens": 100}},
            )
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(scope_type="weekly", date_range=None))

        self.assertEqual(result.command, ["ccusage", "codex", "weekly", "--json", "--offline"])
        self.assertEqual(result.precision, "week_level")
        self.assertEqual(result.input_tokens, 100)

    def test_monthly_scope_invokes_monthly_ccusage_mode(self) -> None:
        run_mock = runner_for(
            discovery_responses(
                "ccusage",
                "codex monthly --json --offline",
                {"totals": {"outputTokens": 44}},
            )
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(scope_type="monthly", date_range=None))

        self.assertEqual(result.command, ["ccusage", "codex", "monthly", "--json", "--offline"])
        self.assertEqual(result.precision, "month_level")
        self.assertEqual(result.output_tokens, 44)

    def test_command_failure_includes_sanitized_mode_exit_stderr_and_command_shape(self) -> None:
        home_path = str(Path.home())
        run_mock = runner_for(
            {
                "npx ccusage@latest --help": completed(ROOT_HELP),
                "npx ccusage@latest codex --help": completed(CODEX_HELP),
                "npx ccusage@latest session --help": completed(SESSION_HELP),
                "npx ccusage@latest codex session --json --offline": completed(
                    {},
                    returncode=1,
                    stderr=f"npm error code EPERM\nnpm error path {home_path}\\AppData\\Local\\npm-cache",
                ),
                "npx ccusage@latest session --all --json --offline": completed(
                    {},
                    returncode=1,
                    stderr=f"npm error code EPERM\nnpm error path {home_path}\\AppData\\Local\\npm-cache",
                ),
            }
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"npx": "npx"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input(), allow_download=True)

        warnings = " ".join(result.warnings)
        self.assertEqual(result.status, "failed")
        self.assertEqual(result.reason, "command_failed")
        self.assertIn("ccusage mode attempted: session", warnings)
        self.assertIn("ccusage attempted command shape: npx ccusage@latest codex session --json --offline", warnings)
        self.assertIn("ccusage exit code: 1", warnings)
        self.assertIn("ccusage stderr summary: npm error code EPERM", warnings)
        self.assertNotIn(home_path, warnings)
        self.assertIn("ccusage exited with code 1", result.errors)

    def test_unsupported_command_returns_specific_reason(self) -> None:
        run_mock = runner_for(
            {
                "ccusage --help": completed("Usage: ccusage\nCommands: daily\n"),
                "ccusage codex --help": completed("Usage: ccusage codex\nCommands: daily\n"),
                "ccusage session --help": completed({}, returncode=1, stderr="unknown command session"),
            }
        )

        with patch("agent_usage_metrics.ccusage_adapter.shutil.which", side_effect=which_from({"ccusage": "ccusage"})):
            with patch("agent_usage_metrics.ccusage_adapter.subprocess.run", run_mock):
                result = load_ccusage_data(make_resolved_input())

        self.assertEqual(result.status, "only_day_level_available")
        self.assertEqual(result.reason, "only_day_level_output_available")
        self.assertEqual(result.precision, "day_level")

    def test_cli_does_not_print_raw_full_output(self) -> None:
        parsed_result = parse_ccusage_json(
            {
                "totalTokens": 1,
                "privateRawOutput": "do not print this raw value",
            },
            make_resolved_input(scope_type="daily"),
            ["ccusage"],
        )

        with patch("verify_ccusage.resolve_input", return_value=make_resolved_input(scope_type="daily")):
            with patch("verify_ccusage.load_ccusage_data", return_value=parsed_result):
                with patch.object(sys, "argv", ["verify_ccusage.py", "--rollout-file", "fake.jsonl"]):
                    output = io.StringIO()
                    with patch("sys.stdout", output):
                        exit_code = verify_ccusage.main()

        self.assertEqual(exit_code, 0)
        self.assertIn('"total_tokens": 1', output.getvalue())
        self.assertNotIn("do not print this raw value", output.getvalue())

    def test_summary_is_safe_and_structured(self) -> None:
        result = CcusageResult(
            status="available",
            command=["ccusage", "codex", "session", "--json", "--offline"],
            scope_requested={"scope_type": "session"},
            scope_returned={"mode": "session"},
            input_tokens=1,
            cached_input_tokens=None,
            output_tokens=2,
            reasoning_output_tokens=None,
            total_tokens=3,
            estimated_cost=0.01,
            currency="USD",
            model_breakdown={"model": {"totalTokens": 3}},
            raw_summary={"top_level_keys": ["summary"], "record_count": 1},
            warnings=[],
            errors=[],
            precision="exact_session",
            reason=None,
            mode_attempted="session",
            command_attempts=[["ccusage", "codex", "session", "--json", "--offline"]],
            session_match={"confidence": "exact"},
        )

        summary = summarize_ccusage_result(result)

        self.assertEqual(summary["status"], "available")
        self.assertEqual(summary["precision"], "exact_session")
        self.assertEqual(summary["mode_attempted"], "session")
        self.assertEqual(summary["total_tokens"], 3)
        self.assertNotIn("raw_output", summary)


if __name__ == "__main__":
    unittest.main()
