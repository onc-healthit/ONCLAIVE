"""Resolve human report requests to exact local Codex or Claude Code sessions."""

from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import dataclass, field, replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from .models import ResolvedInput, UsageQuery


class InputResolverError(ValueError):
    """Raised when the requested usage scope cannot be resolved."""


class NoMatchingSessionsError(InputResolverError):
    """Raised when a structured query matches no local Codex sessions."""


class AmbiguousSessionsError(InputResolverError):
    """Raised when a structured query matches multiple sessions without a selector."""


class NeedsClarificationError(AmbiguousSessionsError):
    """Raised when the request matches multiple safe target interpretations."""

    status = "needs_clarification"

    def __init__(self, message: str, *, clarification: dict[str, Any]):
        super().__init__(message)
        self.clarification = clarification


@dataclass(frozen=True)
class SessionCandidate:
    """Safe metadata used to select a single agent session."""
    rollout_file: Path
    session_date: str | None
    workspace_label: str | None = None
    thread_title: str | None = None
    thread_id: str | None = None
    parent_thread_id: str | None = None
    modified_time: float = 0.0
    start_time: str | None = None
    end_time: str | None = None
    duration_seconds: float | None = None
    event_count: int = 0
    session_ids: set[str] = field(default_factory=set)

    def sort_key(self) -> tuple[str, str, str, float, str]:
        return (
            _rollout_filename_time_key(self.rollout_file.name),
            self.session_date or "",
            self.start_time or "",
            self.modified_time,
            self.rollout_file.name,
        )

    def conversation_key(self) -> tuple[str, str]:
        return (
            _normalize_match_text(self.thread_title or ""),
            _normalize_match_text(self.workspace_label or ""),
            _normalize_match_text(self.thread_id or self.parent_thread_id or ""),
        )

    def privacy_safe_description(self) -> str:
        pieces = [f"file={self.rollout_file.name}"]
        if self.session_date:
            pieces.append(f"date={self.session_date}")
        if self.start_time:
            pieces.append(f"start={self.start_time}")
        if self.end_time:
            pieces.append(f"end={self.end_time}")
        if self.duration_seconds is not None:
            pieces.append(f"duration={_format_duration(self.duration_seconds)}")
        if self.workspace_label:
            pieces.append(f"workspace={_truncate(self.workspace_label)}")
        if self.thread_title:
            pieces.append(f"title={_truncate(self.thread_title)}")
        if self.event_count:
            pieces.append(f"events={self.event_count}")
        return ", ".join(pieces)

    def safe_dict(self) -> dict[str, Any]:
        return {
            "target_type": "session",
            "rollout_file": self.rollout_file.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration_seconds": self.duration_seconds,
            "workspace": self.workspace_label,
            "conversation_title": self.thread_title,
            "thread_id": self.thread_id,
            "parent_thread_id": self.parent_thread_id,
            "event_count": self.event_count,
        }


@dataclass(frozen=True)
class ConversationCandidate:
    """A conversation title and all sessions that belong to it."""
    thread_title: str
    workspace_label: str | None
    sessions: list[SessionCandidate]
    conversation_id: str | None = None

    def sort_key(self) -> tuple[str, str]:
        first = self.sessions[0].sort_key() if self.sessions else ("", 0.0, "")
        return (self.thread_title.casefold(), str(first))

    def privacy_safe_description(self) -> str:
        session_text = "; ".join(session.privacy_safe_description() for session in self.sessions)
        pieces = [f"title={_truncate(self.thread_title)}", f"sessions={len(self.sessions)}"]
        if self.workspace_label:
            pieces.append(f"workspace={_truncate(self.workspace_label)}")
        if session_text:
            pieces.append(f"session candidates: {session_text}")
        return ", ".join(pieces)

    def safe_dict(self) -> dict[str, Any]:
        return {
            "target_type": "conversation",
            "conversation_title": self.thread_title,
            "workspace": self.workspace_label,
            "conversation_id": self.conversation_id,
            "session_count": len(self.sessions),
            "rollout_files": [session.rollout_file.name for session in self.sessions],
            "sessions": [session.safe_dict() for session in self.sessions],
        }


_MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}
_PROMPT_LIKE_KEYS = {"content", "message", "messages", "prompt", "text", "input", "output"}
_THREAD_TITLE_KEYS = {
    "thread_title",
    "threadTitle",
    "thread_name",
    "threadName",
    "title",
    "conversation_title",
    "conversationTitle",
    "session_title",
    "sessionTitle",
    "chat_title",
    "chatTitle",
}
_NORMALIZED_THREAD_TITLE_KEYS = {key.casefold() for key in _THREAD_TITLE_KEYS}
_THREAD_ID_KEYS = {"id", "thread_id", "threadId", "conversation_id", "conversationId"}
_PARENT_THREAD_ID_KEYS = {"parent_thread_id", "parentThreadId", "parent_id", "parentId"}
_SESSION_ID_KEYS = {
    "conversation_id",
    "conversationId",
    "rollout_id",
    "rolloutId",
    "session_id",
    "sessionId",
    "thread_id",
    "threadId",
}
_WORKSPACE_KEYS = {
    "cwd",
    "project",
    "project_name",
    "workspace",
    "workspace_path",
    "working_directory",
}
_DATE_KEYS = {"created_at", "date", "started_at", "timestamp"}
_TIME_KEYS = {"created_at", "date", "ended_at", "finished_at", "started_at", "timestamp"}
_TARGET_SCOPE_EXPLANATION = (
    "Please choose what you want measured:\n\n"
    "1. Session - one agent run / one rollout file. Best for measuring a single Codex execution.\n"
    "2. Conversation - the whole Codex chat/thread. Best when a thread contains multiple agent runs for the same task.\n"
    "3. Workspace - all matching activity in a project/repo, usually with a date range. Best for broader project-level reporting."
)


def resolve_input(
    *,
    query: str | None = None,
    rollout_file: str | Path | None = None,
    codex_home: str | Path | None = None,
    claude_home: str | Path | None = None,
    agent: str | None = None,
    output_dir: str | Path | None = None,
    workspace: str | Path | None = None,
    thread_title: str | None = None,
) -> ResolvedInput:
    """Resolve explicit flags or a natural-language request to a report target."""
    usage_query = parse_usage_query(
        query,
        rollout_file=rollout_file,
        codex_home=codex_home,
        claude_home=claude_home,
        agent=agent,
        output_dir=output_dir,
        workspace=workspace,
        thread_title=thread_title,
    )

    if rollout_file is not None or (usage_query.rollout_file and usage_query.rollout_file.exists()):
        return _resolve_rollout_file(
            rollout_file=usage_query.rollout_file,
            codex_home=codex_home,
            claude_home=claude_home,
            agent=usage_query.agent,
            output_dir=output_dir,
            workspace=workspace,
            thread_title=thread_title or usage_query.thread_title_query,
            date_range=usage_query.date_range,
            warnings=usage_query.warnings,
        )

    if not usage_query.raw_query:
        raise InputResolverError("Either query or rollout_file is required.")

    return _resolve_usage_query(usage_query, workspace=workspace)


def parse_usage_query(
    raw_query: str | None = None,
    *,
    rollout_file: str | Path | None = None,
    codex_home: str | Path | None = None,
    claude_home: str | Path | None = None,
    agent: str | None = None,
    output_dir: str | Path | None = None,
    workspace: str | Path | None = None,
    thread_title: str | None = None,
    today: date | None = None,
) -> UsageQuery:
    """Extract agent, scope, name, workspace, and date hints from a user request."""
    query_text = raw_query.strip() if raw_query else None
    parsed_agent = _normalize_agent(agent) if agent else _agent_from_query(query_text)
    warnings: list[str] = []
    reference_date = today or date.today()

    parsed_rollout_file = Path(rollout_file).expanduser() if rollout_file else None
    if parsed_rollout_file is None and query_text:
        parsed_rollout_file = _extract_rollout_file_from_query(query_text)

    selection_mode = None
    if query_text and re.search(r"\b(latest|newest|most recent|recent)\b", query_text, re.IGNORECASE):
        selection_mode = "latest"
    elif query_text and re.search(r"\b(all[-\s]?time|entire history|all history|everything|historical)\b", query_text, re.IGNORECASE):
        selection_mode = "all_time"

    quoted_phrases = _extract_quoted_phrases(query_text) if query_text else []
    target_type_query = _extract_target_type_query(query_text) if query_text else None

    date_query = None
    date_range = None
    if query_text:
        date_query, date_range, date_warnings = _parse_date_filter(query_text, reference_date)
        warnings.extend(date_warnings)

    workspace_query = _workspace_query_from_input(workspace)
    if workspace_query is None and query_text:
        workspace_query = _extract_workspace_query(query_text)

    thread_title_query = thread_title.strip() if thread_title else None
    if thread_title_query is None and query_text:
        thread_title_query = _extract_thread_title_query(query_text)

    # Natural-language support is intentionally constrained. The resolver can
    # only convert concrete clues into filters: agent=codex, workspace/project,
    # date/date range, thread title, latest selection, or a direct rollout file.
    # It must not semantically search raw prompt contents or infer vague
    # references like "the important run" or "the thing I worked on". If it
    # cannot find exactly one safe match, it must not guess.
    if query_text and not any(
        [
            parsed_rollout_file,
            selection_mode,
            date_range,
            workspace_query,
            thread_title_query,
            quoted_phrases,
            target_type_query,
        ]
    ):
        warnings.append(
            "No concrete resolver filters detected; provide target type, latest, date, workspace, "
            "conversation title, or rollout file."
        )

    return UsageQuery(
        raw_query=query_text,
        agent=parsed_agent,
        workspace_query=workspace_query,
        thread_title_query=thread_title_query,
        date_query=date_query,
        date_range=date_range,
        selection_mode=selection_mode,
        target_type_query=target_type_query,
        quoted_phrases=quoted_phrases,
        rollout_file=parsed_rollout_file,
        codex_home=Path(codex_home).expanduser() if codex_home else None,
        claude_home=Path(claude_home).expanduser() if claude_home else None,
        output_dir=Path(output_dir).expanduser() if output_dir else None,
        warnings=warnings,
    )


