# Attestation Policy

Use this policy to decide when an IG change should become automated Inferno behavior versus visual inspection or attestation.

## What Attestation Means

An attestation test is an Inferno test where the system operator confirms that an operational, legal, policy, or
implementation practice is satisfied. It commonly uses a radio input, optional notes, `verifies_requirements`, and an
assertion that the attestation answer is affirmative.

Attestation is valid coverage when the requirement is real but not reliably observable through a deterministic FHIR API
request during a test run.

## Prefer Automated Tests When

- The requirement can be verified by FHIR read, search, operation, validation, or SMART discovery responses.
- The test kit can construct a deterministic request and evaluate a deterministic response.
- The behavior is controlled by profile cardinality, terminology binding, invariants, search parameter declarations, or
  CapabilityStatement interaction requirements.
- Positive and negative fixtures can demonstrate the expected pass/fail behavior.
- The requirement is SHALL-level and failure can be detected without relying on out-of-band implementation knowledge.

Examples:

- A new required search parameter.
- A changed allowed HTTP response status.
- A required `_include` value.
- A required profile invariant.
- A required element path that profile validation or a custom assertion can inspect.

## Prefer Attestation When

- The requirement is legal, policy, privacy, organizational, or operational.
- The requirement concerns implementation process rather than API response shape.
- Verifying it would require access to infrastructure outside the FHIR endpoint, such as TLS stack configuration, audit logs,
  security controls, legal compliance evidence, or internal provenance recording.
- The requirement references broad external guidance and does not select one deterministic pass/fail criterion.
- A SHOULD-level recommendation is meaningful to collect but should not block conformance as an automated failure.

Examples:

- HIPAA or applicable-law compliance.
- TLS version policy when the harness cannot reliably inspect all deployed endpoints.
- Audit/provenance event recording when logs are not exposed to Inferno.
- Organizational privacy/security controls.
- Licensing attestations.

## Avoid Attestation When

- The requirement is directly testable by existing Inferno primitives.
- The attestation would duplicate an automated test and create conflicting results.
- The attestation wording turns MAY/SHOULD guidance into a hard SHALL-level failure.
- The attestation merely repeats broad IG narrative with no implementer action to confirm.

## Decision Mapping

- New deterministic SHALL behavior: usually `add_test`.
- Existing deterministic assertion needs changed behavior: usually `revise_existing_test`.
- Deterministic requirement relaxed from SHALL to SHOULD/MAY: usually `remove_or_relax_test`.
- Non-deterministic SHALL behavior that is still conformance-relevant: usually `add_test` with `update_type` set to an
  attestation-oriented value.
- Broad SHOULD-level guidance with unclear scope: often `manual_review_required`.
- Narrative-only guidance with no expected suite behavior: usually `no_test_change_needed`.

## Attestation Quality Bar

Good attestation work orders identify:

- exact requirement text or requirement IDs,
- why the requirement is not automated,
- the likely group where the attestation belongs,
- whether the attestation should be mandatory or optional,
- expected pass/fail wording,
- related automated tests, if any,
- validation steps such as suite load, group registration, and spec coverage for the input/pass/fail behavior.

## Confidence Guidance

- High confidence: the baseline kit already has a similar attestation pattern and the changed requirement clearly belongs there.
- Medium confidence: attestation is the likely path, but group placement or wording needs review.
- Low confidence: the requirement is broad, external, or mixed with testable subrequirements.

