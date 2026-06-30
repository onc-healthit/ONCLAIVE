# Inferno Test Kit Updater Examples

These examples describe implementation patterns. Adapt them to the local test-kit style and the actual decision ledger.

## Revise Allowed Status Assertion

Decision: unauthorized requests may return 401, 403, or 404.

Implementation pattern:

- Locate the existing unauthorized request assertion or helper.
- Replace a single-status expectation with an allowed-status set.
- Add targeted spec cases for 401, 403, 404, and an invalid status.
- Preserve existing failure messages where possible.

Report shape:

```yaml
- change_id: c4bb-001
  decision: revise_existing_test
  status: implemented
  files_changed:
    - lib/example/security_test.rb
    - spec/example/security_test_spec.rb
  behavior_implemented:
    - Unauthorized response assertion now accepts 401, 403, or 404.
    - Added negative coverage for non-allowed status.
  deviations_from_plan: []
  follow_up: []
```

## Add Generated-Pattern Search Test

Decision: add required `service-start-date` EOB search.

Implementation pattern:

- Prefer generator inputs or metadata when the repo regenerates generated tests.
- If manually maintained, add a generated-style `service_start_date_search_test.rb`.
- Wire the test into the EOB group.
- Add or update metadata for the search parameter.
- Add targeted search spec coverage.

Validation:

```yaml
validation:
  commands:
    - command: bundle exec rspec spec/carin_for_blue_button/carin_search_test_spec.rb
      status: passed
  not_run: []
```

## Add Custom Semantic Test

Decision: transportation supportingInfo must be referenced by item.informationSequence.

Implementation pattern:

- Add a focused custom test rather than trying to make a generic generated must-support test understand the semantic rule.
- Use scratch resources already gathered by EOB searches.
- Skip if no relevant resources are available.
- Assert failure only when Transportation supportingInfo exists and no item references its sequence.
- Add positive and negative fixtures/specs.

## Update Fixture Only

Decision: correct APR-DEG typo to APR-DRG.

Implementation pattern:

- Search fixtures, metadata, descriptions, and specs for the old text.
- Update only stale examples or expected strings.
- Do not alter executable behavior unless validation now fails or passes incorrectly.
- Run affected fixture/spec tests.

## Add Attestation

Decision: audit/provenance recording needs coverage but is not directly observable.

Implementation pattern:

- Add an attestation test to the existing visual inspection/security group.
- Link the relevant requirement ID with `verifies_requirements`.
- Use a yes/no input and optional note, matching local attestation style.
- Register the test in the parent group.
- Add a suite load or group registration spec if the kit has one.

## Skip Manual Review

Decision: `manual_review_required` and no explicit user approval.

Implementation report:

```yaml
- change_id: security-privacy-001
  decision: manual_review_required
  status: skipped_manual_review
  files_changed: []
  behavior_implemented: []
  deviations_from_plan:
    - Manual-review decision was not implemented because no explicit approval was provided.
  follow_up:
    - Confirm whether this broad legal/security requirement should become attestation or metadata only.
```

