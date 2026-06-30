# Impact Decision Examples

These examples illustrate decision selection and level of detail. Keep real ledgers grounded in actual evidence.

## Add Required Search Test

```yaml
- change_id: searchparameters-001
  decision: add_test
  priority: high
  confidence: high
  ig_change_summary: Servers must support ExplanationOfBenefit service-start-date search.
  existing_test_coverage:
    status: not_covered
    relevant_targets: []
    matched_files: []
    matched_tests: []
  required_update:
    summary: Add generated or generator-backed service-start-date search coverage.
    update_type: new_search_test
    expected_behavior: The suite sends service-start-date searches and fails unsupported or invalid responses.
    likely_files_to_edit:
      - DISCOVERY: generator output for target ExplanationOfBenefit service-start-date search test.
    likely_fixtures_to_edit: []
```

## Revise Existing Assertion

```yaml
- change_id: c4bb-001
  decision: revise_existing_test
  priority: high
  confidence: medium
  ig_change_summary: Unauthorized requests may return 401, 403, or 404 instead of only 401.
  existing_test_coverage:
    status: candidate_coverage_needs_review
    relevant_targets:
      - source_file: lib/example/security_test.rb
        runnable_id: c4bb_security_test
        relevance: possibly_relevant
        evidence_sources:
          - code_search
    matched_files:
      - lib/example/security_test.rb
    matched_tests:
      - c4bb_security_test
  required_update:
    summary: Broaden allowed unauthorized response statuses.
    update_type: assertion_change
    expected_behavior: 401, 403, and 404 pass; other statuses fail.
    likely_files_to_edit:
      - lib/example/security_test.rb
    likely_fixtures_to_edit: []
```

## Remove Or Relax Test

```yaml
- change_id: c4bb-organization-001
  decision: remove_or_relax_test
  priority: medium
  confidence: medium
  ig_change_summary: Organization search support changed from required to optional.
  required_update:
    summary: Make Organization search support optional or skippable while preserving required read behavior.
    update_type: optionalization
    expected_behavior: Missing Organization search support does not fail conformance; read behavior remains tested.
    likely_files_to_edit:
      - lib/generated/v1.1.0/organization_group.rb
    likely_fixtures_to_edit: []
```

## Update Fixture

```yaml
- change_id: terminology-example-001
  decision: update_fixture
  priority: medium
  confidence: medium
  ig_change_summary: Example DRG display text changed from APR-DEG to APR-DRG.
  required_update:
    summary: Correct fixtures and example metadata that use the old display.
    update_type: fixture_metadata_text_change
    expected_behavior: Tests no longer reference APR-DEG and fixtures validate with APR-DRG.
    likely_files_to_edit:
      - lib/generated/v1.1.0/eob_inpatient_institutional/metadata.yml
    likely_fixtures_to_edit:
      - spec/fixtures
```

## Manual Review

```yaml
- change_id: security-privacy-001
  decision: manual_review_required
  priority: medium
  confidence: low
  ig_change_summary: Implementations must comply with privacy and security controls required by applicable law.
  required_update:
    summary: Determine whether this broad legal requirement should be represented as attestation, metadata, or no test change.
    update_type: scope_review
    expected_behavior: The suite does not claim automated legal compliance without a defined testable criterion.
    likely_files_to_edit:
      - DISCOVERY: inspect visual inspection and attestation security group.
    likely_fixtures_to_edit: []
```

## No Test Change Needed

```yaml
- change_id: background-001
  decision: no_test_change_needed
  priority: low
  confidence: high
  ig_change_summary: Background narrative wording changed without a conformance requirement.
  required_update:
    summary: No Inferno behavior should change.
    update_type: none
    expected_behavior: Suite behavior remains unchanged.
    likely_files_to_edit: []
    likely_fixtures_to_edit: []
```

