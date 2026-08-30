"""Command-line helper for inspecting normalized Codex events."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from agent_usage_metrics.codex_source_adapter import load_raw_codex_data
from agent_usage_metrics.event_normalizer import normalize_codex_events, summarize_normalized_event_data
from agent_usage_metrics.input_resolver import resolve_input


def main() -> int:
    """Resolve a Codex target and print its normalized event summary."""
    parser = argparse.ArgumentParser(description="Verify Codex event normalization with a safe summary.")
    parser.add_argument("--query", help="Natural-language usage request, resolved through deterministic filters.")
    parser.add_argument("--rollout-file", help="Fallback/debug path to one Codex rollout JSONL file.")
    parser.add_argument("--codex-home", help="Optional path to the Codex home directory.")
    parser.add_argument("--output-dir", help="Optional output directory. Defaults to outputs/.")
    args = parser.parse_args()

    if not args.query and not args.rollout_file:
        parser.error("one of --query or --rollout-file is required")

    resolved = resolve_input(
        query=args.query,
        rollout_file=args.rollout_file,
        codex_home=args.codex_home,
        output_dir=args.output_dir,
    )
    raw_data = load_raw_codex_data(resolved)
    event_data = normalize_codex_events(raw_data)
    print(json.dumps(summarize_normalized_event_data(event_data), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
