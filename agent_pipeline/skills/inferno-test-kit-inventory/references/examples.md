# Inferno Inventory Examples

These examples are illustrative JSONL-style records. Exact fields depend on the inventory script version, but the meaning
should stay stable.

## Generated Search Test Runnable

```json
{
  "id": "c4bb_v110_eob_service_date_search_test",
  "title": "Server returns valid results for ExplanationOfBenefit search by service-date",
  "runnable_type": "test",
  "suite_hint": "c4bb_v110",
  "source_file": "lib/carin_for_blue_button_test_kit/generated/v1.1.0/eob/service_date_search_test.rb",
  "line": 5,
  "requirement_ids": [],
  "resource_types": ["ExplanationOfBenefit"],
  "profile_urls": ["http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit"],
  "search_parameters": ["service-date"],
  "must_support_elements": []
}
```

## Generated Resource Group Runnable

```json
{
  "id": "c4bb_v110_eob",
  "title": "Explanation Of Benefit Tests",
  "runnable_type": "group",
  "suite_hint": "c4bb_v110",
  "source_file": "lib/carin_for_blue_button_test_kit/generated/v1.1.0/eob_group.rb",
  "line": 26,
  "requirement_ids": [],
  "resource_types": ["ExplanationOfBenefit"],
  "profile_urls": [],
  "search_parameters": ["_id", "patient", "_lastUpdated", "type", "identifier", "service-date"],
  "must_support_elements": []
}
```

## Attestation Runnable

```json
{
  "id": "carin_server_requirement_48_57_attestation",
  "title": "Secures data",
  "runnable_type": "test",
  "suite_hint": "c4bb_v200",
  "source_file": "lib/carin_for_blue_button_test_kit/custom_groups/visual_inspection_and_attestation/v200_server/00_authorization_group/attestation_test_requirement_48.rb",
  "line": 2,
  "requirement_ids": [
    "hl7.fhir.us.carin-bb_2.0.0@48",
    "hl7.fhir.us.carin-bb_2.0.0@57"
  ],
  "resource_types": [],
  "profile_urls": [],
  "search_parameters": [],
  "must_support_elements": []
}
```

## Coverage Row

```json
{
  "requirement_id": "hl7.fhir.us.carin-bb_2.0.0@60",
  "runnable_id": "c4bb_v200_smart_scopes",
  "source_file": "lib/carin_for_blue_button_test_kit/custom_groups/v2.0.0/c4bb_smart_launch/smart_scopes_test.rb",
  "coverage_type": "verifies_requirements",
  "note": "Traceability link from Inferno source."
}
```

## Summary Interpretation

```json
{
  "suite_ids": ["c4bb_v110"],
  "runnables": 96,
  "requirements": 0,
  "coverage": 0
}
```

Interpretation: the inventory can still support evidence matching through runnable metadata, but later stages should not
assume requirement-to-test mappings are available.

