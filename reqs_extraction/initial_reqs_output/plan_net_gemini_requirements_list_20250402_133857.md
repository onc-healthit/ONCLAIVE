## REQ-1

**Summary**: HealthcareService.deliveryMethod binding strength
**Description**: "Binding: Example: HealthcareService Delivery Method (Extensible)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: profiles.md/Profiles

## REQ-2

**Summary**: Organization.type binding strength
**Description**: "Binding: Example: Network Type (Extensible)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: profiles.md/Profiles 
## REQ-01

**Summary**: Advertise supported canonical URL for SubscriptionTopic
**Description**: "In order to allow for discovery of supported subscription topics, this guide defines the CapabilityStatement SubscriptionTopic Canonical extension. The extension allows server implementers to advertise the canonical URLs of topics available to clients."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Subscription Discovery Section

## REQ-02

**Summary**: Support out-of-band topic discovery
**Description**: "FHIR R4 servers MAY choose to leave topic discovery completely out-of-band and part of other steps, such as registration or integration."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: MAY, Conditional: False
**Source**: Subscription Configuration Section 
Since the provided text does not contain any conformance language or testable requirements related to FHIR implementation, no requirements can be extracted using the INCOSE format. 
Since the provided text does not contain any testable requirements, I cannot create any INCOSE-style requirements. The text primarily focuses on introductory elements and does not specify any functionality or behavior that can be translated into testable requirements. 
## REQ-01

**Summary**: Plan Net Endpoint resources SHALL conform to the PlannetEndpoint profile.
**Description**: "**Example**   **ResourceType**   **Profiles** \n[AcmeOfCTPortalEndpoint](Endpoint-AcmeOfCTPortalEndpoint.html)   [Endpoint](http://hl7.org/fhir/R4/endpoint.html)   [PlannetEndpoint](StructureDefinition-plannet-Endpoint.html)"
**Verification**: Automated Testing
**Notes**: Actor: Server, Conformance: SHALL, Conditional: Not Applicable
**Source**: Examples Table

## REQ-02

**Summary**: Plan Net HealthcareService resources SHALL conform to the PlannetHealthcareService profile.
**Description**: "**Example**   **ResourceType**   **Profiles** \n[BurrClinicServices](HealthcareService-BurrClinicServices.html)   [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html)   [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html)"
**Verification**: Automated Testing
**Notes**: Actor: Server, Conformance: SHALL, Conditional: Not Applicable
**Source**: Examples Table

## REQ-03

**Summary**: Plan Net InsurancePlan resources SHALL conform to the PlannetInsurancePlan profile.
**Description**: "**Example**   **ResourceType**   **Profiles** \n[AcmeQHPBronze](InsurancePlan-AcmeQHPBronze.html)   [InsurancePlan](http://hl7.org/fhir/R4/insuranceplan.html)   [PlannetInsurancePlan](StructureDefinition-plannet-InsurancePlan.html)"
**Verification**: Automated Testing
**Notes**: Actor: Server, Conformance: SHALL, Conditional: Not Applicable
**Source**: Examples Table

## REQ-04

**Summary**: Plan Net Location resources SHALL conform to the PlannetLocation profile.
**Description**: "**Example**   **ResourceType**   **Profiles** \n[CancerClinicLoc](Location-CancerClinicLoc.html)   [Location](http://hl7.org/fhir/R4/location.html)   [PlannetLocation](StructureDefinition-plannet-Location.html)"
**Verification**: Automated Testing
**Notes**: Actor: Server, Conformance: SHALL, Conditional: Not Applicable
**Source**: Examples Table 
## REQ-01

**Summary**: Use of code `CT` for State
**Description**: "Use code `CT`  - `State` in the element 'address.state'."
**Verification**: Test
**Notes**: Actor: Server/Client, Conformance: SHALL, Conditional: False
**Source**: Location-StateOfCTLocation.html

## REQ-02

**Summary**: Use of  USPS postal code for State
**Description**: "Use a valid US Postal Service code for the state of 'CT'."
**Verification**: Test
**Notes**: Actor: Server/Client, Conformance: SHALL, Conditional: False
**Source**: Location-StateOfCTLocation.html

## REQ-03

**Summary**: Networks SHALL have an NPI
**Description**: "Networks SHALL have an NPI."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: StructureDefinition-plannet-Network.html

## REQ-04

**Summary**: Organizations SHALL have an NPI
**Description**: "Organizations SHALL have an NPI."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: StructureDefinition-plannet-Organization.html

## REQ-05

**Description**: "The participating organization SHALL be identified by their NPI in the identifier with a system of  http://hl7.org/fhir/sid/us-npi."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: StructureDefinition-plannet-OrganizationAffiliation.html

## REQ-06

**Summary**: Practitioner Role SHALL have a Code
**Description**: "Practitioner Roles SHALL have at least one code."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: StructureDefinition-plannet-PractitionerRole.html
## REQ-01

**Summary**: Do not require authentication for Plan-Net service access
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Implementation Notes/Privacy Considerations

## REQ-02

**Summary**: Prohibit storage of consumer-identifying information
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Implementation Notes/Privacy Considerations

## REQ-03

**Summary**: Prohibit requiring consumer identification for directory queries
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL NOT, Conditional: False
**Source**: Implementation Notes/Privacy Considerations

## REQ-04

**Summary**: Prohibit sending consumer identifiable information in directory queries
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Inspection
**Notes**: Actor: Directory Mobile Application, Conformance: SHALL NOT, Conditional: False
**Source**: Implementation Notes/Privacy Considerations

## REQ-05

**Summary**: Populate all Must Support data elements for Health Plan API query results
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Notes**: Actor: Health Plan API, Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

## REQ-06

**Summary**: Omit data elements with minimum cardinality 0 when information is not present
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0 , the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Notes**: Actor: Health Plan API, Conformance: SHALL NOT, Conditional: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

## REQ-07

**Summary**: Provide reason for missing data elements with minimum cardinality > 0
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Notes**: Actor: Health Plan API, Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

## REQ-08

**Summary**: Process resource instances containing Must Support data elements without errors
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Notes**: Actor: Application, Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Application Requirements

## REQ-09

**Summary**: Display or store data elements for human use
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Notes**: Actor: Application, Conformance: SHOULD, Conditional: False
**Source**: Implementation Notes/Must Support/Application Requirements

## REQ-10

**Summary**: Interpret missing Must Support data elements as not present in the Health Plan API system
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Notes**: Actor: Application, Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Application Requirements

## REQ-11

**Summary**: Process resource instances containing Must Support data elements asserting missing information
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information"
**Verification**: Test
**Notes**: Actor: Consumer App, Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Application Requirements

## REQ-12

**Summary**: Provide lastUpdate timestamp in profile data content
**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Client Detection of Updates Directory Content
## REQ-01

