# Inferno Inventory Content Guide

This skill builds the deterministic baseline inventory used by later matching and assessment stages. It should describe
what the existing baseline kit contains, not what the target kit should contain.

## Inventory Scope

Capture evidence from:

- suites,
- groups,
- tests,
- source files and line numbers,
- runnable IDs, titles, descriptions, and types,
- `verifies_requirements` calls,
- profile URLs and resource types,
- search parameters and include parameters,
- Must Support element lists,
- fixtures and fixture-like files when the inventory script supports them,
- shared helpers that provide common behavior.

## Runnable Taxonomy

Classify runnables by what they do:

- suite: top-level collection and requirement set.
- generated group: resource or profile group assembled from generated tests.
- generated search/read/validation/must-support test: repeatable behavior derived from IG artifacts.
- custom automated test: hand-authored assertion or workflow.
- attestation test: user-confirmed visual inspection or operational claim.
- setup or workflow test: launch, auth, initial wait, client simulation, or prerequisite flow.

This taxonomy helps later stages distinguish "test exists" from "the specific changed behavior is covered."

## Requirement Evidence

Requirement-to-test mappings may be absent. Collect the best available evidence in this order:

1. Explicit requirement files or coverage rows.
2. `verifies_requirements` strings in Ruby source.
3. Test titles and descriptions.
4. Resource/profile/search metadata.
5. Source file path and group placement.
6. Helper and fixture usage.

Do not treat missing `requirements.jsonl` or `coverage.jsonl` rows as proof that there is no coverage.

## Generated Patterns

Generated Inferno resource groups often contain:

- `*_group.rb`,
- `read_test.rb`,
- `*_search_test.rb`,
- `incl_*_search_test.rb`,
- `validation_test.rb`,
- `must_support_test.rb`,
- `metadata.yml`.

When inventorying generated tests, preserve the relationship between group files, child test files, and metadata. Later skills
need this to identify whether a change belongs in generated logic, shared helper logic, or custom code.

## Helper And Fixture Awareness

Coverage is not always in the runnable file itself:

- search behavior may live in a shared search helper,
- validation behavior may live in suite-level FHIR validator configuration,
- Must Support behavior may live in shared helper classes,
- special cases may live in custom helper modules,
- fixtures can encode positive and negative behavior even when no requirement ID is present.

If the inventory script cannot capture helper or fixture usage, call that out in the summary rather than overclaiming.

## Reuse Policy

Only reuse an existing inventory when repository identity, baseline suite ID, baseline version intent, and inventory script
behavior match the task. If any are uncertain, rebuild.

Never inventory a future target suite when the task is to plan a migration from a baseline suite, unless the user explicitly
asks to assess an existing target draft.

If target implementation files are available for later comparison, keep them outside the baseline inventory and label them as
an `evaluation_oracle`. The matcher and impact assessor should not consume oracle files as evidence.
