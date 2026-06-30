# Raw IG Change Ledger Examples

These examples show the level of detail expected in `change_ledger_raw_*.yaml`. They are illustrative, not a fixed schema
beyond the raw ledger contract.

## CapabilityStatement Search Parameter Addition

```yaml
- change_id: c4bb-capability-coverage-001
  source_artifact: CapabilityStatement-c4bb.md
  source_section: Coverage search support
  artifact_type: CapabilityStatement
  artifact_id: c4bb
  affected_resource: Coverage
  element_paths:
    - CapabilityStatement.rest.resource[Coverage].searchParam[_id]
  change_type: capability_statement_change
  old_conformance: read-only
  new_conformance: SHALL
  actor: Server
  scope: Coverage search
  planning_to_test: likely
  old_requirement_ids: []
  summary: Coverage search-type support and _id search are newly required.
  old_text: Coverage supported read only.
  new_text: Coverage SHALL support search-type and SHALL support _id search.
  test_action: add_required_assertion
  confidence: high
  source_of_truth_status: extracted
```

## StructureDefinition Semantic Rule

```yaml
- change_id: eob-related-001
  source_artifact: StructureDefinition-C4BB-ExplanationOfBenefit.md
  source_section: Related claims
  artifact_type: StructureDefinition
  artifact_id: C4BB-ExplanationOfBenefit
  affected_resource: ExplanationOfBenefit
  element_paths:
    - ExplanationOfBenefit.related.reference
    - ExplanationOfBenefit.related.relationship
  change_type: profile_structure_change
  old_conformance: SHOULD
  new_conformance: SHALL
  actor: Server
  scope: Adjusted claims
  planning_to_test: likely
  old_requirement_ids: []
  summary: Adjusted claims now have explicit related.reference and related.relationship requirements.
  old_text: Prior claim number should represent the most recent claim.
  new_text: Adjustment requests SHALL populate related.reference and relationship using prior or replacedby.
  test_action: add_required_assertion
  confidence: medium
  source_of_truth_status: extracted
```

## Terminology Or License Guidance

```yaml
- change_id: terminology-license-001
  source_artifact: Terminology_Licensure.md
  source_section: Code systems not requiring licenses
  artifact_type: CodeSystem
  artifact_id: ADA CDT
  affected_resource: unknown
  element_paths: []
  change_type: terminology_valueset_change
  old_conformance: guidance_only
  new_conformance: guidance_only
  actor: All
  scope: Terminology licensing
  planning_to_test: unknown
  old_requirement_ids: []
  summary: ADA CDT was added to the list of code systems that do not require separate license handling.
  old_text: ADA CDT was not listed.
  new_text: ADA CDT appears in the Code Systems Not Requiring Licenses list.
  test_action: update_suite_config
  confidence: medium
  source_of_truth_status: extracted
```

## Guidance-Only Narrative Change

```yaml
- change_id: background-001
  source_artifact: Background.md
  source_section: Consumer-directed exchange
  artifact_type: ImplementationGuidePage
  artifact_id: Background
  affected_resource: unknown
  element_paths: []
  change_type: guidance_change
  old_conformance: guidance_only
  new_conformance: guidance_only
  actor: unknown
  scope: Background narrative
  planning_to_test: unlikely
  old_requirement_ids: []
  summary: The background description of who may act for the consumer was revised.
  old_text: Consumer or individual authorized by a payer.
  new_text: Consumer or authorized personal representative.
  test_action: no_test_change_likely
  confidence: high
  source_of_truth_status: extracted
```

