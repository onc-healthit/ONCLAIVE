---
name: inferno-test-kit-updater
description: Use when Codex needs to implement approved Inferno test-kit changes from an impact decision ledger, including adding or revising tests, updating fixtures, updating requirement metadata, removing or relaxing obsolete assertions, and running targeted validation. Trigger for editing Inferno Ruby test-kit files based on test_update_decisions.yaml, implementation reports, or approved IG-change decisions.
---

# Inferno Test Kit Updater

## Purpose

Implement approved decisions in an Inferno test kit. This skill starts only after the impact assessor has produced an implementation-ready decision ledger.

## Inputs

- Impact decision ledger
- Inferno test kit repository path
- Optional enriched ledger for source evidence
- Target decision IDs or all actionable decisions

## Workflow

1. Confirm the branch, working tree status, target repository, and decision IDs.
2. Read the relevant decision records and inspect the referenced test files, fixtures, helpers, and metadata.
3. Make the smallest code changes that satisfy the decision:
   - Add tests only when existing groups cannot naturally cover the change.
   - Revise existing tests when the behavior belongs to an existing runnable.
   - Update fixtures only when required for the test behavior.
   - Preserve local Ruby style, Inferno DSL patterns, requirement IDs, and generated file conventions.
4. Run targeted validation for edited files where the test kit supports it.
5. Produce an implementation report that maps each decision ID to files changed, behavior implemented, validation run, and any deviations.

## Guardrails

- Do not implement changes for `manual_review_required` decisions unless the user explicitly approves.
- Do not broaden the update beyond the decision ledger without documenting why.
- Do not rewrite generated files unless the project pattern shows they are source-controlled and manually maintained.
- Do not remove tests solely because an inventory match was weak; require a decision ledger rationale.

## Validation

- Run syntax checks or targeted tests for edited Ruby files when available.
- If full tests are too expensive or unavailable, run the narrowest practical command and report the gap.
- Confirm every changed file is tied to a decision ID.
- Leave a concise implementation report for review.

## References

- Read `references/implementation-report-contract.md` before summarizing the update.