def _resolve_usage_query(usage_query: UsageQuery, *, workspace: str | Path | None) -> ResolvedInput:
    """Apply deterministic resolution rules and return clarification instead of guessing."""
    if usage_query.agent == "claude_code":
        return _resolve_claude_usage_query(usage_query, workspace=workspace)
    resolved_codex_home = _resolve_codex_home(None, usage_query.codex_home)
    if resolved_codex_home is None:
        raise InputResolverError("Codex home could not be resolved; provide --codex-home or --rollout-file.")

    warnings = list(usage_query.warnings)
    logs_db, state_db = _resolve_optional_codex_databases(resolved_codex_home, warnings)
    candidates = _discover_sessions(resolved_codex_home, warnings, state_db=state_db)
    context_matches = _context_matching_sessions(candidates, usage_query)

    if not context_matches:
        raise NoMatchingSessionsError(
            "No Codex targets matched the request. Provide a session, conversation title, "
            "workspace/project name with date range, or rollout JSONL file."
        )

    for phrase in usage_query.quoted_phrases:
        resolved = _resolve_quoted_phrase(
            phrase,
            context_matches,
            usage_query,
            workspace=workspace,
            codex_home=resolved_codex_home,
            logs_db=logs_db,
            state_db=state_db,
            warnings=warnings,
        )
        if resolved is not None:
            return resolved

    if usage_query.thread_title_query:
        conversations = _conversation_matches(context_matches, usage_query.thread_title_query, exact=False)
        if len(conversations) == 1:
            return _resolved_conversation(
                conversations[0],
                usage_query,
                workspace=workspace,
                codex_home=resolved_codex_home,
                logs_db=logs_db,
                state_db=state_db,
                warnings=warnings,
                resolution_status="exact" if _text_equal(conversations[0].thread_title, usage_query.thread_title_query) else "inferred",
            )
        if len(conversations) > 1:
            raise _needs_clarification(
                usage_query,
                reason="More than one conversation title matched the request.",
                conversations=conversations,
                sessions=context_matches,
            )

    session_identifier = _session_identifier_query(usage_query)
    if session_identifier:
        session_matches = [
            candidate
            for candidate in context_matches
            if _candidate_matches_session_identifier(candidate, session_identifier)
        ]
        if len(session_matches) == 1:
            return _resolved_session(
                session_matches[0],
                usage_query,
                workspace=workspace,
                codex_home=resolved_codex_home,
                logs_db=logs_db,
                state_db=state_db,
                warnings=warnings,
                resolution_status="exact",
            )
        if len(session_matches) > 1:
            raise _needs_clarification(
                usage_query,
                reason="More than one session matched the requested rollout/session identifier.",
                sessions=session_matches,
            )

    if _requests_workspace_scope(usage_query):
        if not _has_workspace_time_intent(usage_query):
            raise _needs_clarification(
                usage_query,
                reason="Workspace targets need a date range, latest, or explicit all-time scope.",
                conversations=_conversation_groups(context_matches),
                sessions=context_matches,
            )
        if usage_query.selection_mode == "latest":
            selected = max(context_matches, key=lambda candidate: candidate.sort_key())
            return _resolved_workspace(
                [selected],
                usage_query,
                workspace=workspace,
                codex_home=resolved_codex_home,
                logs_db=logs_db,
                state_db=state_db,
                warnings=warnings,
                resolution_status="inferred",
            )
        if usage_query.date_range or usage_query.selection_mode == "all_time":
            return _resolved_workspace(
                context_matches,
                usage_query,
                workspace=workspace,
                codex_home=resolved_codex_home,
                logs_db=logs_db,
                state_db=state_db,
                warnings=warnings,
                resolution_status="exact",
            )

    matches = _matching_sessions(context_matches, usage_query)
    if not matches:
        raise NoMatchingSessionsError(
            "No Codex targets matched the request. Provide a session, conversation title, "
            "workspace/project name with date range, or rollout JSONL file."
        )

    if len(matches) == 1:
        return _resolved_session(
            matches[0],
            usage_query,
            workspace=workspace,
            codex_home=resolved_codex_home,
            logs_db=logs_db,
            state_db=state_db,
            warnings=warnings,
            resolution_status="exact",
        )

    if usage_query.selection_mode == "latest" and _requests_session_scope(usage_query):
        selected = max(matches, key=lambda candidate: candidate.sort_key())
        return _resolved_session(
            selected,
            usage_query,
            workspace=workspace,
            codex_home=resolved_codex_home,
            logs_db=logs_db,
            state_db=state_db,
            warnings=warnings,
            resolution_status="inferred",
        )

    raise _needs_clarification(
        usage_query,
        reason="More than one possible report target matched the request.",
        conversations=_conversation_groups(matches),
        sessions=matches,
    )


def _resolve_rollout_file(
    *,
    rollout_file: str | Path,
    codex_home: str | Path | None,
    claude_home: str | Path | None,
    agent: str,
    output_dir: str | Path | None,
    workspace: str | Path | None,
    thread_title: str | None,
    date_range: tuple[str, str] | None,
    warnings: list[str] | None = None,
) -> ResolvedInput:
    rollout_path = _validate_rollout_file(rollout_file)
    if agent == "claude_code":
        resolved_warnings = list(warnings or [])
        metadata = _read_claude_transcript_metadata(rollout_path, resolved_warnings)
        return ResolvedInput(
            agent="claude_code",
            scope_type="session",
            rollout_files=[rollout_path],
            codex_home=None,
            logs_db=None,
            state_db=None,
            workspace=_resolve_workspace_or_label(workspace, metadata.get("workspace_label")),
            thread_title=thread_title or metadata.get("thread_title"),
            date_range=date_range or _single_date_range(metadata.get("session_date")),
            output_dir=_resolve_output_dir(output_dir),
            warnings=resolved_warnings,
            resolution_status="exact",
            claude_home=_resolve_claude_home(claude_home),
            source_metadata=_claude_source_metadata(metadata),
            session_titles={rollout_path.name: thread_title or metadata.get("thread_title")},
        )
    resolved_codex_home = _resolve_codex_home(rollout_path, codex_home)
    resolved_warnings = list(warnings or [])
    metadata = _read_safe_rollout_metadata(rollout_path, resolved_warnings)

    logs_db: Path | None = None
    state_db: Path | None = None
    if resolved_codex_home:
        logs_db, state_db = _resolve_optional_codex_databases(resolved_codex_home, resolved_warnings)
        index_metadata = _read_session_index_metadata(resolved_codex_home, resolved_warnings)
        state_metadata = _read_state_thread_metadata(state_db, resolved_warnings, index_metadata=index_metadata)
        metadata = _merge_title_metadata(
            _state_metadata_for_rollout(rollout_path, state_metadata, rollout_metadata=metadata),
            metadata,
            index_metadata,
        )
    session_date = _extract_session_date(rollout_path, metadata)

    return ResolvedInput(
        agent="codex",
        scope_type="session",
        rollout_files=[rollout_path],
        codex_home=resolved_codex_home,
        logs_db=logs_db,
        state_db=state_db,
        workspace=_resolve_workspace_or_label(workspace, metadata.get("workspace_label")),
        thread_title=thread_title or metadata.get("thread_title"),
        date_range=date_range or _single_date_range(session_date),
        output_dir=_resolve_output_dir(output_dir),
        warnings=resolved_warnings,
        resolution_status="exact",
        session_titles={rollout_path.name: thread_title or metadata.get("thread_title")},
    )


