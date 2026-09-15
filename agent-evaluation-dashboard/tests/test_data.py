from __future__ import annotations

import io
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

try:
    import streamlit  # noqa: F401
except ModuleNotFoundError:
    sys.modules["streamlit"] = SimpleNamespace()

from components.core_metrics import _single_kpi_card, build_metric_figure
from components.header import _comparison_context, _single_context
from components.metadata import _metadata_card, _run_details_card
from components.overview import (
    RESOURCE_DISTRIBUTION_METRICS,
    build_resource_distribution_figure,
)
from components.token_usage import _single_token_content
from components.warnings import _warning_messages
from data.aggregation import (
    aggregate_metric,
    aggregate_report,
    conversation_name,
    workspace_conversation_count,
)
from data.comparison import (
    CORE_METRICS,
    TOKEN_METRICS,
    compare_metric,
    format_value,
    order_reports,
    takeaway_text,
)
from data.loader import decode_report, load_report
from data.observations import build_highest_token_summary
from data.schema import REQUIRED_METRIC_NAMES, REQUIRED_RUN_METADATA_FIELDS
from data.validator import evaluate_uploads, validate_pair, validate_upload


ROOT = Path(__file__).resolve().parents[1]


def metric(name: str, value: int | float | None = 1, status: str | None = None) -> dict:
    item = {
        "name": name,
        "value": value,
        "status": status or ("missing" if value is None else "computed"),
        "source": None if value is None else "test_source",
        "warnings": [],
        "notes": [],
    }
    if name == "estimated_cost":
        item["unit"] = "USD"
    return item


def payload(
    agent: str,
    metric_overrides: dict[str, dict] | None = None,
    metadata_overrides: dict | None = None,
) -> dict:
    metric_overrides = metric_overrides or {}
    metadata = {
        "agent": agent,
        "session_files": [f"{agent}-session.jsonl"],
        "conversation_name": "Review Claude Phase 1 outputs",
        "workspace_name": "ONCLAIVE",
        "scope_type": "conversation",
        "model": "gpt-5.6-codex" if agent == "codex" else "claude-sonnet-4-5",
        "generated_at": "2026-08-19T14:46:51.421611Z",
    }
    metadata.update(metadata_overrides or {})
    return {
        "run_metadata": metadata,
        "metrics": [metric_overrides.get(name, metric(name)) for name in REQUIRED_METRIC_NAMES],
        "warnings": [],
        "sources_used": ["test_source"],
    }


class UploadedFile(io.BytesIO):
    def __init__(self, name: str, value: bytes):
        super().__init__(value)
        self.name = name

    def getvalue(self) -> bytes:
        return super().getvalue()


def upload(name: str, value: dict) -> UploadedFile:
    return UploadedFile(name, json.dumps(value).encode())


class LoaderTests(unittest.TestCase):
    def test_revised_codex_and_claude_contracts_load(self):
        codex = load_report(payload("codex"))
        claude = load_report(payload("claude_code"))
        self.assertEqual(codex.agent_key, "codex")
        self.assertEqual(claude.agent_key, "claude_code")
        self.assertEqual(codex.run_metadata["conversation_name"], "Review Claude Phase 1 outputs")
        self.assertEqual(codex.run_metadata["workspace_name"], "ONCLAIVE")
        self.assertEqual(codex.run_metadata["generated_at"], "2026-08-19T14:46:51.421611Z")

    def test_schema_version_and_retired_ids_are_not_needed(self):
        value = payload("codex")
        retired = {
            "schema_version",
            "session_id",
            "conversation_id",
            "workspace_id",
            "start_timestamp",
            "end_timestamp",
        }
        self.assertFalse(retired.intersection(value))
        self.assertFalse(retired.intersection(value["run_metadata"]))
        self.assertTrue(validate_upload(upload("codex.json", value)).valid)

    def test_metrics_are_indexed_by_name_not_position(self):
        report = load_report(payload("codex", {
            "total_tokens": metric("total_tokens", 12),
            "wall_clock_time_seconds": metric("wall_clock_time_seconds", 5.5, "partial"),
        }))
        self.assertEqual(report.metrics["wall_clock_time_seconds"].value, 5.5)
        self.assertEqual(report.metrics["total_tokens"].value, 12)

    def test_total_tokens_is_read_directly_and_not_derived(self):
        report = load_report(payload("codex", {
            "input_tokens": metric("input_tokens", 10),
            "output_tokens": metric("output_tokens", 5),
            "total_tokens": metric("total_tokens", 999),
        }))
        self.assertEqual(report.metrics["total_tokens"].value, 999)

    def test_utf8_bom_json_is_accepted(self):
        raw = ("\ufeff" + json.dumps(payload("claude_code"))).encode("utf-8")
        _, report = decode_report(raw)
        self.assertEqual(report.agent_label, "Claude Code")

    def test_agent_value_is_exact_not_inferred(self):
        for alias in ("claude", "Claude Code", "claude-code", "Codex"):
            with self.subTest(alias=alias), self.assertRaisesRegex(ValueError, "exactly"):
                load_report(payload(alias))


