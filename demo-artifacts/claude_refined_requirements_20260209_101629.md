# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

# REQ-001
**ID**: 01
**Summary**: Server SHALL support search parameter 'type' on Organization resource
**Requirement**: "Select Organizations of the specified type"
**Context**: The Plan-Net server must support searching for Organization resources using the 'type' search parameter of type token. This parameter searches on Organization.type and supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple values separated by comma where at least one must be true). Allowed modifier is 'text'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.43.1 SearchParameter: Plannet_sp_organization_type
**Grouping**: Organization

---

# REQ-002
**ID**: 02
**Summary**: Support for Organization endpoint search parameter with multipleAnd
**Requirement**: "The parameter may repeat in order to specify multiple values that must all be true"
**Context**: The organization-endpoint search parameter allows searching for Organization resources by endpoint. This requirement specifies that the server must support multiple repetitions of the endpoint parameter where all specified values must match (AND logic).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.39.1 SearchParameter: Plannet_sp_organization_endpoint
**Grouping**: Organization

---

# REQ-003
**ID**: 03
**Summary**: Support for Organization endpoint search parameter with multipleOr
**Requirement**: "The parameter may have multiple values (separated by comma) where at least one must be true"
**Context**: The organization-endpoint search parameter allows searching for Organization resources by endpoint. This requirement specifies that the server must support comma-separated values for the endpoint parameter where at least one value must match (OR logic).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.39.1 SearchParameter: Plannet_sp_organization_endpoint
**Grouping**: Organization

---

# REQ-004
**ID**: 04
**Summary**: Support search by period parameter on Organization resource
**Requirement**: "Select Organization entries available during the specified period"
**Context**: The Plannet_sp_organization_period search parameter allows searching for Organization resources available during a specified period. The search is based on the organization-period extension (http://hl7.org/fhir/StructureDefinition/organization-period). The parameter supports multipleOr (parameter may have multiple comma-separated values where at least one must be true), and it is up to the server whether multipleAnd is supported.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.42.1 SearchParameter: Plannet_sp_organization_period
**Grouping**: Organization

---

# REQ-005
**ID**: 05
**Summary**: Support search by partof parameter on Organization resource
**Requirement**: "Select Organizations that are part of the specified organization"
**Context**: The Plannet_sp_organization_partof search parameter allows searching for Organization resources that are part of a specified organization using the Organization.partOf element. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). Allowed chains are name, address, and type.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.41.1 SearchParameter: Plannet_sp_organization_partof
**Grouping**: Organization

---

# REQ-006
**ID**: 06
**Summary**: Health Plan API Actor SHALL support searching Organization by address parameter
**Requirement**: "Select organizations with the specified address (matches any of the string elements of an address) [using] Parameter `address`:`string` [with] Expression `Organization.address`"
**Context**: The SearchParameter Plannet_sp_organization_address defines a string-based search parameter for Organization resources based on the address element. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple comma-separated values where at least one must be true) semantics, with exact and contains modifiers allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.38.1 SearchParameter: Plannet_sp_organization_address
**Grouping**: Organization

---

# REQ-007
**ID**: 07
**Summary**: Server SHALL support coverage-area search parameter on Organization resource
**Requirement**: "Select health insurance provider networks available in a region described by the specified location [using the coverage-area search parameter on Organization resource with expression Organization.extension.where(url='http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference')]"
**Context**: The Plannet_sp_network_coverage_area SearchParameter defines a required search capability for Organization resources to filter health insurance provider networks by coverage area using a location reference. The parameter type is reference, targets Location resources, and supports both multipleAnd and multipleOr semantics.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.28.1 SearchParameter: Plannet_sp_network_coverage_area
**Grouping**: Organization

---

# REQ-008
**ID**: 08
**Summary**: Location Reference Extension URL Value
**Requirement**: "url [has cardinality] 1..1 [with fixed value] 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference'"
**Context**: The location-reference extension defines a reference to a Location resource (plannet-Location) that specifies the coverage area of a health insurance provider network. This extension may be used on Organization resources. The url element must be populated with the canonical URL of this extension definition.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the location-reference extension is used on an Organization resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.71.1 Extension: Location Reference - Differential View
**Grouping**: Organization

---

