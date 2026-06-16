# Impact Decision Ledger Contract

Use this contract for `test_update_decisions*.yaml`.

## Top-Level Shape

```yaml
meta:
  decision_stage: impact_assessed
  source_enriched_ledger: path/to/change_ledger_enriched.yaml
  generated_at: YYYYMMDD_HHMMSS
  assessor: codex
decisions: []
```

## Decision Record

```yaml
- change_id: c4bb-001
  decision: revise_existing_test
  priority: high
  confidence: medium
  ig_change_summary: Short requirement-level summary.
  existing_test_coverage:
    status: partially_covered
    relevant_targets:
      - source_file: lib/example.rb
        runnable_id: example_test_id
        relevance: relevant
        evidence_sources:
          - structured_inventory
          - repobase
    matched_files:
      - lib/example.rb
    matched_tests:
      - example_test_id
  required_update:
    summary: What must change in the test kit.
    update_type: assertion_change
    expected_behavior: The observable pass/fail behavior after the update.
    likely_files_to_edit:
      - lib/example.rb
    likely_fixtures_to_edit: []
  evidence:
    inventory_matches: []
    code_search: []
    gaps: []
  implementation_notes:
    - Preserve existing group structure.
  validation_plan:
    - Run the targeted test file or suite.
```

## Allowed Decisions

- `add_test`
- `revise_existing_test`
- `remove_or_relax_test`
- `update_fixture`
- `update_metadata_or_requirement_link`
- `no_test_change_needed`
- `manual_review_required`

## Quality Rules

- Every change receives one decision.
- Actionable decisions must include likely edit locations or a precise discovery instruction.
- Manual-review decisions must explain what evidence is missing.
- Decisions must not contain code diffs.
