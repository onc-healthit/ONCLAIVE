"""Overview layers for multiple conversations and workspace reports."""

from __future__ import annotations

from html import escape
from typing import Sequence

import plotly.graph_objects as go
import streamlit as st

from components.core_metrics import AGENT_COLORS
from data.aggregation import (
    OVERVIEW_METRICS,
    WORKSPACE_OVERVIEW_METRICS,
    aggregate_metric,
    conversation_name,
    workspace_conversation_count,
)
from data.comparison import MetricDefinition, format_value, is_number, metric_for
from data.loader import AgentReport
from data.observations import build_highest_token_summary


RESOURCE_DISTRIBUTION_METRICS = (
    ("Runtime", OVERVIEW_METRICS[0][1]),
    ("Estimated Cost", OVERVIEW_METRICS[1][1]),
    ("Total Tokens", OVERVIEW_METRICS[2][1]),
    ("Human Prompts", OVERVIEW_METRICS[3][1]),
    ("Tool Calls", OVERVIEW_METRICS[4][1]),
    ("File Edits", OVERVIEW_METRICS[5][1]),
)

DISTRIBUTION_AXIS_TITLES = {
    "wall_clock_time_seconds": "Runtime (seconds)",
    "estimated_cost": "USD",
    "total_tokens": "Tokens",
    "human_prompts_required": "Prompts",
    "tool_calls": "Tool calls",
    "file_edits": "File edits",
}

DISTRIBUTION_HEADROOM_FACTOR = 1.18
DISTRIBUTION_TICK_COUNT = 7


def _context(items: Sequence[tuple[str, str]]) -> str:
    return '<div class="overview-context">' + "".join(
        '<div class="overview-context-item">'
        f'<span class="overview-context-label">{escape(label)}</span>'
        f'<strong class="overview-context-value">{escape(value)}</strong></div>'
        for label, value in items
    ) + "</div>"


def _kpi_grid(values: Sequence[tuple[str, object, str]]) -> str:
    cards = "".join(
        '<div class="single-kpi-card">'
        f'<div class="single-kpi-label">{escape(label)}</div>'
        f'<div class="single-kpi-value">{escape(format_value(value, kind))}</div></div>'
        for label, value, kind in values
    )
    return f'<div class="overview-kpi-grid">{cards}</div>'


def _aggregate_kpis(reports: Sequence[AgentReport]) -> str:
    return _kpi_grid(
        [
            (label, aggregate_metric(reports, definition).value, definition.kind)
            for label, definition in OVERVIEW_METRICS
        ]
    )


def _workspace_kpis(report: AgentReport) -> str:
    return _kpi_grid(
        [
            (label, metric_for(report, definition).value, definition.kind)
            for label, definition in WORKSPACE_OVERVIEW_METRICS
        ]
    )


def _distribution_axis(definition: MetricDefinition, maximum: float) -> dict:
    padded_maximum = maximum * DISTRIBUTION_HEADROOM_FACTOR if maximum > 0 else 1.0
    axis = {
        "fixedrange": True,
        "range": [0, padded_maximum],
        "nticks": DISTRIBUTION_TICK_COUNT,
        "showgrid": True,
        "gridcolor": "#ECE8E2",
        "gridwidth": 1,
        "showline": False,
        "zeroline": False,
        "tickfont": {"color": "#716E68", "size": 11},
        "title": {
            "text": DISTRIBUTION_AXIS_TITLES[definition.names[0]],
            "font": {"color": "#716E68", "size": 11},
            "standoff": 14,
        },
        "automargin": True,
    }
    if definition.kind == "currency":
        axis.update({"tickformat": ",.2f", "tickprefix": "$"})
    elif definition.names[0] == "total_tokens":
        axis["tickformat"] = "~s"
    elif definition.kind == "integer":
        axis["tickformat"] = ",.0f"
        if maximum <= 8:
            axis.update({"tickmode": "linear", "tick0": 0, "dtick": 1})
    else:
        axis.update({"tickformat": ",.0f", "ticksuffix": "s"})
    return axis


def _conversation_axis_label(name: str, line_limit: int = 26) -> str:
    """Keep long conversation labels horizontal using at most two compact lines."""
    text = " ".join(name.split()) or "N/A"
    if len(text) <= line_limit:
        return text

    words = text.split(" ")
    first_line: list[str] = []
    while words and len(" ".join((*first_line, words[0]))) <= line_limit:
        first_line.append(words.pop(0))

    if not first_line:
        return f"{text[: line_limit - 1]}…"

    remainder = " ".join(words)
    if len(remainder) > line_limit:
        remainder = f"{remainder[: line_limit - 1].rstrip()}…"
    return f"{' '.join(first_line)}<br>{remainder}"


def _distribution_series(
    reports: Sequence[AgentReport], label: str, definition: MetricDefinition
) -> tuple[list[float | None], list[list[str]], str, list[dict], dict]:
    names = [conversation_name(report) for report in reports]
    positions = list(range(len(reports)))
    metrics = [metric_for(report, definition) for report in reports]
    values = [float(metric.value) if is_number(metric.value) else None for metric in metrics]
    maximum = max((value for value in values if value is not None), default=0.0)
    customdata = [
        [name, format_value(metric.value, definition.kind)]
        for name, metric in zip(names, metrics)
    ]
    hovertemplate = (
        "<b>%{customdata[0]}</b><br>"
        f"{escape(label)}: %{{customdata[1]}}<extra></extra>"
    )
    axis = _distribution_axis(definition, maximum)
    annotations = [
        {
            "xref": "paper",
            "yref": "paper",
            "x": 0,
            "y": 1.25,
            "text": "Metric",
            "showarrow": False,
            "xanchor": "left",
            "font": {"size": 11, "color": "#514E49"},
        }
    ]
    annotations.extend(
        {
            "x": position,
            "y": axis["range"][1] * 0.06,
            "text": "N/A",
            "showarrow": False,
            "font": {"size": 11, "color": "#716E68"},
        }
        for position, value in zip(positions, values)
        if value is None
    )
    return values, customdata, hovertemplate, annotations, axis


