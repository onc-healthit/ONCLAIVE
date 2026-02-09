# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

# REQ-001
**ID**: 01
**Summary**: Health Plan API Actor SHALL support searching HealthcareService by specialty parameter
**Requirement**: "Select services associated with the specified specialty [using] Parameter `specialty`:`token` [with] Expression `HealthcareService.specialty`"
**Context**: The SearchParameter Plannet_sp_healthcareservice_specialty defines a token-based search parameter for HealthcareService resources based on the specialty element. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple comma-separated values where at least one must be true) semantics, with text modifier allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.10.1 SearchParameter: Plannet_sp_healthcareservice_specialty
**Grouping**: HealthcareService

---

# REQ-002
**ID**: 02
**Summary**: Support search by location parameter on HealthcareService resource
**Requirement**: "Select HealthcareServices available at the specified location [using Parameter `location`:`reference` with Expression `HealthcareService.location`]"
**Context**: This search parameter allows querying HealthcareService resources filtered by the Location reference. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (comma-separated values where at least one must be true). Allowed chains include: address, address-postalcode, address-city, address-state, organization, type.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.7.1 SearchParameter: Plannet_sp_healthcareservice_location
**Grouping**: HealthcareService

---

# REQ-003
**ID**: 03
**Summary**: Support search by organization parameter on HealthcareService resource
**Requirement**: "Select HealthcareServices provided by the specified organization [using Parameter `organization`:`reference` with Expression `HealthcareService.providedBy`]"
**Context**: This search parameter allows querying HealthcareService resources filtered by the providing Organization reference. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (comma-separated values where at least one must be true). Allowed chains include: name, address, partof, type.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.9.1 SearchParameter: Plannet_sp_healthcareservice_organization
**Grouping**: HealthcareService

---

# REQ-004
**ID**: 04
**Summary**: Support search by coverage-area parameter on HealthcareService resource
**Requirement**: "Select services available in a region described by the specified location [using Parameter `coverage-area`:`reference` with Expression `HealthcareService.coverageArea`]"
**Context**: This search parameter allows querying HealthcareService resources filtered by the coverage area Location reference. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (comma-separated values where at least one must be true).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.4.1 SearchParameter: Plannet_sp_healthcareservice_coverage_area
**Grouping**: HealthcareService

---

# REQ-005
**ID**: 05
**Summary**: Server SHALL support search-type and read interactions on HealthcareService resource
**Requirement**: "A Server SHALL support search-type, read [on HealthcareService resource]."
**Context**: This requirement mandates support for search-type and read operations on the HealthcareService resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: HealthcareService

---

# REQ-006
**ID**: 06
**Summary**: Server SHOULD support vread interaction on HealthcareService resource
**Requirement**: "A Server SHOULD support vread [on HealthcareService resource]."
**Context**: This requirement recommends support for version-specific read operations on the HealthcareService resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: HealthcareService

---

# REQ-007
**ID**: 07
**Summary**: Server SHALL support returning HealthcareService resource by id
**Requirement**: "A Server SHALL be capable of returning a HealthcareService resource using: GET [base]/HealthcareService/[id]"
**Context**: This requirement mandates the ability to retrieve a specific HealthcareService resource by its logical id.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: HealthcareService

---

# REQ-008
**ID**: 08
**Summary**: Server SHOULD support returning HealthcareService resource by version id
**Requirement**: "A Server SHOULD be capable of returning a HealthcareService resource using: GET [base]/HealthcareService/[id]/_history/vid"
**Context**: This requirement recommends the ability to retrieve a specific version of a HealthcareService resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: HealthcareService

---

# REQ-009
**ID**: 09
**Summary**: Server SHALL support _include for HealthcareService resources
**Requirement**: "A Server SHALL be capable of supporting the following _includes: HealthcareService:location, HealthcareService:coverage-area, HealthcareService:organization, HealthcareService:endpoint"
**Context**: This requirement mandates support for including referenced Location, coverage-area, Organization, and Endpoint resources when searching for HealthcareService resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: HealthcareService

---

# REQ-010
**ID**: 10
**Summary**: Server SHALL support _revinclude for HealthcareService resources
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:service, OrganizationAffiliation:service"
**Context**: This requirement mandates support for reverse includes to retrieve PractitionerRole and OrganizationAffiliation resources that reference a HealthcareService.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: HealthcareService

---

# REQ-011
**ID**: 11
**Summary**: Server SHALL support search parameters on HealthcareService resource
**Requirement**: "A Server SHALL support the following search parameters on HealthcareService: location, coverage-area, organization, endpoint, name, service-category, service-type, specialty, _id, _lastUpdated"
**Context**: This requirement mandates support for searching HealthcareService resources by multiple parameters including references to related resources, name, service classifications, specialty, id, and last updated timestamp.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: HealthcareService

---