# REQ-009
**ID**: 09
**Summary**: Location Reference Extension Value Cardinality and Type
**Requirement**: "value[x] [has cardinality] 1..1 [and type] Reference([Plan-Net Location])"
**Context**: The location-reference extension defines a reference to a Location resource (plannet-Location) that specifies the coverage area of a health insurance provider network. This extension may be used on Organization resources. The value[x] element must contain exactly one reference to a Plan-Net Location resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the location-reference extension is used on an Organization resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.71.1 Extension: Location Reference - Differential View
**Grouping**: Organization

---

# REQ-010
**ID**: 10
**Summary**: Location Reference Extension Nested Extensions Prohibition
**Requirement**: "extension [has cardinality] 0..0"
**Context**: The location-reference extension is a simple extension that does not support nested extensions. When implementing this extension on Organization resources, no nested extensions are permitted within the location-reference extension structure.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the location-reference extension is used on an Organization resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.71.1 Extension: Location Reference - Differential View
**Grouping**: Organization

---

# REQ-011
**ID**: 11
**Summary**: OrgDescription Extension URL Definition
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement specifies that the Extension.url element must be a URI pointing to the structure definition for the org-description extension. The fixed value for this extension is http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---

# REQ-012
**ID**: 12
**Summary**: OrgDescription Extension Governance Requirements
**Requirement**: "There is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: This requirement mandates that when defining the org-description extension, implementers must adhere to governance requirements for extension definition and use within the FHIR specification framework.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---

# REQ-013
**ID**: 13
**Summary**: Server SHALL support search-type and read interactions on Organization resource
**Requirement**: "A Server SHALL support search-type, read [on Organization resource]."
**Context**: This requirement mandates support for search-type and read operations on the Organization resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---

# REQ-014
**ID**: 14
**Summary**: Server SHOULD support vread interaction on Organization resource
**Requirement**: "A Server SHOULD support vread [on Organization resource]."
**Context**: This requirement recommends support for version-specific read operations on the Organization resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---

# REQ-015
**ID**: 15
**Summary**: Server SHALL support returning Organization resource by id
**Requirement**: "A Server SHALL be capable of returning a Organization resource using: GET [base]/Organization/[id]"
**Context**: This requirement mandates the ability to retrieve a specific Organization resource by its logical id.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---

# REQ-016
**ID**: 16
**Summary**: Server SHOULD support returning Organization resource by version id
**Requirement**: "A Server SHOULD be capable of returning a Organization resource using: GET [base]/Organization/[id]/_history/vid"
**Context**: This requirement recommends the ability to retrieve a specific version of an Organization resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---

# REQ-017
**ID**: 17
**Summary**: Server SHALL support _include for Organization resources
**Requirement**: "A Server SHALL be capable of supporting the following _includes: Organization:partof, Organization:endpoint, Organization:coverage-area"
**Context**: This requirement mandates support for including referenced parent Organization, Endpoint, and coverage-area Location resources when searching for Organization resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---

# REQ-018
**ID**: 18
**Summary**: Server SHALL support _revinclude for Organization resources
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: Endpoint:organization, HealthcareService:organization, InsurancePlan:administered-by, InsurancePlan:owned-by, OrganizationAffiliation:primary-organization, PractitionerRole:organization, PractitionerRole:network, OrganizationAffiliation:participating-organization"
**Context**: This requirement mandates support for reverse includes to retrieve resources that reference an Organization, including Endpoint, HealthcareService, InsurancePlan, OrganizationAffiliation, and PractitionerRole resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---

# REQ-019
**ID**: 19
**Summary**: Server SHALL support search parameters on Organization resource
**Requirement**: "A Server SHALL support the following search parameters on Organization: partof, endpoint, address, name, _id, _lastUpdated, type, coverage-area"
**Context**: This requirement mandates support for searching Organization resources by parent organization, endpoint, address, name, id, last updated timestamp, organization type, and coverage area.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---

