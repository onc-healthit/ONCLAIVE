# Inferno Test Kit Updater Content Guide

This skill implements approved decision-ledger records in an Inferno test kit. It should make focused code changes and leave
a factual implementation report.

## Implementation Principles

- Implement only approved decisions.
- Do not implement `manual_review_required` decisions unless the user explicitly approves.
- Keep each changed file tied to one or more decision IDs.
- Prefer existing local patterns over new abstractions.
- Preserve Inferno DSL style, Ruby module/class naming, test IDs, and requirement-link conventions.
- Use the smallest change that satisfies expected behavior.
- Run targeted validation or explain why it could not run.

## Generated File Policy

Generated files may be source-controlled, but they still need care:

- If the repo normally regenerates generated files from IG packages, prefer updating generator inputs or documenting a
  regeneration step.
- If the repo manually maintains generated output, edit narrowly and preserve generated style.
- If a change is semantic or custom, avoid forcing it into many generated files when a shared helper or custom test is the
  local pattern.
- If generated output and custom groups both need updates, keep their responsibilities separate.

## Common Edit Locations

- Generated search/read/validation/must-support files for artifact-driven behavior.
- Shared helpers for behavior used by many generated tests.
- Custom groups for semantic, SMART, security, or workflow behavior.
- Visual inspection and attestation groups for non-deterministic requirements.
- Fixtures for positive and negative examples.
- Specs for test-kit behavior validation.
- Requirement metadata or docs for traceability-only updates.

## Validation Strategy

Prefer the narrowest meaningful validation:

1. Ruby syntax check for edited Ruby files.
2. Targeted specs for edited tests/helpers.
3. Suite load or registration check for group wiring.
4. Fixture validation specs when fixtures changed.
5. Broader suite command only when targeted tests are unavailable or insufficient.

Record commands exactly as run. If dependency or environment issues block validation, report the command, failure reason,
and residual risk.

## Report Expectations

The implementation report should say:

- which decision IDs were implemented,
- files changed,
- behavior implemented,
- deviations from the decision plan,
- validation commands and outcomes,
- follow-up or residual risk.

Do not restate the whole decision ledger. Keep the report factual and reviewable.

