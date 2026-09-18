---
name: agent-usage-metrics-skill
description: Generate privacy-safe Agent Usage Metrics reports for Codex agent runs, conversations, and workspace/date scopes. Use when asked to inspect local Codex usage, summarize agent run metrics, export Markdown reports, or evaluate ONCLAIVE-style usage metrics from Codex session/log sources.
---

# Agent Usage Metrics Skill

Use the bundled scripts from the skill directory root. Do not reimplement Codex log parsing or report formatting unless the user explicitly asks to modify the skill.

## Target Types

The user-facing report targets are:

- `session` - one agent run / one rollout JSONL file. Best for measuring a single Codex execution.
- `conversation` - one Codex chat/thread/conversation. A conversation may contain multiple sessions/agent runs for the same task.
- `workspace` - broader project/repo activity, usually over a date, date range, latest, or explicit all-time intent. Best for broader project-level reporting.

Do not add a fourth user-facing target type for task-like labels. If a phrase looks like a task name, treat it as evidence for a conversation title, session identifier, or workspace search term.

For `conversation` and `workspace` reports, Codex-derived metrics are computed by running the single-session metric path for each resolved rollout/session file and summing the per-session metric results. Wall-clock time is the sum of session wall-clock durations, not the elapsed span from the first session start to the last session end.

## Available Scripts

- `scripts/run_metrics.py` - Generate the user-facing metrics report and export Markdown.
- `scripts/verify_sources.py` - Inspect source loading with a privacy-safe summary.
- `scripts/verify_normalization.py` - Inspect event normalization with a privacy-safe summary.
- `scripts/verify_metrics.py` - Inspect basic metric output with a privacy-safe summary.
- `scripts/verify_ccusage.py` - Inspect ccusage token/cost enrichment with a privacy-safe summary.

Run `python <script> --help` for exact flags.

## Report Workflow

For a natural-language request:

```powershell
python scripts/run_metrics.py --query 'Create a report for the "Build v1.1.0 inventory" conversation in the ONCLAIVE project.' --codex-home "<CODEX_HOME>"
```

For a direct rollout/session file:

```powershell
python scripts/run_metrics.py --rollout-file "<SESSION_JSONL>" --output-dir outputs
```

For a direct Claude Code transcript:

```powershell
python scripts/run_metrics.py --agent claude_code --transcript-file "<CLAUDE_TRANSCRIPT_JSONL>" --output-dir outputs
```

Claude Code discovery reads transcript JSONL under `~/.claude/projects`. Workflow metrics are computed from transcripts. ccusage remains a separate token/cost enrichment source and must match a Claude session confidently by session ID or a reliable combination of workspace, activity time, and model metadata.

Claude Code API request count is unavailable because transcripts do not provide reliable request telemetry. File edits are partial because shell commands can modify files without explicit Write/Edit events. Transcript duration is elapsed first-to-last transcript time, not active agent time.

Then return the console summary and the Markdown report path printed by the script. If a multi-session `conversation` or `workspace` report creates a per-session breakdown, return that Markdown path too.

## Good Prompts

- `Create a report for session rollout-2026-07-07T21-38-07-019f3f60-07d8-7a53-b30e-a74e67f53be6.jsonl.`
- `Create a report for the "Build v1.1.0 inventory" conversation in the ONCLAIVE project.`
- `Create an ONCLAIVE workspace report for 2026-07-07.`
- `Create an all-time ONCLAIVE workspace report.`
- `Create a report for the latest Codex run in workspace ONCLAIVE.`

## Ambiguous Prompts

- `Create a report for "Build v1.1.0 inventory" in ONCLAIVE` is ambiguous if the phrase only partially matches multiple conversations or sessions.
- `Create an ONCLAIVE project report` is ambiguous when multiple sessions exist and no date range or target type is provided.
- `Create a report for the inventory work` is too vague unless local metadata contains an exact safe title or identifier match.

When the target is ambiguous, return a `needs_clarification` result. Explain the three target types only in this clarification path, list safe candidate metadata when available, and ask whether the user wants a whole conversation/workspace or one specific session.

## Resolution Rules