# REQ-020
**ID**: 20
**Summary**: OrganizationAffiliation SHALL contain either organization or participatingOrganization
**Requirement**: "PlannetOrganizationAffiliation.organization or PlannetOrganizationAffiliation.participatingOrganization (`organization.exists() or participatingOrganization.exists()`)"
**Context**: This is an invariant constraint on the PlannetOrganizationAffiliation profile that ensures at least one of the two key organization references is populated. This ensures that the affiliation relationship has at least one organization participant defined.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-021
**ID**: 21
**Summary**: OrganizationAffiliation.identifier.type element must support coded identifier types
**Requirement**: "OrganizationAffiliation.identifier.type [Must Support] true"
**Context**: The identifier.type element, which provides a coded type for the identifier, is marked as Must Support in the PlannetOrganizationAffiliation profile. This means systems claiming conformance must be capable of populating and processing this element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-022
**ID**: 22
**Summary**: OrganizationAffiliation.identifier.value element must be supported
**Requirement**: "OrganizationAffiliation.identifier.value [Must Support] true"
**Context**: The identifier.value element, which contains the actual identifier value, is marked as Must Support in the PlannetOrganizationAffiliation profile. This means systems claiming conformance must be capable of populating and processing this element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-023
**ID**: 23
**Summary**: OrganizationAffiliation.active element must be supported and has pattern value of true
**Requirement**: "OrganizationAffiliation.active [Must Support] true, Pattern Value `true`"
**Context**: The active element indicates whether the organization affiliation record is in active use and is marked as Must Support with a pattern value of true. Systems must support this element and should default to true when creating affiliations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-024
**ID**: 24
**Summary**: OrganizationAffiliation.period element must be supported
**Requirement**: "OrganizationAffiliation.period [Must Support] true"
**Context**: The period element, which defines the time period during which the participatingOrganization is affiliated with the primary organization, is marked as Must Support. This enables temporal tracking of affiliation relationships.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-025
**ID**: 25
**Summary**: OrganizationAffiliation.organization element must be supported and reference Plan-Net Organization
**Requirement**: "OrganizationAffiliation.organization [Type] Reference([Plan-Net Organization]), [Must Support] true"
**Context**: The organization element references the primary organization where the role is available and must conform to the Plan-Net Organization profile. This element is Must Support to ensure the primary organization in the affiliation relationship is captured.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-026
**ID**: 26
**Summary**: OrganizationAffiliation.participatingOrganization element must be supported and reference Plan-Net Organization
**Requirement**: "OrganizationAffiliation.participatingOrganization [Type] Reference([Plan-Net Organization]), [Must Support] true"
**Context**: The participatingOrganization element references the organization that provides/performs the role and must conform to the Plan-Net Organization profile. This element is Must Support to ensure the participating organization in the affiliation relationship is captured.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-027
**ID**: 27
**Summary**: OrganizationAffiliation.network element must be supported and reference Plan-Net Network
**Requirement**: "OrganizationAffiliation.network [Type] Reference([Plan-Net Network]), [Must Support] true"
**Context**: The network element references the health insurance provider network in which the participatingOrganization provides services and must conform to the Plan-Net Network profile. This element is Must Support to capture network associations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-028
**ID**: 28
**Summary**: OrganizationAffiliation.code element must be supported with extensible binding to OrganizationAffiliationRoleVS
**Requirement**: "OrganizationAffiliation.code [Binding] Unless not suitable, these codes SHALL be taken from [OrganizationAffiliation Roles]([extensible]), [Must Support] true"
**Context**: The code element defines the role the participatingOrganization plays in the association and must be bound to the OrganizationAffiliationRoleVS value set with extensible binding strength. This element is Must Support to ensure role categorization is captured.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-029
**ID**: 29
**Summary**: OrganizationAffiliation.specialty element must be supported with required binding to SpecialtiesVS
**Requirement**: "OrganizationAffiliation.specialty [Binding] The codes SHALL be taken from [Specialties VS]([required]), [Must Support] true"
**Context**: The specialty element captures the specific specialty of the participatingOrganization in the context of the role and must be bound to the SpecialtiesVS value set with required binding strength. This element is Must Support to ensure specialty information is captured.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-030
**ID**: 30
**Summary**: OrganizationAffiliation.location element must be supported and reference Plan-Net Location
**Requirement**: "OrganizationAffiliation.location [Type] Reference([Plan-Net Location]), [Must Support] true"
**Context**: The location element references the locations at which the role occurs and must conform to the Plan-Net Location profile. This element is Must Support to capture where the affiliation relationship is active.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-031
**ID**: 31
**Summary**: OrganizationAffiliation.healthcareService element must be supported and reference Plan-Net HealthcareService
**Requirement**: "OrganizationAffiliation.healthcareService [Type] Reference([Plan-Net HealthcareService]), [Must Support] true"
**Context**: The healthcareService element references healthcare services provided through the role and must conform to the Plan-Net HealthcareService profile. This element is Must Support to capture the services associated with the affiliation.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-032
**ID**: 32
**Summary**: OrganizationAffiliation.telecom element and its system, value, and rank sub-elements must be supported
**Requirement**: "OrganizationAffiliation.telecom [Must Support] true; OrganizationAffiliation.telecom.system [Must Support] true; OrganizationAffiliation.telecom.value [Must Support] true; OrganizationAffiliation.telecom.rank [Must Support] true"
**Context**: The telecom element provides contact details at the participatingOrganization relevant to the affiliation. The system, value, and rank sub-elements are all marked as Must Support to ensure complete contact information can be captured and prioritized.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-033
**ID**: 33
**Summary**: OrganizationAffiliation.endpoint element must be supported and reference Plan-Net Endpoint
**Requirement**: "OrganizationAffiliation.endpoint [Type] Reference([Plan-Net Endpoint]), [Must Support] true"
**Context**: The endpoint element references technical endpoints providing access to services operated for the affiliation role and must conform to the Plan-Net Endpoint profile. This element is Must Support to capture technical service access points.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: Organization

