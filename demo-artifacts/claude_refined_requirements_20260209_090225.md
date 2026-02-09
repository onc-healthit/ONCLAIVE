# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Plan-Net Server SHALL support search-type and read interactions on InsurancePlan resource
**Requirement**: "A Server SHALL support search-type, read [on InsurancePlan resource]."
**Context**: This requirement mandates that the server must support the ability to search for InsurancePlan resources and read individual InsurancePlan resources by their logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-002
**ID**: 02
**Summary**: Plan-Net Server SHOULD support vread interaction on InsurancePlan resource
**Requirement**: "A Server SHOULD support vread [on InsurancePlan resource]."
**Context**: This requirement recommends that the server should support retrieving specific historical versions of an InsurancePlan resource using the version-aware read (vread) operation.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-003
**ID**: 03
**Summary**: Plan-Net Server SHALL support reading InsurancePlan resource by id
**Requirement**: "A Server SHALL be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]`"
**Context**: This requirement mandates that the server must support retrieving a specific InsurancePlan resource using its logical ID via a GET operation.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-004
**ID**: 04
**Summary**: Plan-Net Server SHOULD support vread on InsurancePlan resource by id and version
**Requirement**: "A Server SHOULD be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]/_history/vid`"
**Context**: This requirement recommends that the server should support retrieving a specific version of an InsurancePlan resource using its logical ID and version ID.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-005
**ID**: 05
**Summary**: Plan-Net Server SHALL support _include parameters for InsurancePlan resource
**Requirement**: "A Server SHALL be capable of supporting the following _includes: InsurancePlan:administered-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:administered-by`; InsurancePlan:owned-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:owned-by`; InsurancePlan:coverage-area - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:coverage-area`"
**Context**: This requirement mandates that the server must support including referenced Organization resources (administered-by, owned-by) and Location resources (coverage-area) when searching for InsurancePlan resources using the _include parameter.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---

---
# REQ-006
**ID**: 06
**Summary**: Plan-Net Server SHALL support search parameters on InsurancePlan resource
**Requirement**: "A Server SHALL support the following search parameters on InsurancePlan: administered-by, owned-by, coverage-area, name, plan-type, identifier, _id, _lastUpdated, type"
**Context**: This requirement mandates that the server must support searching for InsurancePlan resources using the specified reference parameters (administered-by, owned-by, coverage-area), string parameter (name), token parameters (plan-type, identifier, type), and standard parameters (_id, _lastUpdated).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: InsurancePlan
---
