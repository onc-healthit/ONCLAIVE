# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Server SHALL support search by given name on Practitioner resource
**Requirement**: "Select Practitioners with the specified given name [using parameter `given`:`string` with Expression `Practitioner.name.given`]"
**Context**: The Plannet_sp_practitioner_given_name search parameter enables searching for Practitioner resources by the practitioner's given name. The search supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The exact modifier is allowed for precise matching.
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

---
# REQ-002
**ID**: 02
**Summary**: Practitioner family name search parameter support
**Requirement**: "Select Practitioners with the specified family name [using search parameter `family`:`string` on Practitioner resource with Expression `Practitioner.name.family`]"
**Context**: The implementation guide defines a search parameter for Practitioner resources that allows searching by family name. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The allowed modifier is exact.
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

---
# REQ-003
**ID**: 03
**Summary**: Health Plan API Actor SHALL support searching Practitioners by name parameter
**Requirement**: "Select Practitioners with the specified name (matches against any of the elements in the HumanName data type)" using Parameter `name`:`string` with Expression `Practitioner.name`
**Context**: The SearchParameter Plannet_sp_practitioner_name enables searching for Practitioner resources by name, matching against any element in the HumanName data type. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). Allowed modifiers are: exact, contains.
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

---
# REQ-004
**ID**: 04
**Summary**: Health Plan API Actor SHALL support period search parameter on Practitioner resource
**Requirement**: "Select Practitioner entries available during the specified period [using] Parameter `period`:`date` [with] Expression `Practitioner.extension.where(url='http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-period').value`"
**Context**: This search parameter allows querying Practitioner resources by their availability period using a date-based search on a custom extension. The parameter supports multipleOr (comma-separated values where at least one must be true), and support for multipleAnd is at server discretion.
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

---
# REQ-005
**ID**: 05
**Summary**: Communication proficiency extension value binding requirement
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [Language Proficiency VS]"
**Context**: The communication-proficiency extension is used on Practitioner.communication to express a practitioner's spoken proficiency with the indicated language. The value[x] element of this extension must use a CodeableConcept constrained to the LanguageProficiencyVS value set, which contains valid codes from the Language Proficiency CS code system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.67.1.1.1 Terminology Bindings
**Grouping**: Practitioner
---

---
# REQ-006
**ID**: 06
**Summary**: Extension.url SHALL be a URI for the Structure Definition defining the extension
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element within the Extension.url definition for the practitioner-period extension. The url element identifies the meaning and definition of the extension and must be a valid URI pointing to the Structure Definition.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions, Extension.url element
**Grouping**: Practitioner
---

---
# REQ-007
**ID**: 07
**Summary**: Extension SHALL have either extensions or value[x], not both
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: This is an invariant (ext-1) that applies to the Extension element of the practitioner-period extension. It enforces that an extension must contain either nested extensions or a value, but not both simultaneously.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions, Extension element invariants
**Grouping**: Practitioner
---

---
# REQ-008
**ID**: 08
**Summary**: All FHIR elements must have a @value or children
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: This is an invariant (ele-1) that applies to all FHIR elements within the practitioner-period extension. It ensures that every element contains either a value attribute or child elements beyond just an id.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions, Element invariants
**Grouping**: Practitioner
---

---
# REQ-009
**ID**: 09
**Summary**: Extension.value[x] codes SHALL be from Language Proficiency VS
**Requirement**: "The codes SHALL be taken from [Language Proficiency VS](ValueSet-LanguageProficiencyVS.html) (required to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/LanguageProficiencyVS`)"
**Context**: This requirement constrains the value element of the CommunicationProficiency extension. When a value is provided for this extension, it must be a code from the specified Language Proficiency value set, which is bound with required strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.67.1 Extension: CommunicationProficiency - Detailed Descriptions, Element Extension.value[x]
**Grouping**: Practitioner
---

---
# REQ-010
**ID**: 10
**Summary**: Practitioner Qualification Extension - Status Element Cardinality
**Requirement**: "The Practitioner Qualification extension SHALL include exactly one status element [with cardinality 1..1]"
**Context**: The Practitioner Qualification extension is used to add status and whereValid elements to a practitioner's qualifications on the Practitioner.qualification element. The status sub-extension is mandatory and must appear exactly once in any instance of this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1.1 Formal Views of Extension Content - Differential Table
**Grouping**: Practitioner
---

