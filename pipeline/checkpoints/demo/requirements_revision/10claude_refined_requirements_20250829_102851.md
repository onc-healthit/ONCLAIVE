# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the US Core FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.

---
# REQ-001
**Summary**: US Core server shall support US Core Condition Encounter Diagnosis Profile
**Text**: "SHALL support: US Core Condition Encounter Diagnosis Profile"
**Context**: Within the CapabilityStatement for US Core Server, defining required profile support for Condition resources used for encounter diagnosis
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Supported Profiles
---

---
# REQ-002
**Summary**: US Core server shall support US Core Condition Problems and Health Concerns Profile
**Text**: "SHALL support: US Core Condition Problems and Health Concerns Profile"
**Context**: Within the CapabilityStatement for US Core Server, defining required profile support for Condition resources used for problems and health concerns
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Supported Profiles
---

---
# REQ-003
**Summary**: US Core server shall support search-type and read interactions for Condition
**Text**: "SHALL support `search-type`, `read`."
**Context**: Defining mandatory interaction capabilities for Condition resources in US Core Server CapabilityStatement
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Profile Interaction Summary
---

---
# REQ-004
**Summary**: US Core server should support vread and history-instance interactions for Condition
**Text**: "SHOULD support `vread`, `history-instance`."
**Context**: Defining recommended interaction capabilities for Condition resources in US Core Server CapabilityStatement
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Profile Interaction Summary
---

---
# REQ-005
**Summary**: US Core server shall be capable of returning Condition resource using GET by ID
**Text**: "A Server SHALL be capable of returning a Condition resource using: `GET [base]/Condition/[id]`"
**Context**: Defining fetch capability requirements for individual Condition resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Fetch and Search Criteria
---

---
# REQ-006
**Summary**: US Core server shall support Provenance revinclude for Condition searches
**Text**: "A Server SHALL be capable of supporting the following _revincludes: Provenance:target - `GET [base]/Condition?[parameter=value]&_revinclude=Provenance:target`"
**Context**: Defining required reverse include capability for retrieving Provenance resources that reference Condition resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Fetch and Search Criteria
---

---
# REQ-007
**Summary**: US Core server shall support patient search parameter for Condition
**Text**: "SHALL [patient] reference"
**Context**: Defining mandatory search parameter support for finding Condition resources by patient reference
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Summary
---

---
# REQ-008
**Summary**: US Core server shall support patient+category search parameter combination for Condition
**Text**: "SHALL [patient]+[category] reference+token"
**Context**: Defining mandatory search parameter combination for finding Condition resources by patient and category
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-009
**Summary**: US Core server should support patient+category+encounter search parameter combination for Condition
**Text**: "SHOULD [patient]+[category]+[encounter] reference+token+reference"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient, category, and encounter
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-010
**Summary**: US Core server should support patient+recorded-date search parameter combination for Condition
**Text**: "SHOULD [patient]+[recorded-date] reference+date"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient and recorded date
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---
