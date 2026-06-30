# Change Evidence Matcher Examples

These examples illustrate `relevance_assessment` patterns.

## Exact Search Parameter Match

```yaml
relevance_assessment:
  status: relevant_existing_test_found
  confidence: high
  summary: Existing EOB service-date search test is directly relevant to the changed EOB search behavior.
  relevant_targets:
    - source_file: lib/carin_for_blue_button_test_kit/generated/v1.1.0/eob/service_date_search_test.rb
      line: 5
      runnable_id: c4bb_v110_eob_service_date_search_test
      title: Server returns valid results for ExplanationOfBenefit search by service-date
      relevance: relevant
      evidence_sources:
        - structured_inventory
        - code_search
      why_relevant:
        - Matches affected resource ExplanationOfBenefit.
        - Matches exact search parameter service-date.
        - The test delegates to the shared search helper for executable search behavior.
  possible_targets: []
  rejected_candidates: []
  gaps: []
```

## Profile Match But Specific Assertion Unknown

```yaml
relevance_assessment:
  status: possible_existing_test_found
  confidence: medium
  summary: Existing Pharmacy EOB validation and Must Support tests match the profile, but no explicit 11-digit NDC assertion was found.
  relevant_targets: []
  possible_targets:
    - source_file: lib/carin_for_blue_button_test_kit/generated/v1.1.0/eob_pharmacy/validation_test.rb
      runnable_id: c4bb_v110_eob_pharmacy_validation_test
      relevance: possibly_relevant
      evidence_sources:
        - structured_inventory
      why_possibly_relevant:
        - Matches the changed Pharmacy EOB profile.
        - Profile validation may cover constraints if encoded in the IG package.
        - Code search did not find an explicit 11-digit NDC assertion.
  rejected_candidates: []
  gaps:
    - Need impact assessment to decide whether profile validation is enough or custom assertion/fixture work is needed.
```

## Broad Candidate Rejected

```yaml
relevance_assessment:
  status: no_relevant_existing_test_found
  confidence: medium
  summary: Candidate CapabilityStatement group is too broad for the changed unauthorized status-code requirement.
  relevant_targets: []
  possible_targets: []
  rejected_candidates:
    - source_file: lib/carin_for_blue_button_test_kit/capability_statement/capability_statement_group.rb
      runnable_id: capability_statement_group
      relevance: not_relevant
      why_rejected:
        - Broad capability-statement match only.
        - No code-search evidence for unauthorized status-code assertion.
        - No 401, 403, or 404 handling found in this file.
  gaps:
    - No baseline executable target was found for unauthorized request rejection status.
```

## Attestation Evidence

```yaml
relevance_assessment:
  status: relevant_existing_test_found
  confidence: high
  summary: Existing security attestation covers TLS and privacy controls.
  relevant_targets:
    - source_file: lib/carin_for_blue_button_test_kit/custom_groups/visual_inspection_and_attestation/v200_server/00_authorization_group/attestation_test_requirement_48.rb
      runnable_id: carin_server_requirement_48_57_attestation
      title: Secures data
      relevance: relevant
      evidence_sources:
        - code_search
      why_relevant:
        - Text names TLS and NIST SP 800-52.
        - Text names HIPAA privacy/security controls.
        - Uses verifies_requirements for related security requirements.
  possible_targets: []
  rejected_candidates: []
  gaps:
    - This is attestation coverage, not automated TLS probing.
```

