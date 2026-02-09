# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Server SHALL support search parameter 'name' on InsurancePlan resource
**Requirement**: "Select products with the specified name"
**Context**: The Plan-Net server must support searching for InsurancePlan resources using the 'name' search parameter of type string. This parameter searches on 'name' and 'alias' fields and supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple values separated by comma where at least one must be true). Allowed modifiers are 'exact' and 'contains'.
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
**Summary**: Server SHALL support search by plan-type parameter on InsurancePlan resource
**Requirement**: "Select plans of the specified type"
**Context**: The Implementation Guide defines a search parameter Plannet_sp_insuranceplan_plan_type that enables searching InsurancePlan resources by the plan type. The parameter is of type token and uses the expression InsurancePlan.plan.type. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple values separated by comma where at least one must be true). The allowed modifier is 'text'.
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
# REQ-003
**ID**: 03
**Summary**: Server SHALL support search by network parameter on InsurancePlan resource
**Requirement**: "Select Organization entries in a given InsurancePlan's network"
**Context**: The Implementation Guide defines a search parameter Plannet_sp_insuranceplan_network that enables searching InsurancePlan resources by their associated network. The parameter is of type reference and uses the expression InsurancePlan.network. The parameter supports multipleOr (parameter may have multiple values separated by comma where at least one must be true). For multipleAnd, it's up to the server whether the parameter may repeat to specify multiple values that must all be true.
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
# REQ-004
**ID**: 04
**Summary**: Server SHALL support searching HealthcareService by name
**Requirement**: "Select HealthcareServices with the specified name [using search parameter `name` of type `string` with Expression `HealthcareService.name`]"
**Context**: The implementation guide defines a search parameter for finding HealthcareService resources based on the name element. This search parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The 'exact' and 'contains' modifiers are allowed.
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
# REQ-005
**ID**: 05
**Summary**: Server SHALL support service-type search parameter on HealthcareService resource
**Requirement**: "Server SHALL support Parameter `service-type`:`token` [to] Select HealthcareServices of the specified type [using Expression] `HealthcareService.type` [with] multipleAnd: The parameter may repeat in order to specify multiple values that must all be true [and] multipleOr: The parameter may have multiple values (separated by comma) where at least one must be true [and] Modifiers Allowed: text"
**Context**: This requirement defines a search parameter for HealthcareService resources that allows filtering by service type using token-based search. The search parameter supports both AND and OR logic for multiple values and allows text modifiers.
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
# REQ-006
**ID**: 06
**Summary**: Server SHALL support organization search parameter on Endpoint resource
**Requirement**: "Server SHALL support Parameter `organization`:`reference` [to] Select Endpoints managed by the specified organization [using Expression] `Endpoint.managingOrganization` [with Target Resources] Organization [and] multipleAnd: The parameter may repeat in order to specify multiple values that must all be true [and] multipleOr: The parameter may have multiple values (separated by comma) where at least one must be true [and] Chains Allowed: name, address, partof, type"
**Context**: This requirement defines a reference-based search parameter for Endpoint resources that allows filtering by managing organization. The search supports chaining to Organization resource attributes (name, address, partof, type) and allows multiple AND/OR combinations.
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
# REQ-007
**ID**: 07
**Summary**: Health Plan API Actor SHALL support searching InsurancePlan by owned-by parameter
**Requirement**: "Select products that are owned by the specified organization [using] Parameter `owned-by`:`reference` [with] Expression `InsurancePlan.ownedBy` [targeting] Organization"
**Context**: The SearchParameter Plannet_sp_insuranceplan_owned_by defines a reference-based search parameter for InsurancePlan resources based on the ownedBy element. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple comma-separated values where at least one must be true) semantics, with name and partof chain parameters allowed.
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
# REQ-008
**ID**: 08
**Summary**: Server SHALL support search by role parameter on OrganizationAffiliation resource
**Requirement**: "Select OrganizationAffiliations with the specified role [using] Parameter `role`:`token` [with] Expression `OrganizationAffiliation.code`"
**Context**: This search parameter enables searching for OrganizationAffiliation resources by their role code. The parameter supports multipleAnd (repeating parameters where all values must match) and multipleOr (comma-separated values where at least one must match), and allows the text modifier.
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
# REQ-009
**ID**: 09
**Summary**: Server SHALL support search by coverage-area parameter on InsurancePlan resource
**Requirement**: "Select products that are offered in the specified location [using] Parameter `coverage-area`:`reference` [with] Expression `InsurancePlan.coverageArea` [targeting] Target Resources [Location]"
**Context**: This search parameter enables searching for InsurancePlan resources by their coverage area (geographic location). The parameter supports multipleAnd (repeating parameters where all values must match) and multipleOr (comma-separated values where at least one must match). The target resource type is Location.
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
# REQ-010
**ID**: 10
**Summary**: Server SHALL support search by service-category parameter on HealthcareService resource
**Requirement**: "Select HealthcareServices providing the specified category of services [using] Parameter `service-category`:`token` [with] Expression `HealthcareService.category`"
**Context**: This search parameter enables searching for HealthcareService resources by their service category. The parameter supports multipleAnd (repeating parameters where all values must match) and multipleOr (comma-separated values where at least one must match), and allows the text modifier.
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
# REQ-011
**ID**: 11
**Summary**: Server SHALL support search by endpoint parameter on HealthcareService resource
**Requirement**: "Select HealthcareServices with the specified endpoint [using] Parameter `endpoint`:`reference` [with] Expression `HealthcareService.endpoint` [targeting] Target Resources [Endpoint]"
**Context**: This search parameter enables searching for HealthcareService resources by their associated endpoint. The parameter supports multipleAnd (repeating parameters where all values must match) and multipleOr (comma-separated values where at least one must match). The target resource type is Endpoint. Chain searches are allowed on the organization element.
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
# REQ-012
**ID**: 12
**Summary**: Health Plan API SHALL support search by period on OrganizationAffiliation resource
**Requirement**: "Select Organization Affiliations available in the specified period [using Parameter `period`:`date` on Resource OrganizationAffiliation with Expression `OrganizationAffiliation.period`]"
**Context**: This search parameter allows filtering of OrganizationAffiliation resources by their period of validity. The parameter supports multipleOr (at least one of comma-separated values must be true), and it is up to the server whether multipleAnd is supported.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.33.1 SearchParameter: Plannet_sp_organizationaffiliation_period
**Grouping**: General/Cross-Resource

