# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the US Core FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.

---
# REQ-001
**Summary**: US Core Server SHALL support US Core Patient resource profile and additional resource profile
**Text**: "The US Core Server **SHALL**: 1. Support the US Core Patient resource profile AND at least one additional resource profile from the list of US Core Profiles AND and all *Must Support* US Core Profiles and resources it references."
**Context**: Basic capability requirements for US Core Server implementation defining minimum profile support
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.2 FHIR RESTful Capabilities
---

---
# REQ-002
**Summary**: US Core Server SHALL follow General Requirements and Must Support pages
**Text**: "Follow the requirements documented in the [General Requirements](general-requirements.html) and [Must Support](must-support.html) pages"
**Context**: US Core Server must comply with foundational requirements and Must Support definitions
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.2 FHIR RESTful Capabilities
---

---
# REQ-003
**Summary**: US Core Server SHALL return specific HTTP response status codes
**Text**: "Return the following response classes: * (Status 400): invalid parameter * (Status 401/4xx): unauthorized request * (Status 403): insufficient scopes * (Status 404): unknown resource"
**Context**: Required HTTP status codes for error handling in US Core Server responses
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.2 FHIR RESTful Capabilities
---

---
# REQ-004
**Summary**: US Core Server SHALL support JSON source formats
**Text**: "Support JSON source formats for all US Core interactions."
**Context**: Required data format support for US Core Server interactions
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.2 FHIR RESTful Capabilities
---

---
# REQ-005
**Summary**: US Core Server SHOULD support XML source formats
**Text**: "Support XML source formats for all US Core interactions."
**Context**: Recommended additional data format support for US Core Server interactions
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.2 FHIR RESTful Capabilities
---

---
# REQ-006
**Summary**: US Core Server SHOULD identify supported profiles in meta.profile attribute
**Text**: "Identify the US Core profiles supported as part of the FHIR `meta.profile` attribute for each instance."
**Context**: Profile identification for returned FHIR resources to support client validation
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Section 14.3.2 FHIR RESTful Capabilities
---

