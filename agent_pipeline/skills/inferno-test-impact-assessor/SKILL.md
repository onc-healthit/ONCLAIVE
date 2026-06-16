---
name: inferno-test-impact-assessor
description: "Use when Codex needs to review enriched IG change evidence and decide what an Inferno test kit should do next: add tests, revise existing tests, remove or relax tests, update fixtures, update metadata or requirement links, mark no test change needed, or flag manual review. Trigger for impact assessment, decision ledgers, test_update_decisions.yaml, implementation-ready work orders, or determining test-kit changes from an enriched ledger."
---

# Inferno Test Impact Assessor

## Purpose

Turn enriched IG-change evidence into implementation-ready test-kit update decisions. This skill creates the work order for the updater skill.

## Inputs

- Enriched change ledger YAML or JSONL with `relevance_assessment` when available
- Any supplemental evidence notes or source-search findings
- Optional baseline test kit repository path for targeted inspection

## Workflow

1. Load the enriched ledger and inspect each change with its `inventory_match` and `relevance_assessment`.
2. Treat `relevance_assessment.relevant_targets` as the evidence matcher's ranked judgment about which existing tests/files are actually relevant.
3. For each change, decide whether the test kit needs an update.
4. Use only these decision values:

```text
add_test
revise_existing_test
remove_or_relax_test
update_fixture
update_metadata_or_requirement_link
no_test_change_needed
manual_review_required
```

5. For every non-`no_test_change_needed` decision, identify likely files, target tests, expected behavior, and validation steps.
6. Preserve uncertainty. Use `manual_review_required` when relevance evidence is weak, contradictory, or absent.
7. Write an implementation-ready decision ledger. Do not edit code in this skill.

## Decision Quality Bar

The updater should be able to continue from the decision ledger without rediscovering the rationale. Include:

- Change ID and short IG-change summary
- Decision and confidence
- Existing coverage status
- Relevant targets from the evidence matcher
- Likely files/tests/fixtures to inspect or edit
- Required behavior after the update
- Evidence supporting the decision
- Implementation notes and validation plan

## Validation

- Confirm every change has exactly one decision.
- Confirm every actionable decision has at least one target or a clear discovery instruction.
- Confirm every decision cites evidence or explains why evidence is missing.
- Confirm no source files were modified.

## References

- Read `references/decision-ledger-contract.md` before producing the decision ledger.