---

# REQ-034
**ID**: 34
**Summary**: Organization SHALL at least have a name or an identifier
**Requirement**: "The organization SHALL at least have a name or an identifier, and possibly more than one"
**Context**: This is a base FHIR constraint (org-1) applied to the PlannetNetwork profile. It ensures that every Organization resource representing a network has at least one means of identification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization invariant org-1
**Grouping**: Organization

---

# REQ-035
**ID**: 35
**Summary**: Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)."
**Context**: This requirement applies to the modifierExtension element of the Organization resource in the PlannetNetwork profile, ensuring that modifier extensions are used appropriately and do not alter the fundamental meaning of resource elements.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.modifierExtension
**Grouping**: Organization

---

# REQ-036
**ID**: 36
**Summary**: Organization.identifier.type binding conformance
**Requirement**: "Unless not suitable, these codes SHALL be taken from Identifier Type Codes"
**Context**: The identifier.type element for Organization in the PlannetNetwork profile should use codes from the Identifier Type Codes value set with extensible binding, meaning implementers should use these codes unless not suitable for their use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier.type
**Grouping**: Organization

---

# REQ-037
**ID**: 37
**Summary**: NPI identifier must be 10 digits
**Requirement**: "NPI must be 10 digits"
**Context**: When an NPI (National Provider Identifier) is provided in the Organization.identifier:NPI slice, it must conform to the format of exactly 10 digits as defined by invariant us-core-16.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If NPI identifier is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier:NPI invariant us-core-16
**Grouping**: Organization

---

# REQ-038
**ID**: 38
**Summary**: NPI check digit must be valid (Luhn algorithm)
**Requirement**: "NPI check digit must be valid (Luhn algorithm check)"
**Context**: When an NPI identifier is provided in the Organization.identifier:NPI slice, the check digit must be valid according to the Luhn algorithm as specified in invariant us-core-17.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If NPI identifier is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier:NPI invariant us-core-17
**Grouping**: Organization

---

# REQ-039
**ID**: 39
**Summary**: CLIA number must be 10 digits with letter D in third position
**Requirement**: "CLIA number must be 10 digits with a letter 'D' in third position"
**Context**: When a CLIA (Clinical Laboratory Improvement Amendments) identifier is provided in the Organization.identifier:CLIA slice, it must conform to the format of 10 digits with the letter 'D' in the third position as defined by invariant us-core-18.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If CLIA identifier is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier:CLIA invariant us-core-18
**Grouping**: Organization

---

# REQ-040
**ID**: 40
**Summary**: NAIC must be 5 digits
**Requirement**: "NAIC must be 5 digits"
**Context**: When a NAIC (National Association of Insurance Commissioners) identifier is provided in the Organization.identifier:NAIC slice, it must consist of exactly 5 digits as defined by invariant us-core-19.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If NAIC identifier is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier:NAIC invariant us-core-19
**Grouping**: Organization

