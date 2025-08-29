#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questions about IG (CapabilityStatement → unresolved questions)
- Splits doc by headers
- Model chosen via API_TYPE and API_CONFIGS
"""
import sys, re, json, time
from pathlib import Path

# ---------- CONFIG ----------
LLM_UTILS_PATH = "llm_utils.py"
ENV_PATH       = "./.env"
IG_MD_PATH     = "us-core/test_set/CapabilityStatement-us-core-server2.md" #TODO: Dynamically update
PROMPT_PATH    = "prompts/IG_questions.txt" 
OUT_DIR        = "./reports"
API_TYPE       = "claude"
MAX_TOKENS     = 6000
# -----------------------------


# --- setup imports ---
sys.path.insert(0, str(Path(LLM_UTILS_PATH).parent))
try:
    import dotenv; dotenv.load_dotenv(ENV_PATH)
except Exception: 
    pass

from llm_utils import LLMApiClient, API_CONFIGS
client = LLMApiClient(config=API_CONFIGS)

# --- helpers ---
def _split_md_sections(md: str):
    parts, cur_title, buf = [], "Document Start", []
    for line in md.splitlines():
        if line.startswith("#"):
            if buf:
                parts.append((cur_title, "\n".join(buf))); buf = []
            cur_title = line.strip("# ").strip()
        else:
            buf.append(line)
    parts.append((cur_title, "\n".join(buf)))
    return parts

def _force_json(text: str):
    """Try to coerce Claude/GPT output into JSON."""
    if not text or not text.strip():
        raise ValueError("LLM returned empty response")
    try:
        return json.loads(text)
    except Exception:
        # salvage inner {...}
        m = re.search(r"\{.*\}", text, re.S)
        if m:
            return json.loads(m.group(0))
        raise

# --- main ---
def main():
    start_time = time.time()

    ig_md  = Path(IG_MD_PATH).read_text()
    prompt = Path(PROMPT_PATH).read_text()

    sections = _split_md_sections(ig_md)
    all_questions = []

    for title, body in sections:
        if not body.strip():
            continue

        user = f"{prompt.strip()}\n\n##SECTION: {title}\n{body}"
        out = client.make_llm_request(
            api_type=API_TYPE,
            prompt=user,
            sys_prompt="You are precise and return only valid JSON.",
            max_tokens=MAX_TOKENS,
        )

        # --- DEBUG: see what the model returned ---
        # print(f"\n=== RAW OUTPUT for section: {title} ===")
        # print(out)  # print first 1000 chars
        # print("=== END RAW OUTPUT ===\n")

        data = _force_json(out)
        all_questions.extend(data.get("questions", []))

    # Dedup by (summary, section)
    seen, uniq = set(), []
    for q in all_questions:
        key = (q.get("summary","").strip(), q.get("section","").strip())
        if key not in seen:
            uniq.append(q); seen.add(key)

    ig_file = Path(IG_MD_PATH).name 

    report = {
        "ig_source": ig_file,
        "question_count": len(uniq),
        "questions": uniq
    }

    out_dir = Path(OUT_DIR); out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "ig_questions.json").write_text(json.dumps(report, indent=2))

    lines = [f"# Questions about IG\n", f"Total: {len(uniq)}\n", "## Questions\n"]
    for q in uniq:
        lines.append(f"- **{q.get('id','')}** [{q.get('section','')}] {q.get('summary','')} "
                     f"(impact: {q.get('impact','')}, severity: {q.get('severity','')}, blocking: {q.get('blocking')})")
    (out_dir / "ig_questions.md").write_text("\n".join(lines))

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds ({elapsed_time/60:.1f} minutes)")

if __name__ == "__main__":
    main()