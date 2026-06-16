# Implementation Report Contract

Use this contract after applying a decision ledger to an Inferno test kit.

## Top-Level Shape

```yaml
meta:
  implementation_stage: implemented
  source_decision_ledger: path/to/test_update_decisions.yaml
  test_kit_repo: path/to/inferno-test-kit
  generated_at: YYYYMMDD_HHMMSS
results: []
validation:
  commands: []
  not_run: []
```

## Result Record

```yaml
- change_id: c4bb-001
  decision: revise_existing_test
  status: implemented
  files_changed:
    - lib/example.rb
  behavior_implemented:
    - Added assertion for new required element.
  deviations_from_plan: []
  follow_up: []
```

## Status Values

- `implemented`
- `partially_implemented`
- `not_implemented`
- `skipped_manual_review`

## Rules

- Tie every changed file to a decision ID.
- Record validation commands exactly as run.
- If validation cannot run, explain why and identify residual risk.
- Keep report factual; do not restate the entire ledger.
