---
name: inferno-change-evidence-matcher
description: Use when coding agent needs to enrich a raw FHIR IG change ledger with candidate Inferno test-kit matches, deterministic inventory evidence, source-code search hits, optional Repobase findings, and a reconciled relevance assessment before any implementation decision is made. Trigger for inventory_change_enricher.py, change_ledger_enriched_*.yaml, candidate_tests, inventory_match, repobase_queries, relevance_assessment, or evidence gathering between IG changes and Inferno tests.
---

# Inferno Change Evidence Matcher

## Purpose

Gather and reconcile evidence about where each IG change may map into the baseline Inferno test kit. This skill decides which existing tests/files are relevant; it does not decide what test-kit update to make and does not edit code.

## Inputs

- Raw change ledger YAML
- Inferno inventory directory
- Baseline IG version and suite ID
- Target IG version
- Optional profile filters for focused generated-test matching
- Optional baseline test kit repository path for source search

Do not use target-version test-kit implementation files as matcher evidence during pre-target planning. If the user wants to
compare a generated candidate to the real target implementation, defer that to the updater/evaluation phase and treat the
target implementation as an oracle, not as evidence for matching.

## Workflow

1. Validate the raw ledger and inventory directory.
   Confirm the inventory and any source-search repository are for the baseline suite/version, not the future target suite.
2. Run deterministic inventory enrichment:

```bash
python3 ig_version_differences/inventory_change_enricher.py \
  <change_ledger_raw.yaml> \
  --inventory-dir <inventory_dir> \
  --output <change_ledger_enriched.yaml> \
  --jsonl-output <change_ledger_enriched.jsonl> \
  --baseline-ig-version <old_version> \
  --target-ig-version <new_version> \
  --baseline-suite-id <suite_id> \
  --inventory-label "<human readable inventory label>"
```

3. Add `--profile-filter <profile_id_or_url>` when the user wants candidates constrained to specific profiles.
4. Review `inventory_match.status`, `confidence`, `candidate_tests`, `candidate_coverage`, and `repobase_queries`.
5. For weak, broad, conflicting, or missing matches, search only the baseline test kit with `rg` and Repobase using resource
   names, profile IDs, element paths, requirement IDs, and generated `repobase_queries`.
   If the local repository also contains target-version implementation folders, restrict search paths to baseline files and
   shared helpers needed to interpret those baseline files.
6. Normalize structured inventory candidates and Repobase/code-search candidates by file path, runnable ID, requirement ID, profile, resource, and element path.
7. Reconcile the evidence:
   - Mark each candidate as `relevant`, `possibly_relevant`, or `not_relevant`.
   - Prefer candidates supported by both structured inventory and Repobase/code search.
   - Keep candidates with only one evidence source when the source directly matches the changed profile, resource, element path, requirement ID, or assertion behavior.
   - Reject candidates that only match broad resources, capability statements, shared helpers, or unrelated requirement text.
8. Write a `relevance_assessment` for each reviewed change with ranked relevant targets, rejected candidates, confidence, and rationale.
9. Preserve evidence in the enriched ledger or a separate evidence note rather than making implementation decisions in chat only.

## Evidence Rules

- Treat `candidate_tests` as places to inspect, not proof of coverage.
- Prefer source files and line references over broad conceptual claims.
- Distinguish deterministic inventory evidence from exploratory search evidence.
- Compare structured inventory and Repobase/code-search results before declaring a target relevant.
- A relevance decision can say an existing test/file is relevant, but it must not say whether to add, revise, remove, or relax a test.
- Mark gaps explicitly when no credible test-kit location is found.
- `source_file` entries in `inventory_match`, `relevance_assessment`, `evidence_notes`, and code-search findings must point to
  baseline files or shared helpers inspected because of baseline evidence.
- Do not cite target-version files, target generated output, or current target implementation behavior as evidence unless the
  user explicitly says the task is to assess an existing target draft.
- If target implementation files are present and needed later as the answer key, label them `evaluation_oracle` and do not use
  them until after the candidate update has been produced.

## Validation

- Confirm enriched YAML and JSONL outputs exist.
- Confirm `meta.ledger_stage: inventory_enriched_change_ledger`.
- Confirm the enriched ledger records its evidence scope as baseline-only unless explicitly assessing a target draft.
- Summarize counts by `inventory_match.status` and confidence.
- Summarize counts by relevance status when `relevance_assessment` is added.
- Confirm rejected candidates include reasons, not just omissions.
- Confirm no target-version implementation files appear in evidence fields during baseline-only planning.
- Do not edit the Inferno test kit.

## References

- Read `references/evidence-contract.md` when creating or reviewing evidence notes.
- Read `references/content-guide.md` before reconciling candidate evidence.
- Read `references/examples.md` when writing `relevance_assessment` records.
