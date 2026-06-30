# Raw IG Change Ledger Content Guide

This skill produces an IG-only change ledger. It should describe what changed in the Implementation Guide without deciding
which Inferno tests to update.

## What To Capture

For every requirement-level change, capture:

- the changed artifact and section,
- the artifact type, such as CapabilityStatement, StructureDefinition, SearchParameter, ValueSet, CodeSystem, or narrative page,
- affected resource and element paths when known,
- old and new conformance language,
- old and new requirement IDs when available,
- actor and scope when stated,
- exact old/new evidence text when available,
- a short summary,
- a provisional `test_action` that describes likely test relevance without naming files.

## Artifact Interpretation

- CapabilityStatement changes often affect interactions, search parameters, `_include` support, required resources, SMART
  discovery, or allowed response behavior.
- StructureDefinition changes often affect validation, cardinality, slicing, bindings, invariants, Must Support, examples,
  and element-level semantics.
- SearchParameter changes often affect generated search tests or include tests.
- ValueSet and CodeSystem changes often affect terminology validation, fixtures, binding expectations, or license/configuration
  notes.
- Narrative pages can contain real conformance requirements, but also contain background and guidance. Keep their conformance
  strength explicit.

## Conformance Normalization

Normalize conformance using the strongest directly supported wording:

- `SHALL`, `MUST`, required cardinality, required binding, or required invariant: required.
- `SHOULD`, recommended, best practice: recommended.
- `MAY`, optional, permitted: optional.
- Background or descriptive text without testable obligation: guidance-only.
- Removed text with unclear replacement: unknown until later review.

Do not upgrade MAY/SHOULD/guidance-only text to required. Do not downgrade explicit SHALL text just because it appears in a
narrative page.

## Change Type Hints

Use consistent change types so later skills can match and assess evidence:

- `capability_statement_change`: interactions, search support, scopes, includes, response statuses, or server behavior.
- `profile_structure_change`: StructureDefinition cardinality, slicing, invariants, Must Support, or element semantics.
- `terminology_valueset_change`: ValueSet, CodeSystem, binding, code, display, or license-related terminology updates.
- `search_parameter_change`: added, removed, or changed SearchParameter or `_include` support.
- `security_privacy_change`: SMART, OAuth, TLS, audit, privacy, legal, or authorization requirements.
- `guidance_change`: background or narrative guidance that may not directly affect tests.

## Test Action Hints

`test_action` is a planning hint, not a decision. Use broad values such as:

- `add_required_assertion`
- `update_fixture_or_assertion`
- `delete_or_make_optional`
- `author_new_test`
- `update_suite_config`
- `update_preconditions`
- `manual_review`
- `no_test_change_likely`

Do not include concrete file paths or final decisions in the raw ledger.

## Noise Filtering

Skip or mark low confidence when the diff is only:

- generated table formatting,
- navigation, footer, publication, or copyright boilerplate,
- whitespace or punctuation with no requirement change,
- repeated text already captured in a more specific artifact,
- broken markdown extraction without reliable old/new context.

If a repeated change appears in multiple artifacts, prefer the artifact closest to the requirement source.

## Quality Bar

A good raw record lets later skills search for test evidence without rereading the full IG diff. It preserves enough source
text to support or correct downstream judgments.

