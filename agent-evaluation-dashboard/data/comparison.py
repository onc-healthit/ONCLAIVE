"""Metric lookup and comparison logic, independent from Streamlit."""

from __future__ import annotations

from dataclasses import dataclass
from numbers import Real

from .loader import AgentReport, Metric


@dataclass(frozen=True)
class MetricDefinition:
    label: str
    names: tuple[str, ...]
    kind: str = "number"


@dataclass(frozen=True)
class MetricComparison:
    definition: MetricDefinition
    codex: Metric
    claude: Metric

    @property
    def difference(self) -> float | None:
        if is_number(self.codex.value) and is_number(self.claude.value):
            return abs(float(self.codex.value) - float(self.claude.value))
        return None


CORE_METRICS = (
    MetricDefinition("Wall-clock time", ("wall_clock_time_seconds",), "duration"),
    MetricDefinition("Estimated cost", ("estimated_cost",), "currency"),
    MetricDefinition("Human prompts required", ("human_prompts_required",), "integer"),
    MetricDefinition("Tool calls", ("tool_calls",), "integer"),
    MetricDefinition("File edits", ("file_edits",), "integer"),
    MetricDefinition("Total tokens", ("total_tokens",), "integer"),
)

TOKEN_METRICS = (
    MetricDefinition("Input Tokens", ("input_tokens",), "integer"),
    MetricDefinition("Output Tokens", ("output_tokens",), "integer"),
    MetricDefinition("Total Tokens", ("total_tokens",), "integer"),
)


def is_number(value: object) -> bool:
    return isinstance(value, Real) and not isinstance(value, bool)


def metric_for(report: AgentReport, definition: MetricDefinition) -> Metric:
    for name in definition.names:
        if name in report.metrics:
            return report.metrics[name]
    return Metric(name=definition.names[0])


def compare_metric(
    codex: AgentReport, claude: AgentReport, definition: MetricDefinition
) -> MetricComparison:
    return MetricComparison(definition, metric_for(codex, definition), metric_for(claude, definition))


def order_reports(reports: list[AgentReport]) -> tuple[AgentReport, AgentReport]:
    indexed = {report.agent_key: report for report in reports}
    if set(indexed) != {"codex", "claude_code"}:
        raise ValueError("Expected one Codex report and one Claude Code report")
    return indexed["codex"], indexed["claude_code"]


def format_value(value: object, kind: str) -> str:
    if not is_number(value):
        return "N/A"
    number = float(value)
    if kind == "duration":
        if number >= 60:
            minutes, seconds = divmod(round(number), 60)
            return f"{minutes}m {seconds:02d}s"
        formatted = f"{number:,.1f}".rstrip("0").rstrip(".")
        return f"{formatted}s"
    if kind == "currency":
        return f"${number:,.2f}"
    if kind == "integer":
        return f"{number:,.0f}"
    return f"{number:,.2f}"


def takeaway_text(
    codex: AgentReport, claude: AgentReport, definition: MetricDefinition
) -> str | None:
    """Build a natural-language takeaway only when both values are available."""
    comparison = compare_metric(codex, claude, definition)
    difference = comparison.difference
    if difference is None:
        return None

    codex_value = float(comparison.codex.value)
    claude_value = float(comparison.claude.value)
    amount = abs(codex_value - claude_value)
    if amount < 1e-9:
        return (
            "Same estimated cost"
            if definition.kind == "currency"
            else "Same runtime"
        )
    winner = "Claude Code" if claude_value < codex_value else "Codex"
    if definition.kind == "currency":
        return f"{winner} cost ${amount:,.2f} less"
    return f"{winner} finished {format_value(amount, 'duration')} faster"
