# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: InsurancePlan search parameter support for name
**Requirement**: "Select products with the specified name using Parameter `name`:`string` [with] Expression `name | alias`"
**Context**: This requirement defines a search parameter for the InsurancePlan resource that allows searching by product name or alias. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple values separated by comma where at least one must be true). Allowed modifiers are exact and contains.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.15.1 SearchParameter: Plannet_sp_insuranceplan_name
**Grouping**: General/Cross-Resource

---
# REQ-002
**ID**: 02
**Summary**: Support for InsurancePlan type search parameter
**Requirement**: "Select insurance plans of the specified type [using Parameter `type`:`token` on Resource InsurancePlan with Expression `InsurancePlan.type`]"
**Context**: This search parameter allows filtering of InsurancePlan resources by their type element. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The text modifier is allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.19.1 SearchParameter: Plannet_sp_insuranceplan_type
**Grouping**: General/Cross-Resource

---
# REQ-003
**ID**: 03
**Summary**: Server SHALL support plan-type search parameter on InsurancePlan resource
**Requirement**: "Select plans of the specified type"
**Context**: The Plan-Net Implementation Guide defines a search parameter `plan-type` of type `token` that enables searching for InsurancePlan resources based on their plan type. The expression used is `InsurancePlan.plan.type`. This search parameter supports multipleAnd (the parameter may repeat to specify multiple values that must all be true) and multipleOr (the parameter may have multiple values separated by comma where at least one must be true). The allowed modifier is: text.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.18.1 SearchParameter: Plannet_sp_insuranceplan_plan_type
**Grouping**: General/Cross-Resource

---
# REQ-004
**ID**: 04
**Summary**: Server SHALL support network search parameter on InsurancePlan resource
**Requirement**: "Select Organization entries in a given InsurancePlan's network"
**Context**: The Plan-Net Implementation Guide defines a search parameter `network` of type `reference` that enables searching for InsurancePlan resources based on their network organizations. The expression used is `InsurancePlan.network`. This search parameter supports multipleOr (the parameter may have multiple values separated by comma where at least one must be true). For multipleAnd, it's up to the server whether the parameter may repeat to specify multiple values that must all be true.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.16.1 SearchParameter: Plannet_sp_insuranceplan_network
**Grouping**: General/Cross-Resource

---
# REQ-005
**ID**: 05
**Summary**: Server SHALL support search by name on HealthcareService resource
**Requirement**: "Select HealthcareServices with the specified name [using parameter `name`:`string` with Expression `HealthcareService.name`]"
**Context**: The Plannet_sp_healthcareservice_name search parameter enables searching for HealthcareService resources by the service name. The search supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The exact and contains modifiers are allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.8.1 SearchParameter: Plannet_sp_healthcareservice_name
**Grouping**: General/Cross-Resource

---
# REQ-006
**ID**: 06
**Summary**: InsurancePlan identifier search parameter support
**Requirement**: "Select products with the specified identifier [using search parameter `identifier`:`token` on InsurancePlan resource with Expression `InsurancePlan.identifier`]"
**Context**: The implementation guide defines a search parameter for InsurancePlan resources that allows searching by identifier. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). Allowed modifiers are text and of-type.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.14.1 SearchParameter: Plannet_sp_insuranceplan_identifier
**Grouping**: General/Cross-Resource

---
# REQ-007
**ID**: 07
**Summary**: Health Plan API Actor SHALL support service-type search parameter on HealthcareService resource
**Requirement**: "Select HealthcareServices of the specified type [using] Parameter `service-type`:`token` [with] Expression `HealthcareService.type`"
**Context**: This search parameter allows querying HealthcareService resources by their service type using a token-based search. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (comma-separated values where at least one must be true). The text modifier is allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.11.1 SearchParameter: Plannet_sp_healthcareservice_type
**Grouping**: General/Cross-Resource

---
# REQ-008
**ID**: 08
**Summary**: Health Plan API Actor SHALL support organization search parameter on Endpoint resource
**Requirement**: "Select Endpoints managed by the specified organization [using] Parameter `organization`:`reference` [with] Expression `Endpoint.managingOrganization`"
**Context**: This search parameter allows querying Endpoint resources by their managing organization using a reference-based search. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (comma-separated values where at least one must be true). Allowed chains include: name, address, partof, type.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.2.1 SearchParameter: Plannet_sp_endpoint_organization
**Grouping**: General/Cross-Resource

---
# REQ-009
**ID**: 09
**Summary**: Health Plan API Actor SHALL support searching InsurancePlan by owned-by parameter
**Requirement**: "Select products that are owned by the specified organization" using the search parameter `owned-by` of type `reference` on the InsurancePlan resource with expression `InsurancePlan.ownedBy` targeting Organization resources
**Context**: The SearchParameter definition Plannet_sp_insuranceplan_owned_by specifies that servers must support searching for InsurancePlan resources by the owned-by search parameter. This parameter is of type reference and uses the expression InsurancePlan.ownedBy, targeting Organization resources. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple comma-separated values where at least one must be true), with chains allowed for name and partof.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.17.1 SearchParameter: Plannet_sp_insuranceplan_owned_by
**Grouping**: General/Cross-Resource

---
# REQ-010
**ID**: 10
**Summary**: Support search by role parameter on OrganizationAffiliation resource
**Requirement**: "[Server SHALL] Select OrganizationAffiliations with the specified role [using parameter `role`:`token` with Expression `OrganizationAffiliation.code`]"
**Context**: This search parameter enables querying OrganizationAffiliation resources by their role code. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The text modifier is allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.35.1 SearchParameter: Plannet_sp_organizationaffiliation_role
**Grouping**: General/Cross-Resource

---
# REQ-011
**ID**: 11
**Summary**: Support search by coverage-area parameter on InsurancePlan resource
**Requirement**: "[Server SHALL] Select products that are offered in the specified location [using parameter `coverage-area`:`reference` with Expression `InsurancePlan.coverageArea` targeting Location resources]"
**Context**: This search parameter enables querying InsurancePlan resources by their coverage area, which references Location resources. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.13.1 SearchParameter: Plannet_sp_insuranceplan_coverage_area
**Grouping**: General/Cross-Resource

