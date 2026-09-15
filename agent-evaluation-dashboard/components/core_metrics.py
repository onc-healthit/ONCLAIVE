"""Reusable single-report and comparison metric visualizations."""

from __future__ import annotations

from html import escape
import math
from typing import Sequence

import plotly.graph_objects as go
import streamlit as st

from data.comparison import (
    CORE_METRICS,
    TOKEN_METRICS,
    MetricDefinition,
    format_value,
    is_number,
    metric_for,
)
from data.loader import AgentReport, Metric


AGENT_COLORS = {
    "codex": "#5F7F6B",
    "claude_code": "#C6763D",
}

SINGLE_CORE_METRICS = (
    ("Run Time", CORE_METRICS[0]),
    ("Estimated Cost", CORE_METRICS[1]),
    ("Human Prompts", CORE_METRICS[2]),
    ("Tool Calls", CORE_METRICS[3]),
    ("File Edits", CORE_METRICS[4]),
)

COMPARISON_CORE_METRICS = (
    ("Run Time", CORE_METRICS[0]),
    ("Estimated Cost", CORE_METRICS[1]),
    ("Human Prompts", CORE_METRICS[2]),
    ("Tool Calls", CORE_METRICS[3]),
    ("File Edits", CORE_METRICS[4]),
    ("Total Tokens", CORE_METRICS[5]),
)

AXIS_TITLES = {
    "wall_clock_time_seconds": "Time",
    "estimated_cost": "USD",
    "human_prompts_required": "Prompts",
    "tool_calls": "Tool calls",
    "file_edits": "File edits",
    "total_tokens": "Tokens",
}

COMPARISON_DISPLAY_LABELS = {
    definition.names[0]: label for label, definition in COMPARISON_CORE_METRICS
}


def _status_value(metric: Metric) -> str:
    status = metric.status if metric.value is not None else "missing"
    return status if status in {"computed", "partial", "missing", "estimated"} else "missing"


def _nice_step(maximum: float, integer: bool) -> float:
    if maximum <= 0:
        return 1.0
    rough = maximum / 3
    magnitude = 10 ** math.floor(math.log10(rough))
    fraction = rough / magnitude
    nice_fraction = 1 if fraction <= 1 else 2 if fraction <= 2 else 5 if fraction <= 5 else 10
    step = nice_fraction * magnitude
    return max(1.0, step) if integer else step


def _duration_label(value: float) -> str:
    if value >= 60:
        minutes, seconds = divmod(round(value), 60)
        return f"{minutes}m {seconds:02d}s"
    formatted = f"{value:.1f}".rstrip("0").rstrip(".")
    return f"{formatted}s"


def _token_tick_label(value: float) -> str:
    if abs(value) >= 1_000_000:
        return f"{value / 1_000_000:g}M"
    if abs(value) >= 1_000:
        return f"{value / 1_000:g}k"
    return f"{value:,.0f}"


def _axis_tick_label(value: float, definition: MetricDefinition) -> str:
    if definition.kind == "duration":
        return _duration_label(value)
    if definition.kind == "currency":
        return f"${value:,.2f}" if value < 10 else f"${value:,.0f}"
    if definition.names[0] == "total_tokens":
        return _token_tick_label(value)
    return f"{value:,.0f}"


def _axis_scale(values: Sequence[float | None], definition: MetricDefinition) -> tuple[float, list[float], list[str]]:
    numeric = [value for value in values if value is not None]
    maximum = max(numeric, default=0.0)
    integer = definition.kind == "integer"
    step = _nice_step(maximum, integer)
    axis_max = math.ceil(maximum / step) * step if maximum > 0 else step
    if maximum > 0 and math.isclose(axis_max, maximum):
        axis_max += step
    tick_count = int(round(axis_max / step))
    tick_values = [index * step for index in range(tick_count + 1)]
    tick_text = [_axis_tick_label(value, definition) for value in tick_values]
    return axis_max, tick_values, tick_text


