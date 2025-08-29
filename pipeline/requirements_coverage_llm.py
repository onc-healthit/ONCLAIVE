#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Requirements Coverage (detail-aware)
- Chunks requirements into batches for scalability
- Model is read from API_CONFIGS; just set API_TYPE below
"""

import sys, re, json
from pathlib import Path

# ---------- CONFIG ----------
LLM_UTILS_PATH = "llm_utils.py"
ENV_PATH       = "./.env"
REQ_PATH       = "pipeline/checkpoints/claude_uscore_capstatement_test_set_reqs.md" #TODO: Dynamically update
TEST_PLAN_PATH = "pipeline/checkpoints/claude_test_plan_20250827_115316.md" #TODO: Dynamically update
PROMPT_PATH    = "prompts/requirements_coverage.txt"
OUT_DIR        = "./reports"

API_TYPE       = "claude"   # change to "gpt" or "gemini" if needed
MAX_TOKENS     = 5000
BATCH_SIZE     = 12
RAW_PREVIEW    = 1000       # how many chars of raw LLM output to echo
# -----------------------------

# --- setup imports ---
sys.path.insert(0, str(Path(LLM_UTILS_PATH).parent))
try:
    import dotenv; dotenv.load_dotenv(ENV_PATH)
except Exception:
    pass

from llm_utils import LLMApiClient, API_CONFIGS
client = LLMApiClient(config=API_CONFIGS)

REQ_BLOCK_RE = re.compile(r"^---\s*#\s*(REQ-\d+)(.*?)^---", re.M | re.S)

def _force_json(text: str):
    """Try to coerce model output into JSON (with inner { ... } salvage)."""
    if not text or not text.strip():
        raise ValueError("LLM returned empty response")
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{.*\}", text, re.S)
        if m:
            return json.loads(m.group(0))
        raise

def _extract_req_blocks(req_md: str):
    return [(m.group(1).strip(), m.group(2)) for m in REQ_BLOCK_RE.finditer(req_md)]

def main():
    req_md   = Path(REQ_PATH).read_text()
    plan_md  = Path(TEST_PLAN_PATH).read_text()
    prompt   = Path(PROMPT_PATH).read_text()

    req_blocks = _extract_req_blocks(req_md)
    all_details = []

    for i in range(0, len(req_blocks), BATCH_SIZE):
        batch = req_blocks[i:i+BATCH_SIZE]
        batch_md = "\n".join([f"--- # {rid}\n{blk}\n---" for rid, blk in batch])
        user = f"{prompt.strip()}\n\n## REQUIREMENTS (markdown)\n{batch_md}\n\n## TEST PLAN (markdown)\n{plan_md}"

        out = client.make_llm_request(
            api_type=API_TYPE,
            prompt=user,
            sys_prompt="You are precise and return only valid JSON.",
            max_tokens=MAX_TOKENS,
        )

        # --- DEBUG: raw response for this batch ---
        print(f"\n=== RAW OUTPUT (Requirements batch {i//BATCH_SIZE + 1}) ===")
        print((out or "")[:RAW_PREVIEW])
        print("=== END RAW OUTPUT ===\n")

        data = _force_json(out)
        all_details.extend(data.get("details", []))

    # Consolidate per-REQ
    by_req = {d.get("req_id"): d for d in all_details if d.get("req_id")}
    covered = sum(1 for d in by_req.values()
                  if d.get("facets") and all(f.get("covered") for f in d["facets"]))
    total = len(by_req)
    coverage_pct = covered / total if total else 0.0

    report = {
        "profile": "us-core Condition",
        "requirements_total": total,
        "requirements_covered": covered,
        "coverage_pct": coverage_pct,
        "details": list(by_req.values()),
    }

    out_dir = Path(OUT_DIR); out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "requirements_coverage.json").write_text(json.dumps(report, indent=2))

    lines = [f"# Requirements Coverage (detail-aware)\n",
             f"Coverage: {coverage_pct*100:.1f}%\n",
             "## Details\n"]
    for rid, d in by_req.items():
        lines.append(f"### {rid} (score: {d.get('score')})")
        for fct in d.get("facets", []):
            lines.append(f"- [{'x' if fct.get('covered') else ' '}] {fct.get('name')} — {fct.get('notes','')}")
        lines.append("")
    (out_dir / "requirements_coverage.md").write_text("\n".join(lines))

if __name__ == "__main__":
    main()
