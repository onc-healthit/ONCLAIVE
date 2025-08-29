#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Plan Coverage (detail-aware, plan→kit only), scalable across many Ruby files.
"""

import sys, re, os, json
from pathlib import Path
from typing import Dict, List

# ---------- CONFIG ----------
LLM_UTILS_PATH    = "llm_utils.py"
ENV_PATH          = "./.env"
TEST_PLAN_PATH    = "pipeline/checkpoints/claude_test_plan_20250827_115316.md" #TODO: Dynamically update
TEST_KIT_ROOT     = "pipeline/checkpoints/test_kit" #TODO: Dynamically update
PROMPT_PATH       = "prompts/test_plan_coverage.txt"
DSL_GUIDANCE_PATH = "dsl-guidance.md"

OUT_DIR           = "./reports"
API_TYPE          = "claude"   # change to "gpt"/"gemini" if desired
MAX_TOKENS        = 9000

# Batching knobs
MAX_CHARS_PER_BATCH = 120_000
MAX_FILES_PER_BATCH = 25
RAW_PREVIEW         = 800

# Optional subtree filter. Leave [] to scan all dynamically.
INCLUDE_PATH_FILTER: List[str] = []
# -----------------------------

# --- setup imports ---
sys.path.insert(0, str(Path(LLM_UTILS_PATH).parent))
try:
    import dotenv; dotenv.load_dotenv(ENV_PATH)
except Exception:
    pass
from llm_utils import LLMApiClient, API_CONFIGS

# Force deterministic-ish settings
if API_TYPE in API_CONFIGS:
    cfg = dict(API_CONFIGS[API_TYPE])  # copy
    cfg["temperature"] = 0.1
    API_CONFIGS[API_TYPE] = cfg

client = LLMApiClient(config=API_CONFIGS)

# --- Helpers: I/O + JSON salvage ---
def _force_json(text: str) -> dict:
    if not text or not text.strip():
        raise ValueError("LLM returned empty response")
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{.*\}", text, re.S)
        if m:
            return json.loads(m.group(0))
        raise

def _should_include(path: Path) -> bool:
    if not INCLUDE_PATH_FILTER:
        return True
    p = str(path).replace("\\", "/")
    return any(token in p for token in INCLUDE_PATH_FILTER)

def find_ruby_files(root: str) -> List[Path]:
    files = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith(".rb"):
                p = Path(dirpath) / fname
                if _should_include(p):
                    files.append(p)
    return files

# --- Robust REQ detection (underscore-safe) ---
REQ_PATTERNS = [
    re.compile(r"REQ[-_\s]?(\d{3})(?=\D|$)", re.IGNORECASE),
    re.compile(r"Requirement[-_\s]?(\d{3})(?=\D|$)", re.IGNORECASE),
]
FILENAME_PATTERNS = [
    re.compile(r"req[-_]?(\d{3})(?=\D|$)", re.IGNORECASE),
    re.compile(r"(?<!\d)(\d{3})(?!\d)", re.IGNORECASE),
]

def _norm_req(num: str) -> str:
    d = num[-3:]
    d = d.zfill(3)
    return f"REQ-{d}"

def detect_req_ids_from_string(s: str) -> List[str]:
    hits = []
    for pat in REQ_PATTERNS:
        hits.extend(m.group(1) for m in pat.finditer(s or ""))
    seen, out = set(), []
    for h in hits:
        rid = _norm_req(h)
        if rid not in seen:
            out.append(rid); seen.add(rid)
    return out

def detect_req_ids_from_filename(name: str) -> List[str]:
    hits = []
    for pat in FILENAME_PATTERNS:
        hits.extend(m.group(1) for m in pat.finditer(name or ""))
    seen, out = set(), []
    for h in hits:
        rid = _norm_req(h)
        if rid not in seen:
            out.append(rid); seen.add(rid)
    return out

def detect_req_ids_for_file(path: Path, body: str) -> List[str]:
    ids = detect_req_ids_from_string(str(path))
    if ids:
        return ids
    ids = detect_req_ids_from_filename(path.name)
    if ids:
        return ids
    ids = detect_req_ids_from_string(body)
    if ids:
        return ids
    return []

def bucket_by_req(files: List[Path]) -> Dict[str, List[Path]]:
    buckets: Dict[str, List[Path]] = {}
    for p in files:
        try:
            body = p.read_text(errors="ignore")
        except Exception:
            body = ""
        ids = detect_req_ids_for_file(p, body)
        if not ids:
            ids = ["misc"]
        for rid in ids:
            buckets.setdefault(rid, []).append(p)
    return buckets

# --- Batching ---
def chunk_files(paths: List[Path]) -> List[List[Path]]:
    batches: List[List[Path]] = []
    cur, cur_size = [], 0
    for p in paths:
        try:
            txt = p.read_text(errors="ignore")
        except Exception:
            txt = ""
        size = len(txt)
        if cur and (cur_size + size > MAX_CHARS_PER_BATCH or len(cur) >= MAX_FILES_PER_BATCH):
            batches.append(cur)
            cur, cur_size = [], 0
        cur.append(p)
        cur_size += size
    if cur:
        batches.append(cur)
    return batches

def files_blob(batch: List[Path]) -> str:
    parts = []
    for p in batch:
        try:
            content = p.read_text(errors="ignore").splitlines()
        except Exception:
            content = []
        numbered = "\n".join(f"{i+1:>5}  {line}" for i, line in enumerate(content))
        parts.append(f"### FILE: {p.name}\n```\n{numbered}\n```")
    return "\n".join(parts)

def extract_req_sections_from_plan(plan_md: str, req_id: str) -> str:
    idx = plan_md.find(req_id)
    if idx == -1:
        return plan_md
    span = 5000
    start = max(0, idx - span)
    end   = min(len(plan_md), idx + span)
    snippet = plan_md[start:end]
    return f"(Plan excerpt for {req_id})\n{snippet}"

def merge_batches(per_batch: List[dict]) -> dict:
    by_name = {}
    for b in per_batch:
        for r in b.get("requirements", []):
            for f in r.get("facets", []):
                name = (f.get("name") or "").strip()
                if not name:
                    continue
                if name not in by_name:
                    by_name[name] = {
                        "name": name,
                        "implemented": bool(f.get("implemented")),
                        "evidence": f.get("evidence"),
                    }
                else:
                    if f.get("implemented") and not by_name[name]["implemented"]:
                        by_name[name]["implemented"] = True
                        by_name[name]["evidence"] = f.get("evidence")
    facets = [by_name[k] for k in sorted(by_name.keys())]
    total = len(facets)
    implemented = sum(1 for f in facets if f.get("implemented"))
    return {
        "facets": facets,
        "facets_total": total,
        "facets_implemented": implemented,
        "scores": {"tpc": (implemented / total) if total else 0.0},
    }

# --- Main ---
def main():
    plan_md = Path(TEST_PLAN_PATH).read_text()
    prompt  = Path(PROMPT_PATH).read_text()
    dsl_md  = Path(DSL_GUIDANCE_PATH).read_text() if Path(DSL_GUIDANCE_PATH).exists() else ""

    rb_files = find_ruby_files(TEST_KIT_ROOT)
    if not rb_files:
        print("No Ruby files found at:", TEST_KIT_ROOT)
        return

    buckets = bucket_by_req(rb_files)

    print("\n=== REQ Buckets Summary ===")
    for rid in sorted(buckets.keys()):
        sample = ", ".join([q.name for q in buckets[rid][:5]])
        more = "" if len(buckets[rid]) <= 5 else f" (+{len(buckets[rid]) - 5} more)"
        print(f"{rid}: {len(buckets[rid])} file(s) -> {sample}{more}")
    print("=== END REQ Buckets Summary ===\n")

    results = []
    for req_id, paths in sorted(buckets.items()):
        if req_id == "misc":
            continue

        batches = chunk_files(paths)
        per_batch_outputs = []
        plan_excerpt = extract_req_sections_from_plan(plan_md, req_id)

        for bi, batch in enumerate(batches, start=1):
            batch_blob = files_blob(batch)
            user = (
                f"{prompt.strip()}\n\n"
                f"## DSL GUIDANCE (markdown)\n{dsl_md}\n\n"  # ← NEW line to include DSL guidance
                f"## TEST PLAN (markdown)\n{plan_excerpt}\n\n"
                f"## RUBY TEST FILES (subset for {req_id}, batch {bi}/{len(batches)})\n{batch_blob}\n"
            )

            out = client.make_llm_request(
                api_type=API_TYPE,
                prompt=user,
                sys_prompt="You are precise and return only valid JSON.",
                max_tokens=MAX_TOKENS,
            )

            print(f"\n=== RAW OUTPUT ({req_id} batch {bi}/{len(batches)}) ===")
            print((out or "")[:RAW_PREVIEW])
            print("=== END RAW OUTPUT ===\n")

            data = _force_json(out)
            per_batch_outputs.append(data)

        merged = merge_batches(per_batch_outputs)
        merged["req_id"] = req_id
        results.append(merged)

    tpcs = [r["scores"]["tpc"] for r in results if "scores" in r]
    tpc_overall = sum(tpcs) / len(tpcs) if tpcs else 0.0

    output = {
        "profile": "us-core Condition",
        "requirements": [
            {
                "req_id": r["req_id"],
                "facets_total": r["facets_total"],
                "facets_implemented": r["facets_implemented"],
                "facets": r["facets"],
                "scores": {"tpc": r["scores"]["tpc"]},
            }
            for r in results
        ],
        "tpc_overall": tpc_overall,
    }

    out_dir = Path(OUT_DIR); out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "test_plan_coverage.json").write_text(json.dumps(output, indent=2))

    lines = [
        "# Test Plan Coverage (detail-aware, batched)\n",
        f"Overall TPC: {tpc_overall*100:.1f}%\n",
        "## Per-Requirement\n"
    ]
    for r in output["requirements"]:
        lines.append(f"### {r['req_id']} — TPC {r['scores']['tpc']*100:.1f}%")
        if r.get("facets"):
            lines.append("Facets:")
            for fct in r["facets"]:
                mark = "x" if fct.get("implemented") else " "
                ev = fct.get("evidence")
                evs = f" (evidence: {ev.get('file')} — {ev.get('rationale')})" if ev else ""
                lines.append(f"- [{mark}] {fct.get('name','')}{evs}")
        missing = [f for f in r.get("facets", []) if not f.get("implemented")]
        if missing:
            lines.append("Missing facets noted by LLM:")
            for f in missing:
                lines.append(f"- {f.get('name')}")
        lines.append("")
    (out_dir / "test_plan_coverage.md").write_text("\n".join(lines))

if __name__ == "__main__":
    main()