---
# REQ-013
**ID**: 13
**Summary**: Health Plan API SHALL support search by specialty on OrganizationAffiliation resource
**Requirement**: "Select OrganizationAffiliations associated with the specified specialty [using Parameter `specialty`:`token` on Resource OrganizationAffiliation with Expression `OrganizationAffiliation.specialty`]"
**Context**: This search parameter allows filtering of OrganizationAffiliation resources by their specialty. The parameter supports multipleAnd (multiple values must all be true) and multipleOr (at least one of comma-separated values must be true). Allowed modifier includes text.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.37.1 SearchParameter: Plannet_sp_organizationaffiliation_specialty
**Grouping**: General/Cross-Resource

---
# REQ-014
**ID**: 14
**Summary**: Server SHALL support endpoint search parameter on OrganizationAffiliation resource
**Requirement**: "Select OrganizationAffiliations with the specified endpoint [using the endpoint search parameter on OrganizationAffiliation resource with expression OrganizationAffiliation.endpoint]"
**Context**: The Plannet_sp_organizationaffiliation_endpoint SearchParameter defines a required search capability for OrganizationAffiliation resources to filter by endpoint reference. The parameter type is reference, targets Endpoint resources, supports both multipleAnd and multipleOr semantics, and allows chaining with 'organization'.
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
# REQ-015
**ID**: 15
**Summary**: Server SHALL support delivery-method search parameter on HealthcareService resource
**Requirement**: "Select HealthcareServices based on the delivery method type [using the delivery-method search parameter on HealthcareService resource with expression HealthcareService.extension.where(url='http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method').extension.where(url='type')]"
**Context**: The Plannet_sp_healthcareservice_delivery_method SearchParameter defines a required search capability for HealthcareService resources to filter by delivery method type. The parameter type is token and supports both multipleAnd and multipleOr semantics.
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
# REQ-016
**ID**: 16
**Summary**: Server SHALL support service search parameter on OrganizationAffiliation resource
**Requirement**: "Select OrganizationAffiliations providing the specified service [using the service search parameter on OrganizationAffiliation resource with expression OrganizationAffiliation.healthcareService]"
**Context**: The Plannet_sp_organizationaffiliation_service SearchParameter defines a required search capability for OrganizationAffiliation resources to filter by healthcare service reference. The parameter type is reference, targets HealthcareService resources, supports both multipleAnd and multipleOr semantics, and allows chaining with 'service-category', 'organization', and 'location'.
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
# REQ-017
**ID**: 17
**Summary**: Conformance to HRex Conformance Expectations
**Requirement**: "All systems claiming conformance to this guide SHALL conform to the requirements listed in [the Health Record Exchange (Hrex) Conformance Expectations] section."
**Context**: This requirement establishes that all systems implementing this Plan-Net IG must also conform to the broader Da Vinci HRex conformance expectations, ensuring consistency across Da Vinci implementation guides.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: HRex Conformance Expectations (External)
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 4.1 Conformance Expectations
**Grouping**: General/Cross-Resource