def _resolve_quoted_phrase(
    phrase: str,
    context_matches: list[SessionCandidate],
    usage_query: UsageQuery,
    *,
    workspace: str | Path | None,
    codex_home: Path,
    logs_db: Path | None,
    state_db: Path | None,
    warnings: list[str],
) -> ResolvedInput | None:
    """Prioritize exact conversation, session, and workspace matches for quoted names."""
    conversations = _conversation_matches(context_matches, phrase, exact=True)
    if len(conversations) == 1:
        return _resolved_conversation(
            conversations[0],
            usage_query,
            workspace=workspace,
            codex_home=codex_home,
            logs_db=logs_db,
            state_db=state_db,
            warnings=warnings,
            resolution_status="exact",
        )
    if len(conversations) > 1:
        raise _needs_clarification(
            usage_query,
            reason=f'More than one conversation matched "{phrase}".',
            conversations=conversations,
            sessions=context_matches,
        )

    session_matches = [
        candidate
        for candidate in context_matches
        if _candidate_matches_session_identifier(candidate, phrase)
    ]
    if len(session_matches) == 1:
        return _resolved_session(
            session_matches[0],
            usage_query,
            workspace=workspace,
            codex_home=codex_home,
            logs_db=logs_db,
            state_db=state_db,
            warnings=warnings,
            resolution_status="exact",
        )
    if len(session_matches) > 1:
        raise _needs_clarification(
            usage_query,
            reason=f'More than one session matched "{phrase}".',
            sessions=session_matches,
        )

    workspace_matches = [
        candidate
        for candidate in context_matches
        if candidate.workspace_label and _text_equal(candidate.workspace_label, phrase)
    ]
    if workspace_matches:
        if _requests_workspace_scope(usage_query):
            if not _has_workspace_time_intent(usage_query):
                raise _needs_clarification(
                    usage_query,
                    reason=f'"{phrase}" matched a workspace. Workspace reports need a date range, latest, or explicit all-time scope.',
                    conversations=_conversation_groups(workspace_matches),
                    sessions=workspace_matches,
                )
            selected_workspace_matches = workspace_matches
            resolution_status = "exact"
            if usage_query.selection_mode == "latest":
                selected_workspace_matches = [max(workspace_matches, key=lambda candidate: candidate.sort_key())]
                resolution_status = "inferred"
            return _resolved_workspace(
                selected_workspace_matches,
                usage_query,
                workspace=workspace,
                codex_home=codex_home,
                logs_db=logs_db,
                state_db=state_db,
                warnings=warnings,
                resolution_status=resolution_status,
            )
        if len(workspace_matches) == 1:
            return _resolved_session(
                workspace_matches[0],
                usage_query,
                workspace=workspace,
                codex_home=codex_home,
                logs_db=logs_db,
                state_db=state_db,
                warnings=warnings,
                resolution_status="exact",
            )
        raise _needs_clarification(
            usage_query,
            reason=f'"{phrase}" matched a workspace with multiple sessions.',
            conversations=_conversation_groups(workspace_matches),
            sessions=workspace_matches,
        )

    fuzzy_conversations = _conversation_matches(context_matches, phrase, exact=False)
    if len(fuzzy_conversations) == 1:
        return _resolved_conversation(
            fuzzy_conversations[0],
            usage_query,
            workspace=workspace,
            codex_home=codex_home,
            logs_db=logs_db,
            state_db=state_db,
            warnings=warnings,
            resolution_status="inferred",
        )
    if len(fuzzy_conversations) > 1:
        raise _needs_clarification(
            usage_query,
            reason=f'More than one conversation title partially matched "{phrase}".',
            conversations=fuzzy_conversations,
            sessions=context_matches,
        )

    return None


def _resolved_session(
    selected: SessionCandidate,
    usage_query: UsageQuery,
    *,
    workspace: str | Path | None,
    codex_home: Path,
    logs_db: Path | None,
    state_db: Path | None,
    warnings: list[str],
    resolution_status: str,
) -> ResolvedInput:
    return ResolvedInput(
        agent=usage_query.agent,
        scope_type="session",
        rollout_files=[selected.rollout_file],
        codex_home=codex_home,
        logs_db=logs_db,
        state_db=state_db,
        workspace=_resolve_workspace_or_label(workspace, selected.workspace_label),
        thread_title=selected.thread_title or usage_query.thread_title_query,
        date_range=usage_query.date_range or _single_date_range(selected.session_date),
        output_dir=_resolve_output_dir(usage_query.output_dir),
        warnings=warnings,
        resolution_status=resolution_status,
        session_titles={selected.rollout_file.name: selected.thread_title},
    )


def _resolved_conversation(
    selected: ConversationCandidate,
    usage_query: UsageQuery,
    *,
    workspace: str | Path | None,
    codex_home: Path,
    logs_db: Path | None,
    state_db: Path | None,
    warnings: list[str],
    resolution_status: str,
) -> ResolvedInput:
    sessions = sorted(selected.sessions, key=lambda candidate: candidate.sort_key())
    return ResolvedInput(
        agent=usage_query.agent,
        scope_type="conversation",
        rollout_files=[session.rollout_file for session in sessions],
        codex_home=codex_home,
        logs_db=logs_db,
        state_db=state_db,
        workspace=_resolve_workspace_or_label(workspace, selected.workspace_label),
        thread_title=selected.thread_title,
        date_range=usage_query.date_range or _date_range_from_sessions(sessions),
        output_dir=_resolve_output_dir(usage_query.output_dir),
        warnings=warnings,
        resolution_status=resolution_status,
        session_titles=_session_titles_for_candidates(sessions),
    )


def _resolved_workspace(
    sessions: list[SessionCandidate],
    usage_query: UsageQuery,
    *,
    workspace: str | Path | None,
    codex_home: Path,
    logs_db: Path | None,
    state_db: Path | None,
    warnings: list[str],
    resolution_status: str,
) -> ResolvedInput:
    selected_sessions = sorted(sessions, key=lambda candidate: candidate.sort_key())
    return ResolvedInput(
        agent=usage_query.agent,
        scope_type="workspace",
        rollout_files=[session.rollout_file for session in selected_sessions],
        codex_home=codex_home,
        logs_db=logs_db,
        state_db=state_db,
        workspace=_resolve_workspace_or_label(workspace, _common_workspace_label(selected_sessions)),
        thread_title=None,
        date_range=usage_query.date_range or _date_range_from_sessions(selected_sessions),
        output_dir=_resolve_output_dir(usage_query.output_dir),
        warnings=warnings,
        resolution_status=resolution_status,
        session_titles=_session_titles_for_candidates(selected_sessions),
    )


def _needs_clarification(
    usage_query: UsageQuery,
    *,
    reason: str,
    conversations: list[ConversationCandidate] | None = None,
    sessions: list[SessionCandidate] | None = None,
) -> NeedsClarificationError:
    conversations = sorted(conversations or [], key=lambda candidate: candidate.sort_key())
    sessions = sorted(sessions or [], key=lambda candidate: candidate.sort_key())
    label = _clarification_label(usage_query)
    candidate_lines: list[str] = []
    if conversations:
        candidate_lines.extend(
            f"- Conversation: {conversation.privacy_safe_description()}"
            for conversation in conversations
        )
    elif sessions:
        candidate_lines.extend(
            f"- Session: {session.privacy_safe_description()}"
            for session in sessions
        )

    message_parts = [
        f'I found more than one possible target for "{label}".',
        reason,
        _TARGET_SCOPE_EXPLANATION,
    ]
    if candidate_lines:
        message_parts.extend(["", "Matching candidates:", *candidate_lines])
    message_parts.append("")
    message_parts.append("Do you want the whole conversation/workspace or one specific session?")

    clarification = {
        "status": "needs_clarification",
        "reason": reason,
        "target_options": ["session", "conversation", "workspace"],
        "conversations": [conversation.safe_dict() for conversation in conversations],
        "sessions": [session.safe_dict() for session in sessions],
    }
    return NeedsClarificationError("\n".join(message_parts), clarification=clarification)


def _validate_rollout_file(rollout_file: str | Path) -> Path:
    rollout_path = Path(rollout_file).expanduser()
    if not rollout_path.exists():
        raise FileNotFoundError(f"Rollout file does not exist: {rollout_path}")
    if not rollout_path.is_file():
        raise InputResolverError(f"Rollout file is not a file: {rollout_path}")
    if rollout_path.suffix.lower() != ".jsonl":
        raise InputResolverError(f"Rollout file must have a .jsonl extension: {rollout_path}")

    try:
        with rollout_path.open("r", encoding="utf-8"):
            pass
    except OSError as exc:
        raise PermissionError(f"Rollout file is not readable: {rollout_path}") from exc

    return rollout_path.resolve()


def _resolve_codex_home(rollout_path: Path | None, codex_home: str | Path | None) -> Path | None:
    if codex_home:
        return Path(codex_home).expanduser().resolve()

    if rollout_path:
        for candidate in (rollout_path.parent, *rollout_path.parents):
            if candidate.name == ".codex":
                return candidate.resolve()
        return None

    default_codex_home = Path.home() / ".codex"
    if default_codex_home.exists():
        return default_codex_home.resolve()
    return None


def _resolve_optional_codex_databases(codex_home: Path, warnings: list[str]) -> tuple[Path | None, Path | None]:
    logs_db: Path | None = None
    state_db: Path | None = None
    logs_db_candidate = codex_home / "logs_2.sqlite"
    state_db_candidate = codex_home / "state_5.sqlite"

    if logs_db_candidate.exists():
        logs_db = logs_db_candidate.resolve()
    else:
        warnings.append("logs_2.sqlite not found under codex_home")

    if state_db_candidate.exists():
        state_db = state_db_candidate.resolve()
    else:
        warnings.append("state_5.sqlite not found under codex_home")

    return logs_db, state_db


