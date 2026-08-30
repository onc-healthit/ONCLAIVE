"""Tests for exact, ambiguous, and multi-session report target resolution."""

from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from agent_usage_metrics.input_resolver import (
    AmbiguousSessionsError,
    InputResolverError,
    NeedsClarificationError,
    NoMatchingSessionsError,
    parse_usage_query,
    resolve_input,
)
from agent_usage_metrics.models import ResolvedInput, UsageQuery


def make_rollout(root: Path) -> Path:
    rollout = root / ".codex" / "sessions" / "2026" / "06" / "29" / "rollout-test.jsonl"
    rollout.parent.mkdir(parents=True)
    rollout.write_text("", encoding="utf-8")
    return rollout


def make_session(
    root: Path,
    session_date: str,
    name: str,
    *,
    metadata: dict[str, str] | None = None,
    events: list[dict[str, str]] | None = None,
) -> Path:
    year, month, day = session_date.split("-")
    rollout = root / ".codex" / "sessions" / year / month / day / name
    rollout.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    if metadata:
        lines.append(json.dumps({"metadata": metadata}))
    for event in events or []:
        lines.append(json.dumps(event))
    rollout.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return rollout


def make_archived_session(
    root: Path,
    name: str,
    *,
    metadata: dict[str, str] | None = None,
    events: list[dict[str, str]] | None = None,
) -> Path:
    rollout = root / ".codex" / "archived_sessions" / name
    rollout.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    if metadata:
        lines.append(json.dumps({"metadata": metadata}))
    for event in events or []:
        lines.append(json.dumps(event))
    rollout.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return rollout


def make_session_index(root: Path, rows: list[dict[str, str]]) -> Path:
    index = root / ".codex" / "session_index.jsonl"
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")
    return index


def make_state_db(root: Path, rows: list[dict[str, str]]) -> Path:
    state_db = root / ".codex" / "state_5.sqlite"
    state_db.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(state_db)
    try:
        connection.execute("CREATE TABLE threads (id TEXT, rollout_path TEXT, cwd TEXT, title TEXT, name TEXT)")
        normalized_rows = [
            {
                "id": row.get("id") or Path(row["rollout_path"]).stem.removeprefix("rollout-"),
                "rollout_path": row["rollout_path"],
                "cwd": row["cwd"],
                "title": row.get("title"),
                "name": row.get("name"),
            }
            for row in rows
        ]
        connection.executemany(
            "INSERT INTO threads (id, rollout_path, cwd, title, name) VALUES (:id, :rollout_path, :cwd, :title, :name)",
            normalized_rows,
        )
        connection.commit()
    finally:
        connection.close()
    return state_db