---

# REQ-041
**ID**: 41
**Summary**: Organization.active must be true for PlannetNetwork
**Requirement**: "Whether the organization's record is still in active use" with Fixed Value `true`
**Context**: The PlannetNetwork profile constrains the Organization.active element to have a fixed value of true, meaning all network organization records must be active.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.active
**Grouping**: Organization

---

# REQ-042
**ID**: 42
**Summary**: Organization.type binding to Network Type VS
**Requirement**: "The codes SHALL be taken from Network Type VS"
**Context**: The Organization.type element for the PlannetNetwork profile must use codes from the Network Type VS value set (http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/NetworkTypeVS) with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.type
**Grouping**: Organization

---

# REQ-043
**ID**: 43
**Summary**: Organization telecom cannot be of use 'home'
**Requirement**: "The telecom of an organization can never be of use 'home'"
**Context**: The Organization.telecom element is constrained by invariant org-3 to prevent the use code 'home' from being used for organizational contact points, as this is not applicable to organizations.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If Organization.telecom is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.telecom invariant org-3
**Grouping**: Organization

---

# REQ-044
**ID**: 44
**Summary**: Organization address cannot be of use 'home'
**Requirement**: "An address of an organization can never be of use 'home'"
**Context**: The Organization.address element is constrained by invariant org-2 to prevent the use code 'home' from being used for organizational addresses, as this is not applicable to organizations.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If Organization.address is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.address invariant org-2
**Grouping**: Organization

---

# REQ-045
**ID**: 45
**Summary**: Organization.address.state binding to USPS state codes
**Requirement**: "Unless not suitable, these codes SHALL be taken from USPS Two Letter Alphabetic Codes"
**Context**: The Organization.address.state element should use codes from the USPS Two Letter Alphabetic Codes value set with extensible binding, representing standard two-letter US state abbreviations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.address.state
**Grouping**: Organization

---

# REQ-046
**ID**: 46
**Summary**: Plan-Net Network Organization active element must be true
**Requirement**: "[The Plan-Net Network Organization] active [element has a] Fixed Value: true"
**Context**: The Plan-Net Network profile constrains the Organization resource to represent healthcare provider insurance networks. The active element indicates whether the organization's record is still in active use. This requirement mandates that all Plan-Net Network Organization instances must have the active flag set to true.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: Plan-Net Network
**Grouping**: Organization

---

# REQ-047
**ID**: 47
**Summary**: Plan-Net Network Organization type must be from NetworkTypeVS value set
**Requirement**: "[The Plan-Net Network Organization] type [element has cardinality] 1.1 [and] Binding: Network Type VS ([required])"
**Context**: The type element identifies the kind of organization. For Plan-Net Network Organizations, this must be a value from the NetworkTypeVS value set to properly classify the type of healthcare provider insurance network. The required binding strength means implementations must use a code from this value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: Plan-Net Network
**Grouping**: Organization

---

# REQ-048
**ID**: 48
**Summary**: Plan-Net Network Organization must have a partOf reference to Plan-Net Organization
**Requirement**: "[The Plan-Net Network Organization] partOf [element has cardinality] 1.1 [and type] Reference(Plan-Net Organization) [and description] The organization that manages this network"
**Context**: The partOf element establishes the relationship between the network and the managing organization (typically a payer). This is a mandatory element that must reference a Plan-Net Organization resource, establishing the ownership/management relationship of the network.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile: Plan-Net Network
**Grouping**: Organization

---

# REQ-049
**ID**: 49
**Summary**: Organization contained resources SHALL NOT contain nested Resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources"
**Context**: This is a general FHIR constraint (dom-2) that applies to the Organization resource when it is contained within another resource. It prevents recursive containment of resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the Organization resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions, Organization element (0)
**Grouping**: Organization

---

# REQ-050
**ID**: 50
**Summary**: Organization contained resources SHALL be referenced from elsewhere or refer to containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This is a general FHIR constraint (dom-3) ensuring that contained resources have a purpose and are actually used within the parent resource structure.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the Organization resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions, Organization element (0)
**Grouping**: Organization

---