---
# REQ-018
**ID**: 18
**Summary**: Health Plan API Population of Must Support Elements
**Requirement**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."
**Context**: When responding to queries, Health Plan API actors must include all data elements marked as Must Support in the profiles if the data is available in their systems.
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
# REQ-019
**ID**: 19
**Summary**: Health Plan API Omission of Missing Must Support Elements with Minimum Cardinality 0
**Requirement**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors SHALL NOT include the data elements in the resource instance returned as part of the query results."
**Context**: When Must Support elements with minimum cardinality of 0 have no data available, servers must omit these elements entirely from the response rather than including them with null or empty values.
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
# REQ-020
**ID**: 20
**Summary**: Health Plan API Handling of Missing Must Support Elements with Minimum Cardinality >0
**Requirement**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 [the Health Plan API actors] SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Context**: When Must Support elements with minimum cardinality greater than 0 have no data available, servers must include the element with an appropriate reason for absence rather than omitting it, ensuring required elements are always present.
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
# REQ-021
**ID**: 21
**Summary**: Application Processing of Must Support Elements Without Error
**Requirement**: "Application actors SHALL be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Context**: Applications must be able to handle all Must Support elements defined in the profiles without crashing or producing errors, ensuring robust processing of conformant resources.
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
# REQ-022
**ID**: 22
**Summary**: Application Display or Storage of Must Support Elements
**Requirement**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."
**Context**: While applications must process Must Support elements, they are strongly encouraged to also meaningfully use the data by either displaying it to users or persisting it for other purposes.
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
# REQ-023
**ID**: 23
**Summary**: Application Interpretation of Missing Must Support Elements
**Requirement**: "When querying Health Plan API actors, Application actors SHALL interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Context**: Applications must correctly understand that absent Must Support elements (with minimum cardinality 0) indicate the data is not available in the server's system, not that there was an error or omission in the response.
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
# REQ-024
**ID**: 24
**Summary**: Consumer App Processing of Must Support Elements with Missing Information
**Requirement**: "Consumer App actors SHALL be able to process resource instances containing Must Support data elements asserting missing information."
**Context**: Consumer applications must be able to handle Must Support elements that explicitly indicate missing information through mechanisms like dataAbsentReason, ensuring graceful handling of incomplete data.
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
**Summary**: Server MAY support Bulk Data IG for directory data retrieval
**Requirement**: "A server MAY support [Bulk Data IG](http://hl7.org/fhir/uv/bulkdata/index.html) for the retrieval of directory data."
**Context**: Servers implementing Plan-Net may optionally support the Bulk Data IG to enable bulk retrieval of directory data. This is draft guidance and has not been fully tested. Authorization mechanisms are not specified but the Bulk IG provides guidance on SMART Backend Service Authorization.
**Conformance**: MAY
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 7.3 Bulk Data
**Grouping**: General/Cross-Resource