class ValidationTests(unittest.TestCase):
    def test_valid_revised_contract_is_accepted_for_both_agents(self):
        for agent in ("codex", "claude_code"):
            with self.subTest(agent=agent):
                item = validate_upload(upload(f"{agent}.json", payload(agent)))
                self.assertTrue(item.valid, item.error)

    def test_all_revised_metadata_fields_are_required(self):
        for field in REQUIRED_RUN_METADATA_FIELDS:
            value = payload("codex")
            del value["run_metadata"][field]
            item = validate_upload(upload("codex.json", value))
            self.assertFalse(item.valid, field)
            self.assertIn(field, item.error)

    def test_session_files_must_be_a_nonempty_string_array(self):
        invalid_values = ("session.jsonl", [], ["valid.jsonl", 42])
        for session_files in invalid_values:
            with self.subTest(session_files=session_files):
                item = validate_upload(upload(
                    "codex.json",
                    payload("codex", metadata_overrides={"session_files": session_files}),
                ))
                self.assertFalse(item.valid)
                self.assertIn("session_files", item.error)

    def test_nullable_names_and_model_are_accepted(self):
        item = validate_upload(upload(
            "codex.json",
            payload("codex", metadata_overrides={
                "conversation_name": None,
                "workspace_name": None,
                "model": None,
            }),
        ))
        self.assertTrue(item.valid, item.error)

    def test_workspace_scope_is_accepted_without_normalization(self):
        item = validate_upload(upload(
            "codex.json",
            payload("codex", metadata_overrides={"scope_type": "workspace"}),
        ))
        self.assertTrue(item.valid, item.error)
        self.assertEqual(item.report.run_metadata["scope_type"], "workspace")

    def test_unknown_scope_type_is_rejected(self):
        item = validate_upload(upload(
            "codex.json",
            payload("codex", metadata_overrides={"scope_type": "project"}),
        ))
        self.assertFalse(item.valid)
        self.assertIn("scope_type", item.error)

    def test_generated_at_must_be_a_nonempty_string(self):
        for generated_at in (None, "", 123):
            with self.subTest(generated_at=generated_at):
                item = validate_upload(upload(
                    "codex.json",
                    payload("codex", metadata_overrides={"generated_at": generated_at}),
                ))
                self.assertFalse(item.valid)
                self.assertIn("generated_at", item.error)

    def test_invalid_json_is_reported(self):
        item = validate_upload(UploadedFile("bad.json", b"not json"))
        self.assertFalse(item.valid)
        self.assertIn("Invalid JSON", item.error)

    def test_all_eight_metrics_are_required_including_total_tokens(self):
        self.assertEqual(len(REQUIRED_METRIC_NAMES), 8)
        for missing_name in REQUIRED_METRIC_NAMES:
            value = payload("codex")
            value["metrics"] = [item for item in value["metrics"] if item["name"] != missing_name]
            item = validate_upload(upload("codex.json", value))
            self.assertFalse(item.valid)
            self.assertIn(f"missing required metrics: {missing_name}", item.error)

    def test_api_request_count_is_not_required_or_supported(self):
        value = payload("codex")
        self.assertNotIn("api_request_count", {item["name"] for item in value["metrics"]})
        self.assertTrue(validate_upload(upload("codex.json", value)).valid)
        value["metrics"].append(metric("api_request_count", 4))
        item = validate_upload(upload("codex.json", value))
        self.assertFalse(item.valid)
        self.assertIn("unsupported metrics: api_request_count", item.error)

    def test_null_value_requires_missing_status_and_is_not_zero(self):
        value = payload("codex", {"estimated_cost": metric("estimated_cost", None)})
        item = validate_upload(upload("codex.json", value))
        self.assertTrue(item.valid, item.error)
        self.assertIsNone(item.report.metrics["estimated_cost"].value)
        value["metrics"][1]["status"] = "computed"
        item = validate_upload(upload("codex.json", value))
        self.assertFalse(item.valid)
        self.assertIn("must use status 'missing'", item.error)

    def test_estimated_cost_uses_usd(self):
        value = payload("codex")
        value["metrics"][1]["unit"] = "EUR"
        item = validate_upload(upload("codex.json", value))
        self.assertFalse(item.valid)
        self.assertIn("must use unit 'USD'", item.error)

    def test_pair_must_contain_exactly_one_of_each_agent(self):
        same_agent = [
            validate_upload(upload("one.json", payload("codex"))),
            validate_upload(upload("two.json", payload("codex"))),
        ]
        self.assertEqual(
            validate_pair(same_agent),
            [
                "Comparison requires one Codex report and one Claude Code report. "
                "Two reports from the same agent cannot be compared."
            ],
        )
        self.assertEqual(validate_pair(same_agent[:1]), ["Upload exactly two JSON reports."])
        valid_pair = [same_agent[0], validate_upload(upload("claude.json", payload("claude_code")))]
        self.assertEqual(validate_pair(valid_pair), [])