---
# REQ-011
**ID**: 11
**Summary**: Practitioner Qualification Extension - Status Value Binding
**Requirement**: "The status value[x] element SHALL be bound to the Qualification Status VS value set with required conformance"
**Context**: When populating the status sub-extension within the Practitioner Qualification extension, the code value must come from the specified Qualification Status value set. This is a required binding, meaning the concept must be from the specified value set to be conformant.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1.1.1 Terminology Bindings
**Grouping**: Practitioner
---

---
# REQ-012
**ID**: 12
**Summary**: Practitioner Qualification Extension - WhereValid ValueCodeableConcept Binding
**Requirement**: "The whereValid value[x]:valueCodeableConcept element SHALL be bound to the USPS Two Letter Alphabetic Codes value set with required conformance"
**Context**: When the whereValid sub-extension uses a CodeableConcept data type to indicate where a practitioner's qualification is valid, it must use codes from the USPS Two Letter Alphabetic Codes value set. This is a required binding.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the whereValid sub-extension is present and uses the valueCodeableConcept slice (rather than valueReference).
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1.1.1 Terminology Bindings
**Grouping**: Practitioner
---

---
# REQ-013
**ID**: 13
**Summary**: Practitioner Qualification Extension - Extension Element Cardinality
**Requirement**: "The Practitioner Qualification extension SHALL include at least one extension element [with cardinality 1..*]"
**Context**: The Practitioner Qualification complex extension must contain at least one sub-extension element. Given that the status sub-extension is required (1..1) and whereValid is optional (0..*), this requirement ensures the extension structure contains extension elements.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1.1 Formal Views of Extension Content - Differential Table
**Grouping**: Practitioner
---

---
# REQ-014
**ID**: 14
**Summary**: Plan-Net Server SHALL support search-type and read interactions on Practitioner resource
**Requirement**: "A Server SHALL support search-type, read [on Practitioner resource]."
**Context**: This requirement mandates that the server must support the ability to search for Practitioner resources and read individual Practitioner resources by their logical ID.
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

---
# REQ-015
**ID**: 15
**Summary**: Plan-Net Server SHOULD support vread interaction on Practitioner resource
**Requirement**: "A Server SHOULD support vread [on Practitioner resource]."
**Context**: This requirement recommends that the server should support retrieving specific historical versions of a Practitioner resource using the version-aware read (vread) operation.
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

---
# REQ-016
**ID**: 16
**Summary**: Plan-Net Server SHALL support reading Practitioner resource by id
**Requirement**: "A Server SHALL be capable of returning a Practitioner resource using: `GET [base]/Practitioner/[id]`"
**Context**: This requirement mandates that the server must support retrieving a specific Practitioner resource using its logical ID via a GET operation.
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

---
# REQ-017
**ID**: 17
**Summary**: Plan-Net Server SHOULD support vread on Practitioner resource by id and version
**Requirement**: "A Server SHOULD be capable of returning a Practitioner resource using: `GET [base]/Practitioner/[id]/_history/vid`"
**Context**: This requirement recommends that the server should support retrieving a specific version of a Practitioner resource using its logical ID and version ID.
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

---
# REQ-018
**ID**: 18
**Summary**: Plan-Net Server SHALL support _revinclude parameter for Practitioner resource
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:practitioner - `GET [base]/Practitioner?[parameter=value]&_revinclude=PractitionerRole:practitioner`"
**Context**: This requirement mandates that the server must support reverse includes to retrieve PractitionerRole resources that reference the Practitioner resources in the search results.
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

---
# REQ-019
**ID**: 19
**Summary**: Plan-Net Server SHALL support search parameters on Practitioner resource
**Requirement**: "A Server SHALL support the following search parameters on Practitioner: name, _id, _lastUpdated, family, given"
**Context**: This requirement mandates that the server must support searching for Practitioner resources using the specified string parameters (name, family, given) and standard parameters (_id, _lastUpdated).
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

---
# REQ-020
**ID**: 20
**Summary**: PractitionerQualification extension URL fixed value
**Requirement**: "Extension.url [Fixed Value]: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification"
**Context**: The extension URL element must have the fixed value identifying this as the PractitionerQualification extension. This is required to properly identify the extension in FHIR resources.
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

---
# REQ-021
**ID**: 21
**Summary**: PractitionerQualification extension status URL fixed value
**Requirement**: "Extension.extension:status.url [Fixed Value]: status"
**Context**: The status sub-extension URL must have the fixed value 'status' to properly identify this sub-extension within the PractitionerQualification extension structure.
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

