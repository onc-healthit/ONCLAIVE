#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Plan Coverage (detail-aware, plan→kit only), scalable across many Ruby files.
Optimized for efficiency and rate-limit resilience:
- Single-pass file indexing (no repeated disk I/O)
- Exact per-REQ plan excerpt extraction (anchor-based)
- Global job queue + small worker pool (ThreadPoolExecutor)
- Exponential backoff with jitter on overload/5xx
- Per-batch checkpointing for resume
- REQ range selection (--req "1-123,1000-1228,77,REQ-200")
- Selective redo that deletes only targeted checkpoints (--redo)

Outputs:
  reports_uscore_full/test_plan_coverage.json
  reports_uscore_full/test_plan_coverage.md
  reports_uscore_full/.chk/<REQ>__batch_###.json  (checkpoints)
"""

import sys, re, os, json, time, random, argparse, glob
from pathlib import Path
from typing import Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------- CONFIG ----------
LLM_UTILS_PATH    = "pipeline/llm_utils.py"
ENV_PATH          = "./.env"

TEST_PLAN_PATH    = "pipeline/checkpoints/claude_test_plan_20250730_140520.md"
TEST_KIT_ROOT     = "pipeline/checkpoints/gemini_8_13"

PROMPT_PATH       = "prompts/test_plan_coverage.txt"
DSL_GUIDANCE_PATH = "dsl-guidance.md"

OUT_DIR           = "./reports_plannet_test_plan"
CHK_DIR           = Path(OUT_DIR) / ".chk"   # per-batch checkpoint folder

API_TYPE          = "claude"
MAX_TOKENS        = 16000

# Batching 
MAX_CHARS_PER_BATCH = 120_000
MAX_FILES_PER_BATCH = 25
RAW_PREVIEW         = 800

# Concurrency + retries
MAX_WORKERS         = 3        # gentle concurrency
MAX_RETRIES         = 5
INITIAL_BACKOFF_S   = 2.0

# Optional subtree filter. Leave [] to scan entire tree dynamically.
INCLUDE_PATH_FILTER: List[str] = []
# -----------------------------

# Setup imports
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

# ------------------ Utilities ------------------

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

# --- Robust REQ detection (any digits, not just 3) ---
REQ_PATTERNS = [
    re.compile(r"REQ[-_\s]?(\d+)(?=\D|$)", re.IGNORECASE),
    re.compile(r"Requirement[-_\s]?(\d+)(?=\D|$)", re.IGNORECASE),
]

# Prefer explicit "req-####" in filenames, but allow any contiguous digits as cautious fallback.
FILENAME_PATTERNS = [
    re.compile(r"req[-_]?(\d+)(?=\D|$)", re.IGNORECASE),     # matches req_1003_test.rb
    re.compile(r"(?<!\d)(\d{3,6})(?!\d)", re.IGNORECASE),    # fallback: 3–6 digits (avoid sweeping long numbers)
]

def _norm_req(num: str) -> str:
    # keep full number; remove leading zeros; pad to 3 only if very short
    try:
        n = str(int(num))  # '0007' -> '7', '1003' -> '1003'
    except ValueError:
        n = re.sub(r"^0+", "", num) or "0"
    if len(n) < 3:
        n = n.zfill(3)    # '7' -> '007', '12' -> '012'
    return f"REQ-{n}"

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

# ------------------ Indexers (single pass) ------------------

def strip_ruby_comments_and_blank_lines(text: str) -> str:
    """Cheap token trim: drop lines that are empty or start with # (keeps semantics for matching)."""
    out = []
    for ln in (text or "").splitlines():
        s = ln.lstrip()
        if not s:           # blank
            continue
        if s.startswith("#"):
            continue
        out.append(ln)
    return "\n".join(out)

def build_file_index(rb_files: List[Path]) -> Dict[Path, Dict[str, str]]:
    """Read each Ruby file once; keep raw + trimmed + size for batching."""
    index: Dict[Path, Dict[str, str]] = {}
    for p in rb_files:
        try:
            raw = p.read_text(errors="ignore")
        except Exception:
            raw = ""
        trimmed = strip_ruby_comments_and_blank_lines(raw)
        index[p] = {
            "raw": raw,
            "trimmed": trimmed,
            "size": len(trimmed),
        }
    return index

def bucket_by_req_indexed(files: List[Path], file_index: Dict[Path, Dict[str, str]]) -> Dict[str, List[Path]]:
    """Bucket by REQ using cached content (no second file reads)."""
    buckets: Dict[str, List[Path]] = {}
    for p in files:
        body = file_index[p]["raw"]
        # Prefer filename, then body, then full path
        ids = (
            detect_req_ids_from_filename(p.name)
            or detect_req_ids_from_string(body)
            or detect_req_ids_from_string(str(p))
        )
        if not ids:
            ids = ["misc"]
        for rid in ids:
            buckets.setdefault(rid, []).append(p)
    return buckets

# ------------------ Plan excerpt extraction (anchor-based) ------------------

ANCHOR_RE = re.compile(r"<a id='req-(\d+)'>", re.IGNORECASE)