class ComparisonTests(unittest.TestCase):
    def test_reports_are_ordered_from_contents(self):
        claude = load_report(payload("claude_code"))
        codex = load_report(payload("codex"))
        ordered = order_reports([claude, codex])
        self.assertEqual([report.agent_key for report in ordered], ["codex", "claude_code"])

    def test_difference_is_absolute(self):
        codex = load_report(payload("codex", {"tool_calls": metric("tool_calls", 8)}))
        claude = load_report(payload("claude_code", {"tool_calls": metric("tool_calls", 13)}))
        result = compare_metric(codex, claude, CORE_METRICS[3])
        self.assertEqual(result.difference, 5)

    def test_missing_value_displays_na_and_has_no_delta_or_takeaway(self):
        codex = load_report(payload("codex", {"estimated_cost": metric("estimated_cost", None)}))
        claude = load_report(payload("claude_code"))
        comparison = compare_metric(codex, claude, CORE_METRICS[1])
        self.assertIsNone(comparison.difference)
        self.assertEqual(format_value(comparison.codex.value, "currency"), "N/A")
        self.assertIsNone(takeaway_text(codex, claude, CORE_METRICS[1]))

    def test_takeaway_uses_report_values(self):
        codex = load_report(payload("codex", {"estimated_cost": metric("estimated_cost", 1.67, "estimated")}))
        claude = load_report(payload("claude_code", {"estimated_cost": metric("estimated_cost", 0.83, "estimated")}))
        self.assertEqual(
            takeaway_text(codex, claude, CORE_METRICS[1]),
            "Claude Code cost $0.84 less",
        )

    def test_takeaway_dynamically_changes_winner(self):
        codex = load_report(payload("codex", {
            "estimated_cost": metric("estimated_cost", 0.25, "estimated"),
            "wall_clock_time_seconds": metric("wall_clock_time_seconds", 47),
        }))
        claude = load_report(payload("claude_code", {
            "estimated_cost": metric("estimated_cost", 1.00, "estimated"),
            "wall_clock_time_seconds": metric("wall_clock_time_seconds", 94),
        }))
        self.assertEqual(takeaway_text(codex, claude, CORE_METRICS[1]), "Codex cost $0.75 less")
        self.assertEqual(
            takeaway_text(codex, claude, CORE_METRICS[0]),
            "Codex finished 47s faster",
        )

    def test_duration_format_is_readable_for_hover_and_axes(self):
        self.assertEqual(format_value(545, "duration"), "9m 05s")
        self.assertEqual(format_value(47, "duration"), "47s")

    def test_token_section_uses_only_uploaded_contract_metrics(self):
        self.assertEqual(
            [definition.names[0] for definition in TOKEN_METRICS],
            ["input_tokens", "output_tokens", "total_tokens"],
        )