---
# REQ-022
**ID**: 22
**Summary**: PractitionerQualification extension whereValid URL fixed value
**Requirement**: "Extension.extension:whereValid.url [Fixed Value]: whereValid"
**Context**: The whereValid sub-extension URL must have the fixed value 'whereValid' to properly identify this sub-extension within the PractitionerQualification extension structure.
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

---
# REQ-023
**ID**: 23
**Summary**: Practitioner resource SHALL have at least one identifier
**Requirement**: "Practitioner.identifier [has cardinality] 1..*"
**Context**: The Plan-Net Practitioner profile requires that each Practitioner resource instance must include at least one identifier to uniquely identify the practitioner in their role.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: N/A
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile - Plan-Net Practitioner
**Grouping**: Practitioner
---

---
# REQ-024
**ID**: 24
**Summary**: Practitioner identifier system SHALL be present
**Requirement**: "Practitioner.identifier.system [has cardinality] 1.1"
**Context**: Each identifier for a Practitioner must include the system that establishes the namespace for the identifier value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: N/A
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile - Plan-Net Practitioner
**Grouping**: Practitioner
---

---
# REQ-025
**ID**: 25
**Summary**: Practitioner identifier value SHALL be present
**Requirement**: "Practitioner.identifier.value [has cardinality] 1.1"
**Context**: Each identifier for a Practitioner must include a value that is unique within the context of the system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: N/A
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile - Plan-Net Practitioner
**Grouping**: Practitioner
---

---
# REQ-026
**ID**: 26
**Summary**: Practitioner NPI identifier system SHALL be fixed value
**Requirement**: "Practitioner.identifier:NPI.system [has] Fixed Value: http://hl7.org/fhir/sid/us-npi"
**Context**: When a Practitioner identifier is of type NPI, the system element must be set to the fixed value representing the US National Provider Identifier system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when identifier slice is of type NPI
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile - Plan-Net Practitioner
**Grouping**: Practitioner
---

---
# REQ-027
**ID**: 27
**Summary**: Practitioner NPI must be 10 digits
**Requirement**: "NPI must be 10 digits: value.matches('^[0-9]{10}$')"
**Context**: Constraint us-core-16 requires that when an NPI identifier is provided, the value must be exactly 10 numeric digits.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when identifier slice is of type NPI
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1.1.10 Constraints
**Grouping**: Practitioner
---

---
# REQ-028
**ID**: 28
**Summary**: Practitioner NPI check digit must be valid per Luhn algorithm
**Requirement**: "NPI check digit must be valid (Luhn algorithm check): (((select(value.substring(0,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(1,1).toInteger())+(select(value.substring(2,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(3,1).toInteger())+(select(value.substring(4,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(5,1).toInteger())+(select(value.substring(6,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(7,1).toInteger())+(select(value.substring(8,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(9,1).toInteger()) + 24)mod 10=0)"
**Context**: Constraint us-core-17 requires that the NPI check digit must be valid according to the Luhn algorithm to ensure data integrity.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when identifier slice is of type NPI
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1.1.10 Constraints
**Grouping**: Practitioner
---

---
# REQ-029
**ID**: 29
**Summary**: Practitioner active status SHALL be present and true
**Requirement**: "Practitioner.active [has cardinality] 1.1 [with] Required Pattern: true"
**Context**: The Practitioner profile requires the active element to be present with a value of true, indicating the practitioner's record is in active use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: N/A
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile - Plan-Net Practitioner
**Grouping**: Practitioner
---

---
# REQ-030
**ID**: 30
**Summary**: Practitioner SHALL have at least one name
**Requirement**: "Practitioner.name [has cardinality] 1..*"
**Context**: The Plan-Net Practitioner profile requires that each Practitioner resource must include at least one name associated with the practitioner.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: N/A
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile - Plan-Net Practitioner
**Grouping**: Practitioner
---

---
# REQ-031
**ID**: 31
**Summary**: Practitioner name SHALL include family name
**Requirement**: "Practitioner.name.family [has cardinality] 1.1"
**Context**: Each name for a Practitioner must include the family name (surname) to properly identify the practitioner.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: N/A
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile - Plan-Net Practitioner
**Grouping**: Practitioner
---

---
# REQ-032
**ID**: 32
**Summary**: Practitioner qualification code SHALL be present
**Requirement**: "Practitioner.qualification.code [has cardinality] 1.1"
**Context**: When qualification information is provided for a Practitioner, the coded representation of the qualification must be included.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when qualification element is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile - Plan-Net Practitioner
**Grouping**: Practitioner
---