---
# REQ-012
**ID**: 12
**Summary**: Support search by service-category parameter on HealthcareService resource
**Requirement**: "[Server SHALL] Select HealthcareServices providing the specified category of services [using parameter `service-category`:`token` with Expression `HealthcareService.category`]"
**Context**: This search parameter enables querying HealthcareService resources by their service category. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The text modifier is allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.3.1 SearchParameter: Plannet_sp_healthcareservice_category
**Grouping**: General/Cross-Resource

---
# REQ-013
**ID**: 13
**Summary**: Support search by endpoint parameter on HealthcareService resource
**Requirement**: "[Server SHALL] Select HealthcareServices with the specified endpoint [using parameter `endpoint`:`reference` with Expression `HealthcareService.endpoint` targeting Endpoint resources]"
**Context**: This search parameter enables querying HealthcareService resources by their associated endpoint. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The organization chain parameter is allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.6.1 SearchParameter: Plannet_sp_healthcareservice_endpoint
**Grouping**: General/Cross-Resource

---
# REQ-014
**ID**: 14
**Summary**: Plan-Net Server SHALL support search parameter 'administered-by' on InsurancePlan resource
**Requirement**: "Parameter `administered-by`:`reference` - Select products that are administered by the specified organization. Resource [InsurancePlan]. Expression `InsurancePlan.administeredBy`. The parameter may repeat in order to specify multiple values that must all be true (multipleAnd). The parameter may have multiple values (separated by comma) where at least one must be true (multipleOr). Chains Allowed: name, partof"
**Context**: This search parameter enables querying InsurancePlan resources by the organization that administers them. The parameter supports both multipleAnd and multipleOr semantics, and allows chaining to search by organization characteristics such as name and partof.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.12.1 SearchParameter: Plannet_sp_insuranceplan_administered_by
**Grouping**: General/Cross-Resource

---
# REQ-015
**ID**: 15
**Summary**: Server SHALL support endpoint search parameter on OrganizationAffiliation resource
**Requirement**: "Select OrganizationAffiliations with the specified endpoint [using the endpoint search parameter]"
**Context**: The Plannet_sp_organizationaffiliation_endpoint search parameter enables searching for OrganizationAffiliation resources by endpoint. The parameter is of type reference and uses the expression `OrganizationAffiliation.endpoint` to target Endpoint resources. The parameter supports both multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The parameter allows chaining on the organization element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.29.1 SearchParameter: Plannet_sp_organizationaffiliation_endpoint
**Grouping**: General/Cross-Resource

---
# REQ-016
**ID**: 16
**Summary**: Server SHALL support delivery-method search parameter on HealthcareService resource
**Requirement**: "Select HealthcareServices based on the delivery method type [using the delivery-method search parameter]"
**Context**: The Plannet_sp_healthcareservice_delivery_method search parameter enables searching for HealthcareService resources by delivery method type. The parameter is of type token and uses the expression `HealthcareService.extension.where(url='http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method').extension.where(url='type')`. The parameter supports both multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.5.1 SearchParameter: Plannet_sp_healthcareservice_delivery_method
**Grouping**: General/Cross-Resource

---
# REQ-017
**ID**: 17
**Summary**: Server SHALL support service search parameter on OrganizationAffiliation resource
**Requirement**: "Select OrganizationAffiliations providing the specified service [using the service search parameter]"
**Context**: The Plannet_sp_organizationaffiliation_service search parameter enables searching for OrganizationAffiliation resources by the healthcare service they provide. The parameter is of type reference and uses the expression `OrganizationAffiliation.healthcareService` to target HealthcareService resources. The parameter supports both multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The parameter allows chaining on service-category, organization, and location elements.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.36.1 SearchParameter: Plannet_sp_organizationaffiliation_service
**Grouping**: General/Cross-Resource

---
# REQ-018
**ID**: 18
**Summary**: Support for network search parameter on OrganizationAffiliation resource
**Requirement**: "Parameter `network`:`reference` - Select roles where the organization is a member of the specified health insurance provider network. Expression: `OrganizationAffiliation.network`. The parameter may repeat in order to specify multiple values that must all be true (multipleAnd). The parameter may have multiple values (separated by comma) where at least one must be true (multipleOr). Chains Allowed: name, partof"
**Context**: This search parameter enables searching OrganizationAffiliation resources by the health insurance provider network to which the organization belongs. The network is directly referenced in the OrganizationAffiliation resource. The search supports both AND and OR combinations of multiple values, as well as chained searches on related Organization attributes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.31.1 SearchParameter: Plannet_sp_organizationaffiliation_network
**Grouping**: General/Cross-Resource

---
# REQ-019
**ID**: 19
**Summary**: Support for location search parameter on OrganizationAffiliation resource
**Requirement**: "Parameter `location`:`reference` - Select OrganizationAffiliations available at the specified location. Expression: `OrganizationAffiliation.location`. The parameter may repeat in order to specify multiple values that must all be true (multipleAnd). The parameter may have multiple values (separated by comma) where at least one must be true (multipleOr). Chains Allowed: address, address-postalcode, address-city, address-state, organization, type"
**Context**: This search parameter enables searching OrganizationAffiliation resources by the location where the affiliation is available. The location is directly referenced in the OrganizationAffiliation resource. The search supports both AND and OR combinations of multiple values, as well as chained searches on Location and Organization attributes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.30.1 SearchParameter: Plannet_sp_organizationaffiliation_location
**Grouping**: General/Cross-Resource

---
# REQ-020
**ID**: 20
**Summary**: Health Plan API SHALL conform to HRex conformance expectations
**Requirement**: "All systems claiming conformance to this guide **SHALL** conform to the requirements listed in [the Health Record Exchange (Hrex) Conformance Expectations] section."
**Context**: This requirement establishes that all systems implementing the Plan-Net IG must meet the baseline conformance expectations defined in the Da Vinci HRex IG Conformance Expectations section.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: HRex IG Conformance Expectations (external reference)
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 4.1 Conformance Expectations
**Grouping**: General/Cross-Resource

---
# REQ-021
**ID**: 21
**Summary**: Health Plan API SHALL populate all Must Support data elements
**Requirement**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Context**: This requirement establishes that Health Plan API systems must be able to populate all data elements marked as Must Support in Plan-Net profiles when returning query results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.1 Health Plan API Requirements
**Grouping**: General/Cross-Resource

---
# REQ-022
**ID**: 22
**Summary**: Health Plan API SHALL NOT include Must Support elements with minimum cardinality 0 when data is not present
**Requirement**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Context**: This requirement specifies that when a Must Support element with minimum cardinality of 0 has no data available, the Health Plan API must omit that element from the returned resource instance rather than including it with a null or empty value.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When information on a particular Must Support data element is not present and the minimum cardinality is 0
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.1 Health Plan API Requirements
**Grouping**: General/Cross-Resource

---
# REQ-023
**ID**: 23
**Summary**: Health Plan API SHALL send reason for missing information when minimum cardinality >0
**Requirement**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 [Health Plan API actors] **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Context**: This requirement mandates that when a data element with minimum cardinality greater than 0 has no data available, the Health Plan API must provide a reason for the missing data using appropriate coding systems or the dataAbsentReason extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When information on a particular data element is not present and the minimum cardinality is >0
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.1 Health Plan API Requirements
**Grouping**: General/Cross-Resource

---
# REQ-024
**ID**: 24
**Summary**: Application SHALL process Must Support data elements without error
**Requirement**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Context**: This requirement establishes that Application actors must be able to successfully process resources containing all Must Support data elements defined in Plan-Net profiles without experiencing errors or failures.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.2 Application Requirements
**Grouping**: General/Cross-Resource

---
# REQ-025
**ID**: 25
**Summary**: Application SHOULD display or store Must Support data elements
**Requirement**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Context**: This requirement recommends that Application actors should have the capability to either display Must Support data elements to users or persist them for future use, though this is not mandatory.
**Conformance**: SHOULD
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 4.2.2 Application Requirements
**Grouping**: General/Cross-Resource

---
# REQ-026
**ID**: 26
**Summary**: Application SHALL interpret missing Must Support elements as data not present
**Requirement**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Context**: This requirement specifies that when Application actors receive resources from Health Plan API actors with missing Must Support elements, they must interpret this absence as indicating the data does not exist in the source system, rather than as an error or incomplete response.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 4.2.2 Application Requirements
**Grouping**: General/Cross-Resource

---
# REQ-027
**ID**: 27
**Summary**: Application SHALL process Must Support elements asserting missing information
**Requirement**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information."
**Context**: This requirement mandates that Application actors must be capable of successfully processing resources where Must Support data elements explicitly assert that information is missing (e.g., through dataAbsentReason or nullFlavors), distinguishing this from elements that are simply omitted.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.2 Application Requirements
**Grouping**: General/Cross-Resource

---
# REQ-028
**ID**: 28
**Summary**: Accessibility extension value[x] SHALL use codes from AccessibilityVS value set
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Accessibility VS]"
**Context**: The accessibility extension is used to describe accessibility options offered by a practitioner or at a location. The value[x] element of this extension has an extensible binding to the AccessibilityVS value set, meaning implementations SHALL use codes from this value set unless not suitable for their use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: The requirement is conditional - codes SHALL be taken from the specified value set "unless not suitable"
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.66.1 Extension: Accessibility - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-029
**ID**: 29
**Summary**: Accessibility extension URL SHALL be the defined URI
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The Extension.url element identifies the meaning of the extension and must point to the structure definition. For the accessibility extension, this URL has a fixed value of http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.66.1 Extension: Accessibility - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-030
**ID**: 30
**Summary**: ViaIntermediary Extension url must have fixed value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The via-intermediary extension is used to provide a reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for an organization. The Extension.url element must contain the fixed value `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary` to properly identify this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-031
**ID**: 31
**Summary**: ViaIntermediary Extension value[x] element must have a value
**Requirement**: "Extension.value[x] [must have] [Control] 1.1"
**Context**: The via-intermediary extension must include a value element with cardinality of 1..1, meaning it is required and must contain exactly one value. This value must be a Reference to one of the specified Plan-Net profile types (PractitionerRole, OrganizationAffiliation, Location, or Organization) and is marked as Must Support.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-032
**ID**: 32
**Summary**: ViaIntermediary Extension must satisfy ext-1 invariant
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: The via-intermediary extension must conform to the ext-1 invariant which ensures that an extension has either nested extensions or a value element, but not both simultaneously. This is a fundamental FHIR constraint for extension structure.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-033
**ID**: 33
**Summary**: ViaIntermediary Extension must satisfy ele-1 invariant
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: All elements within the via-intermediary extension must satisfy the ele-1 invariant, which requires that every FHIR element must have either a value attribute or child elements (beyond just an id). This applies to the Extension element itself, Extension.extension, Extension.value[x], and other nested elements.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-034
**ID**: 34
**Summary**: Delivery Method Extension SHALL include type sub-extension
**Requirement**: "extension:type [cardinality] 1.1"
**Context**: The Delivery Method extension is a complex extension that describes the service delivery method for HealthcareService resources. The extension has two sub-extensions: type (which is mandatory) and virtualModalities (which is optional). The type sub-extension indicates whether service delivery is physical or virtual.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When the Delivery Method extension is used on a HealthcareService resource, the type sub-extension must be present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: Delivery Method - Differential Table
**Grouping**: General/Cross-Resource

