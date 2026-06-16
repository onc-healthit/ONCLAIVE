# Raw Change Ledger Contract

Use this contract for `change_ledger_raw_*.yaml`.

## Required Top-Level Shape

```yaml
meta:
  ledger_stage: raw_ig_change_ledger
  inventory_enriched: false
  provider: openai
  diff_file: path/to/differences_YYYYMMDD_HHMMSS.md
  total_changes_extracted: 0
  total_skipped: 0
changes: []
skipped: []
```

## Required Change Fields

Each item in `changes` should preserve enough IG context for later matching:

- `change_id`
- `source_artifact`
- `artifact_id`
- `artifact_type`
- `source_section`
- `affected_resource`
- `element_paths`
- `change_type`
- `old_text`
- `new_text`
- `summary`
- `old_conformance`
- `new_conformance`
- `actor`
- `scope`
- `planning_to_test`
- `old_requirement_ids`
- `test_action`
- `confidence`
- `source_of_truth_status`

## Rules

- Keep this ledger about the IG only.
- Do not include `inventory_match`, `candidate_tests`, `candidate_coverage`, decisions, or implementation notes.
- Use stable `change_id` values when rerunning from the same diff.
- Preserve exact old/new text when available; summarize only in `summary`.
