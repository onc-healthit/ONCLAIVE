"""High-level cost and speed conclusions."""

from __future__ import annotations

from html import escape

import streamlit as st

from data.comparison import CORE_METRICS, takeaway_text
from data.loader import AgentReport


def _takeaway(label: str, text: str) -> str:
    return (
        '<div class="comparison-takeaway">'
        f'<div class="comparison-takeaway-label">{escape(label.upper())}</div>'
        f'<div class="comparison-takeaway-value">{escape(text)}</div></div>'
    )


def render_takeaways(codex: AgentReport, claude: AgentReport) -> None:
    cost_text = takeaway_text(codex, claude, CORE_METRICS[1])
    speed_text = takeaway_text(codex, claude, CORE_METRICS[0])
    takeaways = [
        _takeaway(label, text)
        for label, text in (("Cost", cost_text), ("Runtime", speed_text))
        if text
    ]
    if not takeaways:
        return
    st.header("Primary Takeaways")
    st.markdown(
        f'<div class="comparison-takeaway-grid">{"".join(takeaways)}</div>',
        unsafe_allow_html=True,
    )
