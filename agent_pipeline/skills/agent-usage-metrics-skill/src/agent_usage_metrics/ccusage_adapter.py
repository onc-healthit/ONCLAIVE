"""Load ccusage token and cost data and match it carefully to resolved sessions."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from .models import CcusageResult, ResolvedInput


_TOKEN_FIELD_ALIASES = {
    "input_tokens": ("inputTokens", "input_tokens", "promptTokens", "prompt_tokens"),
    "cached_input_tokens": (
        "cachedInputTokens",
        "cached_input_tokens",
        "cacheReadTokens",
        "cache_read_tokens",
    ),
    "output_tokens": ("outputTokens", "output_tokens", "completionTokens", "completion_tokens"),
    "reasoning_output_tokens": ("reasoningOutputTokens", "reasoning_output_tokens"),
    "total_tokens": ("totalTokens", "total_tokens", "tokens"),
}
_COST_FIELD_ALIASES = (
    "cost",
    "costUSD",
    "totalCost",
    "totalCostUSD",
    "total_cost",
    "estimatedCost",
    "estimated_cost",
)
_CURRENCY_FIELD_ALIASES = ("currency",)
_MODEL_FIELD_ALIASES = ("models", "modelBreakdown", "model_breakdown", "modelBreakdowns", "model_breakdowns")
_MODEL_NAME_FIELD_ALIASES = ("model", "modelName", "model_name")
_DATE_FIELD_ALIASES = ("date", "day", "startDate", "start_date", "endDate", "end_date")
_SESSION_FIELD_ALIASES = (
    "sessionId",
    "session_id",
    "session",
    "conversationId",
    "conversation_id",
    "conversation",
    "threadId",
    "thread_id",
    "rolloutId",
    "rollout_id",
)
_WORKSPACE_FIELD_ALIASES = (
    "cwd",
    "directory",
    "project",
    "projectPath",
    "project_path",
    "workspace",
    "workspacePath",
    "workspace_path",
    "workingDirectory",
    "working_directory",
)
_THREAD_FIELD_ALIASES = (
    "threadTitle",
    "thread_title",
    "title",
    "conversationTitle",
    "conversation_title",
)
_START_TIME_ALIASES = (
    "firstActivity",
    "first_activity",
    "firstMessageAt",
    "first_message_at",
    "startedAt",
    "started_at",
    "startTime",
    "start_time",
    "createdAt",
    "created_at",
    "timestamp",
    "time",
    "ts",
)
_END_TIME_ALIASES = (
    "lastActivity",
    "last_activity",
    "lastMessageAt",
    "last_message_at",
    "endedAt",
    "ended_at",
    "endTime",
    "end_time",
    "updatedAt",
    "updated_at",
    "timestamp",
    "time",
    "ts",
)
_RECORD_LIST_KEYS_BY_MODE = {
    "daily": ("daily", "days", "entries", "records", "rows", "data", "items"),
    "weekly": ("weekly", "weeks", "entries", "records", "rows", "data", "items"),
    "monthly": ("monthly", "months", "entries", "records", "rows", "data", "items"),
    "session": ("sessions", "session", "entries", "records", "rows", "data", "items"),
}
_PACKAGE_RUNTIME_WARNING = (
    "ccusage may need to be downloaded or cached by bunx/npx/pnpm; rerun with allow_download=True "
    "or install ccusage globally."
)
_SINGLE_SESSION_SCOPE_WARNING = (
    "ccusage session enrichment requires a confident match between the selected Codex rollout "
    "and a ccusage session row."
)
_SINGLE_SESSION_DAILY_DATA_WARNING = (
    "ccusage returned only day-level totals, which cannot be safely attributed to the selected "
    "session scope."
)
_STDERR_SUMMARY_LIMIT = 500
_DISCOVERY_MODES = ("daily", "weekly", "monthly", "session")
_CONFIDENCE_SCORES = {
    "exact": 5,
    "strong": 4,
    "medium": 3,
    "weak": 2,
    "weakest": 1,
}
_CONFIDENT_SESSION_SCORES = {_CONFIDENCE_SCORES["exact"], _CONFIDENCE_SCORES["strong"], _CONFIDENCE_SCORES["medium"]}
_TIME_OVERLAP_TOLERANCE = timedelta(minutes=5)


@dataclass(frozen=True)
class CcusageRuntime:
    """A usable local or package-runner command for invoking ccusage."""
    name: str
    command_prefix: list[str]
    status: str
    requires_download: bool


@dataclass(frozen=True)
class CommandCandidate:
    """One possible ccusage invocation for a runtime and requested scope."""
    mode: str
    source: str
    args: list[str]
    precision: str


@dataclass(frozen=True)
class CommandSupport:
    """Capabilities discovered from ccusage help and command probes."""
    codex_modes: set[str]
    unified_modes: set[str]
    unified_session_all: bool
    discovery_attempts: list[list[str]]
    warnings: list[str]
    unknown: bool


@dataclass(frozen=True)
class CommandFailure:
    """A failed ccusage command retained for clear unavailable-state reporting."""
    command: list[str]
    mode: str
    kind: str
    exit_code: int | None = None
    stderr: str | None = None
    error: str | None = None


@dataclass(frozen=True)
class UsageValues:
    """Token and cost fields extracted from one ccusage response or session row."""
    input_tokens: int | float | None = None
    cached_input_tokens: int | float | None = None
    output_tokens: int | float | None = None
    reasoning_output_tokens: int | float | None = None
    total_tokens: int | float | None = None
    estimated_cost: int | float | None = None
    currency: str | None = None
    model_breakdown: dict[str, Any] | None = None

    def has_token_or_cost_data(self) -> bool:
        return any(
            value is not None
            for value in (
                self.input_tokens,
                self.cached_input_tokens,
                self.output_tokens,
                self.reasoning_output_tokens,
                self.total_tokens,
                self.estimated_cost,
            )
        )


@dataclass(frozen=True)
class TargetSession:
    """Safe metadata collected from the selected rollout for ccusage matching."""
    session_ids: set[str]
    workspace_labels: set[str]
    thread_titles: set[str]
    first_activity: datetime | None
    last_activity: datetime | None
    dates: set[str]
    models: set[str]


@dataclass(frozen=True)
class SessionRow:
    """One candidate ccusage session row with normalized matching fields."""
    payload: dict[str, Any]
    index: int
    session_ids: set[str]
    workspace_labels: set[str]
    thread_titles: set[str]
    first_activity: datetime | None
    last_activity: datetime | None
    dates: set[str]
    models: set[str]


@dataclass(frozen=True)
class SessionMatch:
    """A scored candidate association between one rollout and one ccusage row."""
    row: SessionRow
    confidence: str
    score: int
    reasons: list[str]


@dataclass(frozen=True)
class SessionMatchDecision:
    """Selected match or a reason token/cost enrichment cannot be trusted."""
    match: SessionMatch | None
    status: str
    precision: str
    reason: str | None
    warnings: list[str]
    session_match: dict[str, Any]


def check_ccusage_availability(
    allow_download: bool = False,
    command_args: list[str] | None = None,
) -> tuple[CcusageRuntime | None, CcusageResult | None]:
    """Check whether ccusage can run locally or needs explicit download permission."""
    representative_args = command_args or _default_command_args("daily", source="codex")
    global_ccusage = shutil.which("ccusage")
    package_runtimes = [
        _runtime_from_executable("bunx", "available_via_bunx", ["ccusage"]),
        _runtime_from_executable("npx", "available_via_npx", ["ccusage@latest"]),
        _runtime_from_executable("pnpm", "available_via_pnpm", ["dlx", "ccusage"]),
    ]

    if global_ccusage:
        return CcusageRuntime("ccusage", [global_ccusage], "available", False), None

    if allow_download:
        for runtime in package_runtimes:
            if runtime is not None:
                return runtime, None
    else:
        for runtime in package_runtimes:
            if runtime is not None:
                return None, _empty_result(
                    status="requires_permission",
                    command=runtime.command_prefix + representative_args,
                    precision="unavailable",
                    reason="permission_required",
                    mode_attempted=_mode_from_args(representative_args),
                    command_attempts=[runtime.command_prefix + representative_args],
                    warnings=[_PACKAGE_RUNTIME_WARNING],
                )

    return None, _empty_result(
        status="node_runtime_missing",
        precision="unavailable",
        reason="ccusage_unavailable",
        warnings=["No ccusage runtime found. Install ccusage globally or make bunx, npx, or pnpm available."],
    )


def build_ccusage_command(resolved_input: ResolvedInput, runtime: CcusageRuntime) -> list[str]:
    mode = _requested_mode(resolved_input)
    return runtime.command_prefix + _default_command_args(mode, source=_ccusage_source(resolved_input))


def load_ccusage_data(
    resolved_input: ResolvedInput,
    *,
    allow_download: bool = False,
    timeout_seconds: int = 30,
) -> CcusageResult:
    """Run ccusage and return only enrichment that matches the requested scope."""
    representative_args = _default_command_args(
        _requested_mode(resolved_input), source=_ccusage_source(resolved_input)
    )
    runtime, availability_result = check_ccusage_availability(
        allow_download=allow_download,
        command_args=representative_args,
    )
    if availability_result is not None:
        return _with_scope(availability_result, resolved_input)
    if runtime is None:
        return _with_scope(
            _empty_result(
                status="unavailable",
                precision="unavailable",
                reason="ccusage_unavailable",
                warnings=["ccusage runtime could not be selected."],
            ),
            resolved_input,
        )

    support = discover_ccusage_commands(runtime, timeout_seconds=timeout_seconds)
    candidates = _command_candidates(resolved_input, runtime, support)
    attempted_commands = list(support.discovery_attempts)
    attempted_commands.extend(runtime.command_prefix + candidate.args for candidate in candidates)

    if not candidates:
        return _with_scope(
            _unsupported_command_result(
                resolved_input,
                runtime,
                support,
                attempted_commands,
            ),
            resolved_input,
        )

    failures: list[CommandFailure] = []
    for candidate in candidates:
        command = runtime.command_prefix + candidate.args
        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                check=False,
            )
        except subprocess.TimeoutExpired:
            failures.append(
                CommandFailure(
                    command=command,
                    mode=candidate.mode,
                    kind="timeout",
                    error=f"ccusage timed out after {timeout_seconds} seconds",
                )
            )
            continue
        except OSError as exc:
            failures.append(
                CommandFailure(
                    command=command,
                    mode=candidate.mode,
                    kind="start_failed",
                    error=f"ccusage failed to start: {exc.__class__.__name__}",
                )
            )
            continue

        if completed.returncode != 0:
            failures.append(
                CommandFailure(
                    command=command,
                    mode=candidate.mode,
                    kind="unsupported" if _looks_like_unsupported_command(completed.stderr) else "failed",
                    exit_code=completed.returncode,
                    stderr=completed.stderr,
                    error=f"ccusage exited with code {completed.returncode}",
                )
            )
            continue

        try:
            parsed = json.loads(completed.stdout)
        except json.JSONDecodeError:
            failures.append(
                CommandFailure(
                    command=command,
                    mode=candidate.mode,
                    kind="invalid_json",
                    error="ccusage did not return valid JSON",
                )
            )
            continue

        return parse_ccusage_json(
            parsed,
            resolved_input,
            command,
            status=runtime.status,
            mode_attempted=candidate.mode,
            precision=candidate.precision,
            command_attempts=attempted_commands,
            discovery_warnings=support.warnings,
        )

    return _with_scope(
        _failed_command_result(
            resolved_input,
            failures,
            attempted_commands,
        ),
        resolved_input,
    )


def discover_ccusage_commands(
    runtime: CcusageRuntime,
    *,
    timeout_seconds: int = 30,
) -> CommandSupport:
    """Probe supported ccusage command forms without assuming one version."""
    discovery_attempts: list[list[str]] = []
    warnings: list[str] = []
    codex_modes: set[str] = set()
    unified_modes: set[str] = set()
    meaningful_help_seen = False

    root_help = _run_help(runtime, ["--help"], timeout_seconds, discovery_attempts, warnings)
    if root_help:
        root_modes = _modes_mentioned_in_help(root_help)
        unified_modes.update(root_modes)
        meaningful_help_seen = meaningful_help_seen or bool(root_modes)

    codex_help = _run_help(runtime, ["codex", "--help"], timeout_seconds, discovery_attempts, warnings)
    if codex_help:
        codex_help_modes = _modes_mentioned_in_help(codex_help)
        codex_modes.update(codex_help_modes)
        meaningful_help_seen = meaningful_help_seen or bool(codex_help_modes)

    session_help = _run_help(runtime, ["session", "--help"], timeout_seconds, discovery_attempts, warnings)
    unified_session_all = True
    if session_help:
        unified_session_all = "--all" in session_help
        if "session" in _modes_mentioned_in_help(session_help) or "usage by session" in session_help.casefold():
            unified_modes.add("session")
            meaningful_help_seen = True

    return CommandSupport(
        codex_modes=codex_modes,
        unified_modes=unified_modes,
        unified_session_all=unified_session_all,
        discovery_attempts=discovery_attempts,
        warnings=warnings,
        unknown=not meaningful_help_seen,
    )


def parse_ccusage_json(
    data: Any,
    resolved_input: ResolvedInput,
    command_used: list[str] | None,
    *,
    status: str = "available",
    mode_attempted: str | None = None,
    precision: str | None = None,
    command_attempts: list[list[str]] | None = None,
    discovery_warnings: list[str] | None = None,
) -> CcusageResult:
    """Parse ccusage output while preserving unavailable or unsupported states."""
    mode = mode_attempted or _mode_from_command(command_used) or _mode_from_data(data) or "daily"
    requested_precision = precision or _precision_for_scope(resolved_input, mode)
    scope_returned = _scope_returned(data, command_used, mode, requested_precision)
    warnings = [*_scope_warnings(resolved_input), *list(discovery_warnings or [])]

    if _is_session_scope(resolved_input):
        if mode != "session":
            if _aggregate_has_usage_data(data):
                warnings.append(_SINGLE_SESSION_DAILY_DATA_WARNING)
            return _empty_result(
                status="only_day_level_available" if mode == "daily" else "no_confident_match",
                command=command_used,
                scope_requested=_scope_requested(resolved_input),
                scope_returned=scope_returned,
                precision="day_level" if mode == "daily" else "no_confident_match",
                reason="only_day_level_output_available" if mode == "daily" else "session_mode_not_returned",
                mode_attempted=mode,
                command_attempts=command_attempts,
                raw_summary=_raw_summary(data),
                warnings=warnings,
            )
        return _parse_session_json(
            data,
            resolved_input,
            command_used,
            status,
            scope_returned,
            warnings,
            command_attempts,
        )

    if _is_multi_session_scope(resolved_input):
        if mode != "session":
            if _aggregate_has_usage_data(data):
                warnings.append(
                    "ccusage returned aggregate/day-level totals, which cannot be safely attributed to the selected "
                    f"{resolved_input.scope_type} sessions."
                )
            return _empty_result(
                status="only_day_level_available" if mode == "daily" else "no_confident_match",
                command=command_used,
                scope_requested=_scope_requested(resolved_input),
                scope_returned=scope_returned,
                precision="day_level" if mode == "daily" else "no_confident_match",
                reason="only_day_level_output_available" if mode == "daily" else "session_mode_not_returned",
                mode_attempted=mode,
                command_attempts=command_attempts,
                raw_summary=_raw_summary(data),
                warnings=warnings,
            )
        return _parse_multi_session_json(
            data,
            resolved_input,
            command_used,
            status,
            scope_returned,
            warnings,
            command_attempts,
        )

    values, value_status, value_warning = _usage_values_for_non_session_scope(data, resolved_input, mode)
    if value_warning:
        warnings.append(value_warning)
    if not values.has_token_or_cost_data():
        return _empty_result(
            status=value_status or "parser_unsupported_output_shape",
            command=command_used,
            scope_requested=_scope_requested(resolved_input),
            scope_returned=scope_returned,
            precision="failed" if value_status == "parser_unsupported_output_shape" else requested_precision,
            reason=value_status or "parser_unsupported_output_shape",
            mode_attempted=mode,
            command_attempts=command_attempts,
            raw_summary=_raw_summary(data),
            warnings=warnings or ["ccusage JSON did not contain recognized token or cost fields."],
        )

    result_status = status
    if _scope_mismatch(resolved_input, scope_returned):
        warnings.append("ccusage returned scope does not match the requested date range.")
        result_status = "scope_mismatch"

    return _result_from_values(
        values,
        status=result_status,
        command=command_used,
        scope_requested=_scope_requested(resolved_input),
        scope_returned=scope_returned,
        raw_summary=_raw_summary(data),
        warnings=warnings,
        precision=requested_precision,
        reason=None,
        mode_attempted=mode,
        command_attempts=command_attempts,
    )


def summarize_ccusage_result(result: CcusageResult) -> dict[str, Any]:
    return {
        "status": result.status,
        "precision": result.precision,
        "reason": result.reason,
        "mode_attempted": result.mode_attempted,
        "command": result.command,
        "command_attempts": result.command_attempts,
        "scope_requested": result.scope_requested,
        "scope_returned": result.scope_returned,
        "session_match": _strip_match_diagnostics(result.session_match),
        "input_tokens": result.input_tokens,
        "cached_input_tokens": result.cached_input_tokens,
        "output_tokens": result.output_tokens,
        "reasoning_output_tokens": result.reasoning_output_tokens,
        "total_tokens": result.total_tokens,
        "estimated_cost": result.estimated_cost,
        "currency": result.currency,
        "model_breakdown": result.model_breakdown,
        "raw_summary": result.raw_summary,
        "warnings": list(result.warnings),
        "errors": list(result.errors),
    }


def summarize_ccusage_match_diagnostics(result: CcusageResult) -> dict[str, Any]:
    summary = summarize_ccusage_result(result)
    match = result.session_match
    if isinstance(match, dict):
        summary["session_match"] = match
        summary["match_diagnostics"] = match.get("diagnostics")
    else:
        summary["match_diagnostics"] = None
    return summary


def _parse_session_json(
    data: Any,
    resolved_input: ResolvedInput,
    command_used: list[str] | None,
    status: str,
    scope_returned: dict[str, Any] | None,
    warnings: list[str],
    command_attempts: list[list[str]] | None,
) -> CcusageResult:
    """Match a selected rollout to a ccusage session before accepting token values."""
    rows = _extract_session_rows(data)
    if not rows:
        warnings.append("ccusage session output did not contain recognizable session rows.")
        return _empty_result(
            status="parser_unsupported_output_shape",
            command=command_used,
            scope_requested=_scope_requested(resolved_input),
            scope_returned=scope_returned,
            precision="failed",
            reason="parser_unsupported_output_shape",
            mode_attempted="session",
            command_attempts=command_attempts,
            raw_summary=_raw_summary(data),
            warnings=warnings,
        )

    target = _target_session(resolved_input)
    decision = _select_session_match(target, rows, agent=resolved_input.agent)
    warnings.extend(decision.warnings)
    if decision.match is None:
        return _empty_result(
            status=decision.status,
            command=command_used,
            scope_requested=_scope_requested(resolved_input),
            scope_returned=scope_returned,
            precision=decision.precision,
            reason=decision.reason,
            mode_attempted="session",
            command_attempts=command_attempts,
            raw_summary=_raw_summary(data),
            warnings=warnings,
            session_match=decision.session_match,
        )

    match = decision.match
    values = _usage_values(match.row.payload)
    if not values.has_token_or_cost_data():
        warnings.append("Matched ccusage session row did not contain recognized token or cost fields.")
        return _empty_result(
            status="parser_unsupported_output_shape",
            command=command_used,
            scope_requested=_scope_requested(resolved_input),
            scope_returned=scope_returned,
            precision="failed",
            reason="parser_unsupported_output_shape",
            mode_attempted="session",
            command_attempts=command_attempts,
            raw_summary=_raw_summary(data),
            warnings=warnings,
            session_match=decision.session_match,
        )
    warnings.extend(_estimated_cost_warnings(values))

    return _result_from_values(
        values,
        status=status,
        command=command_used,
        scope_requested=_scope_requested(resolved_input),
        scope_returned=scope_returned,
        raw_summary=_raw_summary(data),
        warnings=warnings,
        precision="exact_session",
        reason=_estimated_cost_reason(values),
        mode_attempted="session",
        command_attempts=command_attempts,
        session_match=decision.session_match,
    )


def _parse_multi_session_json(
    data: Any,
    resolved_input: ResolvedInput,
    command_used: list[str] | None,
    status: str,
    scope_returned: dict[str, Any] | None,
    warnings: list[str],
    command_attempts: list[list[str]] | None,
) -> CcusageResult:
    """Match each resolved session independently before summing enrichment."""
    rows = _extract_session_rows(data)
    scope = resolved_input.scope_type.casefold()
    if not rows:
        warnings.append("ccusage session output did not contain recognizable session rows.")
        return _empty_result(
            status="parser_unsupported_output_shape",
            command=command_used,
            scope_requested=_scope_requested(resolved_input),
            scope_returned=scope_returned,
            precision="failed",
            reason="parser_unsupported_output_shape",
            mode_attempted="session",
            command_attempts=command_attempts,
            raw_summary=_raw_summary(data),
            warnings=warnings,
            session_match={
                "requested_session_count": len(resolved_input.rollout_files),
                "matched_session_count": 0,
                "sessions": [],
            },
        )

    matched_records: list[dict[str, Any]] = []
    session_details: list[dict[str, Any]] = []
    used_row_indices: set[int] = set()

    for rollout_file in resolved_input.rollout_files:
        session_input = _single_session_resolved_input(resolved_input, rollout_file)
        decision = _select_session_match(
            _target_session(session_input), rows, agent=resolved_input.agent
        )
        detail = _session_detail_from_decision(rollout_file, decision)
        warnings.extend(decision.warnings)

        if decision.match is not None and decision.match.row.index in used_row_indices:
            detail.update(
                {
                    "status": "ambiguous_match",
                    "precision": "no_confident_match",
                    "reason": "duplicate_session_match",
                    "input_tokens": None,
                    "output_tokens": None,
                    "estimated_cost": None,
                }
            )
            warnings.append(
                f"ccusage row for {Path(rollout_file).name} was already matched to another rollout; "
                "token/cost metrics for that session were left missing to avoid double-counting."
            )
            session_details.append(detail)
            continue

        if decision.match is None:
            session_details.append(detail)
            continue

        values = _usage_values(decision.match.row.payload)
        if not values.has_token_or_cost_data():
            detail.update(
                {
                    "status": "parser_unsupported_output_shape",
                    "precision": "failed",
                    "reason": "parser_unsupported_output_shape",
                    "input_tokens": None,
                    "output_tokens": None,
                    "estimated_cost": None,
                }
            )
            warnings.append(f"Matched ccusage session row for {Path(rollout_file).name} did not contain token or cost fields.")
            session_details.append(detail)
            continue

        used_row_indices.add(decision.match.row.index)
        matched_records.append(decision.match.row.payload)
        detail.update(_usage_detail(values))
        warnings.extend(_estimated_cost_warnings(values, rollout_file=rollout_file))
        session_details.append(detail)

    requested_count = len(resolved_input.rollout_files)
    matched_count = len(matched_records)
    session_match = {
        "requested_session_count": requested_count,
        "matched_session_count": matched_count,
        "unmatched_session_count": requested_count - matched_count,
        "scope_type": scope,
        "sessions": session_details,
    }

    if matched_count == 0:
        warnings.append(
            f"ccusage matched 0 of {requested_count} {scope} sessions; token/cost metrics are missing."
        )
        return _empty_result(
            status="no_confident_match",
            command=command_used,
            scope_requested=_scope_requested(resolved_input),
            scope_returned=scope_returned,
            precision="no_confident_match",
            reason="no_confident_session_matches",
            mode_attempted="session",
            command_attempts=command_attempts,
            raw_summary=_raw_summary(data),
            warnings=warnings,
            session_match=session_match,
        )

    values = _sum_usage_values(matched_records)
    if not values.has_token_or_cost_data():
        warnings.append("Matched ccusage session rows did not contain recognized token or cost fields.")
        return _empty_result(
            status="parser_unsupported_output_shape",
            command=command_used,
            scope_requested=_scope_requested(resolved_input),
            scope_returned=scope_returned,
            precision="failed",
            reason="parser_unsupported_output_shape",
            mode_attempted="session",
            command_attempts=command_attempts,
            raw_summary=_raw_summary(data),
            warnings=warnings,
            session_match=session_match,
        )
    warnings.extend(_estimated_cost_warnings(values))

    if matched_count < requested_count:
        warnings.append(
            f"ccusage matched {matched_count} of {requested_count} {scope} sessions; token/cost metrics are partial."
        )
        result_status = "partial"
        result_precision = f"partial_{scope}"
        reason = "partial_session_matches"
    else:
        result_status = "success" if status.startswith("available") else status
        result_precision = f"exact_{scope}"
        reason = None
    reason = reason or _estimated_cost_reason(values)

    return _result_from_values(
        values,
        status=result_status,
        command=command_used,
        scope_requested=_scope_requested(resolved_input),
        scope_returned=scope_returned,
        raw_summary=_raw_summary(data),
        warnings=warnings,
        precision=result_precision,
        reason=reason,
        mode_attempted="session",
        command_attempts=command_attempts,
        session_match=session_match,
    )


def _usage_values_for_non_session_scope(
    data: Any,
    resolved_input: ResolvedInput,
    mode: str,
) -> tuple[UsageValues, str | None, str | None]:
    """Use aggregate ccusage data only when it represents the requested broader scope."""
    aggregate_values = _usage_values(data)
    if _preferred_total_containers(data) and aggregate_values.has_token_or_cost_data():
        return aggregate_values, None, None

    records = _records_for_mode(data, mode)
    if mode == "daily" and resolved_input.date_range and records:
        start, end = resolved_input.date_range
        filtered = [
            record
            for record in records
            if (record_date := _record_date(record)) is not None and start <= record_date <= end
        ]
        if filtered:
            filtered_values = _sum_usage_values(filtered)
            if filtered_values.has_token_or_cost_data():
                return filtered_values, None, None
            if aggregate_values.has_token_or_cost_data():
                return aggregate_values, None, None
        return (
            UsageValues(),
            "scope_mismatch",
            "ccusage daily output did not include rows in the requested date range.",
        )

    if records:
        values = _sum_usage_values(records)
        if values.has_token_or_cost_data():
            return values, None, None

    if aggregate_values.has_token_or_cost_data():
        return aggregate_values, None, None
    return UsageValues(), "parser_unsupported_output_shape", "ccusage JSON did not contain recognized token or cost fields."


def _command_candidates(
    resolved_input: ResolvedInput,
    runtime: CcusageRuntime,
    support: CommandSupport,
) -> list[CommandCandidate]:
    del runtime
    mode = _requested_mode(resolved_input)
    precision = _precision_for_scope(resolved_input, mode)
    candidates: list[CommandCandidate] = []

    source = _ccusage_source(resolved_input)
    if source == "codex" and (support.unknown or mode in support.codex_modes):
        candidates.append(
            CommandCandidate(
                mode=mode,
                source="codex",
                args=_default_command_args(mode, source="codex"),
                precision=precision,
            )
        )

    if support.unknown or mode in support.unified_modes:
        candidates.append(
            CommandCandidate(
                mode=mode,
                source="unified",
                args=_default_command_args(
                    mode,
                    source="unified",
                    unified_session_all=support.unified_session_all,
                ),
                precision=precision,
            )
        )

    return _dedupe_candidates(candidates)


def _ccusage_source(resolved_input: ResolvedInput) -> str:
    return "unified" if resolved_input.agent == "claude_code" else "codex"


def _default_command_args(
    mode: str,
    *,
    source: str,
    unified_session_all: bool = True,
) -> list[str]:
    if source == "codex":
        return ["codex", mode, "--json", "--offline"]
    if mode == "session" and unified_session_all:
        return ["session", "--all", "--json", "--offline"]
    return [mode, "--json", "--offline"]


def _is_session_scope(resolved_input: ResolvedInput) -> bool:
    return resolved_input.scope_type.casefold() in {"session", "single_session"}


def _is_multi_session_scope(resolved_input: ResolvedInput) -> bool:
    return resolved_input.scope_type.casefold() in {"conversation", "workspace"}


def _is_conversation_scope(resolved_input: ResolvedInput) -> bool:
    return resolved_input.scope_type.casefold() == "conversation"


def _is_workspace_scope(resolved_input: ResolvedInput) -> bool:
    return resolved_input.scope_type.casefold() == "workspace"


def _requested_mode(resolved_input: ResolvedInput) -> str:
    scope = resolved_input.scope_type.casefold()
    if scope in {"session", "single_session", "conversation", "workspace"}:
        return "session"
    if "week" in scope:
        return "weekly"
    if "month" in scope:
        return "monthly"
    return "daily"


def _precision_for_scope(resolved_input: ResolvedInput, mode: str) -> str:
    if _is_session_scope(resolved_input) and mode == "session":
        return "exact_session"
    if _is_conversation_scope(resolved_input) and mode == "session":
        return "exact_conversation"
    if _is_workspace_scope(resolved_input) and mode == "session":
        return "exact_workspace"
    if mode == "weekly":
        return "week_level"
    if mode == "monthly":
        return "month_level"
    if mode == "daily":
        if resolved_input.date_range and resolved_input.date_range[0] != resolved_input.date_range[1]:
            return "date_range"
        if resolved_input.scope_type == "date_range":
            return "date_range"
        return "day_level"
    return "unavailable"


def _runtime_from_executable(
    executable_name: str,
    status: str,
    arguments: list[str],
) -> CcusageRuntime | None:
    executable = shutil.which(executable_name)
    if not executable:
        return None
    return CcusageRuntime(
        name=executable_name,
        command_prefix=[executable, *arguments],
        status=status,
        requires_download=True,
    )


def _run_help(
    runtime: CcusageRuntime,
    args: list[str],
    timeout_seconds: int,
    discovery_attempts: list[list[str]],
    warnings: list[str],
) -> str | None:
    command = runtime.command_prefix + args
    discovery_attempts.append(command)
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        warnings.append(f"ccusage command discovery failed for {_command_shape(command)}: {exc.__class__.__name__}")
        return None
    if completed.returncode != 0:
        stderr_summary = _safe_process_output_summary(completed.stderr)
        warning = f"ccusage command discovery failed for {_command_shape(command)} with exit code {completed.returncode}"
        if stderr_summary:
            warning = f"{warning}: {stderr_summary}"
        warnings.append(warning)
        return None
    return "\n".join(part for part in (completed.stdout, completed.stderr) if part)


def _modes_mentioned_in_help(help_text: str) -> set[str]:
    normalized = help_text.casefold()
    if not any(word in normalized for word in ("usage", "commands", "subcommands", "ccusage")):
        return set()
    return {mode for mode in _DISCOVERY_MODES if re.search(rf"\b{re.escape(mode)}\b", normalized)}


def _unsupported_command_result(
    resolved_input: ResolvedInput,
    runtime: CcusageRuntime,
    support: CommandSupport,
    attempted_commands: list[list[str]],
) -> CcusageResult:
    mode = _requested_mode(resolved_input)
    warnings = [
        *_scope_warnings(resolved_input),
        *support.warnings,
        f"ccusage command unsupported for requested mode: {mode}",
    ]
    if (_is_session_scope(resolved_input) or _is_multi_session_scope(resolved_input)) and (
        "daily" in support.codex_modes or "daily" in support.unified_modes
    ):
        warnings.append(_daily_data_warning(resolved_input))
        return _empty_result(
            status="only_day_level_available",
            command=None,
            scope_requested=_scope_requested(resolved_input),
            precision="day_level",
            reason="only_day_level_output_available",
            mode_attempted="session",
            command_attempts=attempted_commands,
            warnings=warnings,
        )

    return _empty_result(
        status="unsupported_command",
        scope_requested=_scope_requested(resolved_input),
        precision="unavailable",
        reason="command_unsupported",
        mode_attempted=mode,
        command_attempts=attempted_commands,
        warnings=warnings,
    )


def _failed_command_result(
    resolved_input: ResolvedInput,
    failures: list[CommandFailure],
    attempted_commands: list[list[str]],
) -> CcusageResult:
    mode = _requested_mode(resolved_input)
    unsupported_only = bool(failures) and all(failure.kind == "unsupported" for failure in failures)
    invalid_json_only = bool(failures) and all(failure.kind == "invalid_json" for failure in failures)
    status = "unsupported_command" if unsupported_only else "invalid_json" if invalid_json_only else "failed"
    reason = "command_unsupported" if unsupported_only else "parser_unsupported_output_shape" if invalid_json_only else "command_failed"
    primary = failures[-1] if failures else None
    command = primary.command if primary else None
    warnings = [*_scope_warnings(resolved_input)]
    errors: list[str] = []

    for failure in failures:
        warnings.extend(_failure_warnings(resolved_input, failure.command, failure.mode, failure.exit_code, failure.stderr))
        if failure.error:
            errors.append(failure.error)

    return _empty_result(
        status=status,
        command=command,
        scope_requested=_scope_requested(resolved_input),
        precision="failed" if status in {"failed", "invalid_json"} else "unavailable",
        reason=reason,
        mode_attempted=mode,
        command_attempts=attempted_commands,
        warnings=_dedupe(warnings),
        errors=_dedupe(errors),
    )


def _result_from_values(
    values: UsageValues,
    *,
    status: str,
    command: list[str] | None,
    scope_requested: dict[str, Any] | None,
    scope_returned: dict[str, Any] | None,
    raw_summary: dict[str, Any] | None,
    warnings: list[str],
    precision: str,
    reason: str | None,
    mode_attempted: str | None,
    command_attempts: list[list[str]] | None,
    session_match: dict[str, Any] | None = None,
) -> CcusageResult:
    return CcusageResult(
        status=status,
        command=command,
        scope_requested=scope_requested,
        scope_returned=scope_returned,
        input_tokens=_to_int(values.input_tokens),
        cached_input_tokens=_to_int(values.cached_input_tokens),
        output_tokens=_to_int(values.output_tokens),
        reasoning_output_tokens=_to_int(values.reasoning_output_tokens),
        total_tokens=_to_int(values.total_tokens),
        estimated_cost=_to_float(values.estimated_cost),
        currency=values.currency,
        model_breakdown=_safe_model_breakdown(values.model_breakdown),
        raw_summary=raw_summary,
        warnings=_dedupe(warnings),
        errors=[],
        precision=precision,
        reason=reason,
        mode_attempted=mode_attempted,
        command_attempts=list(command_attempts or ([] if command is None else [command])),
        session_match=session_match,
    )


def _empty_result(
    *,
    status: str,
    command: list[str] | None = None,
    scope_requested: dict[str, Any] | None = None,
    scope_returned: dict[str, Any] | None = None,
    precision: str = "unavailable",
    reason: str | None = None,
    mode_attempted: str | None = None,
    command_attempts: list[list[str]] | None = None,
    raw_summary: dict[str, Any] | None = None,
    warnings: list[str] | None = None,
    errors: list[str] | None = None,
    session_match: dict[str, Any] | None = None,
) -> CcusageResult:
    return CcusageResult(
        status=status,
        command=command,
        scope_requested=scope_requested,
        scope_returned=scope_returned,
        input_tokens=None,
        cached_input_tokens=None,
        output_tokens=None,
        reasoning_output_tokens=None,
        total_tokens=None,
        estimated_cost=None,
        currency=None,
        model_breakdown=None,
        raw_summary=raw_summary,
        warnings=_dedupe(list(warnings or [])),
        errors=_dedupe(list(errors or [])),
        precision=precision,
        reason=reason,
        mode_attempted=mode_attempted,
        command_attempts=list(command_attempts or ([] if command is None else [command])),
        session_match=session_match,
    )


def _with_scope(result: CcusageResult, resolved_input: ResolvedInput) -> CcusageResult:
    return CcusageResult(
        status=result.status,
        command=result.command,
        scope_requested=result.scope_requested or _scope_requested(resolved_input),
        scope_returned=result.scope_returned,
        input_tokens=result.input_tokens,
        cached_input_tokens=result.cached_input_tokens,
        output_tokens=result.output_tokens,
        reasoning_output_tokens=result.reasoning_output_tokens,
        total_tokens=result.total_tokens,
        estimated_cost=result.estimated_cost,
        currency=result.currency,
        model_breakdown=result.model_breakdown,
        raw_summary=result.raw_summary,
        warnings=_dedupe([*result.warnings, *_scope_warnings(resolved_input)]),
        errors=list(result.errors),
        precision=result.precision,
        reason=result.reason,
        mode_attempted=result.mode_attempted,
        command_attempts=list(result.command_attempts),
        session_match=result.session_match,
    )


def _scope_requested(resolved_input: ResolvedInput) -> dict[str, Any]:
    return {
        "agent": resolved_input.agent,
        "scope_type": resolved_input.scope_type,
        "date_range": list(resolved_input.date_range) if resolved_input.date_range else None,
        "rollout_file_count": len(resolved_input.rollout_files),
    }


def _scope_warnings(resolved_input: ResolvedInput) -> list[str]:
    if _is_session_scope(resolved_input):
        if resolved_input.agent == "claude_code":
            return [
                "ccusage session enrichment requires a confident match between the selected Claude Code transcript "
                "and a ccusage session row."
            ]
        return [_SINGLE_SESSION_SCOPE_WARNING]
    return []


def _daily_data_warning(resolved_input: ResolvedInput) -> str:
    if _is_session_scope(resolved_input):
        return _SINGLE_SESSION_DAILY_DATA_WARNING
    return (
        "ccusage returned only aggregate/day-level totals, which cannot be safely attributed "
        f"to the selected {resolved_input.scope_type} sessions."
    )


def _scope_returned(
    data: Any,
    command_used: list[str] | None = None,
    mode: str | None = None,
    precision: str | None = None,
) -> dict[str, Any] | None:
    dates = _find_all_strings(data, _DATE_FIELD_ALIASES)
    sessions = _find_all_strings(data, _SESSION_FIELD_ALIASES)
    returned_mode = mode or _mode_from_command(command_used) or _mode_from_data(data) or ("session" if sessions else "daily")
    scope: dict[str, Any] = {"mode": returned_mode}
    if precision:
        scope["precision"] = precision
    if dates:
        normalized_dates = [date for value in dates if (date := _normalize_iso_date(value))]
        scope["dates"] = sorted(set(normalized_dates or dates))
    if sessions:
        scope["sessions"] = sorted(set(sessions))
    return scope


def _scope_mismatch(resolved_input: ResolvedInput, scope_returned: dict[str, Any] | None) -> bool:
    if not resolved_input.date_range or not scope_returned:
        return False
    returned_dates = scope_returned.get("dates")
    if not isinstance(returned_dates, list) or not returned_dates:
        return False
    requested_start, requested_end = resolved_input.date_range
    return not any(requested_start <= str(date) <= requested_end for date in returned_dates)


def _usage_values(data: Any) -> UsageValues:
    token_values = {
        field_name: _find_first_number(data, aliases)
        for field_name, aliases in _TOKEN_FIELD_ALIASES.items()
    }
    model_breakdown = _find_first_dict(data, _MODEL_FIELD_ALIASES)
    if model_breakdown is None:
        model_names = _normalized_strings(_find_all_strings(data, _MODEL_NAME_FIELD_ALIASES))
        if model_names:
            model_breakdown = {model_name: {} for model_name in sorted(model_names)}
    return UsageValues(
        input_tokens=token_values["input_tokens"],
        cached_input_tokens=token_values["cached_input_tokens"],
        output_tokens=token_values["output_tokens"],
        reasoning_output_tokens=token_values["reasoning_output_tokens"],
        total_tokens=token_values["total_tokens"],
        estimated_cost=_find_first_number(data, _COST_FIELD_ALIASES),
        currency=_find_first_string(data, _CURRENCY_FIELD_ALIASES),
        model_breakdown=model_breakdown,
    )


def _sum_usage_values(records: list[dict[str, Any]]) -> UsageValues:
    values = [_usage_values(record) for record in records]

    def sum_field(name: str) -> int | float | None:
        found = [getattr(value, name) for value in values if getattr(value, name) is not None]
        if not found:
            return None
        return sum(found)

    currency = next((value.currency for value in values if value.currency), None)
    model_breakdown = next((value.model_breakdown for value in values if value.model_breakdown), None)
    return UsageValues(
        input_tokens=sum_field("input_tokens"),
        cached_input_tokens=sum_field("cached_input_tokens"),
        output_tokens=sum_field("output_tokens"),
        reasoning_output_tokens=sum_field("reasoning_output_tokens"),
        total_tokens=sum_field("total_tokens"),
        estimated_cost=sum_field("estimated_cost"),
        currency=currency,
        model_breakdown=model_breakdown,
    )


def _records_for_mode(data: Any, mode: str) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if not isinstance(data, dict):
        return []
    for key in _RECORD_LIST_KEYS_BY_MODE.get(mode, ("entries", "records", "rows")):
        value = data.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    return []


def _record_date(record: dict[str, Any]) -> str | None:
    for value in _find_all_strings(record, _DATE_FIELD_ALIASES):
        normalized = _normalize_iso_date(value)
        if normalized:
            return normalized
    return None


def _aggregate_has_usage_data(data: Any) -> bool:
    return _usage_values(data).has_token_or_cost_data()


def _extract_session_rows(data: Any) -> list[SessionRow]:
    records = _records_for_mode(data, "session")
    if not records and isinstance(data, dict) and (_has_session_metadata(data) or _usage_values(data).has_token_or_cost_data()):
        records = [data]

    rows: list[SessionRow] = []
    for index, record in enumerate(records):
        rows.append(
            SessionRow(
                payload=record,
                index=index,
                session_ids=_ccusage_session_id_aliases(_find_all_strings(record, _SESSION_FIELD_ALIASES)),
                workspace_labels=_workspace_labels(_find_all_strings(record, _WORKSPACE_FIELD_ALIASES)),
                thread_titles=_normalized_strings(_find_all_strings(record, _THREAD_FIELD_ALIASES)),
                first_activity=_first_datetime(record, _START_TIME_ALIASES),
                last_activity=_first_datetime(record, _END_TIME_ALIASES),
                dates=_record_dates(record),
                models=_normalized_strings(_find_all_strings(record, _MODEL_NAME_FIELD_ALIASES)),
            )
        )
    return rows


def _target_session(resolved_input: ResolvedInput) -> TargetSession:
    session_ids: set[str] = set()
    workspace_labels = _workspace_labels([str(resolved_input.workspace)] if resolved_input.workspace else [])
    thread_titles = _normalized_strings([resolved_input.thread_title] if resolved_input.thread_title else [])
    dates: set[str] = set(resolved_input.date_range or ())
    models: set[str] = set()
    first_activity: datetime | None = None
    last_activity: datetime | None = None

    for rollout_file in resolved_input.rollout_files:
        session_ids.update(_session_ids_from_rollout_name(rollout_file))
        rollout_metadata = _rollout_session_metadata(rollout_file)
        if resolved_input.agent == "claude_code":
            session_ids.update(rollout_metadata["session_ids"])
        workspace_labels.update(rollout_metadata["workspace_labels"])
        thread_titles.update(rollout_metadata["thread_titles"])
        dates.update(rollout_metadata["dates"])
        models.update(rollout_metadata["models"])
        first_activity = _min_datetime(first_activity, rollout_metadata["first_activity"])
        last_activity = _max_datetime(last_activity, rollout_metadata["last_activity"])

    return TargetSession(
        session_ids=session_ids,
        workspace_labels=workspace_labels,
        thread_titles=thread_titles,
        first_activity=first_activity,
        last_activity=last_activity,
        dates={date for date in dates if _normalize_iso_date(date)},
        models=models,
    )


def _rollout_session_metadata(rollout_file: Path) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "session_ids": set(),
        "workspace_labels": set(),
        "thread_titles": set(),
        "dates": set(),
        "models": set(),
        "first_activity": None,
        "last_activity": None,
    }
    path = Path(rollout_file)
    if not path.exists() or not path.is_file():
        return metadata
    try:
        with path.open("r", encoding="utf-8-sig") as handle:
            for line in handle:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    payload = json.loads(stripped)
                except json.JSONDecodeError:
                    continue
                metadata["session_ids"].update(_normalized_strings(_find_all_strings(payload, _SESSION_FIELD_ALIASES)))
                metadata["workspace_labels"].update(_workspace_labels(_find_all_strings(payload, _WORKSPACE_FIELD_ALIASES)))
                metadata["thread_titles"].update(_normalized_strings(_find_all_strings(payload, _THREAD_FIELD_ALIASES)))
                metadata["dates"].update(_record_dates(payload))
                metadata["models"].update(
                    _normalized_strings(_find_all_strings(payload, _MODEL_NAME_FIELD_ALIASES))
                )
                timestamp = _first_datetime(payload, _START_TIME_ALIASES)
                metadata["first_activity"] = _min_datetime(metadata["first_activity"], timestamp)
                metadata["last_activity"] = _max_datetime(metadata["last_activity"], timestamp)
    except OSError:
        return metadata
    return metadata


def _session_ids_from_rollout_name(rollout_file: Path) -> set[str]:
    path = Path(rollout_file)
    candidates = {path.name, path.stem}
    return _normalized_strings(candidates)


def _ccusage_session_id_aliases(values: list[str]) -> set[str]:
    aliases: set[str] = set()
    for value in values:
        text = str(value).strip()
        if not text:
            continue
        aliases.add(text)
        basename = _path_like_basename(text)
        if basename and (_is_rollout_shaped_identifier(basename) or Path(basename).suffix.casefold() == ".jsonl"):
            aliases.add(basename)
            aliases.add(Path(basename).stem)
        elif _has_extension(text) and _is_rollout_shaped_identifier(Path(text).name):
            aliases.add(Path(text).stem)
    return _normalized_strings(aliases)


def _path_like_basename(value: str) -> str | None:
    if "/" not in value and "\\" not in value:
        return None
    parts = re.split(r"[\\/]+", value.strip().rstrip("\\/"))
    return parts[-1] if parts else None


def _has_extension(value: str) -> bool:
    return bool(Path(value).suffix)


def _is_rollout_shaped_identifier(value: str) -> bool:
    name = Path(value).name.casefold()
    stem = Path(name).stem
    return stem.startswith("rollout-")


def _match_session_row(target: TargetSession, row: SessionRow) -> SessionMatch | None:
    """Score agreement across identifiers, context, and activity time for one row."""
    if target.session_ids and row.session_ids and target.session_ids.intersection(row.session_ids):
        return SessionMatch(row=row, confidence="exact", score=_CONFIDENCE_SCORES["exact"], reasons=["exact session id"])

    workspace_match = bool(target.workspace_labels and row.workspace_labels and target.workspace_labels.intersection(row.workspace_labels))
    thread_match = bool(target.thread_titles and row.thread_titles and target.thread_titles.intersection(row.thread_titles))
    time_overlap = _activity_overlaps(target.first_activity, target.last_activity, row.first_activity, row.last_activity)
    same_day = bool(target.dates and row.dates and target.dates.intersection(row.dates))
    model_match = bool(target.models and row.models and target.models.intersection(row.models))

    if workspace_match and time_overlap:
        return SessionMatch(row=row, confidence="strong", score=_CONFIDENCE_SCORES["strong"], reasons=["workspace and activity time overlap"])
    if thread_match and time_overlap:
        return SessionMatch(row=row, confidence="medium", score=_CONFIDENCE_SCORES["medium"], reasons=["thread metadata and activity time overlap"])
    if model_match and time_overlap:
        return SessionMatch(row=row, confidence="medium", score=_CONFIDENCE_SCORES["medium"], reasons=["model and activity time overlap"])
    if time_overlap:
        return SessionMatch(row=row, confidence="weak", score=_CONFIDENCE_SCORES["weak"], reasons=["activity time overlap only"])
    if same_day:
        return SessionMatch(row=row, confidence="weakest", score=_CONFIDENCE_SCORES["weakest"], reasons=["same day only"])
    return None


def _select_session_match(
    target: TargetSession,
    rows: list[SessionRow],
    *,
    agent: str = "codex",
) -> SessionMatchDecision:
    """Accept only a clearly best candidate; ties and weak evidence stay ambiguous."""
    source_label = "Claude Code transcript" if agent == "claude_code" else "Codex rollout"
    matches = [_match_session_row(target, row) for row in rows]
    matches = [match for match in matches if match is not None]
    if not matches:
        return SessionMatchDecision(
            match=None,
            status="no_confident_match",
            precision="no_confident_match",
            reason="no_confident_session_match",
            warnings=[
                f"No ccusage session row confidently matched the selected {source_label}. "
                "Provide workspace/thread metadata or compare ccusage session IDs manually."
            ],
            session_match=_session_match_summary(None, matches, target=target, rows=rows),
        )

    top_score = max(match.score for match in matches)
    top_matches = [match for match in matches if match.score == top_score]
    if len(top_matches) > 1:
        return SessionMatchDecision(
            match=None,
            status="ambiguous_match",
            precision="no_confident_match",
            reason="multiple_ambiguous_session_matches",
            warnings=[
                f"Multiple ccusage session rows matched the selected {source_label} with the same confidence. "
                "Token/cost metrics were left missing to avoid attributing another session's usage."
            ],
            session_match=_session_match_summary(None, matches, target=target, rows=rows),
        )

    match = top_matches[0]
    if match.score not in _CONFIDENT_SESSION_SCORES:
        return SessionMatchDecision(
            match=None,
            status="no_confident_match",
            precision="no_confident_match",
            reason="weak_session_match",
            warnings=[
                f"Best ccusage session match was {match.confidence}; exact single-session metrics require "
                "exact, strong, or medium confidence."
            ],
            session_match=_session_match_summary(match, matches, target=target, rows=rows),
        )

    return SessionMatchDecision(
        match=match,
        status="success",
        precision="exact_session",
        reason=None,
        warnings=[],
        session_match=_session_match_summary(match, matches, target=target, rows=rows),
    )


def _session_match_summary(
    selected: SessionMatch | None,
    matches: list[SessionMatch],
    *,
    target: TargetSession | None = None,
    rows: list[SessionRow] | None = None,
) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "match_count": len(matches),
        "candidate_confidences": sorted({match.confidence for match in matches}),
    }
    if selected is not None:
        summary.update(
            {
                "confidence": selected.confidence,
                "reasons": list(selected.reasons),
                "row_index": selected.row.index,
            }
        )
    if target is not None and rows is not None:
        summary["diagnostics"] = _session_match_diagnostics(target, rows, selected, matches)
    return summary


def _session_match_diagnostics(
    target: TargetSession,
    rows: list[SessionRow],
    selected: SessionMatch | None,
    matches: list[SessionMatch],
) -> dict[str, Any]:
    matches_by_row = {match.row.index: match for match in matches}
    top_score = max((match.score for match in matches), default=None)
    top_row_indexes = [match.row.index for match in matches if match.score == top_score]
    if not matches:
        decision_reason = "no ccusage row matched by session id, workspace/time, thread/time, time overlap, or same day"
    elif selected is None and len(top_row_indexes) > 1:
        decision_reason = "ambiguous multiple ccusage rows shared the top confidence"
    elif selected is None:
        decision_reason = "best ccusage row did not meet the minimum confident score"
    else:
        decision_reason = "selected single confident ccusage row"

    return {
        "target": _target_session_summary(target),
        "ccusage_row_count": len(rows),
        "ccusage_rows_considered": [
            _session_row_summary(row)
            for row in rows
            if row.index in matches_by_row
        ],
        "candidate_matches": [
            _candidate_match_summary(match, target)
            for match in sorted(matches, key=lambda item: (-item.score, item.row.index))
        ],
        "non_candidate_count": len(rows) - len(matches),
        "non_candidate_sample": [
            _non_candidate_summary(row, target)
            for row in rows
            if row.index not in matches_by_row
        ][:5],
        "decision": {
            "selected_row_index": selected.row.index if selected is not None else None,
            "top_score": top_score,
            "top_row_indexes": top_row_indexes,
            "reason": decision_reason,
        },
    }


def _target_session_summary(target: TargetSession) -> dict[str, Any]:
    return {
        "session_ids": sorted(target.session_ids),
        "workspace_labels": _safe_labels(target.workspace_labels),
        "thread_titles": sorted(target.thread_titles),
        "first_activity": _format_datetime(target.first_activity),
        "last_activity": _format_datetime(target.last_activity),
        "dates": sorted(target.dates),
        "models": sorted(target.models),
    }


def _session_row_summary(row: SessionRow) -> dict[str, Any]:
    return {
        "row_index": row.index,
        "session_ids": sorted(row.session_ids),
        "workspace_labels": _safe_labels(row.workspace_labels),
        "thread_titles": sorted(row.thread_titles),
        "first_activity": _format_datetime(row.first_activity),
        "last_activity": _format_datetime(row.last_activity),
        "dates": sorted(row.dates),
        "models": sorted(row.models),
        "usage": _usage_value_summary(_usage_values(row.payload)),
    }


def _candidate_match_summary(match: SessionMatch, target: TargetSession) -> dict[str, Any]:
    return {
        "row_index": match.row.index,
        "confidence": match.confidence,
        "score": match.score,
        "reasons": list(match.reasons),
        "checks": _match_checks(target, match.row),
    }


def _non_candidate_summary(row: SessionRow, target: TargetSession) -> dict[str, Any]:
    return {
        "row_index": row.index,
        "checks": _match_checks(target, row),
        "reason": "no matching session id, no qualifying metadata/time match, and no same-day fallback",
    }


def _match_checks(target: TargetSession, row: SessionRow) -> dict[str, Any]:
    session_id_overlap = sorted(target.session_ids.intersection(row.session_ids))
    workspace_overlap = _safe_labels(target.workspace_labels.intersection(row.workspace_labels))
    thread_overlap = sorted(target.thread_titles.intersection(row.thread_titles))
    date_overlap = sorted(target.dates.intersection(row.dates))
    model_overlap = sorted(target.models.intersection(row.models))
    return {
        "session_id_overlap": session_id_overlap,
        "workspace_overlap": workspace_overlap,
        "thread_title_overlap": thread_overlap,
        "time_overlap": _activity_overlaps(target.first_activity, target.last_activity, row.first_activity, row.last_activity),
        "same_day": bool(date_overlap),
        "date_overlap": date_overlap,
        "model_overlap": model_overlap,
    }


def _usage_value_summary(values: UsageValues) -> dict[str, Any]:
    return {
        "input_tokens": _to_int(values.input_tokens),
        "cached_input_tokens": _to_int(values.cached_input_tokens),
        "output_tokens": _to_int(values.output_tokens),
        "reasoning_output_tokens": _to_int(values.reasoning_output_tokens),
        "total_tokens": _to_int(values.total_tokens),
        "estimated_cost": _to_float(values.estimated_cost),
        "currency": values.currency,
    }


def _format_datetime(value: datetime | None) -> str | None:
    return value.isoformat() if value is not None else None


def _safe_labels(values: set[str]) -> list[str]:
    return sorted(_safe_label(value) for value in values)


def _safe_label(value: str) -> str:
    text = str(value).replace("\\", "/")
    home = str(Path.home()).replace("\\", "/")
    if home and text.casefold().startswith(home.casefold()):
        text = "~" + text[len(home) :]
    username = Path.home().name
    if username:
        text = re.sub(re.escape(username), "<user>", text, flags=re.IGNORECASE)
    return text


def _strip_match_diagnostics(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _strip_match_diagnostics(item)
            for key, item in value.items()
            if key != "diagnostics"
        }
    if isinstance(value, list):
        return [_strip_match_diagnostics(item) for item in value]
    return value


def _single_session_resolved_input(resolved_input: ResolvedInput, rollout_file: Path) -> ResolvedInput:
    return ResolvedInput(
        agent=resolved_input.agent,
        scope_type="session",
        rollout_files=[Path(rollout_file)],
        codex_home=resolved_input.codex_home,
        logs_db=resolved_input.logs_db,
        state_db=resolved_input.state_db,
        workspace=resolved_input.workspace,
        thread_title=resolved_input.thread_title,
        date_range=resolved_input.date_range,
        output_dir=resolved_input.output_dir,
        warnings=list(resolved_input.warnings),
        resolution_status=resolved_input.resolution_status,
        claude_home=resolved_input.claude_home,
        source_metadata=dict(resolved_input.source_metadata),
    )


def _session_detail_from_decision(rollout_file: Path, decision: SessionMatchDecision) -> dict[str, Any]:
    detail: dict[str, Any] = {
        "rollout_file": Path(rollout_file).name,
        "status": decision.status,
        "precision": decision.precision,
        "reason": decision.reason,
        "input_tokens": None,
        "output_tokens": None,
        "estimated_cost": None,
    }
    if decision.match is not None:
        detail.update(
            {
                "confidence": decision.match.confidence,
                "reasons": list(decision.match.reasons),
                "row_index": decision.match.row.index,
            }
        )
    elif decision.session_match:
        detail["candidate_confidences"] = list(decision.session_match.get("candidate_confidences", []))
        detail["match_count"] = decision.session_match.get("match_count")
    if decision.session_match and "diagnostics" in decision.session_match:
        detail["diagnostics"] = decision.session_match["diagnostics"]
    return detail


def _usage_detail(values: UsageValues) -> dict[str, Any]:
    return {
        "status": "success",
        "precision": "exact_session",
        "reason": _estimated_cost_reason(values),
        "input_tokens": _to_int(values.input_tokens),
        "cached_input_tokens": _to_int(values.cached_input_tokens),
        "output_tokens": _to_int(values.output_tokens),
        "reasoning_output_tokens": _to_int(values.reasoning_output_tokens),
        "total_tokens": _to_int(values.total_tokens),
        "estimated_cost": _to_float(values.estimated_cost),
        "currency": values.currency,
    }


def _estimated_cost_reason(values: UsageValues) -> str | None:
    if values.has_token_or_cost_data() and values.estimated_cost is None:
        return "estimated_cost_not_provided"
    return None


def _estimated_cost_warnings(values: UsageValues, rollout_file: Path | None = None) -> list[str]:
    if _estimated_cost_reason(values) is None:
        return []
    if rollout_file is not None:
        return [f"ccusage did not provide estimated_cost for {Path(rollout_file).name}."]
    return ["ccusage did not provide estimated_cost for matched session row(s)."]


def _activity_overlaps(
    target_start: datetime | None,
    target_end: datetime | None,
    row_start: datetime | None,
    row_end: datetime | None,
) -> bool:
    if target_start is None or row_start is None:
        return False
    target_end = target_end or target_start
    row_end = row_end or row_start
    return (target_start - _TIME_OVERLAP_TOLERANCE) <= row_end and (row_start - _TIME_OVERLAP_TOLERANCE) <= target_end


def _has_session_metadata(data: dict[str, Any]) -> bool:
    return bool(
        _find_all_strings(data, _SESSION_FIELD_ALIASES)
        or _find_all_strings(data, _WORKSPACE_FIELD_ALIASES)
        or _find_all_strings(data, _THREAD_FIELD_ALIASES)
    )


def _record_dates(data: Any) -> set[str]:
    dates = {_normalize_iso_date(value) for value in _find_all_strings(data, _DATE_FIELD_ALIASES)}
    dates.update(
        date
        for dt in (_first_datetime(data, _START_TIME_ALIASES), _first_datetime(data, _END_TIME_ALIASES))
        if dt is not None
        for date in [dt.date().isoformat()]
    )
    return {date for date in dates if date}


def _first_datetime(data: Any, aliases: tuple[str, ...]) -> datetime | None:
    for value in _find_all_strings(data, aliases):
        parsed = _parse_datetime(value)
        if parsed is not None:
            return parsed
    return None


def _parse_datetime(value: str) -> datetime | None:
    text = value.strip()
    if not text:
        return None
    if text.isdigit():
        try:
            numeric = int(text)
            if numeric > 10_000_000_000:
                numeric = numeric / 1000
            return datetime.fromtimestamp(numeric, tz=timezone.utc)
        except (OverflowError, ValueError, OSError):
            return None
    normalized = text.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _normalize_iso_date(value: str | None) -> str | None:
    if value is None:
        return None
    match = re.search(r"\b(20\d{2}|19\d{2})-(0[1-9]|1[0-2])-([0-2]\d|3[01])\b", str(value))
    if not match:
        return None
    return match.group(0)


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


def _find_first_number(data: Any, aliases: tuple[str, ...]) -> int | float | None:
    for preferred_data in _preferred_total_containers(data):
        value = _find_first_number_in_tree(preferred_data, aliases)
        if value is not None:
            return value
    return _find_first_number_in_tree(data, aliases)


def _find_first_number_in_tree(data: Any, aliases: tuple[str, ...]) -> int | float | None:
    normalized_aliases = {_normalize_key(alias) for alias in aliases}
    for key, value in _walk_key_values(data):
        if _normalize_key(key) in normalized_aliases and isinstance(value, int | float):
            return value
        if _normalize_key(key) in normalized_aliases and isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                continue
    return None


def _preferred_total_containers(data: Any) -> list[Any]:
    if not isinstance(data, dict):
        return []
    preferred_keys = {"totals", "total", "summary"}
    return [
        value
        for key, value in data.items()
        if _normalize_key(str(key)) in preferred_keys and isinstance(value, dict)
    ]


def _find_first_string(data: Any, aliases: tuple[str, ...]) -> str | None:
    normalized_aliases = {_normalize_key(alias) for alias in aliases}
    for key, value in _walk_key_values(data):
        if _normalize_key(key) in normalized_aliases and isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _find_all_strings(data: Any, aliases: tuple[str, ...]) -> list[str]:
    normalized_aliases = {_normalize_key(alias) for alias in aliases}
    values: list[str] = []
    for key, value in _walk_key_values(data):
        if _normalize_key(key) in normalized_aliases:
            if isinstance(value, str) and value.strip():
                values.append(value.strip())
            elif isinstance(value, int | float):
                values.append(str(value))
    return values


def _find_first_dict(data: Any, aliases: tuple[str, ...]) -> dict[str, Any] | None:
    normalized_aliases = {_normalize_key(alias) for alias in aliases}
    for key, value in _walk_key_values(data):
        if _normalize_key(key) in normalized_aliases and isinstance(value, dict):
            return value
    return None


def _walk_key_values(data: Any) -> list[tuple[str, Any]]:
    values: list[tuple[str, Any]] = []
    if isinstance(data, dict):
        for key, value in data.items():
            values.append((str(key), value))
            values.extend(_walk_key_values(value))
    elif isinstance(data, list):
        for item in data:
            values.extend(_walk_key_values(item))
    return values


def _normalized_strings(values: Any) -> set[str]:
    normalized: set[str] = set()
    for value in values:
        text = str(value).strip()
        if text:
            normalized.add(text.casefold())
    return normalized


def _workspace_labels(values: list[str]) -> set[str]:
    labels: set[str] = set()
    for value in values:
        cleaned = str(value).strip().rstrip("\\/")
        if not cleaned:
            continue
        normalized_full = cleaned.replace("\\", "/").casefold()
        labels.add(normalized_full)
        labels.add(Path(cleaned).name.casefold())
    return labels


def _normalize_key(key: str) -> str:
    return key.replace("_", "").replace("-", "").casefold()


def _failure_warnings(
    resolved_input: ResolvedInput,
    command: list[str],
    mode: str,
    exit_code: int | None = None,
    stderr: str | None = None,
) -> list[str]:
    del resolved_input
    warnings = [
        f"ccusage mode attempted: {mode}",
        f"ccusage attempted command shape: {_command_shape(command)}",
    ]
    if exit_code is not None:
        warnings.append(f"ccusage exit code: {exit_code}")
    stderr_summary = _safe_process_output_summary(stderr)
    if stderr_summary:
        warnings.append(f"ccusage stderr summary: {stderr_summary}")
    return warnings


def _command_shape(command: list[str]) -> str:
    shaped_parts: list[str] = []
    for index, part in enumerate(command):
        text = str(part)
        if index == 0:
            text = Path(text).name
            for suffix in (".cmd", ".exe", ".ps1", ".bat"):
                if text.casefold().endswith(suffix):
                    text = text[: -len(suffix)]
                    break
        shaped_parts.append(text)
    return " ".join(shaped_parts)


def _mode_from_args(args: list[str] | None) -> str | None:
    if not args:
        return None
    normalized = [_normalize_key(str(part)) for part in args]
    for mode in _DISCOVERY_MODES:
        if mode in normalized:
            return mode
    return None


def _mode_from_command(command: list[str] | None) -> str | None:
    return _mode_from_args(command)


def _mode_from_data(data: Any) -> str | None:
    if isinstance(data, dict):
        normalized_keys = {_normalize_key(str(key)) for key in data.keys()}
        for mode in ("session", "daily", "weekly", "monthly"):
            if mode in normalized_keys or f"{mode}s" in normalized_keys:
                return mode
    return None


def _looks_like_unsupported_command(stderr: str | None) -> bool:
    text = (stderr or "").casefold()
    return any(needle in text for needle in ("unknown command", "unknown subcommand", "invalid command", "not supported"))


def _safe_process_output_summary(text: str | None) -> str | None:
    if not text:
        return None
    summary = text.replace(str(Path.home()), "~")
    username = Path.home().name
    if username:
        summary = summary.replace(username, "<user>")
    summary = re.sub(r"\x1b\[[0-9;]*m", "", summary)
    summary = re.sub(r"\s+", " ", summary).strip()
    if not summary:
        return None
    if len(summary) > _STDERR_SUMMARY_LIMIT:
        return f"{summary[:_STDERR_SUMMARY_LIMIT]}..."
    return summary


def _to_int(value: int | float | None) -> int | None:
    if value is None:
        return None
    return int(value)


def _to_float(value: int | float | None) -> float | None:
    if value is None:
        return None
    return float(value)


def _safe_model_breakdown(model_breakdown: dict[str, Any] | None) -> dict[str, Any] | None:
    if model_breakdown is None:
        return None

    safe: dict[str, Any] = {}
    for model_name, value in model_breakdown.items():
        if isinstance(value, dict):
            safe[str(model_name)] = {
                key: item
                for key, item in value.items()
                if isinstance(item, (int, float, str, type(None)))
            }
        elif isinstance(value, (int, float, str, type(None))):
            safe[str(model_name)] = value
    return safe


def _raw_summary(data: Any) -> dict[str, Any]:
    if isinstance(data, dict):
        return {
            "top_level_keys": sorted(str(key) for key in data.keys()),
            "record_count": _record_count(data),
        }
    if isinstance(data, list):
        return {
            "top_level_type": "list",
            "record_count": len(data),
        }
    return {
        "top_level_type": type(data).__name__,
        "record_count": 0,
    }


def _record_count(data: Any) -> int:
    if isinstance(data, dict):
        for keys in _RECORD_LIST_KEYS_BY_MODE.values():
            for key in keys:
                value = data.get(key)
                if isinstance(value, list):
                    return len(value)
        return 1
    if isinstance(data, list):
        return len(data)
    return 0


def _dedupe(values: list[str]) -> list[str]:
    deduped: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not value:
            continue
        if value in seen:
            continue
        seen.add(value)
        deduped.append(value)
    return deduped


def _dedupe_candidates(candidates: list[CommandCandidate]) -> list[CommandCandidate]:
    deduped: list[CommandCandidate] = []
    seen: set[tuple[str, ...]] = set()
    for candidate in candidates:
        key = tuple(candidate.args)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(candidate)
    return deduped
