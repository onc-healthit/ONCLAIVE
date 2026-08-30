"""Command-line helper for inspecting ccusage enrichment results."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from agent_usage_metrics.ccusage_adapter import (
    load_ccusage_data,
    summarize_ccusage_match_diagnostics,
    summarize_ccusage_result,
)
from agent_usage_metrics.input_resolver import resolve_input


def main() -> int:
    """Resolve a Codex target and print a compact ccusage summary."""
    parser = argparse.ArgumentParser(description="Verify ccusage token/cost enrichment with a safe summary.")
    parser.add_argument("--query", help="Natural-language usage request, resolved through deterministic filters.")
    parser.add_argument("--rollout-file", help="Fallback/debug path to one Codex rollout JSONL file.")
    parser.add_argument("--codex-home", help="Optional path to the Codex home directory.")
    parser.add_argument("--workspace", help="Optional workspace/project filter.")
    parser.add_argument("--thread-title", help="Optional conversation/thread title filter.")
    parser.add_argument("--output-dir", help="Optional output directory. Defaults to outputs/.")
    parser.add_argument(
        "--allow-download",
        action="store_true",
        help="Permit bunx/npx/pnpm to download or cache ccusage if needed.",
    )
    parser.add_argument(
        "--match-diagnostics",
        action="store_true",
        help="Include safe ccusage session matching diagnostics.",
    )
    args = parser.parse_args()

    if not args.query and not args.rollout_file:
        parser.error("one of --query or --rollout-file is required")

    resolved = resolve_input(
        query=args.query,
        rollout_file=args.rollout_file,
        codex_home=args.codex_home,
        output_dir=args.output_dir,
        workspace=args.workspace,
        thread_title=args.thread_title,
    )
    result = load_ccusage_data(resolved, allow_download=args.allow_download)
    summary = summarize_ccusage_match_diagnostics(result) if args.match_diagnostics else summarize_ccusage_result(result)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
