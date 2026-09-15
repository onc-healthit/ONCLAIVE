"""Normalize Agent Usage Metrics JSON reports into a small typed model."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Mapping


AGENT_LABELS = {
    "codex": "Codex",
    "claude_code": "Claude Code",
}


@dataclass(frozen=True)
class Metric:
    name: str
    value: Any = None
    status: str = "missing"
    source: str | None = None
    unit: str | None = None
    warnings: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class AgentReport:
    agent_key: str
    agent_label: str
    run_metadata: Mapping[str, Any]
    metrics: Mapping[str, Metric]
    warnings: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    sources_used: tuple[str, ...] = ()
    raw: Mapping[str, Any] = field(default_factory=dict)


def normalize_agent(value: Any) -> tuple[str, str]:
    """Validate the contract agent value and return its UI label."""
    key = value if isinstance(value, str) else ""
    label = AGENT_LABELS.get(key)
    if not label:
        raise ValueError("run_metadata.agent must be exactly 'codex' or 'claude_code'")
    return key, label


def _string_tuple(value: Any) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()
    return tuple(str(item) for item in value if item is not None)


def load_report(payload: Mapping[str, Any]) -> AgentReport:
    """Load an already-decoded JSON object and index metrics by name."""
    metadata = payload.get("run_metadata", {})
    if not isinstance(metadata, Mapping):
        raise ValueError("run_metadata must be a JSON object")

    agent_key, agent_label = normalize_agent(metadata.get("agent"))
    metric_items = payload.get("metrics", [])
    if metric_items is None:
        metric_items = []
    if not isinstance(metric_items, list):
        raise ValueError("metrics must be a JSON array")

    metrics: dict[str, Metric] = {}
    for item in metric_items:
        if not isinstance(item, Mapping):
            raise ValueError("each metrics item must be a JSON object")
        name = str(item.get("name", "")).strip()
        if not name:
            raise ValueError("each metrics item must have a non-empty name")
        metrics[name] = Metric(
            name=name,
            value=item.get("value"),
            status=str(item.get("status") or "missing").lower(),
            source=str(item["source"]) if item.get("source") is not None else None,
            unit=str(item["unit"]) if item.get("unit") is not None else None,
            warnings=_string_tuple(item.get("warnings")),
            notes=_string_tuple(item.get("notes")),
        )

    return AgentReport(
        agent_key=agent_key,
        agent_label=agent_label,
        run_metadata=dict(metadata),
        metrics=metrics,
        warnings=_string_tuple(payload.get("warnings")),
        notes=_string_tuple(payload.get("notes")),
        sources_used=_string_tuple(payload.get("sources_used")),
        raw=dict(payload),
    )


def decode_report(content: bytes | str) -> tuple[dict[str, Any], AgentReport]:
    """Decode UTF-8 JSON and return both the raw payload and normalized report."""
    try:
        text = content.decode("utf-8-sig") if isinstance(content, bytes) else content
        payload = json.loads(text)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Invalid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("Report root must be a JSON object")
    return payload, load_report(payload)
