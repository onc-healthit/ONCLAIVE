# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Server SHALL support search-type and read interactions on InsurancePlan resource
**Requirement**: "A Server SHALL support search-type, read [on InsurancePlan resource]."
**Context**: This requirement mandates support for search-type and read operations on the InsurancePlan resource.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-002
**ID**: 02
**Summary**: Server SHOULD support vread interaction on InsurancePlan resource
**Requirement**: "A Server SHOULD support vread [on InsurancePlan resource]."
**Context**: This requirement recommends support for version-specific read operations on the InsurancePlan resource.
**Conformance**: "SHOULD"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-003
**ID**: 03
**Summary**: Server SHALL support returning InsurancePlan resource by id
**Requirement**: "A Server SHALL be capable of returning a InsurancePlan resource using: GET [base]/InsurancePlan/[id]"
**Context**: This requirement mandates the ability to retrieve a specific InsurancePlan resource by its logical id.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-004
**ID**: 04
**Summary**: Server SHOULD support returning InsurancePlan resource by version id
**Requirement**: "A Server SHOULD be capable of returning a InsurancePlan resource using: GET [base]/InsurancePlan/[id]/_history/vid"
**Context**: This requirement recommends the ability to retrieve a specific version of an InsurancePlan resource.
**Conformance**: "SHOULD"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-005
**ID**: 05
**Summary**: Server SHALL support _include for InsurancePlan resources
**Requirement**: "A Server SHALL be capable of supporting the following _includes: InsurancePlan:administered-by, InsurancePlan:owned-by, InsurancePlan:coverage-area"
**Context**: This requirement mandates support for including referenced Organization resources (administered-by, owned-by) and Location resources (coverage-area) when searching for InsurancePlan resources.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-006
**ID**: 06
**Summary**: Server SHALL support search parameters on InsurancePlan resource
**Requirement**: "A Server SHALL support the following search parameters on InsurancePlan: administered-by, owned-by, coverage-area, name, plan-type, identifier, _id, _lastUpdated, type"
**Context**: This requirement mandates support for searching InsurancePlan resources by administrative organization, owning organization, coverage area, plan name, plan type, identifier, id, last updated timestamp, and type.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---
