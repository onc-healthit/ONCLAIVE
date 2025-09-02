#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Requirements Coverage script with preprocessing for large requirements files.
Now updated to process batches concurrently for faster runtime.
"""

import sys, re, json, time
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------- CONFIG ----------
LLM_UTILS_PATH = "pipeline/llm_utils.py"
ENV_PATH       = "./.env"
REQ_PATH       = "pipeline/checkpoints/claude_reqs_list_v2_20250730_122703.md"  #TODO: Dynamically update with appropriate file path
TEST_PLAN_PATH = "pipeline/checkpoints/claude_test_plan_20250730_140520.md"  #TODO: Dynamically update with appropriate file path
PROMPT_PATH    = "prompts/requirements_coverage.txt"
OUT_DIR        = "./reports"

API_TYPE       = "claude"
MAX_TOKENS     = 16000
BATCH_SIZE     = 10
RAW_PREVIEW    = 10

# Parallelism
MAX_WORKERS    = 3   # Safe concurrency level

# Preprocessing options
ENABLE_PREPROCESSING = True
# -----------------------------

sys.path.insert(0, str(Path(LLM_UTILS_PATH).parent))
try:
    import dotenv; dotenv.load_dotenv(ENV_PATH)
except Exception:
    pass

from llm_utils import LLMApiClient, API_CONFIGS

if API_TYPE in API_CONFIGS:
    cfg = dict(API_CONFIGS[API_TYPE])
    cfg["temperature"] = 0.2
    API_CONFIGS[API_TYPE] = cfg

client = LLMApiClient(config=API_CONFIGS)

# ------------------ HELPERS ------------------

def _extract_req_blocks(req_md: str):
    """Extract requirement blocks using the CORRECT pattern."""
    sections = re.split(r'^---\s*$', req_md, flags=re.MULTILINE)
    
    blocks = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        match = re.match(r'^#\s+(REQ-\d+)\s*\n(.*)', section, re.DOTALL)
        if match:
            req_id = match.group(1)
            content = match.group(2).strip()
            blocks.append((req_id, content))
    
    print(f"Extracted {len(blocks)} requirement blocks")
    return blocks


def _parse_toc_from_test_plan(test_plan_content):
    """Parse table of contents from test plan file to group requirements by resource."""
    if not ENABLE_PREPROCESSING:
        return {}
        
    toc_match = re.search(r'## Table of Contents\s*\n(.*?)## Test Specifications',
                          test_plan_content, re.DOTALL)
    if not toc_match:
        print("WARNING: Could not find TOC section in test plan")
        return {}
        
    toc_content = toc_match.group(1)
    resource_groups = defaultdict(list)
    current_resource = None
    
    for line in toc_content.split('\n'):
        line = line.strip()
        
        # Resource headings
        if line.startswith('- [') and not line.startswith('  - [') and 'REQ-' not in line:
            match = re.match(r'- \[([^\]]+)\]', line)
            if match:
                current_resource = match.group(1)
                
        # Requirement entries
        elif line.startswith('  - [') and 'REQ-' in line and current_resource:
            req_match = re.search(r'(REQ-\d+)', line)
            if req_match:
                req_id = req_match.group(1)
                resource_groups[current_resource].append(req_id)
                
    print(f"Parsed {len(resource_groups)} resource groups from TOC")
    return dict(resource_groups)


def _extract_test_chunks(test_plan_content):
    """Extract individual test specifications from test plan."""
    if not ENABLE_PREPROCESSING:
        return {}
        
    pattern = r"<a id='(req-\d+)'></a>(.*?)(?=<a id='req-\d+'|$)"
    matches = re.finditer(pattern, test_plan_content, re.DOTALL)
    
    test_chunks = {}
    for match in matches:
        req_id_raw = match.group(1)
        req_num = req_id_raw.split('-')[1]
        req_id = f'REQ-{req_num}'
        content = match.group(2).strip()
        
        if content.endswith('---'):
            content = content[:-3].strip()
            
        test_chunks[req_id] = content
        
    print(f"Extracted {len(test_chunks)} test specifications")
    return test_chunks


def _get_relevant_test_content(batch_req_ids, test_chunks):
    """Get only the test specifications relevant to the current batch."""
    if not ENABLE_PREPROCESSING or not test_chunks:
        return ""
        
    relevant_tests = []
    for req_id in batch_req_ids:
        if req_id in test_chunks:
            relevant_tests.append(f"<a id='{req_id.lower()}'></a>\n{test_chunks[req_id]}")
            
    return "\n\n---\n\n".join(relevant_tests)


def _force_json(text: str):
    """Try to coerce model output into JSON."""
    if not text or not text.strip():
        raise ValueError("LLM returned empty response")
    
    try:
        return json.loads(text)
    except Exception:
        patterns = [
            r'```json\s*(\{.*?\})\s*```',
            r'```\s*(\{.*?\})\s*```',
            r'(\{[^{}]*"details"[^{}]*\[.*?\]\s*\})'
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1))
                except:
                    continue
        
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except:
                pass
        
        raise ValueError(f"Could not extract valid JSON from response: {text[:500]}...")


# ------------------ BATCH PROCESSOR ------------------

def process_batch(i, batch, plan_md, prompt, test_chunks):
    batch_num = i // BATCH_SIZE + 1
    total_batches = (len(req_blocks) + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"\n=== Processing Batch {batch_num}/{total_batches} ===")
    
    batch_req_ids = [rid for rid, _ in batch]
    batch_md = "\n".join([f"--- # {rid}\n{content}\n---" for rid, content in batch])
    test_section = (_get_relevant_test_content(batch_req_ids, test_chunks)
                    if ENABLE_PREPROCESSING else plan_md)
    
    user_prompt = f"{prompt.strip()}\n\n## REQUIREMENTS (markdown)\n{batch_md}\n\n## TEST PLAN (markdown)\n{test_section}"
    out = client.make_llm_request(
        api_type=API_TYPE,
        prompt=user_prompt,
        sys_prompt=f"Analyze exactly {len(batch)} requirements ({', '.join(batch_req_ids)}). Return valid JSON with 'details' array containing {len(batch)} objects, one per requirement.",
        max_tokens=MAX_TOKENS,
    )
    
    print(f"Response preview: {(out or '')[:RAW_PREVIEW]}")
    data = _force_json(out)
    return data.get("details", [])


# ------------------ MAIN ------------------

def main():
    start_time = time.time()
    
    print("Reading input files.")
    req_md = Path(REQ_PATH).read_text()
    plan_md = Path(TEST_PLAN_PATH).read_text()
    prompt = Path(PROMPT_PATH).read_text()
    
    print("Extracting requirement blocks.")
    global req_blocks
    req_blocks = _extract_req_blocks(req_md)
    
    if ENABLE_PREPROCESSING:
        print("Preprocessing enabled - parsing TOC and test chunks.")
        resource_groups = _parse_toc_from_test_plan(plan_md)
        test_chunks = _extract_test_chunks(plan_md)
        print(f"Found {len(test_chunks)} test specifications")
    else:
        print("Preprocessing disabled - using original behavior")
        resource_groups = {}
        test_chunks = {}
    
    print(f"\nProcessing {len(req_blocks)} requirements in batches of {BATCH_SIZE}, using {MAX_WORKERS} workers.")
    
    all_details = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(process_batch, i, req_blocks[i:i+BATCH_SIZE], plan_md, prompt, test_chunks)
                   for i in range(0, len(req_blocks), BATCH_SIZE)]
        for f in as_completed(futures):
            try:
                all_details.extend(f.result())
            except Exception as e:
                print(f"ERROR in batch: {e}")
    
    # Final processing
    print(f"\n=== FINAL RESULTS ===")
    by_req = {d.get("req_id"): d for d in all_details if d.get("req_id")}
    
    print(f"Requirements extracted: {len(req_blocks)}")
    print(f"Requirements processed: {len(by_req)}")
    
    covered = sum(1 for d in by_req.values()
                  if d.get("facets") and all(f.get("covered", False) for f in d["facets"]))
    total = len(by_req)
    coverage_pct = covered / total if total else 0.0
    
    print(f"Coverage: {covered}/{total} = {coverage_pct*100:.1f}%")
    
    # Generate outputs
    report = {
        "requirements_total": total,
        "requirements_covered": covered,
        "coverage_pct": coverage_pct,
        "details": list(by_req.values()),
    }
    
    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    (out_dir / "requirements_coverage.json").write_text(json.dumps(report, indent=2))
    
    lines = [
        f"# Requirements Coverage\n",
        f"Coverage: {coverage_pct*100:.1f}%\n",
        "## Details\n"
    ]
    
    for rid in sorted(by_req.keys()):
        d = by_req[rid]
        score = d.get('score', 0.0)
        lines.append(f"### {rid} (score: {score})")
        for fct in d.get("facets", []):
            check = 'x' if fct.get('covered', False) else ' '
            name = fct.get('name', '')
            notes = fct.get('notes', '')
            lines.append(f"- [{check}] {name} — {notes}")
        lines.append("")
    
    (out_dir / "requirements_coverage.md").write_text("\n".join(lines))
    
    print(f"Reports written to {out_dir}")
    print(f"Total execution time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
