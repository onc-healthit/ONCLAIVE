"""Single-run token composition and comparison token usage views."""

from __future__ import annotations

from html import escape
from typing import Sequence

import streamlit as st

from data.comparison import TOKEN_METRICS, format_value, is_number, metric_for
from data.loader import AgentReport, Metric


def _status_value(metric: Metric) -> str:
    status = metric.status if metric.value is not None else "missing"
    return status if status in {"computed", "partial", "missing", "estimated"} else "missing"


def _width(value: object, maximum: float) -> float:
    return max(0.0, min(100.0, float(value) / maximum * 100)) if is_number(value) else 0.0


def _agent_class(report: AgentReport) -> str:
    return "codex" if report.agent_key == "codex" else "claude"


def _token_tooltip(label: str, metric: Metric, direction: str) -> str:
    return (
        f'<span class="single-token-tooltip token-tooltip-{direction}" role="tooltip">'
        f'<strong>{escape(label)}</strong>'
        f'<span>Count: {escape(format_value(metric.value, "integer"))}</span>'
        f'<span>Status: {escape(_status_value(metric))}</span>'
        f'<span>Source: {escape(metric.source or "Not provided")}</span>'
        "</span>"
    )


def _single_token_content(report: AgentReport) -> str:
    """Render one aligned stack with deterministic vertical tooltip arrows."""
    total = metric_for(report, TOKEN_METRICS[2])
    segment_specs = (
        ("Input Tokens", metric_for(report, TOKEN_METRICS[0]), "input", "above"),
        ("Output Tokens", metric_for(report, TOKEN_METRICS[1]), "output", "below"),
    )
    numeric_total = sum(
        float(metric.value) for _, metric, _, _ in segment_specs if is_number(metric.value)
    )
    available_count = sum(is_number(metric.value) for _, metric, _, _ in segment_specs)

    legend = "".join(
        '<span class="single-token-legend-item">'
        f'<span class="single-token-swatch token-swatch-{segment_class}" aria-hidden="true"></span>'
        f'{escape(label)}'
        f'{"" if is_number(metric.value) else " · N/A"}'
        "</span>"
        for label, metric, segment_class, _ in segment_specs
    )
    segments: list[str] = []
    for label, metric, segment_class, direction in segment_specs:
        if not is_number(metric.value):
            continue
        percentage = float(metric.value) / numeric_total * 100 if numeric_total > 0 else 0.0
        only_class = " token-segment-only" if available_count == 1 else ""
        segments.append(
            f'<span class="single-token-segment token-segment-{segment_class}{only_class}" '
            f'style="width:{percentage:.4f}%" tabindex="0" '
            f'aria-label="{escape(label)}: {escape(format_value(metric.value, "integer"))}; '
            f'status {_status_value(metric)}; source {escape(metric.source or "Not provided")}">'
            f'{_token_tooltip(label, metric, direction)}</span>'
        )

    if segments and numeric_total > 0:
        stack = (
            '<div class="single-token-stack" role="img" '
            'aria-label="Input and output token composition">'
            f'{"".join(segments)}</div>'
        )
    else:
        stack = '<div class="single-token-stack-empty">Token composition unavailable</div>'

    return (
        '<div class="single-token-content">'
        '<div class="single-token-summary">'
        '<div class="single-token-label">Total Tokens</div>'
        f'<div class="single-token-value">{escape(format_value(total.value, "integer"))}</div>'
        "</div>"
        f'<div class="single-token-legend">{legend}</div>'
        f'{stack}</div>'
    )


def _render_single_token_usage(report: AgentReport, key_suffix: str = "") -> None:
    key = "single_token_card" + (f"_{key_suffix}" if key_suffix else "")
    with st.container(key=key):
        st.markdown(_single_token_content(report), unsafe_allow_html=True)


def _render_comparison_token_usage(reports: Sequence[AgentReport]) -> None:
    for definition in TOKEN_METRICS:
        metrics = [metric_for(report, definition) for report in reports]
        numeric = [float(metric.value) for metric in metrics if is_number(metric.value)]
        maximum = max(numeric, default=1.0) or 1.0
        rows: list[str] = []
        for report, metric in zip(reports, metrics):
            agent_class = _agent_class(report)
            value = escape(format_value(metric.value, "integer"))
            if is_number(metric.value):
                visual = (
                    '<div class="bar-track" aria-hidden="true">'
                    f'<div class="bar-fill-{agent_class}" style="width:{_width(metric.value, maximum):.1f}%">'
                    "</div></div>"
                )
            else:
                visual = '<div class="bar-unavailable">Unavailable</div>'
            rows.append(
                '<div class="bar-row">'
                f'<span class="agent-label agent-{agent_class}">{escape(report.agent_label)}</span>'
                f'{visual}<span class="bar-number">{value}</span></div>'
            )
        st.markdown(
            '<div class="bar-card">'
            f'<div class="bar-header">{escape(definition.label)}</div>'
            f'{"".join(rows)}</div>',
            unsafe_allow_html=True,
        )


def render_token_usage(reports: Sequence[AgentReport], key_suffix: str = "") -> None:
    st.header("Token Usage")
    if len(reports) == 1:
        _render_single_token_usage(reports[0], key_suffix)
        return
    _render_comparison_token_usage(reports)