def _resolve_output_dir(output_dir: str | Path | None) -> Path:
    resolved_output_dir = Path(output_dir or "outputs").expanduser()
    resolved_output_dir.mkdir(parents=True, exist_ok=True)
    return resolved_output_dir.resolve()


def _resolve_workspace(workspace: str | Path | None) -> Path | None:
    return Path(workspace).expanduser().resolve() if workspace else None


def _resolve_workspace_or_label(workspace: str | Path | None, workspace_label: str | None) -> Path | None:
    resolved_workspace = _resolve_workspace(workspace)
    if resolved_workspace is not None:
        return resolved_workspace
    if workspace_label:
        return Path(workspace_label)
    return None


def _single_date_range(session_date: str | None) -> tuple[str, str] | None:
    if not session_date:
        return None
    return (session_date, session_date)


def _discover_sessions(codex_home: Path, warnings: list[str], *, state_db: Path | None = None) -> list[SessionCandidate]:
    session_roots = [
        root
        for root in (codex_home / "sessions", codex_home / "archived_sessions")
        if root.exists()
    ]
    if not session_roots:
        warnings.append("sessions directory not found under codex_home")
        return []

    index_metadata = _read_session_index_metadata(codex_home, warnings)
    state_metadata = _read_state_thread_metadata(state_db, warnings, index_metadata=index_metadata)
    candidates: list[SessionCandidate] = []
    seen_rollouts: set[Path] = set()
    for sessions_root in session_roots:
        for rollout_file in sorted(sessions_root.rglob("*.jsonl")):
            if not rollout_file.is_file():
                continue
            resolved_rollout = rollout_file.resolve()
            if resolved_rollout in seen_rollouts:
                continue
            seen_rollouts.add(resolved_rollout)
            metadata = _read_safe_rollout_metadata(rollout_file, warnings)
            metadata = _merge_title_metadata(
                _state_metadata_for_rollout(rollout_file, state_metadata, rollout_metadata=metadata),
                metadata,
                index_metadata,
            )
            session_date = _extract_session_date(rollout_file, metadata)
            session_ids = set(metadata.get("session_ids", "").split(",")) if metadata.get("session_ids") else set()
            session_ids.update(_rollout_identifier_set(rollout_file))
            session_ids.update(
                value
                for value in (metadata.get("thread_id"), metadata.get("parent_thread_id"))
                if value
            )
            candidates.append(
                SessionCandidate(
                    rollout_file=resolved_rollout,
                    session_date=session_date,
                    workspace_label=metadata.get("workspace_label"),
                    thread_title=metadata.get("thread_title"),
                    thread_id=metadata.get("thread_id"),
                    parent_thread_id=metadata.get("parent_thread_id"),
                    modified_time=rollout_file.stat().st_mtime,
                    start_time=metadata.get("start_time"),
                    end_time=metadata.get("end_time"),
                    duration_seconds=_float_or_none(metadata.get("duration_seconds")),
                    event_count=int(metadata.get("event_count", "0")),
                    session_ids={item for item in session_ids if item},
                )
            )

    return _propagate_thread_titles(candidates)


def _read_session_index_metadata(codex_home: Path, warnings: list[str]) -> dict[str, dict[str, str]]:
    index_path = codex_home / "session_index.jsonl"
    if not index_path.exists():
        return {}

    metadata_by_id: dict[str, dict[str, str]] = {}
    try:
        with index_path.open("r", encoding="utf-8-sig") as handle:
            for line in handle:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    row = json.loads(stripped)
                except json.JSONDecodeError:
                    continue
                thread_id = _normalize_match_text(_string_or_none(row.get("id")) or "")
                thread_name = _safe_thread_title(_string_or_none(row.get("thread_name")))
                if not thread_id or not thread_name:
                    continue
                metadata_by_id[thread_id] = {"thread_title": thread_name}
    except OSError:
        warnings.append("session_index.jsonl unavailable for thread title metadata")
    return metadata_by_id