# REQ-012
**ID**: 12
**Summary**: HealthcareService.active SHALL be present and have a value of true
**Requirement**: "HealthcareService.active [Control: 1.1] [Must Support: true] [Pattern Value: true]"
**Context**: The active element indicates whether the HealthcareService record is in active use. This requirement mandates that the active element must be present (cardinality 1.1), must be supported by implementations, and must have a pattern value of 'true', meaning only active healthcare service records should be represented.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-013
**ID**: 13
**Summary**: HealthcareService.category SHALL be present with at least one value
**Requirement**: "HealthcareService.category [Control: 1.*] [Must Support: true]"
**Context**: The category element identifies the broad category of service being performed or delivered. This requirement mandates that at least one category must be present in a HealthcareService resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-014
**ID**: 14
**Summary**: HealthcareService.category plan-net-category slice SHALL use codes from Healthcare Service CategoryVS value set
**Requirement**: "HealthcareService.category:plan-net-category [Binding: The codes SHALL be taken from Healthcare Service CategoryVS (required)]"
**Context**: When the plan-net-category slice is used for the category element, it must use codes from the specified Healthcare Service CategoryVS value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-015
**ID**: 15
**Summary**: HealthcareService.type SHALL use codes from HealthcareService Types VS value set unless not suitable
**Requirement**: "HealthcareService.type [Binding: Unless not suitable, these codes SHALL be taken from HealthcareService Types VS (extensible)]"
**Context**: The type element specifies the specific type of service that may be delivered or performed. Codes should be taken from the HealthcareService Types VS value set unless not suitable for the use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-016
**ID**: 16
**Summary**: HealthcareService.specialty SHALL use codes from Specialties VS value set
**Requirement**: "HealthcareService.specialty [Binding: The codes SHALL be taken from Specialties VS (required)]"
**Context**: The specialty element contains the collection of specialties handled by the service site. Codes must be taken from the Specialties VS value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-017
**ID**: 17
**Summary**: HealthcareService.identifier.type SHOULD use codes from Identifier Type Codes value set unless not suitable
**Requirement**: "HealthcareService.identifier.type [Binding: Unless not suitable, these codes SHALL be taken from Identifier Type Codes (extensible)]"
**Context**: The identifier.type element provides a coded type for the identifier. Codes should be taken from the Identifier Type Codes value set unless not suitable.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-018
**ID**: 18
**Summary**: HealthcareService.identifier.use SHALL use codes from IdentifierUse value set
**Requirement**: "HealthcareService.identifier.use [Binding: The codes SHALL be taken from IdentifierUse (required)]"
**Context**: The identifier.use element identifies the purpose of the identifier. Codes must be taken from the IdentifierUse value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-019
**ID**: 19
**Summary**: HealthcareService.telecom.system SHALL use codes from ContactPointSystem value set
**Requirement**: "HealthcareService.telecom.system [Binding: The codes SHALL be taken from ContactPointSystem (required)]"
**Context**: The telecom.system element specifies the telecommunications form for the contact point. Codes must be taken from the ContactPointSystem value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-020
**ID**: 20
**Summary**: HealthcareService.telecom.use SHALL use codes from ContactPointUse value set
**Requirement**: "HealthcareService.telecom.use [Binding: The codes SHALL be taken from ContactPointUse (required)]"
**Context**: The telecom.use element identifies the purpose for the contact point. Codes must be taken from the ContactPointUse value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-021
**ID**: 21
**Summary**: HealthcareService.availableTime.daysOfWeek SHALL use codes from DaysOfWeek value set
**Requirement**: "HealthcareService.availableTime.daysOfWeek [Binding: The codes SHALL be taken from DaysOfWeek (required)]"
**Context**: The availableTime.daysOfWeek element indicates which days of the week are available. Codes must be taken from the DaysOfWeek value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-022
**ID**: 22
**Summary**: HealthcareService.notAvailable.description SHALL be present
**Requirement**: "HealthcareService.notAvailable.description [Control: 1.1] [Must Support: true]"
**Context**: When a notAvailable element is present, the description explaining why the time is not available must be provided. This requirement mandates that the description element must be present (cardinality 1.1) and must be supported by implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the HealthcareService.notAvailable element is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-023
**ID**: 23
**Summary**: If the HealthcareService resource is contained in another resource, it SHALL NOT contain nested Resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources (contained.contained.empty())"
**Context**: This invariant (dom-2) ensures that contained resources do not have their own contained resources, preventing multiple levels of nesting which could complicate resource processing.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the HealthcareService resource is contained within another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-024
**ID**: 24
**Summary**: If the HealthcareService resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This invariant (dom-3) ensures that contained resources are actually used by requiring they either be referenced from the containing resource or reference back to it.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the HealthcareService resource is contained within another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-025
**ID**: 25
**Summary**: If a HealthcareService resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (contained.meta.versionId.empty() and contained.meta.lastUpdated.empty())"
**Context**: This invariant (dom-4) prevents contained resources from having version metadata, as versioning is managed at the containing resource level.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the HealthcareService resource is contained within another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-026
**ID**: 26
**Summary**: If a HealthcareService resource is contained in another resource, it SHALL NOT have a security label
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label (contained.meta.security.empty())"
**Context**: This invariant (dom-5) prevents contained resources from having their own security labels, as security is managed at the containing resource level.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the HealthcareService resource is contained within another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-027
**ID**: 27
**Summary**: Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)."
**Context**: This requirement ensures that modifier extensions only modify understanding within their specific context and do not alter the fundamental meaning of standard resource elements.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService

---

# REQ-028
**ID**: 28
**Summary**: If no new patients are accepted in the newpatients extension, no characteristics are allowed
**Requirement**: "If no new patients are accepted, no characteristics are allowed (extension.where(url='acceptingPatients').value.ofType(CodeableConcept).coding.where(code = 'no') implies extension.where(url='characteristics').empty())"
**Context**: This invariant (new-patients-characteristics) for the newpatients extension ensures that when new patients are not being accepted, no patient characteristics can be specified.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the acceptingPatients sub-element of the newpatients extension has a value indicating no new patients are accepted.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions
**Grouping**: HealthcareService
