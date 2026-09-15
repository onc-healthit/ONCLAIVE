from __future__ import annotations

import json
import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]


def sample_payload(filename: str) -> dict:
    return json.loads((ROOT / "sample_data" / filename).read_text())


def stored_report(filename: str) -> dict[str, object]:
    return {
        "name": filename,
        "content": (ROOT / "sample_data" / filename).read_bytes(),
    }


def stored_payload(filename: str, payload: dict) -> dict[str, object]:
    return {"name": filename, "content": json.dumps(payload).encode()}


def conversation_payload(
    name: str,
    *,
    runtime: float,
    cost: float,
    tokens: int,
    prompts: int,
    tools: int,
    edits: int,
) -> dict:
    value = sample_payload("codex-report.json")
    value["run_metadata"]["conversation_name"] = name
    overrides = {
        "wall_clock_time_seconds": runtime,
        "estimated_cost": cost,
        "total_tokens": tokens,
        "human_prompts_required": prompts,
        "tool_calls": tools,
        "file_edits": edits,
        "input_tokens": int(tokens * 0.8),
        "output_tokens": tokens - int(tokens * 0.8),
    }
    for item in value["metrics"]:
        if item["name"] in overrides:
            item["value"] = overrides[item["name"]]
    return value


def workspace_payload() -> dict:
    value = conversation_payload(
        "Workspace aggregate",
        runtime=300,
        cost=4.5,
        tokens=12_000,
        prompts=10,
        tools=80,
        edits=14,
    )
    value["run_metadata"]["scope_type"] = "workspace"
    value["run_metadata"]["conversation_name"] = None
    value["run_metadata"]["workspace_name"] = "ONCLAIVE"
    return value


def upload_screen(
    mode: str | None,
    reports: list[dict[str, object]] | None = None,
    view_scope: str | None = None,
) -> AppTest:
    app = AppTest.from_file(str(ROOT / "streamlit_app.py"))
    app.session_state["screen"] = "upload"
    app.session_state["upload_mode"] = mode
    app.session_state["view_scope"] = view_scope
    app.session_state["uploader_generation"] = 0
    app.session_state["uploaded_reports"] = reports or []
    return app.run(timeout=15)


def dashboard(payloads: list[dict], dashboard_mode: str | None = None) -> AppTest:
    app = AppTest.from_file(str(ROOT / "streamlit_app.py"))
    app.session_state["screen"] = "dashboard"
    resolved_mode = dashboard_mode or ("single" if len(payloads) == 1 else "comparison")
    app.session_state["upload_mode"] = "compare" if resolved_mode == "comparison" else "view"
    app.session_state["view_scope"] = None
    app.session_state["dashboard_mode"] = resolved_mode
    app.session_state["uploader_generation"] = 0
    app.session_state["uploaded_reports"] = []
    app.session_state["report_payloads"] = payloads
    return app.run(timeout=15)


