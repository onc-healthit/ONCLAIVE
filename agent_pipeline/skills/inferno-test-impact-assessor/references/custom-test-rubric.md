# Custom Test Rubric

Use this rubric to decide whether a change belongs in generated tests, custom tests, fixtures, metadata, no change, or manual
review.

## Generated vs Custom Decision

Generated tests are appropriate when the target IG artifact can drive the behavior through established generator patterns:

- resource group creation from profiles,
- read tests from CapabilityStatement interactions,
- search tests from SearchParameter or CapabilityStatement search expectations,
- `_include` tests from declared include expectations,
- validation tests from profile URLs and IG packages,
- Must Support tests from StructureDefinition metadata,
- metadata files generated from IG artifacts.

Custom tests are appropriate when the behavior needs hand-authored logic beyond normal generated patterns:

- cross-field relationships,
- conditional rules based on values,
- semantic checks not represented by profile validation,
- security or SMART-specific workflows,
- special error-status behavior,
- include-all semantics beyond basic include request construction,
- fixture-driven edge cases,
- visual inspection or attestation,
- requirement text that cannot be encoded in target IG artifacts.

## Decision Rubric

### Choose `add_test`

Use when a new conformance-relevant behavior is not covered by baseline tests and should be represented in the updated kit.

Strong indicators:

- New SHALL search parameter, include, interaction, operation, profile, invariant, or SMART behavior.
- New resource group or profile introduced by the target IG.
- Existing generator pattern can produce it from target IG artifacts.
- Existing custom-test pattern can be extended for a new semantic requirement.

Required ledger detail:

- baseline file evidence in `likely_files_to_edit` when available,
- expected generated/custom target file pattern in `target_output_hints` or a discovery instruction,
- target resource/profile/search parameter/requirement,
- expected pass/fail behavior,
- validation plan.

### Choose `revise_existing_test`

Use when baseline coverage exists but the assertion, accepted values, status handling, scope, or requirement text must change.

Strong indicators:

- Same resource/test exists in baseline.
- Conformance remains required, but details changed.
- Existing helper behavior is shared across many generated tests.

Examples:

- Accept 401, 403, or 404 instead of only 401.
- Change an expected code, element path, or relationship value.
- Adjust SMART scope list.

### Choose `remove_or_relax_test`

Use when target IG relaxes an old requirement and baseline tests would now be too strict.

Strong indicators:

- SHALL became SHOULD, MAY, optional, recommended, or guidance-only.
- Search support or resource support is no longer mandatory.
- Existing tests should become optional, skippable, warning-oriented, or removed from the mandatory group.

Do not use this for required behavior that merely moved to another element path; that is usually `revise_existing_test`.

### Choose `update_fixture`

Use when the code behavior is mostly correct but examples, fixture data, metadata examples, or spec fixtures need changes.

Strong indicators:

- Typo or example correction.
- New valid example form should be accepted.
- Existing negative fixture is no longer invalid.
- Terminology, code display, NDC format, Data Absent Reason, or profile example changed.

If the fixture change also requires a new assertion, choose `add_test` or `revise_existing_test` and list fixtures as likely
fixture edits.

### Choose `update_metadata_or_requirement_link`

Use when test behavior is unchanged but traceability or presentation must change.

Strong indicators:

- Requirement IDs changed.
- Requirement text, title, description, or source links changed.
- Suite metadata, docs, or requirement-set declarations need updating.
- Test already does the right thing but points at old IG material.

### Choose `no_test_change_needed`

Use when the change should not alter test-kit behavior.

Strong indicators:

- Guidance-only narrative with no conformance impact.
- MAY-level permission with no need for a new optional test.
- Background wording change that does not affect actor, suite, or workflow semantics.
- Target IG validation package will naturally accept the change without test-kit logic or fixture updates.

Always explain why no test behavior should change.

### Choose `manual_review_required`

Use when evidence is weak, missing, contradictory, too broad, or the correct implementation path requires human policy judgment.

Strong indicators:

- Legal, privacy, security, or external-framework requirement with unclear testability.
- Requirement-to-test mapping is absent and code search only finds topical matches.
- The change affects broad suite scope or actor interpretation.
- Existing generated and custom patterns point in different directions.
- The right answer depends on certification, policy, or project-specific conformance stance.

Manual review records must explain the missing evidence and provide a precise discovery instruction.

## Generator Inference Rules

Use generator inference only from baseline patterns and target IG artifacts. Do not use target-version implementation files
unless explicitly authorized as a draft implementation.

When documenting generator inference, keep baseline files in `likely_files_to_edit` and place expected target generated files
in `target_output_hints`. If no baseline file exists for a newly introduced resource or behavior, leave
`likely_files_to_edit` empty and provide a precise generator or target-output discovery instruction.

Assume the generator can probably handle:

- new profile validation tests,
- profile-derived Must Support lists,
- basic read tests,
- basic search parameter tests,
- basic include tests,
- metadata refreshes from profile and CapabilityStatement artifacts.

Assume custom work is probably needed for:

- moved semantics not captured as profile constraints,
- cross-field linkage rules,
- value-dependent requirements,
- "at least one referenced resource type" include-all assertions,
- broad SMART/security/privacy requirements,
- status-code policy changes not encoded in generated search/read helpers,
- attestations.

## Confidence Calibration

- High: exact runnable/test/helper match plus exact changed element, search parameter, status, scope, or requirement.
- Medium: resource/profile match and plausible local pattern, but exact assertion needs inspection.
- Low: topical match only, weak inventory score, broad narrative, or no code evidence.

When confidence is low and the change is conformance-relevant, prefer `manual_review_required` over inventing a precise edit.
