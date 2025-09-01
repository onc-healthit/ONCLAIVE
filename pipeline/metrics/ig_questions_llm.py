#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IG Questions extractor at scale (batched):
- Batches multiple markdown files per LLM call to reduce API calls.
- Falls back to splitting a single large file across chunks only when needed.
- Retries on 429/529 "overloaded" with exponential backoff + jitter.
"""

import sys, re, json, os, time, random
from pathlib import Path
from typing import List, Dict, Tuple

# ---------- CONFIG ----------
LLM_UTILS_PATH = "pipeline/llm_utils.py"
ENV_PATH       = "./.env"
IG_MD_DIR      = "pipeline/checkpoints/markdown2_site"
PROMPT_PATH    = "prompts/ig_questions_new.txt"
OUT_DIR        = "./reports"

API_TYPE       = "claude"
MAX_TOKENS     = 6000

# Batching (tune as needed)
MAX_CHARS_PER_CALL = 120_000   # approximate cap for total text sent per call (prompt + batch)
MAX_FILES_PER_CALL = 25        # safety cap for number of files per batch
SINGLE_FILE_CHUNK  = 100_000   # if one file exceeds this, split it by sections

# Backoff on overload/rate-limit
MAX_RETRIES        = 6
BASE_BACKOFF_SEC   = 2.0
JITTER_SEC         = (0.2, 0.8)
SLEEP_BETWEEN_CALLS= 0.4
RAW_PREVIEW        = 800
# -----------------------------

# --- setup imports ---
sys.path.insert(0, str(Path(LLM_UTILS_PATH).parent))
try:
    import dotenv; dotenv.load_dotenv(ENV_PATH)
except Exception:
    pass

from llm_utils import LLMApiClient, API_CONFIGS

# Make runs steadier
if API_TYPE in API_CONFIGS:
    cfg = dict(API_CONFIGS[API_TYPE])
    cfg["temperature"] = 0.0
    cfg["top_p"] = 1.0
    API_CONFIGS[API_TYPE] = cfg

client = LLMApiClient(config=API_CONFIGS)

# --- helpers ---
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

def md_files(dir_path: Path) -> List[Path]:
    return sorted(dir_path.glob("*.md"), key=lambda p: p.name.lower())

def read_len(p: Path) -> Tuple[str, int]:
    s = p.read_text()
    return s, len(s)

def split_large_markdown(md: str, max_chars: int) -> List[str]:
    """Header-aware splitting for a single oversized file."""
    if len(md) <= max_chars:
        return [md]
    lines = md.splitlines(keepends=True)
    chunks, buf, size = [], [], 0

    def flush():
        nonlocal buf, size, chunks
        if buf:
            chunks.append("".join(buf)); buf, size = [], 0

    for ln in lines:
        # try to break at headers when we’re getting big
        if ln.lstrip().startswith("#") and size >= max_chars * 0.75:
            flush()
        buf.append(ln); size += len(ln)
        if size >= max_chars:
            flush()
    flush()
    return chunks

def pack_batches(files: List[Path]) -> List[List[Tuple[Path, str]]]:
    """
    Pack multiple files into as few batches as possible, under MAX_CHARS_PER_CALL.
    If a single file is huge, it is split into sub-chunks (treated as pseudo-files).
    Returns: list of batches; each batch is a list of (Path_or_pseudo, content) tuples.
    """
    batches: List[List[Tuple[Path, str]]] = []
    cur: List[Tuple[Path, str]] = []
    cur_size = 0

    for p in files:
        text, n = read_len(p)

        # if a single file is huge, split it into parts
        if n > SINGLE_FILE_CHUNK:
            parts = split_large_markdown(text, SINGLE_FILE_CHUNK)
            for idx, part in enumerate(parts, start=1):
                pseudo = Path(f"{p.name}#part{idx}")
                # flush if needed
                if cur and (cur_size + len(part) > MAX_CHARS_PER_CALL or len(cur) >= MAX_FILES_PER_CALL):
                    batches.append(cur); cur, cur_size = [], 0
                cur.append((pseudo, part)); cur_size += len(part)
        else:
            if cur and (cur_size + n > MAX_CHARS_PER_CALL or len(cur) >= MAX_FILES_PER_CALL):
                batches.append(cur); cur, cur_size = [], 0
            cur.append((p, text)); cur_size += n

    if cur:
        batches.append(cur)
    return batches

def render_batch_user_message(prompt: str, batch: List[Tuple[Path, str]]) -> str:
    parts = [prompt.strip()]
    for p, content in batch:
        # If it's a pseudo path (with #part), keep name as given
        name = p.name
        parts.append("==== FILE START ====")
        parts.append(f"FILENAME: {name}\n")
        parts.append(content.strip())
        parts.append("==== FILE END ====")
    return "\n\n".join(parts)

def _should_retry(exc: Exception) -> bool:
    s = f"{exc}".lower()
    return ("overload" in s or "overloaded" in s or "rate" in s and "limit" in s or "429" in s or "529" in s)

def llm_call_with_backoff(user_msg: str) -> str:
    attempt = 0
    while True:
        attempt += 1
        try:
            out = client.make_llm_request(
                api_type=API_TYPE,
                prompt=user_msg,
                sys_prompt="You are precise and return only valid JSON.",
                max_tokens=MAX_TOKENS,
            )
            # quick sanity parse
            _ = _force_json(out)
            time.sleep(SLEEP_BETWEEN_CALLS)
            return out
        except Exception as e:
            if attempt >= MAX_RETRIES or not _should_retry(e):
                raise
            back = (BASE_BACKOFF_SEC * (2 ** (attempt - 1))) + random.uniform(*JITTER_SEC)
            print(f"[Backoff] attempt {attempt}/{MAX_RETRIES} after error: {e}. Sleeping {back:.2f}s...")
            time.sleep(back)

def write_per_file_outputs(batch: List[Tuple[Path, str]], data: dict):
    """
    Save results per file. If a huge file was split (#partN), merge by base filename.
    """
    out_dir = Path(OUT_DIR); out_dir.mkdir(parents=True, exist_ok=True)

    # Normalize map from JSON
    json_files: Dict[str, dict] = {}
    for fobj in data.get("files", []):
        src = fobj.get("ig_source") or ""
        json_files[src] = fobj

    # Determine unique base names from batch (collapse #partN)
    base_names = {}
    for p, _ in batch:
        base = p.name.split("#part")[0]
        base_names.setdefault(base, []).append(p.name)

    for base, variants in base_names.items():
        # Collect questions across variants if model returned per-part names
        q_all = []
        count = 0
        found_any = False
        for v in variants:
            fobj = json_files.get(v) or json_files.get(base)
            if fobj:
                found_any = True
                q_all.extend(fobj.get("questions", []))
                count += fobj.get("question_count", 0)

        # If the model grouped them under base only, dedup the combined questions
        if found_any:
            # De-dup by (summary, section)
            seen, uniq = set(), []
            for q in q_all:
                key = (q.get("summary","").strip(), q.get("section","").strip())
                if key not in seen:
                    uniq.append(q); seen.add(key)

            report = {"ig_source": base, "question_count": len(uniq), "questions": uniq}
            (out_dir / f"{Path(base).stem}_ig_questions.json").write_text(json.dumps(report, indent=2))

            lines = [f"# Questions about IG ({base})\n",
                     f"Total: {len(uniq)}\n", "## Questions\n"]
            for q in uniq:
                lines.append(f"- **{q.get('id','')}** [{q.get('section','')}] {q.get('summary','')} "
                             f"(impact: {q.get('impact','')}, severity: {q.get('severity','')}, blocking: {q.get('blocking')})")
            (out_dir / f"{Path(base).stem}_ig_questions.md").write_text("\n".join(lines))
        else:
            # If the model omitted a file entirely, still write an empty report
            report = {"ig_source": base, "question_count": 0, "questions": []}
            (out_dir / f"{Path(base).stem}_ig_questions.json").write_text(json.dumps(report, indent=2))
            (out_dir / f"{Path(base).stem}_ig_questions.md").write_text(
                f"# Questions about IG ({base})\n\nTotal: 0\n\n## Questions\n"
            )

def main():
    prompt = Path(PROMPT_PATH).read_text()
    files = md_files(Path(IG_MD_DIR))
    if not files:
        print(f"No markdown files found in {IG_MD_DIR}")
        return

    print(f"Found {len(files)} markdown files to process")

    # 1) Pack many files into as few calls as possible
    batches = pack_batches(files)
    print(f"Planned {len(batches)} LLM calls (batched).")

    # 2) Process each batch
    for bi, batch in enumerate(batches, start=1):
        print(f"\n=== Calling LLM for batch {bi}/{len(batches)} ({len(batch)} files) ===")
        user_msg = render_batch_user_message(prompt, batch)

        try:
            out = llm_call_with_backoff(user_msg)
        except Exception as e:
            print(f"Batch {bi} failed: {e}")
            # As a fallback: try per-file within this batch to keep moving
            for (p, content) in batch:
                print(f"  ↳ Fallback single-file call: {p.name}")
                single_msg = render_batch_user_message(prompt, [(p, content)])
                try:
                    s_out = llm_call_with_backoff(single_msg)
                    data = _force_json(s_out)
                    write_per_file_outputs([(p, content)], data)
                except Exception as e2:
                    print(f"Failed on {p.name}: {e2}")
            continue

        print("=== RAW OUTPUT (preview) ===")
        print((out or "")[:RAW_PREVIEW])
        print("=== END RAW OUTPUT ===\n")

        data = _force_json(out)
        write_per_file_outputs(batch, data)

if __name__ == "__main__":
    main()