---
# REQ-026
**ID**: 26
**Summary**: Accessibility Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the accessibility extension's URL element, which must be set to the fixed value 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility'. This ensures consistent identification of the accessibility extension across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.66.1 Extension: Accessibility - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-027
**ID**: 27
**Summary**: Accessibility Extension Value Binding
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Accessibility VS](ValueSet-AccessibilityVS.html)([extensible] to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/AccessibilityVS`)"
**Context**: The accessibility extension's value[x] element must use codes from the Accessibility ValueSet when suitable. The binding is extensible, meaning that if the ValueSet does not contain an appropriate code, codes from other systems may be used, but the preference is to use codes from the specified ValueSet.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: The requirement applies unless the codes in the specified ValueSet are not suitable for the use case.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.66.1 Extension: Accessibility - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-028
**ID**: 28
**Summary**: ViaIntermediary Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement specifies that the Extension.url element for the ViaIntermediary extension must contain a fixed URI value that points to the Structure Definition. The fixed value must be "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary". This ensures consistent identification of the extension across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-029
**ID**: 29
**Summary**: ViaIntermediary Extension Must Have Extensions or Value
**Requirement**: "Must have either extensions or value[x], not both (`extension.exists() != value.exists()`)"
**Context**: This invariant (ext-1) applies to the ViaIntermediary Extension and requires that the extension must contain either nested extensions OR a value element, but not both simultaneously. This ensures proper structure of the extension data.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-030
**ID**: 30
**Summary**: ViaIntermediary Extension Elements Must Have Value or Children
**Requirement**: "All FHIR elements must have a @value or children (`hasValue() or (children().count() > id.count())`)"
**Context**: This invariant (ele-1) applies to all elements within the ViaIntermediary Extension and requires that every FHIR element must contain either a value attribute or child elements (excluding just an id). This ensures that elements are not empty placeholders.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
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
**Summary**: Delivery method extension type value SHALL be from DeliveryMethodVS value set
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [DeliveryMethodVS]"
**Context**: The delivery-method extension is used on HealthcareService resources to describe the service delivery method (physical or virtual). The extension:type sub-extension indicates whether service delivery is physical or virtual and must use a code from the required DeliveryMethodVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: Delivery Method - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-032
**ID**: 32
**Summary**: Delivery method extension virtualModalities value SHALL be from VirtualModalitiesVS value set if applicable
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [VirtualModalitiesVS] if any of the codes within the value set can apply to the concept being communicated"
**Context**: The delivery-method extension is used on HealthcareService resources. The extension:virtualModalities sub-extension specifies the modalities of virtual service delivery when the service is delivered virtually. This sub-extension has an extensible binding to the VirtualModalitiesVS value set, meaning codes from the value set must be used if applicable, but alternate codings may be used if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If any of the codes within the VirtualModalitiesVS value set can apply to the concept being communicated
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: Delivery Method - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-033
**ID**: 33
**Summary**: Contactpoint Availabletime Extension daysOfWeek value binding requirement
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [DaysOfWeek (http://hl7.org/fhir/ValueSet/days-of-week)]"
**Context**: The contactpoint-availabletime extension includes a daysOfWeek sub-extension with a code datatype value. This requirement constrains the allowed code values to those defined in the FHIR standard DaysOfWeek value set, ensuring interoperability and consistency in representing days of the week when specifying contact point availability.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the daysOfWeek extension element is populated with a value
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1.1.1 Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-034
**ID**: 34
**Summary**: New Patients Extension SHALL include acceptingPatients element with required binding
**Requirement**: "Extension.extension:acceptingPatients.value[x] SHALL be from the specified value set AcceptingPatientsVS (required conformance)"
**Context**: The New Patients extension, which may be used on HealthcareService, Location, and PractitionerRole resources, includes a mandatory acceptingPatients element that indicates whether new patients are being accepted. This element has a required binding to the AcceptingPatientsVS value set, meaning conformant implementations must use codes from this specific value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-035
**ID**: 35
**Summary**: New Patients Extension constraint - no characteristics allowed when not accepting patients
**Requirement**: "If no new patients are accepted, no characteristics are allowed: extension.where(url='acceptingPatients').value.ofType(CodeableConcept).coding.where(code = 'no') implies extension.where(url='characteristics').empty()"
**Context**: The New Patients extension includes a constraint (new-patients-characteristics) that enforces business logic: when the acceptingPatients element has a code value of 'no', the characteristics extension element must be empty. This prevents contradictory data where a provider indicates they are not accepting new patients but also specifies characteristics of patients they would accept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This constraint only applies when extension.where(url='acceptingPatients').value.ofType(CodeableConcept).coding.where(code = 'no') evaluates to true
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients - Constraints
**Grouping**: General/Cross-Resource

---
# REQ-036
**ID**: 36
**Summary**: Qualification Extension - Code Element Cardinality
**Requirement**: "[The Qualification extension] extension:code [has cardinality] 1.1"
**Context**: The Qualification extension is used to add qualifications for an organization (e.g., accreditation) or practitionerRole (e.g., registered to prescribe controlled substances). The extension can be applied to Organization, OrganizationAffiliation, and PractitionerRole resources. The code element within this extension is mandatory and must appear exactly once, representing the type of qualification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Differential View
**Grouping**: General/Cross-Resource

---
# REQ-037
**ID**: 37
**Summary**: Qualification Extension - Code Element Value Binding
**Requirement**: "To be conformant, the concept in [extension:code.value[x]] element SHALL be from the specified value set [SpecialtyAndDegreeLicenseCertificateVS] if any of the codes within the value set can apply to the concept being communicated."
**Context**: The code element's value must use codes from the SpecialtyAndDegreeLicenseCertificateVS value set when applicable codes exist within that value set. This is an extensible binding, allowing alternate codings or text when the value set does not cover the concept being communicated.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If any of the codes within the SpecialtyAndDegreeLicenseCertificateVS value set can apply to the concept being communicated
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-038
**ID**: 38
**Summary**: Qualification Extension - Status Element Cardinality
**Requirement**: "[The Qualification extension] extension:status [has cardinality] 1.1"
**Context**: The status element within the Qualification extension is mandatory and must appear exactly once, indicating the current status of the qualification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Differential View
**Grouping**: General/Cross-Resource

---
# REQ-039
**ID**: 39
**Summary**: Qualification Extension - Status Element Required Binding
**Requirement**: "To be conformant, the concept in [extension:status.value[x]] element SHALL be from the specified value set [QualificationStatusVS]."
**Context**: The status element's value must use a code from the QualificationStatusVS value set. This is a required binding with a fixed value of 'active'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-040
**ID**: 40
**Summary**: Qualification Extension - WhereValid Element Required Binding
**Requirement**: "To be conformant, the concept in [extension:whereValid.value[x]] element SHALL be from the specified value set [UspsTwoLetterAlphabeticCodes]."
**Context**: The whereValid element's value, when provided, must use a valid code from the USPS Two Letter Alphabetic Codes value set (us-core-usps-state). This is a required binding that constrains the geographic validity of the qualification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-041
**ID**: 41
**Summary**: Extension.extension:type is Must Support
**Requirement**: "Extension.extension:type [Must Support] true"
**Context**: The endpoint-usecase extension includes a type sub-extension that indicates the type of services supported by the endpoint. This sub-extension is marked as Must Support, meaning systems claiming conformance to this profile must be capable of populating and processing this element.
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
# REQ-042
**ID**: 42
**Summary**: Extension.extension:type.value[x] binding to EndpointUsecaseVS
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Endpoint Usecases VS](ValueSet-EndpointUsecaseVS.html) (extensible to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/EndpointUsecaseVS`)"
**Context**: The value[x] element of the type sub-extension must use codes from the EndpointUsecaseVS value set with extensible binding strength. This means codes should be taken from the specified value set unless they are not suitable for the use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable, these codes SHALL be taken from the specified value set
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-043
**ID**: 43
**Summary**: Extension.extension:standard is Must Support
**Requirement**: "Extension.extension:standard [Must Support] true"
**Context**: The endpoint-usecase extension includes a standard sub-extension that provides a URI to a published standard describing the services supported by the endpoint (e.g., an HL7 implementation guide). This sub-extension is marked as Must Support, meaning systems claiming conformance to this profile must be capable of populating and processing this element.
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
# REQ-044
**ID**: 44
**Summary**: Extension url fixed value requirement
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The url element of the Extension must contain the canonical URI that uniquely identifies the endpoint-usecase extension structure definition. The fixed value is `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase`.
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
# REQ-045
**ID**: 45
**Summary**: Extension must satisfy ele-1 invariant
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: The ele-1 invariant ensures that every FHIR element either has a value attribute or has child elements beyond just an id. This applies to the Extension and all its sub-elements.
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
**Summary**: Extension must satisfy ext-1 invariant
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: The ext-1 invariant ensures that an extension element has either sub-extensions or a value[x] element, but not both simultaneously. This applies to the Extension and all its sub-extension elements.
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
# REQ-047
**ID**: 47
**Summary**: Delivery method extension type value binding requirement
**Requirement**: "The codes SHALL be taken from [Delivery Methods VS](ValueSet-DeliveryMethodVS.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/DeliveryMethodVS`)"
**Context**: The delivery-method extension includes a type sub-extension that indicates whether service delivery is physical or virtual. The value[x] element of this type sub-extension must use codes from the Delivery Methods value set with required binding strength.
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
# REQ-048
**ID**: 48
**Summary**: Virtual modalities value binding requirement
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Virtual Modalities VS](ValueSet-VirtualModalitiesVS.html)([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/VirtualModalitiesVS`)"
**Context**: The delivery-method extension includes a virtualModalities sub-extension that specifies modalities of virtual delivery. The value[x] element of this virtualModalities sub-extension should use codes from the Virtual Modalities value set with extensible binding strength.
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
# REQ-049
**ID**: 49
**Summary**: Extension definition URI requirement
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The url element of the delivery-method extension and its sub-extensions must contain a URI pointing to the Structure Definition that defines the extension.
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
# REQ-050
**ID**: 50
**Summary**: Extension governance requirements
**Requirement**: "Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: The delivery-method extension follows FHIR's governance requirements for extension definition to ensure safe and manageable use of extensions.
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
# REQ-051
**ID**: 51
**Summary**: Extension URL must be defined as a URI for Structure Definition
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the contactpoint-availabletime extension and its sub-extensions (daysOfWeek, allDay, availableStartTime, availableEndTime). The url element identifies the meaning of the extension and must point to the Structure Definition that formally defines it.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: ContactPointAvailableTime - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-052
**ID**: 52
**Summary**: Extension must have either extensions or value[x], not both
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: This invariant (ext-1) applies to the contactpoint-availabletime extension and all its sub-extensions. An extension cannot simultaneously have both nested extensions and a direct value - it must be one or the other.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: ContactPointAvailableTime - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-053
**ID**: 53
**Summary**: All FHIR elements must have a value or children
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: This invariant (ele-1) applies to all elements within the contactpoint-availabletime extension structure. Each element must contain either a value attribute or child elements (beyond just an id).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: ContactPointAvailableTime - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-054
**ID**: 54
**Summary**: daysOfWeek value must be from DaysOfWeek ValueSet
**Requirement**: "The codes SHALL be taken from [DaysOfWeek] (required to http://hl7.org/fhir/ValueSet/days-of-week)"
**Context**: The daysOfWeek sub-extension value[x] element has a required binding to the DaysOfWeek ValueSet. This constrains the acceptable codes for specifying days of the week when the contact point is available.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: ContactPointAvailableTime - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-055
**ID**: 55
**Summary**: Qualification extension code sub-element binding requirement
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html) (extensible to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/SpecialtyAndDegreeLicenseCertificateVS`)"
**Context**: The qualification extension includes a 'code' sub-element that describes the type of qualification (e.g., specialty, degree, license, certificate). This requirement constrains the value set that SHALL be used to code qualifications, with an extensible binding allowing other codes when the provided value set is not suitable.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies "unless not suitable" - the binding is extensible, so other codes may be used if the specified value set is not appropriate for the qualification being represented.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions, Element 18 (Extension.extension:code.value[x])
**Grouping**: General/Cross-Resource

---
# REQ-056
**ID**: 56
**Summary**: Qualification extension status sub-element binding requirement
**Requirement**: "The codes SHALL be taken from [Qualification Status VS](ValueSet-QualificationStatusVS.html) (required to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/QualificationStatusVS`)"
**Context**: The qualification extension includes a 'status' sub-element that indicates the current state of the qualification. This requirement constrains the value set that SHALL be used to code the qualification status, with a required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions, Element 34 (Extension.extension:status.value[x])
**Grouping**: General/Cross-Resource

---
# REQ-057
**ID**: 57
**Summary**: Qualification extension whereValid sub-element binding requirement
**Requirement**: "The codes SHALL be taken from [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU7/ValueSet-us-core-usps-state.html) (required to `http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state`)"
**Context**: The qualification extension includes a 'whereValid' sub-element that specifies the geographic location(s) where the qualification is valid. When coded as a CodeableConcept, this requirement constrains the value set that SHALL be used, requiring USPS state codes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions, Element 50 (Extension.extension:whereValid.value[x])
**Grouping**: General/Cross-Resource

---
# REQ-058
**ID**: 58
**Summary**: Qualification extension url element value requirement
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the 'url' element of the qualification extension, which identifies the meaning of the extension. The url must be a URI pointing to the structure definition.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions, Multiple elements (8, 16, 24, 32, 40, 48, 52, 62, 66)
**Grouping**: General/Cross-Resource

---
# REQ-059
**ID**: 59
**Summary**: OrganizationAffiliation active element must be true
**Requirement**: "Whether this organization affiliation record is in active use. [OrganizationAffiliation.active] Required Pattern: true"
**Context**: The Plan-Net OrganizationAffiliation profile requires that the active element have a cardinality of 1..1 and a required pattern of true, meaning all OrganizationAffiliation resources conforming to this profile must have active set to true.
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
# REQ-060
**ID**: 60
**Summary**: OrganizationAffiliation must have organization or participatingOrganization
**Requirement**: "PlannetOrganizationAffiliation.organization or PlannetOrganizationAffiliation.participatingOrganization: organization.exists() or participatingOrganization.exists()"
**Context**: This is a constraint (organization-or-participatingOrganization) that requires either the organization element or the participatingOrganization element (or both) to be present in the OrganizationAffiliation resource. This ensures that the affiliation relationship is properly defined with at least one of the two organizations specified.
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
# REQ-061
**ID**: 61
**Summary**: OrganizationAffiliation.code must use OrganizationAffiliationRoleVS value set
**Requirement**: "Definition of the role the participatingOrganization plays [OrganizationAffiliation.code] Binding: OrganizationAffiliation Roles (http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/OrganizationAffiliationRoleVS) (extensible)"
**Context**: The code element that defines the role the participating organization plays in the affiliation must draw from the OrganizationAffiliationRoleVS value set. This is an extensible binding, meaning codes should be from this value set if applicable, but alternate codings may be used if the value set does not cover the concept.
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
# REQ-062
**ID**: 62
**Summary**: OrganizationAffiliation.specialty must use SpecialtiesVS value set
**Requirement**: "Specific specialty of the participatingOrganization in the context of the role [OrganizationAffiliation.specialty] Binding: Specialties VS (http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/SpecialtiesVS) (required)"
**Context**: The specialty element that specifies the specialty of the participating organization in the context of the role must use codes from the SpecialtiesVS value set. This is a required binding, meaning concepts must be from the specified value set.
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
# REQ-063
**ID**: 63
**Summary**: OrganizationAffiliation.identifier.use must use IdentifierUse value set
**Requirement**: "The purpose of this identifier [OrganizationAffiliation.identifier.use] Binding: IdentifierUse (http://hl7.org/fhir/ValueSet/identifier-use) (required)"
**Context**: The use element within identifier that indicates the purpose of the identifier must use codes from the IdentifierUse value set. This is a required binding from the FHIR Standard.
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
# REQ-064
**ID**: 64
**Summary**: OrganizationAffiliation.telecom.system must use ContactPointSystem value set
**Requirement**: "Telecommunications form for contact point [OrganizationAffiliation.telecom.system] Binding: ContactPointSystem (http://hl7.org/fhir/ValueSet/contact-point-system) (required)"
**Context**: The system element within telecom that indicates the telecommunications form must use codes from the ContactPointSystem value set. This is a required binding from the FHIR Standard.
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
# REQ-065
**ID**: 65
**Summary**: OrganizationAffiliation.telecom.use must use ContactPointUse value set
**Requirement**: "Identifies the purpose for the contact point [OrganizationAffiliation.telecom.use] Binding: ContactPointUse (http://hl7.org/fhir/ValueSet/contact-point-use) (required)"
**Context**: The use element within telecom that identifies the purpose for the contact point must use codes from the ContactPointUse value set. This is a required binding from the FHIR Standard.
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
# REQ-066
**ID**: 66
**Summary**: InsurancePlan resource SHALL have a name or identifier
**Requirement**: "The organization SHALL at least have a name or an idendtifier, and possibly more than one (`(identifier.count() + name.count()) > 0`)"
**Context**: This is an invariant (ipn-1) on the InsurancePlan resource profile that ensures the resource can be identified through either a business identifier or a name. This requirement is affected by elements InsurancePlan.identifier and InsurancePlan.name.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - Invariants
**Grouping**: General/Cross-Resource

---
# REQ-067
**ID**: 67
**Summary**: InsurancePlan SHALL define network at plan or InsurancePlan level
**Requirement**: "If an insuranceplan does not define a network, then each plan must define one (`network.exists() or plan.network.exists()`)"
**Context**: This is an invariant (network-or-plan-Network) on the InsurancePlan resource that ensures a network is defined either at the InsurancePlan level or at each individual plan level within the InsurancePlan.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If an InsurancePlan does not define a network at the resource level, then each plan within the InsurancePlan must define one.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - Invariants
**Grouping**: General/Cross-Resource

---
# REQ-068
**ID**: 68
**Summary**: InsurancePlan plan types SHALL be distinct
**Requirement**: "Each InsurancePlan.plan should have a distinct plan.type. (`plan.type.coding.code.isDistinct()`)"
**Context**: This is an invariant (plan-type-is-distinct) on the InsurancePlan resource ensuring that each plan within an InsurancePlan has a unique plan type, preventing duplicate plan type codes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - Invariants
**Grouping**: General/Cross-Resource

---
# REQ-069
**ID**: 69
**Summary**: InsurancePlan status SHALL be active
**Requirement**: "The current state of the health insurance product [status field has] Fixed Value `active`"
**Context**: The InsurancePlan.status element is required (cardinality 1.1) and must be set to the fixed value of 'active'. This indicates that only active insurance plans should be represented in this profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - InsurancePlan.status
**Grouping**: General/Cross-Resource

---
# REQ-070
**ID**: 70
**Summary**: Modifier extensions SHALL NOT change meaning of resource elements
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)."
**Context**: This requirement applies to all modifierExtension elements within the InsurancePlan resource and its sub-elements. It constrains how modifier extensions can be used to ensure they don't alter the fundamental meaning of standard FHIR elements.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - modifierExtension elements
**Grouping**: General/Cross-Resource

