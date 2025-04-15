---
# REQ-01
**Summary**: Advertise supported canonical URL for SubscriptionTopic
**Description**: "In order to allow for discovery of supported subscription topics, this guide defines the CapabilityStatement SubscriptionTopic Canonical extension. The extension allows server implementers to advertise the canonical URLs of topics available to clients."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Subscription Discovery Section
---
---
# REQ-02
**Summary**: Plan Net Endpoint resources SHALL conform to the PlannetEndpoint profile.
**Description**: "**Example**   **ResourceType**   **Profiles** \n[AcmeOfCTPortalEndpoint](Endpoint-AcmeOfCTPortalEndpoint.html)   [Endpoint](http://hl7.org/fhir/R4/endpoint.html)   [PlannetEndpoint](StructureDefinition-plannet-Endpoint.html)"
**Verification**: Automated Testing
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Examples Table
---
---
# REQ-03
**Summary**: Plan Net HealthcareService resources SHALL conform to the PlannetHealthcareService profile.
**Description**: "**Example**   **ResourceType**   **Profiles** \n[BurrClinicServices](HealthcareService-BurrClinicServices.html)   [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html)   [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html)"
**Verification**: Automated Testing
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Examples Table
---
---
# REQ-04
**Summary**: Plan Net InsurancePlan resources SHALL conform to the PlannetInsurancePlan profile.
**Description**: "**Example**   **ResourceType**   **Profiles** \n[AcmeQHPBronze](InsurancePlan-AcmeQHPBronze.html)   [InsurancePlan](http://hl7.org/fhir/R4/insuranceplan.html)   [PlannetInsurancePlan](StructureDefinition-plannet-InsurancePlan.html)"
**Verification**: Automated Testing
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Examples Table
---
---
# REQ-05
**Summary**: Plan Net Location resources SHALL conform to the PlannetLocation profile.
**Description**: "**Example**   **ResourceType**   **Profiles** \n[CancerClinicLoc](Location-CancerClinicLoc.html)   [Location](http://hl7.org/fhir/R4/location.html)   [PlannetLocation](StructureDefinition-plannet-Location.html)"
**Verification**: Automated Testing
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Examples Table 
---
---
# REQ-06
**Summary**: Use of code `CT` for State
**Description**: "Use code `CT`  - `State` in the element 'address.state'."
**Verification**: Test
**Actor**: Server/Client
**Conformance**: SHALL
**Conditional**: False
**Source**: Location-StateOfCTLocation.html
---
---
# REQ-07
**Summary**: Use of  USPS postal code for State
**Description**: "Use a valid US Postal Service code for the state of 'CT'."
**Verification**: Test
**Actor**: Server/Client
**Conformance**: SHALL
**Conditional**: False
**Source**: Location-StateOfCTLocation.html
---
---
# REQ-08
**Summary**: Networks SHALL have an NPI
**Description**: "Networks SHALL have an NPI."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: StructureDefinition-plannet-Network.html
---
---
# REQ-09
**Summary**: Organizations SHALL have an NPI
**Description**: "Organizations SHALL have an NPI."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: StructureDefinition-plannet-Organization.html
---
---
# REQ-10
**Description**: "The participating organization SHALL be identified by their NPI in the identifier with a system of  http://hl7.org/fhir/sid/us-npi."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: StructureDefinition-plannet-OrganizationAffiliation.html
---
---
# REQ-11
**Summary**: Practitioner Role SHALL have a Code
**Description**: "Practitioner Roles SHALL have at least one code."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: StructureDefinition-plannet-PractitionerRole.html
---
---
# REQ-12
**Summary**: Do not require authentication for Plan-Net service access
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations
---
---
# REQ-13
**Summary**: Prohibit storage of consumer-identifying information
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations
---
---
# REQ-14
**Summary**: Prohibit requiring consumer identification for directory queries
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations
---
---
# REQ-15
**Summary**: Prohibit sending consumer identifiable information in directory queries
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Inspection
**Actor**: Directory Mobile Application
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations
---
---
# REQ-16
**Summary**: Populate all Must Support data elements for Health Plan API query results
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements
---
---
# REQ-17
**Summary**: Omit data elements with minimum cardinality 0 when information is not present
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0 , the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements
---
---
# REQ-18
**Summary**: Provide reason for missing data elements with minimum cardinality > 0
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements
---
---
# REQ-19
**Summary**: Process resource instances containing Must Support data elements without errors
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements
---
---
# REQ-20
**Summary**: Display or store data elements for human use
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Actor**: Application
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements
---
---
# REQ-21
**Summary**: Interpret missing Must Support data elements as not present in the Health Plan API system
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements
---
---
# REQ-22
**Summary**: Process resource instances containing Must Support data elements asserting missing information
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information"
**Verification**: Test
**Actor**: Consumer App
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements
---
---
# REQ-23
**Summary**: Provide lastUpdate timestamp in profile data content
**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Client Detection of Updates Directory Content
---
---
# REQ-24
**Summary**: Define HealthcareServices for Service Search
**Description**: "All organizations that provide service should define an appropriate set of HealthcareServices to facilitate search."
**Verification**: Inspection
**Actor**: Organization
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService Section
---
---
# REQ-25
**Summary**: Link Insurance Plans to Networks
**Description**: "Each payer will offer one or more products -- Insurance Plans -- and each plan is associated with one or more Networks."
**Verification**: Inspection
**Actor**: Payer
**Conformance**: SHALL
**Conditional**: False
**Source**: Insurance Plan and Network Section
---
---
# REQ-26
**Summary**: Associate Practitioners and Organizations with Networks
**Description**: "Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively."
**Verification**: Inspection
**Actor**: Practitioners and Organizations
**Conformance**: SHALL
**Conditional**: False
**Source**: Insurance Plan and Network Section
---
---
# REQ-27
**Summary**: Support Organization Resource for Organization Information
**Description**: "Organization instances provide information about a specific organization and organizational hierarchies, including organization name, specialty, type, address and contact information."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organizations and Organization Affiliations Section
---
---
# REQ-28
**Summary**: Support OrganizationAffiliation Resource for Role Descriptions
**Description**: "Organization Affiliation instances describe a role, and link a participating organization that provides or performs the role, with an organization where that role is available, and also links the participating organization to a HealthcareServices and networks."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organizations and Organization Affiliations Section
---
---
# REQ-29
**Summary**: Support HealthcareService Association with Networks via OrganizationAffiliation
**Description**: "OrganizationalAffiliation can also be used to associate a HealthcareService provided by an organization with networks."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organizations and Organization Affiliations Section
---
---
# REQ-30
**Summary**: Support Endpoint Resource for Technical Details of Electronic Service Endpoints
**Description**: "An Endpoint instance provides  technical details of an endpoint that can be used for electronic services, such as a portal or FHIR REST services, messaging or operations, or DIRECT messaging."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoints Section 
---
---
# REQ-31
**Summary**: Support all defined profiles
**Description**: "The Plan-Net Server **SHALL**:
1. Support all profiles defined in this Implementation Guide."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-32
**Summary**: Implement RESTful behavior according to FHIR specification
**Description**: "The Plan-Net Server **SHALL**:
2. Implement the RESTful behavior according to the FHIR specification."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-33
**Summary**: Return Status 400 for invalid parameter
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 400): invalid parameter"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-34
**Summary**: Return Status 401/4xx for unauthorized request
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 401/4xx): unauthorized request"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-35
**Summary**: Return Status 403 for insufficient scope
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 403): insufficient scope"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-36
**Summary**: Return Status 404 for unknown resource
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 404): unknown resource"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-37
**Summary**: Return Status 410 for deleted resource
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 410): deleted resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-38
**Summary**: Support JSON source formats
**Description**: "The Plan-Net Server **SHALL**:
4. Support json source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-39
**Summary**: Identify supported Plan-Net profiles in meta.profile attribute
**Description**: "The Plan-Net Server **SHALL**:
5. Identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-40
**Summary**: Support searchParameters individually and in combination
**Description**: "The Plan-Net Server **SHALL**:
6. Support the searchParameters on each profile individually and in combination."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-41
**Summary**: Support forward and reverse chaining for search parameters with 'chain' property
**Description**: "The Plan-Net Server **SHALL**:
1.Support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-42
**Summary**: Support XML source formats
**Description**: "The Plan-Net Server **SHOULD**:
1. Support xml source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-43
**Summary**: Reject unauthorized requests with HTTP 401
**Description**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, Security
---
---
# REQ-44
**Summary**: Support Plan-Net Endpoint profile
**Description**: "Supported Profiles: [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint Section
---
---
# REQ-45
**Summary**: Support search-type and read interactions for Endpoint
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Profile Interaction Summary
---
---
# REQ-46
**Summary**: Support vread interaction for Endpoint
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Endpoint - Profile Interaction Summary
---
---
# REQ-47
**Summary**: Return Endpoint resource using ID
**Description**: "A Server **SHALL** be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria
---
---
# REQ-48
**Summary**: Return Endpoint resource using ID and version ID
**Description**: "A Server **SHOULD** be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria
---
---
# REQ-49
**Summary**: Support _include for Endpoint:organization
**Description**: "A Server **SHALL** be capable of supporting the following _includes: Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria
---
---
# REQ-50
**Summary**: Support organization search parameter for Endpoint
**Description**: "**SHALL**   [organization](SearchParameter-endpoint-organization.html)   reference   `GET [base]/Endpoint?organization=[organization]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Search Parameter Summary
---

