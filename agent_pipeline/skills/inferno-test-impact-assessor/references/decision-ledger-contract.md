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
    # Baseline test-kit files only. Do not put target-version implementation paths here
    # unless target implementation files were explicitly authorized as draft evidence.
    likely_files_to_edit:
      - lib/example.rb
    target_output_hints:
      - path_pattern: lib/generated/{target_version}/example.rb
        inference_basis: baseline versioned path plus generator output convention
        confidence: medium
    discovery_instructions: []
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
- Actionable decisions must include baseline likely edit locations, target output hints, or a precise discovery instruction.
- Manual-review decisions must explain what evidence is missing.
- Decisions must not contain code diffs.
- `required_update.likely_files_to_edit` must come from baseline inventory, baseline source search, or baseline file inspection.
- When target implementation files are not explicitly authorized, do not cite concrete target-version files as `code_search`
  evidence and do not place target-version paths in `likely_files_to_edit`.
- Expected target-version files may appear only in `target_output_hints` or `discovery_instructions`, and each target hint must
  state its inference basis.
