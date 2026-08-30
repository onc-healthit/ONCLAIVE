# agent-usage-metrics-skill

This skill creates Markdown usage metrics reports for agent runs. It supports Codex runs, conversations, and workspace reports. Claude Code is also supported: workflow metrics come from Claude transcript logs, while token and cost values are enriched with ccusage only when it can confidently match the run.

## How to use it

To report on one Codex conversation, provide its exact conversation name. If it belongs to a workspace, also provide the exact workspace name.

To report on a whole workspace, provide the exact workspace name and a time range, `latest`, or an explicit all-time request. If more than one target matches, the skill asks for clarification instead of guessing.

## Outputs

The main output is a Markdown report, written by default to:

```text
outputs/agent_usage_metrics_report.md
```

When a conversation or workspace report contains multiple sessions, the skill also writes a per-session breakdown:

```text
outputs/agent_usage_metrics_session_breakdown.md
```

The main report links to this breakdown. If you choose a custom main report filename, the breakdown uses the same stem with `_session_breakdown.md` appended.

Workspace reports list the conversation/thread title for each matched session when local Codex or Claude Code metadata provides it. Codex `state_5.sqlite` `threads.title` is the primary Codex title source, followed by `threads.name`, `session_index.jsonl` `thread_name`, and recognized rollout title fields. When no title is available, the report shows `Unavailable` and retains the rollout/session filename as the fallback identifier.

## Metrics currently supported

Available metrics depend on the source data, but include:

- Session duration: recorded duration or wall-clock time for Codex; transcript/session duration for Claude Code.
- Human prompts.
- Tool calls, including shell commands when they are part of tool activity; Claude Code also reports shell commands separately.
- File edit candidates.
- API request count when Codex telemetry provides it.
- Warnings and errors when source data provides them.
- Token and cost enrichment when ccusage can confidently match the run.

## Notes on partial metrics

- File edits are partial because shell commands or scripts can modify files without explicit edit events.
- Token and cost values depend on ccusage being available and confidently matched to the session.
- If token or cost matching is ambiguous, the report marks those values unavailable or ambiguous instead of guessing.

For agent execution details, see `SKILL.md`.
