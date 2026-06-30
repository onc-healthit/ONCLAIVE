# Inferno Pattern Primer

Use this primer when interpreting existing Inferno test-kit code and inventories. It is intentionally limited to patterns
needed for impact assessment, not implementation.

## Evidence Ladder

Prefer stronger evidence before weaker evidence:

1. Explicit requirement-to-test mapping, if available.
2. `verifies_requirements` calls in source files.
3. Runnable inventory with test IDs, titles, descriptions, groups, and source files.
4. Code search over baseline tests using resource names, element paths, search parameters, terminology, old/new text, and
   conformance words.
5. Fixture and helper search, because coverage may live in shared logic rather than an obvious test file.
6. Generator-pattern inference from baseline generated tests and target IG artifacts.
7. Manual review when evidence is absent, weak, broad, contradictory, or process-oriented.

Requirement-to-test mappings are optional. Do not treat their absence as proof that there is no coverage.

## Core Inferno Concepts

- `Inferno::TestSuite`: top-level suite. It declares suite ID, IG metadata, FHIR validator configuration, inputs, clients,
  groups, and requirement sets.
- `Inferno::TestGroup`: ordered group of tests or child groups. Groups often represent a resource, workflow, or
  visual-inspection section.
- `Inferno::Test`: one executable or attestation unit. It has an `id`, `title`, `description`, inputs, optional
  `verifies_requirements`, and a `run` block.
- `id`: stable runnable ID. Use it when writing `matched_tests` or likely target tests.
- `test from:` and `group from:`: references to registered tests/groups. These show how tests are assembled into a suite.
- `run_as_group`: child tests share group execution semantics; this often matters for setup and skip behavior.
- `optional: true`: suite/group/test is not hard-required in the same way as mandatory executable checks.
- `input`: runtime user or system input. Attestation tests frequently use radio inputs and notes.
- `skip_if`: the test can skip when prerequisites or discoverable data are absent. Skips can be appropriate for data-driven
  searches where no example data is available.
- `assert`: pass/fail assertion. Use this to distinguish executable coverage from descriptive text.
- `assert_response_status`: common HTTP status assertion. A requirement changing allowed statuses usually maps here or nearby.
- `fhir_resource_validator`: suite-level validation setup, usually pointing at IG packages.
- `scratch`: shared storage across tests in a run. Search tests often populate resources for later validation or must-support
  tests.

## Common Test-Kit File Patterns

- Generated resource groups usually contain:
  - `*_group.rb` files that require child test files and register them with `test from:`.
  - `read_test.rb` for required read behavior.
  - `*_search_test.rb` for FHIR search parameter behavior.
  - `incl_*_search_test.rb` for `_include` behavior.
  - `validation_test.rb` for profile validation against the IG package.
  - `must_support_test.rb` for profile-derived Must Support element coverage.
  - `metadata.yml` describing profile URL, search definitions, must-support elements, references, and test IDs.
- Shared helpers usually contain the real reusable assertion behavior. Search, read, validation, must-support, date-search,
  and resource-navigation helpers should be considered likely edit locations when many generated tests share one behavior.
- Specs and fixtures validate the test kit itself. A decision should mention specs/fixtures when behavior changes need proof.
- Visual inspection and attestation groups are still coverage, but they are not the same as automated FHIR-response assertions.

## Baseline vs Target Inputs

Use baseline implementation files and baseline inventories as primary evidence for existing coverage. Do not inspect
target-version implementation files unless the user explicitly says they are an existing draft implementation to assess.
For migration planning, infer target work from:

- baseline test patterns,
- target IG structured artifacts,
- generator behavior,
- requirement/conformance evidence, and
- known custom-test or attestation conventions.

If target-version implementation files are available in the local repository but the task is a pre-target migration plan,
avoid using them as evidence.

## Coverage Interpretation

- A direct test ID, exact search parameter, exact element path, or exact requirement link is stronger than a resource-name match.
- A generated resource group match is often partial coverage, not proof that the specific changed assertion exists.
- A weak topical match, such as only `Patient` matching a privacy requirement, should not be treated as concrete coverage.
- A validation test may cover cardinality, binding, and invariant changes when the target IG package contains those constraints.
- A validation test usually does not cover narrative-only, workflow, legal, or operational requirements.
- Must Support tests usually cover presence across returned resources, not semantic correctness of values unless custom logic adds it.
- Search tests usually cover status, bundle validity, returned resource type, and parameter matching. They may not cover policy
  requirements beyond the search itself.

## Decision Hints

- Required, deterministic FHIR behavior with no existing coverage usually points to `add_test`.
- Existing automated behavior that now needs a different assertion points to `revise_existing_test`.
- Required behavior relaxed to SHOULD/MAY usually points to `remove_or_relax_test`.
- Example data, fixtures, terminology display examples, or generated metadata corrections often point to `update_fixture`.
- Requirement IDs, links, titles, descriptions, or requirement-set metadata often point to `update_metadata_or_requirement_link`.
- Guidance-only or optional behavior with no conformance effect often points to `no_test_change_needed`.
- Broad security, legal, privacy, operational, or external-framework requirements often require `manual_review_required` or an
  attestation decision.

