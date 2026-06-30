---
name: inferno-test-kit-inventory
description: Use when Codex needs to scan an Inferno test kit repository and create searchable JSONL inventory files for suites, groups, tests, requirements, coverage rows, FHIR resources, profiles, search parameters, and source file locations. Trigger for inferno_inventory.py, runnables.jsonl, requirements.jsonl, coverage.jsonl, repos.jsonl, summary.json, or baseline suite inventory work.
---

# Inferno Test Kit Inventory

## Purpose

Build the deterministic baseline test-kit inventory used by later matching and impact-assessment skills.

## Inputs

- Inferno test kit repository path
- One or more baseline suite IDs
- Inventory output directory
- Optional suite hint overrides only when the default suite-to-path mapping is insufficient

## Workflow

1. Confirm the baseline repository and suite ID. Use the baseline suite, not the future target suite, when planning an update from an existing kit.
2. Generate inventory:

```bash
python3 pipeline/inferno_inventory.py \
  <inferno_test_kit_repo> \
  --suite-id <suite_id> \
  --output-dir <inventory_dir>
```

3. If multiple suite IDs are needed, repeat `--suite-id` or use comma-separated values if supported by the script version.
4. Reuse an existing inventory only when the repository commit, suite ID, and intended baseline version match the task.

## Outputs

The inventory directory must contain:

- `repos.jsonl`
- `runnables.jsonl`
- `requirements.jsonl`
- `coverage.jsonl`
- `summary.json`

## Validation

- Confirm all five output files exist.
- Read `summary.json` and report counts for runnables, requirements, and coverage rows.
- Inspect a few `runnables.jsonl` records when matching later depends on profile URLs, requirement IDs, or source file locations.
- Do not edit the test kit in this skill.

## References

- Read `references/inventory-contract.md` when validating inventory contents or explaining fields to another agent.
- Read `references/content-guide.md` before interpreting Inferno source structure.
- Read `references/examples.md` when reviewing sample inventory records.
