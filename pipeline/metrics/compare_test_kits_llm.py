
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Repeatability checker: compare two generated versions of a FHIR Ruby test kit using an LLM.

Design mirrors your prior batch script:
- Top-of-file config (no CLI) for paths, API type, tokens, workers
- Uses llm_utils.LLMApiClient + API_CONFIGS exactly like your existing code
- Single-pass indexing of both versions; robust to differing folder layouts
- Pairing by requirement id with best-match fallback
- Minimal, efficient code (no extra bells & whistles)
- Per-REQ checkpoints (resumable), JSON + Markdown reports

Outputs:
  <OUT_DIR>/compare_report.json
  <OUT_DIR>/compare_report.md
  <OUT_DIR>/.chk/REQ_<id>.json
"""

from __future__ import annotations
import os, re, json, time, random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from collections import Counter

# --------------------------- CONFIG (edit here) ---------------------------

LLM_UTILS_PATH    = "pipeline/llm_utils.py"
ENV_PATH          = "./.env"

V1_ROOT           = "pipeline/checkpoints/gemini_8_13"
V2_ROOT           = "pipeline/checkpoints/gemini_7_30"

OUT_DIR           = "./reports_compare_kits_813_vs_730"
CHK_DIR           = Path(OUT_DIR) / ".chk"

API_TYPE          = "claude"     # must exist in your llm_utils.API_CONFIGS
MAX_TOKENS        = 16000        # like your other script

# Concurrency + retries (same shape as your prior script)
MAX_WORKERS         = 4
MAX_RETRIES         = 5
INITIAL_BACKOFF_S   = 2.0

# Optional requirement filter (use ranges like "1-19,77,100-120"; leave "" to compare all)
REQ_FILTER          = ""

# Cap payload size for each file passed to the LLM (keeps requests efficient)
MAX_CHARS_PER_FILE  = 120_000

# ------------------------------------------------------------------------

# Setup imports (same pattern as your previous script)
import sys
sys.path.insert(0, str(Path(LLM_UTILS_PATH).parent))
try:
    import dotenv; dotenv.load_dotenv(ENV_PATH)
except Exception:
    pass
from llm_utils import LLMApiClient, API_CONFIGS

# Force low temperature for repeatability (only for the selected API_TYPE)
if API_TYPE in API_CONFIGS:
    cfg = dict(API_CONFIGS[API_TYPE])
    cfg["temperature"] = 0.1
    API_CONFIGS[API_TYPE] = cfg

client = LLMApiClient(config=API_CONFIGS)

# --------------------------- Helpers ---------------------------

REQ_FILE_REGEX   = re.compile(r"req_(\d+)_test\.rb$", re.IGNORECASE)
REQ_INLINE_REGEX = re.compile(r"\bREQ[-_ ]?(\d+)\b", re.IGNORECASE)

@dataclass
class FileEntry:
    req_id: int
    path: Path
    relpath: str
    content: str

@dataclass
class VersionIndex:
    root: Path
    by_req: Dict[int, List[FileEntry]]
    all_files: List[FileEntry]

def read_text(p: Path, max_bytes: int = MAX_CHARS_PER_FILE) -> str:
    data = p.read_bytes()
    if len(data) > max_bytes:
        return data[:max_bytes].decode("utf-8", errors="ignore") + "\n# [TRUNCATED]\n"
    return data.decode("utf-8", errors="ignore")

def find_req_from_filename(p: Path) -> Optional[int]:
    m = REQ_FILE_REGEX.search(p.name)
    return int(m.group(1)) if m else None

def find_req_from_content(text: str) -> Optional[int]:
    m = REQ_INLINE_REGEX.search(text)
    return int(m.group(1)) if m else None

def shortpath(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root))
    except Exception:
        return str(p)

def index_version(root: Path) -> VersionIndex:
    root = root.resolve()
    by_req: Dict[int, List[FileEntry]] = {}
    all_entries: List[FileEntry] = []
    for p in root.rglob("*.rb"):
        text = read_text(p)
        rid = find_req_from_filename(p)
        if rid is None:
            rid = find_req_from_content(text)
        if rid is None:
            continue
        entry = FileEntry(req_id=rid, path=p, relpath=shortpath(p, root), content=text)
        all_entries.append(entry)
        by_req.setdefault(rid, []).append(entry)
    all_entries.sort(key=lambda e: (e.req_id, e.relpath))
    return VersionIndex(root=root, by_req=by_req, all_files=all_entries)

def tokens(s: str) -> List[str]:
    return re.findall(r"[A-Za-z0-9_/#:.]+", s)

def jaccard(a: List[str], b: List[str]) -> float:
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    u = len(sa | sb)
    return len(sa & sb) / u if u else 0.0

def heuristic_similarity(a: str, b: str) -> Dict[str, float]:
    ratio = SequenceMatcher(None, a, b).ratio()
    jac   = jaccard(tokens(a), tokens(b))
    return {"diff_ratio": ratio, "token_jaccard": jac}

def best_pair_for_req(rid: int, a: VersionIndex, b: VersionIndex) -> Optional[Tuple[FileEntry, FileEntry]]:
    la = a.by_req.get(rid, [])
    lb = b.by_req.get(rid, [])
    if not la or not lb:
        return None
    # prefer exact basename match
    for ea in la:
        for eb in lb:
            if ea.path.name == eb.path.name:
                return (ea, eb)
    # else choose by highest content similarity
    best = None
    best_score = -1.0
    for ea in la:
        for eb in lb:
            s = SequenceMatcher(None, ea.content, eb.content).ratio()
            if s > best_score:
                best = (ea, eb); best_score = s
    return best

# --------------------------- LLM ---------------------------

SYS_PROMPT = "You are precise and return only valid JSON."

def llm_user_prompt(req_id: int, path_a: str, path_b: str, code_a: str, code_b: str) -> str:
    return f"""