def _read_state_thread_metadata(
    state_db: Path | None,
    warnings: list[str],
    *,
    index_metadata: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    if state_db is None or not state_db.exists():
        return {}

    metadata_by_key: dict[str, dict[str, str]] = {}
    connection: sqlite3.Connection | None = None
    try:
        connection = sqlite3.connect(f"{state_db.resolve().as_uri()}?mode=ro", uri=True)
        connection.row_factory = sqlite3.Row
        if not _state_threads_table_available(connection):
            return {}
        columns = _state_threads_columns(connection)
        title_column = "title" if "title" in columns else None
        name_column = "name" if "name" in columns else None
        if title_column is None and name_column is None:
            return {}
        selected_columns = ["id", "rollout_path", "cwd"]
        selected_columns.extend(column for column in (title_column, name_column) if column is not None)
        cursor = connection.execute(
            f"SELECT {', '.join(selected_columns)} FROM threads"
        )
        for row in cursor:
            rollout_path = _string_or_none(row["rollout_path"])
            metadata: dict[str, str] = {}
            thread_id = _normalize_match_text(_string_or_none(row["id"]) or "")
            if thread_id:
                metadata["thread_id"] = thread_id
            workspace_label = _safe_workspace_label(_string_or_none(row["cwd"]) or "")
            if workspace_label:
                metadata["workspace_label"] = workspace_label
            thread_title = _authoritative_state_title(_string_or_none(row["title"])) if title_column else None
            if not thread_title and name_column:
                thread_title = _authoritative_state_title(_string_or_none(row["name"]))
            if thread_title:
                metadata["thread_title"] = thread_title
            if not metadata:
                continue
            if rollout_path:
                for key in _rollout_lookup_keys(Path(rollout_path)):
                    metadata_by_key.setdefault(key, metadata)
            if thread_id:
                metadata_by_key.setdefault(f"thread:{thread_id}", metadata)
    except sqlite3.Error as exc:
        warnings.append(f"state_5.sqlite thread metadata unavailable: {exc.__class__.__name__}")
    finally:
        if connection is not None:
            connection.close()
    return metadata_by_key


def _state_threads_columns(connection: sqlite3.Connection) -> set[str]:
    return {
        str(row["name"])
        for row in connection.execute("PRAGMA table_info(threads)").fetchall()
    }


def _state_threads_table_available(connection: sqlite3.Connection) -> bool:
    table = connection.execute(
        "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'threads' LIMIT 1"
    ).fetchone()
    if table is None:
        return False
    columns = _state_threads_columns(connection)
    return {"id", "rollout_path", "cwd"}.issubset(columns) and bool({"title", "name"}.intersection(columns))


def _state_metadata_for_rollout(
    rollout_file: Path,
    metadata_by_key: dict[str, dict[str, str]],
    *,
    rollout_metadata: dict[str, str] | None = None,
) -> dict[str, str]:
    for key in _rollout_lookup_keys(rollout_file):
        metadata = metadata_by_key.get(key)
        if metadata:
            return dict(metadata)
    for identifier in (
        (rollout_metadata or {}).get("thread_id"),
        (rollout_metadata or {}).get("parent_thread_id"),
    ):
        if not identifier:
            continue
        metadata = metadata_by_key.get(f"thread:{_normalize_match_text(identifier)}")
        if metadata:
            return dict(metadata)
    return {}


def _merge_title_metadata(
    state_metadata: dict[str, str],
    rollout_metadata: dict[str, str],
    index_metadata: dict[str, dict[str, str]],
) -> dict[str, str]:
    """Apply the shared Codex title precedence for all report scopes."""
    enriched = {**state_metadata, **rollout_metadata}
    state_title = state_metadata.get("thread_title")
    if state_title:
        enriched["thread_title"] = state_title
        return enriched

    for key in ("thread_id", "parent_thread_id"):
        thread_id = _normalize_match_text(enriched.get(key) or "")
        if not thread_id:
            continue
        thread_title = index_metadata.get(thread_id, {}).get("thread_title")
        if thread_title:
            enriched["thread_title"] = thread_title
            return enriched
    rollout_title = rollout_metadata.get("thread_title")
    if rollout_title:
        enriched["thread_title"] = rollout_title
    return enriched


def _rollout_lookup_keys(rollout_file: Path) -> set[str]:
    keys = {_normalize_path_key(rollout_file), rollout_file.name.casefold()}
    try:
        keys.add(_normalize_path_key(rollout_file.resolve()))
    except OSError:
        pass
    return {key for key in keys if key}


def _normalize_path_key(path: Path) -> str:
    text = str(path).strip()
    if text.startswith("\\\\?\\"):
        text = text[4:]
    return text.rstrip("\\/").casefold()


def _string_or_none(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _context_matching_sessions(candidates: list[SessionCandidate], usage_query: UsageQuery) -> list[SessionCandidate]:
    matches: list[SessionCandidate] = []
    for candidate in candidates:
        if usage_query.date_range:
            if not candidate.session_date:
                continue
            start, end = usage_query.date_range
            if not start <= candidate.session_date <= end:
                continue

        if usage_query.workspace_query:
            if not candidate.workspace_label:
                continue
            if usage_query.workspace_query.casefold() not in candidate.workspace_label.casefold():
                continue

        matches.append(candidate)

    return matches


def _matching_sessions(candidates: list[SessionCandidate], usage_query: UsageQuery) -> list[SessionCandidate]:
    matches: list[SessionCandidate] = []
    for candidate in candidates:
        if usage_query.thread_title_query:
            if not candidate.thread_title:
                continue
            if usage_query.thread_title_query.casefold() not in candidate.thread_title.casefold():
                continue

        matches.append(candidate)

    return matches


def _conversation_matches(
    candidates: list[SessionCandidate],
    title_query: str,
    *,
    exact: bool,
) -> list[ConversationCandidate]:
    roots = [
        candidate
        for candidate in candidates
        if candidate.thread_title
        and (_text_equal(candidate.thread_title, title_query) if exact else _text_contains(candidate.thread_title, title_query))
    ]
    conversations = [
        _conversation_from_root(root, candidates)
        for root in roots
    ]
    return _dedupe_conversations(conversations)


def _conversation_from_root(root: SessionCandidate, candidates: list[SessionCandidate]) -> ConversationCandidate:
    sessions = _expand_conversation_sessions(root, candidates)
    return ConversationCandidate(
        thread_title=root.thread_title or "",
        workspace_label=_common_workspace_label(sessions) or root.workspace_label,
        sessions=sessions,
        conversation_id=_conversation_identity(root),
    )


def _expand_conversation_sessions(root: SessionCandidate, candidates: list[SessionCandidate]) -> list[SessionCandidate]:
    """Include linked follow-up sessions so an exact conversation is not silently truncated."""
    expanded = [
        candidate
        for candidate in candidates
        if _candidate_belongs_to_conversation(root, candidate)
    ]
    if root not in expanded:
        expanded.append(root)
    return sorted(_dedupe_session_candidates(expanded), key=lambda candidate: candidate.sort_key())


def _candidate_belongs_to_conversation(root: SessionCandidate, candidate: SessionCandidate) -> bool:
    root_ids = _conversation_identities(root)
    candidate_ids = _conversation_identities(candidate)
    if root_ids and candidate_ids and root_ids.intersection(candidate_ids):
        return True

    if root.thread_title and candidate.thread_title and _text_equal(root.thread_title, candidate.thread_title):
        return _same_workspace(root, candidate)

    return _related_followup_title(root, candidate)


def _related_followup_title(root: SessionCandidate, candidate: SessionCandidate) -> bool:
    """Recognize related titles only within the same workspace as a fallback link."""
    if not root.thread_title or not candidate.thread_title:
        return False
    if not _same_workspace(root, candidate):
        return False
    if root.session_date and candidate.session_date and root.session_date != candidate.session_date:
        return False

    root_tokens = _significant_title_tokens(root.thread_title)
    candidate_tokens = _significant_title_tokens(candidate.thread_title)
    if len(root_tokens) < 2:
        return False
    return root_tokens.issubset(candidate_tokens)


def _significant_title_tokens(value: str) -> set[str]:
    stop_words = {
        "a",
        "an",
        "and",
        "build",
        "create",
        "for",
        "report",
        "run",
        "session",
        "test",
        "the",
    }
    tokens = {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*", value)
    }
    return {token for token in tokens if token not in stop_words}


def _same_workspace(left: SessionCandidate, right: SessionCandidate) -> bool:
    if left.workspace_label and right.workspace_label:
        return _text_equal(left.workspace_label, right.workspace_label)
    return True


def _conversation_identity(candidate: SessionCandidate) -> str | None:
    identities = _conversation_identities(candidate)
    return sorted(identities)[0] if identities else None


def _conversation_identities(candidate: SessionCandidate) -> set[str]:
    identities = {
        _normalize_match_text(candidate.thread_id or ""),
        _normalize_match_text(candidate.parent_thread_id or ""),
        *candidate.session_ids,
        *_rollout_identifier_set(candidate.rollout_file),
    }
    return {identity for identity in identities if identity}


def _dedupe_conversations(conversations: list[ConversationCandidate]) -> list[ConversationCandidate]:
    deduped: list[ConversationCandidate] = []
    seen: set[tuple[str, str, tuple[str, ...]]] = set()
    for conversation in sorted(conversations, key=lambda candidate: candidate.sort_key()):
        key = (
            _normalize_match_text(conversation.thread_title),
            _normalize_match_text(conversation.workspace_label or ""),
            tuple(session.rollout_file.name for session in conversation.sessions),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(conversation)
    return deduped


def _dedupe_session_candidates(candidates: list[SessionCandidate]) -> list[SessionCandidate]:
    deduped: list[SessionCandidate] = []
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate.rollout_file in seen:
            continue
        seen.add(candidate.rollout_file)
        deduped.append(candidate)
    return deduped


def _conversation_groups(candidates: list[SessionCandidate]) -> list[ConversationCandidate]:
    groups: dict[tuple[str, str], list[SessionCandidate]] = {}
    for candidate in candidates:
        if not candidate.thread_title:
            continue
        groups.setdefault(candidate.conversation_key(), []).append(candidate)

    conversations: list[ConversationCandidate] = []
    for group in groups.values():
        sessions = sorted(group, key=lambda candidate: candidate.sort_key())
        first = sessions[0]
        conversations.append(
            ConversationCandidate(
                thread_title=first.thread_title or "",
                workspace_label=_common_workspace_label(sessions),
                sessions=sessions,
            )
        )
    return sorted(conversations, key=lambda candidate: candidate.sort_key())


def _candidate_matches_session_identifier(candidate: SessionCandidate, value: str) -> bool:
    normalized = _normalize_match_text(value)
    if not normalized:
        return False
    identifiers = {
        _normalize_match_text(candidate.rollout_file.name),
        _normalize_match_text(candidate.rollout_file.stem),
        *candidate.session_ids,
    }
    if candidate.rollout_file.stem.startswith("rollout-"):
        identifiers.add(_normalize_match_text(candidate.rollout_file.stem[len("rollout-") :]))
    identifiers.update(
        _normalize_match_text(match)
        for match in re.findall(
            r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            candidate.rollout_file.stem,
        )
    )
    return normalized in identifiers


def _session_identifier_query(usage_query: UsageQuery) -> str | None:
    if usage_query.rollout_file:
        return usage_query.rollout_file.name
    for phrase in usage_query.quoted_phrases:
        if phrase.endswith(".jsonl") or "rollout-" in phrase.casefold():
            return phrase
    return None


def _requests_session_scope(usage_query: UsageQuery) -> bool:
    return usage_query.target_type_query in {None, "session"}


def _requests_workspace_scope(usage_query: UsageQuery) -> bool:
    return usage_query.target_type_query == "workspace" or (
        usage_query.workspace_query is not None
        and _has_workspace_time_intent(usage_query)
        and not usage_query.quoted_phrases
        and usage_query.target_type_query != "session"
    )


def _has_workspace_time_intent(usage_query: UsageQuery) -> bool:
    return usage_query.date_range is not None or usage_query.selection_mode in {"latest", "all_time"}


def _common_workspace_label(candidates: list[SessionCandidate]) -> str | None:
    labels = [candidate.workspace_label for candidate in candidates if candidate.workspace_label]
    if not labels:
        return None
    first = labels[0]
    if all(_text_equal(first, label) for label in labels):
        return first
    return None


def _date_range_from_sessions(candidates: list[SessionCandidate]) -> tuple[str, str] | None:
    dates = sorted(candidate.session_date for candidate in candidates if candidate.session_date)
    if not dates:
        return None
    return (dates[0], dates[-1])


def _session_titles_for_candidates(candidates: list[SessionCandidate]) -> dict[str, str | None]:
    """Return safe per-session titles without inventing values for missing metadata."""
    return {
        candidate.rollout_file.name: candidate.thread_title
        for candidate in candidates
    }


def _propagate_thread_titles(candidates: list[SessionCandidate]) -> list[SessionCandidate]:
    """Fill missing titles from explicitly linked sessions without changing metrics."""
    related: dict[int, set[int]] = {index: set() for index in range(len(candidates))}
    identities = [_conversation_identities(candidate) for candidate in candidates]
    for left in range(len(candidates)):
        for right in range(left + 1, len(candidates)):
            if identities[left].intersection(identities[right]):
                related[left].add(right)
                related[right].add(left)

    propagated = list(candidates)
    visited: set[int] = set()
    for index in range(len(candidates)):
        if index in visited:
            continue
        stack = [index]
        component: list[int] = []
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            component.append(current)
            stack.extend(related[current] - visited)
        titles = [candidates[item].thread_title for item in component if candidates[item].thread_title]
        if not titles:
            continue
        best_title = sorted(titles, key=lambda title: (_normalize_match_text(title), title))[0]
        for item in component:
            if propagated[item].thread_title is None:
                propagated[item] = replace(propagated[item], thread_title=best_title)
    return propagated


def _clarification_label(usage_query: UsageQuery) -> str:
    if usage_query.quoted_phrases:
        return usage_query.quoted_phrases[0]
    if usage_query.thread_title_query:
        return usage_query.thread_title_query
    if usage_query.workspace_query:
        return usage_query.workspace_query
    return usage_query.raw_query or "request"


def _read_safe_rollout_metadata(rollout_file: Path, warnings: list[str]) -> dict[str, str]:
    metadata: dict[str, str] = {}
    session_ids: set[str] = set()
    start_time: datetime | None = None
    end_time: datetime | None = None
    event_count = 0
    try:
        with rollout_file.open("r", encoding="utf-8-sig") as handle:
            for line_number, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                event_count += 1
                if len(stripped) > 20_000:
                    timestamp = _extract_safe_timestamp_from_line(stripped)
                    start_time = _min_datetime(start_time, timestamp)
                    end_time = _max_datetime(end_time, timestamp)
                    session_ids.update(_extract_safe_session_ids_from_line(stripped))
                    metadata.update(_extract_safe_metadata_fields_from_line(stripped))
                    continue
                if line_number > 500:
                    continue
                if _has_any_json_key(stripped, _PROMPT_LIKE_KEYS):
                    timestamp = _extract_safe_timestamp_from_line(stripped)
                    start_time = _min_datetime(start_time, timestamp)
                    end_time = _max_datetime(end_time, timestamp)
                    session_ids.update(_extract_safe_session_ids_from_line(stripped))
                    metadata.update(_extract_safe_metadata_fields_from_line(stripped))
                    continue
                try:
                    event = json.loads(stripped)
                except json.JSONDecodeError:
                    continue
                timestamp = _extract_safe_timestamp(event)
                start_time = _min_datetime(start_time, timestamp)
                end_time = _max_datetime(end_time, timestamp)
                session_ids.update(_extract_safe_session_ids(event))
                if not _has_any_json_key(stripped, _THREAD_TITLE_KEYS | _WORKSPACE_KEYS | _DATE_KEYS | _SESSION_ID_KEYS | _THREAD_ID_KEYS | _PARENT_THREAD_ID_KEYS):
                    continue
                metadata.update(_extract_safe_metadata_fields(event))
    except OSError:
        warnings.append(f"Skipped unreadable rollout candidate: {rollout_file.name}")

    if start_time:
        metadata["start_time"] = start_time.isoformat().replace("+00:00", "Z")
    if end_time:
        metadata["end_time"] = end_time.isoformat().replace("+00:00", "Z")
    if start_time and end_time:
        metadata["duration_seconds"] = str(max((end_time - start_time).total_seconds(), 0.0))
    if event_count:
        metadata["event_count"] = str(event_count)
    if session_ids:
        metadata["session_ids"] = ",".join(sorted(session_ids))
    return metadata


def _extract_safe_metadata_fields(event: Any) -> dict[str, str]:
    if not isinstance(event, dict):
        return {}

    safe_metadata: dict[str, str] = {}
    containers: list[dict[str, Any]] = [event]
    for key in ("payload", "metadata", "session", "thread", "conversation"):
        value = event.get(key)
        if isinstance(value, dict):
            containers.append(value)

    for container in containers:
        for key, value in container.items():
            normalized_key = str(key).casefold()
            if normalized_key in _PROMPT_LIKE_KEYS:
                continue
            if normalized_key in _NORMALIZED_THREAD_TITLE_KEYS and isinstance(value, str):
                thread_title = _safe_rollout_thread_title(value)
                if thread_title:
                    safe_metadata["thread_title"] = thread_title
            elif normalized_key in {key.casefold() for key in _THREAD_ID_KEYS} and isinstance(value, str):
                thread_id = _normalize_match_text(value)
                if thread_id:
                    safe_metadata["thread_id"] = thread_id
            elif normalized_key in {key.casefold() for key in _PARENT_THREAD_ID_KEYS} and isinstance(value, str):
                parent_thread_id = _normalize_match_text(value)
                if parent_thread_id:
                    safe_metadata["parent_thread_id"] = parent_thread_id
            elif normalized_key in _WORKSPACE_KEYS and isinstance(value, str):
                safe_metadata["workspace_label"] = _safe_workspace_label(value)
            elif normalized_key in _DATE_KEYS and isinstance(value, str):
                event_date = _normalize_iso_date(value)
                if event_date:
                    safe_metadata["event_date"] = event_date

    return {key: value for key, value in safe_metadata.items() if value}


def _extract_safe_metadata_fields_from_line(line: str) -> dict[str, str]:
    safe_metadata: dict[str, str] = {}
    for value in _extract_json_string_values_from_line(line, _THREAD_TITLE_KEYS):
        thread_title = _safe_rollout_thread_title(value)
        if thread_title:
            safe_metadata["thread_title"] = thread_title
            break
    for value in _extract_json_string_values_from_line(line, _THREAD_ID_KEYS):
        thread_id = _normalize_match_text(value)
        if thread_id:
            safe_metadata["thread_id"] = thread_id
            break
    for value in _extract_json_string_values_from_line(line, _PARENT_THREAD_ID_KEYS):
        parent_thread_id = _normalize_match_text(value)
        if parent_thread_id:
            safe_metadata["parent_thread_id"] = parent_thread_id
            break
    for value in _extract_json_string_values_from_line(line, _WORKSPACE_KEYS):
        workspace_label = _safe_workspace_label(value)
        if workspace_label:
            safe_metadata["workspace_label"] = workspace_label
            break
    for value in _extract_json_string_values_from_line(line, _DATE_KEYS):
        event_date = _normalize_iso_date(value)
        if event_date:
            safe_metadata["event_date"] = event_date
            break
    return safe_metadata


def _extract_safe_session_ids_from_line(line: str) -> set[str]:
    return {
        normalized
        for value in _extract_json_string_values_from_line(line, _SESSION_ID_KEYS)
        if (normalized := _normalize_match_text(value))
    }


def _extract_json_string_values_from_line(line: str, keys: set[str]) -> list[str]:
    values: list[str] = []
    for key in keys:
        pattern = rf'(?<!\\)"{re.escape(key)}"\s*:\s*"((?:\\.|[^"\\])*)"'
        for match in re.finditer(pattern, line, re.IGNORECASE):
            values.append(_decode_json_string_fragment(match.group(1)))
    return values


def _decode_json_string_fragment(value: str) -> str:
    try:
        decoded = json.loads(f'"{value}"')
    except json.JSONDecodeError:
        return value
    return decoded if isinstance(decoded, str) else value


def _has_any_json_key(line: str, keys: set[str]) -> bool:
    return any(re.search(rf'"{re.escape(key)}"\s*:', line, re.IGNORECASE) for key in keys)


def _extract_session_date(rollout_file: Path, metadata: dict[str, str]) -> str | None:
    parts = rollout_file.parts
    for index, part in enumerate(parts):
        if part == "sessions" and index + 3 < len(parts):
            maybe_date = _format_date_parts(parts[index + 1], parts[index + 2], parts[index + 3])
            if maybe_date:
                return maybe_date

    joined_path = str(rollout_file)
    match = re.search(r"\b(20\d{2}|19\d{2})[-_/](0?[1-9]|1[0-2])[-_/]([0-2]?\d|3[01])\b", joined_path)
    if match:
        return _format_date_parts(match.group(1), match.group(2), match.group(3))

    return metadata.get("event_date")


def _format_date_parts(year: str, month: str, day: str) -> str | None:
    try:
        parsed = date(int(year), int(month), int(day))
    except ValueError:
        return None
    return parsed.isoformat()


def _parse_date_filter(query_text: str, reference_date: date) -> tuple[str | None, tuple[str, str] | None, list[str]]:
    warnings: list[str] = []

    today_match = re.search(r"\btoday\b", query_text, re.IGNORECASE)
    if today_match:
        date_text = reference_date.isoformat()
        return "today", (date_text, date_text), warnings

    yesterday_match = re.search(r"\byesterday\b", query_text, re.IGNORECASE)
    if yesterday_match:
        yesterday = reference_date - timedelta(days=1)
        date_text = yesterday.isoformat()
        return "yesterday", (date_text, date_text), warnings

    iso_match = re.search(r"\b(20\d{2}|19\d{2})-(0[1-9]|1[0-2])-([0-2]\d|3[01])\b", query_text)
    if iso_match:
        try:
            parsed = date.fromisoformat(iso_match.group(0))
        except ValueError:
            warnings.append(f"Ignored invalid date filter: {iso_match.group(0)}")
            return iso_match.group(0), None, warnings
        date_text = parsed.isoformat()
        return iso_match.group(0), (date_text, date_text), warnings

    month_names = "|".join(_MONTHS)
    month_match = re.search(
        rf"\b({month_names})\.?\s+([0-3]?\d)(?:,?\s+(20\d{{2}}|19\d{{2}}))?\b",
        query_text,
        re.IGNORECASE,
    )
    if month_match:
        month = _MONTHS[month_match.group(1).casefold()]
        day = int(month_match.group(2))
        year = int(month_match.group(3) or reference_date.year)
        try:
            parsed = date(year, month, day)
        except ValueError:
            warnings.append(f"Ignored invalid date filter: {month_match.group(0)}")
            return month_match.group(0), None, warnings
        date_text = parsed.isoformat()
        return month_match.group(0), (date_text, date_text), warnings

    return None, None, warnings


def _extract_quoted_phrases(query_text: str | None) -> list[str]:
    if not query_text:
        return []
    return [
        match.strip()
        for match in re.findall(r"""["']([^"']+)["']""", query_text)
        if match.strip()
    ]


def _extract_target_type_query(query_text: str | None) -> str | None:
    if not query_text:
        return None
    text = query_text.casefold()
    if re.search(r"\b(conversation|thread|chat)\b", text):
        return "conversation"
    if re.search(r"\b(session|rollout|run|execution)\b", text):
        return "session"
    if re.search(r"\b(workspace|project|repo|repository)\b", text):
        return "workspace"
    return None


def _extract_safe_timestamp_from_line(line: str) -> datetime | None:
    if not _has_any_json_key(line, _TIME_KEYS):
        return None
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        return None
    return _extract_safe_timestamp(event)


def _extract_safe_timestamp(event: Any) -> datetime | None:
    for value in _extract_first_string_values(event, _TIME_KEYS):
        parsed = _parse_datetime(value)
        if parsed is not None:
            return parsed
    return None


def _extract_safe_session_ids(event: Any) -> set[str]:
    return {
        _normalize_match_text(value)
        for value in _extract_first_string_values(event, _SESSION_ID_KEYS)
        if _normalize_match_text(value)
    }


def _normalize_iso_date(value: str) -> str | None:
    match = re.search(r"\b(20\d{2}|19\d{2})-(0[1-9]|1[0-2])-([0-2]\d|3[01])\b", value)
    if not match:
        return None
    try:
        return date.fromisoformat(match.group(0)).isoformat()
    except ValueError:
        return None


def _parse_datetime(value: str) -> datetime | None:
    text = str(value).strip()
    if not text:
        return None
    if text.isdigit():
        try:
            numeric = int(text)
            if numeric > 10_000_000_000:
                numeric = numeric / 1000
            return datetime.fromtimestamp(numeric, tz=timezone.utc)
        except (OSError, OverflowError, ValueError):
            return None
    normalized = text.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _min_datetime(left: datetime | None, right: datetime | None) -> datetime | None:
    if left is None:
        return right
    if right is None:
        return left
    return min(left, right)


def _max_datetime(left: datetime | None, right: datetime | None) -> datetime | None:
    if left is None:
        return right
    if right is None:
        return left
    return max(left, right)


def _float_or_none(value: str | None) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def _format_duration(seconds: float) -> str:
    total_seconds = int(round(seconds))
    minutes, remaining_seconds = divmod(total_seconds, 60)
    if minutes:
        return f"{minutes}m{remaining_seconds}s"
    return f"{remaining_seconds}s"


def _rollout_filename_time_key(filename: str) -> str:
    match = re.search(r"rollout-(\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2})", filename)
    return match.group(1) if match else filename


def _rollout_identifier_set(rollout_file: Path) -> set[str]:
    stem = rollout_file.stem
    identifiers = {
        _normalize_match_text(stem),
    }
    if stem.startswith("rollout-"):
        identifiers.add(_normalize_match_text(stem[len("rollout-") :]))
    identifiers.update(
        _normalize_match_text(match)
        for match in re.findall(
            r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            stem,
        )
    )
    return {identifier for identifier in identifiers if identifier}


def _extract_rollout_file_from_query(query_text: str) -> Path | None:
    quoted_match = re.search(r"""["']([^"']+\.jsonl)["']""", query_text, re.IGNORECASE)
    if quoted_match:
        return Path(quoted_match.group(1)).expanduser()

    unquoted_match = re.search(r"\b((?:[A-Za-z]:)?[^\s\"']+\.jsonl)\b", query_text, re.IGNORECASE)
    if unquoted_match:
        return Path(unquoted_match.group(1)).expanduser()

    return None


def _extract_first_string_values(payload: Any, keys: set[str]) -> list[str]:
    if not isinstance(payload, dict):
        return []

    values: list[str] = []
    normalized_keys = {key.casefold() for key in keys}
    for key, value in payload.items():
        if str(key).casefold() in normalized_keys:
            if isinstance(value, str) and value.strip():
                values.append(value.strip())
            elif isinstance(value, int | float):
                values.append(str(value))
        if isinstance(value, dict):
            values.extend(_extract_first_string_values(value, keys))
    return values


def _workspace_query_from_input(workspace: str | Path | None) -> str | None:
    if workspace is None:
        return None
    return _safe_workspace_label(str(workspace))


def _extract_workspace_query(query_text: str) -> str | None:
    quoted_match = re.search(
        r"""\b(?:workspace|project)\s+(?:named\s+|called\s+)?["']([^"']+)["']""",
        query_text,
        re.IGNORECASE,
    )
    if quoted_match:
        return quoted_match.group(1).strip()

    preceding_label_match = re.search(
        r"\b([A-Za-z0-9][A-Za-z0-9_.-]{1,80})\s+(?:workspace|project|repo|repository)\b",
        query_text,
        re.IGNORECASE,
    )
    if preceding_label_match:
        return preceding_label_match.group(1).strip()

    labeled_match = re.search(
        r"\b(?:workspace|project)\s+(?:named\s+|called\s+)?([A-Za-z0-9][A-Za-z0-9_.-]{1,80})\b",
        query_text,
        re.IGNORECASE,
    )
    if labeled_match:
        return labeled_match.group(1).strip()

    uppercase_tokens = [
        token
        for token in re.findall(r"\b[A-Z][A-Z0-9_-]{2,}\b", query_text)
        if token.casefold() not in {"codex", "jsonl"}
    ]
    if uppercase_tokens:
        return uppercase_tokens[0]

    return None


def _extract_thread_title_query(query_text: str) -> str | None:
    quoted_match = re.search(
        r"""\b(?:thread\s+title|thread|titled)\s+(?:named\s+|called\s+)?["']([^"']+)["']""",
        query_text,
        re.IGNORECASE,
    )
    if quoted_match:
        return quoted_match.group(1).strip()
    return None


def _safe_workspace_label(value: str) -> str:
    cleaned = value.strip().rstrip("\\/")
    if cleaned.startswith("\\\\?\\"):
        cleaned = cleaned[4:]
    if not cleaned:
        return ""
    return re.split(r"[\\/]", cleaned)[-1]


def _safe_thread_title(value: str | None) -> str | None:
    """Accept trusted title metadata while rejecting serialized payloads."""
    if not value:
        return None
    cleaned = value.strip()
    if not cleaned or cleaned.startswith(("{", "[")):
        return None
    return cleaned


def _safe_rollout_thread_title(value: str | None) -> str | None:
    """Reject Codex rollout values that look like prompt or transcript content."""
    if not value:
        return None
    cleaned = re.sub(r"\s+", " ", value.strip())
    if not cleaned or len(cleaned) > 120 or cleaned.startswith(("{", "[")):
        return None
    unsafe_markers = (
        "transcript start",
        "approval request",
        "tool call",
        "tool result",
        "planned action",
        "raw prompt",
        "user:",
        "assistant:",
        "system:",
    )
    normalized = cleaned.casefold()
    if any(marker in normalized for marker in unsafe_markers):
        return None
    return cleaned


def _authoritative_state_title(value: str | None) -> str | None:
    """Preserve Codex state title metadata without treating it as rollout content."""
    if not value:
        return None
    cleaned = value.strip()
    if not cleaned or cleaned.startswith(("{", "[")):
        return None
    return cleaned


def _normalize_match_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value).strip()).casefold()


def _text_equal(left: str, right: str) -> bool:
    return _normalize_match_text(left) == _normalize_match_text(right)


def _text_contains(value: str, query: str) -> bool:
    normalized_value = _normalize_match_text(value)
    normalized_query = _normalize_match_text(query)
    return bool(normalized_query and normalized_query in normalized_value)


def _format_ambiguity_error(matches: list[SessionCandidate]) -> str:
    candidates = "; ".join(candidate.privacy_safe_description() for candidate in sorted(matches, key=lambda item: item.sort_key()))
    return (
        "Multiple Codex sessions matched the request. Add latest, a date, workspace, "
        f"thread title, or rollout file. Candidates: {candidates}"
    )


def _truncate(value: str, limit: int = 80) -> str:
    if len(value) <= limit:
        return value
    return f"{value[: limit - 3]}..."


def _normalize_agent(value: str) -> str:
    normalized = value.strip().replace("-", "_").replace(" ", "_").casefold()
    if normalized in {"claude", "claude_code", "claudecode"}:
        return "claude_code"
    if normalized == "codex":
        return "codex"
    raise InputResolverError(f"Unsupported agent source: {value}")


def _agent_from_query(query_text: str | None) -> str:
    if query_text and re.search(r"\bclaude(?:\s+code)?\b", query_text, re.IGNORECASE):
        return "claude_code"
    return "codex"


def _resolve_claude_home(claude_home: str | Path | None) -> Path | None:
    candidate = Path(claude_home).expanduser() if claude_home else Path.home() / ".claude"
    return candidate.resolve() if candidate.exists() else None


def _resolve_claude_usage_query(
    usage_query: UsageQuery,
    *,
    workspace: str | Path | None,
) -> ResolvedInput:
    claude_home = _resolve_claude_home(usage_query.claude_home)
    if claude_home is None:
        raise InputResolverError("Claude home could not be resolved; provide --claude-home or --transcript-file.")

    warnings = list(usage_query.warnings)
    candidates = _discover_claude_sessions(claude_home, warnings)
    context_matches = _context_matching_sessions(candidates, usage_query)
    if not context_matches:
        raise NoMatchingSessionsError(
            "No Claude Code sessions matched the request. Provide a session ID, workspace/date filter, "
            "latest selector, or transcript JSONL file."
        )

    identifiers = [*usage_query.quoted_phrases]
    explicit_identifier = _session_identifier_query(usage_query)
    if explicit_identifier:
        identifiers.append(explicit_identifier)
    for identifier in identifiers:
        matches = [
            candidate
            for candidate in context_matches
            if _candidate_matches_session_identifier(candidate, identifier)
        ]
        if len(matches) == 1:
            return _resolved_claude_candidates(
                matches,
                usage_query,
                workspace=workspace,
                claude_home=claude_home,
                warnings=warnings,
                scope_type="session",
            )
        if len(matches) > 1:
            raise _needs_clarification(
                usage_query,
                reason="More than one Claude Code transcript matched the requested session identifier.",
                sessions=matches,
            )

    if usage_query.selection_mode == "latest":
        selected = max(context_matches, key=lambda candidate: candidate.sort_key())
        scope = "workspace" if _requests_workspace_scope(usage_query) else "session"
        return _resolved_claude_candidates(
            [selected], usage_query, workspace=workspace, claude_home=claude_home,
            warnings=warnings, scope_type=scope, resolution_status="inferred",
        )

    if _requests_workspace_scope(usage_query):
        if not _has_workspace_time_intent(usage_query):
            raise _needs_clarification(
                usage_query,
                reason="Claude Code workspace targets need a date range, latest, or explicit all-time scope.",
                sessions=context_matches,
            )
        return _resolved_claude_candidates(
            context_matches, usage_query, workspace=workspace, claude_home=claude_home,
            warnings=warnings, scope_type="workspace",
        )

    if len(context_matches) == 1:
        return _resolved_claude_candidates(
            context_matches, usage_query, workspace=workspace, claude_home=claude_home,
            warnings=warnings, scope_type="session",
        )

    raise _needs_clarification(
        usage_query,
        reason="More than one Claude Code session matched the request.",
        sessions=context_matches,
    )


def _resolved_claude_candidates(
    candidates: list[SessionCandidate],
    usage_query: UsageQuery,
    *,
    workspace: str | Path | None,
    claude_home: Path,
    warnings: list[str],
    scope_type: str,
    resolution_status: str = "exact",
) -> ResolvedInput:
    selected = sorted(candidates, key=lambda candidate: candidate.sort_key())
    metadata_items = [_read_claude_transcript_metadata(item.rollout_file, warnings) for item in selected]
    source_metadata = _merge_claude_source_metadata(metadata_items)
    workspace_label = _common_workspace_label(selected)
    return ResolvedInput(
        agent="claude_code",
        scope_type=scope_type,
        rollout_files=[candidate.rollout_file for candidate in selected],
        codex_home=None,
        logs_db=None,
        state_db=None,
        workspace=_resolve_workspace_or_label(workspace, workspace_label),
        thread_title=None,
        date_range=usage_query.date_range or _date_range_from_sessions(selected),
        output_dir=_resolve_output_dir(usage_query.output_dir),
        warnings=list(dict.fromkeys(warnings)),
        resolution_status=resolution_status,
        claude_home=claude_home,
        source_metadata=source_metadata,
        session_titles=_session_titles_for_candidates(selected),
    )


def _discover_claude_sessions(claude_home: Path, warnings: list[str]) -> list[SessionCandidate]:
    """Find Claude transcript files and read only the metadata needed for resolution."""
    projects_root = claude_home if claude_home.name.casefold() == "projects" else claude_home / "projects"
    if not projects_root.exists():
        warnings.append("projects directory not found under claude_home")
        return []

    candidates: list[SessionCandidate] = []
    for transcript_file in sorted(projects_root.rglob("*.jsonl")):
        if not transcript_file.is_file():
            continue
        metadata = _read_claude_transcript_metadata(transcript_file, warnings)
        session_ids = {metadata["session_id"]} if metadata.get("session_id") else set()
        session_ids.update({transcript_file.name, transcript_file.stem})
        candidates.append(
            SessionCandidate(
                rollout_file=transcript_file.resolve(),
                session_date=metadata.get("session_date"),
                workspace_label=metadata.get("workspace_label") or transcript_file.parent.name,
                thread_title=metadata.get("thread_title"),
                modified_time=transcript_file.stat().st_mtime,
                start_time=metadata.get("start_timestamp"),
                end_time=metadata.get("end_timestamp"),
                duration_seconds=_duration_between(
                    metadata.get("start_timestamp"), metadata.get("end_timestamp")
                ),
                event_count=int(metadata.get("event_count", "0")),
                session_ids=session_ids,
            )
        )
    return _dedupe_session_candidates(candidates)


def _read_claude_transcript_metadata(path: Path, warnings: list[str]) -> dict[str, str]:
    session_ids: set[str] = set()
    workspace_labels: set[str] = set()
    branches: set[str] = set()
    timestamps: list[datetime] = []
    custom_title: str | None = None
    ai_title: str | None = None
    metadata_title: str | None = None
    event_count = 0
    try:
        with Path(path).open("r", encoding="utf-8-sig") as handle:
            for line_number, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    payload = json.loads(stripped)
                except json.JSONDecodeError:
                    warnings.append(f"Malformed Claude Code JSONL skipped in {Path(path).name} at line {line_number}")
                    continue
                if not isinstance(payload, dict):
                    continue
                event_count += 1
                payload_type = _string_or_none(payload.get("type"))
                custom_title_value = _safe_thread_title(_string_or_none(payload.get("customTitle")))
                ai_title_value = _safe_thread_title(_string_or_none(payload.get("aiTitle")))
                if custom_title_value and payload_type == "custom-title":
                    custom_title = custom_title_value
                if ai_title_value and payload_type == "ai-title":
                    ai_title = ai_title_value
                for key in (
                    "conversationTitle",
                    "conversation_title",
                    "threadTitle",
                    "thread_title",
                    "sessionTitle",
                    "session_title",
                    "chatTitle",
                    "chat_title",
                ):
                    title_value = _safe_thread_title(_string_or_none(payload.get(key)))
                    if title_value:
                        metadata_title = title_value
                for value, target in (
                    (payload.get("sessionId"), session_ids),
                    (payload.get("cwd"), workspace_labels),
                    (payload.get("gitBranch"), branches),
                ):
                    if isinstance(value, str) and value.strip():
                        target.add(value.strip())
                timestamp = payload.get("timestamp")
                if isinstance(timestamp, str):
                    parsed = _parse_datetime(timestamp)
                    if parsed is not None:
                        timestamps.append(parsed)
    except OSError:
        warnings.append(f"Claude Code transcript is not readable: {Path(path).name}")

    first = min(timestamps).isoformat().replace("+00:00", "Z") if timestamps else None
    last = max(timestamps).isoformat().replace("+00:00", "Z") if timestamps else None
    metadata: dict[str, str] = {"event_count": str(event_count)}
    thread_title = custom_title or ai_title or metadata_title
    if thread_title:
        metadata["thread_title"] = thread_title
    if len(session_ids) == 1:
        metadata["session_id"] = next(iter(session_ids))
    if len(workspace_labels) == 1:
        workspace = next(iter(workspace_labels))
        metadata["workspace_path"] = workspace
        metadata["workspace_label"] = _safe_workspace_label(workspace)
    if len(branches) == 1:
        metadata["git_branch"] = next(iter(branches))
    if first:
        metadata["start_timestamp"] = first
        metadata["session_date"] = first[:10]
    if last:
        metadata["end_timestamp"] = last
    return metadata


def _claude_source_metadata(metadata: dict[str, str]) -> dict[str, Any]:
    return {
        key: metadata[key]
        for key in ("session_id", "git_branch", "start_timestamp", "end_timestamp", "thread_title")
        if metadata.get(key)
    }


def _merge_claude_source_metadata(items: list[dict[str, str]]) -> dict[str, Any]:
    if not items:
        return {}
    result: dict[str, Any] = {"session_count": len(items)}
    for key in ("session_id", "git_branch"):
        values = {item[key] for item in items if item.get(key)}
        if len(values) == 1:
            result[key] = next(iter(values))
    starts = [item["start_timestamp"] for item in items if item.get("start_timestamp")]
    ends = [item["end_timestamp"] for item in items if item.get("end_timestamp")]
    if starts:
        result["start_timestamp"] = min(starts)
    if ends:
        result["end_timestamp"] = max(ends)
    return result


def _duration_between(start: str | None, end: str | None) -> float | None:
    if not start or not end:
        return None
    started = _parse_datetime(start)
    ended = _parse_datetime(end)
    if started is None or ended is None:
        return None
    return max(0.0, (ended - started).total_seconds())
