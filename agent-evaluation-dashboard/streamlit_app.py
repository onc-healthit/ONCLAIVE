"""ONCLAIVE Agent Evaluation Dashboard entry point."""

import streamlit as st

from components.core_metrics import render_core_metrics
from components.header import render_header, render_single_context
from components.metadata import render_metadata
from components.overview import (
    render_multiple_summary,
    render_multiple_overview,
    render_workspace_overview,
)
from components.styles import apply_styles
from components.takeaway_cards import render_takeaways
from components.token_usage import render_token_usage
from components.upload import render_scope_selection, render_upload_card
from data.aggregation import conversation_name
from data.comparison import order_reports
from data.loader import load_report


DEMO_VIEW_RESULTS_ONLY = True


st.set_page_config(
    page_title="ONCLAIVE Agent Evaluation Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)
apply_styles()

if "screen" not in st.session_state:
    st.session_state.screen = "upload"
if "uploader_generation" not in st.session_state:
    st.session_state.uploader_generation = 0
if "uploaded_reports" not in st.session_state:
    st.session_state.uploaded_reports = []
if "upload_mode" not in st.session_state:
    st.session_state.upload_mode = "view"
if "view_scope" not in st.session_state:
    st.session_state.view_scope = None


def _reset_upload_state() -> None:
    st.session_state.pop("report_payloads", None)
    st.session_state.uploaded_reports = []
    st.session_state.pop("upload_notice", None)
    st.session_state.pop("dashboard_mode", None)
    st.session_state.uploader_generation += 1


def select_upload_mode(mode: str) -> None:
    _reset_upload_state()
    st.session_state.upload_mode = mode
    st.session_state.view_scope = None
    st.session_state.screen = "upload"


def select_view_scope(scope: str) -> None:
    _reset_upload_state()
    st.session_state.upload_mode = "view"
    st.session_state.view_scope = scope
    st.session_state.screen = "upload"


def show_scope_selection() -> None:
    _reset_upload_state()
    st.session_state.upload_mode = "view"
    st.session_state.view_scope = None
    st.session_state.screen = "upload"


def show_mode_selection() -> None:
    """Legacy reset target; this demo branch returns directly to result scopes."""
    show_scope_selection()


def replace_reports() -> None:
    show_scope_selection()


if st.session_state.screen in {"dashboard", "comparison"} and st.session_state.get(
    "report_payloads"
):
    try:
        reports = [load_report(payload) for payload in st.session_state.report_payloads]
        dashboard_mode = st.session_state.get("dashboard_mode")
        if dashboard_mode is None:
            dashboard_mode = "comparison" if len(reports) == 2 else "single"
        if DEMO_VIEW_RESULTS_ONLY and dashboard_mode == "comparison":
            replace_reports()
            st.rerun()
        if dashboard_mode == "comparison":
            reports = list(order_reports(reports))
        elif dashboard_mode == "multiple":
            if len(reports) < 2 or len({report.agent_key for report in reports}) != 1:
                raise ValueError("Expected at least two same-agent conversation reports")
        elif dashboard_mode in {"single", "workspace"}:
            if len(reports) != 1:
                raise ValueError("Expected exactly one report")
        else:
            raise ValueError("Unsupported dashboard mode")
    except (TypeError, ValueError):
        replace_reports()
        st.rerun()

    if dashboard_mode == "single":
        render_header(reports, on_replace=replace_reports)
        render_core_metrics(reports)
        render_token_usage(reports)
        render_metadata(reports)
    elif dashboard_mode == "comparison":
        render_header(reports, on_replace=replace_reports)
        render_takeaways(reports[0], reports[1])
        render_core_metrics(reports)
        render_metadata(reports)
    elif dashboard_mode == "multiple":
        render_header(on_replace=replace_reports)
        tab_names = ["Overview", *[conversation_name(report) for report in reports]]
        tabs = st.tabs(tab_names)
        with tabs[0]:
            render_multiple_summary(reports)
            render_multiple_overview(reports)
        for index, (tab, report) in enumerate(zip(tabs[1:], reports)):
            with tab:
                render_single_context(report)
                render_core_metrics([report])
                render_token_usage([report], key_suffix=f"conversation_{index}")
                render_metadata([report], key_suffix=f"conversation_{index}")
    else:
        render_header(on_replace=replace_reports)
        render_workspace_overview(reports[0])
        render_token_usage(reports, key_suffix="workspace_overview")
        render_metadata(reports, key_suffix="workspace_overview")
else:
    render_header()
    if DEMO_VIEW_RESULTS_ONLY and st.session_state.upload_mode != "view":
        show_scope_selection()
    if st.session_state.upload_mode == "view" and st.session_state.view_scope is None:
        render_scope_selection(select_view_scope)
    else:
        upload_mode = (
            st.session_state.view_scope
            if st.session_state.upload_mode == "view"
            else st.session_state.upload_mode
        )
        render_upload_card(
            f"report_uploader_{st.session_state.uploader_generation}",
            upload_mode,
            show_scope_selection,
        )