def _base_layout(
    figure: go.Figure,
    values: Sequence[float | None],
    definition: MetricDefinition,
    *,
    stacked: bool = False,
) -> float:
    axis_max, tick_values, tick_text = _axis_scale(values, definition)
    padded_axis_max = axis_max * 1.06
    figure.update_layout(
        height=224,
        margin={"l": 82, "r": 10, "t": 8, "b": 38},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        bargap=0.42,
        barmode="stack" if stacked else "group",
        hovermode="closest",
        hoverlabel={
            "bgcolor": "#2E2B27",
            "bordercolor": "#2E2B27",
            "font": {"color": "#FFFFFF", "size": 13, "family": "Inter, sans-serif"},
        },
        legend={
            "orientation": "h",
            "traceorder": "normal",
            "x": 0.5,
            "xanchor": "center",
            "y": 1.03,
            "yanchor": "bottom",
            "font": {"color": "#514E49", "size": 11},
        },
        xaxis={
            "fixedrange": True,
            "showgrid": False,
            "zeroline": False,
            "tickfont": {"color": "#33312E", "size": 11},
            "linecolor": "#DEDAD3",
            "automargin": True,
        },
        yaxis={
            "fixedrange": True,
            "range": [0, padded_axis_max],
            "tickmode": "array",
            "tickvals": tick_values,
            "ticktext": tick_text,
            "showgrid": True,
            "gridcolor": "#ECE8E2",
            "gridwidth": 1,
            "showline": False,
            "zeroline": False,
            "tickfont": {"color": "#716E68", "size": 10},
            "title": {
                "text": AXIS_TITLES[definition.names[0]],
                "font": {"color": "#716E68", "size": 10},
                "standoff": 16,
            },
            "automargin": True,
        },
        font={"family": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},
    )
    return padded_axis_max


def _annotate_missing(
    figure: go.Figure, labels: Sequence[str], values: Sequence[float | None], axis_max: float
) -> None:
    for label, value in zip(labels, values):
        if value is None:
            figure.add_annotation(
                x=label,
                y=axis_max * 0.08,
                text="N/A",
                showarrow=False,
                font={"size": 11, "color": "#716E68"},
            )


def build_total_tokens_figure(reports: Sequence[AgentReport]) -> go.Figure:
    labels = [report.agent_label for report in reports]
    total_metrics = [metric_for(report, CORE_METRICS[5]) for report in reports]
    input_metrics = [metric_for(report, TOKEN_METRICS[0]) for report in reports]
    output_metrics = [metric_for(report, TOKEN_METRICS[1]) for report in reports]
    totals = [float(metric.value) if is_number(metric.value) else None for metric in total_metrics]
    input_visual: list[float | None] = []
    output_visual: list[float | None] = []
    customdata: list[list[str]] = []
    for report, total, input_metric, output_metric in zip(
        reports, total_metrics, input_metrics, output_metrics
    ):
        can_stack = (
            is_number(total.value)
            and is_number(input_metric.value)
            and is_number(output_metric.value)
        )
        composition = (
            float(input_metric.value) + float(output_metric.value) if can_stack else 0.0
        )
        if can_stack and composition > 0:
            total_value = float(total.value)
            input_visual.append(total_value * float(input_metric.value) / composition)
            output_visual.append(total_value * float(output_metric.value) / composition)
        elif can_stack and float(total.value) == 0:
            input_visual.append(0.0)
            output_visual.append(0.0)
        else:
            input_visual.append(None)
            output_visual.append(None)
        customdata.append(
            [
                report.agent_label,
                format_value(total.value, "integer"),
                format_value(input_metric.value, "integer"),
                format_value(output_metric.value, "integer"),
            ]
        )

    figure = go.Figure()
    figure.add_trace(
        go.Bar(
            name="Input",
            x=labels,
            y=input_visual,
            customdata=customdata,
            marker={"color": ["#5F7F6B", "#C6763D"]},
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Total Tokens: %{customdata[1]}<br>"
                "Input Tokens: %{customdata[2]}<br>"
                "Output Tokens: %{customdata[3]}<extra></extra>"
            ),
        )
    )
    figure.add_trace(
        go.Bar(
            name="Output",
            x=labels,
            y=output_visual,
            customdata=customdata,
            marker={
                "color": ["#A4B8AA", "#E2AD86"],
                "pattern": {"shape": ["/", "/"], "solidity": 0.18},
            },
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Total Tokens: %{customdata[1]}<br>"
                "Input Tokens: %{customdata[2]}<br>"
                "Output Tokens: %{customdata[3]}<extra></extra>"
            ),
        )
    )
    axis_max = _base_layout(figure, totals, CORE_METRICS[5], stacked=True)
    plotted_totals = [
        total if input_value is not None and output_value is not None else None
        for total, input_value, output_value in zip(totals, input_visual, output_visual)
    ]
    _annotate_missing(figure, labels, plotted_totals, axis_max)
    return figure


