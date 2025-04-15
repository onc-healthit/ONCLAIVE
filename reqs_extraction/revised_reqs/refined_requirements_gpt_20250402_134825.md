---
# REQ-01
**Summary**: Advertise supported canonical URL for SubscriptionTopic
**Description**: "Server SHALL advertise the canonical URLs of supported subscription topics using the CapabilityStatement SubscriptionTopic Canonical extension."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Subscription Discovery Section
---

---
# REQ-02
**Summary**: Plan Net Endpoint resources SHALL conform to the PlannetEndpoint profile.
**Description**: "Server SHALL ensure Plan Net Endpoint resources conform to the PlannetEndpoint profile."
**Verification**: Automated Testing
**Actor**: Server
**Conformance**: SHALL
**Conditional**: Not Applicable
**Source**: Examples Table
---

---
# REQ-03
**Summary**: Networks SHALL have an NPI
**Description**: "Server SHALL ensure that Networks have an NPI."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: StructureDefinition-plannet-Network.html
---

---
# REQ-04
**Summary**: Prohibit requiring consumer identification for directory queries
**Description**: "Server SHALL NOT require a directory mobile application to send consumer identifying information to query content."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations
---

---
# REQ-05
**Summary**: Populate all Must Support data elements for Health Plan API query results
**Description**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements
---

---
# REQ-06
**Summary**: Provide lastUpdate timestamp in profile data content
**Description**: "Server SHALL provide the lastUpdate timestamp as part of each profile's data content."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Client Detection of Updates Directory Content
---

---
# REQ-07
**Summary**: Support Organization Resource for Organization Information
**Description**: "Server SHALL support Organization instances to provide information about a specific organization and organizational hierarchies."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organizations and Organization Affiliations Section
---

---
# REQ-08
**Summary**: Return Status 404 for unknown resource
**Description**: "Server SHALL return Status 404 for unknown resources."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---

---
# REQ-09
**Summary**: Support JSON source formats
**Description**: "Server SHALL support JSON source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---

---
# REQ-10
**Summary**: Support search-type and read interactions for Endpoint
**Description**: "Server SHALL support `search-type` and `read` interactions for the Endpoint resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Profile Interaction Summary
---

---
# REQ-11
**Summary**: Support _include for Endpoint:organization
**Description**: "Server SHALL support the _include parameter for Endpoint:organization."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria
---

---
# REQ-12
**Summary**: Support Plan-Net HealthcareService profile
**Description**: "Server SHALL support the Plan-Net HealthcareService profile."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService Section
---

---
# REQ-13
**Summary**: Support _revincludes for HealthcareService
**Description**: "Server SHALL support the _revincludes PractitionerRole:service and OrganizationAffiliation:service for HealthcareService."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria
---

---
# REQ-14
**Summary**: Support location search parameter for HealthcareService
**Description**: "Server SHALL support the location search parameter for HealthcareService."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---

---
# REQ-15
**Summary**: Support search-type and read interactions for InsurancePlan
**Description**: "Server SHALL support `search-type` and `read` interactions for the InsurancePlan resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Profile Interaction Summary
---

---
# REQ-16
**Summary**: Support _includes for InsurancePlan
**Description**: "Server SHALL support _includes for InsurancePlan:administered-by, InsurancePlan:owned-by, and InsurancePlan:coverage-area."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Fetch and Search Criteria
---

---
# REQ-17
**Summary**: Support type search parameter for InsurancePlan
**Description**: "Server SHALL support the type search parameter for InsurancePlan."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---

---
# REQ-18
**Summary**: Support search-type and read interactions for Location resource
**Description**: "Server SHALL support `search-type` and `read` interactions for the Location resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Profile Interaction Summary
---

---
# REQ-19
**Summary**: Support _include for Location:endpoint
**Description**: "Server SHALL support the _include parameter for Location:endpoint."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---

---
# REQ-20
**Summary**: Support organization search parameter for Location resource
**Description**: "Server SHALL support the organization search parameter for Location."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary
---

---
# REQ-21
**Summary**: Support search-type and read interactions for Organization resource
**Description**: "Server SHALL support `search-type` and `read` interactions for the Organization resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Profile Interaction Summary
---

---
# REQ-22
**Summary**: Support _revinclude for PractitionerRole:organization
**Description**: "Server SHALL support the _revinclude parameter for PractitionerRole:organization."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria
---

---
# REQ-23
**Summary**: Support name search parameter for Organization resource
**Description**: "Server SHALL support the name search parameter for Organization."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Search Parameter Summary
---

---
# REQ-24
**Summary**: Support OrganizationAffiliation Resource
**Description**: "Server SHALL support the OrganizationAffiliation resource."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: OrganizationAffiliation
---

---
# REQ-25
**Summary**: Support search-type and read interactions for OrganizationAffiliation
**Description**: "Server SHALL support `search-type` and `read` interactions for the OrganizationAffiliation resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: OrganizationAffiliation - Profile Interaction Summary
---