class UploadFlowTests(unittest.TestCase):
    def test_no_valid_report_disables_visualize_action(self):
        decision = evaluate_uploads([], "visualize")
        self.assertFalse(decision.ready)
        self.assertEqual(decision.cta_label, "Visualize Report")

    def test_one_codex_report_enables_single_visualization(self):
        decision = evaluate_uploads(
            [validate_upload(upload("codex.json", payload("codex")))], "visualize"
        )
        self.assertTrue(decision.ready)
        self.assertEqual(decision.mode, "single")
        self.assertEqual(decision.cta_label, "Visualize Report")
        self.assertEqual(decision.valid_items[0].report.agent_label, "Codex")

    def test_one_claude_report_enables_single_visualization(self):
        decision = evaluate_uploads(
            [validate_upload(upload("claude.json", payload("claude_code")))],
            "visualize",
        )
        self.assertTrue(decision.ready)
        self.assertEqual(decision.mode, "single")
        self.assertEqual(decision.cta_label, "Visualize Report")
        self.assertEqual(decision.valid_items[0].report.agent_label, "Claude Code")

    def test_compatible_pair_enables_comparison_action(self):
        decision = evaluate_uploads(
            [
                validate_upload(upload("claude.json", payload("claude_code"))),
                validate_upload(upload("codex.json", payload("codex"))),
            ],
            "compare",
        )
        self.assertTrue(decision.ready)
        self.assertEqual(decision.mode, "comparison")
        self.assertEqual(decision.cta_label, "Compare Reports")

    def test_same_agent_pairs_do_not_allow_comparison(self):
        for agent in ("codex", "claude_code"):
            with self.subTest(agent=agent):
                decision = evaluate_uploads(
                    [
                        validate_upload(upload("one.json", payload(agent))),
                        validate_upload(upload("two.json", payload(agent))),
                    ],
                    "compare",
                )
                self.assertFalse(decision.ready)
                self.assertEqual(decision.cta_label, "Compare Reports")
                self.assertIn("requires one Codex report", " ".join(decision.errors))

    def test_invalid_second_file_keeps_comparison_disabled(self):
        decision = evaluate_uploads(
            [
                validate_upload(upload("codex.json", payload("codex"))),
                validate_upload(UploadedFile("bad.json", b"not json")),
            ],
            "compare",
        )
        self.assertFalse(decision.ready)
        self.assertIsNone(decision.mode)
        self.assertEqual(len(decision.valid_items), 1)

    def test_one_valid_report_does_not_enable_comparison(self):
        decision = evaluate_uploads(
            [validate_upload(upload("codex.json", payload("codex")))], "compare"
        )
        self.assertFalse(decision.ready)
        self.assertEqual(decision.cta_label, "Compare Reports")

    def test_visualize_mode_rejects_an_invalid_report(self):
        decision = evaluate_uploads(
            [validate_upload(UploadedFile("bad.json", b"not json"))], "visualize"
        )
        self.assertFalse(decision.ready)
        self.assertIn("bad.json", " ".join(decision.errors))

    def test_single_conversation_requires_exactly_one_conversation_report(self):
        valid = evaluate_uploads(
            [validate_upload(upload("conversation.json", payload("codex")))],
            "single_conversation",
        )
        workspace = evaluate_uploads(
            [
                validate_upload(upload(
                    "workspace.json",
                    payload("codex", metadata_overrides={"scope_type": "workspace"}),
                ))
            ],
            "single_conversation",
        )
        self.assertTrue(valid.ready)
        self.assertEqual(valid.mode, "single")
        self.assertEqual(valid.cta_label, "View Results")
        self.assertFalse(workspace.ready)
        self.assertIn("conversation-level", " ".join(workspace.errors))

    def test_multiple_conversations_accepts_any_count_above_one_from_same_agent(self):
        items = [
            validate_upload(upload(
                f"conversation-{index}.json",
                payload("codex", metadata_overrides={"conversation_name": f"Conversation {index}"}),
            ))
            for index in range(1, 4)
        ]
        decision = evaluate_uploads(items, "multiple_conversations")
        self.assertTrue(decision.ready)
        self.assertEqual(decision.mode, "multiple")
        self.assertEqual(len(decision.valid_items), 3)
        self.assertEqual(decision.cta_label, "View Conversations")

    def test_multiple_conversations_requires_two_reports_from_the_same_agent(self):
        one = evaluate_uploads(
            [validate_upload(upload("one.json", payload("codex")))],
            "multiple_conversations",
        )
        mixed = evaluate_uploads(
            [
                validate_upload(upload("codex.json", payload("codex"))),
                validate_upload(upload("claude.json", payload("claude_code"))),
            ],
            "multiple_conversations",
        )
        self.assertFalse(one.ready)
        self.assertFalse(mixed.ready)
        self.assertIn("same agent", " ".join(mixed.errors))

    def test_workspace_mode_requires_one_workspace_report(self):
        workspace_payload = payload(
            "codex", metadata_overrides={"scope_type": "workspace", "conversation_name": None}
        )
        valid = evaluate_uploads(
            [validate_upload(upload("workspace.json", workspace_payload))], "workspace"
        )
        conversation = evaluate_uploads(
            [validate_upload(upload("conversation.json", payload("codex")))], "workspace"
        )
        self.assertTrue(valid.ready)
        self.assertEqual(valid.mode, "workspace")
        self.assertFalse(conversation.ready)
        self.assertIn("workspace-level", " ".join(conversation.errors))