class InputResolverTests(unittest.TestCase):
    def test_valid_rollout_file_returns_resolved_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root)
            codex_home = root / ".codex"
            (codex_home / "logs_2.sqlite").write_text("", encoding="utf-8")
            (codex_home / "state_5.sqlite").write_text("", encoding="utf-8")

            resolved = resolve_input(rollout_file=rollout, output_dir=root / "out")

            self.assertIsInstance(resolved, ResolvedInput)
            self.assertEqual(resolved.agent, "codex")
            self.assertEqual(resolved.scope_type, "session")
            self.assertEqual(resolved.codex_home, codex_home.resolve())
            self.assertEqual(resolved.logs_db, (codex_home / "logs_2.sqlite").resolve())
            self.assertEqual(resolved.state_db, (codex_home / "state_5.sqlite").resolve())
            self.assertEqual(resolved.warnings, [])

    def test_rollout_files_is_a_list(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root)

            resolved = resolve_input(rollout_file=rollout, output_dir=root / "out")

            self.assertIsInstance(resolved.rollout_files, list)
            self.assertEqual(resolved.rollout_files, [rollout.resolve()])

    def test_direct_rollout_uses_safe_metadata_when_available(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_session(
                root,
                "2026-07-07",
                "rollout-test.jsonl",
                metadata={
                    "workspace": "ONCLAIVE 2",
                    "thread_title": "Build Inventory",
                },
            )

            resolved = resolve_input(rollout_file=rollout, output_dir=root / "out")

            self.assertEqual(resolved.workspace, Path("ONCLAIVE 2"))
            self.assertEqual(resolved.thread_title, "Build Inventory")
            self.assertEqual(resolved.date_range, ("2026-07-07", "2026-07-07"))

    def test_direct_rollout_uses_safe_metadata_from_nested_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_session(
                root,
                "2026-07-07",
                "rollout-test.jsonl",
                events=[
                    {
                        "type": "session_meta",
                        "payload": {
                            "cwd": str(root / "ONCLAIVE 2"),
                            "thread_title": "Build Inventory",
                        },
                    }
                ],
            )

            resolved = resolve_input(rollout_file=rollout, output_dir=root / "out")

            self.assertEqual(resolved.workspace, Path("ONCLAIVE 2"))
            self.assertEqual(resolved.thread_title, "Build Inventory")

    def test_missing_rollout_file_raises_clear_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            missing = root / "missing.jsonl"

            with self.assertRaisesRegex(FileNotFoundError, "Rollout file does not exist"):
                resolve_input(rollout_file=missing, output_dir=root / "out")

    def test_non_jsonl_rollout_file_raises_clear_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            not_jsonl = root / "rollout.txt"
            not_jsonl.write_text("", encoding="utf-8")

            with self.assertRaisesRegex(InputResolverError, "must have a .jsonl extension"):
                resolve_input(rollout_file=not_jsonl, output_dir=root / "out")

    def test_missing_sqlite_files_produce_warnings_not_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root)

            resolved = resolve_input(rollout_file=rollout, output_dir=root / "out")

            self.assertIsNone(resolved.logs_db)
            self.assertIsNone(resolved.state_db)
            self.assertIn("logs_2.sqlite not found under codex_home", resolved.warnings)
            self.assertIn("state_5.sqlite not found under codex_home", resolved.warnings)

    def test_output_dir_is_created_if_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root)
            output_dir = root / "new-output-dir"

            self.assertFalse(output_dir.exists())
            resolved = resolve_input(rollout_file=rollout, output_dir=output_dir)

            self.assertTrue(output_dir.exists())
            self.assertTrue(output_dir.is_dir())
            self.assertEqual(resolved.output_dir, output_dir.resolve())

    def test_query_parser_detects_latest_workspace_and_codex_agent(self) -> None:
        parsed = parse_usage_query("latest ONCLAIVE Codex run")

        self.assertIsInstance(parsed, UsageQuery)
        self.assertEqual(parsed.agent, "codex")
        self.assertEqual(parsed.selection_mode, "latest")
        self.assertEqual(parsed.workspace_query, "ONCLAIVE")

    def test_query_parser_detects_dates(self) -> None:
        june_date = parse_usage_query("Codex run from June 25", today=date(2026, 6, 30))
        iso_date = parse_usage_query("Codex run from 2026-06-25", today=date(2026, 6, 30))
        yesterday = parse_usage_query("yesterday's Codex run", today=date(2026, 6, 30))

        self.assertEqual(june_date.date_range, ("2026-06-25", "2026-06-25"))
        self.assertEqual(iso_date.date_range, ("2026-06-25", "2026-06-25"))
        self.assertEqual(yesterday.date_range, ("2026-06-29", "2026-06-29"))

    def test_query_with_direct_rollout_path_uses_fallback_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_rollout(root)

            resolved = resolve_input(
                query=f'Use rollout file "{rollout}"',
                output_dir=root / "out",
            )

            self.assertEqual(resolved.rollout_files, [rollout.resolve()])
            self.assertEqual(resolved.scope_type, "session")

    def test_no_matching_sessions_raises_clear_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            make_session(
                root,
                "2026-06-25",
                "rollout-other.jsonl",
                metadata={"workspace": "OTHER"},
            )

            with self.assertRaisesRegex(NoMatchingSessionsError, "No Codex targets matched"):
                resolve_input(
                    query="ONCLAIVE Codex run",
                    codex_home=codex_home,
                    output_dir=root / "out",
                )

    def test_multiple_matches_without_latest_raises_ambiguity_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            make_session(root, "2026-06-25", "rollout-a.jsonl", metadata={"workspace": "ONCLAIVE"})
            make_session(root, "2026-06-26", "rollout-b.jsonl", metadata={"workspace": "ONCLAIVE"})

            with self.assertRaises(AmbiguousSessionsError) as raised:
                resolve_input(
                    query="ONCLAIVE Codex run",
                    codex_home=codex_home,
                    output_dir=root / "out",
                )

            self.assertIsInstance(raised.exception, NeedsClarificationError)
            self.assertEqual(raised.exception.status, "needs_clarification")
            self.assertIn("Please choose what you want measured", str(raised.exception))
            self.assertIn("Session - one agent run", str(raised.exception))
            self.assertIn("Conversation - the whole Codex chat", str(raised.exception))
            self.assertIn("Workspace - all matching activity", str(raised.exception))
            self.assertNotIn(str(root), str(raised.exception))

    def test_latest_chooses_most_recent_matching_session(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            older = make_session(root, "2026-06-25", "rollout-a.jsonl", metadata={"workspace": "ONCLAIVE"})
            newer = make_session(root, "2026-06-26", "rollout-b.jsonl", metadata={"workspace": "ONCLAIVE"})

            resolved = resolve_input(
                query="latest ONCLAIVE Codex run",
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertNotEqual(resolved.rollout_files, [older.resolve()])
            self.assertEqual(resolved.rollout_files, [newer.resolve()])

    def test_missing_sqlite_files_produce_warnings_for_query_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            make_session(root, "2026-06-25", "rollout-a.jsonl", metadata={"workspace": "ONCLAIVE"})

            resolved = resolve_input(
                query="latest ONCLAIVE Codex run",
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertIsNone(resolved.logs_db)
            self.assertIsNone(resolved.state_db)
            self.assertIn("logs_2.sqlite not found under codex_home", resolved.warnings)
            self.assertIn("state_5.sqlite not found under codex_home", resolved.warnings)

    def test_resolver_does_not_semantically_search_raw_prompt_contents(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            make_session(
                root,
                "2026-06-25",
                "rollout-a.jsonl",
                events=[{"type": "message", "content": "ONCLAIVE appears only in raw prompt text"}],
            )

            with self.assertRaises(NoMatchingSessionsError):
                resolve_input(
                    query="ONCLAIVE Codex run",
                    codex_home=codex_home,
                    output_dir=root / "out",
                )

    def test_thread_title_filter_matches_safe_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            rollout = make_session(
                root,
                "2026-06-25",
                "rollout-a.jsonl",
                metadata={"thread_title": "Input Resolver Refactor"},
            )

            resolved = resolve_input(
                query='Codex thread "Input Resolver"',
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.rollout_files, [rollout.resolve()])
            self.assertEqual(resolved.thread_title, "Input Resolver Refactor")

    def test_quoted_title_matching_conversation_title_resolves_conversation_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            first = make_session(
                root,
                "2026-07-07",
                "rollout-a.jsonl",
                metadata={"workspace": "ONCLAIVE", "thread_title": "Build v1.1.0 inventory"},
                events=[{"timestamp": "2026-07-07T21:38:07Z"}],
            )
            second = make_session(
                root,
                "2026-07-07",
                "rollout-b.jsonl",
                metadata={"workspace": "ONCLAIVE", "thread_title": "Build v1.1.0 inventory"},
                events=[{"timestamp": "2026-07-07T21:47:59Z"}],
            )

            resolved = resolve_input(
                query='Create a report for the "Build v1.1.0 inventory" in the ONCLAIVE project.',
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "conversation")
            self.assertEqual(resolved.thread_title, "Build v1.1.0 inventory")
            self.assertEqual(resolved.rollout_files, [first.resolve(), second.resolve()])
            self.assertEqual(resolved.resolution_status, "exact")

    def test_state_thread_metadata_can_resolve_conversation_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            first = make_session(root, "2026-07-07", "rollout-a.jsonl")
            second = make_session(root, "2026-07-07", "rollout-b.jsonl")
            make_state_db(
                root,
                [
                    {
                        "rollout_path": str(first),
                        "cwd": str(root / "ONCLAIVE 2"),
                        "title": "Build v1.1.0 inventory",
                    },
                    {
                        "rollout_path": str(second),
                        "cwd": str(root / "ONCLAIVE 2"),
                        "title": "Build v1.1.0 inventory",
                    },
                ],
            )

            resolved = resolve_input(
                query='Create a report for the "Build v1.1.0 inventory" in the ONCLAIVE project.',
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "conversation")
            self.assertEqual(resolved.thread_title, "Build v1.1.0 inventory")
            self.assertEqual(resolved.rollout_files, [first.resolve(), second.resolve()])

    def test_exact_conversation_title_expands_root_thread_membership(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            root_rollout = make_session(
                root,
                "2026-07-07",
                "rollout-2026-07-07T21-22-28-root.jsonl",
                events=[
                    {
                        "type": "session_meta",
                        "payload": {
                            "id": "root-thread",
                            "cwd": str(root / "ONCLAIVE 2"),
                        },
                    }
                ],
            )
            guardian = make_session(
                root,
                "2026-07-07",
                "rollout-2026-07-07T21-24-41-guardian.jsonl",
                events=[
                    {
                        "type": "session_meta",
                        "payload": {
                            "id": "guardian-thread",
                            "parent_thread_id": "root-thread",
                            "cwd": str(root / "ONCLAIVE 2"),
                            "base_instructions": {"text": "private prompt content should not print " * 700},
                        },
                    }
                ],
            )
            archived_followup = make_archived_session(
                root,
                "rollout-2026-07-07T21-38-07-followup.jsonl",
                events=[
                    {
                        "type": "session_meta",
                        "payload": {
                            "id": "followup-thread",
                            "cwd": str(root / "ONCLAIVE 2"),
                        },
                    }
                ],
            )
            report_followup = make_session(
                root,
                "2026-07-07",
                "rollout-2026-07-07T21-47-59-report.jsonl",
                events=[
                    {
                        "type": "session_meta",
                        "payload": {
                            "id": "report-thread",
                            "cwd": str(root / "ONCLAIVE 2"),
                        },
                    }
                ],
            )
            make_session_index(
                root,
                [
                    {"id": "root-thread", "thread_name": "Build v1.1.0 inventory"},
                    {"id": "followup-thread", "thread_name": "Create v1.1.0 inventory report"},
                    {"id": "report-thread", "thread_name": "Create v1.1.0 inventory report test 1"},
                ],
            )
            make_state_db(
                root,
                [
                    {
                        "id": "root-thread",
                        "rollout_path": str(root_rollout),
                        "cwd": str(root / "ONCLAIVE 2"),
                        "title": "Build v1.1.0 inventory",
                    },
                    {
                        "id": "guardian-thread",
                        "rollout_path": str(guardian),
                        "cwd": str(root / "ONCLAIVE 2"),
                        "title": "TRANSCRIPT START user: private prompt content should not print",
                    },
                    {
                        "id": "followup-thread",
                        "rollout_path": str(archived_followup),
                        "cwd": str(root / "ONCLAIVE 2"),
                        "title": "TRANSCRIPT START user: private prompt content should not print",
                    },
                    {
                        "id": "report-thread",
                        "rollout_path": str(report_followup),
                        "cwd": str(root / "ONCLAIVE 2"),
                        "title": "Create v1.1.0 inventory report test 1",
                    },
                ],
            )

            resolved = resolve_input(
                query='Create a report for the "Build v1.1.0 inventory" in the ONCLAIVE project.',
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "conversation")
            self.assertEqual(resolved.thread_title, "Build v1.1.0 inventory")
            self.assertEqual(
                [path.name for path in resolved.rollout_files],
                [
                    root_rollout.name,
                    guardian.name,
                    report_followup.name,
                ],
            )
            self.assertIn("private prompt", str(resolved.to_dict()))

    def test_serialized_state_thread_titles_are_not_exposed_in_clarification(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            first = make_session(root, "2026-07-07", "rollout-a.jsonl")
            second = make_session(root, "2026-07-08", "rollout-b.jsonl")
            unsafe_title = '{"payload":"private prompt content should not print"}'
            make_state_db(
                root,
                [
                    {"rollout_path": str(first), "cwd": str(root / "ONCLAIVE 2"), "title": unsafe_title},
                    {"rollout_path": str(second), "cwd": str(root / "ONCLAIVE 2"), "title": unsafe_title},
                ],
            )

            with self.assertRaises(NeedsClarificationError) as raised:
                resolve_input(
                    query="Create an ONCLAIVE project report",
                    codex_home=codex_home,
                    output_dir=root / "out",
                )

            message = str(raised.exception)
            self.assertIn("rollout-a.jsonl", message)
            self.assertNotIn("private prompt", message)
            self.assertNotIn("payload", message)

    def test_same_conversation_prompt_does_not_select_different_single_rollouts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            make_session(
                root,
                "2026-07-07",
                "rollout-2026-07-07T21-38-07-019f3f60-07d8-7a53-b30e-a74e67f53be6.jsonl",
                metadata={"workspace": "ONCLAIVE", "thread_title": "Build v1.1.0 inventory"},
            )
            make_session(
                root,
                "2026-07-07",
                "rollout-2026-07-07T21-47-59-019f3f69-0136-78d2-9cd9-c3975a9c2266.jsonl",
                metadata={"workspace": "ONCLAIVE", "thread_title": "Build v1.1.0 inventory"},
            )

            first_resolution = resolve_input(
                query='Create a report for the "Build v1.1.0 inventory" in the ONCLAIVE project.',
                codex_home=codex_home,
                output_dir=root / "out-a",
            )
            second_resolution = resolve_input(
                query='Create a report for the "Build v1.1.0 inventory" in the ONCLAIVE project.',
                codex_home=codex_home,
                output_dir=root / "out-b",
            )

            self.assertEqual(first_resolution.scope_type, "conversation")
            self.assertEqual(second_resolution.scope_type, "conversation")
            self.assertEqual(first_resolution.rollout_files, second_resolution.rollout_files)
            self.assertEqual(len(first_resolution.rollout_files), 2)

    def test_ambiguous_request_includes_target_scope_explanation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            make_session(root, "2026-07-07", "rollout-a.jsonl", metadata={"workspace": "ONCLAIVE"})
            make_session(root, "2026-07-08", "rollout-b.jsonl", metadata={"workspace": "ONCLAIVE"})

            with self.assertRaises(NeedsClarificationError) as raised:
                resolve_input(
                    query="Create an ONCLAIVE project report",
                    codex_home=codex_home,
                    output_dir=root / "out",
                )

            message = str(raised.exception)
            self.assertIn("Session - one agent run", message)
            self.assertIn("Conversation - the whole Codex chat", message)
            self.assertIn("Workspace - all matching activity", message)
            self.assertIn("rollout-a.jsonl", message)
            self.assertNotIn(str(root), message)

    def test_exact_rollout_filename_resolves_to_session_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            rollout = make_session(root, "2026-07-07", "rollout-exact.jsonl", metadata={"workspace": "ONCLAIVE"})

            resolved = resolve_input(
                query='Create a report for "rollout-exact.jsonl"',
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "session")
            self.assertEqual(resolved.rollout_files, [rollout.resolve()])

    def test_exact_session_id_resolves_to_session_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            rollout = make_session(
                root,
                "2026-07-07",
                "rollout-a.jsonl",
                metadata={"workspace": "ONCLAIVE", "session_id": "session-123"},
            )

            resolved = resolve_input(
                query='Create a report for "session-123"',
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "session")
            self.assertEqual(resolved.rollout_files, [rollout.resolve()])

    def test_workspace_with_date_range_resolves_workspace_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            first = make_session(
                root,
                "2026-07-07",
                "rollout-a.jsonl",
                metadata={"workspace": "ONCLAIVE", "thread_title": "Workspace inventory review"},
            )
            second = make_session(root, "2026-07-07", "rollout-b.jsonl", metadata={"workspace": "ONCLAIVE"})
            make_session(root, "2026-07-08", "rollout-c.jsonl", metadata={"workspace": "ONCLAIVE"})

            resolved = resolve_input(
                query="Create an ONCLAIVE project report for 2026-07-07",
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "workspace")
            self.assertEqual(resolved.rollout_files, [first.resolve(), second.resolve()])
            self.assertEqual(resolved.date_range, ("2026-07-07", "2026-07-07"))
            self.assertEqual(resolved.session_titles[first.name], "Workspace inventory review")
            self.assertIsNone(resolved.session_titles[second.name])

    def test_workspace_uses_session_index_titles_for_rollout_thread_ids(self) -> None:
        """Workspace discovery uses the same indexed title lookup as conversations."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            first = make_session(
                root,
                "2026-07-07",
                "rollout-a.jsonl",
                metadata={"workspace": "Test Run 1", "thread_id": "thread-a"},
            )
            second = make_session(
                root,
                "2026-07-07",
                "rollout-b.jsonl",
                metadata={"workspace": "Test Run 1", "thread_id": "thread-b"},
            )
            make_session_index(root, [{"id": "thread-a", "thread_name": "Inventory baseline"}])

            resolved = resolve_input(
                query="Create an all-time workspace report",
                codex_home=codex_home,
                output_dir=root / "out",
                workspace="Test Run 1",
            )

            self.assertEqual(resolved.scope_type, "workspace")
            self.assertEqual(resolved.session_titles[first.name], "Inventory baseline")
            self.assertIsNone(resolved.session_titles[second.name])

    def test_workspace_request_without_date_latest_or_all_time_asks_for_clarification(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            make_session(root, "2026-07-07", "rollout-a.jsonl", metadata={"workspace": "ONCLAIVE"})

            with self.assertRaises(NeedsClarificationError) as raised:
                resolve_input(
                    query="Create an ONCLAIVE project report",
                    codex_home=codex_home,
                    output_dir=root / "out",
                )

            message = str(raised.exception)
            self.assertIn("Workspace targets need a date range, latest, or explicit all-time scope.", message)
            self.assertIn("Session - one agent run", message)
            self.assertIn("Conversation - the whole Codex chat", message)
            self.assertIn("Workspace - all matching activity", message)

    def test_workspace_all_time_resolves_all_matching_workspace_sessions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            first = make_session(root, "2026-07-07", "rollout-a.jsonl", metadata={"workspace": "ONCLAIVE"})
            second = make_session(root, "2026-07-08", "rollout-b.jsonl", metadata={"workspace": "ONCLAIVE"})
            make_session(root, "2026-07-08", "rollout-c.jsonl", metadata={"workspace": "OTHER"})

            resolved = resolve_input(
                query="Create an all-time ONCLAIVE workspace report",
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "workspace")
            self.assertEqual(resolved.rollout_files, [first.resolve(), second.resolve()])
            self.assertEqual(resolved.date_range, ("2026-07-07", "2026-07-08"))
            self.assertEqual(
                resolved.session_titles,
                {first.name: None, second.name: None},
            )

    def test_latest_workspace_report_resolves_workspace_scope_with_latest_session(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            make_session(root, "2026-07-07", "rollout-a.jsonl", metadata={"workspace": "ONCLAIVE"})
            newer = make_session(root, "2026-07-08", "rollout-b.jsonl", metadata={"workspace": "ONCLAIVE"})

            resolved = resolve_input(
                query="Create a latest ONCLAIVE workspace report",
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "workspace")
            self.assertEqual(resolved.rollout_files, [newer.resolve()])
            self.assertEqual(resolved.resolution_status, "inferred")

    def test_state_title_is_primary_and_accepts_long_values(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            rollout = make_session(
                root,
                "2026-07-07",
                "rollout-a.jsonl",
                metadata={"workspace": "ONCLAIVE", "thread_title": "Rollout fallback"},
            )
            state_title = "Codex stored title " + ("with useful detail " * 12)
            make_state_db(root, [{"rollout_path": str(rollout), "cwd": str(root / "ONCLAIVE"), "title": state_title, "name": "State name fallback"}])

            resolved = resolve_input(
                query=f'Create a report for the "{state_title.strip()}" conversation.',
                codex_home=codex_home,
                output_dir=root / "out",
            )

            self.assertEqual(resolved.scope_type, "conversation")
            self.assertEqual(resolved.thread_title, state_title.strip())

    def test_prompt_like_state_title_is_accepted_as_authoritative_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_session(root, "2026-07-07", "rollout-a.jsonl", metadata={"thread_title": "Rollout fallback"})
            state_title = "TRANSCRIPT START user: Codex stored this prompt-like value as the thread title"
            make_state_db(
                root,
                [{"rollout_path": str(rollout), "cwd": str(root / "ONCLAIVE"), "title": state_title}],
            )

            resolved = resolve_input(rollout_file=rollout, output_dir=root / "out")

            self.assertEqual(resolved.thread_title, state_title)
            self.assertNotIn(
                "Conversation titles were excluded because the available metadata contained raw conversation content.",
                resolved.warnings,
            )

    def test_state_name_precedes_session_index_title(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = make_session(root, "2026-07-07", "rollout-a.jsonl", metadata={"thread_id": "thread-a"})
            make_session_index(root, [{"id": "thread-a", "thread_name": "Index title"}])
            make_state_db(root, [{"id": "thread-a", "rollout_path": str(rollout), "cwd": str(root / "ONCLAIVE"), "title": "", "name": "State name"}])

            resolved = resolve_input(rollout_file=rollout, output_dir=root / "out")

            self.assertEqual(resolved.thread_title, "State name")

    def test_rollout_prompt_and_transcript_content_is_not_used_as_a_title(self) -> None:
        rejected_titles = (
            "TRANSCRIPT START user: private rollout conversation content",
            "User: " + ("private rollout prompt detail " * 10),
        )
        for rejected_title in rejected_titles:
            with self.subTest(rejected_title=rejected_title[:30]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                rollout = make_session(
                    root,
                    "2026-07-07",
                    "rollout-a.jsonl",
                    metadata={"workspace": "ONCLAIVE", "thread_title": rejected_title},
                )

                resolved = resolve_input(rollout_file=rollout, output_dir=root / "out")

                self.assertIsNone(resolved.thread_title)
                self.assertIsNone(resolved.session_titles[rollout.name])

    def test_conversation_and_workspace_use_state_titles_and_propagate_related_sessions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            parent = make_session(root, "2026-07-07", "rollout-parent.jsonl", metadata={"thread_id": "parent", "workspace": "ONCLAIVE"})
            child = make_session(root, "2026-07-07", "rollout-child.jsonl", metadata={"thread_id": "child", "parent_thread_id": "parent", "workspace": "ONCLAIVE"})
            make_state_db(root, [{"id": "parent", "rollout_path": str(parent), "cwd": str(root / "ONCLAIVE"), "title": "Codex parent title"}])

            conversation = resolve_input(query='Create a report for the "Codex parent title" conversation.', codex_home=codex_home, output_dir=root / "conversation")
            workspace = resolve_input(query="Create an all-time ONCLAIVE workspace report", codex_home=codex_home, output_dir=root / "workspace")

            self.assertEqual(conversation.thread_title, "Codex parent title")
            self.assertEqual(workspace.session_titles, {parent.name: "Codex parent title", child.name: "Codex parent title"})

    def test_natural_language_constraints_are_documented_near_parser(self) -> None:
        source = (SRC_ROOT / "agent_usage_metrics" / "input_resolver.py").read_text(encoding="utf-8")

        self.assertIn("only convert concrete clues into filters", source)
        self.assertIn("must not semantically search raw prompt contents", source)
        self.assertIn("must not guess", source)


if __name__ == "__main__":
    unittest.main()