def build_metric_figure(
    reports: Sequence[AgentReport], definition: MetricDefinition
) -> go.Figure:
    """Build one independently scaled comparison chart for a metric card."""
    if len(reports) != 2:
        raise ValueError("Comparison metric charts require exactly two reports")
    if definition.names[0] == "total_tokens":
        return build_total_tokens_figure(reports)

    labels = [report.agent_label for report in reports]
    metrics = [metric_for(report, definition) for report in reports]
    values = [float(metric.value) if is_number(metric.value) else None for metric in metrics]
    customdata = [
        [
            report.agent_label,
            format_value(metric.value, definition.kind),
            _status_value(metric),
            metric.source or "Not provided",
        ]
        for report, metric in zip(reports, metrics)
    ]
    colors = [AGENT_COLORS[report.agent_key] for report in reports]
    display_label = COMPARISON_DISPLAY_LABELS[definition.names[0]]
    figure = go.Figure(
        go.Bar(
            x=labels,
            y=values,
            customdata=customdata,
            marker={"color": colors, "line": {"color": colors, "width": 1}},
            width=0.56,
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                f"{escape(display_label)}: %{{customdata[1]}}<br>"
                "Status: %{customdata[2]}<br>"
                "Source: %{customdata[3]}<extra></extra>"
            ),
        )
    )
    axis_max = _base_layout(figure, values, definition)
    _annotate_missing(figure, labels, values, axis_max)
    return figure


def _single_kpi_card(
    report: AgentReport, label: str, definition: MetricDefinition
) -> str:
    """Render a compact, value-first KPI without implying an arbitrary scale."""
    metric = metric_for(report, definition)
    value = format_value(metric.value, definition.kind)
    return (
        '<div class="single-kpi-card">'
        f'<div class="single-kpi-label">{escape(label)}</div>'
        f'<div class="single-kpi-value">{escape(value)}</div>'
        "</div>"
    )


def render_core_metrics(reports: Sequence[AgentReport]) -> None:
    st.header("Core Metrics")
    if len(reports) == 1:
        cards = "".join(
            _single_kpi_card(reports[0], label, definition)
            for label, definition in SINGLE_CORE_METRICS
        )
        st.markdown(f'<div class="single-kpi-grid">{cards}</div>', unsafe_allow_html=True)
        return

    with st.container(key="core_metric_grid"):
        columns = st.columns(len(COMPARISON_CORE_METRICS), gap="small")
        for index, (column, (label, definition)) in enumerate(
            zip(columns, COMPARISON_CORE_METRICS)
        ):
            with column:
                with st.container(border=True, key=f"metric_card_{index}"):
                    st.markdown(
                        '<div class="metric-header">'
                        f'<div class="metric-title">{escape(label)}</div></div>',
                        unsafe_allow_html=True,
                    )
                    st.plotly_chart(
                        build_metric_figure(reports, definition),
                        key=f"metric_chart_{definition.names[0]}",
                        config={
                            "displayModeBar": False,
                            "displaylogo": False,
                            "scrollZoom": False,
                            "responsive": True,
                        },
                        use_container_width=True,
                    )
