"""Command-line entry point for generating agent usage reports."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from agent_usage_metrics.input_resolver import InputResolverError, NeedsClarificationError, resolve_input
from agent_usage_metrics.report_builder import format_report_table
from agent_usage_metrics.report_flow import run_report_flow


REQUIRES_PERMISSION_EXIT_CODE = 3
NEEDS_CLARIFICATION_EXIT_CODE = 4


def main() -> int:
    """Parse report options, resolve a target, and print the generated report paths."""
    parser = argparse.ArgumentParser(description="Generate a privacy-safe Agent Usage Metrics report.")
    parser.add_argument("--query", help="Natural-language usage request, resolved through deterministic filters.")
    parser.add_argument("--rollout-file", help="Path to one Codex rollout JSONL file for a session target.")
    parser.add_argument("--transcript-file", help="Path to one Claude Code transcript JSONL file.")
    parser.add_argument("--agent", choices=("codex", "claude_code"), help="Agent source. Inferred from a Claude Code query or --transcript-file when omitted.")
    parser.add_argument("--codex-home", help="Optional path to the Codex home directory.")
    parser.add_argument("--claude-home", help="Optional path to the Claude home directory. Defaults to ~/.claude.")
    parser.add_argument("--workspace", help="Optional workspace/project filter.")
    parser.add_argument("--thread-title", help="Optional conversation/thread title filter.")
    parser.add_argument("--output-dir", help="Optional output directory. Defaults to outputs/.")
    parser.add_argument(
        "--skip-ccusage",
        action="store_true",
        help="Skip default ccusage token/cost enrichment.",
    )
    parser.add_argument(
        "--allow-download",
        action="store_true",
        help="Permit bunx/npx/pnpm to download or cache ccusage if needed.",
    )
    parser.add_argument(
        "--decline-download",
        action="store_true",
        help="Treat ccusage download/cache permission as declined and continue with token/cost metrics missing.",
    )
    parser.add_argument(
        "--md-filename",
        help="Output Markdown filename. Defaults to agent_usage_metrics_report.md.",
    )
    args = parser.parse_args()

    if not args.query and not args.rollout_file and not args.transcript_file:
        parser.error("one of --query, --rollout-file, or --transcript-file is required")
    if args.rollout_file and args.transcript_file:
        parser.error("--rollout-file and --transcript-file cannot be used together")
    if args.allow_download and args.decline_download:
        parser.error("--allow-download and --decline-download cannot be used together")

    selected_file = args.transcript_file or args.rollout_file
    selected_agent = args.agent or ("claude_code" if args.transcript_file else None)
    try:
        resolved = resolve_input(
            query=args.query,
            rollout_file=selected_file,
            codex_home=args.codex_home,
            claude_home=args.claude_home,
            agent=selected_agent,
            output_dir=args.output_dir,
            workspace=args.workspace,
            thread_title=args.thread_title,
        )
    except NeedsClarificationError as exc:
        print("Resolver status: needs_clarification")
        print(str(exc))
        return NEEDS_CLARIFICATION_EXIT_CODE
    except (InputResolverError, FileNotFoundError, PermissionError) as exc:
        print(f"Could not resolve agent usage report target: {exc}", file=sys.stderr)
        print(
            "Provide one of: session/run, conversation/thread title, workspace/project with date range, "
            "or rollout/transcript JSONL file path.",
            file=sys.stderr,
        )
        return 2

    flow_result = run_report_flow(
        resolved,
        skip_ccusage=args.skip_ccusage,
        allow_download=args.allow_download,
        decline_download=args.decline_download,
        md_filename=args.md_filename,
    )
    if flow_result.status == "requires_permission":
        print("ccusage status: requires_permission")
        print(flow_result.permission_question)
        print("No report was finalized. Rerun with --allow-download if approved or --decline-download if declined.")
        return REQUIRES_PERMISSION_EXIT_CODE

    if flow_result.report is None:
        print("Report flow did not produce a report.", file=sys.stderr)
        return 1

    print(format_report_table(flow_result.report))
    print()
    print(f"Markdown report written to: {flow_result.markdown_path}")
    if flow_result.breakdown_path:
        print(f"Per-session breakdown written to: {flow_result.breakdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