class DashboardAppTests(unittest.TestCase):
    def assert_no_exception(self, app: AppTest) -> None:
        self.assertEqual([str(item.value) for item in app.exception], [])

    def test_initial_screen_opens_directly_to_result_scopes(self):
        app = upload_screen(None)
        self.assert_no_exception(app)
        self.assertEqual(
            [button.label for button in app.button],
            ["Single Conversation", "Multiple Conversations", "Workspace"],
        )
        self.assertEqual(app.session_state["upload_mode"], "view")
        self.assertIsNone(app.session_state["view_scope"])
        self.assertEqual(len(app.get("file_uploader")), 0)
        content = " ".join(item.value for item in app.markdown)
        self.assertNotIn("Compare Agents", content)
        self.assertNotIn("Compare Reports", content)
        self.assertNotIn("run_metadata.agent", content)
        self.assertNotIn("Add one report to visualize a run", content)

    def test_landing_page_has_no_comparison_navigation(self):
        app = upload_screen(None)
        self.assert_no_exception(app)
        labels = [button.label for button in app.button]
        self.assertNotIn("View Agent Results", labels)
        self.assertNotIn("Compare Agents", labels)
        self.assertNotIn("Compare Reports", labels)

    def test_single_conversation_choice_opens_its_upload_step(self):
        app = upload_screen("view")
        next(button for button in app.button if button.label == "Single Conversation").click().run(
            timeout=15
        )
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["view_scope"], "single_conversation")
        self.assertEqual([button.label for button in app.button], ["← Back", "View Results"])
        self.assertTrue(next(button for button in app.button if button.label == "View Results").disabled)
        self.assertIn("Upload one conversation JSON report.", [item.value for item in app.caption])

    def test_multiple_conversations_choice_opens_its_upload_step(self):
        app = upload_screen(None)
        next(
            button for button in app.button if button.label == "Multiple Conversations"
        ).click().run(timeout=15)
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["upload_mode"], "view")
        self.assertEqual(app.session_state["view_scope"], "multiple_conversations")
        self.assertEqual(
            [button.label for button in app.button], ["← Back", "View Conversations"]
        )
        self.assertTrue(
            next(
                button for button in app.button if button.label == "View Conversations"
            ).disabled
        )

    def test_workspace_choice_opens_its_upload_step(self):
        app = upload_screen(None)
        next(button for button in app.button if button.label == "Workspace").click().run(
            timeout=15
        )
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["upload_mode"], "view")
        self.assertEqual(app.session_state["view_scope"], "workspace")
        self.assertEqual([button.label for button in app.button], ["← Back", "View Workspace"])
        self.assertTrue(next(button for button in app.button if button.label == "View Workspace").disabled)

    def test_back_returns_to_scope_selection_and_clears_upload_state(self):
        app = upload_screen(
            "view", [stored_report("codex-report.json")], "single_conversation"
        )
        app.session_state["upload_notice"] = "old validation"
        next(button for button in app.button if button.label == "← Back").click().run(timeout=15)
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["upload_mode"], "view")
        self.assertIsNone(app.session_state["view_scope"])
        self.assertEqual(app.session_state["uploaded_reports"], [])
        self.assertNotIn("upload_notice", app.session_state)
        self.assertEqual(
            [button.label for button in app.button],
            ["Single Conversation", "Multiple Conversations", "Workspace"],
        )

    def test_back_from_scope_upload_returns_to_scope_selection_and_clears_files(self):
        app = upload_screen(
            "view", [stored_report("codex-report.json")], "single_conversation"
        )
        next(button for button in app.button if button.label == "← Back").click().run(timeout=15)
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["upload_mode"], "view")
        self.assertIsNone(app.session_state["view_scope"])
        self.assertEqual(app.session_state["uploaded_reports"], [])
        self.assertEqual(
            [button.label for button in app.button],
            ["Single Conversation", "Multiple Conversations", "Workspace"],
        )

    def test_one_valid_report_enables_single_conversation_cta(self):
        app = upload_screen(
            "view", [stored_report("codex-report.json")], "single_conversation"
        )
        self.assert_no_exception(app)
        cta = next(button for button in app.button if button.label == "View Results")
        self.assertFalse(cta.disabled)
        self.assertIn("Codex · Validated", " ".join(item.value for item in app.markdown))
        cta.click().run(timeout=15)
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["screen"], "dashboard")
        self.assertIn("Core Metrics", [item.value for item in app.header])

    def test_valid_workspace_report_opens_workspace_dashboard(self):
        app = upload_screen(
            "view",
            [stored_payload("workspace.json", workspace_payload())],
            "workspace",
        )
        self.assert_no_exception(app)
        cta = next(button for button in app.button if button.label == "View Workspace")
        self.assertFalse(cta.disabled)
        cta.click().run(timeout=15)
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["screen"], "dashboard")
        self.assertIn("Workspace Overview", [item.value for item in app.header])

    def test_legacy_compare_upload_state_redirects_to_scope_landing(self):
        app = upload_screen("compare", [stored_report("codex-report.json")])
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["upload_mode"], "view")
        self.assertEqual(app.session_state["uploaded_reports"], [])
        self.assertEqual(
            [button.label for button in app.button],
            ["Single Conversation", "Multiple Conversations", "Workspace"],
        )

    def test_multiple_conversation_upload_accepts_more_than_two_reports(self):
        reports = [
            stored_payload(
                f"conversation-{index}.json",
                conversation_payload(
                    f"Conversation {index}",
                    runtime=10 * index,
                    cost=0.5 * index,
                    tokens=1000 * index,
                    prompts=index,
                    tools=4 * index,
                    edits=2 * index,
                ),
            )
            for index in range(1, 4)
        ]
        app = upload_screen("view", reports, "multiple_conversations")
        self.assert_no_exception(app)
        cta = next(button for button in app.button if button.label == "View Conversations")
        self.assertFalse(cta.disabled)
        content = " ".join(item.value for item in app.markdown)
        self.assertIn("3 valid · 3 files", content)

    def test_multiple_conversation_dashboard_aggregates_and_reuses_single_view(self):
        reports = [
            conversation_payload(
                "Inventory",
                runtime=10,
                cost=1.25,
                tokens=1000,
                prompts=2,
                tools=4,
                edits=1,
            ),
            conversation_payload(
                "Release review",
                runtime=20,
                cost=0.75,
                tokens=2000,
                prompts=3,
                tools=6,
                edits=2,
            ),
        ]
        app = dashboard(reports, "multiple")
        self.assert_no_exception(app)
        self.assertEqual([tab.label for tab in app.tabs], ["Overview", "Inventory", "Release review"])
        content = " ".join(item.value for item in app.markdown)
        overview = next(
            item.value
            for item in app.markdown
            if '<div class="overview-kpi-grid">' in item.value
        )
        self.assertIn("Conversations", content)
        self.assertIn(">2</strong>", content)
        for value in ("30s", "$2.00", "3,000", "5", "10", "3"):
            self.assertIn(value, overview)
        headers = [item.value for item in app.header]
        self.assertIn("Overall Metrics", headers)
        self.assertIn("Resource Distribution Across Conversations", headers)
        self.assertNotIn("Aggregate Metrics", headers)
        self.assertNotIn("Conversation Breakdown", headers)
        self.assertNotIn("conversation-breakdown-row", content)
        self.assertEqual(len(app.get("plotly_chart")), 1)
        self.assertEqual(len(app.selectbox), 0)
        self.assertEqual(content.count('class="single-kpi-grid"'), 2)
        self.assertEqual([item.value for item in app.header].count("Run Details"), 2)
        self.assertNotIn("Key Observations", content)
        self.assertNotIn("File edit counts are partial", content)
        self.assertIn(
            "Across 2 conversations, Release review had the highest token usage, "
            "accounting for 66.7% of the total.",
            content,
        )

    def test_two_codex_sample_reports_render_two_conversations_and_correct_totals(self):
        app = upload_screen(
            "view",
            [stored_report("codex-report.json"), stored_report("codex-report-2.json")],
            "multiple_conversations",
        )
        next(
            button for button in app.button if button.label == "View Conversations"
        ).click().run(timeout=15)

        self.assert_no_exception(app)
        self.assertEqual(app.session_state["screen"], "dashboard")
        self.assertEqual(
            [tab.label for tab in app.tabs],
            [
                "Overview",
                sample_payload("codex-report.json")["run_metadata"]["conversation_name"],
                sample_payload("codex-report-2.json")["run_metadata"]["conversation_name"],
            ],
        )
        content = " ".join(item.value for item in app.markdown)
        self.assertIn(">2</strong>", content)
        overview = next(
            item.value
            for item in app.markdown
            if '<div class="overview-kpi-grid">' in item.value
        )
        for value in ("3m 44s", "$3.81", "131,720", "10", "82", "21"):
            self.assertIn(value, overview)
        self.assertEqual(len(app.get("plotly_chart")), 1)

    def test_workspace_dashboard_uses_aggregate_report_without_inventing_tabs(self):
        app = dashboard([workspace_payload()], "workspace")
        self.assert_no_exception(app)
        self.assertEqual(len(app.tabs), 0)
        headers = [item.value for item in app.header]
        self.assertIn("Workspace Overview", headers)
        self.assertIn("Aggregate Metrics", headers)
        content = " ".join(item.value for item in app.markdown)
        self.assertIn("ONCLAIVE", content)
        self.assertIn("Conversations", content)
        self.assertIn("N/A", content)
        self.assertIn("conversation drill-down are unavailable", " ".join(
            item.value for item in app.caption
        ))
        overview = next(
            item.value
            for item in app.markdown
            if '<div class="overview-kpi-grid">' in item.value
        )
        for value in ("5m 00s", "$4.50", "12,000", "10", "80", "14"):
            self.assertIn(value, overview)

    def test_single_codex_dashboard_renders_without_comparison_takeaways(self):
        app = dashboard([sample_payload("codex-report.json")])
        self.assert_no_exception(app)
        headers = [item.value for item in app.header]
        self.assertIn("Core Metrics", headers)
        self.assertIn("Token Usage", headers)
        self.assertNotIn("Warnings & Data Quality", headers)
        self.assertIn("Run Details", headers)
        self.assertNotIn("Run Metadata", headers)
        self.assertNotIn("Primary Takeaways", headers)
        content = " ".join(item.value for item in app.markdown)
        for label in ("Run Time", "Estimated Cost", "Human Prompts", "Tool Calls", "File Edits"):
            self.assertIn(label, content)
        self.assertEqual(content.count('class="single-kpi-card"'), 5)
        self.assertIn("Total Tokens", content)
        self.assertNotIn("Each metric uses its own scale", content)
        self.assertEqual(len(app.get("plotly_chart")), 0)
        kpi_markup = next(item.value for item in app.markdown if "single-kpi-grid" in item.value)
        token_markup = next(
            item.value for item in app.markdown if "single-token-summary" in item.value
        )
        self.assertNotIn('class="status', kpi_markup)
        self.assertNotIn('class="status', token_markup)
        self.assertIn("single-token-legend", token_markup)
        self.assertIn("single-token-stack", token_markup)
        self.assertIn("token-tooltip-above", token_markup)
        self.assertIn("token-tooltip-below", token_markup)

    def test_single_dashboard_hides_warnings_even_when_report_contains_them(self):
        report = sample_payload("codex-report.json")
        self.assertTrue(report["warnings"])
        app = dashboard([report])
        self.assert_no_exception(app)
        self.assertNotIn("Warnings & Data Quality", [item.value for item in app.header])

    def test_single_claude_dashboard_uses_the_same_kpi_presentation(self):
        app = dashboard([sample_payload("claude-code-report.json")])
        self.assert_no_exception(app)
        content = " ".join(item.value for item in app.markdown)
        self.assertIn("Claude Code", content)
        self.assertEqual(content.count('class="single-kpi-card"'), 5)
        self.assertEqual(len(app.get("plotly_chart")), 0)

    def test_legacy_comparison_dashboard_state_is_unreachable_but_code_is_preserved(self):
        app = dashboard(
            [sample_payload("claude-code-report.json"), sample_payload("codex-report.json")]
        )
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["screen"], "upload")
        self.assertEqual(app.session_state["upload_mode"], "view")
        self.assertEqual(
            [button.label for button in app.button],
            ["Single Conversation", "Multiple Conversations", "Workspace"],
        )
        source = (ROOT / "streamlit_app.py").read_text()
        self.assertIn('elif dashboard_mode == "comparison":', source)
        self.assertIn("render_takeaways(reports[0], reports[1])", source)
        self.assertTrue((ROOT / "data" / "comparison.py").exists())

    def test_replace_reports_returns_dashboards_to_clean_scope_selection(self):
        for payloads, mode in (
            ([sample_payload("codex-report.json")], "single"),
            (
                [sample_payload("codex-report.json"), sample_payload("codex-report-2.json")],
                "multiple",
            ),
            ([workspace_payload()], "workspace"),
        ):
            with self.subTest(dashboard_mode=mode):
                app = dashboard(payloads, mode)
                next(button for button in app.button if button.label == "Replace Reports").click().run(
                    timeout=15
                )
                self.assert_no_exception(app)
                self.assertEqual(app.session_state["screen"], "upload")
                self.assertEqual(app.session_state["upload_mode"], "view")
                self.assertIsNone(app.session_state["view_scope"])
                self.assertEqual(app.session_state["uploaded_reports"], [])
                self.assertEqual(
                    [button.label for button in app.button],
                    ["Single Conversation", "Multiple Conversations", "Workspace"],
                )

    def test_responsive_and_light_uploader_styles_are_present(self):
        styles = (ROOT / "components" / "styles.py").read_text()
        self.assertIn("@media (max-width: 1199px)", styles)
        self.assertIn("@media (max-width: 767px)", styles)
        self.assertIn("@media (max-width: 480px)", styles)
        self.assertIn("overflow-x: hidden", styles)
        self.assertIn(".st-key-mode_selection", styles)
        self.assertIn('[data-testid="stFileUploaderDropzone"] > div', styles)
        self.assertIn("background: var(--surface) !important", styles)
        self.assertIn('[data-testid="stFileUploaderDropzone"] button:hover', styles)
        self.assertIn(".single-kpi-grid", styles)
        self.assertIn(".single-run-context", styles)
        self.assertIn('[class*="st-key-single_run_details"]', styles)
        self.assertIn(".st-key-scope_selection", styles)
        self.assertIn(".overview-kpi-grid", styles)
        self.assertIn(".st-key-conversation_distribution", styles)
        self.assertIn(".multiple-summary", styles)
        tab_list_rule = styles.split(
            '[data-testid="stTabs"] [data-baseweb="tab-list"] {', 1
        )[1].split("}", 1)[0]
        self.assertIn("justify-content: flex-start", tab_list_rule)
        self.assertIn("gap: 1.5rem", tab_list_rule)
        self.assertIn("width: min(100%, 760px)", styles)
        self.assertIn(".token-tooltip-above::after", styles)
        self.assertIn("border-top-color: #2E2B27", styles)
        self.assertIn(".token-tooltip-below::after", styles)
        self.assertIn("border-bottom-color: #2E2B27", styles)
        context_rule = styles.split(".single-run-context {", 1)[1].split("}", 1)[0]
        self.assertNotIn("border", context_rule)
        self.assertIn(".file-row { align-items: center; flex-direction: row", styles)


if __name__ == "__main__":
    unittest.main()