**Summary**: Define HealthcareServices for Service Search
**Description**: "All organizations that provide service should define an appropriate set of HealthcareServices to facilitate search."
**Verification**: Inspection
**Notes**: Actor: Organization, Conformance: SHOULD, Conditional: False
**Source**: HealthcareService Section

## REQ-02

**Summary**: Link Insurance Plans to Networks
**Description**: "Each payer will offer one or more products -- Insurance Plans -- and each plan is associated with one or more Networks."
**Verification**: Inspection
**Notes**: Actor: Payer, Conformance: SHALL, Conditional: False
**Source**: Insurance Plan and Network Section

## REQ-03

**Summary**: Associate Practitioners and Organizations with Networks
**Description**: "Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively."
**Verification**: Inspection
**Notes**: Actor: Practitioners and Organizations, Conformance: SHALL, Conditional: False
**Source**: Insurance Plan and Network Section
## REQ-01

**Summary**: Support Organization Resource for Organization Information
**Description**: "Organization instances provide information about a specific organization and organizational hierarchies, including organization name, specialty, type, address and contact information."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organizations and Organization Affiliations Section

## REQ-02

**Summary**: Support OrganizationAffiliation Resource for Role Descriptions
**Description**: "Organization Affiliation instances describe a role, and link a participating organization that provides or performs the role, with an organization where that role is available, and also links the participating organization to a HealthcareServices and networks."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organizations and Organization Affiliations Section

## REQ-03

**Summary**: Support HealthcareService Association with Networks via OrganizationAffiliation
**Description**: "OrganizationalAffiliation can also be used to associate a HealthcareService provided by an organization with networks."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organizations and Organization Affiliations Section

## REQ-04

**Summary**: Support Endpoint Resource for Technical Details of Electronic Service Endpoints
**Description**: "An Endpoint instance provides  technical details of an endpoint that can be used for electronic services, such as a portal or FHIR REST services, messaging or operations, or DIRECT messaging."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoints Section 
## REQ-01

**Summary**: Support all defined profiles
**Description**: "The Plan-Net Server **SHALL**:
1. Support all profiles defined in this Implementation Guide."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-02

**Summary**: Implement RESTful behavior according to FHIR specification
**Description**: "The Plan-Net Server **SHALL**:
2. Implement the RESTful behavior according to the FHIR specification."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-03

**Summary**: Return Status 400 for invalid parameter
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 400): invalid parameter"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-04

**Summary**: Return Status 401/4xx for unauthorized request
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 401/4xx): unauthorized request"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-05

**Summary**: Return Status 403 for insufficient scope
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 403): insufficient scope"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-06

**Summary**: Return Status 404 for unknown resource
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 404): unknown resource"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-07

**Summary**: Return Status 410 for deleted resource
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 410): deleted resource."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-08

**Summary**: Support JSON source formats
**Description**: "The Plan-Net Server **SHALL**:
4. Support json source formats for all Plan-Net interactions."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-09

**Summary**: Identify supported Plan-Net profiles in meta.profile attribute
**Description**: "The Plan-Net Server **SHALL**:
5. Identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-10

**Summary**: Support searchParameters individually and in combination
**Description**: "The Plan-Net Server **SHALL**:
6. Support the searchParameters on each profile individually and in combination."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-11

**Summary**: Support forward and reverse chaining for search parameters with 'chain' property
**Description**: "The Plan-Net Server **SHALL**:
1.Support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-12

**Summary**: Support XML source formats
**Description**: "The Plan-Net Server **SHOULD**:
1. Support xml source formats for all Plan-Net interactions."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

## REQ-13