---
# REQ-035
**ID**: 35
**Summary**: Delivery Method type sub-extension SHALL use required binding to DeliveryMethodVS
**Requirement**: "value[x] [for extension:type] 1.1 CodeableConcept Binding: Delivery Methods VS ([required])"
**Context**: The type sub-extension of the Delivery Method extension must contain a CodeableConcept value that is bound to the DeliveryMethodVS value set with required conformance. This ensures that only valid codes from the Delivery Methods code system are used to indicate whether service delivery is physical or virtual.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When the Delivery Method extension type sub-extension is populated, it must use a code from the DeliveryMethodVS value set.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: Delivery Method - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-036
**ID**: 36
**Summary**: Delivery Method virtualModalities sub-extension SHALL use extensible binding to VirtualModalitiesVS when present
**Requirement**: "value[x] [for extension:virtualModalities] 1.1 CodeableConcept Binding: Virtual Modalities VS ([extensible])"
**Context**: The virtualModalities sub-extension of the Delivery Method extension, when present, must contain a CodeableConcept value that is bound to the VirtualModalitiesVS value set with extensible conformance. This extension specifies the modalities of virtual delivery when service delivery is virtual. The extensible binding allows for alternate codings if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When the Delivery Method extension virtualModalities sub-extension is populated, it should use a code from the VirtualModalitiesVS value set if applicable, but may use alternate codings if the value set does not cover the concept.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: Delivery Method - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-037
**ID**: 37
**Summary**: DaysOfWeek value binding requirement for contactpoint-availabletime extension
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [DaysOfWeek (http://hl7.org/fhir/ValueSet/days-of-week)]"
**Context**: The contactpoint-availabletime extension includes a daysOfWeek sub-extension that represents the days of the week when a contact point is available. This extension is used on ContactPoint elements within resources such as HealthcareService, Location, Network, Organization, Practitioner, and PractitionerRole profiles. The daysOfWeek value must be bound to the standard FHIR DaysOfWeek value set with required conformance, ensuring consistent representation of weekday values across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-038
**ID**: 38
**Summary**: New Patients Extension - Accepting Patients Sub-Extension Cardinality
**Requirement**: "extension:acceptingPatients [SHALL have cardinality] 1..1"
**Context**: The New Patients extension is a complex extension used in PractitionerRole, HealthcareService, and Location profiles to indicate whether new patients are being accepted in general or from a specific network. The acceptingPatients sub-extension is mandatory and must appear exactly once.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients - Differential View
**Grouping**: General/Cross-Resource

---
# REQ-039
**ID**: 39
**Summary**: New Patients Extension - Accepting Patients Value Binding
**Requirement**: "extension:acceptingPatients.value[x] [SHALL be bound to] Accepting Patients Codes VS (required)"
**Context**: The acceptingPatients sub-extension value must be a CodeableConcept conforming to the AcceptingPatientsVS value set with required binding strength, ensuring interoperable representation of whether new patients are being accepted.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-040
**ID**: 40
**Summary**: New Patients Extension - From Network Sub-Extension Cardinality
**Requirement**: "extension:fromNetwork [SHALL have cardinality] 0..1"
**Context**: The fromNetwork sub-extension is optional within the New Patients extension and, when present, must reference a Plan-Net Network resource to specify which network the new patient acceptance applies to.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients - Differential View
**Grouping**: General/Cross-Resource

---
# REQ-041
**ID**: 41
**Summary**: New Patients Extension - Characteristics Constraint
**Requirement**: "If no new patients are accepted, no characteristics are allowed: extension.where(url='acceptingPatients').value.ofType(CodeableConcept).coding.where(code = 'no') implies extension.where(url='characteristics').empty()"
**Context**: This constraint ensures logical consistency within the New Patients extension by prohibiting the specification of patient characteristics when the provider is not accepting new patients. The constraint is enforced through FHIRPath expression validation.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: The constraint applies when the acceptingPatients code is 'no'
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1.1.2 Constraints
**Grouping**: General/Cross-Resource

---
# REQ-042
**ID**: 42
**Summary**: Qualification Extension Code Element SHALL be CodeableConcept from Specified ValueSet
**Requirement**: "[The] extension:code.value[x] [SHALL be a] CodeableConcept [and] to be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated."
**Context**: The qualification extension includes a mandatory 'code' sub-extension (cardinality 1..1) that identifies the type of qualification. This code element must use a CodeableConcept data type and must be drawn from the SpecialtyAndDegreeLicenseCertificateVS value set with extensible binding, meaning that if the value set covers the concept, a code from that value set SHALL be used.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when any of the codes within the SpecialtyAndDegreeLicenseCertificateVS value set can apply to the concept being communicated.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1.1.1 Terminology Bindings - Extension.extension:code.value[x]
**Grouping**: General/Cross-Resource

---
# REQ-043
**ID**: 43
**Summary**: Qualification Extension Status Element SHALL be from Required ValueSet
**Requirement**: "[The] extension:status.value[x] [binding is] required [meaning] to be conformant, the concept in this element SHALL be from the specified value set [QualificationStatusVS]."
**Context**: The qualification extension includes a mandatory 'status' sub-extension (cardinality 1..1) that indicates the status of the qualification. This status element uses required binding to the QualificationStatusVS value set and has a fixed value of 'active', meaning implementations must use a code from this value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1.1.1 Terminology Bindings - Extension.extension:status.value[x]
**Grouping**: General/Cross-Resource

---
# REQ-044
**ID**: 44
**Summary**: Qualification Extension WhereValid Element SHALL be from Required USPS State ValueSet
**Requirement**: "[The] extension:whereValid.value[x] [binding is] required [meaning] to be conformant, the concept in this element SHALL be from the specified value set [USPS Two Letter Alphabetic Codes]."
**Context**: The qualification extension includes an optional 'whereValid' sub-extension (cardinality 0..*) that indicates where the qualification is valid, either as a state code or location reference. When a CodeableConcept is used for this element, it must use required binding to the US Core USPS state value set, meaning only valid USPS two-letter state codes are permitted.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1.1.1 Terminology Bindings - Extension.extension:whereValid.value[x]
**Grouping**: General/Cross-Resource

---
# REQ-045
**ID**: 45
**Summary**: Extension.extension:type cardinality requirement
**Requirement**: "Extension.extension:type [Control]: 1.1"
**Context**: This requirement specifies that the 'type' extension within the EndpointUsecase extension must have a cardinality of exactly 1..1, meaning it is mandatory and must appear exactly once. The type extension provides "An indication of the type of services supported by the endpoint".
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-046
**ID**: 46
**Summary**: Extension.extension:type Must Support requirement
**Requirement**: "Extension.extension:type [Must Support]: true"
**Context**: This requirement specifies that the 'type' extension within the EndpointUsecase extension must be supported by implementations. This indicates that systems claiming conformance to this profile must be capable of populating and processing this element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-047
**ID**: 47
**Summary**: Extension.extension:type.value[x] binding requirement
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Endpoint Usecases VS] (extensible to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/EndpointUsecaseVS`)"
**Context**: This requirement specifies that the value for the type extension must use codes from the Endpoint Usecases VS value set, with extensible binding strength. The extensible binding means that codes should come from the specified value set unless no suitable code exists, in which case other codes may be used.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when a suitable code exists in the value set
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-048
**ID**: 48
**Summary**: Extension.extension:type.value[x] cardinality requirement
**Requirement**: "Extension.extension:type.value[x] [Control]: 1.1"
**Context**: This requirement specifies that the value element of the type extension must have a cardinality of exactly 1..1, meaning it is mandatory and must appear exactly once. The value must be of type CodeableConcept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-049
**ID**: 49
**Summary**: Extension.extension:standard cardinality requirement
**Requirement**: "Extension.extension:standard [Control]: 0.1"
**Context**: This requirement specifies that the 'standard' extension within the EndpointUsecase extension must have a cardinality of 0..1, meaning it is optional but if present must appear at most once. The standard extension provides "A URI to a published standard describing the services supported by the endpoint (e.g. an HL7 implementation guide)".
**Conformance**: MAY
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-050
**ID**: 50
**Summary**: Extension.extension:standard Must Support requirement
**Requirement**: "Extension.extension:standard [Must Support]: true"
**Context**: This requirement specifies that the 'standard' extension within the EndpointUsecase extension must be supported by implementations. This indicates that systems claiming conformance to this profile must be capable of populating and processing this element when present.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-051
**ID**: 51
**Summary**: Extension.extension:standard.value[x] cardinality requirement
**Requirement**: "Extension.extension:standard.value[x] [Control]: 1.1"
**Context**: This requirement specifies that when the standard extension is present, its value element must have a cardinality of exactly 1..1, meaning it is mandatory and must appear exactly once. The value must be of type uri.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when the standard extension is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-052
**ID**: 52
**Summary**: Extension.url fixed value requirement
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension [with Fixed Value: `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase`]"
**Context**: This requirement specifies that the url element of the Extension must be fixed to the specific value 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase'. This identifies the extension definition being used.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-053
**ID**: 53
**Summary**: Extension.extension invariant ext-1 requirement
**Requirement**: "Must have either extensions or value[x], not both (`extension.exists() != value.exists()`)"
**Context**: This requirement specifies that the Extension.extension element must satisfy the invariant ext-1, which ensures that an extension cannot have both nested extensions and a direct value - it must have one or the other but not both.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-054
**ID**: 54
**Summary**: Extension invariant ele-1 requirement
**Requirement**: "All FHIR elements must have a @value or children (`hasValue() or (children().count() > id.count())`)"
**Context**: This requirement specifies that all Extension elements must satisfy the invariant ele-1, which ensures that every FHIR element must have either a value attribute or child elements (excluding the id).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-055
**ID**: 55
**Summary**: Delivery method extension type value SHALL use required value set
**Requirement**: "The codes SHALL be taken from [Delivery Methods VS](ValueSet-DeliveryMethodVS.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/DeliveryMethodVS`)"
**Context**: The delivery-method extension includes a 'type' sub-extension that indicates whether service delivery is physical or virtual. The value[x] element of this type sub-extension must use codes from the DeliveryMethodVS value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: DeliveryMethod - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-056
**ID**: 56
**Summary**: Virtual modalities extension value SHALL use extensible value set
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Virtual Modalities VS](ValueSet-VirtualModalitiesVS.html)([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/VirtualModalitiesVS`)"
**Context**: The delivery-method extension includes a 'virtualModalities' sub-extension that specifies the modalities of virtual delivery. The value[x] element of this virtualModalities sub-extension should use codes from the VirtualModalitiesVS value set with extensible binding strength, meaning codes from the value set SHALL be used unless not suitable for a particular use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: DeliveryMethod - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-057
**ID**: 57
**Summary**: Extension definition SHALL be a URI for the Structure Definition
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the extension and its sub-extensions. The url element provides the source of the definition for the extension code and must be a URI pointing to the Structure Definition that formally defines the extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: DeliveryMethod - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-058
**ID**: 58
**Summary**: Extension SHALL be met as part of the definition requirements
**Requirement**: "Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: This is a general requirement for defining extensions within FHIR. While the specific requirements are referenced elsewhere in the FHIR specification, this establishes that extensions must conform to governance requirements for their definition.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.69.1 Extension: DeliveryMethod - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-059
**ID**: 59
**Summary**: NewPatients Extension url element SHALL be fixed to the canonical URL
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The url element of the NewPatients extension must contain the fixed canonical URL `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients` to properly identify the extension definition.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions, Elements 8, 12, 16, 24, 28, 32, 36
**Grouping**: General/Cross-Resource

---
# REQ-060
**ID**: 60
**Summary**: Extension URL SHALL be a URI for the Structure Definition
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the daysOfWeek, allDay, availableStartTime, and availableEndTime sub-extensions within the contactpoint-availabletime extension. The url must reference the structure definition that formally defines the extension.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-061
**ID**: 61
**Summary**: Extension daysOfWeek value SHALL use codes from DaysOfWeek value set
**Requirement**: "The codes SHALL be taken from [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html) ([required] to `http://hl7.org/fhir/ValueSet/days-of-week`)"
**Context**: The daysOfWeek sub-extension value[x] element must use codes from the DaysOfWeek value set. This constrains which day values can be used when specifying available days for a contact point.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-062
**ID**: 62
**Summary**: Extension elements SHALL meet governance requirements for extension definition
**Requirement**: "Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: This applies to the nested extension elements within daysOfWeek, allDay, availableStartTime, and availableEndTime sub-extensions. Extensions must follow FHIR governance rules for their definition to ensure they are safe and manageable.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-063
**ID**: 63
**Summary**: OrganizationAffiliation SHALL satisfy organization-or-participatingOrganization invariant
**Requirement**: "PlannetOrganizationAffiliation.organization or PlannetOrganizationAffiliation.participatingOrganization (`organization.exists() or participatingOrganization.exists()`)"
**Context**: The Plan-Net OrganizationAffiliation profile requires that either the organization element or the participatingOrganization element must be present. This invariant ensures that at least one of these two required references is populated to properly define the affiliation relationship between organizations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-064
**ID**: 64
**Summary**: OrganizationAffiliation.identifier.type SHALL be bound to Identifier Type Codes value set
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Identifier Type Codes](http://hl7.org/fhir/R4/valueset-identifier-type.html)([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) to `http://hl7.org/fhir/ValueSet/identifier-type`)"
**Context**: The identifier.type element in OrganizationAffiliation must use codes from the FHIR standard Identifier Type Codes value set to ensure consistent coding of identifier types across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-065
**ID**: 65
**Summary**: OrganizationAffiliation.identifier.value must be treated as case sensitive
**Requirement**: "Identifier.value is to be treated as case sensitive unless knowledge of the Identifier.system allows the processer to be confident that non-case-sensitive processing is safe."
**Context**: The value component of an identifier in OrganizationAffiliation should be treated as case sensitive to ensure accurate matching and comparison, unless the specific identifier system is known to support case-insensitive processing.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless knowledge of the Identifier.system allows the processer to be confident that non-case-sensitive processing is safe
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-066
**ID**: 66
**Summary**: OrganizationAffiliation.code SHALL be bound to OrganizationAffiliation Roles value set
**Requirement**: "Unless not suitable, these codes SHALL be taken from [OrganizationAffiliation Roles](ValueSet-OrganizationAffiliationRoleVS.html)([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/OrganizationAffiliationRoleVS`)"
**Context**: The code element that defines the role of the participating organization in the affiliation must use codes from the Plan-Net OrganizationAffiliation Roles value set to ensure consistent representation of affiliation roles.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-067
**ID**: 67
**Summary**: OrganizationAffiliation.specialty SHALL be bound to Specialties VS value set
**Requirement**: "The codes SHALL be taken from [Specialties VS](ValueSet-SpecialtiesVS.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/SpecialtiesVS`)"
**Context**: The specialty element that describes the specific specialty of the participating organization in the context of the role must use codes from the Plan-Net Specialties value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-068
**ID**: 68
**Summary**: OrganizationAffiliation.telecom.system SHALL be bound to ContactPointSystem value set
**Requirement**: "The codes SHALL be taken from [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/ValueSet/contact-point-system 4.0.1`)"
**Context**: The system element in telecom that identifies the telecommunications form must use codes from the FHIR ContactPointSystem value set with required binding to ensure consistent representation of contact point types.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-069
**ID**: 69
**Summary**: OrganizationAffiliation.telecom.use SHALL be bound to ContactPointUse value set
**Requirement**: "The codes SHALL be taken from [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/ValueSet/contact-point-use 4.0.1`)"
**Context**: The use element in telecom that identifies the purpose for the contact point must use codes from the FHIR ContactPointUse value set with required binding to ensure consistent representation of contact point purposes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-070
**ID**: 70
**Summary**: Qualification Extension Code Value Binding Requirement
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html)([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/SpecialtyAndDegreeLicenseCertificateVS`)"
**Context**: The Qualification extension's code sub-extension value must use codes from the Specialties, Degrees, Licenses, and Certificates value set with extensible binding strength, allowing for codes outside the value set when necessary.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-071
**ID**: 71
**Summary**: Qualification Extension Status Value Binding Requirement
**Requirement**: "The codes SHALL be taken from [Qualification Status VS](ValueSet-QualificationStatusVS.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/QualificationStatusVS`)"
**Context**: The Qualification extension's status sub-extension value must use codes from the Qualification Status value set with required binding strength, limiting codes strictly to those in the value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-072
**ID**: 72
**Summary**: Qualification Extension WhereValid Value Binding Requirement
**Requirement**: "The codes SHALL be taken from [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU7/ValueSet-us-core-usps-state.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state`)"
**Context**: The Qualification extension's whereValid sub-extension value must use codes from the USPS Two Letter Alphabetic Codes value set with required binding strength when the value is a CodeableConcept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-073
**ID**: 73
**Summary**: Qualification Extension URL Definition Requirement
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The url element of the Qualification extension and all sub-extensions must be a URI that points to the Structure Definition that defines the extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-074
**ID**: 74
**Summary**: OrganizationAffiliation active element is mandatory and must be true
**Requirement**: "OrganizationAffiliation.active [is mandatory with] Required Pattern: true"
**Context**: The Plan-Net OrganizationAffiliation profile requires that the active element be present (cardinality 1..1) and have a value of true. This indicates that the organization affiliation record must be in active use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: Plan-Net OrganizationAffiliation
**Grouping**: General/Cross-Resource

---
# REQ-075
**ID**: 75
**Summary**: OrganizationAffiliation must have either organization or participatingOrganization
**Requirement**: "PlannetOrganizationAffiliation.organization or PlannetOrganizationAffiliation.participatingOrganization: organization.exists() or participatingOrganization.exists()"
**Context**: The Plan-Net OrganizationAffiliation profile defines a constraint (organization-or-participatingOrganization) requiring that at least one of the organization or participatingOrganization elements must be present in the resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.2 Constraints
**Grouping**: General/Cross-Resource

---
# REQ-076
**ID**: 76
**Summary**: OrganizationAffiliation.code must use OrganizationAffiliationRoleVS value set (extensible)
**Requirement**: "OrganizationAffiliation.code [has] Binding: [OrganizationAffiliation Roles](ValueSet-OrganizationAffiliationRoleVS.html) ([extensible])"
**Context**: The code element that defines the role the participatingOrganization plays in the association must draw from the OrganizationAffiliationRoleVS value set. As an extensible binding, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated; alternate codings may be included if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-077
**ID**: 77
**Summary**: OrganizationAffiliation.specialty must use SpecialtiesVS value set (required)
**Requirement**: "OrganizationAffiliation.specialty [has] Binding: [Specialties VS](ValueSet-SpecialtiesVS.html) ([required])"
**Context**: The specialty element that indicates the specific specialty of the participatingOrganization in the context of the role must use codes from the SpecialtiesVS value set. As a required binding, the concept in this element SHALL be from the specified value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-078
**ID**: 78
**Summary**: OrganizationAffiliation.identifier.use must use IdentifierUse value set (required)
**Requirement**: "OrganizationAffiliation.identifier.use [has] Binding: [IdentifierUse](http://hl7.org/fhir/R4/valueset-identifier-use.html) ([required])"
**Context**: The purpose of an identifier must be drawn from the IdentifierUse value set. As a required binding, the concept in this element SHALL be from the specified value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-079
**ID**: 79
**Summary**: OrganizationAffiliation.identifier.type must use Identifier Type Codes value set (extensible)
**Requirement**: "OrganizationAffiliation.identifier.type [has] Binding: [Identifier Type Codes](http://hl7.org/fhir/R4/valueset-identifier-type.html) ([extensible])"
**Context**: The coded type for the identifier must draw from the Identifier Type Codes value set. As an extensible binding, the concept SHALL be from the specified value set if any of the codes within the value set can apply; alternate codings may be included if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-080
**ID**: 80
**Summary**: OrganizationAffiliation.telecom.system must use ContactPointSystem value set (required)
**Requirement**: "OrganizationAffiliation.telecom.system [has] Binding: [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) ([required])"
**Context**: The telecommunications form for contact point (system) must use codes from the ContactPointSystem value set. As a required binding, the concept in this element SHALL be from the specified value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-081
**ID**: 81
**Summary**: OrganizationAffiliation.telecom.use must use ContactPointUse value set (required)
**Requirement**: "OrganizationAffiliation.telecom.use [has] Binding: [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) ([required])"
**Context**: The purpose for the contact point must use codes from the ContactPointUse value set. As a required binding, the concept in this element SHALL be from the specified value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-082
**ID**: 82
**Summary**: InsurancePlan resource SHALL contain nested Resources constraint
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources"
**Context**: This is a base FHIR constraint (dom-2) that applies to the InsurancePlan resource when it is contained within another resource. It ensures that containment does not create deep nesting hierarchies.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the InsurancePlan resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant dom-2
**Grouping**: General/Cross-Resource

---
# REQ-083
**ID**: 83
**Summary**: InsurancePlan contained resource SHALL be referenced or refer to containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This is a base FHIR constraint (dom-3) ensuring that contained resources have a purpose and relationship within the containing resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the InsurancePlan resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant dom-3
**Grouping**: General/Cross-Resource

---
# REQ-084
**ID**: 84
**Summary**: InsurancePlan contained resource SHALL NOT have meta.versionId or meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated"
**Context**: This is a base FHIR constraint (dom-4) that prevents version management of contained resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the InsurancePlan resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant dom-4
**Grouping**: General/Cross-Resource

---
# REQ-085
**ID**: 85
**Summary**: InsurancePlan SHALL have name or identifier
**Requirement**: "The organization SHALL at least have a name or an idendtifier, and possibly more than one"
**Context**: This constraint (ipn-1) ensures that an InsurancePlan can be identified through either a name or an identifier (or both). The formal expression is: (identifier.count() + name.count()) > 0
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant ipn-1
**Grouping**: General/Cross-Resource

---
# REQ-086
**ID**: 86
**Summary**: InsurancePlan network definition requirement
**Requirement**: "If an insuranceplan does not define a network, then each plan must define one"
**Context**: This constraint (network-or-plan-Network) ensures that network information is present either at the InsurancePlan level or at each individual plan level. The formal expression is: network.exists() or plan.network.exists()
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only enforced when InsurancePlan.network does not exist
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant network-or-plan-Network
**Grouping**: General/Cross-Resource

---
# REQ-087
**ID**: 87
**Summary**: InsurancePlan.identifier.use codes SHALL be from IdentifierUse value set
**Requirement**: "The codes SHALL be taken from IdentifierUse"
**Context**: When InsurancePlan.identifier.use is present, it must use a code from the required IdentifierUse value set (http://hl7.org/fhir/ValueSet/identifier-use).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when InsurancePlan.identifier.use is populated
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 8
**Grouping**: General/Cross-Resource

---
# REQ-088
**ID**: 88
**Summary**: InsurancePlan.identifier.type codes SHALL be from Identifier Type Codes unless not suitable
**Requirement**: "Unless not suitable, these codes SHALL be taken from Identifier Type Codes"
**Context**: When InsurancePlan.identifier.type is present, it should use codes from the extensible Identifier Type Codes value set (http://hl7.org/fhir/ValueSet/identifier-type), unless the codes are not suitable for the use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when InsurancePlan.identifier.type is populated and suitable codes exist
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 10
**Grouping**: General/Cross-Resource

---
# REQ-089
**ID**: 89
**Summary**: InsurancePlan.identifier.value SHALL be urn:ietf:rfc:3986 if full URI
**Requirement**: "If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986"
**Context**: When InsurancePlan.identifier.value contains a full URI, the corresponding system element must be set to urn:ietf:rfc:3986.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when identifier.value is a full URI
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 12
**Grouping**: General/Cross-Resource

---
# REQ-090
**ID**: 90
**Summary**: InsurancePlan.status SHALL be from PublicationStatus value set
**Requirement**: "The codes SHALL be taken from PublicationStatus"
**Context**: InsurancePlan.status is required (cardinality 1..1) and must use a code from the required PublicationStatus value set (http://hl7.org/fhir/ValueSet/publication-status). The profile fixes this value to 'active'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 16, Element 36
**Grouping**: General/Cross-Resource

---
# REQ-091
**ID**: 91
**Summary**: InsurancePlan.type codes SHALL be from Insurance Product Type VS unless not suitable
**Requirement**: "Unless not suitable, these codes SHALL be taken from Insurance Product Type VS"
**Context**: InsurancePlan.type is required (cardinality 1..1) and should use codes from the extensible InsuranceProductTypeVS value set, unless the codes are not suitable for the use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when suitable codes exist in the value set
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 18, Element 38
**Grouping**: General/Cross-Resource

---
# REQ-092
**ID**: 92
**Summary**: InsurancePlan.contact.name.use codes SHALL be from NameUse value set
**Requirement**: "The codes SHALL be taken from NameUse"
**Context**: When InsurancePlan.contact.name.use is present, it must use a code from the required NameUse value set (http://hl7.org/fhir/ValueSet/name-use).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when InsurancePlan.contact.name.use is populated
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 38, Element 68
**Grouping**: General/Cross-Resource

---
# REQ-093
**ID**: 93
**Summary**: InsurancePlan.contact.name text and parts content consistency
**Requirement**: "Applications updating a name SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part"
**Context**: When both InsurancePlan.contact.name.text and name parts (family, given, etc.) are present, applications must ensure consistency between them during updates.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when both text and parts are present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 40, Element 70
**Grouping**: General/Cross-Resource

---
# REQ-094
**ID**: 94
**Summary**: InsurancePlan.contact.telecom.system codes SHALL be from ContactPointSystem value set
**Requirement**: "The codes SHALL be taken from ContactPointSystem"
**Context**: When InsurancePlan.contact.telecom.system is present, it must use a code from the required ContactPointSystem value set (http://hl7.org/fhir/ValueSet/contact-point-system).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when InsurancePlan.contact.telecom.system is populated
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 44, Element 88
**Grouping**: General/Cross-Resource

---
# REQ-095
**ID**: 95
**Summary**: InsurancePlan.contact.telecom.use codes SHALL be from ContactPointUse value set
**Requirement**: "The codes SHALL be taken from ContactPointUse"
**Context**: When InsurancePlan.contact.telecom.use is present, it must use a code from the required ContactPointUse value set (http://hl7.org/fhir/ValueSet/contact-point-use).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when InsurancePlan.contact.telecom.use is populated
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 48, Element 92
**Grouping**: General/Cross-Resource

---
# REQ-096
**ID**: 96
**Summary**: InsurancePlan.plan.type codes SHALL be from Insurance Plan TypeVS unless not suitable
**Requirement**: "Unless not suitable, these codes SHALL be taken from Insurance Plan TypeVS"
**Context**: When InsurancePlan.plan.type is present, it should use codes from the extensible InsurancePlanTypeVS value set, unless the codes are not suitable for the use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when InsurancePlan.plan.type is populated and suitable codes exist
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 58, Element 150
**Grouping**: General/Cross-Resource

---
# REQ-097
**ID**: 97
**Summary**: InsurancePlan.coverage.benefit.cost.applicability codes SHALL be from BenefitCostApplicability value set
**Requirement**: "The codes SHALL be taken from BenefitCostApplicability"
**Context**: When InsurancePlan.coverage.benefit.cost.applicability is present, it must use a code from the required BenefitCostApplicability value set (http://hl7.org/fhir/ValueSet/insuranceplan-applicability).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when InsurancePlan.coverage.benefit.cost.applicability is populated
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 202
**Grouping**: General/Cross-Resource

---
# REQ-098
**ID**: 98
**Summary**: Modifier extensions SHALL NOT change meaning of resource elements
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)"
**Context**: This requirement appears multiple times throughout the profile for various modifierExtension elements. Modifier extensions must not alter the meaning of the elements they are applied to or the containing resource.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Elements 4, 34, 56, 110, 122, 134, etc.
**Grouping**: General/Cross-Resource

---
# REQ-099
**ID**: 99
**Summary**: InsurancePlan status must be active
**Requirement**: "The current state of the health insurance product [status SHALL be] active"
**Context**: The InsurancePlan resource profile constrains the status element to a fixed value of 'active', indicating that only active insurance plans should be represented in this implementation guide.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource

---
# REQ-100
**ID**: 100
**Summary**: InsurancePlan type is mandatory
**Requirement**: "The kind of health insurance product [type SHALL be provided with cardinality] 1.1"
**Context**: Each InsurancePlan must include a type element that categorizes the kind of health insurance product using values from the InsuranceProductTypeVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource

---
# REQ-101
**ID**: 101
**Summary**: InsurancePlan ownedBy is mandatory
**Requirement**: "The entity that is providing the health insurance product and underwriting the risk [ownedBy SHALL be provided with cardinality] 1.1"
**Context**: Each InsurancePlan must reference the organization that owns and underwrites the insurance product, typically an insurance carrier or payer.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource

---
# REQ-102
**ID**: 102
**Summary**: InsurancePlan administeredBy is mandatory
**Requirement**: "An organization which administer other services such as underwriting, customer service and/or claims processing on behalf of the health insurance product owner [administeredBy SHALL be provided with cardinality] 1.1"
**Context**: Each InsurancePlan must reference the organization that administers the plan, which may be different from the organization that owns it.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource

---
# REQ-103
**ID**: 103
**Summary**: InsurancePlan must define network or each plan must define network
**Requirement**: "If an insuranceplan does not define a network, then each plan must define one: network.exists() or plan.network.exists()"
**Context**: This constraint ensures that network information is present either at the InsurancePlan level or within each individual plan, so that network coverage information is always available.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If the InsurancePlan does not have a network element populated, then each plan within the InsurancePlan must have a network element populated.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan - Constraints
**Grouping**: General/Cross-Resource

---
# REQ-104
**ID**: 104
**Summary**: Each InsurancePlan.plan must have distinct plan type
**Requirement**: "Each InsurancePlan.plan should have a distinct plan.type.: plan.type.coding.code.isDistinct()"
**Context**: This constraint ensures that within a single InsurancePlan resource, each plan has a unique type, preventing duplicate plan types within the same insurance product offering.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan - Constraints
**Grouping**: General/Cross-Resource

---
# REQ-105
**ID**: 105
**Summary**: InsurancePlan must have name or identifier
**Requirement**: "The organization SHALL at least have a name or an idendtifier, and possibly more than one"
**Context**: This constraint ensures that each InsurancePlan can be identified through either a name or an identifier (or both), providing minimum necessary identification information.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan - Constraints
**Grouping**: General/Cross-Resource