---
# REQ-071
**ID**: 71
**Summary**: Applications processing InsurancePlan SHALL check for modifier extensions
**Requirement**: "Applications processing a resource are required to check for modifier extensions."
**Context**: This requirement applies to consuming applications (Application Actor) when processing InsurancePlan resources. Applications must check for the presence of modifier extensions in the resource and its sub-elements to ensure proper interpretation of the data.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - modifierExtension elements
**Grouping**: General/Cross-Resource

---
# REQ-072
**ID**: 72
**Summary**: Applications updating InsurancePlan contact name SHALL ensure text and parts consistency
**Requirement**: "Applications updating a name SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part."
**Context**: This requirement applies to the InsurancePlan.contact.name element when both the text representation and individual name parts (family, given, etc.) are provided. Applications must maintain consistency between these representations.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When both InsurancePlan.contact.name.text and name parts (family, given, prefix, suffix) are present in an update operation.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - InsurancePlan.contact.name.text
**Grouping**: General/Cross-Resource

---
# REQ-073
**ID**: 73
**Summary**: Contained resources SHALL NOT contain nested resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources (contained.contained.empty())"
**Context**: This is invariant dom-2 that applies when an InsurancePlan resource is contained within another resource. It prevents recursive nesting of contained resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When the InsurancePlan resource is contained in another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - Invariants
**Grouping**: General/Cross-Resource