**Summary**: Reject unauthorized requests with HTTP 401
**Description**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, Security
```
## REQ-01

**Summary**: Support Plan-Net Endpoint profile
**Description**: "Supported Profiles: [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint Section

## REQ-02

**Summary**: Support search-type and read interactions for Endpoint
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint - Profile Interaction Summary

## REQ-03

**Summary**: Support vread interaction for Endpoint
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Endpoint - Profile Interaction Summary

## REQ-04

**Summary**: Return Endpoint resource using ID
**Description**: "A Server **SHALL** be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint - Fetch and Search Criteria

## REQ-05

**Summary**: Return Endpoint resource using ID and version ID
**Description**: "A Server **SHOULD** be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Endpoint - Fetch and Search Criteria

## REQ-06

**Summary**: Support _include for Endpoint:organization
**Description**: "A Server **SHALL** be capable of supporting the following _includes: Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint - Fetch and Search Criteria

## REQ-07

**Summary**: Support organization search parameter for Endpoint
**Description**: "**SHALL**   [organization](SearchParameter-endpoint-organization.html)   reference   `GET [base]/Endpoint?organization=[organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint - Search Parameter Summary

## REQ-08

**Summary**: Support _id search parameter for Endpoint
**Description**: "**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/Endpoint?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint - Search Parameter Summary

## REQ-09

**Summary**: Support _lastUpdated search parameter for Endpoint
**Description**: "**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/Endpoint?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint - Search Parameter Summary

## REQ-10

**Summary**: Support Plan-Net HealthcareService profile
**Description**: "Supported Profiles: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService Section

## REQ-11

**Summary**: Support search-type and read interactions for HealthcareService
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Profile Interaction Summary

## REQ-12

**Summary**: Support vread interaction for HealthcareService
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: HealthcareService - Profile Interaction Summary

## REQ-13

**Summary**: Return HealthcareService resource using ID
**Description**: "A Server **SHALL** be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Fetch and Search Criteria

## REQ-14

**Summary**: Return HealthcareService resource using ID and version ID
**Description**: "A Server **SHOULD** be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: HealthcareService - Fetch and Search Criteria

## REQ-15

**Summary**: Support _includes for HealthcareService
**Description**: "A Server **SHALL** be capable of supporting the following _includes: HealthcareService:location - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:location` HealthcareService:coverage-area - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:coverage-area` HealthcareService:organization - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:organization` HealthcareService:endpoint - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:endpoint`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Fetch and Search Criteria

## REQ-16

**Summary**: Support _revincludes for HealthcareService
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes: PractitionerRole:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=PractitionerRole:service` OrganizationAffiliation:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=OrganizationAffiliation:service`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Fetch and Search Criteria

## REQ-17

**Summary**: Support location search parameter for HealthcareService
**Description**: "**SHALL**   [location](SearchParameter-healthcareservice-location.html)   reference   `GET [base]/HealthcareService?location=[location]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-18

**Summary**: Support coverage-area search parameter for HealthcareService
**Description**: "**SHALL**   [coverage-area](SearchParameter-healthcareservice-coverage-area.html)   reference   `GET [base]/HealthcareService?coverage-area=[coverage-area]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-19

**Summary**: Support organization search parameter for HealthcareService
**Description**: "**SHALL**   [organization](SearchParameter-healthcareservice-organization.html)   reference   `GET [base]/HealthcareService?organization=[organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-20

**Summary**: Support endpoint search parameter for HealthcareService
**Description**: "**SHALL**   [endpoint](SearchParameter-healthcareservice-endpoint.html)   reference   `GET [base]/HealthcareService?endpoint=[endpoint]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-21

**Summary**: Support name search parameter for HealthcareService
**Description**: "**SHALL**   [name](SearchParameter-healthcareservice-name.html)   string   `GET [base]/HealthcareService?name=[name]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-22

**Summary**: Support service-category search parameter for HealthcareService
**Description**: "**SHALL**   [service-category](SearchParameter-healthcareservice-service-category.html)   token   `GET [base]/HealthcareService?service-category=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-23

**Summary**: Support service-type search parameter for HealthcareService
**Description**: "**SHALL**   [service-type](SearchParameter-healthcareservice-service-type.html)   token   `GET [base]/HealthcareService?service-type=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-24

**Summary**: Support specialty search parameter for HealthcareService
**Description**: "**SHALL**   [specialty](SearchParameter-healthcareservice-specialty.html)   token   `GET [base]/HealthcareService?specialty=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-25

**Summary**: Support _id search parameter for HealthcareService
**Description**: "**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/HealthcareService?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-26

**Summary**: Support _lastUpdated search parameter for HealthcareService
**Description**: "**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/HealthcareService?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService - Search Parameter Summary

## REQ-27

**Summary**: Support Plan-Net InsurancePlan profile
**Description**: "Supported Profiles: [Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan Section

## REQ-28

**Summary**: Support search-type and read interactions for InsurancePlan
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Profile Interaction Summary

## REQ-29

**Summary**: Support vread interaction for InsurancePlan
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: InsurancePlan - Profile Interaction Summary

## REQ-30

**Summary**: Return InsurancePlan resource using ID
**Description**: "A Server **SHALL** be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Fetch and Search Criteria

## REQ-31

**Summary**: Return InsurancePlan resource using ID and version ID
**Description**: "A Server **SHOULD** be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: InsurancePlan - Fetch and Search Criteria

## REQ-32

**Summary**: Support _includes for InsurancePlan
**Description**: "A Server **SHALL** be capable of supporting the following _includes: InsurancePlan:administered-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:administered-by` InsurancePlan:owned-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:owned-by` InsurancePlan:coverage-area - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:coverage-area`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Fetch and Search Criteria

## REQ-33

**Summary**: Support administered-by search parameter for InsurancePlan
**Description**: "**SHALL**   [administered-by](SearchParameter-insuranceplan-administered-by.html)   reference   `GET [base]/InsurancePlan?administered-by=[administered-by]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary

## REQ-34

**Summary**: Support owned-by search parameter for InsurancePlan
**Description**: "**SHALL**   [owned-by](SearchParameter-insuranceplan-owned-by.html)   reference   `GET [base]/InsurancePlan?owned-by=[owned-by]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary

## REQ-35

**Summary**: Support coverage-area search parameter for InsurancePlan
**Description**: "**SHALL**   [coverage-area](SearchParameter-insuranceplan-coverage-area.html)   reference   `GET [base]/InsurancePlan?coverage-area=[coverage-area]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary

## REQ-36

**Summary**: Support name search parameter for InsurancePlan
**Description**: "**SHALL**   [name](SearchParameter-insuranceplan-name.html)   string   `GET [base]/InsurancePlan?name=[name]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary

## REQ-37

**Summary**: Support plan-type search parameter for InsurancePlan
**Description**: "**SHALL**   [plan-type](SearchParameter-insuranceplan-plan-type.html)   token   `GET [base]/InsurancePlan?plan-type=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary

## REQ-38

**Summary**: Support identifier search parameter for InsurancePlan
**Description**: "**SHALL**   [identifier](SearchParameter-insuranceplan-identifier.html)   token   `GET [base]/InsurancePlan?identifier=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary

## REQ-39

**Summary**: Support _id search parameter for InsurancePlan
**Description**: "**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/InsurancePlan?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary

## REQ-40

**Summary**: Support _lastUpdated search parameter for InsurancePlan
**Description**: "**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/InsurancePlan?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary

## REQ-41

**Summary**: Support type search parameter for InsurancePlan
**Description**: "**SHALL**   [type](SearchParameter-insuranceplan-type.html)   token   `GET [base]/InsurancePlan?type=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan - Search Parameter Summary
## REQ-01

**Summary**: Support Plan-Net Location profile for Location resource
**Description**: "Supported Profiles: [Plan-Net Location](StructureDefinition-plannet-Location.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section

## REQ-02

**Summary**: Support search-type and read interactions for Location resource
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Profile Interaction Summary

## REQ-03

**Summary**: Support vread interaction for Location resource
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Location Section, Profile Interaction Summary

## REQ-04

**Summary**: Return Location resource using ID
**Description**: "A Server SHALL be capable of returning a Location resource using: `GET [base]/Location/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-05

**Summary**: Return Location resource using ID and version ID
**Description**: "A Server SHOULD be capable of returning a Location resource using: `GET [base]/Location/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-06

**Summary**: Support _include for Location:endpoint
**Description**: "A Server SHALL be capable of supporting the following _includes: Location:endpoint - `GET [base]/Location?[parameter=value]&_include=Location:endpoint`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-07

**Summary**: Support _include for Location:organization
**Description**: "A Server SHALL be capable of supporting the following _includes: Location:organization - `GET [base]/Location?[parameter=value]&_include=Location:organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-08

**Summary**: Support _include for Location:partof
**Description**: "A Server SHALL be capable of supporting the following _includes: Location:partof - `GET [base]/Location?[parameter=value]&_include=Location:partof`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-09

**Summary**: Support _revinclude for HealthcareService:location
**Description**: "A Server SHALL be capable of supporting the following _revincludes: HealthcareService:location - `GET [base]/Location?[parameter=value]&_revinclude=HealthcareService:location`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-10

**Summary**: Support _revinclude for InsurancePlan:coverage-area
**Description**: "A Server SHALL be capable of supporting the following _revincludes: InsurancePlan:coverage-area - `GET [base]/Location?[parameter=value]&_revinclude=InsurancePlan:coverage-area`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-11

**Summary**: Support _revinclude for OrganizationAffiliation:location
**Description**: "A Server SHALL be capable of supporting the following _revincludes: OrganizationAffiliation:location - `GET [base]/Location?[parameter=value]&_revinclude=OrganizationAffiliation:location`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-12

**Summary**: Support _revinclude for PractitionerRole:location
**Description**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:location - `GET [base]/Location?[parameter=value]&_revinclude=PractitionerRole:location`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

## REQ-13

**Summary**: Support partof search parameter for Location resource
**Description**: "SHALL [partof](SearchParameter-location-partof.html) reference `GET [base]/Location?partof=[partof]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-14

**Summary**: Support organization search parameter for Location resource
**Description**: "SHALL [organization](SearchParameter-location-organization.html) reference `GET [base]/Location?organization=[organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-15

**Summary**: Support endpoint search parameter for Location resource
**Description**: "SHALL [endpoint](SearchParameter-location-endpoint.html) reference `GET [base]/Location?endpoint=[endpoint]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-16

**Summary**: Support address-city search parameter for Location resource
**Description**: "SHALL [address-city](SearchParameter-location-address-city.html) string `GET [base]/Location?address-city=[address-city]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-17

**Summary**: Support address-state search parameter for Location resource
**Description**: "SHALL [address-state](SearchParameter-location-address-state.html) string `GET [base]/Location?address-state=[address-state]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-18

**Summary**: Support address-postalcode search parameter for Location resource
**Description**: "SHALL [address-postalcode](SearchParameter-location-address-postalcode.html) string `GET [base]/Location?address-postalcode=[address-postalcode]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-19

**Summary**: Support address search parameter for Location resource
**Description**: "SHALL [address](SearchParameter-location-address.html) string `GET [base]/Location?address=[address]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-20

**Summary**: Support type search parameter for Location resource
**Description**: "SHALL [type](SearchParameter-location-type.html) token `GET [base]/Location?type=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-21

**Summary**: Support _id search parameter for Location resource
**Description**: "SHALL [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/Location?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-22

**Summary**: Support _lastUpdated search parameter for Location resource
**Description**: "SHALL [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/Location?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary

## REQ-23

**Summary**: Support Plan-Net Network and Plan-Net Organization profiles for Organization resource
**Description**: "Supported Profiles: [Plan-Net Network](StructureDefinition-plannet-Network.html), [Plan-Net Organization](StructureDefinition-plannet-Organization.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section

## REQ-24

**Summary**: Support search-type and read interactions for Organization resource
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Profile Interaction Summary

## REQ-25

**Summary**: Support vread interaction for Organization resource
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Organization Section, Profile Interaction Summary

## REQ-26

**Summary**: Return Organization resource using ID
**Description**: "A Server SHALL be capable of returning a Organization resource using: `GET [base]/Organization/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-27

**Summary**: Return Organization resource using ID and version ID
**Description**: "A Server SHOULD be capable of returning a Organization resource using: `GET [base]/Organization/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-28

**Summary**: Support _include for Organization:partof
**Description**: "A Server SHALL be capable of supporting the following _includes: Organization:partof - `GET [base]/Organization?[parameter=value]&_include=Organization:partof`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-29

**Summary**: Support _include for Organization:endpoint
**Description**: "A Server SHALL be capable of supporting the following _includes: Organization:endpoint - `GET [base]/Organization?[parameter=value]&_include=Organization:endpoint`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-30

**Summary**: Support _include for Organization:coverage-area
**Description**: "A Server SHALL be capable of supporting the following _includes: Organization:coverage-area - `GET [base]/Organization?[parameter=value]&_include=Organization:coverage-area`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-31

**Summary**: Support _revinclude for Endpoint:organization
**Description**: "A Server SHALL be capable of supporting the following _revincludes: Endpoint:organization - `GET [base]/Organization?[parameter=value]&_revinclude=Endpoint:organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-32

**Summary**: Support _revinclude for HealthcareService:organization
**Description**: "A Server SHALL be capable of supporting the following _revincludes: HealthcareService:organization - `GET [base]/Organization?[parameter=value]&_revinclude=HealthcareService:organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-33

**Summary**: Support _revinclude for InsurancePlan:administered-by
**Description**: "A Server SHALL be capable of supporting the following _revincludes: InsurancePlan:administered-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:administered-by`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-34

**Summary**: Support _revinclude for InsurancePlan:owned-by
**Description**: "A Server SHALL be capable of supporting the following _revincludes: InsurancePlan:owned-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:owned-by`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-35

**Summary**: Support _revinclude for OrganizationAffiliation:primary-organization
**Description**: "A Server SHALL be capable of supporting the following _revincludes: OrganizationAffiliation:primary-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:primary-organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-36

**Summary**: Support _revinclude for PractitionerRole:organization
**Description**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:organization - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-37

**Summary**: Support _revinclude for PractitionerRole:network
**Description**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:network - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:network`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-38

**Summary**: Support _revinclude for OrganizationAffiliation:participating-organization
**Description**: "A Server SHALL be capable of supporting the following _revincludes: OrganizationAffiliation:participating-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:participating-organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

## REQ-39

**Summary**: Support partof search parameter for Organization resource
**Description**: "SHALL [partof](SearchParameter-organization-partof.html) reference `GET [base]/Organization?partof=[partof]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary

## REQ-40

**Summary**: Support endpoint search parameter for Organization resource
**Description**: "SHALL [endpoint](SearchParameter-organization-endpoint.html) reference `GET [base]/Organization?endpoint=[endpoint]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary

## REQ-41

**Summary**: Support address search parameter for Organization resource
**Description**: "SHALL [address](SearchParameter-organization-address.html) string `GET [base]/Organization?address=[address]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary

## REQ-42

**Summary**: Support name search parameter for Organization resource
**Description**: "SHALL [name](SearchParameter-organization-name.html) string `GET [base]/Organization?name=[name]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary

## REQ-43

**Summary**: Support _id search parameter for Organization resource
**Description**: "SHALL [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/Organization?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary

## REQ-44

**Summary**: Support _lastUpdated search parameter for Organization resource
**Description**: "SHALL [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/Organization?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary

## REQ-45

**Summary**: Support type search parameter for Organization resource
**Description**: "SHALL [type](SearchParameter-organization-type.html) token `GET [base]/Organization?type=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary

## REQ-46

**Summary**: Support coverage-area search parameter for Organization resource
**Description**: "SHALL [coverage-area](SearchParameter-organization-coverage-area.html) reference `GET [base]/Organization?coverage-area=[coverage-area]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary
## REQ-01

**Summary**: Support OrganizationAffiliation Resource
**Description**: "Conformance Expectation: **SHALL**"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation

## REQ-02

**Summary**: Support Plan-Net OrganizationAffiliation Profile
**Description**: "Supported Profiles: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation

## REQ-03

**Summary**: Use 'resolves' Reference Policy for OrganizationAffiliation
**Description**: "Reference Policy: `resolves`"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation

## REQ-04

**Summary**: Support search-type and read interactions for OrganizationAffiliation
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Profile Interaction Summary

## REQ-05

**Summary**: Support vread interaction for OrganizationAffiliation
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: OrganizationAffiliation - Profile Interaction Summary

## REQ-06

**Summary**: Return OrganizationAffiliation resource by ID
**Description**: "A Server **SHALL** be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Fetch and Search Criteria

## REQ-07

**Summary**: Return OrganizationAffiliation resource version by ID
**Description**: "A Server **SHOULD** be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: OrganizationAffiliation - Fetch and Search Criteria

## REQ-08

**Summary**: Support OrganizationAffiliation includes for primary-organization
**Description**: "A Server **SHALL** be capable of supporting the following _includes: OrganizationAffiliation:primary-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:primary-organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Fetch and Search Criteria

## REQ-09

**Summary**: Support OrganizationAffiliation includes for participating-organization
**Description**: "A Server **SHALL** be capable of supporting the following _includes: OrganizationAffiliation:participating-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:participating-organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Fetch and Search Criteria

## REQ-10

**Summary**: Support OrganizationAffiliation includes for location
**Description**: "A Server **SHALL** be capable of supporting the following _includes: OrganizationAffiliation:location - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:location`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Fetch and Search Criteria

## REQ-11

**Summary**: Support OrganizationAffiliation includes for service
**Description**: "A Server **SHALL** be capable of supporting the following _includes: OrganizationAffiliation:service - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:service`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Fetch and Search Criteria

## REQ-12

**Summary**: Support OrganizationAffiliation includes for endpoint
**Description**: "A Server **SHALL** be capable of supporting the following _includes: OrganizationAffiliation:endpoint - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:endpoint`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Fetch and Search Criteria

## REQ-13

**Summary**: Support OrganizationAffiliation includes for network
**Description**: "A Server **SHALL** be capable of supporting the following _includes: OrganizationAffiliation:network - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:network`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Fetch and Search Criteria

## REQ-14

**Summary**: Support OrganizationAffiliation search by primary-organization
**Description**: "**SHALL**   [primary-organization](SearchParameter-organizationaffiliation-primary-organization.html)   reference   `GET [base]/OrganizationAffiliation?primary-organization=[primary-organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-15

**Summary**: Support OrganizationAffiliation search by participating-organization
**Description**: "**SHALL**   [participating-organization](SearchParameter-organizationaffiliation-participating-organization.html)   reference   `GET [base]/OrganizationAffiliation?participating-organization=[participating-organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-16

**Summary**: Support OrganizationAffiliation search by location
**Description**: "**SHALL**   [location](SearchParameter-organizationaffiliation-location.html)   reference   `GET [base]/OrganizationAffiliation?location=[location]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-17

**Summary**: Support OrganizationAffiliation search by service
**Description**: "**SHALL**   [service](SearchParameter-organizationaffiliation-service.html)   reference   `GET [base]/OrganizationAffiliation?service=[service]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-18

**Summary**: Support OrganizationAffiliation search by network
**Description**: "**SHALL**   [network](SearchParameter-organizationaffiliation-network.html)   reference   `GET [base]/OrganizationAffiliation?network=[network]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-19

**Summary**: Support OrganizationAffiliation search by endpoint
**Description**: "**SHALL**   [endpoint](SearchParameter-organizationaffiliation-endpoint.html)   reference   `GET [base]/OrganizationAffiliation?endpoint=[endpoint]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-20

**Summary**: Support OrganizationAffiliation search by role
**Description**: "**SHALL**   [role](SearchParameter-organizationaffiliation-role.html)   token   `GET [base]/OrganizationAffiliation?role=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-21

**Summary**: Support OrganizationAffiliation search by specialty
**Description**: "**SHALL**   [specialty](SearchParameter-organizationaffiliation-specialty.html)   token   `GET [base]/OrganizationAffiliation?specialty=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-22

**Summary**: Support OrganizationAffiliation search by _id
**Description**: "**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/OrganizationAffiliation?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-23

**Summary**: Support OrganizationAffiliation search by _lastUpdated
**Description**: "**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/OrganizationAffiliation?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation - Search Parameter Summary

## REQ-24

**Summary**: Support Practitioner Resource
**Description**: "Conformance Expectation: **SHALL**"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner

## REQ-25

**Summary**: Support Plan-Net Practitioner Profile
**Description**: "Supported Profiles: [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner

## REQ-26

**Summary**: Use 'resolves' Reference Policy for Practitioner
**Description**: "Reference Policy: `resolves`"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner

## REQ-27

**Summary**: Support search-type and read interactions for Practitioner
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner - Profile Interaction Summary

## REQ-28

**Summary**: Support vread interaction for Practitioner
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Practitioner - Profile Interaction Summary

## REQ-29

**Summary**: Return Practitioner resource by ID
**Description**: "A Server **SHALL** be capable of returning a Practitioner resource using: `GET [base]/Practitioner/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner - Fetch and Search Criteria

## REQ-30

**Summary**: Return Practitioner resource version by ID
**Description**: "A Server **SHOULD** be capable of returning a Practitioner resource using: `GET [base]/Practitioner/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Practitioner - Fetch and Search Criteria

## REQ-31

**Summary**: Support Practitioner revinclude for PractitionerRole:practitioner
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes: PractitionerRole:practitioner - `GET [base]/Practitioner?[parameter=value]&_revinclude=PractitionerRole:practitioner`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner - Fetch and Search Criteria

## REQ-32

**Summary**: Support Practitioner search by name
**Description**: "**SHALL**   [name](SearchParameter-practitioner-name.html)   string   `GET [base]/Practitioner?name=[name]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner - Search Parameter Summary

## REQ-33

**Summary**: Support Practitioner search by _id
**Description**: "**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/Practitioner?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner - Search Parameter Summary

## REQ-34

**Summary**: Support Practitioner search by _lastUpdated
**Description**: "**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/Practitioner?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner - Search Parameter Summary

## REQ-35

**Summary**: Support Practitioner search by family
**Description**: "**SHALL**   [family](SearchParameter-practitioner-family-name.html)   string   `GET [base]/Practitioner?family=[family]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner - Search Parameter Summary

## REQ-36

**Summary**: Support Practitioner search by given
**Description**: "**SHALL**   [given](SearchParameter-practitioner-given-name.html)   string   `GET [base]/Practitioner?given=[given]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner - Search Parameter Summary
## REQ-01

**Summary**: Support Plan-Net PractitionerRole profile
**Description**: "Supported Profiles: [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section

## REQ-02

**Summary**: Support PractitionerRole search-type interaction
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Profile Interaction Summary

## REQ-03

**Summary**: Support PractitionerRole read interaction
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Profile Interaction Summary

## REQ-04

**Summary**: Support PractitionerRole vread interaction
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: PractitionerRole Section, Profile Interaction Summary

## REQ-05

**Summary**: Return PractitionerRole resource by ID
**Description**: "A Server SHALL be capable of returning a PractitionerRole resource using: `GET [base]/PractitionerRole/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Fetch and Search Criteria

## REQ-06

**Summary**: Return PractitionerRole resource by ID and version
**Description**: "A Server SHOULD be capable of returning a PractitionerRole resource using: `GET [base]/PractitionerRole/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: PractitionerRole Section, Fetch and Search Criteria

## REQ-07

**Summary**: Support PractitionerRole include for practitioner
**Description**: "A Server SHALL be capable of supporting the following _includes: PractitionerRole:practitioner - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:practitioner`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Fetch and Search Criteria

## REQ-08

**Summary**: Support PractitionerRole include for organization
**Description**: "A Server SHALL be capable of supporting the following _includes: PractitionerRole:organization - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Fetch and Search Criteria

## REQ-09

**Summary**: Support PractitionerRole include for location
**Description**: "A Server SHALL be capable of supporting the following _includes: PractitionerRole:location - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:location`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Fetch and Search Criteria

## REQ-10

**Summary**: Support PractitionerRole include for service
**Description**: "A Server SHALL be capable of supporting the following _includes: PractitionerRole:service - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:service`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Fetch and Search Criteria

## REQ-11

**Summary**: Support PractitionerRole include for network
**Description**: "A Server SHALL be capable of supporting the following _includes: PractitionerRole:network - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:network`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Fetch and Search Criteria

## REQ-12

**Summary**: Support PractitionerRole include for endpoint
**Description**: "A Server SHALL be capable of supporting the following _includes: PractitionerRole:endpoint - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:endpoint`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Fetch and Search Criteria

## REQ-13

**Summary**: Support PractitionerRole search by practitioner
**Description**: "SHALL [practitioner](SearchParameter-practitionerrole-practitioner.html) reference `GET [base]/PractitionerRole?practitioner=[practitioner]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-14

**Summary**: Support PractitionerRole search by organization
**Description**: "SHALL [organization](SearchParameter-practitionerrole-organization.html) reference `GET [base]/PractitionerRole?organization=[organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-15

**Summary**: Support PractitionerRole search by location
**Description**: "SHALL [location](SearchParameter-practitionerrole-location.html) reference `GET [base]/PractitionerRole?location=[location]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-16

**Summary**: Support PractitionerRole search by service
**Description**: "SHALL [service](SearchParameter-practitionerrole-service.html) reference `GET [base]/PractitionerRole?service=[service]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-17

**Summary**: Support PractitionerRole search by network
**Description**: "SHALL [network](SearchParameter-practitionerrole-network.html) reference `GET [base]/PractitionerRole?network=[network]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-18

**Summary**: Support PractitionerRole search by endpoint
**Description**: "SHALL [endpoint](SearchParameter-practitionerrole-endpoint.html) reference `GET [base]/PractitionerRole?endpoint=[endpoint]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-19

**Summary**: Support PractitionerRole search by role
**Description**: "SHALL [role](SearchParameter-practitionerrole-role.html) token `GET [base]/PractitionerRole?role=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-20

**Summary**: Support PractitionerRole search by specialty
**Description**: "SHALL [specialty](SearchParameter-practitionerrole-specialty.html) token `GET [base]/PractitionerRole?specialty=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-21

**Summary**: Support PractitionerRole search by _id
**Description**: "SHALL [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/PractitionerRole?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary

## REQ-22

**Summary**: Support PractitionerRole search by _lastUpdated
**Description**: "SHALL [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/PractitionerRole?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section, Search Parameter Summary
``` 
## REQ-01

**Summary**: Declare conformance to Plan-Net CapabilityStatement
**Description**: "Systems conforming to this implementation guide are expected to declare conformance to one or more of the following capability statements."
**Verification**: Inspection
**Notes**: Actor: System, Conformance: SHALL, Conditional: False
**Source**: Artifacts Summary/Behavior: Capability Statements

## REQ-02

**Summary**: Meet CMS Final Rule requirement for provider directory access
**Description**: "Systems implementing this capability statement should meet the CMS FInal Rule requirement for provider directory access."
**Verification**: Inspection
**Notes**: Actor: System implementing Plan-Net CapabilityStatement, Conformance: SHOULD, Conditional: False
**Source**: Artifacts Summary/Behavior: Capability Statements 
## REQ-01

**Summary**: Support the `endpoint-organization` search parameter for the Endpoint resource.
**Description**: "Select Endpoints managed by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_endpoint_organization](SearchParameter-endpoint-organization.html "SearchParameter/endpoint-organization")

## REQ-02

**Summary**: Support the `coverage-area` search parameter for the HealthcareService resource.
**Description**: "Select services available in a region described by the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_healthcareservice_coverage_area](SearchParameter-healthcareservice-coverage-area.html "SearchParameter/healthcareservice-coverage-area")

## REQ-03

**Summary**: Support the `organization` search parameter for the HealthcareService resource.
**Description**: "Select HealthcareServices provided by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_healthcareservice_organization](SearchParameter-healthcareservice-organization.html "SearchParameter/healthcareservice-organization")

## REQ-04

**Summary**: Support the `endpoint` search parameter for the HealthcareService resource.
**Description**: "Select HealthcareServices with the specified endpoint"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_healthcareservice_endpoint](SearchParameter-healthcareservice-endpoint.html "SearchParameter/healthcareservice-endpoint")

## REQ-05

**Summary**: Support the `location` search parameter for the HealthcareService resource.
**Description**: "Select HealthcareServices available at the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_healthcareservice_location](SearchParameter-healthcareservice-location.html "SearchParameter/healthcareservice-location")

## REQ-06

**Summary**: Support the `name` search parameter for the HealthcareService resource.
**Description**: "Select HealthcareServices with the specified name"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_healthcareservice_name](SearchParameter-healthcareservice-name.html "SearchParameter/healthcareservice-name")

## REQ-07

**Summary**: Support the `service-category` search parameter for the HealthcareService resource.
**Description**: "Select HealthcareServices providing the specified category of services"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_healthcareservice_category](SearchParameter-healthcareservice-service-category.html "SearchParameter/healthcareservice-service-category")

## REQ-08

**Summary**: Support the `service-type` search parameter for the HealthcareService resource.
**Description**: "Select HealthcareServices of the specified type"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_healthcareservice_type](SearchParameter-healthcareservice-service-type.html "SearchParameter/healthcareservice-service-type")

## REQ-09

**Summary**: Support the `specialty` search parameter for the HealthcareService resource.
**Description**: "Select services associated with the specified specialty"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_healthcareservice_specialty](SearchParameter-healthcareservice-specialty.html "SearchParameter/healthcareservice-specialty")

## REQ-10

**Summary**: Support the `administered-by` search parameter for the InsurancePlan resource.
**Description**: "Select products that are administered by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_insuranceplan_administered_by](SearchParameter-insuranceplan-administered-by.html "SearchParameter/insuranceplan-administered-by")

## REQ-11

**Summary**: Support the `coverage-area` search parameter for the InsurancePlan resource.
**Description**: "Select products that are offered in the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_insuranceplan_coverage_area](SearchParameter-insuranceplan-coverage-area.html "SearchParameter/insuranceplan-coverage-area")

## REQ-12

**Summary**: Support the `identifier` search parameter for the InsurancePlan resource.
**Description**: "Select products with the specified identifier"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_insuranceplan_identifier](SearchParameter-insuranceplan-identifier.html "SearchParameter/insuranceplan-identifier")

## REQ-13

**Summary**: Support the `name` search parameter for the InsurancePlan resource.
**Description**: "Select products with the specified name"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_insuranceplan_name](SearchParameter-insuranceplan-name.html "SearchParameter/insuranceplan-name")

## REQ-14

**Summary**: Support the `owned-by` search parameter for the InsurancePlan resource.
**Description**: "Select products that are owned by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_insuranceplan_owned-by](SearchParameter-insuranceplan-owned-by.html "SearchParameter/insuranceplan-owned-by")

## REQ-15

**Summary**: Support the `plan-type` search parameter for the InsurancePlan resource.
**Description**: "Select plans of the specified type"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_insuranceplan_plan-type](SearchParameter-insuranceplan-plan-type.html "SearchParameter/insuranceplan-plan-type")

## REQ-16

**Summary**: Support the `type` search parameter for the InsurancePlan resource.
**Description**: "Select insurance plans of the specified type"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_insuranceplan_type](SearchParameter-insuranceplan-type.html "SearchParameter/insuranceplan-type")

## REQ-17

**Summary**: Support the `address-city` search parameter for the Location resource.
**Description**: "Select Locations with the specified address.city"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Behavior: Search Parameters / [Plannet_sp_location_address_city](SearchParameter-location-address-city.html "SearchParameter/location-address-city")
## REQ-01

**Summary**: Support the `location-address-postalcode` search parameter
**Description**: "Select Locations with the specified address"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-location-address-postalcode

## REQ-02

**Summary**: Support the `location-address-state` search parameter
**Description**: "Select Locations with the specified address.state"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-location-address-state

## REQ-03

**Summary**: Support the `location-address` search parameter
**Description**: "Select Locations with the specified address"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-location-address

## REQ-04

**Summary**: Support the `location-endpoint` search parameter
**Description**: "Select Locations with the specified endpoint"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-location-endpoint

## REQ-05

**Summary**: Support the `location-organization` search parameter
**Description**: "Select Locations managed by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-location-organization

## REQ-06

**Summary**: Support the `location-partof` search parameter
**Description**: "Select Locations that are part of the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-location-partof

## REQ-07

**Summary**: Support the `location-type` search parameter
**Description**: "Select Locations of the specified type"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-location-type

## REQ-08

**Summary**: Support the `organization-address` search parameter
**Description**: "Select organizations with the specified address (matches any of the string elements of an address)"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organization-address

## REQ-09

**Summary**: Support the `organization-coverage-area` search parameter
**Description**: "Select health insurance provider networks available in a region described by the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organization-coverage-area

## REQ-10

**Summary**: Support the `organization-endpoint` search parameter
**Description**: "Select Organizations with the specified endpoint"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organization-endpoint

## REQ-11

**Summary**: Support the `organization-name` search parameter
**Description**: "Select Organizations with the specified name"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organization-name

## REQ-12

**Summary**: Support the `organization-partof` search parameter
**Description**: "Select Organizations that are part of the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organization-partof

## REQ-13

**Summary**: Support the `organization-type` search parameter
**Description**: "Select Organizations of the specified type"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organization-type

## REQ-14

**Summary**: Support the `organizationaffiliation-endpoint` search parameter
**Description**: "Select OrganizationAffiliations with the specified endpoint"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-endpoint

## REQ-15

**Summary**: Support the `organizationaffiliation-location` search parameter
**Description**: "Select OrganizationAffiliations available at the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-location

## REQ-16

**Summary**: Support the `organizationaffiliation-network` search parameter
**Description**: "Select roles where the organization is a member of the specified health insurance provider network"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-network

## REQ-17

**Summary**: Support the `organizationaffiliation-participating-organization` search parameter
**Description**: "Select roles filled by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-participating-organization

## REQ-18

**Summary**: Support the `organizationaffiliation-period` search parameter
**Description**: "Select Organization Affiliations available in the specified period"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-period

## REQ-19

**Summary**: Support the `organizationaffiliation-primary-organization` search parameter
**Description**: "Select roles offered by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-primary-organization

## REQ-20

**Summary**: Support the `organizationaffiliation-role` search parameter
**Description**: "Select OrganizationAffiliations with the specified role"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-role

## REQ-21

**Summary**: Support the `organizationaffiliation-service` search parameter
**Description**: "Select OrganizationAffiliations providing the specified service"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-service

## REQ-22

**Summary**: Support the `organizationaffiliation-specialty` search parameter
**Description**: "Select OrganizationAffiliations associated with the specified specialty"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-organizationaffiliation-specialty

## REQ-23

**Summary**: Support the `practitioner-family-name` search parameter
**Description**: "Select Practitioners with the specified family name"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitioner-family-name

## REQ-24

**Summary**: Support the `practitioner-given-name` search parameter
**Description**: "Select Practitioners with the specified given name"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitioner-given-name

## REQ-25

**Summary**: Support the `practitioner-name` search parameter
**Description**: "Select Practitioners with the specified name (matches against any of the elements in the HumanName data type)"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitioner-name

## REQ-26

**Summary**: Support the `practitionerrole-endpoint` search parameter
**Description**: "Select PractitionerRoles with the specified endpoint"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-endpoint

## REQ-27

**Summary**: Support the `practitionerrole-location` search parameter
**Description**: "Select PractitionerRoles available at the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-location

## REQ-28

**Summary**: Support the `practitionerrole-network` search parameter
**Description**: "Select roles where the practitioner is a member of the specified health insurance provider network"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-network

## REQ-29

**Summary**: Support the `practitionerrole-organization` search parameter
**Description**: "Select PractitionerRoles available at the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-organization

## REQ-30

**Summary**: Support the `practitionerrole-period` search parameter
**Description**: "Select PractitionerRoles available in the specified period"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-period

## REQ-31

**Summary**: Support the `practitionerrole-practitioner` search parameter
**Description**: "Select roles filled by the specified practitioner"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-practitioner

## REQ-32

**Summary**: Support the `practitionerrole-role` search parameter
**Description**: "Select PractitionerRoles with the specified role"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-role

## REQ-33

**Summary**: Support the `practitionerrole-service` search parameter
**Description**: "Select PractitionerRoles providing the specified service"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-service

## REQ-34

**Summary**: Support the `practitionerrole-specialty` search parameter
**Description**: "Select PractitionerRoles associated with the specified specialty"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: SearchParameter-practitionerrole-specialty
## REQ-01

**Summary**: Plan-Net Endpoint resources SHALL use the Plan-Net Endpoint profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html "StructureDefinition/plannet-Endpoint")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net Endpoint

## REQ-02

**Summary**: Plan-Net HealthcareService resources SHALL use the Plan-Net HealthcareService profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html "StructureDefinition/plannet-HealthcareService")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net HealthcareService

## REQ-03

**Summary**: Plan-Net InsurancePlan resources SHALL use the Plan-Net InsurancePlan profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html "StructureDefinition/plannet-InsurancePlan")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net InsurancePlan

## REQ-04

**Summary**: Plan-Net Location resources SHALL use the Plan-Net Location profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net Location](StructureDefinition-plannet-Location.html "StructureDefinition/plannet-Location")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net Location

## REQ-05

**Summary**: Plan-Net Network resources SHALL use the Plan-Net Network profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net Network](StructureDefinition-plannet-Network.html "StructureDefinition/plannet-Network")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net Network

## REQ-06

**Summary**: Plan-Net Organization resources SHALL use the Plan-Net Organization profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net Organization](StructureDefinition-plannet-Organization.html "StructureDefinition/plannet-Organization")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net Organization

## REQ-07

**Summary**: Plan-Net OrganizationAffiliation resources SHALL use the Plan-Net OrganizationAffiliation profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html "StructureDefinition/plannet-OrganizationAffiliation")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net OrganizationAffiliation

## REQ-08

**Summary**: Plan-Net Practitioner resources SHALL use the Plan-Net Practitioner profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html "StructureDefinition/plannet-Practitioner")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net Practitioner

## REQ-09

**Summary**: Plan-Net PractitionerRole resources SHALL use the Plan-Net PractitionerRole profile.
**Description**: "These define constraints on FHIR resources for systems conforming to this implementation guide [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html "StructureDefinition/plannet-PractitionerRole")"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Resource Profiles, Plan-Net PractitionerRole

## REQ-10

**Summary**: When the contact is a department, the Organization.contact.name SHALL include a blank family and given name, and provide the department name in contact.name.text.
**Description**: "Guidance: When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: When the contact is a department name rather than a human
**Source**: Structures: Resource Profiles, Plan-Net Organization 
## REQ-01

**Summary**: Support Accessibility Extension
**Description**: "An extension to describe accessibility options offered by a practitioner or at a location."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Accessibility

## REQ-02

**Summary**: Support Communication Proficiency Extension
**Description**: "An extension to express a practitioner’s spoken proficiency with the language indicated in practitioner.communication."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Communication Proficiency

## REQ-03

**Summary**: Support Contactpoint Availabletime Extension
**Description**: "An extension representing the days and times a contact point is available"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Contactpoint Availabletime

## REQ-04

**Summary**: Support Delivery Method Extension
**Description**: "An extension describing the service delivery method. If service delivery is virtual, one or more delivery modalities should be specified."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Delivery Method

## REQ-05

**Summary**: Support Endpoint Usecase Extension
**Description**: "EndpointUseCase is an enumeration of the specific use cases (service descriptions) supported by the endpoint"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Endpoint Usecase

## REQ-06

**Summary**: Support Location Reference Extension
**Description**: "A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Location Reference

## REQ-07

**Summary**: Support Network Reference Extension
**Description**: "A reference to the healthcare provider insurance networks (plannet-Network) the practitioner participates in through their role"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Network Reference

## REQ-08

**Summary**: Support New Patients Extension
**Description**: "New Patients indicates whether new patients are being accepted in general, or from a specific network.   This extension is included in the PractitionerRole, HealthcareService, and Location profiles.  This provides needed flexibility for specifying whether a provider accepts new patients by location and network."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - New Patients

## REQ-09

**Summary**: Support Org Description Extension
**Description**: "An extension to provide a human-readable description of an organization."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Org Description

## REQ-10

**Summary**: Support Practitioner Qualification Extension
**Description**: "An extension to add status and whereValid elements to a practitioner’s qualifications."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Practitioner Qualification

## REQ-11

**Summary**: Support Qualification Extension
**Description**: "An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances)."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Qualification

## REQ-12

**Summary**: Support Via Intermediary Extension
**Description**: "A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Structures: Extension Definitions - Via Intermediary 
## REQ-01

**Summary**: Constrain Endpoint Payload Types to NA
**Description**: "Endpoint Payload Types are constrained to NA (Not Applicable) as part of this IG"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Terminology: Code Systems - Endpoint Payload Types

## REQ-02

**Summary**: Constrain Endpoint Payload Types to NA
**Description**: "Endpoint Payload Types are constrained to NA (Not Applicable) as part of this IG"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Terminology: Value Sets - Endpoint Payload Types VS
## REQ-01

**Summary**: Provide example instance for Payer Organization
**Description**: "[Acme](Organization-Acme.html "Organization/Acme")   Payer Organization"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Example Instances Section

## REQ-02

**Summary**: Provide example instance for Endpoint
**Description**: "[AcmeOfCTPortalEndpoint](Endpoint-AcmeOfCTPortalEndpoint.html "Endpoint/AcmeOfCTPortalEndpoint")   Endpoint for Acme of CT Portal"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Example Instances Section

## REQ-03

**Summary**: Provide example instance for Insurance Plan
**Description**: "[AcmeQHPBronze](InsurancePlan-AcmeQHPBronze.html "InsurancePlan/AcmeQHPBronze")   Acme of CT QHP Bronze Plan"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Example Instances Section

## REQ-04

**Summary**: Provide example instance for Insurance Plan
**Description**: "[AcmeQHPGold](InsurancePlan-AcmeQHPGold.html "InsurancePlan/AcmeQHPGold")   Acme of CT QHP Gold Plan"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Example Instances Section

## REQ-05

**Summary**: Provide example instance for Premium Network Organization
**Description**: "[AcmeofCTPremNet](Organization-AcmeofCTPremNet.html "Organization/AcmeofCTPremNet")   Acme of CT Premium Premium Network"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Example Instances Section

## REQ-06

**Summary**: Provide example instance for Standard Network Organization
**Description**: "[AcmeofCTStdNet](Organization-AcmeofCTStdNet.html "Organization/AcmeofCTStdNet")   Acme of CT Standard Network"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Example Instances Section

## REQ-07

**Summary**: Provide example instance for Practitioner Role
**Description**: "[AnonRole](PractitionerRole-AnonRole.html "PractitionerRole/AnonRole")   Practitioner role that doesn’t refer to a specific practitioner"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Example Instances Section

## REQ-08

**Summary**: Provide example instance for Organization
**Description**: "[BigBox](Organization-BigBox.html "Organization/BigBox")   Organization that Manages 2 of PharmChain’s pharmacies"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Example Instances Section
