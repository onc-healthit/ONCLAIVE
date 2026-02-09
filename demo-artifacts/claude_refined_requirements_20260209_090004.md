# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Health Plan API Actor SHALL support searching HealthcareService by specialty parameter
**Requirement**: "Select services associated with the specified specialty" using the search parameter `specialty` of type `token` on the HealthcareService resource with expression `HealthcareService.specialty`
**Context**: The SearchParameter definition Plannet_sp_healthcareservice_specialty specifies that servers must support searching for HealthcareService resources by the specialty search parameter. This parameter is of type token and uses the expression HealthcareService.specialty. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple comma-separated values where at least one must be true), with the text modifier allowed.
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
**Summary**: Plan-Net Server SHALL support search parameter 'location' on HealthcareService resource
**Requirement**: "Parameter `location`:`reference` - Select HealthcareServices available at the specified location. Resource [HealthcareService]. Expression `HealthcareService.location`. The parameter may repeat in order to specify multiple values that must all be true (multipleAnd). The parameter may have multiple values (separated by comma) where at least one must be true (multipleOr). Chains Allowed: address, address-postalcode, address-city, address-state, organization, type"
**Context**: This search parameter enables querying HealthcareService resources by their associated location reference. The parameter supports both multipleAnd and multipleOr semantics, and allows chaining to search by location characteristics such as address, address-postalcode, address-city, address-state, organization, and type.
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
**Summary**: Plan-Net Server SHALL support search parameter 'organization' on HealthcareService resource
**Requirement**: "Parameter `organization`:`reference` - Select HealthcareServices provided by the specified organization. Resource [HealthcareService]. Expression `HealthcareService.providedBy`. The parameter may repeat in order to specify multiple values that must all be true (multipleAnd). The parameter may have multiple values (separated by comma) where at least one must be true (multipleOr). Chains Allowed: name, address, partof, type"
**Context**: This search parameter enables querying HealthcareService resources by the organization that provides them. The parameter supports both multipleAnd and multipleOr semantics, and allows chaining to search by organization characteristics such as name, address, partof, and type.
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
**Summary**: Plan-Net Server SHALL support search parameter 'coverage-area' on HealthcareService resource
**Requirement**: "Parameter `coverage-area`:`reference` - Select services available in a region described by the specified location. Resource [HealthcareService]. Expression `HealthcareService.coverageArea`. The parameter may repeat in order to specify multiple values that must all be true (multipleAnd). The parameter may have multiple values (separated by comma) where at least one must be true (multipleOr)"
**Context**: This search parameter enables querying HealthcareService resources by their coverage area, which is defined as a location reference. The parameter supports both multipleAnd and multipleOr semantics to allow searching for services available in multiple regions or requiring all specified regions.
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
**Summary**: Plan-Net Server SHALL support search-type and read interactions on HealthcareService resource
**Requirement**: "A Server SHALL support search-type, read [on HealthcareService resource]."
**Context**: This requirement mandates that the server must support the ability to search for HealthcareService resources and read individual HealthcareService resources by their logical ID.
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
**Summary**: Plan-Net Server SHOULD support vread interaction on HealthcareService resource
**Requirement**: "A Server SHOULD support vread [on HealthcareService resource]."
**Context**: This requirement recommends that the server should support retrieving specific historical versions of a HealthcareService resource using the version-aware read (vread) operation.
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
**Summary**: Plan-Net Server SHALL support reading HealthcareService resource by id
**Requirement**: "A Server SHALL be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]`"
**Context**: This requirement mandates that the server must support retrieving a specific HealthcareService resource using its logical ID via a GET operation.
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
**Summary**: Plan-Net Server SHOULD support vread on HealthcareService resource by id and version
**Requirement**: "A Server SHOULD be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]/_history/vid`"
**Context**: This requirement recommends that the server should support retrieving a specific version of a HealthcareService resource using its logical ID and version ID.
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
**Summary**: Plan-Net Server SHALL support _include parameters for HealthcareService resource
**Requirement**: "A Server SHALL be capable of supporting the following _includes: HealthcareService:location - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:location`; HealthcareService:coverage-area - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:coverage-area`; HealthcareService:organization - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:organization`; HealthcareService:endpoint - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:endpoint`"
**Context**: This requirement mandates that the server must support including referenced Location, coverage-area (Location), Organization, and Endpoint resources when searching for HealthcareService resources using the _include parameter.
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
**Summary**: Plan-Net Server SHALL support _revinclude parameters for HealthcareService resource
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=PractitionerRole:service`; OrganizationAffiliation:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=OrganizationAffiliation:service`"
**Context**: This requirement mandates that the server must support reverse includes to retrieve PractitionerRole and OrganizationAffiliation resources that reference the HealthcareService resources in the search results.
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
**Summary**: Plan-Net Server SHALL support search parameters on HealthcareService resource
**Requirement**: "A Server SHALL support the following search parameters on HealthcareService: location, coverage-area, organization, endpoint, name, service-category, service-type, specialty, _id, _lastUpdated"
**Context**: This requirement mandates that the server must support searching for HealthcareService resources using the specified reference parameters (location, coverage-area, organization, endpoint), string parameters (name), token parameters (service-category, service-type, specialty), and standard parameters (_id, _lastUpdated).
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
**Summary**: HealthcareService active element must be supported
**Requirement**: "HealthcareService.active [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The active element indicates whether the HealthcareService record is in active use and must be supported by implementations of this profile.
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
**Summary**: HealthcareService active element must have pattern value of true
**Requirement**: "HealthcareService.active [has] Pattern Value `true`"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The active element must have a fixed value of true, indicating that the HealthcareService record is in active use.
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
**Summary**: HealthcareService identifier type must be supported
**Requirement**: "HealthcareService.identifier.type [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The identifier.type element provides a coded type for the identifier and must be supported by implementations.
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
**Summary**: HealthcareService identifier value must be supported
**Requirement**: "HealthcareService.identifier.value [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The identifier.value element contains the unique value of the identifier and must be supported by implementations.
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
**Summary**: HealthcareService providedBy must be supported
**Requirement**: "HealthcareService.providedBy [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The providedBy element references the organization that provides the healthcare service and must be supported by implementations.
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
**Summary**: HealthcareService category must be supported
**Requirement**: "HealthcareService.category [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The category element identifies the broad category of service being performed or delivered and must be supported by implementations.
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
**Summary**: HealthcareService category plan-net-category slice must be supported
**Requirement**: "HealthcareService.category:plan-net-category [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The plan-net-category slice of the category element must be supported and uses the Healthcare Service CategoryVS value set with required binding.
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
**Summary**: HealthcareService type must be supported
**Requirement**: "HealthcareService.type [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The type element specifies the specific type of service that may be delivered or performed and must be supported by implementations.
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
**Summary**: HealthcareService specialty must be supported
**Requirement**: "HealthcareService.specialty [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The specialty element contains the collection of specialties handled by the service site and must be supported by implementations.
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
**Summary**: HealthcareService location must be supported
**Requirement**: "HealthcareService.location [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The location element references the location(s) where the healthcare service may be provided and must be supported by implementations.
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
**Summary**: HealthcareService name must be supported
**Requirement**: "HealthcareService.name [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The name element provides a description of the service as it would be presented to a consumer while searching and must be supported by implementations.
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
# REQ-023
**ID**: 23
**Summary**: HealthcareService comment must be supported
**Requirement**: "HealthcareService.comment [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The comment element contains any additional description of the service and must be supported by implementations.
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
# REQ-024
**ID**: 24
**Summary**: HealthcareService telecom must be supported
**Requirement**: "HealthcareService.telecom [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The telecom element contains contact information related to the healthcare service and must be supported by implementations.
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
# REQ-025
**ID**: 25
**Summary**: HealthcareService telecom contactpoint-availabletime extension must be supported
**Requirement**: "HealthcareService.telecom.extension:contactpoint-availabletime [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The contactpoint-availabletime extension representing the days and times a contact point is available must be supported by implementations.
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
# REQ-026
**ID**: 26
**Summary**: HealthcareService telecom via-intermediary extension must be supported
**Requirement**: "HealthcareService.telecom.extension:via-intermediary [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The via-intermediary extension provides a reference to an alternative point of contact and must be supported by implementations.
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
# REQ-027
**ID**: 27
**Summary**: HealthcareService telecom system must be supported
**Requirement**: "HealthcareService.telecom.system [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The telecom.system element identifies the telecommunications form for the contact point and must be supported by implementations.
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
# REQ-028
**ID**: 28
**Summary**: HealthcareService telecom value must be supported
**Requirement**: "HealthcareService.telecom.value [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The telecom.value element contains the actual contact point details and must be supported by implementations.
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
# REQ-029
**ID**: 29
**Summary**: HealthcareService coverageArea must be supported
**Requirement**: "HealthcareService.coverageArea [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The coverageArea element indicates the location(s) that the service is available to and must be supported by implementations.
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
# REQ-030
**ID**: 30
**Summary**: HealthcareService appointmentRequired must be supported
**Requirement**: "HealthcareService.appointmentRequired [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The appointmentRequired element indicates whether an appointment is required for access to the service and must be supported by implementations.
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
# REQ-031
**ID**: 31
**Summary**: HealthcareService availableTime must be supported
**Requirement**: "HealthcareService.availableTime [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The availableTime element contains times that the service site is available and must be supported by implementations.
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
# REQ-032
**ID**: 32
**Summary**: HealthcareService availableTime daysOfWeek must be supported
**Requirement**: "HealthcareService.availableTime.daysOfWeek [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The availableTime.daysOfWeek element indicates which days of the week are available and must be supported by implementations.
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
# REQ-033
**ID**: 33
**Summary**: HealthcareService availableTime allDay must be supported
**Requirement**: "HealthcareService.availableTime.allDay [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The availableTime.allDay element indicates if the service is always available and must be supported by implementations.
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
# REQ-034
**ID**: 34
**Summary**: HealthcareService availableTime availableStartTime must be supported
**Requirement**: "HealthcareService.availableTime.availableStartTime [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The availableTime.availableStartTime element indicates the opening time of day and must be supported by implementations.
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
# REQ-035
**ID**: 35
**Summary**: HealthcareService availableTime availableEndTime must be supported
**Requirement**: "HealthcareService.availableTime.availableEndTime [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The availableTime.availableEndTime element indicates the closing time of day and must be supported by implementations.
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
# REQ-036
**ID**: 36
**Summary**: HealthcareService notAvailable must be supported
**Requirement**: "HealthcareService.notAvailable [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The notAvailable element indicates when the HealthcareService is not available and must be supported by implementations.
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
# REQ-037
**ID**: 37
**Summary**: HealthcareService notAvailable description must be supported
**Requirement**: "HealthcareService.notAvailable.description [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The notAvailable.description element provides the reason for unavailability and must be supported by implementations.
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
# REQ-038
**ID**: 38
**Summary**: HealthcareService notAvailable during must be supported
**Requirement**: "HealthcareService.notAvailable.during [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The notAvailable.during element indicates the period when service is not available and must be supported by implementations.
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
# REQ-039
**ID**: 39
**Summary**: HealthcareService availabilityExceptions must be supported
**Requirement**: "HealthcareService.availabilityExceptions [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The availabilityExceptions element provides a description of site availability exceptions and must be supported by implementations.
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
# REQ-040
**ID**: 40
**Summary**: HealthcareService endpoint must be supported
**Requirement**: "HealthcareService.endpoint [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The endpoint element provides technical endpoints for accessing services and must be supported by implementations.
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
# REQ-041
**ID**: 41
**Summary**: HealthcareService newpatients extension must be supported
**Requirement**: "HealthcareService.extension:newpatients [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The newpatients extension indicates whether new patients are being accepted and must be supported by implementations.
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
# REQ-042
**ID**: 42
**Summary**: HealthcareService deliverymethod extension must be supported
**Requirement**: "HealthcareService.extension:deliverymethod [must be supported]"
**Context**: This requirement pertains to the Plan-Net HealthcareService profile. The deliverymethod extension describes the service delivery method and must be supported by implementations.
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
# REQ-043
**ID**: 43
**Summary**: HealthcareService.active SHALL be true
**Requirement**: "HealthcareService.active SHALL be 1.1 [boolean] with Required Pattern: true"
**Context**: The Plan-Net HealthcareService profile requires that the active element be present with a cardinality of 1..1 and must have a value of true, indicating that the healthcare service record is in active use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-044
**ID**: 44
**Summary**: HealthcareService.category SHALL have at least one value
**Requirement**: "HealthcareService.category [SHALL be] 1..* [CodeableConcept] Broad category of service being performed or delivered"
**Context**: The Plan-Net HealthcareService profile requires that at least one category element be present to identify the broad category of service being performed or delivered. The category:plan-net-category slice is bound to the HealthcareServiceCategoryVS value set with required conformance.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-045
**ID**: 45
**Summary**: HealthcareService.category:plan-net-category SHALL use values from HealthcareServiceCategoryVS
**Requirement**: "HealthcareService.category:plan-net-category [SHALL use] Binding: [Healthcare Service CategoryVS] ([required])"
**Context**: When the plan-net-category slice of the category element is used, it must conform to the required HealthcareServiceCategoryVS value set defined in this implementation guide.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-046
**ID**: 46
**Summary**: HealthcareService.type SHALL use extensible binding to HealthcareServiceTypeVS
**Requirement**: "HealthcareService.type [SHALL be from] Binding: [HealthcareService Types VS] ([extensible])"
**Context**: The type element, which describes the specific type of service that may be delivered or performed, must conform to the extensible HealthcareServiceTypeVS value set. If the value set does not cover the concept, alternate codings or text may be included.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-047
**ID**: 47
**Summary**: HealthcareService.specialty SHALL use values from SpecialtiesVS
**Requirement**: "HealthcareService.specialty [SHALL use] Binding: [Specialties VS] ([required])"
**Context**: The specialty element, which describes the collection of specialties handled by the service site, must conform to the required SpecialtiesVS value set defined in this implementation guide.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-048
**ID**: 48
**Summary**: HealthcareService.notAvailable.description SHALL be present when notAvailable is used
**Requirement**: "HealthcareService.notAvailable.description [SHALL be] 1..1 [string] Reason presented to the user explaining why time not available"
**Context**: When the notAvailable element is present to indicate that the healthcare service is not available during a period of time, the description element must be present with a cardinality of 1..1 to provide the reason that can be presented to the user.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement is conditional on the presence of the notAvailable element.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-049
**ID**: 49
**Summary**: HealthcareService.providedBy SHALL reference Plan-Net Organization when present
**Requirement**: "HealthcareService.providedBy [SHALL be] 0..1 [Reference]([Plan-Net Organization]) Organization that provides this service"
**Context**: When the providedBy element is present to indicate the organization that provides the healthcare service, it must reference a Plan-Net Organization profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement is conditional on the presence of the providedBy element.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-050
**ID**: 50
**Summary**: HealthcareService.location SHALL reference Plan-Net Location when present
**Requirement**: "HealthcareService.location [SHALL be] 0..* [Reference]([Plan-Net Location]) Location(s) where service may be provided"
**Context**: When the location element is present to indicate the location(s) where the healthcare service may be provided, it must reference Plan-Net Location profile(s).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement is conditional on the presence of the location element.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-051
**ID**: 51
**Summary**: HealthcareService.coverageArea SHALL reference Plan-Net Location when present
**Requirement**: "HealthcareService.coverageArea [SHALL be] 0..* [Reference]([Plan-Net Location]) Location(s) service is intended for/available to"
**Context**: When the coverageArea element is present to indicate the location(s) that the service is available to (not where the service is provided), it must reference Plan-Net Location profile(s).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement is conditional on the presence of the coverageArea element.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-052
**ID**: 52
**Summary**: HealthcareService.endpoint SHALL reference Plan-Net Endpoint when present
**Requirement**: "HealthcareService.endpoint [SHALL be] 0..* [Reference]([Plan-Net Endpoint]) Technical endpoints providing access to electronic services operated for the healthcare service"
**Context**: When the endpoint element is present to indicate technical endpoints providing access to services operated for the specific healthcare services, it must reference Plan-Net Endpoint profile(s).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement is conditional on the presence of the endpoint element.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-053
**ID**: 53
**Summary**: HealthcareService.telecom.extension:via-intermediary SHALL reference Plan-Net profiles when present
**Requirement**: "HealthcareService.telecom.extension:via-intermediary [SHALL be] 0..* [Reference]([Plan-Net PractitionerRole] [Plan-Net OrganizationAffiliation] [Plan-Net Location] [Plan-Net Organization])"
**Context**: When the via-intermediary extension is present on telecom to indicate intermediary contact information, it must reference one of the specified Plan-Net profiles: PractitionerRole, OrganizationAffiliation, Location, or Organization.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement is conditional on the presence of the via-intermediary extension.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService
