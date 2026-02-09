# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Server SHALL support searching Practitioner by given name
**Requirement**: "Select Practitioners with the specified given name [using search parameter `given` of type `string` with Expression `Practitioner.name.given`]"
**Context**: The implementation guide defines a search parameter for finding Practitioner resources based on the given name element. This search parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The 'exact' modifier is allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.54.1 SearchParameter: Plannet_sp_practitioner_given_name
**Grouping**: Practitioner

---
# REQ-002
**ID**: 02
**Summary**: Support for Practitioner family name search parameter with multipleAnd
**Requirement**: "The parameter may repeat in order to specify multiple values that must all be true"
**Context**: The practitioner-family-name search parameter allows searching for Practitioner resources by family name. This requirement specifies that the server must support multiple repetitions of the family parameter where all specified values must match (AND logic).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.53.1 SearchParameter: Plannet_sp_practitioner_family_name
**Grouping**: Practitioner

---
# REQ-003
**ID**: 03
**Summary**: Support for Practitioner family name search parameter with multipleOr
**Requirement**: "The parameter may have multiple values (separated by comma) where at least one must be true"
**Context**: The practitioner-family-name search parameter allows searching for Practitioner resources by family name. This requirement specifies that the server must support comma-separated values for the family parameter where at least one value must match (OR logic).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.53.1 SearchParameter: Plannet_sp_practitioner_family_name
**Grouping**: Practitioner

---
# REQ-004
**ID**: 04
**Summary**: Support search by name parameter on Practitioner resource
**Requirement**: "Select Practitioners with the specified name (matches against any of the elements in the HumanName data type)"
**Context**: The Plannet_sp_practitioner_name search parameter allows searching for Practitioner resources using the name parameter which matches against any element in the HumanName data type. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). Allowed modifiers are exact and contains.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.55.1 SearchParameter: Plannet_sp_practitioner_name
**Grouping**: Practitioner

---
# REQ-005
**ID**: 05
**Summary**: Server SHALL support period search parameter on Practitioner resource
**Requirement**: "Server SHALL support Parameter `period`:`date` [to] Select Practitioner entries available during the specified period [using Expression] `Practitioner.extension.where(url='http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-period').value` [with] multipleAnd: It's up to the server whether the parameter may repeat in order to specify multiple values that must all be true [and] multipleOr: The parameter may have multiple values (separated by comma) where at least one must be true"
**Context**: This requirement defines a date-based search parameter for Practitioner resources that searches on an extension field (practitioner-period) to filter practitioners by availability period. The multipleAnd behavior is server-discretionary while multipleOr is required.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.56.1 SearchParameter: Plannet_sp_practitioner_period
**Grouping**: Practitioner

---
# REQ-006
**ID**: 06
**Summary**: Communication Proficiency Extension value[x] SHALL use required value set
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [Language Proficiency VS]"
**Context**: The Communication Proficiency extension is used to express a practitioner's spoken proficiency with languages indicated in Practitioner.communication. The value[x] element of this extension must contain a CodeableConcept that is bound to the Language Proficiency value set with required binding strength, meaning the code must come from the specified value set.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.67.1 Extension: Communication Proficiency / 11.67.1.1.1 Terminology Bindings
**Grouping**: Practitioner