def build_plan_chunks(plan_md: str) -> Dict[str, str]:
    """
    Extract exact per-REQ sections from anchors of the form:
      <a id='req-1203'></a>
    Returns { 'REQ-1203': '...excerpt...' }
    """
    matches = list(ANCHOR_RE.finditer(plan_md))
    chunks: Dict[str, str] = {}
    for i, m in enumerate(matches):
        rid_num = m.group(1)  # keep full digits (supports 1000+)
        rid = _norm_req(rid_num)  # normalize to REQ-1003 / REQ-15678 etc.
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(plan_md)
        chunk = plan_md[start:end].strip()
        chunks[rid] = chunk
    return chunks

# ------------------ Batching ------------------

def chunk_paths_by_size(paths: List[Path], file_index: Dict[Path, Dict[str, str]]) -> List[List[Path]]:
    """Greedy chunking by char size and max files per batch using cached sizes."""
    batches: List[List[Path]] = []
    cur: List[Path] = []
    cur_size = 0
    for p in paths:
        sz = file_index[p]["size"]
        too_big = (cur and (cur_size + sz > MAX_CHARS_PER_BATCH)) or (len(cur) >= MAX_FILES_PER_BATCH)
        if too_big:
            batches.append(cur)
            cur, cur_size = [], 0
        cur.append(p)
        cur_size += sz
    if cur:
        batches.append(cur)
    return batches

def render_files_blob(batch: List[Path], file_index: Dict[Path, Dict[str, str]]) -> str:
    """Pretty blob with line numbers per file (trimmed content to save tokens)."""
    parts = []
    for p in batch:
        content = file_index[p]["trimmed"]
        numbered = "\n".join(f"{i+1:>5}  {ln}" for i, ln in enumerate(content.splitlines()))
        parts.append(f"### FILE: {p}\n```\n{numbered}\n```")
    return "\n".join(parts)

# ------------------ Checkpointing ------------------

def ckpath(req_id: str, bi: int) -> Path:
    CHK_DIR.mkdir(parents=True, exist_ok=True)
    return CHK_DIR / f"{req_id}__batch_{bi:03d}.json"

def load_checkpoint(req_id: str, bi: int) -> dict | None:
    p = ckpath(req_id, bi)
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            return None
    return None

def save_checkpoint(req_id: str, bi: int, data: dict) -> None:
    p = ckpath(req_id, bi)
    p.write_text(json.dumps(data, indent=2))

# ------------------ LLM call with retries ------------------

def call_llm_with_retry(prompt: str, sys_prompt: str, max_tokens: int) -> str:
    delay = INITIAL_BACKOFF_S
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return client.make_llm_request(
                api_type=API_TYPE,
                prompt=prompt,
                sys_prompt=sys_prompt,
                max_tokens=max_tokens,
            )
        except Exception as e:
            msg = str(e)
            retriable = any(token in msg for token in (" 529", " 429", "overload", "timeout", "5"))
            if attempt < MAX_RETRIES and retriable:
                time.sleep(delay + random.uniform(0, 0.5 * delay))  # jitter
                delay *= 1.7
                continue
            raise

# ------------------ Merge (same scoring) ------------------

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

# ------------------ Range selection helpers ------------------

def req_id_to_int(req_id: str) -> int:
    m = re.search(r"(\d+)", req_id)
    return int(m.group(1)) if m else -1

def parse_req_spec(spec: str) -> List[Tuple[int, int]]:
    """
    Parse strings like: "1-123,1000-1228, 77, REQ-200"
    into inclusive integer ranges: [(1,123), (1000,1228), (77,77), (200,200)]
    Tolerates reversed ranges (e.g., "1228-1000").
    """
    if not spec:
        return []
    out: List[Tuple[int, int]] = []
    for tok in spec.split(","):
        tok = tok.strip()
        if not tok:
            continue
        m = re.findall(r"\d+", tok)
        if not m:
            continue
        if len(m) == 1:
            n = int(m[0])
            out.append((n, n))
        else:
            a, b = int(m[0]), int(m[1])
            if a <= b:
                out.append((a, b))
            else:
                out.append((b, a))
    return out

def req_selected(req_id: str, ranges: List[Tuple[int, int]]) -> bool:
    if not ranges:
        return True  # no filter -> include all
    n = req_id_to_int(req_id)
    return any(a <= n <= b for (a, b) in ranges)

# ------------------ Worker ------------------

def make_user_prompt(req_id: str, bi: int, total_batches: int, files_md: str, plan_excerpt: str, prompt: str, dsl_md: str) -> str:
    return (
        f"{prompt.strip()}\n\n"
        f"## DSL GUIDANCE (markdown)\n{dsl_md}\n\n"
        f"## TEST PLAN (markdown)\n{plan_excerpt}\n\n"
        f"## RUBY TEST FILES (subset for {req_id}, batch {bi}/{total_batches})\n{files_md}\n"
    )

def worker(job: Tuple[str, int, int, List[Path]],
           plan_chunks: Dict[str, str],
           prompt: str,
           dsl_md: str,
           file_index: Dict[Path, Dict[str, str]]) -> Tuple[str, int, dict]:
    req_id, bi, total, batch = job

    # checkpoint check
    cached = load_checkpoint(req_id, bi)
    if cached is not None:
        return req_id, bi, cached

    files_md = render_files_blob(batch, file_index)
    plan_excerpt = plan_chunks.get(req_id, "")  # blank means "not found"
    user = make_user_prompt(req_id, bi, total, files_md, plan_excerpt, prompt, dsl_md)

    out = call_llm_with_retry(
        prompt=user,
        sys_prompt="You are precise and return only valid JSON.",
        max_tokens=MAX_TOKENS,
    )
    print(f"\n=== RAW OUTPUT ({req_id} batch {bi}/{total}) ===")
    print((out or "")[:RAW_PREVIEW])
    print("=== END RAW OUTPUT ===\n")

    data = _force_json(out)
    save_checkpoint(req_id, bi, data)
    return req_id, bi, data

# ------------------ CLI ------------------

def parse_args():
    ap = argparse.ArgumentParser(description="Test Plan Coverage (batched)")
    ap.add_argument(
        "--req",
        type=str,
        default="",
        help="Comma-separated REQ ranges/ids to process (e.g. '1-123,1000-1228,77,REQ-200'). "
             "If omitted, all REQs are processed."
    )
    ap.add_argument(
        "--redo",
        action="store_true",
        help="Re-run selected REQs even if checkpoints exist (deletes matching .chk files first)."
    )
    return ap.parse_args()

# ------------------ Main ------------------

def main():
    args = parse_args()

    start_time = time.time()

    # Load inputs
    plan_md = Path(TEST_PLAN_PATH).read_text()
    prompt  = Path(PROMPT_PATH).read_text()
    dsl_md  = Path(DSL_GUIDANCE_PATH).read_text() if Path(DSL_GUIDANCE_PATH).exists() else ""

    # Discover and index files (single pass)
    rb_files = find_ruby_files(TEST_KIT_ROOT)
    if not rb_files:
        print("No Ruby files found at:", TEST_KIT_ROOT)
        return
    file_index = build_file_index(rb_files)

    # Bucket by REQ using cached content
    buckets = bucket_by_req_indexed(rb_files, file_index)

    # Plan chunks (anchor-based, single pass)
    plan_chunks = build_plan_chunks(plan_md)

    # compute selection from --req
    ranges = parse_req_spec(args.req)

    # If --redo: delete checkpoints for selected REQs before we build jobs
    if args.redo:
        CHK_DIR.mkdir(parents=True, exist_ok=True)
        for rid in list(buckets.keys()):
            if rid == "misc":
                continue
            if req_selected(rid, ranges):
                pattern = str(CHK_DIR / f"{rid}__batch_*.json")
                for p in glob.glob(pattern):
                    try:
                        os.remove(p)
                    except Exception as e:
                        print(f"Warning: could not delete {p}: {e}")

    # Log bucket summary (filtered view)
    print("\n=== REQ Buckets Summary ===")
    for rid in sorted(buckets.keys(), key=req_id_to_int):
        if rid == "misc" or not req_selected(rid, ranges):
            continue
        sample = ", ".join([q.name for q in buckets[rid][:5]])
        more = "" if len(buckets[rid]) <= 5 else f" (+{len(buckets[rid]) - 5} more)"
        print(f"{rid}: {len(buckets[rid])} file(s) -> {sample}{more}")
    print("=== END REQ Buckets Summary ===\n")

    # Build a global job list of (req_id, bi, total_batches, batch_paths)
    jobs: List[Tuple[str, int, int, List[Path]]] = []
    for req_id, paths in sorted(buckets.items(), key=lambda kv: req_id_to_int(kv[0])):
        if req_id == "misc":
            continue
        if not req_selected(req_id, ranges):
            continue
        batches = chunk_paths_by_size(paths, file_index)
        total = len(batches)
        for bi, batch in enumerate(batches, start=1):
            jobs.append((req_id, bi, total, batch))

    # Run a small worker pool
    per_req_outputs: Dict[str, List[dict]] = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = [ex.submit(worker, j, plan_chunks, prompt, dsl_md, file_index) for j in jobs]
        for f in as_completed(futs):
            try:
                req_id, bi, data = f.result()
                per_req_outputs.setdefault(req_id, []).append(data)
            except Exception as e:
                print("ERROR in batch:", e)

    # Merge per-REQ
    results = []
    for req_id, batch_outputs in per_req_outputs.items():
        merged = merge_batches(batch_outputs)
        merged["req_id"] = req_id
        results.append(merged)

    # TPC overall
    tpcs = [r["scores"]["tpc"] for r in results if "scores" in r]
    tpc_overall = sum(tpcs) / len(tpcs) if tpcs else 0.0

    # Outputs
    out_dir = Path(OUT_DIR); out_dir.mkdir(parents=True, exist_ok=True)
    output = {
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

    elapsed = time.time() - start_time
    print(f"Reports written to {out_dir}")
    print(f"Total execution time: {elapsed:.2f} seconds ({elapsed/60:.1f} minutes)")

if __name__ == "__main__":
    main()