---
# REQ-26
**Summary**: Support Practitioner Resource
**Description**: "Server SHALL support the Practitioner resource."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Practitioner
---

---
# REQ-27
**Summary**: Support search-type and read interactions for Practitioner
**Description**: "Server SHALL support `search-type` and `read` interactions for the Practitioner resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Practitioner - Profile Interaction Summary
---

---
# REQ-28
**Summary**: Support PractitionerRole search-type interaction
**Description**: "Server SHALL support `search-type` interactions for the PractitionerRole resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: PractitionerRole Section, Profile Interaction Summary
---

---
# REQ-29
**Summary**: Support PractitionerRole include for organization
**Description**: "Server SHALL support the _include parameter for PractitionerRole:organization."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: PractitionerRole Section, Fetch and Search Criteria
---

---
# REQ-30
**Summary**: Support PractitionerRole search by practitioner
**Description**: "Server SHALL support the practitioner search parameter for PractitionerRole."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: PractitionerRole Section, Search Parameter Summary
---

---
# REQ-31
**Summary**: Support PractitionerRole search by location
**Description**: "Server SHALL support the location search parameter for PractitionerRole."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: PractitionerRole Section, Search Parameter Summary
---

---
# REQ-32
**Summary**: Declare conformance to Plan-Net CapabilityStatement
**Description**: "System SHALL declare conformance to one or more Plan-Net CapabilityStatements."
**Verification**: Inspection
**Actor**: System
**Conformance**: SHALL
**Conditional**: False
**Source**: Artifacts Summary/Behavior: Capability Statements
---

---
# REQ-33
**Summary**: Support the `endpoint-organization` search parameter for the Endpoint resource.
**Description**: "Server SHALL support the `endpoint-organization` parameter to select Endpoints managed by a specified organization."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Behavior: Search Parameters / Plannet_sp_endpoint_organization
---

---
# REQ-34
**Summary**: Support the `coverage-area` search parameter for the HealthcareService resource.
**Description**: "Server SHALL support the `coverage-area` parameter to select services available in a specified region."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Behavior: Search Parameters / Plannet_sp_healthcareservice_coverage_area
---

---
# REQ-35
**Summary**: Support the `organization` search parameter for the HealthcareService resource.
**Description**: "Server SHALL support the `organization` parameter to select HealthcareServices provided by a specified organization."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Behavior: Search Parameters / Plannet_sp_healthcareservice_organization
---

---
# REQ-36
**Summary**: Support the `service-category` search parameter for the HealthcareService resource.
**Description**: "Server SHALL support the `service-category` parameter to select HealthcareServices by service category."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Behavior: Search Parameters / Plannet_sp_healthcareservice_category
---

---
# REQ-37
**Summary**: Support the `administered-by` search parameter for the InsurancePlan resource.
**Description**: "Server SHALL support the `administered-by` parameter to select products administered by a specified organization."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Behavior: Search Parameters / Plannet_sp_insuranceplan_administered_by
---

---
# REQ-38
**Summary**: Support the `address-city` search parameter for the Location resource.
**Description**: "Server SHALL support the `address-city` parameter to select Locations with specified city."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Behavior: Search Parameters / Plannet_sp_location_address_city
---

---
# REQ-39
**Summary**: Support the `location-address-state` search parameter
**Description**: "Server SHALL support the `location-address-state` parameter to select Locations with specified state."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: SearchParameter-location-address-state
---

---
# REQ-40
**Summary**: Support the `organization-address` search parameter
**Description**: "Server SHALL support the `organization-address` parameter to select organizations with specified address."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: SearchParameter-organization-address
---

---
# REQ-41
**Summary**: Support the `organization-type` search parameter
**Description**: "Server SHALL support the `organization-type` parameter to select Organizations by specified type."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: SearchParameter-organization-type
---

---
# REQ-42
**Summary**: Support the `practitioner-family-name` search parameter
**Description**: "Server SHALL support the `practitioner-family-name` parameter to select Practitioners by family name."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: SearchParameter-practitioner-family-name
---

---
# REQ-43
**Summary**: Plan-Net Endpoint resources SHALL use the Plan-Net Endpoint profile.
**Description**: "Server SHALL ensure that Plan-Net Endpoint resources use the Plan-Net Endpoint profile."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Structures: Resource Profiles, Plan-Net Endpoint
---

---
# REQ-44
**Summary**: Support Accessibility Extension
**Description**: "Server SHALL support the Accessibility Extension to describe accessibility options."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Structures: Extension Definitions - Accessibility
---

---
# REQ-45
**Summary**: Constrain Endpoint Payload Types to NA
**Description**: "Server SHALL constrain Endpoint Payload Types to NA (Not Applicable)."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Terminology: Code Systems - Endpoint Payload Types
---