class AggregationTests(unittest.TestCase):
    def _reports(self):
        first = load_report(payload("codex", {
            "wall_clock_time_seconds": metric("wall_clock_time_seconds", 10),
            "estimated_cost": metric("estimated_cost", 1.2, "estimated"),
            "human_prompts_required": metric("human_prompts_required", 2),
            "tool_calls": metric("tool_calls", 4),
            "file_edits": metric("file_edits", 1, "partial"),
            "input_tokens": metric("input_tokens", 80),
            "output_tokens": metric("output_tokens", 20),
            "total_tokens": metric("total_tokens", 100),
        }, {"conversation_name": "First"}))
        second = load_report(payload("codex", {
            "wall_clock_time_seconds": metric("wall_clock_time_seconds", 20),
            "estimated_cost": metric("estimated_cost", 0.8, "estimated"),
            "human_prompts_required": metric("human_prompts_required", 3),
            "tool_calls": metric("tool_calls", 6),
            "file_edits": metric("file_edits", 2, "partial"),
            "input_tokens": metric("input_tokens", 150),
            "output_tokens": metric("output_tokens", 50),
            "total_tokens": metric("total_tokens", 200),
        }, {"conversation_name": "Second"}))
        return first, second

    def test_overview_totals_sum_uploaded_metrics(self):
        reports = self._reports()
        expected = (30, 2, 5, 10, 3, 300)
        definitions = (
            CORE_METRICS[0], CORE_METRICS[1], CORE_METRICS[2],
            CORE_METRICS[3], CORE_METRICS[4], CORE_METRICS[5],
        )
        self.assertEqual(
            tuple(aggregate_metric(reports, definition).value for definition in definitions),
            expected,
        )
        aggregate = aggregate_report(reports)
        self.assertEqual(aggregate.metrics["input_tokens"].value, 230)
        self.assertEqual(aggregate.metrics["output_tokens"].value, 70)

    def test_aggregate_missing_value_remains_unavailable(self):
        first, second = self._reports()
        missing = load_report(payload("codex", {
            "estimated_cost": metric("estimated_cost", None),
        }, {"conversation_name": "Missing"}))
        self.assertIsNone(aggregate_metric([first, second, missing], CORE_METRICS[1]).value)

    def test_conversation_names_and_workspace_count_are_not_inferred(self):
        report = load_report(payload("codex", metadata_overrides={
            "scope_type": "workspace",
            "conversation_name": None,
            "session_files": ["one.jsonl", "two.jsonl", "three.jsonl"],
        }))
        self.assertEqual(conversation_name(report), "N/A")
        self.assertIsNone(workspace_conversation_count(report))

    def test_highest_token_summary_is_deterministic_and_uses_uploaded_values(self):
        self.assertEqual(
            build_highest_token_summary(self._reports()),
            "Across 2 conversations, Second had the highest token usage, "
            "accounting for 66.7% of the total.",
        )

    def test_highest_token_observation_is_omitted_when_any_value_is_missing(self):
        first, _ = self._reports()
        missing = load_report(payload("codex", {
            "total_tokens": metric("total_tokens", None),
        }, {"conversation_name": "Missing tokens"}))

        self.assertIsNone(build_highest_token_summary([first, missing]))

    def test_single_conversation_does_not_generate_highest_token_observation(self):
        self.assertIsNone(build_highest_token_summary([self._reports()[0]]))


