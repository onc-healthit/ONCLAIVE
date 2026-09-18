"""Secondary, traceability-focused run metadata."""

from html import escape
from typing import Any, Sequence

import streamlit as st

from data.loader import AgentReport


FIELDS = (
    ("Conversation", "conversation_name"),
    ("Workspace", "workspace_name"),
    ("Model", "model"),
    ("Scope", "scope_type"),
    ("Generated At", "generated_at"),
    ("Session Files", "session_files"),
)


def _display(value: Any) -> str:
    if value is None or value == "":
        return "N/A"
    if isinstance(value, (list, tuple)):
        return ", ".join(map(str, value)) or "N/A"
    return str(value)


def _metadata_value(key: str, value: Any) -> str:
    if key == "session_files" and isinstance(value, (list, tuple)):
        if not value:
            return '<span class="metadata-list-item">N/A</span>'
        return "".join(
            f'<span class="metadata-list-item">{escape(str(item))}</span>' for item in value
        )
    return escape(_display(value))


def _metadata_card(report: AgentReport) -> str:
    rows = "".join(
        '<div class="metadata-row">'
        f'<span>{escape(label)}</span><strong class="metadata-value metadata-{key.replace("_", "-")}">'
        f'{_metadata_value(key, report.run_metadata.get(key))}</strong>'
        "</div>"
        for label, key in FIELDS
    )
    rows += (
        '<div class="metadata-row"><span>Sources Used</span>'
        f'<strong>{escape(_display(report.sources_used))}</strong></div>'
    )
    return (
        '<div class="metadata-card">'
        f'<div class="metadata-agent agent-label agent-{report.agent_key.replace("_code", "")}">'
        f'{escape(report.agent_label)}</div>{rows}</div>'
    )


def _run_details_card(report: AgentReport) -> str:
    rows = (
        '<div class="metadata-row">'
        '<span>Session Files</span>'
        '<strong class="metadata-value metadata-session-files">'
        f'{_metadata_value("session_files", report.run_metadata.get("session_files"))}'
        "</strong></div>"
        '<div class="metadata-row">'
        '<span>Sources Used</span>'
        f'<strong>{escape(_display(report.sources_used))}</strong>'
        "</div>"
    )
    return f'<div class="metadata-card run-details-card">{rows}</div>'


def render_metadata(reports: Sequence[AgentReport], key_suffix: str = "") -> None:
    if len(reports) == 1:
        st.header("Run Details")
        key = "single_run_details" + (f"_{key_suffix}" if key_suffix else "")
        with st.container(key=key):
            with st.expander("View session files and sources", expanded=False):
                st.markdown(_run_details_card(reports[0]), unsafe_allow_html=True)
        return

    st.header("Run Details")
    with st.container(key="comparison_run_details"):
        with st.expander("View Codex and Claude Code run details", expanded=False):
            cards = "".join(_metadata_card(report) for report in reports)
            st.markdown(f'<div class="metadata-grid">{cards}</div>', unsafe_allow_html=True)
