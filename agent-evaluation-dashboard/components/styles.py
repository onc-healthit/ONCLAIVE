"""Light, readable visual system for the ONCLAIVE dashboard."""

import streamlit as st


def apply_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bg: #F6F4EF;
            --surface: #FFFFFF;
            --surface-soft: #FAF9F6;
            --border: #DEDAD3;
            --border-strong: #CBC5BB;
            --text: #2E2B27;
            --muted: #716E68;
            --muted-strong: #514E49;
            --accent: #BF4E2E;
            --accent-soft: #F8E9E2;
            --codex: #5F7F6B;
            --claude: #C6763D;
            --warning: #A85C24;
        }

        html, body { max-width: 100%; overflow-x: hidden; }
        .stApp, .stApp *:not([data-testid="stIconMaterial"]) {
            font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
        }
        .stApp *, .stApp *::before, .stApp *::after { box-sizing: border-box; }
        .stApp { color: var(--text); background: var(--bg); }
        [data-testid="stHeader"] { background: rgba(246, 244, 239, 0.92); }
        .block-container {
            width: 100%;
            max-width: 1220px;
            padding: 2.4rem 2.5rem 4rem;
            overflow-x: hidden;
        }

        h1, h2, h3 { color: var(--text) !important; }
        h1 {
            margin-bottom: 0.3rem !important;
            font-size: clamp(1.85rem, 3vw, 2.65rem) !important;
            font-weight: 720 !important;
            letter-spacing: -0.04em;
            line-height: 1.12 !important;
        }
        h2 {
            margin-top: 2.45rem !important;
            margin-bottom: 0.65rem !important;
            font-size: 1.25rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }
        h3 { font-size: 1.08rem !important; font-weight: 680 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: var(--muted); }
        [data-testid="stCaptionContainer"] { font-size: 0.86rem; line-height: 1.55; }

        .st-key-dashboard_header,
        .st-key-dashboard_header [data-testid="stColumn"] { min-width: 0; }
        .header-meta {
            min-height: 1.25rem;
            color: var(--muted);
            font-size: 0.82rem;
            line-height: 1.5;
            overflow-wrap: anywhere;
        }
        .header-meta-label { color: var(--muted); }
        .header-meta-value { color: var(--muted-strong); font-weight: 500; }
        .header-meta-sep { margin: 0 0.35rem; color: #A8A39B; }
        .header-meta-report { display: block; min-width: 0; overflow-wrap: anywhere; }
        .header-single-meta { margin-top: 0.85rem; }
        .header-comparison-meta { margin-top: 0.75rem; }
        .comparison-header-context {
            display: flex;
            min-width: 0;
            flex-direction: column;
            gap: 0.18rem;
        }
        .comparison-header-agents {
            color: var(--text);
            font-size: 0.98rem;
            font-weight: 680;
        }
        .comparison-header-models {
            color: var(--muted);
            font-size: 0.8rem;
            font-weight: 520;
            line-height: 1.45;
            overflow-wrap: anywhere;
        }
        .comparison-header-models span { margin: 0 0.25rem; color: #A8A39B; }
        .single-run-context {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            min-width: 0;
            gap: 0.65rem 1rem;
            padding: 0.35rem 0 0;
        }
        .single-run-context-item {
            display: flex;
            min-width: 0;
            flex-direction: column;
            gap: 0.12rem;
        }
        .single-run-context-label {
            color: var(--muted);
            font-size: 0.66rem;
            font-weight: 700;
            letter-spacing: 0.055em;
            text-transform: uppercase;
        }
        .single-run-context-value {
            min-width: 0;
            color: var(--muted-strong);
            font-size: 0.8rem;
            font-weight: 560;
            line-height: 1.4;
            overflow-wrap: anywhere;
        }
        .st-key-replace_reports { display: flex; justify-content: flex-end; padding-top: 0.55rem; }
        .st-key-replace_reports button { max-width: 100%; white-space: nowrap; }

        .st-key-mode_selection {
            width: min(82%, 900px);
            max-width: 100%;
            margin-top: 1.8rem;
        }
        .st-key-mode_selection [data-testid="stHorizontalBlock"] {
            align-items: stretch;
            gap: 1rem;
        }
        .st-key-mode_selection [data-testid="stColumn"] { min-width: 0; }
        .stApp .st-key-choose_view,
        .stApp .st-key-choose_compare,
        .stApp .st-key-choose_view [data-testid="stButton"],
        .stApp .st-key-choose_compare [data-testid="stButton"] { height: 100%; }
        .stApp .st-key-choose_view button,
        .stApp .st-key-choose_compare button {
            width: 100% !important;
            min-height: 148px;
            border: 1px solid var(--border-strong);
            border-radius: 13px;
            color: var(--text);
            background: var(--surface);
            box-shadow: 0 3px 12px rgba(55, 48, 39, 0.05);
            transition: color 170ms ease, background-color 170ms ease, border-color 170ms ease,
                        box-shadow 170ms ease, transform 170ms ease;
        }
        .stApp .st-key-choose_view button p,
        .stApp .st-key-choose_compare button p {
            color: var(--text) !important;
            font-size: 1.08rem;
            font-weight: 700;
        }
        .stApp .st-key-choose_view button:hover,
        .stApp .st-key-choose_compare button:hover {
            border-color: #C96343;
            color: #7E301B;
            background: #FFF6F1;
            box-shadow: 0 7px 18px rgba(157, 66, 38, 0.12);
            transform: translateY(-2px);
        }
        .stApp .st-key-choose_view button:hover p,
        .stApp .st-key-choose_compare button:hover p { color: #7E301B !important; }

        .st-key-scope_selection {
            width: min(96%, 1080px);
            max-width: 100%;
            margin-top: 1.4rem;
        }
        .st-key-scope_selection [data-testid="stHorizontalBlock"] {
            align-items: stretch;
            gap: 0.9rem;
        }
        .st-key-scope_selection [data-testid="stColumn"] { min-width: 0; }
        .stApp .st-key-choose_single_conversation,
        .stApp .st-key-choose_multiple_conversations,
        .stApp .st-key-choose_workspace,
        .stApp .st-key-choose_single_conversation [data-testid="stButton"],
        .stApp .st-key-choose_multiple_conversations [data-testid="stButton"],
        .stApp .st-key-choose_workspace [data-testid="stButton"] { height: 100%; }
        .stApp .st-key-choose_single_conversation button,
        .stApp .st-key-choose_multiple_conversations button,
        .stApp .st-key-choose_workspace button {
            width: 100% !important;
            min-height: 132px;
            border: 1px solid var(--border-strong);
            border-radius: 13px;
            color: var(--text);
            background: var(--surface);
            box-shadow: 0 3px 12px rgba(55, 48, 39, 0.05);
            transition: color 170ms ease, background-color 170ms ease, border-color 170ms ease,
                        box-shadow 170ms ease, transform 170ms ease;
        }
        .stApp .st-key-choose_single_conversation button p,
        .stApp .st-key-choose_multiple_conversations button p,
        .stApp .st-key-choose_workspace button p {
            color: var(--text) !important;
            font-size: 1rem;
            font-weight: 700;
        }
        .stApp .st-key-choose_single_conversation button:hover,
        .stApp .st-key-choose_multiple_conversations button:hover,
        .stApp .st-key-choose_workspace button:hover {
            border-color: #C96343;
            color: #7E301B;
            background: #FFF6F1;
            box-shadow: 0 7px 18px rgba(157, 66, 38, 0.12);
            transform: translateY(-2px);
        }
        .stApp .st-key-choose_single_conversation button:hover p,
        .stApp .st-key-choose_multiple_conversations button:hover p,
        .stApp .st-key-choose_workspace button:hover p { color: #7E301B !important; }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border: 1px solid var(--border);
            border-radius: 14px;
            background: var(--surface);
            box-shadow: 0 3px 12px rgba(55, 48, 39, 0.045);
        }
        .st-key-upload_card {
            width: min(82%, 900px);
            max-width: 100%;
            margin-top: 1.8rem;
        }
        .st-key-upload_card [data-testid="stVerticalBlock"] { gap: 0.75rem; }
        .st-key-upload_card h3 { margin-bottom: 0 !important; }

        [data-testid="stFileUploader"],
        [data-testid="stFileUploader"] section,
        [data-testid="stFileUploaderDropzone"],
        [data-testid="stFileUploaderDropzone"] > div {
            color: var(--text) !important;
            background: var(--surface) !important;
        }
        [data-testid="stFileUploaderDropzone"] {
            width: 100%;
            min-width: 0;
            min-height: 142px;
            border: 1px dashed #B9B2A8 !important;
            border-radius: 11px;
            transition: border-color 160ms ease, background-color 160ms ease;
        }
        [data-testid="stFileUploaderDropzone"]:hover {
            border-color: var(--accent) !important;
            background: #FFF9F5 !important;
        }
        [data-testid="stFileUploaderDropzone"]:hover > div {
            background: #FFF9F5 !important;
        }
        .stApp [data-testid="stFileUploaderDropzone"] button {
            min-height: 38px;
            padding: 0.45rem 0.9rem;
            border: 1px solid var(--border-strong) !important;
            border-radius: 8px;
            color: var(--text) !important;
            background: var(--surface) !important;
            box-shadow: 0 1px 3px rgba(55, 48, 39, 0.06);
            font-size: 0.82rem;
            font-weight: 650;
            transition: color 160ms ease, background-color 160ms ease, border-color 160ms ease,
                        box-shadow 160ms ease;
        }
        .stApp [data-testid="stFileUploaderDropzone"] button p { color: var(--text) !important; }
        .stApp [data-testid="stFileUploaderDropzone"] button:hover {
            border-color: #C96343 !important;
            color: #7E301B !important;
            background: var(--accent-soft) !important;
            box-shadow: 0 3px 8px rgba(157, 66, 38, 0.11);
        }
        .stApp [data-testid="stFileUploaderDropzone"] button:hover p { color: #7E301B !important; }
        [data-testid="stFileUploaderDropzone"] svg { color: var(--muted-strong) !important; }
        [data-testid="stFileUploaderDropzoneInstructions"] { min-width: 0; }
        [data-testid="stFileUploaderDropzoneInstructions"] span { color: var(--text) !important; }
        [data-testid="stFileUploaderDropzoneInstructions"] small { color: var(--muted) !important; }
        [data-testid="stFileUploaderFile"] {
            color: var(--text) !important;
            background: var(--surface-soft) !important;
        }

        .file-count {
            display: flex;
            align-items: center;
            min-height: 39px;
            color: var(--muted-strong);
            font-size: 0.82rem;
            font-weight: 600;
        }
        [class*="st-key-file_entry_"] {
            padding: 0.35rem 0.4rem 0.35rem 0.8rem;
            border: 1px solid var(--border);
            border-radius: 9px;
            background: var(--surface-soft);
        }
        [class*="st-key-file_entry_"] [data-testid="stHorizontalBlock"] {
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            align-items: center;
        }
        [class*="st-key-file_entry_"] [data-testid="stColumn"] {
            display: flex;
            align-items: center;
            min-width: 0;
        }
        [class*="st-key-file_entry_"] [data-testid="stColumn"]:first-child,
        [class*="st-key-file_entry_"] [data-testid="stMarkdownContainer"],
        [class*="st-key-file_entry_"] [data-testid="stMarkdownContainer"] > div { width: 100%; }
        [class*="st-key-file_entry_"] [data-testid="stColumn"]:last-child { justify-content: flex-end; }
        .file-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            min-height: 31px;
            min-width: 0;
            gap: 0.8rem;
        }
        .file-name {
            flex: 1 1 auto;
            min-width: 0;
            overflow: hidden;
            color: var(--text);
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace !important;
            font-size: 0.79rem;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .file-valid, .file-invalid {
            flex: 0 0 auto;
            font-size: 0.76rem;
            font-weight: 650;
            white-space: nowrap;
        }
        .file-valid { color: #496854; }
        .file-invalid { color: var(--warning); }

        [data-testid="stButton"] button {
            min-height: 39px;
            padding: 0.45rem 0.85rem;
            border: 1px solid var(--border-strong);
            border-radius: 8px;
            color: var(--text);
            background: var(--surface);
            font-size: 0.82rem;
            font-weight: 650;
            transition: color 160ms ease, background-color 160ms ease, border-color 160ms ease,
                        box-shadow 160ms ease, transform 160ms ease;
        }
        [data-testid="stButton"] button:hover {
            border-color: #AFA79D;
            background: var(--surface-soft);
        }
        .st-key-back_to_modes,
        .st-key-back_to_top_modes {
            width: fit-content;
            margin-bottom: -0.15rem;
        }
        .st-key-back_to_modes button,
        .st-key-back_to_top_modes button {
            min-height: 31px;
            padding: 0.25rem 0.45rem;
            border-color: transparent;
            color: var(--muted-strong);
            background: transparent;
            box-shadow: none;
        }
        .st-key-back_to_modes button p,
        .st-key-back_to_top_modes button p {
            color: var(--muted-strong) !important;
            font-size: 0.8rem;
        }
        .st-key-back_to_modes button:hover,
        .st-key-back_to_top_modes button:hover {
            border-color: #E7C8B8;
            color: var(--accent);
            background: var(--accent-soft);
            transform: none;
        }
        .st-key-back_to_modes button:hover p,
        .st-key-back_to_top_modes button:hover p { color: var(--accent) !important; }
        [class*="st-key-remove_upload_"] button {
            display: flex;
            width: 31px !important;
            min-width: 31px !important;
            min-height: 31px !important;
            padding: 0 !important;
            align-items: center;
            justify-content: center;
            border-color: transparent;
            color: var(--muted);
            background: transparent;
            font-size: 1.05rem;
        }
        [class*="st-key-remove_upload_"] button p { margin: 0; line-height: 1; }
        [class*="st-key-remove_upload_"] button:hover {
            color: var(--text);
            border-color: var(--border);
            background: #F1EEE9;
        }
        .st-key-upload_actions [data-testid="stHorizontalBlock"] {
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            align-items: flex-end;
        }
        .st-key-upload_actions [data-testid="stColumn"] { min-width: 0; }
        .st-key-report_action { width: 100%; min-width: 0; }
        .st-key-report_action button {
            width: 100% !important;
            white-space: nowrap;
            border-color: #37332F;
            color: #FFFFFF;
            background: #37332F;
            box-shadow: 0 2px 6px rgba(45, 40, 35, 0.12);
        }
        .st-key-report_action button p { color: #FFFFFF !important; }
        .st-key-report_action button:hover {
            border-color: #A43E22;
            color: #FFFFFF;
            background: var(--accent);
            box-shadow: 0 4px 10px rgba(153, 62, 35, 0.18);
            transform: translateY(-1px);
        }
        .st-key-report_action button:hover p { color: #FFFFFF !important; }
        .st-key-report_action button:disabled {
            border-color: #DDD8D0;
            color: #A5A099;
            background: #ECE9E4;
            box-shadow: none;
            transform: none;
        }
        .st-key-report_action button:disabled p { color: #A5A099 !important; }

        .agent-codex, .agent-claude { color: var(--text) !important; }
        .agent-label::before {
            display: inline-block;
            width: 7px;
            height: 7px;
            margin-right: 7px;
            border-radius: 999px;
            background: var(--muted);
            content: "";
            vertical-align: 0.05em;
        }
        .agent-label.agent-codex::before { background: var(--codex); }
        .agent-label.agent-claude::before { background: var(--claude); }

        .comparison-takeaway-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.9rem;
        }
        .comparison-takeaway {
            display: flex;
            min-width: 0;
            min-height: 112px;
            flex-direction: column;
            justify-content: center;
            padding: 1.2rem 1.3rem;
            border: 1px solid var(--border);
            border-radius: 11px;
            background: var(--surface);
            box-shadow: 0 2px 8px rgba(55, 48, 39, 0.035);
        }
        .comparison-takeaway-label {
            color: var(--muted-strong);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.075em;
            text-transform: uppercase;
        }
        .comparison-takeaway-value {
            margin-top: 0.5rem;
            color: var(--text);
            font-size: 1.08rem;
            font-weight: 650;
            line-height: 1.4;
            overflow-wrap: anywhere;
        }

        .single-kpi-grid {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            min-width: 0;
            gap: 0.8rem;
        }
        .single-kpi-card {
            display: flex;
            min-width: 0;
            min-height: 108px;
            flex-direction: column;
            align-items: flex-start;
            justify-content: flex-start;
            gap: 0.72rem;
            padding: 1rem 1.05rem;
            border: 1px solid var(--border);
            border-radius: 11px;
            background: var(--surface);
            box-shadow: 0 2px 8px rgba(55, 48, 39, 0.035);
        }
        .single-kpi-label {
            color: var(--muted-strong);
            font-size: 0.78rem;
            font-weight: 680;
            line-height: 1.35;
            overflow-wrap: anywhere;
        }
        .single-kpi-value {
            max-width: 100%;
            margin: 0;
            color: var(--text);
            font-size: clamp(1.32rem, 2.2vw, 1.72rem);
            font-weight: 730;
            font-variant-numeric: tabular-nums;
            letter-spacing: -0.025em;
            line-height: 1.1;
            overflow-wrap: anywhere;
        }

        .overview-context {
            display: flex;
            min-width: 0;
            flex-wrap: wrap;
            gap: 0.65rem;
            margin-top: 0.75rem;
        }
        .overview-context-item {
            display: flex;
            min-width: 150px;
            flex: 1 1 180px;
            flex-direction: column;
            gap: 0.16rem;
            padding: 0.8rem 0.95rem;
            border: 1px solid var(--border);
            border-radius: 9px;
            background: var(--surface);
        }
        .overview-context-label {
            color: var(--muted);
            font-size: 0.66rem;
            font-weight: 700;
            letter-spacing: 0.055em;
            text-transform: uppercase;
        }
        .overview-context-value {
            min-width: 0;
            color: var(--text);
            font-size: 0.9rem;
            font-weight: 650;
            overflow-wrap: anywhere;
        }
        .overview-kpi-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            min-width: 0;
            gap: 0.8rem;
        }
        .multiple-summary {
            max-width: 1040px;
            margin: 0.9rem 0 1.35rem;
            color: var(--text);
            font-size: clamp(1.1rem, 1.55vw, 1.32rem);
            font-weight: 650;
            line-height: 1.45;
            letter-spacing: -0.014em;
        }
        .st-key-conversation_distribution {
            min-width: 0;
            padding: 0.35rem 0.25rem 0.55rem;
        }
        .st-key-conversation_distribution [data-testid="stPlotlyChart"] {
            max-width: 100%;
        }

        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            width: 100%;
            justify-content: flex-start;
            gap: 1.5rem;
            overflow-x: auto;
            scrollbar-width: thin;
        }
        [data-testid="stTabs"] [data-baseweb="tab"] {
            flex: 0 0 auto;
            min-width: max-content;
            padding-right: 0.25rem;
            padding-left: 0.25rem;
            color: var(--muted-strong);
        }

        .st-key-core_metric_grid > div,
        .st-key-core_metric_grid [data-testid="stHorizontalBlock"] { min-width: 0; }
        .st-key-core_metric_grid [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
            gap: 0.85rem !important;
        }
        .st-key-core_metric_grid [data-testid="stColumn"] {
            width: calc(33.333% - 0.57rem) !important;
            min-width: 250px !important;
            flex: 1 1 calc(33.333% - 0.57rem) !important;
        }
        [class*="st-key-metric_card_"] {
            min-width: 0;
            height: 100%;
        }
        [class*="st-key-metric_card_"] > div[data-testid="stVerticalBlockBorderWrapper"] {
            height: 100%;
            padding: 0.2rem 0.55rem 0.65rem;
        }
        [class*="st-key-metric_card_"] [data-testid="stPlotlyChart"] { max-width: 100%; }
        .metric-header {
            display: flex;
            align-items: center;
            min-height: 30px;
            margin: 0.3rem 0.15rem 0;
        }
        .metric-title {
            flex: 1 1 7rem;
            min-width: 0;
            color: var(--text);
            font-size: 0.92rem;
            font-weight: 680;
            overflow-wrap: anywhere;
        }
        .status-group { display: flex; flex: 0 1 auto; flex-wrap: wrap; justify-content: flex-end; gap: 3px; }
        .status {
            display: inline-block;
            padding: 2px 7px;
            border: 1px solid #D6D1CA;
            border-radius: 999px;
            color: #625E58;
            background: #F6F4F0;
            font-size: 0.66rem;
            font-weight: 600;
            line-height: 1.45;
            text-transform: lowercase;
            white-space: nowrap;
        }
        .status-computed { border-color: #C9D7CD; color: #496353; background: #F1F6F2; }
        .status-estimated { border-color: #E6CFB6; color: #8A5A27; background: #FBF4EA; }
        .status-partial { border-color: #E9C7B4; color: #914E2C; background: #FCF0E9; }
        .status-missing { border-color: #D7D3CC; color: #716E68; background: #F3F1ED; }

        .bar-card {
            min-width: 0;
            margin-bottom: 0.65rem;
            padding: 1rem 1.15rem;
            border: 1px solid var(--border);
            border-radius: 11px;
            background: var(--surface);
        }
        .bar-header { margin-bottom: 0.7rem; color: var(--text); font-size: 0.88rem; font-weight: 680; }
        .bar-row {
            display: grid;
            grid-template-columns: minmax(108px, 125px) minmax(80px, 1fr) minmax(74px, 100px);
            align-items: center;
            gap: 0.85rem;
            margin: 0.65rem 0;
            color: var(--muted);
            font-size: 0.82rem;
        }
        .bar-track {
            min-width: 0;
            height: 8px;
            overflow: hidden;
            border-radius: 999px;
            background: #EEEAE4;
        }
        .bar-fill-codex, .bar-fill-claude { height: 100%; border-radius: 999px; }
        .bar-fill-codex { background: var(--codex); }
        .bar-fill-claude { background: var(--claude); }
        .bar-unavailable { color: var(--muted); font-size: 0.76rem; font-style: italic; }
        .bar-number {
            color: var(--muted-strong);
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace !important;
            font-size: 0.78rem;
            font-variant-numeric: tabular-nums;
            text-align: right;
        }

        [class*="st-key-single_token_card"] {
            min-width: 0;
            max-width: 100%;
            overflow: visible;
        }
        [class*="st-key-single_token_card"] [data-testid="stVerticalBlock"],
        [class*="st-key-single_token_card"] [data-testid="stMarkdownContainer"] { overflow: visible; }
        .single-token-content {
            width: 100%;
            min-width: 0;
            padding: 0;
        }
        .single-token-summary {
            display: block;
            min-width: 0;
        }
        .single-token-label {
            color: var(--muted-strong);
            font-size: 0.78rem;
            font-weight: 680;
        }
        .single-token-value {
            color: var(--text);
            font-size: clamp(1.55rem, 3vw, 2rem);
            font-weight: 740;
            font-variant-numeric: tabular-nums;
            letter-spacing: -0.03em;
            line-height: 1.1;
            overflow-wrap: anywhere;
        }
        .single-token-legend {
            display: flex;
            min-width: 0;
            flex-wrap: wrap;
            align-items: center;
            gap: 0.55rem 1.15rem;
            margin-top: 0.55rem;
            color: var(--muted-strong);
            font-size: 0.76rem;
        }
        .single-token-legend-item {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            white-space: nowrap;
        }
        .single-token-swatch {
            display: inline-block;
            width: 11px;
            height: 11px;
            flex: 0 0 11px;
        }
        .token-swatch-input, .token-segment-input { background: #BF4E2E; }
        .token-swatch-output, .token-segment-output { background: #D99A72; }
        .single-token-stack {
            display: flex;
            position: relative;
            width: 100%;
            min-width: 0;
            height: 46px;
            margin-top: 1.65rem;
            border-radius: 7px;
            background: #EEEAE4;
        }
        .single-token-segment {
            display: block;
            position: relative;
            height: 100%;
            min-width: 0;
            outline: none;
        }
        .token-segment-input { border-radius: 7px 0 0 7px; }
        .token-segment-output { border-radius: 0 7px 7px 0; }
        .token-segment-only { border-radius: 7px; }
        .single-token-segment:focus-visible {
            outline: 2px solid var(--text);
            outline-offset: 3px;
        }
        .single-token-tooltip {
            display: flex;
            position: absolute;
            z-index: 20;
            width: max-content;
            max-width: min(220px, 78vw);
            flex-direction: column;
            gap: 0.12rem;
            padding: 0.55rem 0.65rem;
            border-radius: 5px;
            color: #FFFFFF;
            background: #2E2B27;
            box-shadow: 0 4px 12px rgba(38, 33, 28, 0.18);
            font-size: 0.75rem;
            line-height: 1.35;
            opacity: 0;
            pointer-events: none;
            visibility: hidden;
            transition: opacity 120ms ease, visibility 120ms ease;
        }
        .single-token-tooltip strong { color: #FFFFFF; font-size: 0.78rem; }
        .single-token-tooltip span { color: #FFFFFF; white-space: nowrap; }
        .single-token-tooltip::after {
            position: absolute;
            width: 0;
            height: 0;
            border: 7px solid transparent;
            content: "";
        }
        .token-tooltip-above {
            right: 0.55rem;
            bottom: calc(100% + 0.7rem);
        }
        .token-tooltip-above::after {
            top: 100%;
            right: 1rem;
            border-top-color: #2E2B27;
        }
        .token-tooltip-below {
            top: calc(100% + 0.7rem);
            right: 0.2rem;
        }
        .token-tooltip-below::after {
            right: 1rem;
            bottom: 100%;
            border-bottom-color: #2E2B27;
        }
        .single-token-segment:hover .single-token-tooltip,
        .single-token-segment:focus .single-token-tooltip {
            opacity: 1;
            visibility: visible;
        }
        .single-token-stack-empty {
            display: flex;
            min-height: 46px;
            align-items: center;
            margin-top: 1rem;
            padding: 0.75rem;
            border: 1px dashed var(--border-strong);
            border-radius: 7px;
            color: var(--muted);
            background: var(--surface-soft);
            font-size: 0.78rem;
        }

        .warning-panel {
            min-width: 0;
            padding: 0.95rem 1.15rem;
            border: 1px solid #E3D4C7;
            border-radius: 11px;
            background: #FCF8F3;
        }
        .warning-panel ul { margin: 0; padding-left: 1.2rem; }
        .warning-panel li {
            margin: 0.42rem 0;
            color: var(--muted-strong);
            font-size: 0.83rem;
            line-height: 1.55;
            overflow-wrap: anywhere;
        }
        .warning-panel li::marker { color: var(--warning); }

        [data-testid="stExpander"] {
            border-color: var(--border) !important;
            border-radius: 11px !important;
            background: var(--surface);
        }
        [data-testid="stExpander"] summary { color: var(--muted-strong); font-size: 0.84rem; }
        .st-key-comparison_run_details [data-testid="stExpander"] {
            overflow: hidden;
            border: 1px solid var(--border) !important;
            background: var(--surface) !important;
            box-shadow: 0 2px 8px rgba(55, 48, 39, 0.035);
        }
        .st-key-comparison_run_details [data-testid="stExpander"] summary,
        .st-key-comparison_run_details [data-testid="stExpander"] summary > div {
            color: var(--text) !important;
            background: var(--surface) !important;
        }
        .st-key-comparison_run_details [data-testid="stExpander"] summary:hover,
        .st-key-comparison_run_details [data-testid="stExpander"] summary:hover > div {
            color: #7E301B !important;
            background: var(--accent-soft) !important;
        }
        .st-key-comparison_run_details [data-testid="stExpander"] summary p,
        .st-key-comparison_run_details [data-testid="stExpander"] summary svg {
            color: inherit !important;
        }
        [class*="st-key-single_run_details"] { width: min(100%, 760px); }
        [class*="st-key-single_run_details"] [data-testid="stExpander"] {
            overflow: hidden;
            border: 1px solid var(--border) !important;
            border-radius: 11px !important;
            background: var(--surface) !important;
            box-shadow: 0 2px 8px rgba(55, 48, 39, 0.035);
        }
        [class*="st-key-single_run_details"] [data-testid="stExpander"] summary {
            color: var(--text) !important;
            background: var(--surface) !important;
            transition: color 160ms ease, background-color 160ms ease;
        }
        [class*="st-key-single_run_details"] [data-testid="stExpander"] summary:hover {
            color: #7E301B !important;
            background: var(--accent-soft) !important;
        }
        [class*="st-key-single_run_details"] [data-testid="stExpander"] summary p,
        [class*="st-key-single_run_details"] [data-testid="stExpander"] summary svg {
            color: inherit !important;
        }
        .metadata-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.85rem;
        }
        .metadata-grid > .metadata-card:only-child { grid-column: 1 / -1; max-width: 620px; }
        .metadata-card {
            min-width: 0;
            padding: 0.9rem 1rem;
            border: 1px solid var(--border);
            border-radius: 9px;
            background: var(--surface-soft);
        }
        .metadata-agent {
            margin-bottom: 0.55rem;
            color: var(--text);
            font-size: 0.78rem;
            font-weight: 700;
        }
        .metadata-row {
            display: grid;
            grid-template-columns: 118px minmax(0, 1fr);
            gap: 0.75rem;
            padding: 0.52rem 0;
            border-bottom: 1px solid #EAE6E0;
            font-size: 0.78rem;
        }
        .metadata-row:last-child { border-bottom: 0; }
        .metadata-row span { color: var(--muted); }
        .metadata-row strong {
            overflow-wrap: anywhere;
            color: var(--muted-strong);
            font-size: 0.78rem;
            font-weight: 550;
            text-align: right;
        }
        .metadata-session-files { min-width: 0; }
        .metadata-list-item {
            display: block;
            max-width: 100%;
            margin-bottom: 0.25rem;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace !important;
            overflow-wrap: anywhere;
            word-break: break-word;
        }
        .metadata-list-item:last-child { margin-bottom: 0; }
        .run-details-card {
            width: 100%;
            max-width: none;
            padding: 0.15rem 0;
            border: 0;
            border-radius: 0;
            background: transparent;
        }

        [data-testid="stAlert"] {
            max-width: 100%;
            border-color: var(--border) !important;
            border-radius: 9px;
            color: var(--muted-strong) !important;
            font-size: 0.82rem;
            overflow-wrap: anywhere;
        }
        hr { border-color: var(--border) !important; }

        @media (max-width: 1199px) {
            .block-container { padding: 2rem 2rem 3.5rem; }
            .st-key-mode_selection,
            .st-key-upload_card { width: min(92%, 900px); }
            .st-key-core_metric_grid [data-testid="stColumn"] {
                width: calc(50% - 0.45rem) !important;
                min-width: 280px !important;
                flex-basis: calc(50% - 0.45rem) !important;
            }
            .single-kpi-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
        }

        @media (max-width: 767px) {
            .block-container { padding: 1.35rem 1rem 2.75rem; }
            h1 { font-size: clamp(1.45rem, 7vw, 2rem) !important; }
            h2 { margin-top: 1.9rem !important; font-size: 1.12rem !important; }
            .st-key-dashboard_header [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                flex-wrap: nowrap !important;
                gap: 0.6rem;
            }
            .st-key-dashboard_header [data-testid="stColumn"] {
                width: 100% !important;
                flex: 1 1 100% !important;
            }
    .header-meta { font-size: 0.78rem; }
    .header-comparison-meta { margin-bottom: 0.8rem; }
    .header-meta-sep { display: block; height: 0.2rem; font-size: 0; }
            .single-run-context { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .st-key-replace_reports { justify-content: flex-start; padding-top: 0; }

            .st-key-mode_selection,
            .st-key-scope_selection,
            .st-key-upload_card { width: 100%; margin-top: 1.2rem; }
            .st-key-mode_selection [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                flex-wrap: nowrap !important;
                gap: 0.75rem;
            }
            .st-key-mode_selection [data-testid="stColumn"] {
                width: 100% !important;
                flex: 1 1 100% !important;
            }
            .st-key-scope_selection [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                flex-wrap: nowrap !important;
                gap: 0.75rem;
            }
            .st-key-scope_selection [data-testid="stColumn"] {
                width: 100% !important;
                flex: 1 1 100% !important;
            }
            .st-key-choose_view button,
            .st-key-choose_compare button { min-height: 112px; }
            .st-key-choose_single_conversation button,
            .st-key-choose_multiple_conversations button,
            .st-key-choose_workspace button { min-height: 104px; }
            [data-testid="stFileUploaderDropzone"] { min-height: 122px; }
            [data-testid="stFileUploaderDropzone"] > div { min-width: 0; flex-wrap: wrap; gap: 0.65rem; }
            [class*="st-key-file_entry_"] [data-testid="stHorizontalBlock"] { gap: 0.35rem; }
            [class*="st-key-file_entry_"] [data-testid="stColumn"]:first-child {
                width: auto !important;
                flex: 1 1 auto !important;
            }
            [class*="st-key-file_entry_"] [data-testid="stColumn"]:last-child {
                width: 34px !important;
                flex: 0 0 34px !important;
            }
            .file-row { align-items: center; flex-direction: row; gap: 0.45rem; }
            .file-name { width: auto; }
            .st-key-upload_actions [data-testid="stColumn"]:first-child { flex: 1 1 auto !important; }
            .st-key-upload_actions [data-testid="stColumn"]:last-child {
                width: clamp(168px, 47vw, 220px) !important;
                flex: 0 0 clamp(168px, 47vw, 220px) !important;
            }

            .comparison-takeaway-grid, .metadata-grid { grid-template-columns: minmax(0, 1fr); }
            [data-testid="stTabs"] [data-baseweb="tab-list"] {
                gap: 1rem;
            }
            .single-kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .overview-kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .st-key-core_metric_grid [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                flex-basis: 100% !important;
            }
            .bar-row {
                grid-template-columns: minmax(0, 1fr) auto;
                grid-template-areas: "label number" "track track";
                gap: 0.45rem 0.7rem;
                margin: 0.8rem 0;
            }
            .bar-row > .agent-label { grid-area: label; min-width: 0; }
            .bar-row > .bar-track, .bar-row > .bar-unavailable { grid-area: track; width: 100%; }
            .bar-row > .bar-number { grid-area: number; min-width: 0; }
            .metadata-grid > .metadata-card:only-child { max-width: none; }
            .metadata-row { grid-template-columns: 96px minmax(0, 1fr); }
        }

        @media (max-width: 480px) {
            .block-container { padding-right: 0.75rem; padding-left: 0.75rem; }
            h1 { font-size: 1.42rem !important; }
            [data-testid="stCaptionContainer"] { font-size: 0.8rem; }
            .file-name { font-size: 0.72rem; }
            .file-valid, .file-invalid { font-size: 0.7rem; }
            .file-count { font-size: 0.74rem; }
            .single-kpi-grid { grid-template-columns: minmax(0, 1fr); }
            .overview-kpi-grid { grid-template-columns: minmax(0, 1fr); }
            .single-kpi-card { min-height: 100px; }
            .st-key-conversation_distribution { padding: 0.2rem 0.25rem 0.4rem; }
            .st-key-upload_actions [data-testid="stColumn"]:last-child {
                width: clamp(148px, 49vw, 188px) !important;
                flex-basis: clamp(148px, 49vw, 188px) !important;
            }
            .st-key-report_action button { padding-right: 0.45rem; padding-left: 0.45rem; font-size: 0.75rem; }
            .metadata-row { grid-template-columns: minmax(0, 1fr); gap: 0.25rem; }
            .metadata-row strong { text-align: left; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