class MetricChartTests(unittest.TestCase):
    def test_comparison_chart_rejects_single_report_input(self):
        with self.assertRaisesRegex(ValueError, "exactly two"):
            build_metric_figure([load_report(payload("codex"))], CORE_METRICS[3])

    def test_comparison_mode_figure_has_two_vertical_bars(self):
        figure = build_metric_figure(
            [load_report(payload("codex")), load_report(payload("claude_code"))],
            CORE_METRICS[3],
        )
        self.assertEqual(list(figure.data[0].x), ["Codex", "Claude Code"])
        self.assertEqual(len(figure.data[0].y), 2)

    def test_resource_distribution_uses_one_bar_per_conversation_and_one_agent_color(self):
        first = load_report(payload("codex", {
            "tool_calls": metric("tool_calls", 12),
        }, {"conversation_name": "First conversation"}))
        second = load_report(payload("codex", {
            "tool_calls": metric("tool_calls", 34),
        }, {"conversation_name": "Second conversation"}))
        label, definition = "Tool Calls", CORE_METRICS[3]

        figure = build_resource_distribution_figure([first, second], label, definition)

        self.assertEqual(len(figure.data), 1)
        self.assertEqual(list(figure.data[0].x), [0, 1])
        self.assertEqual(list(figure.data[0].y), [12.0, 34.0])
        self.assertEqual(list(figure.layout.xaxis.ticktext), [
            "First conversation",
            "Second conversation",
        ])
        self.assertEqual(figure.data[0].marker.color, "#5F7F6B")
        self.assertEqual(figure.layout.yaxis.range[0], 0)
        self.assertAlmostEqual(figure.layout.yaxis.range[1], 34 * 1.18)
        self.assertEqual(figure.layout.yaxis.nticks, 7)
        self.assertEqual(figure.layout.xaxis.tickangle, 0)
        self.assertEqual(figure.layout.margin.l, 70)
        self.assertEqual(figure.layout.margin.r, 4)
        self.assertEqual(
            list(figure.data[0].customdata[1]),
            ["Second conversation", "34"],
        )
        self.assertIn("Tool Calls", figure.data[0].hovertemplate)
        self.assertEqual(
            [button.label for button in figure.layout.updatemenus[0].buttons],
            [
                "Runtime",
                "Estimated Cost",
                "Total Tokens",
                "Human Prompts",
                "Tool Calls",
                "File Edits",
            ],
        )
        cost_button = figure.layout.updatemenus[0].buttons[1]
        self.assertEqual(list(cost_button.args[0]["y"][0]), [1.0, 1.0])
        self.assertEqual(cost_button.args[1]["yaxis"]["range"][0], 0)

    def test_resource_distribution_wraps_long_labels_without_rotating_them(self):
        long_name = (
            "Refine multi-conversation reporting experience for stakeholder review"
        )
        first = load_report(payload("codex", metadata_overrides={
            "conversation_name": "Review Claude Phase 1 outputs",
        }))
        second = load_report(payload("codex", metadata_overrides={
            "conversation_name": long_name,
        }))

        figure = build_resource_distribution_figure(
            [first, second], "Runtime", CORE_METRICS[0]
        )

        self.assertEqual(figure.layout.xaxis.tickangle, 0)
        self.assertTrue(all("<br>" in label for label in figure.layout.xaxis.ticktext))
        self.assertTrue(any("…" in label for label in figure.layout.xaxis.ticktext))
        self.assertEqual(
            list(figure.data[0].customdata[1])[0],
            long_name,
        )

    def test_resource_distribution_metric_selector_definitions_cover_all_requested_metrics(self):
        self.assertEqual(
            [label for label, _ in RESOURCE_DISTRIBUTION_METRICS],
            [
                "Runtime",
                "Estimated Cost",
                "Total Tokens",
                "Human Prompts",
                "Tool Calls",
                "File Edits",
            ],
        )

    def test_added_codex_sample_is_contract_valid_and_creates_two_distribution_bars(self):
        reports = []
        for filename in ("codex-report.json", "codex-report-2.json"):
            item = validate_upload(
                UploadedFile(filename, (ROOT / "sample_data" / filename).read_bytes())
            )
            self.assertTrue(item.valid, item.error)
            reports.append(item.report)

        self.assertEqual({report.agent_key for report in reports}, {"codex"})
        self.assertEqual(len({conversation_name(report) for report in reports}), 2)
        self.assertTrue(
            all(set(report.metrics) == set(REQUIRED_METRIC_NAMES) for report in reports)
        )
        figure = build_resource_distribution_figure(
            reports,
            "Runtime",
            CORE_METRICS[0],
        )
        self.assertEqual(len(figure.data[0].y), 2)

    def test_hover_data_contains_exact_value_status_and_source(self):
        codex = load_report(
            payload("codex", {"tool_calls": metric("tool_calls", 50, "partial")})
        )
        figure = build_metric_figure([codex, load_report(payload("claude_code"))], CORE_METRICS[3])
        hover = list(figure.data[0].customdata[0])
        self.assertEqual(hover, ["Codex", "50", "partial", "test_source"])
        self.assertIn("Status", figure.data[0].hovertemplate)
        self.assertIn("Source", figure.data[0].hovertemplate)

    def test_missing_metric_is_none_with_na_annotation_not_zero(self):
        codex = load_report(payload("codex", {"tool_calls": metric("tool_calls", None)}))
        figure = build_metric_figure(
            [codex, load_report(payload("claude_code"))], CORE_METRICS[3]
        )
        self.assertEqual(list(figure.data[0].y), [None, 1.0])
        self.assertEqual(figure.layout.annotations[0].text, "N/A")

    def test_each_metric_figure_calculates_its_own_axis_range(self):
        report = load_report(
            payload(
                "codex",
                {
                    "tool_calls": metric("tool_calls", 10),
                    "total_tokens": metric("total_tokens", 1000),
                },
            )
        )
        claude = load_report(payload("claude_code"))
        calls = build_metric_figure([report, claude], CORE_METRICS[3])
        tokens = build_metric_figure([report, claude], CORE_METRICS[5])
        self.assertLess(calls.layout.yaxis.range[1], tokens.layout.yaxis.range[1])

    def test_all_comparison_axes_start_at_zero_and_use_metric_units(self):
        reports = [load_report(payload("codex")), load_report(payload("claude_code"))]
        expected_titles = ["Time", "USD", "Prompts", "Tool calls", "File edits", "Tokens"]
        for definition, expected_title in zip(CORE_METRICS, expected_titles):
            with self.subTest(metric=definition.names[0]):
                figure = build_metric_figure(reports, definition)
                self.assertEqual(figure.layout.yaxis.range[0], 0)
                self.assertEqual(figure.layout.yaxis.title.text, expected_title)
                self.assertEqual(figure.layout.margin.l, 82)
                self.assertEqual(figure.layout.yaxis.title.standoff, 16)
                self.assertGreater(
                    figure.layout.yaxis.range[1], max(figure.layout.yaxis.tickvals)
                )
                self.assertLessEqual(len(figure.layout.yaxis.tickvals), 5)

    def test_total_tokens_uses_stacked_input_output_bars_and_exact_hover_data(self):
        codex = load_report(payload("codex", {
            "input_tokens": metric("input_tokens", 80),
            "output_tokens": metric("output_tokens", 20),
            "total_tokens": metric("total_tokens", 120),
        }))
        claude = load_report(payload("claude_code", {
            "input_tokens": metric("input_tokens", 30),
            "output_tokens": metric("output_tokens", 20),
            "total_tokens": metric("total_tokens", 75),
        }))
        figure = build_metric_figure([codex, claude], CORE_METRICS[5])
        self.assertEqual(figure.layout.barmode, "stack")
        self.assertFalse(figure.layout.showlegend)
        self.assertEqual([trace.name for trace in figure.data], ["Input", "Output"])
        self.assertEqual(
            [figure.data[0].y[index] + figure.data[1].y[index] for index in range(2)],
            [120, 75],
        )
        self.assertEqual(
            list(figure.data[0].customdata[0]),
            ["Codex", "120", "80", "20"],
        )

    def test_total_token_axis_uses_compact_report_derived_ticks(self):
        codex = load_report(payload("codex", {
            "input_tokens": metric("input_tokens", 90_000),
            "output_tokens": metric("output_tokens", 10_000),
            "total_tokens": metric("total_tokens", 100_000),
        }))
        claude = load_report(payload("claude_code", {
            "input_tokens": metric("input_tokens", 125_000),
            "output_tokens": metric("output_tokens", 25_000),
            "total_tokens": metric("total_tokens", 150_000),
        }))

        figure = build_metric_figure([codex, claude], CORE_METRICS[5])

        self.assertEqual(figure.layout.yaxis.range[0], 0)
        self.assertGreaterEqual(figure.layout.yaxis.range[1], 150_000)
        self.assertIn("50k", figure.layout.yaxis.ticktext)
        self.assertIn("100k", figure.layout.yaxis.ticktext)
        self.assertIn("150k", figure.layout.yaxis.ticktext)
        self.assertLessEqual(len(figure.layout.yaxis.tickvals), 5)
        self.assertIn("Total Tokens", figure.data[0].hovertemplate)
        self.assertIn("Input Tokens", figure.data[0].hovertemplate)
        self.assertIn("Output Tokens", figure.data[0].hovertemplate)


