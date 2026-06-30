# Impact Assessor Content Guide

This skill turns evidence into an implementation-ready decision ledger. It should not edit the test kit.

## Decision Inputs

Use:

- raw IG change fields,
- conformance impact,
- `inventory_match`,
- `relevance_assessment` when available,
- baseline source search evidence,
- baseline generated/custom patterns,
- target IG structured artifacts if provided.

Avoid target-version implementation files unless the user explicitly says they are draft implementation to assess.

## Decision Ladder

Start with conformance and testability:

1. Is the change conformance-relevant?
2. Is it required, recommended, optional, guidance-only, or unknown?
3. Is there relevant existing baseline coverage?
4. Is the behavior deterministic and automatable?
5. Would the generator cover it from target IG artifacts?
6. Is custom logic, fixture work, metadata work, attestation, or manual review needed?

Then choose exactly one allowed decision.

## Coverage Status Interpretation

- `partially_covered`: existing baseline test is relevant but needs changed behavior or target regeneration.
- `not_covered`: no relevant baseline target found.
- `candidate_coverage_needs_review`: resource/profile match exists, but exact behavior is uncertain.
- `covered_by_attestation`: attestation exists or is clearly the expected mode.
- `no_matching_test_and_guidance_only`: no behavior change expected.
- `unknown`: evidence is too weak for a confident assessment.

Use clear status strings even when they are not from a fixed enum.

## Expected Behavior

Every actionable decision should state observable behavior after the update:

- what passes,
- what fails,
- what becomes optional or skippable,
- what fixture form is accepted,
- what requirement link or metadata changes,
- what manual review must discover.

Avoid vague summaries such as "update tests for this change."

## Generated vs Custom

If a target IG artifact can drive the behavior through the existing generator pattern, likely files may be expected generated
paths or generator discovery instructions. If the behavior is semantic, conditional, process-oriented, or attestation-based,
point to custom/helper/fixture locations or a precise discovery instruction.

Do not treat generated profile validation as proof of semantic narrative coverage unless the rule is encoded as cardinality,
binding, invariant, or other validator-visible constraint.

## Confidence

- High: exact changed behavior and target are clear.
- Medium: target is plausible but exact assertion path needs implementation inspection.
- Low: evidence is weak, broad, or policy-dependent.

When confidence is low and conformance impact is important, prefer `manual_review_required`.

