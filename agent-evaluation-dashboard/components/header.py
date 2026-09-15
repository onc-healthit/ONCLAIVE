"""Shared dashboard header and report-derived context line."""

from __future__ import annotations

from html import escape
from typing import Callable, Iterable

import streamlit as st

from data.loader import AgentReport


def _value(report: AgentReport, field: str) -> str | None:
    value = report.run_metadata.get(field)
    return str(value) if value not in (None, "") else None


def _comparison_context(reports: Iterable[AgentReport]) -> str:
    indexed = {report.agent_key: report for report in reports}
    codex = indexed.get("codex")
    claude = indexed.get("claude_code")
    codex_model = _value(codex, "model") if codex else None
    claude_model = _value(claude, "model") if claude else None
    return (
        '<div class="comparison-header-context">'
        '<div class="comparison-header-agents">Codex vs Claude Code</div>'
        '<div class="comparison-header-models">'
        f'{escape(codex_model or "N/A")} '
        '<span aria-hidden="true">vs</span> '
        f'{escape(claude_model or "N/A")}'
        "</div></div>"
    )


def _single_context(report: AgentReport) -> str:
    items = (
        ("Agent", report.agent_label),
        ("Conversation", _value(report, "conversation_name") or "N/A"),
        ("Workspace", _value(report, "workspace_name") or "N/A"),
        ("Model", _value(report, "model") or "N/A"),
        ("Scope", _value(report, "scope_type") or "N/A"),
        ("Generated", _value(report, "generated_at") or "N/A"),
    )
    return '<div class="single-run-context">' + "".join(
        '<div class="single-run-context-item">'
        f'<span class="single-run-context-label">{escape(label)}</span>'
        f'<span class="single-run-context-value">{escape(value)}</span>'
        "</div>"
        for label, value in items
    ) + "</div>"


def render_single_context(report: AgentReport) -> None:
    """Reuse the standalone run context inside an embedded conversation tab."""
    st.markdown(_single_context(report), unsafe_allow_html=True)


def render_header(
    reports: Iterable[AgentReport] = (),
    on_replace: Callable[[], None] | None = None,
) -> None:
    report_list = list(reports)
    with st.container(key="dashboard_header"):
        context = (
            _single_context(report_list[0])
            if len(report_list) == 1
            else _comparison_context(report_list) if len(report_list) == 2 else ""
        )
        if on_replace:
            heading, action = st.columns([5, 1.15], vertical_alignment="top")
            with heading:
                st.title("ONCLAIVE Agent Evaluation Dashboard")
                if context:
                    container_class = (
                        "header-single-meta"
                        if len(report_list) == 1
                        else "header-comparison-meta"
                    )
                    st.markdown(
                        f'<div class="{container_class}">{context}</div>',
                        unsafe_allow_html=True,
                    )
            with action:
                st.button("Replace Reports", key="replace_reports", on_click=on_replace)
        else:
            st.title("ONCLAIVE Agent Evaluation Dashboard")
            if context:
                st.markdown(f'<div class="header-meta">{context}</div>', unsafe_allow_html=True)
