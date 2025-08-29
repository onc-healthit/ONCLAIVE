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

---
# REQ-011
**Summary**: US Core server should support patient+_lastUpdated search parameter combination for Condition
**Text**: "SHOULD [patient]+[_lastUpdated] reference+date"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient and last updated timestamp
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-012
**Summary**: US Core server should support patient+category+clinical-status search parameter combination for Condition
**Text**: "SHOULD [patient]+[category]+[clinical-status] reference+token+token"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient, category, and clinical status
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-013
**Summary**: US Core server should support patient+onset-date search parameter combination for Condition
**Text**: "SHOULD [patient]+[onset-date] reference+date"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient and onset date
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-014
**Summary**: US Core server should support patient+code search parameter combination for Condition
**Text**: "SHOULD [patient]+[code] reference+token"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient and condition code
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-015
**Summary**: US Core server should support patient+clinical-status search parameter combination for Condition
**Text**: "SHOULD [patient]+[clinical-status] reference+token"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient and clinical status
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-016
**Summary**: US Core server should support patient+asserted-date search parameter combination for Condition
**Text**: "SHOULD [patient]+[asserted-date] reference+date"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient and asserted date
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-017
**Summary**: US Core server should support patient+abatement-date search parameter combination for Condition
**Text**: "SHOULD [patient]+[abatement-date] reference+date"
**Context**: Defining recommended search parameter combination for finding Condition resources by patient and abatement date
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Search Parameter Combination Summary
---

---
# REQ-018
**Summary**: Client shall provide abatement-date value precise to second plus time offset
**Text**: "A client SHALL provide a value precise to the *second + time offset*."
**Context**: Defining precision requirements for abatement-date search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (abatement-date)
---

---
# REQ-019
**Summary**: US Core server shall support abatement-date value precise to second plus time offset
**Text**: "A server SHALL support a value precise to the *second + time offset*."
**Context**: Defining precision requirements for abatement-date search parameter support by servers
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (abatement-date)
---

---
# REQ-020
**Summary**: Client shall provide asserted-date value precise to second plus time offset
**Text**: "A client SHALL provide a value precise to the *second + time offset*."
**Context**: Defining precision requirements for asserted-date search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (asserted-date)
---

---
# REQ-021
**Summary**: US Core server shall support asserted-date value precise to second plus time offset
**Text**: "A server SHALL support a value precise to the *second + time offset*."
**Context**: Defining precision requirements for asserted-date search parameter support by servers
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (asserted-date)
---

---
# REQ-022
**Summary**: Client shall provide at least code value for category search parameter
**Text**: "The client SHALL provide at least a code value and MAY provide both the system and code values."
**Context**: Defining format requirements for category search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (category)
---

---
# REQ-023
**Summary**: US Core server shall support both system and code values for category search parameter
**Text**: "The server SHALL support both."
**Context**: Defining support requirements for category search parameter by servers for both system and code values
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (category)
---

---
# REQ-024
**Summary**: Client shall provide at least code value for clinical-status search parameter
**Text**: "The client SHALL provide at least a code value and MAY provide both the system and code values."
**Context**: Defining format requirements for clinical-status search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (clinical-status)
---

---
# REQ-025
**Summary**: US Core server shall support both system and code values for clinical-status search parameter
**Text**: "The server SHALL support both."
**Context**: Defining support requirements for clinical-status search parameter by servers for both system and code values
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (clinical-status)
---

---
# REQ-026
**Summary**: Client shall provide at least code value for code search parameter
**Text**: "The client SHALL provide at least a code value and MAY provide both the system and code values."
**Context**: Defining format requirements for code search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (code)
---

---
# REQ-027
**Summary**: US Core server shall support both system and code values for code search parameter
**Text**: "The server SHALL support both."
**Context**: Defining support requirements for code search parameter by servers for both system and code values
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (code)
---

---
# REQ-028
**Summary**: Client shall provide at least id value for encounter search parameter
**Text**: "The client SHALL provide at least a id value and MAY provide both the Type and id values."
**Context**: Defining format requirements for encounter search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (encounter)
---

---
# REQ-029
**Summary**: US Core server shall support both Type and id values for encounter search parameter
**Text**: "The server SHALL support both."
**Context**: Defining support requirements for encounter search parameter by servers for both Type and id values
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (encounter)
---

---
# REQ-030
**Summary**: Client shall provide onset-date value precise to second plus time offset
**Text**: "A client SHALL provide a value precise to the *second + time offset*."
**Context**: Defining precision requirements for onset-date search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (onset-date)
---

---
# REQ-031
**Summary**: US Core server shall support onset-date value precise to second plus time offset
**Text**: "A server SHALL support a value precise to the *second + time offset*."
**Context**: Defining precision requirements for onset-date search parameter support by servers
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (onset-date)
---

