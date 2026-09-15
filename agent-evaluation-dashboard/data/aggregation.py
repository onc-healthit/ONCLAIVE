"""Strict aggregation helpers for multi-conversation overview UI."""

from __future__ import annotations

from typing import Sequence

from .comparison import CORE_METRICS, TOKEN_METRICS, MetricDefinition, is_number, metric_for
from .loader import AgentReport, Metric


OVERVIEW_METRICS = (
    ("Total Runtime", CORE_METRICS[0]),
    ("Total Estimated Cost", CORE_METRICS[1]),
    ("Total Tokens", CORE_METRICS[5]),
    ("Total Human Prompts", CORE_METRICS[2]),
    ("Total Tool Calls", CORE_METRICS[3]),
    ("Total File Edits", CORE_METRICS[4]),
)

WORKSPACE_OVERVIEW_METRICS = (
    ("Runtime", CORE_METRICS[0]),
    ("Cost", CORE_METRICS[1]),
    ("Tokens", CORE_METRICS[5]),
    ("Human Prompts", CORE_METRICS[2]),
    ("Tool Calls", CORE_METRICS[3]),
    ("File Edits", CORE_METRICS[4]),
)


def aggregate_metric(reports: Sequence[AgentReport], definition: MetricDefinition) -> Metric:
    """Sum a metric only when every report provides it; null remains unavailable."""
    metrics = [metric_for(report, definition) for report in reports]
    if not metrics or any(not is_number(metric.value) for metric in metrics):
        return Metric(name=definition.names[0])

    statuses = {metric.status for metric in metrics}
    status = (
        "partial"
        if "partial" in statuses
        else "estimated"
        if "estimated" in statuses
        else "computed"
    )
    sources = list(dict.fromkeys(metric.source for metric in metrics if metric.source))
    return Metric(
        name=definition.names[0],
        value=sum(float(metric.value) for metric in metrics),
        status=status,
        source=", ".join(sources) or None,
        warnings=tuple(
            dict.fromkeys(warning for metric in metrics for warning in metric.warnings)
        ),
    )


def aggregate_report(reports: Sequence[AgentReport]) -> AgentReport:
    """Create a UI-only aggregate report without changing uploaded payloads."""
    if not reports:
        raise ValueError("At least one report is required")
    agent_keys = {report.agent_key for report in reports}
    if len(agent_keys) != 1:
        raise ValueError("Conversation aggregation requires reports from one agent")

    metrics = {
        definition.names[0]: aggregate_metric(reports, definition)
        for definition in CORE_METRICS
    }
    # Input and output are needed by the existing token composition component.
    for definition in TOKEN_METRICS[:2]:
        metrics[definition.names[0]] = aggregate_metric(reports, definition)

    workspace_values = {
        report.run_metadata.get("workspace_name")
        for report in reports
        if report.run_metadata.get("workspace_name") not in (None, "")
    }
    metadata = {
        "agent": reports[0].agent_key,
        "session_files": [
            filename
            for report in reports
            for filename in report.run_metadata.get("session_files", [])
        ],
        "conversation_name": None,
        "workspace_name": next(iter(workspace_values)) if len(workspace_values) == 1 else None,
        "scope_type": "conversation",
        "model": None,
        "generated_at": reports[0].run_metadata.get("generated_at"),
    }
    return AgentReport(
        agent_key=reports[0].agent_key,
        agent_label=reports[0].agent_label,
        run_metadata=metadata,
        metrics=metrics,
        warnings=tuple(dict.fromkeys(warning for report in reports for warning in report.warnings)),
        sources_used=tuple(
            dict.fromkeys(source for report in reports for source in report.sources_used)
        ),
    )


def conversation_name(report: AgentReport) -> str:
    value = report.run_metadata.get("conversation_name")
    return str(value).strip() if value not in (None, "") else "N/A"


def workspace_conversation_count(report: AgentReport) -> int | None:
    """Use an explicit count only; session files are not conversations."""
    value = report.run_metadata.get("conversation_count")
    if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
        return value
    return None