class SingleReportDisplayTests(unittest.TestCase):
    def test_kpi_card_shows_only_contract_value_and_label(self):
        report = load_report(
            payload("codex", {"tool_calls": metric("tool_calls", 50, "partial")})
        )
        html = _single_kpi_card(report, "Tool Calls", CORE_METRICS[3])
        self.assertIn("single-kpi-value\">50", html)
        self.assertIn("Tool Calls", html)
        self.assertNotIn("status", html)
        self.assertNotIn("partial", html)

    def test_single_token_content_is_one_stacked_horizontal_bar(self):
        report = load_report(
            payload(
                "codex",
                {
                    "input_tokens": metric("input_tokens", 100, "computed"),
                    "output_tokens": metric("output_tokens", 25, "partial"),
                    "total_tokens": metric("total_tokens", 999, "computed"),
                },
            )
        )
        html = _single_token_content(report)
        self.assertEqual(html.count('class="single-token-stack"'), 1)
        self.assertIn('class="single-token-segment token-segment-input"', html)
        self.assertIn('class="single-token-segment token-segment-output"', html)
        self.assertIn('style="width:80.0000%"', html)
        self.assertIn('style="width:20.0000%"', html)
        self.assertIn("Count: 25", html)
        self.assertIn("Status: partial", html)
        self.assertIn("Source: test_source", html)
        self.assertIn("token-tooltip-above", html)
        self.assertIn("token-tooltip-below", html)

    def test_single_token_missing_segment_is_not_zero(self):
        report = load_report(payload("codex", {"input_tokens": metric("input_tokens", None)}))
        html = _single_token_content(report)
        self.assertNotIn("token-segment-input", html)
        self.assertIn("Input Tokens · N/A", html)
        self.assertIn('style="width:100.0000%"', html)

    def test_single_context_contains_only_important_run_context(self):
        html = _single_context(load_report(payload("codex")))
        for label in ("Agent", "Conversation", "Workspace", "Model", "Scope", "Generated"):
            self.assertIn(label, html)
        self.assertNotIn("Session Files", html)
        self.assertNotIn("Sources Used", html)

    def test_run_details_contains_only_technical_traceability_fields(self):
        html = _run_details_card(load_report(payload("codex")))
        self.assertIn("Session Files", html)
        self.assertIn("Sources Used", html)
        for label in ("Conversation", "Workspace", "Model", "Scope", "Generated At"):
            self.assertNotIn(label, html)

    def test_clean_single_report_has_no_warning_messages(self):
        report = load_report(payload("codex"))
        self.assertEqual(_warning_messages([report]), [])

    def test_single_warning_area_deduplicates_report_and_metric_detail(self):
        value = payload(
            "codex",
            {
                "file_edits": {
                    **metric("file_edits", 9, "partial"),
                    "warnings": ["File edits may be incomplete"],
                }
            },
        )
        value["warnings"] = ["File edits may be incomplete"]
        self.assertEqual(
            _warning_messages([load_report(value)]),
            ["File edits may be incomplete"],
        )