---
# REQ-007
**Summary**: Server SHALL reject unauthorized requests with specific HTTP codes
**Text**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` \"Unauthorized\", `HTTP 403` \"Forbidden\", or `HTTP 404` \"Not Found\""
**Context**: Security requirement for handling unauthorized access attempts
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.2 FHIR RESTful Capabilities - Security
---

---
# REQ-008
**Summary**: Server SHALL support search-type and read interactions for AllergyIntolerance
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for AllergyIntolerance resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.2 AllergyIntolerance Profile Interaction Summary
---

---
# REQ-009
**Summary**: Server SHALL support returning AllergyIntolerance resource by ID
**Text**: "A Server **SHALL** be capable of returning a AllergyIntolerance resource using: `GET [base]/AllergyIntolerance/[id]`"
**Context**: Required capability for retrieving specific AllergyIntolerance resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.2 AllergyIntolerance Fetch and Search Criteria
---

---
# REQ-010
**Summary**: Server SHALL support patient search parameter for AllergyIntolerance
**Text**: "**SHALL** [patient](SearchParameter-us-core-allergyintolerance-patient.html) reference"
**Context**: Required search parameter support for finding AllergyIntolerance resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.2 AllergyIntolerance Search Parameter Summary
---

---
# REQ-011
**Summary**: Client SHALL provide at least id value for patient search parameter
**Text**: "The client **SHALL** provide at least a id value and **MAY** provide both the Type and id values."
**Context**: Client requirement for patient search parameter usage in AllergyIntolerance searches
**Verification**: Test
**Actor**: US Core Client
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.2 AllergyIntolerance Search Parameter Requirements
---

---
# REQ-012
**Summary**: Server SHALL support both Type and id values for patient search parameter
**Text**: "The server **SHALL** support both [Type and id values]."
**Context**: Server requirement for patient search parameter support in AllergyIntolerance searches
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.2 AllergyIntolerance Search Parameter Requirements
---

---
# REQ-013
**Summary**: Server SHALL support search-type and read interactions for CarePlan
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for CarePlan resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.3 CarePlan Profile Interaction Summary
---

---
# REQ-014
**Summary**: Server SHALL support patient+category search combination for CarePlan
**Text**: "**SHALL** [patient](SearchParameter-us-core-careplan-patient.html)+ [category](SearchParameter-us-core-careplan-category.html) reference+token"
**Context**: Required search parameter combination for CarePlan resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.3 CarePlan Search Parameter Combination Summary
---

---
# REQ-015
**Summary**: Client SHALL provide at least code value for category search parameter in CarePlan
**Text**: "The client **SHALL** provide at least a code value and **MAY** provide both the system and code values."
**Context**: Client requirement for category search parameter usage in CarePlan searches
**Verification**: Test
**Actor**: US Core Client
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.3 CarePlan Search Parameter Requirements
---

---
# REQ-016
**Summary**: Server SHALL support search-type and read interactions for CareTeam
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for CareTeam resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.4 CareTeam Profile Interaction Summary
---

---
# REQ-017
**Summary**: Server SHALL support patient+status search combination for CareTeam
**Text**: "**SHALL** [patient](SearchParameter-us-core-careteam-patient.html)+ [status](SearchParameter-us-core-careteam-status.html) reference+token"
**Context**: Required search parameter combination for CareTeam resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.4 CareTeam Search Parameter Combination Summary
---

---
# REQ-018
**Summary**: Server SHALL support search-type and read interactions for Condition
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Condition resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition Profile Interaction Summary
---

---
# REQ-019
**Summary**: Server SHALL support patient search parameter for Condition
**Text**: "**SHALL** [patient](SearchParameter-us-core-condition-patient.html) reference"
**Context**: Required search parameter support for finding Condition resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition Search Parameter Summary
---

---
# REQ-020
**Summary**: Server SHALL support patient+category search combination for Condition
**Text**: "**SHALL** [patient](SearchParameter-us-core-condition-patient.html)+ [category](SearchParameter-us-core-condition-category.html) reference+token"
**Context**: Required search parameter combination for Condition resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition Search Parameter Combination Summary
---

---
# REQ-021
**Summary**: Server SHALL support Condition.recordedDate
**Text**: "A server **SHALL** support `Condition.recordedDate`."
**Context**: Required support for recorded date element in Condition resources for diagnosis date tracking
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition Resource Specific Documentation
---

---
# REQ-022
**Summary**: Server SHALL support search-type and read interactions for Coverage
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Coverage resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.6 Coverage Profile Interaction Summary
---

---
# REQ-023
**Summary**: Server SHALL support patient search parameter for Coverage
**Text**: "**SHALL** [patient](SearchParameter-us-core-coverage-patient.html) reference"
**Context**: Required search parameter support for finding Coverage resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.6 Coverage Search Parameter Summary
---

---
# REQ-024
**Summary**: Server SHALL support search-type and read interactions for Device
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Device resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.7 Device Profile Interaction Summary
---

---
# REQ-025
**Summary**: Server SHALL support patient search parameter for Device
**Text**: "**SHALL** [patient](SearchParameter-us-core-device-patient.html) reference"
**Context**: Required search parameter support for finding Device resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.7 Device Search Parameter Summary
---

---
# REQ-026
**Summary**: Implantable devices with UDI SHALL represent UDI code in Device.udiCarrier.carrierHRF
**Text**: "Implantable medical devices that have UDI information **SHALL** represent the UDI code in `Device.udiCarrier.carrierHRF`."
**Context**: Required representation of UDI information for implantable medical devices
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: True
**Source**: Section 14.3.3.7 Device Resource Specific Documentation
---

---
# REQ-027
**Summary**: Server SHALL support search-type and read interactions for DiagnosticReport
**Text**: "**SHALL** support `create`†, `search-type`, `read`."
**Context**: Required interactions for DiagnosticReport resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.8 DiagnosticReport Profile Interaction Summary
---

---
# REQ-028
**Summary**: Server SHALL support patient search parameter for DiagnosticReport
**Text**: "**SHALL** [patient](SearchParameter-us-core-diagnosticreport-patient.html) reference"
**Context**: Required search parameter support for finding DiagnosticReport resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.8 DiagnosticReport Search Parameter Summary
---

---
# REQ-029
**Summary**: Server SHALL support patient+category search combination for DiagnosticReport
**Text**: "**SHALL** [patient](SearchParameter-us-core-diagnosticreport-patient.html)+ [category](SearchParameter-us-core-diagnosticreport-category.html) reference+token"
**Context**: Required search parameter combination for DiagnosticReport resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.8 DiagnosticReport Search Parameter Combination Summary
---

---
# REQ-030
**Summary**: Server SHALL support create, search-type and read interactions for DocumentReference
**Text**: "**SHALL** support `create`, `search-type`, `read`."
**Context**: Required interactions for DocumentReference resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.9 DocumentReference Profile Interaction Summary
---

---
# REQ-031
**Summary**: Server SHALL support $docref operation
**Text**: "**SHALL** support the [$docref](OperationDefinition-docref.html) operation"
**Context**: Required operation support for document reference retrieval
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.9 DocumentReference Operation Summary
---

---
# REQ-032
**Summary**: Server SHALL support _id and patient search parameters for DocumentReference
**Text**: "**SHALL** [_id](SearchParameter-us-core-documentreference-id.html) token **SHALL** [patient](SearchParameter-us-core-documentreference-patient.html) reference"
**Context**: Required search parameter support for finding DocumentReference resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.9 DocumentReference Search Parameter Summary
---

---
# REQ-033
**Summary**: Server SHALL support search-type and read interactions for Encounter
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Encounter resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.10 Encounter Profile Interaction Summary
---

---
# REQ-034
**Summary**: Server SHALL support _id and patient search parameters for Encounter
**Text**: "**SHALL** [_id](SearchParameter-us-core-encounter-id.html) token **SHALL** [patient](SearchParameter-us-core-encounter-patient.html) reference"
**Context**: Required search parameter support for finding Encounter resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.10 Encounter Search Parameter Summary
---

---
# REQ-035
**Summary**: Server SHALL support date+patient search combination for Encounter
**Text**: "**SHALL** [date](SearchParameter-us-core-encounter-date.html)+ [patient](SearchParameter-us-core-encounter-patient.html) date+reference"
**Context**: Required search parameter combination for Encounter resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.10 Encounter Search Parameter Combination Summary
---

---
# REQ-036
**Summary**: Server SHALL support search-type and read interactions for Goal
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Goal resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.12 Goal Profile Interaction Summary
---

---
# REQ-037
**Summary**: Server SHALL support patient search parameter for Goal
**Text**: "**SHALL** [patient](SearchParameter-us-core-goal-patient.html) reference"
**Context**: Required search parameter support for finding Goal resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.12 Goal Search Parameter Summary
---

---
# REQ-038
**Summary**: Server SHALL support search-type and read interactions for Immunization
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Immunization resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.14 Immunization Profile Interaction Summary
---

---
# REQ-039
**Summary**: Server SHALL support patient search parameter for Immunization
**Text**: "**SHALL** [patient](SearchParameter-us-core-immunization-patient.html) reference"
**Context**: Required search parameter support for finding Immunization resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.14 Immunization Search Parameter Summary
---

---
# REQ-040
**Summary**: Server SHALL support search-type and read interactions for Location
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Location resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.15 Location Profile Interaction Summary
---

---
# REQ-041
**Summary**: Server SHALL support address and name search parameters for Location
**Text**: "**SHALL** [address](SearchParameter-us-core-location-address.html) string **SHALL** [name](SearchParameter-us-core-location-name.html) string"
**Context**: Required search parameter support for finding Location resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.15 Location Search Parameter Summary
---

---
# REQ-042
**Summary**: Server SHALL support read interaction for Medication
**Text**: "**SHALL** support `read`."
**Context**: Required interactions for Medication resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.17 Medication Profile Interaction Summary
---

---
# REQ-043
**Summary**: Server SHALL support search-type and read interactions for MedicationDispense
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for MedicationDispense resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.18 MedicationDispense Profile Interaction Summary
---

---
# REQ-044
**Summary**: Server SHALL support patient search parameter for MedicationDispense
**Text**: "**SHALL** [patient](SearchParameter-us-core-medicationdispense-patient.html) reference"
**Context**: Required search parameter support for finding MedicationDispense resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.18 MedicationDispense Search Parameter Summary
---

---
# REQ-045
**Summary**: Server SHALL support search-type and read interactions for MedicationRequest
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for MedicationRequest resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.19 MedicationRequest Profile Interaction Summary
---

---
# REQ-046
**Summary**: Server SHALL support patient+intent+status search combination for MedicationRequest
**Text**: "**SHALL** [patient](SearchParameter-us-core-medicationrequest-patient.html)+ [intent](SearchParameter-us-core-medicationrequest-intent.html)+ [status](SearchParameter-us-core-medicationrequest-status.html) reference+token+token"
**Context**: Required search parameter combination for MedicationRequest resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.19 MedicationRequest Search Parameter Combination Summary
---

---
# REQ-047
**Summary**: Server SHALL support patient+intent search combination for MedicationRequest
**Text**: "**SHALL** [patient](SearchParameter-us-core-medicationrequest-patient.html)+ [intent](SearchParameter-us-core-medicationrequest-intent.html) reference+token"
**Context**: Required search parameter combination for MedicationRequest resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.19 MedicationRequest Search Parameter Combination Summary
---

---
# REQ-048
**Summary**: Server SHALL support search-type and read interactions for Observation
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Observation resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.20 Observation Profile Interaction Summary
---

---
# REQ-049
**Summary**: Server SHALL support patient+category search combination for Observation
**Text**: "**SHALL** [patient](SearchParameter-us-core-observation-patient.html)+ [category](SearchParameter-us-core-observation-category.html) reference+token"
**Context**: Required search parameter combination for Observation resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.20 Observation Search Parameter Combination Summary
---

---
# REQ-050
**Summary**: Server SHALL support patient+category+date search combination for Observation
**Text**: "**SHALL** [patient](SearchParameter-us-core-observation-patient.html)+ [category](SearchParameter-us-core-observation-category.html)+ [date](SearchParameter-us-core-observation-date.html) reference+token+date"
**Context**: Required search parameter combination for Observation resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.20 Observation Search Parameter Combination Summary
---
---
# REQ-051
**Summary**: Server SHALL support patient+code search combination for Observation
**Text**: "**SHALL** [patient](SearchParameter-us-core-observation-patient.html)+ [code](SearchParameter-us-core-observation-code.html) reference+token"
**Context**: Required search parameter combination for Observation resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.20 Observation Search Parameter Combination Summary
---

# REQ-052
**Summary**: Server SHALL support search-type and read interactions for Organization
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Organization resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.21 Organization Profile Interaction Summary
---

# REQ-053
**Summary**: Server SHALL support address and name search parameters for Organization
**Text**: "**SHALL** [address](SearchParameter-us-core-organization-address.html) string **SHALL** [name](SearchParameter-us-core-organization-name.html) string"
**Context**: Required search parameter support for finding Organization resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.21 Organization Search Parameter Summary
---

# REQ-054
**Summary**: Server SHALL support search-type and read interactions for Patient
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Patient resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.22 Patient Profile Interaction Summary
---

# REQ-055
**Summary**: Server SHALL support _id, identifier, and name search parameters for Patient
**Text**: "**SHALL** [_id](SearchParameter-us-core-patient-id.html) token **SHALL** [identifier](SearchParameter-us-core-patient-identifier.html) token **SHALL** [name](SearchParameter-us-core-patient-name.html) string"
**Context**: Required search parameter support for finding Patient resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.22 Patient Search Parameter Summary
---

# REQ-056
**Summary**: Server SHALL support birthdate+name search combination for Patient
**Text**: "**SHALL** [birthdate](SearchParameter-us-core-patient-birthdate.html)+ [name](SearchParameter-us-core-patient-name.html) date+string"
**Context**: Required search parameter combination for Patient resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.22 Patient Search Parameter Combination Summary
---

# REQ-057
**Summary**: Server SHALL support search-type and read interactions for Practitioner
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Practitioner resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.23 Practitioner Profile Interaction Summary
---

# REQ-058
**Summary**: Server SHALL support identifier and name search parameters for Practitioner
**Text**: "**SHALL** [identifier](SearchParameter-us-core-practitioner-identifier.html) token **SHALL** [name](SearchParameter-us-core-practitioner-name.html) string"
**Context**: Required search parameter support for finding Practitioner resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.23 Practitioner Search Parameter Summary
---

# REQ-059
**Summary**: Server SHALL support search-type and read interactions for PractitionerRole
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for PractitionerRole resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.24 PractitionerRole Profile Interaction Summary
---

# REQ-060
**Summary**: Server SHALL support practitioner and specialty search parameters for PractitionerRole
**Text**: "**SHALL** [practitioner](SearchParameter-us-core-practitionerrole-practitioner.html) reference **SHALL** [specialty](SearchParameter-us-core-practitionerrole-specialty.html) token"
**Context**: Required search parameter support for finding PractitionerRole resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.24 PractitionerRole Search Parameter Summary
---

# REQ-061
**Summary**: Server SHALL support search-type and read interactions for Procedure
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Procedure resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.25 Procedure Profile Interaction Summary
---

# REQ-062
**Summary**: Server SHALL support patient search parameter for Procedure
**Text**: "**SHALL** [patient](SearchParameter-us-core-procedure-patient.html) reference"
**Context**: Required search parameter support for finding Procedure resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.25 Procedure Search Parameter Summary
---

# REQ-063
**Summary**: Server SHALL support patient+date search combination for Procedure
**Text**: "**SHALL** [patient](SearchParameter-us-core-procedure-patient.html)+ [date](SearchParameter-us-core-procedure-date.html) reference+date"
**Context**: Required search parameter combination for Procedure resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.25 Procedure Search Parameter Combination Summary
---

# REQ-064
**Summary**: Server SHALL support read interaction for Provenance
**Text**: "**SHALL** support `read`."
**Context**: Required interactions for Provenance resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.26 Provenance Profile Interaction Summary
---

# REQ-065
**Summary**: Server SHALL support _id and patient search parameters for QuestionnaireResponse
**Text**: "**SHALL** [_id](SearchParameter-us-core-questionnaireresponse-id.html) token **SHALL** [patient](SearchParameter-us-core-questionnaireresponse-patient.html) reference"
**Context**: Required search parameter support for finding QuestionnaireResponse resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.28 QuestionnaireResponse Search Parameter Summary
---

# REQ-066
**Summary**: Server SHALL support search-type and read interactions for RelatedPerson
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for RelatedPerson resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.29 RelatedPerson Profile Interaction Summary
---

# REQ-067
**Summary**: Server SHALL support _id search parameter for RelatedPerson
**Text**: "**SHALL** [_id](SearchParameter-us-core-relatedperson-id.html) token"
**Context**: Required search parameter support for finding RelatedPerson resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.29 RelatedPerson Search Parameter Summary
---

# REQ-068
**Summary**: Server SHALL support read interaction for ServiceRequest
**Text**: "**SHALL** support `read`."
**Context**: Required interactions for ServiceRequest resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.30 ServiceRequest Profile Interaction Summary
---

# REQ-069
**Summary**: Server SHALL support _id and patient search parameters for ServiceRequest
**Text**: "**SHALL** [_id](SearchParameter-us-core-servicerequest-id.html) token **SHALL** [patient](SearchParameter-us-core-servicerequest-patient.html) reference"
**Context**: Required search parameter support for finding ServiceRequest resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.30 ServiceRequest Search Parameter Summary
---

# REQ-070
**Summary**: Server SHALL support patient+category search combination for ServiceRequest
**Text**: "**SHALL** [patient](SearchParameter-us-core-servicerequest-patient.html)+ [category](SearchParameter-us-core-servicerequest-category.html) reference+token"
**Context**: Required search parameter combination for ServiceRequest resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.30 ServiceRequest Search Parameter Combination Summary
---
