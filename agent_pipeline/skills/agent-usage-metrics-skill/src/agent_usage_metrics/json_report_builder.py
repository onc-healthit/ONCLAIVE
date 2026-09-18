"""Map normalized Agent Usage Metrics reports to the dashboard JSON contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import AgentUsageReport, MetricResult


DASHBOARD_METRIC_NAMES = (
    "wall_clock_time_seconds",
    "estimated_cost",
    "human_prompts_required",
    "tool_calls",
    "file_edits",
    "input_tokens",
    "output_tokens",
    "total_tokens",
)
SUPPORTED_METRIC_STATUSES = {"computed", "partial", "estimated", "missing"}


def dashboard_report_to_dict(report: AgentUsageReport) -> dict[str, Any]:
    """Create the explicit shared Codex/Claude Code dashboard payload."""
    metrics_by_name = {metric.name: metric for metric in report.metrics}
    metrics = [
        _dashboard_metric(name, metrics_by_name.get(name))
        for name in DASHBOARD_METRIC_NAMES
        if name != "total_tokens"
    ]
    metrics.append(_total_tokens_metric(metrics_by_name))

    metadata = report.run_metadata
    return {
        "run_metadata": {
            "agent": _dashboard_agent(metadata.agent),
            "session_files": [Path(name).name for name in metadata.rollout_files],
            "conversation_name": metadata.thread_title,
            "workspace_name": metadata.workspace,
            "scope_type": metadata.scope_type,
            "model": metadata.model,
            "generated_at": metadata.generated_at,
        },
        "metrics": metrics,
        "warnings": list(report.warnings),
        "sources_used": list(report.sources_used),
    }


def export_dashboard_json(
    report: AgentUsageReport,
    output_dir: str | Path,
    filename: str,
) -> Path:
    """Write one dashboard-ready JSON report."""
    destination_dir = Path(output_dir).expanduser()
    destination_dir.mkdir(parents=True, exist_ok=True)
    output_path = destination_dir / Path(filename).name
    payload = dashboard_report_to_dict(report)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output_path.resolve()


def _dashboard_metric(name: str, metric: MetricResult | None) -> dict[str, Any]:
    if metric is None:
        result = {
            "name": name,
            "value": None,
            "status": "missing",
            "source": None,
            "warnings": [],
            "notes": [],
        }
    else:
        value = _numeric_value(metric.value)
        status = metric.status
        warnings = list(metric.warnings)
        notes = list(metric.notes)
        if status not in SUPPORTED_METRIC_STATUSES:
            warnings.append(f"Unsupported internal metric status '{status}' was exported as missing.")
            value = None
            status = "missing"
        if metric.value is not None and value is None:
            warnings.append(f"{name} was not numeric and was exported as missing.")
            status = "missing"
        result = {
            "name": name,
            "value": value,
            "status": status,
            "source": metric.source,
            "warnings": _dedupe(warnings),
            "notes": notes,
        }

    if name == "estimated_cost":
        result["unit"] = "USD"
    return result


def _total_tokens_metric(metrics_by_name: dict[str, MetricResult]) -> dict[str, Any]:
    input_tokens = metrics_by_name.get("input_tokens")
    output_tokens = metrics_by_name.get("output_tokens")
    input_value = _numeric_value(input_tokens.value) if input_tokens else None
    output_value = _numeric_value(output_tokens.value) if output_tokens else None
    if input_value is None or output_value is None:
        missing_inputs = [
            name
            for name, value in (("input_tokens", input_value), ("output_tokens", output_value))
            if value is None
        ]
        verb = "is" if len(missing_inputs) == 1 else "are"
        return {
            "name": "total_tokens",
            "value": None,
            "status": "missing",
            "source": "derived",
            "warnings": [
                "total_tokens is unavailable because " + " and ".join(missing_inputs) + f" {verb} missing."
            ],
            "notes": ["Derived only when both input_tokens and output_tokens are available."],
        }
    return {
        "name": "total_tokens",
        "value": input_value + output_value,
        "status": "computed",
        "source": "derived",
        "warnings": [],
        "notes": [],
    }


def _numeric_value(value: Any) -> int | float | None:
    if isinstance(value, bool) or not isinstance(value, int | float):
        return None
    return value


def _dashboard_agent(agent: str) -> str:
    if agent not in {"codex", "claude_code"}:
        raise ValueError(f"Unsupported dashboard agent: {agent}")
    return agent


def _dedupe(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))
