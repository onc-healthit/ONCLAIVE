"""Upload screen."""

from __future__ import annotations

from html import escape
from typing import Callable

import streamlit as st

from data.validator import ValidatedUpload, evaluate_uploads, validate_content


def _capture_upload(uploader_key: str, mode: str) -> None:
    """Move selected files into the mode-specific managed list and reset the picker."""
    selected = st.session_state.get(uploader_key)
    selected_files = selected if isinstance(selected, list) else [selected] if selected else []
    stored = st.session_state.setdefault("uploaded_reports", [])
    limit = (
        1
        if mode in {"visualize", "single_conversation", "workspace"}
        else 2
        if mode == "compare"
        else None
    )
    remaining = max(0, limit - len(stored)) if limit is not None else len(selected_files)
    for uploaded_file in selected_files[:remaining]:
        stored.append({"name": uploaded_file.name, "content": uploaded_file.getvalue()})
    if len(selected_files) > remaining:
        noun = "report" if limit == 1 else "reports"
        st.session_state.upload_notice = (
            f"This mode accepts {limit} {noun}. Extra files were not added."
        )
    st.session_state.uploader_generation += 1


def _remove_upload(index: int) -> None:
    stored = st.session_state.get("uploaded_reports", [])
    if 0 <= index < len(stored):
        stored.pop(index)
    st.session_state.uploader_generation += 1


def _file_row(item: ValidatedUpload, index: int) -> None:
    with st.container(key=f"file_entry_{index}"):
        details, action = st.columns([12, 1], gap="small", vertical_alignment="center")
        with details:
            agent = item.report.agent_label if item.valid and item.report else None
            state = f"{agent} · Validated" if agent else "Needs attention"
            state_class = "file-valid" if item.valid else "file-invalid"
            st.markdown(
                '<div class="file-row">'
                f'<span class="file-name">{escape(item.filename)}</span>'
                f'<span class="{state_class}">{escape(state)}</span></div>',
                unsafe_allow_html=True,
            )
        with action:
            st.button(
                "×",
                key=f"remove_upload_{index}",
                help=f"Clear {item.filename}",
                on_click=_remove_upload,
                args=(index,),
            )


def render_mode_selection(on_select: Callable[[str], None]) -> None:
    """Render the uploader-free initial choice between the two workflows."""
    with st.container(key="mode_selection"):
        view, compare = st.columns(2, gap="medium")
        with view:
            st.button(
                "View Agent Results",
                key="choose_view",
                on_click=on_select,
                args=("view",),
                use_container_width=True,
            )
        with compare:
            st.button(
                "Compare Agents",
                key="choose_compare",
                on_click=on_select,
                args=("compare",),
                use_container_width=True,
            )


def render_scope_selection(
    on_select: Callable[[str], None],
    on_back: Callable[[], None] | None = None,
) -> None:
    """Render the uploader-free scope choice for viewing agent results."""
    with st.container(key="scope_selection"):
        if on_back is not None:
            st.button(
                "← Back",
                key="back_to_top_modes",
                on_click=on_back,
                help="Return to agent result options",
            )
        st.subheader("View Agent Results")
        single, multiple, workspace = st.columns(3, gap="medium")
        choices = (
            (single, "Single Conversation", "single_conversation", "choose_single_conversation"),
            (
                multiple,
                "Multiple Conversations",
                "multiple_conversations",
                "choose_multiple_conversations",
            ),
            (workspace, "Workspace", "workspace", "choose_workspace"),
        )
        for column, label, value, key in choices:
            with column:
                st.button(
                    label,
                    key=key,
                    on_click=on_select,
                    args=(value,),
                    use_container_width=True,
                )


def render_upload_card(
    uploader_key: str,
    mode: str,
    on_back: Callable[[], None],
) -> tuple[list[ValidatedUpload], list[str]]:
    configuration = {
        "visualize": (1, "Single Conversation", "Upload one conversation JSON report."),
        "single_conversation": (1, "Single Conversation", "Upload one conversation JSON report."),
        "multiple_conversations": (
            None,
            "Multiple Conversations",
            "Upload at least two conversation JSON reports from the same agent.",
        ),
        "workspace": (1, "Workspace", "Upload one workspace-level JSON report."),
        "compare": (2, "Compare Reports", "Upload one Codex report and one Claude Code report."),
    }
    if mode not in configuration:
        raise ValueError("unsupported upload mode")
    limit, title, caption = configuration[mode]

    with st.container(border=True, key="upload_card"):
        st.button(
            "← Back",
            key="back_to_modes",
            on_click=on_back,
            help="Return to report options",
        )
        st.subheader(title)
        st.caption(caption)
        st.file_uploader(
            "JSON reports",
            type=["json"],
            accept_multiple_files=mode in {"compare", "multiple_conversations"},
            label_visibility="collapsed",
            key=uploader_key,
            help=caption,
            on_change=_capture_upload,
            args=(uploader_key, mode),
        )

        stored_items = st.session_state.get("uploaded_reports", [])
        stored = stored_items[:limit] if limit is not None else stored_items
        validated = [validate_content(item["name"], item["content"]) for item in stored]
        count = len(validated)
        for index, item in enumerate(validated):
            _file_row(item, index)

        notice = st.session_state.pop("upload_notice", None)
        if notice:
            st.info(notice)

        decision = evaluate_uploads(validated, mode)
        for error in decision.errors:
            st.warning(error)

        with st.container(key="upload_actions"):
            counter_column, button_column = st.columns(
                [5.2, 1.7], gap="small", vertical_alignment="bottom"
            )
            with counter_column:
                count_text = (
                    f'{count} / {limit} {"file" if limit == 1 else "files"}'
                    if limit is not None
                    else f'{count} {"file" if count == 1 else "files"}'
                )
                st.markdown(
                    f'<div class="file-count">{len(decision.valid_items)} valid · '
                    f'{count_text}</div>',
                    unsafe_allow_html=True,
                )
            with button_column:
                clicked = st.button(
                    decision.cta_label,
                    key="report_action",
                    disabled=not decision.ready,
                    use_container_width=True,
                )
        if clicked:
            st.session_state.report_payloads = [item.payload for item in decision.valid_items]
            st.session_state.dashboard_mode = decision.mode
            st.session_state.screen = "dashboard"
            st.rerun()
    return validated, list(decision.errors)