class MetadataDisplayTests(unittest.TestCase):
    def test_comparison_header_shows_only_agents_and_uploaded_models(self):
        codex = load_report(payload("codex"))
        claude = load_report(payload("claude_code"))
        html = _comparison_context([codex, claude])
        self.assertIn("Codex vs Claude Code", html)
        self.assertIn("gpt-5.6-codex", html)
        self.assertIn("claude-sonnet-4-5", html)
        self.assertNotIn("Conversation", html)
        self.assertNotIn("Workspace", html)
        self.assertNotIn("Review Claude Phase 1 outputs", html)

    def test_comparison_header_displays_na_for_null_model(self):
        codex = load_report(payload("codex", metadata_overrides={"model": None}))
        claude = load_report(payload("claude_code"))
        html = _comparison_context([codex, claude])
        self.assertIn("N/A", html)
        self.assertIn("claude-sonnet-4-5", html)

    def test_metadata_card_displays_model_generated_at_and_session_files_safely(self):
        long_files = [
            "rollout-2026-08-19T14-24-58-019ffc5e-cac8-72b3-bb6b-d2913cdb515c.jsonl",
            "rollout-2026-08-19T15-00-00-a-second-very-long-session-filename.jsonl",
        ]
        report = load_report(payload("codex", metadata_overrides={"session_files": long_files}))
        html = _metadata_card(report)
        self.assertIn("gpt-5.6-codex", html)
        self.assertIn("2026-08-19T14:46:51.421611Z", html)
        self.assertEqual(html.count('class="metadata-list-item"'), 2)
        for filename in long_files:
            self.assertIn(filename, html)

    def test_model_null_displays_na_and_old_ids_are_not_shown(self):
        report = load_report(payload("codex", metadata_overrides={
            "model": None,
            "session_id": "legacy-session",
            "conversation_id": "legacy-conversation",
            "workspace_id": "legacy-workspace",
            "start_timestamp": "legacy-start",
            "end_timestamp": "legacy-end",
        }))
        html = _metadata_card(report)
        self.assertIn("Model", html)
        self.assertIn("N/A", html)
        for legacy_value in ("legacy-session", "legacy-conversation", "legacy-workspace", "legacy-start", "legacy-end"):
            self.assertNotIn(legacy_value, html)

    def test_revised_sample_files_validate_as_a_pair(self):
        items = []
        for filename in ("codex-report.json", "claude-code-report.json"):
            path = ROOT / "sample_data" / filename
            items.append(validate_upload(UploadedFile(filename, path.read_bytes())))
        self.assertEqual(validate_pair(items), [])


if __name__ == "__main__":
    unittest.main()