---
# REQ-007
**ID**: 07
**Summary**: PractitionerPeriod Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the PractitionerPeriod extension's URL element, which must be a URI pointing to the Structure Definition. The fixed value for this extension is `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-period`.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-008
**ID**: 08
**Summary**: PractitionerPeriod Extension Value Element Must Support
**Requirement**: "Extension.value[x] [Must Support] true"
**Context**: The value[x] element of the PractitionerPeriod extension must be supported by implementations. This element has a cardinality of 1..1 and is constrained to type Period in the snapshot view. The extension indicates when a Practitioner entry is or was active.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-009
**ID**: 09
**Summary**: Extension Must Have Either Extensions or Value[x]
**Requirement**: "Must have either extensions or value[x], not both (`extension.exists() != value.exists()`)"
**Context**: This invariant (ext-1) applies to the Extension element and its nested extension element. An extension must contain either child extensions OR a value, but not both simultaneously.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-010
**ID**: 10
**Summary**: Extension.url fixed value requirement for CommunicationProficiency extension
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the Extension.url element within the CommunicationProficiency extension. The URL must be fixed to the value `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency` to properly identify this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.67.1 Extension: CommunicationProficiency - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-011
**ID**: 11
**Summary**: Value set binding requirement for CommunicationProficiency extension value
**Requirement**: "The codes SHALL be taken from Language Proficiency VS ([required] to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/LanguageProficiencyVS`)"
**Context**: This requirement constrains the Extension.value[x] element of the CommunicationProficiency extension to use codes only from the Language Proficiency Value Set. The value must be a CodeableConcept with codes from the specified value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.67.1 Extension: CommunicationProficiency - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-012
**ID**: 12
**Summary**: Practitioner Qualification Extension status element cardinality
**Requirement**: "The [extension:status] element SHALL have cardinality 1..1"
**Context**: The Practitioner Qualification extension defines a status sub-extension that must be present exactly once when the extension is used on Practitioner.qualification elements. This ensures that qualification status information is consistently provided.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Practitioner Qualification extension is used on a Practitioner.qualification element.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: Practitioner Qualification - Differential Table
**Grouping**: Practitioner

---
# REQ-013
**ID**: 13
**Summary**: Practitioner Qualification Extension status value binding
**Requirement**: "The [extension:status.value[x]] element SHALL be bound to the Qualification Status VS value set (required binding) with Fixed Value: active"
**Context**: When providing qualification status information through the Practitioner Qualification extension, the status value must conform to the QualificationStatusVS value set defined in the implementation guide. The fixed value constraint requires the status to be 'active'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Practitioner Qualification extension is used on a Practitioner.qualification element and includes a status sub-extension.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: Practitioner Qualification - Differential Table, 11.76.1.1.1 Terminology Bindings
**Grouping**: Practitioner

---
# REQ-014
**ID**: 14
**Summary**: Practitioner Qualification Extension whereValid value binding
**Requirement**: "The [extension:whereValid.value[x]:valueCodeableConcept] element SHALL be bound to the USPS Two Letter Alphabetic Codes value set (required binding)"
**Context**: When specifying where a practitioner's qualification is valid using a CodeableConcept, the codes used must come from the US Core USPS state codes value set. This ensures consistent representation of US state/territory jurisdictions where qualifications are valid.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Practitioner Qualification extension includes a whereValid sub-extension with a valueCodeableConcept.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: Practitioner Qualification - Differential Table, 11.76.1.1.1 Terminology Bindings
**Grouping**: Practitioner