def build_resource_distribution_figure(
    reports: Sequence[AgentReport],
    label: str,
    definition: MetricDefinition,
) -> go.Figure:
    """Build one dynamically scaled, same-agent bar chart across conversations."""
    if not reports:
        raise ValueError("At least one conversation report is required")
    if len({report.agent_key for report in reports}) != 1:
        raise ValueError("Resource distribution requires reports from one agent")

    names = [conversation_name(report) for report in reports]
    axis_labels = [_conversation_axis_label(name) for name in names]
    positions = list(range(len(reports)))
    values, customdata, hovertemplate, annotations, axis = _distribution_series(
        reports, label, definition
    )

    color = AGENT_COLORS[reports[0].agent_key]
    figure = go.Figure(
        go.Bar(
            x=positions,
            y=values,
            width=0.58,
            customdata=customdata,
            marker={"color": color, "line": {"color": color, "width": 1}},
            hovertemplate=hovertemplate,
        )
    )
    buttons = []
    for option_label, option_definition in RESOURCE_DISTRIBUTION_METRICS:
        option_values, option_customdata, option_hover, option_annotations, option_axis = (
            _distribution_series(reports, option_label, option_definition)
        )
        buttons.append(
            {
                "label": option_label,
                "method": "update",
                "args": [
                    {
                        "y": [option_values],
                        "customdata": [option_customdata],
                        "hovertemplate": [option_hover],
                    },
                    {"yaxis": option_axis, "annotations": option_annotations},
                ],
            }
        )
    active = next(
        index
        for index, (option_label, _) in enumerate(RESOURCE_DISTRIBUTION_METRICS)
        if option_label == label
    )
    figure.update_layout(
        height=390,
        margin={"l": 70, "r": 4, "t": 88, "b": 90},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        bargap=0.42,
        hovermode="closest",
        hoverlabel={
            "bgcolor": "#2E2B27",
            "bordercolor": "#2E2B27",
            "font": {"color": "#FFFFFF", "size": 13, "family": "Inter, sans-serif"},
        },
        xaxis={
            "fixedrange": True,
            "range": [-0.5, max(0.5, len(reports) - 0.5)],
            "tickmode": "array",
            "tickvals": positions,
            "ticktext": axis_labels,
            "tickangle": 0,
            "showgrid": False,
            "zeroline": False,
            "linecolor": "#DEDAD3",
            "tickfont": {"color": "#33312E", "size": 11},
            "automargin": True,
        },
        yaxis=axis,
        annotations=annotations,
        updatemenus=[
            {
                "type": "dropdown",
                "active": active,
                "buttons": buttons,
                "direction": "down",
                "showactive": True,
                "x": 0,
                "xanchor": "left",
                "y": 1.18,
                "yanchor": "bottom",
                "pad": {"r": 8, "t": 2},
                "bgcolor": "#FFFFFF",
                "bordercolor": "#CBC5BB",
                "borderwidth": 1,
                "font": {"color": "#2E2B27", "size": 12},
            }
        ],
        font={"family": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},
    )
    return figure


def render_multiple_summary(reports: Sequence[AgentReport]) -> None:
    summary = build_highest_token_summary(reports)
    if not summary:
        return
    st.markdown(
        f'<p class="multiple-summary">{escape(summary)}</p>',
        unsafe_allow_html=True,
    )


def render_resource_distribution(reports: Sequence[AgentReport]) -> None:
    with st.container(border=True, key="conversation_distribution"):
        selected, definition = RESOURCE_DISTRIBUTION_METRICS[0]
        st.plotly_chart(
            build_resource_distribution_figure(reports, selected, definition),
            key="conversation_distribution_chart",
            config={
                "displayModeBar": False,
                "displaylogo": False,
                "scrollZoom": False,
                "responsive": True,
            },
            use_container_width=True,
        )


def render_multiple_overview(reports: Sequence[AgentReport]) -> None:
    st.markdown(
        _context(
            (
                ("Agent", reports[0].agent_label),
                ("Conversations", str(len(reports))),
            )
        ),
        unsafe_allow_html=True,
    )
    st.header("Overall Metrics")
    st.markdown(_aggregate_kpis(reports), unsafe_allow_html=True)
    st.header("Resource Distribution Across Conversations")
    render_resource_distribution(reports)


def render_workspace_overview(report: AgentReport) -> None:
    count = workspace_conversation_count(report)
    st.header("Workspace Overview")
    st.markdown(
        _context(
            (
                ("Workspace", str(report.run_metadata.get("workspace_name") or "N/A")),
                ("Agent", report.agent_label),
                ("Conversations", str(count) if count is not None else "N/A"),
            )
        ),
        unsafe_allow_html=True,
    )
    if count is None:
        st.caption(
            "Conversation count and conversation drill-down are unavailable in the current "
            "workspace JSON contract."
        )
    st.header("Aggregate Metrics")
    st.markdown(_workspace_kpis(report), unsafe_allow_html=True)