---
# REQ-032
**Summary**: Client shall provide at least id value for patient search parameter
**Text**: "The client SHALL provide at least a id value and MAY provide both the Type and id values."
**Context**: Defining format requirements for patient search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (patient)
---

---
# REQ-033
**Summary**: US Core server shall support both Type and id values for patient search parameter
**Text**: "The server SHALL support both."
**Context**: Defining support requirements for patient search parameter by servers for both Type and id values
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (patient)
---

---
# REQ-034
**Summary**: Client shall provide recorded-date value precise to second plus time offset
**Text**: "A client SHALL provide a value precise to the *second + time offset*."
**Context**: Defining precision requirements for recorded-date search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (recorded-date)
---

---
# REQ-035
**Summary**: US Core server shall support recorded-date value precise to second plus time offset
**Text**: "A server SHALL support a value precise to the *second + time offset*."
**Context**: Defining precision requirements for recorded-date search parameter support by servers
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (recorded-date)
---

---
# REQ-036
**Summary**: US Core server shall document types of changes detectable using _lastUpdated parameter
**Text**: "A server SHALL document the types of changes that can be detected using this parameter."
**Context**: Defining documentation requirements for _lastUpdated search parameter capabilities
**Verification**: Inspection
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (_lastUpdated)
---

---
# REQ-037
**Summary**: Client shall provide _lastUpdated value precise to second plus time offset
**Text**: "A client SHALL provide a value precise to the *second + time offset*."
**Context**: Defining precision requirements for _lastUpdated search parameter when used by clients
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (_lastUpdated)
---

---
# REQ-038
**Summary**: US Core server shall support _lastUpdated value precise to second plus time offset
**Text**: "A server SHALL support a value precise to the *second + time offset*."
**Context**: Defining precision requirements for _lastUpdated search parameter support by servers
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Search Parameter Requirements (_lastUpdated)
---

---
# REQ-039
**Summary**: Server shall support recordedDate for Condition diagnosis date representation
**Text**: "A server SHALL support `Condition.recordedDate`."
**Context**: Defining mandatory support for recordedDate element as one of the date representations for condition diagnosis within problems and health concerns
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Resource Specific Documentation
---

---
# REQ-040
**Summary**: Server shall support at least one of assertedDate Extension or onsetDateTime for Condition
**Text**: "A server SHALL support at least one of the assertedDate Extension and `Condition.onsetDateTime`."
**Context**: Defining mandatory support requirement for date representation in addition to recordedDate for condition diagnosis within problems and health concerns
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Resource Specific Documentation
---

---
# REQ-041
**Summary**: Client application shall support all three date elements for Condition
**Text**: "The client application SHALL support all three elements."
**Context**: Defining client requirement to support assertedDate Extension, onsetDateTime, and recordedDate elements for condition diagnosis date representation
**Verification**: Test
**Actor**: Client Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition - Resource Specific Documentation
---

---
# REQ-042
**Summary**: Encounter should be referenced when Condition category is encounter-diagnosis
**Text**: "When `Condition.category` is \"encounter-diagnosis\" the encounter, SHOULD be referenced in `Condition.encounter`."
**Context**: Defining recommended practice for linking encounter diagnosis conditions to their associated encounters
**Verification**: Test
**Actor**: System creating Condition resources
**Conformance**: SHOULD
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Resource Specific Documentation
---

---
# REQ-043
**Summary**: Clinical status should be present when Condition category is problems-list-item
**Text**: "When `Condition.category` is a \"problems-list-item\", the `Condition.clinicalStatus` SHOULD be present."
**Context**: Defining recommended practice for including clinical status in problem list items within problems and health concerns conditions
**Verification**: Test
**Actor**: System creating Condition resources
**Conformance**: SHOULD
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Resource Specific Documentation
---

---
# REQ-044
**Summary**: Updates to meta.lastUpdated should reflect new problems and health concerns
**Text**: "Updates to `Condition.meta.lastUpdated` SHOULD reflect: New problems and health concerns"
**Context**: Defining recommended practice for updating lastUpdated timestamp when new problems and health concerns are created
**Verification**: Test
**Actor**: System managing Condition resources
**Conformance**: SHOULD
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Resource Specific Documentation
---

---
# REQ-045
**Summary**: Updates to meta.lastUpdated should reflect changes in clinical status or verification status
**Text**: "Updates to `Condition.meta.lastUpdated` SHOULD reflect: Changes in the clinical status or verifications status of problems or health concern"
**Context**: Defining recommended practice for updating lastUpdated timestamp when clinical or verification status of problems or health concerns changes
**Verification**: Test
**Actor**: System managing Condition resources
**Conformance**: SHOULD
**Conditional**: True
**Source**: Section 14.3.3.5 Condition - Resource Specific Documentation
---
