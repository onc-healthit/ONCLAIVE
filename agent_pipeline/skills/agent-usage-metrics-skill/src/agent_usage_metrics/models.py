"""Shared data models passed between resolution, collection, metrics, and reporting."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class UsageQuery:
    """Parsed user request before it is resolved to local agent session files."""
    raw_query: str | None = None
    agent: str = "codex"
    workspace_query: str | None = None
    thread_title_query: str | None = None
    date_query: str | None = None
    date_range: tuple[str, str] | None = None
    selection_mode: str | None = None
    target_type_query: str | None = None
    quoted_phrases: list[str] = field(default_factory=list)
    rollout_file: Path | None = None
    codex_home: Path | None = None
    claude_home: Path | None = None
    output_dir: Path | None = None
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        result = {
            "raw_query": self.raw_query,
            "agent": self.agent,
            "workspace_query": self.workspace_query,
            "thread_title_query": self.thread_title_query,
            "date_query": self.date_query,
            "date_range": list(self.date_range) if self.date_range else None,
            "selection_mode": self.selection_mode,
            "target_type_query": self.target_type_query,
            "quoted_phrases": list(self.quoted_phrases),
            "rollout_file": str(self.rollout_file) if self.rollout_file else None,
            "codex_home": str(self.codex_home) if self.codex_home else None,
            "output_dir": str(self.output_dir) if self.output_dir else None,
            "warnings": list(self.warnings),
        }
        if self.agent == "claude_code":
            result["claude_home"] = str(self.claude_home) if self.claude_home else None
        return result


@dataclass(frozen=True)
class ResolvedInput:
    """Concrete report target and the local sources needed to analyze it."""
    agent: str
    scope_type: str
    rollout_files: list[Path]
    codex_home: Path | None
    logs_db: Path | None
    state_db: Path | None
    workspace: Path | None
    thread_title: str | None
    date_range: tuple[str, str] | None
    output_dir: Path
    warnings: list[str] = field(default_factory=list)
    resolution_status: str = "exact"
    claude_home: Path | None = None
    source_metadata: dict[str, Any] = field(default_factory=dict)
    session_titles: dict[str, str | None] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = {
            "agent": self.agent,
            "target_type": self.scope_type,
            "scope_type": self.scope_type,
            "rollout_files": [str(path) for path in self.rollout_files],
            "codex_home": str(self.codex_home) if self.codex_home else None,
            "logs_db": str(self.logs_db) if self.logs_db else None,
            "state_db": str(self.state_db) if self.state_db else None,
            "workspace": str(self.workspace) if self.workspace else None,
            "thread_title": self.thread_title,
            "date_range": list(self.date_range) if self.date_range else None,
            "output_dir": str(self.output_dir),
            "warnings": list(self.warnings),
            "resolution_status": self.resolution_status,
            "session_titles": dict(self.session_titles),
        }
        if self.agent == "claude_code":
            result.update(
                {
                    "claude_home": str(self.claude_home) if self.claude_home else None,
                    "source_metadata": dict(self.source_metadata),
                }
            )
        return result


@dataclass(frozen=True)
class RawCodexRecord:
    """One unmodified record loaded from an agent log source."""
    source_type: str
    source_path: Path
    record_kind: str
    timestamp: str | None
    turn_id: str | None
    payload_type: str | None
    raw_payload: Any
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class RawCodexData:
    """Collected raw records and source-loading warnings for one resolved target."""
    records: list[RawCodexRecord]
    source_files: list[Path]
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class CcusageResult:
    """Token and cost enrichment result, including match confidence and limitations."""
    status: str
    command: list[str] | None
    scope_requested: dict[str, Any] | None
    scope_returned: dict[str, Any] | None
    input_tokens: int | None
    cached_input_tokens: int | None
    output_tokens: int | None
    reasoning_output_tokens: int | None
    total_tokens: int | None
    estimated_cost: float | None
    currency: str | None
    model_breakdown: dict[str, Any] | None
    raw_summary: dict[str, Any] | None
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    precision: str = "unavailable"
    reason: str | None = None
    mode_attempted: str | None = None
    command_attempts: list[list[str]] = field(default_factory=list)
    session_match: dict[str, Any] | None = None


@dataclass(frozen=True)
class NormalizedEvent:
    """Common event form used to calculate metrics across supported agents."""
    event_type: str
    timestamp: str | None
    turn_id: str | None
    source_type: str
    source_path: Path
    payload_type: str | None
    role: str | None = None
    tool_name: str | None = None
    command: str | None = None
    file_paths: list[str] = field(default_factory=list)
    duration_ms: int | None = None
    request_type: str | None = None
    sandbox_permissions: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class NormalizedEventData:
    """Normalized events plus source counts and normalization warnings."""
    events: list[NormalizedEvent]
    source_record_count: int
    normalized_event_count: int
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class MetricResult:
    """One reported metric with its value, reliability status, and source notes."""
    name: str
    value: Any
    status: str
    source: str
    warnings: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "value": self.value,
            "status": self.status,
            "source": self.source,
            "warnings": list(self.warnings),
            "notes": list(self.notes),
        }


@dataclass(frozen=True)
class RunMetadata:
    """Safe identifying context shown with a generated report."""
    agent: str
    scope_type: str
    workspace: str | None
    thread_title: str | None
    date_range: tuple[str, str] | None
    rollout_files: list[str]
    resolution_status: str
    codex_home_present: bool
    logs_db_present: bool
    state_db_present: bool
    output_dir: str
    generated_at: str
    session_titles: dict[str, str | None] = field(default_factory=dict)
    source_session_id: str | None = None
    git_branch: str | None = None
    start_timestamp: str | None = None
    end_timestamp: str | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {
            "agent": self.agent,
            "target_type": self.scope_type,
            "scope_type": self.scope_type,
            "workspace": self.workspace,
            "thread_title": self.thread_title,
            "date_range": list(self.date_range) if self.date_range else None,
            "rollout_files": list(self.rollout_files),
            "resolution_status": self.resolution_status,
            "codex_home_present": self.codex_home_present,
            "logs_db_present": self.logs_db_present,
            "state_db_present": self.state_db_present,
            "output_dir": self.output_dir,
            "generated_at": self.generated_at,
            "session_titles": dict(self.session_titles),
        }
        if self.agent == "claude_code":
            result.update(
                {
                    "source_session_id": self.source_session_id,
                    "git_branch": self.git_branch,
                    "start_timestamp": self.start_timestamp,
                    "end_timestamp": self.end_timestamp,
                }
            )
        return result


@dataclass(frozen=True)
class AgentUsageReport:
    """Complete report content before it is formatted as Markdown."""
    run_metadata: RunMetadata
    metrics: list[MetricResult]
    warnings: list[str]
    notes: list[str]
    generated_at: str
    sources_used: list[str]
    ccusage: dict[str, Any] = field(default_factory=dict)
    session_breakdown_path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_metadata": self.run_metadata.to_dict(),
            "metrics": [metric.to_dict() for metric in self.metrics],
            "warnings": list(self.warnings),
            "notes": list(self.notes),
            "generated_at": self.generated_at,
            "sources_used": list(self.sources_used),
            "ccusage": dict(self.ccusage),
            "session_breakdown_path": self.session_breakdown_path,
        }


@dataclass(frozen=True)
class SessionBreakdownRow:
    """Per-session values shown alongside a multi-session report."""
    rollout_file: str
    start_time: str | None
    end_time: str | None
    wall_clock_time_seconds: Any
    api_request_count: Any
    human_prompts_required: Any
    tool_calls: Any
    file_edits: Any
    ccusage_status: str | None
    ccusage_precision: str | None
    ccusage_reason: str | None = None
    input_tokens: Any = None
    output_tokens: Any = None
    estimated_cost: Any = None
    conversation_title: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "rollout_file": self.rollout_file,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "wall_clock_time_seconds": self.wall_clock_time_seconds,
            "api_request_count": self.api_request_count,
            "human_prompts_required": self.human_prompts_required,
            "tool_calls": self.tool_calls,
            "file_edits": self.file_edits,
            "ccusage_status": self.ccusage_status,
            "ccusage_precision": self.ccusage_precision,
            "ccusage_reason": self.ccusage_reason,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "estimated_cost": self.estimated_cost,
            "conversation_title": self.conversation_title,
        }


@dataclass(frozen=True)
class ReportFlowResult:
    """Outcome and output paths returned by the report-generation flow."""
    status: str
    resolved_input: ResolvedInput
    ccusage_result: CcusageResult | None
    report: AgentUsageReport | None
    markdown_path: Path | None = None
    breakdown_path: Path | None = None
    json_path: Path | None = None
    permission_question: str | None = None
