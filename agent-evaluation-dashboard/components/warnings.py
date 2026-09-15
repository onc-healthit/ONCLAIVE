"""Data-quality messages from both reports and contract-level gaps."""

from html import escape
from typing import Sequence

import streamlit as st

from data.comparison import CORE_METRICS, TOKEN_METRICS, metric_for
from data.loader import AgentReport


def _collect(report: AgentReport) -> list[str]:
    messages = list(report.warnings)
    for metric in report.metrics.values():
        messages.extend(metric.warnings)
        if metric.status == "partial":
            messages.append(f"{metric.name.replace('_', ' ').title()} is partial")
        elif metric.status == "estimated":
            messages.append(f"{metric.name.replace('_', ' ').title()} is estimated")
    return messages


def _single_warning_messages(report: AgentReport) -> list[str]:
    """Keep single-run warnings concise while retaining report-provided detail."""
    warnings = list(report.warnings)
    for metric in report.metrics.values():
        warnings.extend(metric.warnings)
        if metric.status == "partial" and not metric.warnings:
            warnings.append(f"{metric.name.replace('_', ' ').title()} is partial")
        elif metric.status == "estimated" and not metric.warnings:
            if metric.name == "estimated_cost":
                warnings.append("Estimated cost is not actual billed cost")
            else:
                warnings.append(f"{metric.name.replace('_', ' ').title()} is estimated")

    for definition in CORE_METRICS:
        if metric_for(report, definition).value is None:
            warnings.append(f"{definition.label} is unavailable")
    for definition in TOKEN_METRICS[:2]:
        if metric_for(report, definition).value is None:
            warnings.append(f"{definition.label} is unavailable")
    return list(dict.fromkeys(warnings))


def _warning_messages(reports: Sequence[AgentReport]) -> list[str]:
    if len(reports) == 1:
        return _single_warning_messages(reports[0])

    warnings: list[str] = []
    for report in reports:
        warnings.extend(f"{report.agent_label}: {message}" for message in _collect(report))

    if any(metric_for(report, CORE_METRICS[4]).status == "partial" for report in reports):
        warnings.append("File edits are partial")
    if any(metric_for(report, CORE_METRICS[1]).status == "estimated" for report in reports):
        warnings.append("Estimated cost is not actual billed cost")
    cost_and_tokens = (CORE_METRICS[1],) + TOKEN_METRICS
    if any(
        metric_for(report, definition).value is None
        for report in reports
        for definition in cost_and_tokens
    ):
        warnings.append("Token/cost metrics may be missing")

    for definition in CORE_METRICS:
        for report in reports:
            if metric_for(report, definition).value is None:
                warnings.append(f"{report.agent_label}: {definition.label} is unavailable")

    return list(dict.fromkeys(warnings))


def render_warnings(reports: Sequence[AgentReport]) -> None:
    if len(reports) == 1:
        return

    unique = _warning_messages(reports)
    st.header("Warnings & Data Quality")
    if not unique:
        st.caption("No data quality warnings were reported.")
        return
    items = "".join(f'<li>{escape(message)}</li>' for message in unique)
    st.markdown(f'<div class="warning-panel"><ul>{items}</ul></div>', unsafe_allow_html=True)
