# Change Evidence Contract

Use this contract when reviewing or augmenting `change_ledger_enriched_*.yaml`.

## Enriched Change Fields

Each enriched change should retain the raw change fields and add:

```yaml
old_requirement_full_ids: []
requirement_context: []
inventory_match:
  status: candidate_found_review_needed
  confidence: medium
  candidate_tests: []
  candidate_coverage: []
  repobase_queries: []
```

When structured inventory and Repobase/code search have been reviewed, add a reconciled relevance assessment:

```yaml
relevance_assessment:
  status: relevant_existing_test_found
  confidence: high
  summary: Existing EOB generated test appears relevant to the changed diagnosis type requirement.
  relevant_targets:
    - source_file: lib/carin_for_blue_button_test_kit/generated/v1.1.0/eob/eob_group.rb
      line: 42
      runnable_id: c4bb_v110_eob_must_support_test
      title: ExplanationOfBenefit must support test
      relevance: relevant
      evidence_sources:
        - structured_inventory
        - repobase
        - code_search
      why_relevant:
        - Matches affected resource ExplanationOfBenefit.
        - Matches profile C4BB-ExplanationOfBenefit-Inpatient-Institutional.
        - Code search found assertion near the changed element path.
  possible_targets: []
  rejected_candidates:
    - source_file: lib/carin_for_blue_button_test_kit/capability_statement/capability_statement_group.rb
      runnable_id: c4bb_v110_capability_statement
      relevance: not_relevant
      why_rejected:
        - Broad capability-statement match only.
        - No assertion or fixture related to the changed element.
  gaps:
    - No relevant target currently checks the new conformance behavior.
```

Optional fields for source notes:

```yaml
evidence_notes:
  code_search:
    - query: "ExplanationOfBenefit diagnosis type"
      files:
        - path: lib/example.rb
          line: 42
          note: Existing assertion checks same profile area.
  repobase:
    - query: "..."
      note: "..."
  gaps:
    - No candidate test checks the new element path.
```

## Relevance Status Values

- `relevant_existing_test_found`: at least one existing test/file is relevant enough for impact assessment.
- `possible_existing_test_found`: evidence suggests a target, but confidence is not high enough to treat it as definitive.
- `no_relevant_existing_test_found`: searched candidates do not appear relevant.
- `manual_relevance_review_required`: evidence is contradictory or insufficient.

## Candidate Relevance Values

- `relevant`: direct match to the changed requirement, profile, resource, element, assertion, fixture, or requirement ID.
- `possibly_relevant`: plausible but not yet proven; impact assessor should be cautious.
- `not_relevant`: rejected after comparison with the IG change and search evidence.

## Status Meanings

- `strong_candidate_found`: deterministic inventory strongly points to likely test coverage.
- `candidate_found_review_needed`: candidate exists, but code inspection is required.
- `weak_candidate_found`: weak candidate; search manually before assessment.
- `no_candidate_found`: no deterministic candidate; use code search or mark gap.
- `manual_review`: enriched data is insufficient for automated interpretation.

## Evidence Rules

- Keep evidence factual and source-linked.
- Reconcile structured inventory candidates with Repobase/code-search findings before ranking targets.
- Preserve rejected candidates when they are plausible enough that another reviewer might ask about them.
- Use `relevance_assessment` to decide what existing tests/files are relevant.
- Do not decide `add_test` or `revise_existing_test` here.
- Do not edit the test kit.
