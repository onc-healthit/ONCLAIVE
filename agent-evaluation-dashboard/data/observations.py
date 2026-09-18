"""Deterministic summary text for multi-conversation reports."""

from __future__ import annotations

from typing import Sequence

from .aggregation import conversation_name
from .comparison import CORE_METRICS, is_number, metric_for
from .loader import AgentReport


def build_highest_token_summary(reports: Sequence[AgentReport]) -> str | None:
    """Describe the highest token share when all uploaded totals are available."""
    if len(reports) <= 1:
        return None
    values = [metric_for(report, CORE_METRICS[5]).value for report in reports]
    if any(not is_number(value) for value in values):
        return None
    numeric = [float(value) for value in values]
    combined = sum(numeric)
    if combined <= 0:
        return None
    highest_index = max(range(len(numeric)), key=numeric.__getitem__)
    percentage = numeric[highest_index] / combined * 100
    count = len(reports)
    noun = "conversation" if count == 1 else "conversations"
    return (
        f"Across {count} {noun}, {conversation_name(reports[highest_index])} had the "
        "highest token usage, "
        f"accounting for {percentage:.1f}% of the total."
    )