Compare the two Ruby test implementations for requirement REQ-{req_id}.
Judge SEMANTIC similarity of test scope and logic (FHIR profile/params, setup, assertions, errors, negative tests).
Return ONLY JSON using this schema:
{{
  "requirement_id": {req_id},
  "similarity_score": <float 0.0-1.0 (1.0 = functionally equivalent)>,
  "verdict": "<one of: same|minor_differences|moderate_differences|major_differences>",
  "coverage_risk": "<one of: low|medium|high>",
  "key_differences": ["<short bullet 1>", "<short bullet 2>"],
  "changed_checks_estimate": <int>,
  "added_removed_tests": <int>,
  "reasoning": "<1-3 concise sentences>"
}}

File A: {path_a}
```ruby
{code_a}
```

File B: {path_b}
```ruby
{code_b}
```""".strip()

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
            retriable = any(t in msg for t in (" 529", " 429", "overload", "timeout", "5"))
            if attempt < MAX_RETRIES and retriable:
                time.sleep(delay + random.uniform(0, 0.5 * delay))
                delay *= 1.7
                continue
            raise

def _force_json(text: str) -> dict:
    # strict first
    try:
        return json.loads(text)
    except Exception:
        pass
    # tolerant: first {} or [] block
    m = re.search(r"(\{.*\}|\[.*\])", text, re.DOTALL)
    if not m:
        raise ValueError("No JSON object found in model output")
    return json.loads(m.group(1))

# --------------------------- Checkpoints & Reports ---------------------------

def ckpath(req_id: int) -> Path:
    return CHK_DIR / f"REQ_{req_id}.json"

def save_checkpoint(req_id: int, data: dict) -> None:
    CHK_DIR.mkdir(parents=True, exist_ok=True)
    ckpath(req_id).write_text(json.dumps(data, indent=2), encoding="utf-8")

def load_checkpoint(req_id: int) -> Optional[dict]:
    p = ckpath(req_id)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return None
    return None

def summarize(results: List[dict]) -> dict:
    verdicts = Counter(r["final"]["verdict"] for r in results)
    sims = [r["final"]["similarity_score"] for r in results]
    avg = sum(sims) / len(sims) if sims else None
    high_risk = [r["requirement_id"] for r in results if (r.get("llm") or {}).get("coverage_risk") == "high"]
    return {
        "compared_requirements": len(results),
        "avg_similarity": round(avg, 4) if avg is not None else None,
        "verdict_counts": dict(verdicts),
        "high_risk_requirements": sorted(high_risk),
    }

def write_reports(meta: dict, results: List[dict]) -> None:
    out = {"meta": meta, "summary": summarize(results), "results": results}
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
    (Path(OUT_DIR) / "compare_report.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    s = []
    s.append("# Test Kit Repeatability Comparison")
    s.append(f"- Version 1 root: `{meta['v1_root']}`")
    s.append(f"- Version 2 root: `{meta['v2_root']}`")
    s.append(f"- API type: `{API_TYPE}`")
    s.append("")
    summ = out["summary"]
    s.append("## Summary")
    s.append(f"- Compared requirements: **{summ['compared_requirements']}**")
    s.append(f"- Average similarity: **{summ['avg_similarity']}**" if summ['avg_similarity'] is not None else "- Average similarity: _n/a_")
    s.append(f"- Verdict counts: `{json.dumps(summ['verdict_counts'])}`")
    s.append(f"- High-risk requirements: {', '.join('REQ-'+str(x) for x in summ['high_risk_requirements']) or 'none'}")
    s.append("")
    s.append("## Per-Requirement")
    s.append("| REQ | v1 file | v2 file | similarity | verdict | key differences |")
    s.append("|:---:|:--------|:--------|:----------:|:-------:|:----------------|")
    for r in sorted(results, key=lambda r: r["requirement_id"]):
        req = r["requirement_id"]
        v1  = r["file_v1"]
        v2  = r["file_v2"]
        sim = r["final"]["similarity_score"]
        ver = r["final"]["verdict"]
        dif = ", ".join((r.get("llm") or {}).get("key_differences", [])[:3])
        s.append(f"| REQ-{req} | `{v1}` | `{v2}` | {sim:.3f} | {ver} | {dif} |")

    (Path(OUT_DIR) / "compare_report.md").write_text("\n".join(s), encoding="utf-8")

# --------------------------- Range filter ---------------------------

def parse_req_filter(s: str) -> List[Tuple[int,int]]:
    s = (s or "").strip()
    if not s:
        return []
    out: List[Tuple[int,int]] = []
    for chunk in s.split(","):
        chunk = chunk.strip().upper().replace("REQ-","")
        if not chunk:
            continue
        if "-" in chunk:
            a,b = chunk.split("-",1)
            ai, bi = int(a), int(b)
            if ai <= bi:
                out.append((ai, bi))
            else:
                out.append((bi, ai))
        else:
            n = int(chunk)
            out.append((n, n))
    return out

def in_ranges(n: int, ranges: List[Tuple[int,int]]) -> bool:
    if not ranges:
        return True
    for a,b in ranges:
        if a <= n <= b:
            return True
    return False

# --------------------------- Worker ---------------------------

def compare_one(req_id: int, pair: Tuple[FileEntry,FileEntry]) -> dict:
    a, b = pair
    heur = heuristic_similarity(a.content, b.content)

    user = llm_user_prompt(req_id, a.relpath, b.relpath, a.content, b.content)
    out  = call_llm_with_retry(user, SYS_PROMPT, MAX_TOKENS)
    data = _force_json(out) if out else {}

    # Blend: trust LLM if it gave a numeric score; otherwise use heuristics average
    if isinstance(data, dict) and isinstance(data.get("similarity_score"), (int,float)):
        sim = float(data["similarity_score"])
        verdict = data.get("verdict", "unknown")
    else:
        sim = 0.5*heur["diff_ratio"] + 0.5*heur["token_jaccard"]
        verdict = "same" if sim>=0.95 else "minor_differences" if sim>=0.8 else "moderate_differences" if sim>=0.6 else "major_differences"

    payload = {
        "requirement_id": req_id,
        "file_v1": a.relpath,
        "file_v2": b.relpath,
        "heuristics": heur,
        "llm": data if isinstance(data, dict) else {"raw": (out or "")[:600]},
        "final": {"similarity_score": round(sim,4), "verdict": verdict},
    }
    save_checkpoint(req_id, payload)
    return payload

# --------------------------- Main ---------------------------

def main():
    root1 = Path(V1_ROOT)
    root2 = Path(V2_ROOT)
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
    CHK_DIR.mkdir(parents=True, exist_ok=True)

    v1 = index_version(root1)
    v2 = index_version(root2)

    req_ids = sorted(set(v1.by_req.keys()) | set(v2.by_req.keys()))
    ranges = parse_req_filter(REQ_FILTER)
    if ranges:
        req_ids = [r for r in req_ids if in_ranges(r, ranges)]

    work: List[Tuple[int,Tuple[FileEntry,FileEntry]]] = []
    for rid in req_ids:
        pair = best_pair_for_req(rid, v1, v2)
        if pair:
            work.append((rid, pair))

    results: List[dict] = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(compare_one, rid, pair): rid for (rid, pair) in work}
        for fut in as_completed(futs):
            rid = futs[fut]
            res = fut.result()
            results.append(res)

    meta = {
        "v1_root": str(v1.root),
        "v2_root": str(v2.root),
        "api_type": API_TYPE,
        "req_count_input": len(req_ids),
        "req_compared": len(results),
    }
    write_reports(meta, results)
    print(f"OK: wrote {Path(OUT_DIR)/'compare_report.json'} and {Path(OUT_DIR)/'compare_report.md'}")
    print(f"Checkpoints: {CHK_DIR}")

if __name__ == "__main__":
    main()