---
# REQ-015
**ID**: 15
**Summary**: Server SHALL support search-type and read interactions on Practitioner resource
**Requirement**: "A Server SHALL support search-type, read [on Practitioner resource]."
**Context**: This requirement mandates support for search-type and read operations on the Practitioner resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-016
**ID**: 16
**Summary**: Server SHOULD support vread interaction on Practitioner resource
**Requirement**: "A Server SHOULD support vread [on Practitioner resource]."
**Context**: This requirement recommends support for version-specific read operations on the Practitioner resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-017
**ID**: 17
**Summary**: Server SHALL support returning Practitioner resource by id
**Requirement**: "A Server SHALL be capable of returning a Practitioner resource using: GET [base]/Practitioner/[id]"
**Context**: This requirement mandates the ability to retrieve a specific Practitioner resource by its logical id.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-018
**ID**: 18
**Summary**: Server SHOULD support returning Practitioner resource by version id
**Requirement**: "A Server SHOULD be capable of returning a Practitioner resource using: GET [base]/Practitioner/[id]/_history/vid"
**Context**: This requirement recommends the ability to retrieve a specific version of a Practitioner resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-019
**ID**: 19
**Summary**: Server SHALL support _revinclude for Practitioner resources
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:practitioner"
**Context**: This requirement mandates support for reverse includes to retrieve PractitionerRole resources that reference a Practitioner.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-020
**ID**: 20
**Summary**: Server SHALL support search parameters on Practitioner resource
**Requirement**: "A Server SHALL support the following search parameters on Practitioner: name, _id, _lastUpdated, family, given"
**Context**: This requirement mandates support for searching Practitioner resources by full name, id, last updated timestamp, family name, and given name.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-021
**ID**: 21
**Summary**: PractitionerQualification extension status element must be present
**Requirement**: "Extension.extension:status [Control: 1.1] [Must Support: true]"
**Context**: The PractitionerQualification extension defines a status sub-extension that indicates the status of a practitioner's qualification. This element has a cardinality of 1..1, meaning it is required and must appear exactly once when the extension is used. The element is marked as Must Support, indicating that systems claiming conformance to this profile must be capable of populating and processing this element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-022
**ID**: 22
**Summary**: PractitionerQualification extension status value must use codes from QualificationStatusVS value set
**Requirement**: "The codes SHALL be taken from [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required] to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/QualificationStatusVS`)"
**Context**: The status sub-extension's value element must use codes from the QualificationStatusVS value set with a required binding strength. This means that only codes from this specific value set are permitted.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-023
**ID**: 23
**Summary**: PractitionerQualification extension whereValid CodeableConcept must use codes from USPS state codes value set
**Requirement**: "The codes SHALL be taken from [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU7/ValueSet-us-core-usps-state.html) ([required] to `http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state`)"
**Context**: When the whereValid sub-extension uses a CodeableConcept data type to indicate where a practitioner's qualification is valid, the codes must be taken from the USPS Two Letter Alphabetic Codes value set with required binding strength. This ensures standardized representation of US state codes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-024
**ID**: 24
**Summary**: Extension definition must be a URI for the Structure Definition
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the extension and its sub-extensions. The url must be a valid URI that points to the Structure Definition that defines the extension, ensuring proper identification and resolution of the extension definition.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-025
**ID**: 25
**Summary**: Extension requirements that SHALL be met as part of extension definition
**Requirement**: "Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: This general requirement establishes that while FHIR allows implementers to define extensions, there are mandatory requirements that must be satisfied when defining extensions to ensure safe and manageable use. This applies to the governance of extension definitions within the FHIR specification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-026
**ID**: 26
**Summary**: Practitioner identifier cardinality requirement
**Requirement**: "Practitioner.identifier [Control: 1.*]"
**Context**: The Plan-Net Practitioner profile requires at least one identifier element to be present. This is a structural constraint on the Practitioner resource that ensures practitioners can be uniquely identified within the system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-027
**ID**: 27
**Summary**: Practitioner identifier system cardinality requirement
**Requirement**: "Practitioner.identifier.system [Control: 1.1]"
**Context**: Within each Practitioner identifier, the system element must be present exactly once to establish the namespace for the identifier value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-028
**ID**: 28
**Summary**: Practitioner identifier value cardinality requirement
**Requirement**: "Practitioner.identifier.value [Control: 1.1]"
**Context**: Within each Practitioner identifier, the value element must be present exactly once to provide the unique identifier value within the specified system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-029
**ID**: 29
**Summary**: Practitioner NPI must be 10 digits
**Requirement**: "NPI must be 10 digits (value.matches('^[0-9]{10}$'))"
**Context**: When a Practitioner identifier is sliced as an NPI (National Provider Identifier), the value must match the pattern of exactly 10 numeric digits. This is enforced through the invariant us-core-16.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the identifier is an NPI (identifier:NPI slice)
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-030
**ID**: 30
**Summary**: Practitioner NPI check digit must be valid
**Requirement**: "NPI check digit must be valid (Luhn algorithm check) ((((select(value.substring(0,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(1,1).toInteger())+(select(value.substring(2,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(3,1).toInteger())+(select(value.substring(4,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(5,1).toInteger())+(select(value.substring(6,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(7,1).toInteger())+(select(value.substring(8,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(9,1).toInteger()) + 24)mod 10=0))"
**Context**: When a Practitioner identifier is sliced as an NPI, the check digit must pass the Luhn algorithm validation. This is enforced through the invariant us-core-17 to ensure the NPI is mathematically valid.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the identifier is an NPI (identifier:NPI slice)
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-031
**ID**: 31
**Summary**: Practitioner active status cardinality requirement
**Requirement**: "Practitioner.active [Control: 1.1]"
**Context**: The active element must be present exactly once in the Practitioner resource to indicate whether the practitioner's record is in active use. The profile sets a pattern value of 'true'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-032
**ID**: 32
**Summary**: Practitioner name cardinality requirement
**Requirement**: "Practitioner.name [Control: 1.*]"
**Context**: At least one name must be present for a Practitioner resource. The name(s) that a Practitioner is known by should be captured, with the name that the practitioner is usually known as being used in displays.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-033
**ID**: 33
**Summary**: Practitioner name family cardinality requirement
**Requirement**: "Practitioner.name.family [Control: 1.1]"
**Context**: Within each Practitioner name, the family (surname) element must be present exactly once to capture the genealogical part of the name.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-034
**ID**: 34
**Summary**: Practitioner qualification code cardinality requirement
**Requirement**: "Practitioner.qualification.code [Control: 1.1]"
**Context**: When a qualification is present for a Practitioner, the coded representation of the qualification must be present exactly once. The binding is extensible to the Individual Specialties, Degrees, Licenses, and Certificates value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when a Practitioner.qualification element is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-035
**ID**: 35
**Summary**: Contained resources must not contain nested resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources (contained.contained.empty())"
**Context**: This is the dom-2 invariant that applies to the Practitioner resource. If a Practitioner resource is contained within another resource, it must not itself contain any contained resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the Practitioner resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-036
**ID**: 36
**Summary**: Contained resources must be referenced or refer to containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource (contained.where((('#'+id in (%resource.descendants().reference   %resource.descendants().as(canonical)   %resource.descendants().as(uri)   %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty())"
**Context**: This is the dom-3 invariant. If a Practitioner resource is contained in another resource, it must be referenced from elsewhere in the containing resource or must refer to the containing resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the Practitioner resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-037
**ID**: 37
**Summary**: Contained resources must not have versionId or lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (contained.meta.versionId.empty() and contained.meta.lastUpdated.empty())"
**Context**: This is the dom-4 invariant. Contained Practitioner resources must not have version metadata.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the Practitioner resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-038
**ID**: 38
**Summary**: Contained resources must not have security labels
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label (contained.meta.security.empty())"
**Context**: This is the dom-5 invariant. Contained Practitioner resources must not have security labels in their meta element.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the Practitioner resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-039
**ID**: 39
**Summary**: Modifier extensions must not change meaning of resource elements
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)."
**Context**: This requirement applies to the modifierExtension element at the Practitioner resource level and within the qualification backbone element. Modifier extensions must follow FHIR governance rules and not alter the core meaning of resource elements.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when modifierExtension elements are present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-040
**ID**: 40
**Summary**: Name text and parts consistency requirement
**Requirement**: "Applications updating a name SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part."
**Context**: When updating a Practitioner's name, if both the text representation and structured parts (family, given, etc.) are present, the application must ensure consistency between them.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when updating a Practitioner name that has both text and parts elements present
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-041
**ID**: 41
**Summary**: Address text and parts consistency requirement
**Requirement**: "Applications updating an address SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part."
**Context**: When updating a Practitioner's address, if both the text representation and structured parts (line, city, state, etc.) are present, the application must ensure consistency between them.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when updating a Practitioner address that has both text and parts elements present
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-042
**ID**: 42
**Summary**: Full URI identifier system requirement
**Requirement**: "If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986."
**Context**: This applies to Practitioner.identifier.value. When the identifier value is a full URI, the system must be set to the specific URN indicating RFC 3986 compliance.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the identifier value is a full URI
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-043
**ID**: 43
**Summary**: NPI identifier system fixed value requirement
**Requirement**: "[For the NPI identifier slice, the] system [element SHALL have a] Fixed Value: http://hl7.org/fhir/sid/us-npi"
**Context**: When an NPI (National Provider Identifier) is provided for a Practitioner, the system element must be set to the fixed value "http://hl7.org/fhir/sid/us-npi" to ensure standardized identification of NPI identifiers.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when an NPI identifier is provided for a Practitioner.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: Plan-Net Practitioner
**Grouping**: Practitioner