---
# REQ-074
**ID**: 74
**Summary**: Contained resources SHALL be referenced or refer to container
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This is invariant dom-3 that requires contained InsurancePlan resources to have a clear relationship with their container through references.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When the InsurancePlan resource is contained in another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - Invariants
**Grouping**: General/Cross-Resource

---
# REQ-075
**ID**: 75
**Summary**: Contained resources SHALL NOT have versionId or lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (contained.meta.versionId.empty() and contained.meta.lastUpdated.empty())"
**Context**: This is invariant dom-4 that prevents contained InsurancePlan resources from having versioning metadata.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When the InsurancePlan resource is contained in another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - Invariants
**Grouping**: General/Cross-Resource

---
# REQ-076
**ID**: 76
**Summary**: Contained resources SHALL NOT have security labels
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label (contained.meta.security.empty())"
**Context**: This is invariant dom-5 that prevents contained InsurancePlan resources from having security labels in their metadata.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When the InsurancePlan resource is contained in another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetInsurancePlan - Detailed Descriptions - Invariants
**Grouping**: General/Cross-Resource

---
# REQ-077
**ID**: 77
**Summary**: InsurancePlan type is mandatory
**Requirement**: "The kind of health insurance product [InsurancePlan.type] Card. 1.1"
**Context**: The Plan-Net InsurancePlan profile requires that every InsurancePlan resource must specify a type indicating the kind of health insurance product, with cardinality 1..1 (exactly one occurrence required).
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
# REQ-078
**ID**: 78
**Summary**: InsurancePlan must reference an owning organization
**Requirement**: "The entity that is providing the health insurance product and underwriting the risk [InsurancePlan.ownedBy] Card. 1.1"
**Context**: The Plan-Net InsurancePlan profile mandates that every InsurancePlan resource must reference a Plan-Net Organization that owns and underwrites the insurance product, with cardinality 1..1 (exactly one occurrence required).
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
# REQ-079
**ID**: 79
**Summary**: InsurancePlan must reference an administering organization
**Requirement**: "An organization which administer other services such as underwriting, customer service and/or claims processing on behalf of the health insurance product owner [InsurancePlan.administeredBy] Card. 1.1"
**Context**: The Plan-Net InsurancePlan profile requires that every InsurancePlan resource must reference a Plan-Net Organization that administers the insurance product, with cardinality 1..1 (exactly one occurrence required).
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
# REQ-080
**ID**: 80
**Summary**: Each InsurancePlan plan must have a distinct plan type
**Requirement**: "Each InsurancePlan.plan should have a distinct plan.type.: plan.type.coding.code.isDistinct()"
**Context**: The Plan-Net InsurancePlan profile includes a constraint (plan-type-is-distinct) that requires each plan within an InsurancePlan to have a unique plan type, ensuring that plans can be distinguished by their type codes.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource
