"""Canonical ONCLAIVE Agent Usage Metrics dashboard contract."""

REQUIRED_METRIC_NAMES = (
    "wall_clock_time_seconds",
    "estimated_cost",
    "human_prompts_required",
    "tool_calls",
    "file_edits",
    "input_tokens",
    "output_tokens",
    "total_tokens",
)

INTEGER_METRIC_NAMES = {
    "human_prompts_required",
    "tool_calls",
    "file_edits",
    "input_tokens",
    "output_tokens",
    "total_tokens",
}

ALLOWED_STATUSES = {"computed", "partial", "missing", "estimated"}

REQUIRED_RUN_METADATA_FIELDS = (
    "agent",
    "session_files",
    "conversation_name",
    "workspace_name",
    "scope_type",
    "model",
    "generated_at",
)

ALLOWED_SCOPE_TYPES = {"conversation", "session", "workspace"}