# REQ-051
**ID**: 51
**Summary**: Organization contained resources SHALL NOT have meta.versionId or meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated"
**Context**: This is a general FHIR constraint (dom-4) that prevents versioning metadata on contained resources, as contained resources are managed as part of their containing resource.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the Organization resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions, Organization element (0)
**Grouping**: Organization

---

# REQ-052
**ID**: 52
**Summary**: Organization contained resources SHALL NOT have security labels
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label"
**Context**: This is a general FHIR constraint (dom-5) preventing security labels on contained resources, as security is managed at the containing resource level.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the Organization resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions, Organization element (0)
**Grouping**: Organization

---

# REQ-053
**ID**: 53
**Summary**: Organization identifier value SHALL be urn:ietf:rfc:3986 if value is full URI
**Requirement**: "If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986"
**Context**: This requirement ensures proper representation of URI-based identifiers by requiring the appropriate system value when an identifier value is expressed as a full URI.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the identifier value is a full URI
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions, Organization.identifier.value element (22)
**Grouping**: Organization

---

# REQ-054
**ID**: 54
**Summary**: Organization address updating SHALL ensure text matches parts
**Requirement**: "Applications updating an address SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part"
**Context**: This requirement ensures consistency between the text representation and structured parts of an address, preventing discrepancies that could lead to confusion or errors.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when both text and structured address parts are present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions, Organization.address.text element (58)
**Grouping**: Organization

---

# REQ-055
**ID**: 55
**Summary**: Organization resource SHALL have active status set to true
**Requirement**: "Organization.active [is required with] Required Pattern: true"
**Context**: The Plan-Net Organization profile mandates that the active element must be present with a cardinality of 1..1 and must have the value of true, indicating the organization's record is in active use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile
**Grouping**: Organization

---

# REQ-056
**ID**: 56
**Summary**: Organization resource SHALL have at least one organization type
**Requirement**: "Organization.type [has cardinality] 1..*" and "The kind(s) of organization that this is."
**Context**: The Plan-Net Organization profile requires that every organization must have at least one type specified from the OrgTypeVS value set with extensible binding.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile
**Grouping**: Organization

---

# REQ-057
**ID**: 57
**Summary**: Organization resource SHALL have a name
**Requirement**: "Organization.name [has cardinality] 1..1" and "A name associated with the organization."
**Context**: The Plan-Net Organization profile requires that every organization must have exactly one name specified.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile
**Grouping**: Organization

---

# REQ-058
**ID**: 58
**Summary**: Organization resource SHALL have at least one address
**Requirement**: "Organization.address [has cardinality] 1..*" and "An address for the organization."
**Context**: The Plan-Net Organization profile requires that every organization must have at least one address specified.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile
**Grouping**: Organization

---

# REQ-059
**ID**: 59
**Summary**: NPI identifier system SHALL be http://hl7.org/fhir/sid/us-npi
**Requirement**: "Organization.identifier:NPI [has] system [with] Fixed Value: http://hl7.org/fhir/sid/us-npi"
**Context**: When providing an NPI identifier for an organization, the system element must be set to the fixed value 'http://hl7.org/fhir/sid/us-npi' with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies only if an NPI identifier slice is used
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile
**Grouping**: Organization

---

# REQ-060
**ID**: 60
**Summary**: CLIA identifier system SHALL be urn:oid:2.16.840.1.113883.4.7
**Requirement**: "Organization.identifier:CLIA [has] system [with] Fixed Value: urn:oid:2.16.840.1.113883.4.7"
**Context**: When providing a CLIA identifier for an organization, the system element must be set to the fixed value 'urn:oid:2.16.840.1.113883.4.7' with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies only if a CLIA identifier slice is used
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile
**Grouping**: Organization

---

# REQ-061
**ID**: 61
**Summary**: NAIC identifier system SHALL be urn:oid:2.16.840.1.113883.6.300
**Requirement**: "Organization.identifier:NAIC [has] system [with] Fixed Value: urn:oid:2.16.840.1.113883.6.300"
**Context**: When providing a NAIC identifier for an organization, the system element must be set to the fixed value 'urn:oid:2.16.840.1.113883.6.300' with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies only if a NAIC identifier slice is used
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile
**Grouping**: Organization