- Exact rollout filename or session ID resolves to `session`.
- Exact conversation/thread/chat title resolves to `conversation`.
- Workspace/project name plus date range, latest, or explicit all-time intent resolves to `workspace`.
- Quoted phrases are matched in this order: conversation titles, session identifiers or rollout filenames, workspace/project names, then broader fuzzy search if needed.
- Workspace reports require a time window unless the user explicitly asks for latest or all-time.
- If a conversation contains multiple sessions, do not silently select one rollout file. Resolve the whole conversation when the match is exact, or clarify when the match is ambiguous.
- If multiple rollout/session files match the same conversation/workspace/date context and no explicit target can be chosen, return `needs_clarification`; do not pick newest or first.

Safe candidate metadata may include rollout basename, start time, end time or duration, workspace label, conversation title, and aggregate counts. Do not expose raw prompts, raw payloads, private Codex log contents, or sensitive full local paths.

When a request is ambiguous, return a `needs_clarification` result. If multiple target types are possible, briefly explain the difference between `session`, `conversation`, and `workspace` so the user understands what they are choosing.

## Report Outputs

Reports are Markdown-only. The main report stays high-level. For `conversation` and `workspace` reports with more than one resolved session, also create a separate per-session breakdown Markdown file and link it from the main report. Do not create a breakdown for single-session reports.

The per-session breakdown should include one row per rollout/session with safe timing, Codex-derived metrics, ccusage status/precision/reason, and token/cost values when confidently available. Do not include raw prompts, raw payloads, private log contents, or sensitive file contents.

Workspace reports should show each matched session's conversation/thread title when local metadata provides one. For Codex, treat nonempty `state_5.sqlite` `threads.title` as authoritative title metadata, followed by `threads.name`, `session_index.jsonl` `thread_name`, and recognized rollout title fields. Preserve the strict raw-content filter for rollout JSONL title candidates. Use `Unavailable` when no supported title metadata is present and retain the rollout/session filename as the fallback identifier. Both the main report and per-session breakdown must include a clear warnings section; show `Warnings: None` when there are no warnings and list the specific messages otherwise.

## ccusage

`scripts/run_metrics.py` attempts ccusage token/cost enrichment for every supported report by default because input tokens, output tokens, and estimated cost come from ccusage.

- For `session`, ccusage must match one ccusage session confidently before token/cost metrics are populated.
- For `conversation`, resolve the underlying rollout/session files, match each file to a ccusage session row, and sum only confidently matched per-session ccusage metrics.
- For `workspace`, resolve the workspace/time-window rollout/session files, match each file to a ccusage session row, and sum only confidently matched per-session ccusage metrics.
- Mark conversation/workspace ccusage precision honestly: exact when all sessions match, partial when only some sessions match, and missing when no confident matches are available.
- If ccusage matching is partial or ambiguous, the main report and breakdown must say so with a clear reason or warning.
- Never use day-level totals as exact `session`, `conversation`, or `workspace` metrics.
- If ccusage is available locally or globally, use it.
- If ccusage reports `requires_permission`, pause before finalizing the report and ask the user exactly: "ccusage is needed to calculate input tokens, output tokens, and estimated cost. It is not currently available locally, but it can be downloaded or cached using bunx/npx/pnpm. Do you approve? yes/no"
- Do not silently download/cache ccusage through bunx/npx/pnpm.
- Do not silently skip ccusage when permission is needed.
- If the user approves, rerun with `--allow-download`.
- If the user declines, rerun with `--decline-download`; token/cost metrics will be marked missing with warnings.
- Use `--skip-ccusage` only when the user explicitly asks to skip token/cost enrichment.
- If ccusage is completely unavailable and no bunx/npx/pnpm runner exists, still generate the report with token/cost metrics missing.

## Script Behavior

- Run scripts non-interactively with command-line flags.
- Use relative paths from the skill directory root.
- Treat nonzero exits as actionable errors; report what selector, file path, clarification, or permission is needed.
- Prefer the exported Markdown report for human reading.
- Keep output concise enough to fit in the agent context.

## Privacy

Do not expose raw prompts, raw payloads, private Codex log contents, local SQLite databases, or sensitive local paths in user-facing output. Do not package local `.codex` data, JSONL sessions, SQLite databases, generated reports, or private fixtures into the skill.
