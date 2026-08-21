---
name: fhir-ig-change-ledger
description: Use when coding agent needs to compare two FHIR Implementation Guide versions, extract and clean IG narrative, identify requirement-level narrative changes, and convert the differences into a raw structured YAML change ledger. Trigger for tasks involving process_igs.py, compare_igs.py, difference_finder_v2.py, diff_to_change_ledger_v2.py, old/new IG zips or package URLs, differences_*.md, or change_ledger_raw_*.yaml.
---

# FHIR IG Change Ledger

## Purpose

Build the raw IG-change ledger. This skill owns the pipeline segment from old/new IG sources through cleaned narrative, narrative comparison, and raw structured YAML.

## Inputs

- Old IG zip or package URL
- New IG zip or package URL
- Artifact directory for the comparison
- LLM provider for comparison and ledger conversion
- Optional old requirements XLSX for comparison context
- Optional CARIN Blue Button mode with `--c4bb-ig`

## Workflow

1. Confirm the comparison pair, artifact directory, and extractor mode.
2. Extract, convert, and clean narrative:

```bash
python3 ig_version_differences/process_igs.py \
  <artifacts_dir> \
  -o <old_ig_zip_or_url> \
  -n <new_ig_zip_or_url> \
  --c4bb-ig \
  --verbose
```

3. Compare cleaned old/new narrative:

```bash
python3 ig_version_differences/compare_igs.py \
  <artifacts_dir> \
  -a gpt
```

Add `--reqs-xlsx <old_requirements.xlsx>` only when the user explicitly wants spreadsheet-assisted narrative comparison.

4. Convert the newest `ig/differences_*.md` into a raw ledger:

```bash
python3 ig_version_differences/diff_to_change_ledger_v2.py \
  --diff-file <artifacts_dir>/ig/differences_YYYYMMDD_HHMMSS.md \
  --provider openai
```

5. Report the raw ledger path and summarize total changes, skipped artifacts, and any obvious extraction or parsing warnings.

## Validation

- Confirm `ig/cleaned_markdown/old/` and `ig/cleaned_markdown/new/` exist and contain `.md` files.
- Confirm a non-empty `ig/differences_*.md` was produced.
- Confirm `change_ledger_raw_*.yaml` parses as YAML and has `meta.ledger_stage: raw_ig_change_ledger`.
- Confirm the raw ledger does not contain `inventory_match`, `candidate_tests`, or implementation decisions.

## References

- Read `references/raw-ledger-contract.md` when inspecting or validating raw ledger shape.
- Read `references/content-guide.md` before classifying IG changes.
- Read `references/examples.md` when you need examples of good raw ledger records.
