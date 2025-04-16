## Introduction

This analysis focuses on the "Change History" and "Profiles" sections of the Da Vinci PDex Plan Net Implementation Guide v1.1.0. These sections primarily document changes between versions and provide an overview of the profiles defined within the guide.  They do not contain explicitly testable requirements using the keywords SHALL, SHOULD, MAY, MUST, REQUIRED, etc. 

Therefore, no extractable INCOSE-style requirements are identified in this chunk. 
## Da Vinci PDex Plan Net Implementation Guide v1.2.0 Requirement Extraction - Chunk 1 of 2

This document outlines the requirements extracted from the Da Vinci PDex Plan Net Implementation Guide v1.2.0, specifically from the provided "Home" section (chunk 1 of 2). 

**Important Note:** The provided content is primarily descriptive and introductory, lacking concrete statements using SHALL, SHOULD, MAY, MUST, REQUIRED, or similar keywords that typically indicate testable requirements. Therefore, no specific requirements for an INCOSE-style Software Requirements Specification could be extracted from this chunk. 

The document focuses on providing an overview of the implementation guide, its purpose, scope, and background information. It also clarifies its relationship with other standards like US Core and VHDir. 

To effectively extract testable requirements, subsequent chunks should contain more specific guidance on API behaviors, data elements, and interactions between the Health Plan API Actor and the Application Actor. 
##  Da Vinci PDex Plan Net Implementation Guide v1.2.0 Requirements - Chunk 2 of 2 Analysis 

This section analyzes the "Credits" and "Authors" sections of the Da Vinci PDex Plan Net Implementation Guide v1.2.0 for extractable requirements. 

**Analysis Result:** This chunk does not contain any testable requirements. It provides information about the development process and authorship of the Implementation Guide but does not define specific behaviors or functionalities for software systems. 
## Da Vinci PDex Plan Net Implementation Guide v1.2.0 Requirement Extraction - Chunk 1 of 3

This document extracts INCOSE-style requirements from the "Examples" section of the Da Vinci PDex Plan Net Implementation Guide v1.2.0. 

**Analysis:**

This section provides an introduction and overview of the guide and does not contain any testable requirements using SHALL, SHOULD, MAY, MUST, REQUIRED, or similar keywords. 

**Therefore, no requirements are extracted from this chunk.** 
## Introduction

This section analyzes the "Examples Table" from the Da Vinci PDex Plan Net Implementation Guide v1.2.0. This table lists example resources, their corresponding FHIR resource types, and the PlanNet profiles they conform to. 

However, this section does not contain any testable requirements using SHALL, SHOULD, MAY, MUST, REQUIRED, or similar keywords. Therefore, no requirements are extracted from this section. 
## Introduction

This requirements extraction focuses on chunk 3 of 3 from the Da Vinci PDex Plan Net Implementation Guide v1.2.0. This chunk primarily provides examples of FHIR resources like Location, Organization, OrganizationAffiliation, Practitioner, and PractitionerRole, illustrating the implementation of the Da Vinci PDex Plan Net profiles. 

## No Requirements Found

This chunk of the implementation guide does not contain explicit requirements using keywords like SHALL, SHOULD, MAY, MUST, REQUIRED, etc. It focuses on providing concrete examples of FHIR resources conforming to the defined profiles. Therefore, no testable requirements can be extracted in this section. 
## Da Vinci PDex Plan Net Implementation Guide v1.2.0 - Requirements Extraction - Chunk 1/3

This document extracts testable requirements from the "Implementation" section of the Da Vinci PDex Plan Net Implementation Guide v1.2.0. This section provides implementation guidance for the Plan-Net specification, focusing on conformance requirements, privacy considerations, "Must Support" interpretations, client detection of updates, and general security considerations. 

## Requirements

**REQ-SERVER-SHALL-01**

**Summary**: Prohibit requirement of consumer identifying information for content query.
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL NOT, Conditional: False
**Source**: Implementation Notes/Privacy Considerations

**REQ-CLIENT-SHALL-01**

**Summary**: Prohibit sending consumer identifiable information when querying Plan-Net service.
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Test
**Notes**: Actor: Client (Directory mobile application), Conformance: SHALL NOT, Conditional: False
**Source**: Implementation Notes/Privacy Considerations

**REQ-SERVER-SHALL-02**

**Summary**: Populate all Must Support data elements for query results.
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Notes**: Actor: Server (Health Plan API actor), Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

**REQ-SERVER-SHALL-03**

**Summary**:  Omit data elements with minimum cardinality 0 when information is not present.
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Notes**: Actor: Server (Health Plan API actor), Conformance: SHALL NOT, Conditional: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

**REQ-SERVER-SHALL-04**

**Summary**: Provide reason for missing information for Must Support data elements with minimum cardinality > 0.
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Notes**: Actor: Server (Health Plan API actor), Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

**REQ-CLIENT-SHALL-02**

**Summary**: Process resource instances containing Must Support data elements without errors.
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Notes**: Actor: Client (Application actor), Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Application Requirements

**REQ-CLIENT-SHOULD-01**

**Summary**: Display or store Must Support data elements for human use.
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Notes**: Actor: Client (Application actor), Conformance: SHOULD, Conditional: False
**Source**: Implementation Notes/Must Support/Application Requirements

**REQ-CLIENT-SHALL-03**

**Summary**: Interpret missing Must Support data elements as not present in the Health Plan API system.
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Notes**: Actor: Client (Application actor), Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Application Requirements

**REQ-CLIENT-SHALL-04**

**Summary**: Process resource instances containing Must Support data elements with missing information.
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Notes**: Actor: Client (Consumer App actor), Conformance: SHALL, Conditional: False
**Source**: Implementation Notes/Must Support/Application Requirements

This concludes the requirements extraction for the provided content chunk. 
## Da Vinci PDex Plan Net Implementation Guide v1.2.0 - Requirements Extraction - Chunk 2 of 3

This section focuses on extracting testable requirements from chunk 2 of 3 of the Da Vinci PDex Plan Net Implementation Guide v1.2.0, related to HealthcareService, Insurance Plan and Network, Location, Practitioners, and PractitionerRoles. The guide predominantly provides implementation guidance and examples rather than explicit requirements. Therefore, this analysis will focus on extracting implicit requirements derived from strong recommendations and expected functionalities. 

## Extracted Requirements

**REQ-SERVER-SHOULD-01**

**Summary**: Support HealthcareService search by category and specialty
**Description**: "The first type of search starts from HealthcareService.category and HealthcareService.specialty, so it is essential that each provider's service be supported by appropriate set of HealthcareService instances."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD (derived from "essential"), Conditional: False
**Source**: HealthcareService Section

**REQ-SERVER-SHOULD-02**

**Summary**: Define HealthcareServices for service organization
**Description**: "All organizations that provide service should define an appropriate set of HealthcareServices to facilitate search."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: HealthcareService Section

**REQ-SERVER-SHOULD-03**

**Summary**: Represent Insurance Plans and associated Networks
**Description**: "Each payer will offer one or more products -- Insurance Plans -- and each plan is associated with one or more Networks."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD (derived from "will"), Conditional: False
**Source**: Insurance Plan and Network Section

**REQ-SERVER-SHOULD-04**

**Summary**: Link Practitioners and Organizations to Networks
**Description**: "Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD (derived from "indicate"), Conditional: False
**Source**: Insurance Plan and Network Section

**REQ-SERVER-SHOULD-05**

**Summary**: Associate PractitionerRole and OrganizationAffiliation with HealthcareServices, Organizations, Networks, and Locations
**Description**: "PractitionerRole and OrganizationAffiliation instances are what tie Practitioners and Organizations to HealthcareServices, Organizations, Networks and Locations."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD (derived from "are what tie"), Conditional: False
**Source**: Insurance Plan and Network Section

**REQ-SERVER-SHOULD-06**

**Summary**: Provide Location information for service provision
**Description**: "Location instances provide information about location where service is provided, including contact information, address, accessibility, hours of operation and contact, as well as position (latitude and longitude)."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD (derived from "provide"), Conditional: False
**Source**: Location Section

**REQ-SERVER-MAY-01**

**Summary**: Represent regions using Location with GeoJSON
**Description**: "Locations can also be used to represent regions using an associated or attached GeoJSON object."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: MAY, Conditional: False
**Source**: Location Section

**REQ-SERVER-SHOULD-07**

**Summary**: Provide Practitioner information
**Description**: "Practitioner instances provide information about a specific person, including name, gender, languages spoken, and qualifications."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD (derived from "provide"), Conditional: False
**Source**: Practitioners and PractitionerRoles Section

**REQ-SERVER-SHOULD-08**

**Summary**: Define PractitionerRole and associate with relevant information
**Description**: "PractitionerRole defines a role for a particular practitioner, and associates it with locations, specialties, an organization, and networks."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHOULD (derived from "defines" and "associates"), Conditional: False
**Source**: Practitioners and PractitionerRoles Section 
## Da Vinci PDex Plan Net Implementation Guide v1.2.0 - Requirements Extraction - Chunk 3/3

This section focuses on requirements related to Organizations, Organization Affiliations, and Endpoints within the Da Vinci PDex Plan Net Implementation Guide v1.2.0. It analyzes the provided text for explicit or implicit requirements using modal verbs like SHALL, SHOULD, MAY, MUST, and similar terms. 

**Analysis:**

This chunk of the Da Vinci PDex Plan Net Implementation Guide primarily provides informative descriptions and examples of how "Organization," "OrganizationAffiliation," and "Endpoint" resources can be used in different scenarios. It does not contain explicitly testable requirements using the defined keywords. 

**Conclusion:**

No testable requirements were identified in this section of the Da Vinci PDex Plan Net Implementation Guide v1.2.0. 
## Introduction

This document extracts testable requirements from the "CapabilityStatement: Plan-Net CapabilityStatement" section of the Da Vinci PDex Plan Net Implementation Guide v1.2.0. This section focuses on the capabilities expected of a Plan-Net Server, including supported profiles, RESTful behaviors, response codes, and search parameters. 

## Requirements

**REQ-SERVER-SHALL-01**

**Summary**: Support all defined profiles.
**Description**: "The Plan-Net Server **SHALL**: 1. Support all profiles defined in this Implementation Guide."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

**REQ-SERVER-SHALL-02**

**Summary**: Implement RESTful behavior according to FHIR specification.
**Description**: "The Plan-Net Server **SHALL**: 2. Implement the RESTful behavior according to the FHIR specification."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

**REQ-SERVER-SHALL-03**

**Summary**: Return specific response classes.
**Description**: "The Plan-Net Server **SHALL**: 3. Return the following response classes:
* (Status 400): invalid parameter
* (Status 401/4xx): unauthorized request
* (Status 403): insufficient scope
* (Status 404): unknown resource
* (Status 410): deleted resource."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

**REQ-SERVER-SHALL-04**

**Summary**: Support JSON format for Plan-Net interactions.
**Description**: "The Plan-Net Server **SHALL**: 4. Support json source formats for all Plan-Net interactions."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

**REQ-SERVER-SHALL-05**

**Summary**: Identify supported Plan-Net profiles using meta.profile attribute.
**Description**: "The Plan-Net Server **SHALL**: 5. Identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance."
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

**REQ-SERVER-SHALL-06**

**Summary**: Support searchParameters individually and in combination.
**Description**: "The Plan-Net Server **SHALL**: 6. Support the searchParameters on each profile individually and in combination."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

**REQ-SERVER-SHALL-07**

**Summary**: Support forward and reverse chaining for search parameters with 'chain' property.
**Description**: "The Plan-Net Server **SHALL**: 7. Support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

**REQ-SERVER-SHOULD-01**

**Summary**: Support XML format for Plan-Net interactions.
**Description**: "The Plan-Net Server **SHOULD**: 1. Support xml source formats for all Plan-Net interactions."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

**REQ-SERVER-SHALL-08**

**Summary**: Reject unauthorized requests with HTTP 401.
**Description**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, Security 
## REQ-SERVER-SHALL-01

**Summary**: Support Plan-Net Endpoint profile and search-type, read interactions.
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)
Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint Section

## REQ-SERVER-SHOULD-01

**Summary**: Support vread interaction for Endpoint resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Endpoint Section

## REQ-SERVER-SHALL-02

**Summary**: Return Endpoint resource using ID.
**Description**: "A Server **SHALL** be capable of returning a Endpoint resource using:
`GET [base]/Endpoint/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint Section - Fetch and Search Criteria

## REQ-SERVER-SHOULD-02

**Summary**: Return Endpoint resource using ID and version ID.
**Description**: "A Server **SHOULD** be capable of returning a Endpoint resource using:
`GET [base]/Endpoint/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Endpoint Section - Fetch and Search Criteria

## REQ-SERVER-SHALL-03

**Summary**: Support _include for Endpoint:organization.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint Section - Fetch and Search Criteria

## REQ-SERVER-SHALL-04

**Summary**: Support search by organization, _id, and _lastUpdated for Endpoint.
**Description**: "Search Parameter Summary:
Conformance   Parameter   Type   Example
**SHALL**   [organization](SearchParameter-endpoint-organization.html)   reference   `GET [base]/Endpoint?organization=[organization]`
**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/Endpoint?_id=[id]`
**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/Endpoint?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Endpoint Section - Search Parameter Summary

## REQ-SERVER-SHALL-05

**Summary**: Support Plan-Net HealthcareService profile and search-type, read interactions.
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)
Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService Section

## REQ-SERVER-SHOULD-03

**Summary**: Support vread interaction for HealthcareService resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: HealthcareService Section

## REQ-SERVER-SHALL-06

**Summary**: Return HealthcareService resource using ID.
**Description**: "A Server **SHALL** be capable of returning a HealthcareService resource using:
`GET [base]/HealthcareService/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService Section - Fetch and Search Criteria

## REQ-SERVER-SHOULD-04

**Summary**: Return HealthcareService resource using ID and version ID.
**Description**: "A Server **SHOULD** be capable of returning a HealthcareService resource using:
`GET [base]/HealthcareService/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: HealthcareService Section - Fetch and Search Criteria

## REQ-SERVER-SHALL-07

**Summary**: Support _includes for HealthcareService:location, :coverage-area, :organization, and :endpoint.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
HealthcareService:location - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:location`
HealthcareService:coverage-area - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:coverage-area`
HealthcareService:organization - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:organization`
HealthcareService:endpoint - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:endpoint`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService Section - Fetch and Search Criteria

## REQ-SERVER-SHALL-08

**Summary**: Support _revincludes for PractitionerRole:service and OrganizationAffiliation:service.
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes:
PractitionerRole:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=PractitionerRole:service`
OrganizationAffiliation:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=OrganizationAffiliation:service`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService Section - Fetch and Search Criteria

## REQ-SERVER-SHALL-09

**Summary**: Support searches for HealthcareService by location, coverage-area, organization, endpoint, name, service-category, service-type, specialty, _id, and _lastUpdated.
**Description**: "Search Parameter Summary:
Conformance   Parameter   Type   Example
**SHALL**   [location](SearchParameter-healthcareservice-location.html)   reference   `GET [base]/HealthcareService?location=[location]`
**SHALL**   [coverage-area](SearchParameter-healthcareservice-coverage-area.html)   reference   `GET [base]/HealthcareService?coverage-area=[coverage-area]`
**SHALL**   [organization](SearchParameter-healthcareservice-organization.html)   reference   `GET [base]/HealthcareService?organization=[organization]`
**SHALL**   [endpoint](SearchParameter-healthcareservice-endpoint.html)   reference   `GET [base]/HealthcareService?endpoint=[endpoint]`
**SHALL**   [name](SearchParameter-healthcareservice-name.html)   string   `GET [base]/HealthcareService?name=[name]`
**SHALL**   [service-category](SearchParameter-healthcareservice-service-category.html)   token   `GET [base]/HealthcareService?service-category=[system] [code]`
**SHALL**   [service-type](SearchParameter-healthcareservice-service-type.html)   token   `GET [base]/HealthcareService?service-type=[system] [code]`
**SHALL**   [specialty](SearchParameter-healthcareservice-specialty.html)   token   `GET [base]/HealthcareService?specialty=[system] [code]`
**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/HealthcareService?_id=[id]`
**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/HealthcareService?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: HealthcareService Section - Search Parameter Summary

## REQ-SERVER-SHALL-10

**Summary**: Support Plan-Net InsurancePlan profile and search-type, read interactions.
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html)
Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan Section

## REQ-SERVER-SHOULD-05

**Summary**: Support vread interaction for InsurancePlan resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: InsurancePlan Section

## REQ-SERVER-SHALL-11

**Summary**: Return InsurancePlan resource using ID.
**Description**: "A Server **SHALL** be capable of returning a InsurancePlan resource using:
`GET [base]/InsurancePlan/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan Section - Fetch and Search Criteria

## REQ-SERVER-SHOULD-06

**Summary**: Return InsurancePlan resource using ID and version ID.
**Description**: "A Server **SHOULD** be capable of returning a InsurancePlan resource using:
`GET [base]/InsurancePlan/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: InsurancePlan Section - Fetch and Search Criteria

## REQ-SERVER-SHALL-12

**Summary**: Support _includes for InsurancePlan:administered-by, :owned-by, and :coverage-area.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
InsurancePlan:administered-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:administered-by`
InsurancePlan:owned-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:owned-by`
InsurancePlan:coverage-area - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:coverage-area`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan Section - Fetch and Search Criteria

## REQ-SERVER-SHALL-13

**Summary**: Support searches for InsurancePlan by administered-by, owned-by, coverage-area, name, plan-type, identifier, _id, _lastUpdated, and type.
**Description**: "Search Parameter Summary:
Conformance   Parameter   Type   Example
**SHALL**   [administered-by](SearchParameter-insuranceplan-administered-by.html)   reference   `GET [base]/InsurancePlan?administered-by=[administered-by]`
**SHALL**   [owned-by](SearchParameter-insuranceplan-owned-by.html)   reference   `GET [base]/InsurancePlan?owned-by=[owned-by]`
**SHALL**   [coverage-area](SearchParameter-insuranceplan-coverage-area.html)   reference   `GET [base]/InsurancePlan?coverage-area=[coverage-area]`
**SHALL**   [name](SearchParameter-insuranceplan-name.html)   string   `GET [base]/InsurancePlan?name=[name]`
**SHALL**   [plan-type](SearchParameter-insuranceplan-plan-type.html)   token   `GET [base]/InsurancePlan?plan-type=[system] [code]`
**SHALL**   [identifier](SearchParameter-insuranceplan-identifier.html)   token   `GET [base]/InsurancePlan?identifier=[system] [code]`
**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/InsurancePlan?_id=[id]`
**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/InsurancePlan?_lastUpdated=[_lastUpdated]`
**SHALL**   [type](SearchParameter-insuranceplan-type.html)   token   `GET [base]/InsurancePlan?type=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: InsurancePlan Section - Search Parameter Summary
## REQ-SERVER-SHALL-01

**Summary**: Support Location Resource with Plan-Net Profile
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net Location](StructureDefinition-plannet-Location.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section

### REQ-SERVER-SHALL-02

**Summary**: Support search-type and read interactions for Location resource.
**Description**: "Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section

### REQ-SERVER-SHOULD-01

**Summary**: Support vread interaction for Location resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Location Section

### REQ-SERVER-SHALL-03

**Summary**: Return Location resource by ID.
**Description**: "A Server **SHALL** be capable of returning a Location resource using:
`GET [base]/Location/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

### REQ-SERVER-SHOULD-02

**Summary**: Return Location resource by ID and version.
**Description**: "A Server **SHOULD** be capable of returning a Location resource using:
`GET [base]/Location/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

### REQ-SERVER-SHALL-04

**Summary**: Support _include for Location resource.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
Location:endpoint - `GET [base]/Location?[parameter=value]&_include=Location:endpoint`
Location:organization - `GET [base]/Location?[parameter=value]&_include=Location:organization`
Location:partof - `GET [base]/Location?[parameter=value]&_include=Location:partof`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

### REQ-SERVER-SHALL-05

**Summary**: Support _revinclude for Location resource.
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes:
HealthcareService:location - `GET [base]/Location?[parameter=value]&_revinclude=HealthcareService:location`
InsurancePlan:coverage-area - `GET [base]/Location?[parameter=value]&_revinclude=InsurancePlan:coverage-area`
OrganizationAffiliation:location - `GET [base]/Location?[parameter=value]&_revinclude=OrganizationAffiliation:location`
PractitionerRole:location - `GET [base]/Location?[parameter=value]&_revinclude=PractitionerRole:location`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Fetch and Search Criteria

### REQ-SERVER-SHALL-06

**Summary**: Support all SHALL search parameters for Location resource.
**Description**: "Search Parameter Summary - Conformance column: **SHALL**"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Location Section, Search Parameter Summary.  Note: This requirement consolidates all SHALL requirements for search parameters within the Location section. Individual requirements can be created for each parameter if desired.


## Organization Resource Requirements

### REQ-SERVER-SHALL-07

**Summary**: Support Organization Resource with Plan-Net Profiles
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net Network](StructureDefinition-plannet-Network.html),
[Plan-Net Organization](StructureDefinition-plannet-Organization.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section

### REQ-SERVER-SHALL-08

**Summary**: Support search-type and read interactions for Organization resource.
**Description**: "Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section

### REQ-SERVER-SHOULD-03

**Summary**: Support vread interaction for Organization resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Organization Section

### REQ-SERVER-SHALL-09

**Summary**: Return Organization resource by ID.
**Description**: "A Server **SHALL** be capable of returning a Organization resource using:
`GET [base]/Organization/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

### REQ-SERVER-SHOULD-04

**Summary**: Return Organization resource by ID and version.
**Description**: "A Server **SHOULD** be capable of returning a Organization resource using:
`GET [base]/Organization/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

### REQ-SERVER-SHALL-10

**Summary**: Support _include for Organization resource.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
Organization:partof - `GET [base]/Organization?[parameter=value]&_include=Organization:partof`
Organization:endpoint - `GET [base]/Organization?[parameter=value]&_include=Organization:endpoint`
Organization:coverage-area - `GET [base]/Organization?[parameter=value]&_include=Organization:coverage-area`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

### REQ-SERVER-SHALL-11

**Summary**: Support _revinclude for Organization resource.
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes:
Endpoint:organization - `GET [base]/Organization?[parameter=value]&_revinclude=Endpoint:organization`
HealthcareService:organization - `GET [base]/Organization?[parameter=value]&_revinclude=HealthcareService:organization`
InsurancePlan:administered-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:administered-by`
InsurancePlan:owned-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:owned-by`
OrganizationAffiliation:primary-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:primary-organization`
PractitionerRole:organization - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:organization`
PractitionerRole:network - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:network`
OrganizationAffiliation:participating-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:participating-organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Fetch and Search Criteria

### REQ-SERVER-SHALL-12

**Summary**: Support all SHALL search parameters for Organization resource.
**Description**: "Search Parameter Summary - Conformance column: **SHALL**"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Organization Section, Search Parameter Summary.  Note: This requirement consolidates all SHALL requirements for search parameters within the Organization section. Individual requirements can be created for each parameter if desired.
## REQ-SERVER-SHALL-01

**Summary**: Support OrganizationAffiliation Resource
**Description**: "Conformance Expectation: **SHALL**"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation Section

## REQ-SERVER-SHALL-02

**Summary**: Support OrganizationAffiliation Profile
**Description**: "Supported Profiles: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation Section

## REQ-SERVER-SHALL-03

**Summary**: Implement OrganizationAffiliation resolves Reference Policy
**Description**: "Reference Policy: `resolves`"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation Section

## REQ-SERVER-SHALL-04

**Summary**: Support OrganizationAffiliation search-type and read interactions
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Profile Interaction Summary Section

## REQ-SERVER-SHOULD-01

**Summary**: Support OrganizationAffiliation vread interaction
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: OrganizationAffiliation, Profile Interaction Summary Section

## REQ-SERVER-SHALL-05

**Summary**: Return OrganizationAffiliation using ID
**Description**: "A Server **SHALL** be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Fetch and Search Criteria Section

## REQ-SERVER-SHOULD-02

**Summary**: Return OrganizationAffiliation history using ID and version ID
**Description**: "A Server **SHOULD** be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: OrganizationAffiliation, Fetch and Search Criteria Section

## REQ-SERVER-SHALL-06

**Summary**: Support OrganizationAffiliation includes
**Description**: "A Server **SHALL** be capable of supporting the following _includes: 
OrganizationAffiliation:primary-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:primary-organization`
OrganizationAffiliation:participating-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:participating-organization`
OrganizationAffiliation:location - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:location`
OrganizationAffiliation:service - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:service`
OrganizationAffiliation:endpoint - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:endpoint`
OrganizationAffiliation:network - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:network`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Fetch and Search Criteria Section

## REQ-SERVER-SHALL-07

**Summary**: Support OrganizationAffiliation search by primary-organization
**Description**: "Conformance **SHALL**   Parameter   [primary-organization](SearchParameter-organizationaffiliation-primary-organization.html)   Type   reference   Example  `GET [base]/OrganizationAffiliation?primary-organization=[primary-organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-08

**Summary**: Support OrganizationAffiliation search by participating-organization
**Description**: "Conformance **SHALL**   Parameter   [participating-organization](SearchParameter-organizationaffiliation-participating-organization.html)   Type   reference   Example  `GET [base]/OrganizationAffiliation?participating-organization=[participating-organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-09

**Summary**: Support OrganizationAffiliation search by location
**Description**: "Conformance **SHALL**   Parameter   [location](SearchParameter-organizationaffiliation-location.html)   Type   reference   Example  `GET [base]/OrganizationAffiliation?location=[location]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-10

**Summary**: Support OrganizationAffiliation search by service
**Description**: "Conformance **SHALL**   Parameter   [service](SearchParameter-organizationaffiliation-service.html)   Type   reference   Example  `GET [base]/OrganizationAffiliation?service=[service]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-11

**Summary**: Support OrganizationAffiliation search by network
**Description**: "Conformance **SHALL**   Parameter   [network](SearchParameter-organizationaffiliation-network.html)   Type   reference   Example  `GET [base]/OrganizationAffiliation?network=[network]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-12

**Summary**: Support OrganizationAffiliation search by endpoint
**Description**: "Conformance **SHALL**   Parameter   [endpoint](SearchParameter-organizationaffiliation-endpoint.html)   Type   reference   Example  `GET [base]/OrganizationAffiliation?endpoint=[endpoint]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-13

**Summary**: Support OrganizationAffiliation search by role
**Description**: "Conformance **SHALL**   Parameter   [role](SearchParameter-organizationaffiliation-role.html)   Type   token   Example  `GET [base]/OrganizationAffiliation?role=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-14

**Summary**: Support OrganizationAffiliation search by specialty
**Description**: "Conformance **SHALL**   Parameter   [specialty](SearchParameter-organizationaffiliation-specialty.html)   Type   token   Example  `GET [base]/OrganizationAffiliation?specialty=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-15

**Summary**: Support OrganizationAffiliation search by _id
**Description**: "Conformance **SHALL**   Parameter   [_id](http://hl7.org/fhir/R4/search.html)   Type   token   Example  `GET [base]/OrganizationAffiliation?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-16

**Summary**: Support OrganizationAffiliation search by _lastUpdated
**Description**: "Conformance **SHALL**   Parameter   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   Type   date   Example  `GET [base]/OrganizationAffiliation?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: OrganizationAffiliation, Search Parameter Summary Section

## REQ-SERVER-SHALL-17

**Summary**: Support Practitioner Resource
**Description**: "Conformance Expectation: **SHALL**"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner Section

## REQ-SERVER-SHALL-18

**Summary**: Support Practitioner Profile
**Description**: "Supported Profiles: [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner Section

## REQ-SERVER-SHALL-19

**Summary**: Implement Practitioner resolves Reference Policy
**Description**: "Reference Policy: `resolves`"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner Section

## REQ-SERVER-SHALL-20

**Summary**: Support Practitioner search-type and read interactions
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner, Profile Interaction Summary Section

## REQ-SERVER-SHOULD-03

**Summary**: Support Practitioner vread interaction
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Practitioner, Profile Interaction Summary Section

## REQ-SERVER-SHALL-21

**Summary**: Return Practitioner using ID
**Description**: "A Server **SHALL** be capable of returning a Practitioner resource using: `GET [base]/Practitioner/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner, Fetch and Search Criteria Section

## REQ-SERVER-SHOULD-04

**Summary**: Return Practitioner history using ID and version ID
**Description**: "A Server **SHOULD** be capable of returning a Practitioner resource using: `GET [base]/Practitioner/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: Practitioner, Fetch and Search Criteria Section

## REQ-SERVER-SHALL-22

**Summary**: Support Practitioner revincludes
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes:
PractitionerRole:practitioner - `GET [base]/Practitioner?[parameter=value]&_revinclude=PractitionerRole:practitioner`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner, Fetch and Search Criteria Section

## REQ-SERVER-SHALL-23

**Summary**: Support Practitioner search by name
**Description**: "Conformance **SHALL**   Parameter   [name](SearchParameter-practitioner-name.html)   Type   string   Example  `GET [base]/Practitioner?name=[name]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner, Search Parameter Summary Section

## REQ-SERVER-SHALL-24

**Summary**: Support Practitioner search by _id
**Description**: "Conformance **SHALL**   Parameter   [_id](http://hl7.org/fhir/R4/search.html)   Type   token   Example  `GET [base]/Practitioner?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner, Search Parameter Summary Section

## REQ-SERVER-SHALL-25

**Summary**: Support Practitioner search by _lastUpdated
**Description**: "Conformance **SHALL**   Parameter   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   Type   date   Example  `GET [base]/Practitioner?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner, Search Parameter Summary Section

## REQ-SERVER-SHALL-26

**Summary**: Support Practitioner search by family
**Description**: "Conformance **SHALL**   Parameter   [family](SearchParameter-practitioner-family-name.html)   Type   string   Example  `GET [base]/Practitioner?family=[family]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner, Search Parameter Summary Section

## REQ-SERVER-SHALL-27

**Summary**: Support Practitioner search by given
**Description**: "Conformance **SHALL**   Parameter   [given](SearchParameter-practitioner-given-name.html)   Type   string   Example  `GET [base]/Practitioner?given=[given]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: Practitioner, Search Parameter Summary Section
## REQ-SERVER-SHALL-01

**Summary**: Support PractitionerRole Resource
**Description**: "Conformance Expectation: **SHALL** Supported Profiles: [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)"
**Verification**: Inspection
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole Section

## REQ-SERVER-SHALL-02

**Summary**: Support PractitionerRole search-type and read interactions
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Profile Interaction Summary

## REQ-SERVER-SHOULD-01

**Summary**: Support PractitionerRole vread interaction
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: PractitionerRole - Profile Interaction Summary

## REQ-SERVER-SHALL-03

**Summary**: Return PractitionerRole using ID
**Description**: "A Server **SHALL** be capable of returning a PractitionerRole resource using: `GET [base]/PractitionerRole/[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Fetch and Search Criteria

## REQ-SERVER-SHOULD-02

**Summary**: Return PractitionerRole version using ID and version ID
**Description**: "A Server **SHOULD** be capable of returning a PractitionerRole resource using: `GET [base]/PractitionerRole/[id]/_history/vid`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHOULD, Conditional: False
**Source**: PractitionerRole - Fetch and Search Criteria

## REQ-SERVER-SHALL-04

**Summary**: Support PractitionerRole includes for practitioner
**Description**: "A Server **SHALL** be capable of supporting the following _includes: PractitionerRole:practitioner - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:practitioner`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Fetch and Search Criteria

## REQ-SERVER-SHALL-05

**Summary**: Support PractitionerRole includes for organization
**Description**: "A Server **SHALL** be capable of supporting the following _includes: PractitionerRole:organization - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:organization`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Fetch and Search Criteria

## REQ-SERVER-SHALL-06

**Summary**: Support PractitionerRole includes for location
**Description**: "A Server **SHALL** be capable of supporting the following _includes: PractitionerRole:location - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:location`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Fetch and Search Criteria

## REQ-SERVER-SHALL-07

**Summary**: Support PractitionerRole includes for service
**Description**: "A Server **SHALL** be capable of supporting the following _includes: PractitionerRole:service - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:service`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Fetch and Search Criteria

## REQ-SERVER-SHALL-08

**Summary**: Support PractitionerRole includes for network
**Description**: "A Server **SHALL** be capable of supporting the following _includes: PractitionerRole:network - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:network`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Fetch and Search Criteria

## REQ-SERVER-SHALL-09

**Summary**: Support PractitionerRole includes for endpoint
**Description**: "A Server **SHALL** be capable of supporting the following _includes: PractitionerRole:endpoint - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:endpoint`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Fetch and Search Criteria

## REQ-SERVER-SHALL-10

**Summary**: Support PractitionerRole search by practitioner
**Description**: "**SHALL** [practitioner](SearchParameter-practitionerrole-practitioner.html) reference `GET [base]/PractitionerRole?practitioner=[practitioner]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-11

**Summary**: Support PractitionerRole search by organization
**Description**: "**SHALL** [organization](SearchParameter-practitionerrole-organization.html) reference `GET [base]/PractitionerRole?organization=[organization]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-12

**Summary**: Support PractitionerRole search by location
**Description**: "**SHALL** [location](SearchParameter-practitionerrole-location.html) reference `GET [base]/PractitionerRole?location=[location]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-13

**Summary**: Support PractitionerRole search by service
**Description**: "**SHALL** [service](SearchParameter-practitionerrole-service.html) reference `GET [base]/PractitionerRole?service=[service]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-14

**Summary**: Support PractitionerRole search by network
**Description**: "**SHALL** [network](SearchParameter-practitionerrole-network.html) reference `GET [base]/PractitionerRole?network=[network]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-15

**Summary**: Support PractitionerRole search by endpoint
**Description**: "**SHALL** [endpoint](SearchParameter-practitionerrole-endpoint.html) reference `GET [base]/PractitionerRole?endpoint=[endpoint]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-16

**Summary**: Support PractitionerRole search by role
**Description**: "**SHALL** [role](SearchParameter-practitionerrole-role.html) token `GET [base]/PractitionerRole?role=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-17

**Summary**: Support PractitionerRole search by specialty
**Description**: "**SHALL** [specialty](SearchParameter-practitionerrole-specialty.html) token `GET [base]/PractitionerRole?specialty=[system] [code]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-18

**Summary**: Support PractitionerRole search by _id
**Description**: "**SHALL** [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/PractitionerRole?_id=[id]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary

## REQ-SERVER-SHALL-19

**Summary**: Support PractitionerRole search by _lastUpdated
**Description**: "**SHALL** [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/PractitionerRole?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False
**Source**: PractitionerRole - Search Parameter Summary
## Da Vinci PDex Plan Net Implementation Guide v1.2.0
## Requirements Extraction - Chunk 1 of 7: Artifacts Summary

This document extracts testable requirements from the "Artifacts Summary" section of the Da Vinci PDex Plan Net Implementation Guide v1.2.0. This section primarily provides an overview of the artifacts within the guide and sets the context for the capabilities expected of conformant systems.

While this section contains important information about the implementation guide's structure and the expectations for conformant systems, it does **not** contain explicitly testable requirements using SHALL, SHOULD, MAY, MUST, REQUIRED, etc. Therefore, no requirements are extracted from this section. 

The following sections, which detail specific artifacts like Capability Statements, Search Parameters, and Resource Profiles, are expected to contain concrete requirements that can be extracted and formatted according to the provided guidelines. 
## REQ-SERVER-SHALL-01

**Summary**: Support `endpoint-organization` search parameter for Endpoints
**Description**: "Select Endpoints managed by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**:  [Plannet_sp_endpoint_organization](SearchParameter-endpoint-organization.html "SearchParameter/endpoint-organization")

## REQ-SERVER-SHALL-02

**Summary**: Support `coverage-area` search parameter for HealthcareServices
**Description**: "Select services available in a region described by the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_healthcareservice_coverage_area](SearchParameter-healthcareservice-coverage-area.html "SearchParameter/healthcareservice-coverage-area")

## REQ-SERVER-SHALL-03

**Summary**: Support `organization` search parameter for HealthcareServices
**Description**: "Select HealthcareServices provided by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_healthcareservice_organization](SearchParameter-healthcareservice-organization.html "SearchParameter/healthcareservice-organization")

## REQ-SERVER-SHALL-04

**Summary**: Support `endpoint` search parameter for HealthcareServices
**Description**: "Select HealthcareServices with the specified endpoint"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_healthcareservice_endpoint](SearchParameter-healthcareservice-endpoint.html "SearchParameter/healthcareservice-endpoint")

## REQ-SERVER-SHALL-05

**Summary**: Support `location` search parameter for HealthcareServices
**Description**: "Select HealthcareServices available at the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_healthcareservice_location](SearchParameter-healthcareservice-location.html "SearchParameter/healthcareservice-location")

## REQ-SERVER-SHALL-06

**Summary**: Support `name` search parameter for HealthcareServices
**Description**: "Select HealthcareServices with the specified name"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_healthcareservice_name](SearchParameter-healthcareservice-name.html "SearchParameter/healthcareservice-name")

## REQ-SERVER-SHALL-07

**Summary**: Support `service-category` search parameter for HealthcareServices
**Description**: "Select HealthcareServices providing the specified category of services"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_healthcareservice_category](SearchParameter-healthcareservice-service-category.html "SearchParameter/healthcareservice-service-category")

## REQ-SERVER-SHALL-08

**Summary**: Support `service-type` search parameter for HealthcareServices
**Description**: "Select HealthcareServices of the specified type"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_healthcareservice_type](SearchParameter-healthcareservice-service-type.html "SearchParameter/healthcareservice-service-type")

## REQ-SERVER-SHALL-09

**Summary**: Support `specialty` search parameter for HealthcareServices
**Description**: "Select services associated with the specified specialty"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_healthcareservice_specialty](SearchParameter-healthcareservice-specialty.html "SearchParameter/healthcareservice-specialty")

## REQ-SERVER-SHALL-10

**Summary**: Support `administered-by` search parameter for InsurancePlans
**Description**: "Select products that are administered by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_insuranceplan_administered_by](SearchParameter-insuranceplan-administered-by.html "SearchParameter/insuranceplan-administered-by")

## REQ-SERVER-SHALL-11

**Summary**: Support `coverage-area` search parameter for InsurancePlans
**Description**: "Select products that are offered in the specified location"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_insuranceplan_coverage_area](SearchParameter-insuranceplan-coverage-area.html "SearchParameter/insuranceplan-coverage-area")

## REQ-SERVER-SHALL-12

**Summary**: Support `identifier` search parameter for InsurancePlans
**Description**: "Select products with the specified identifier"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_insuranceplan_identifier](SearchParameter-insuranceplan-identifier.html "SearchParameter/insuranceplan-identifier")

## REQ-SERVER-SHALL-13

**Summary**: Support `name` search parameter for InsurancePlans
**Description**: "Select products with the specified name"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_insuranceplan_name](SearchParameter-insuranceplan-name.html "SearchParameter/insuranceplan-name")

## REQ-SERVER-SHALL-14

**Summary**: Support `owned-by` search parameter for InsurancePlans
**Description**: "Select products that are owned by the specified organization"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_insuranceplan_owned_by](SearchParameter-insuranceplan-owned_by.html "SearchParameter/insuranceplan-owned_by")

## REQ-SERVER-SHALL-15

**Summary**: Support `plan-type` search parameter for InsurancePlans
**Description**: "Select plans of the specified type"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_insuranceplan_plan_type](SearchParameter-insuranceplan-plan-type.html "SearchParameter/insuranceplan-plan-type")

## REQ-SERVER-SHALL-16

**Summary**: Support `type` search parameter for InsurancePlans
**Description**: "Select insurance plans of the specified type"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_insuranceplan_type](SearchParameter-insuranceplan-type.html "SearchParameter/insuranceplan-type")

## REQ-SERVER-SHALL-17

**Summary**: Support `address-city` search parameter for Locations
**Description**: "Select Locations with the specified address.city"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL (derived from SHOULD), Conditional: False
**Source**: [Plannet_sp_location_address_city](SearchParameter-location-address-city.html "SearchParameter/location-address-city") 
## REQ-SERVER-SHALL-01

**Summary**: Support `location-address-postalcode` search parameter for Location resources.
**Description**: "Select Locations with the specified address"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False, Resource: Location
**Source**: [Plannet_sp_location_address_postalcode](SearchParameter-location-address-postalcode.html "SearchParameter/location-address-postalcode")

## REQ-SERVER-SHALL-02

**Summary**: Support `location-address-state` search parameter for Location resources.
**Description**: "Select Locations with the specified address.state"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False, Resource: Location
**Source**: [Plannet_sp_location_address_state](SearchParameter-location-address-state.html "SearchParameter/location-address-state")

## REQ-SERVER-SHALL-03

**Summary**: Support `location-address` search parameter for Location resources.
**Description**: "Select Locations with the specified address"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False, Resource: Location
**Source**: [Plannet_sp_location_address](SearchParameter-location-address.html "SearchParameter/location-address")

**(Similarly for the rest of the search parameters)**

...

## REQ-SERVER-SHALL-29

**Summary**: Support `practitionerrole-specialty` search parameter for PractitionerRole resources.
**Description**: "Select PractitionerRoles associated with the specified specialty"
**Verification**: Test
**Notes**: Actor: Server, Conformance: SHALL, Conditional: False, Resource: PractitionerRole
**Source**: [Plannet_sp_practitionerrole_specialty](SearchParameter-practitionerrole-specialty.html "SearchParameter/practitionerrole-specialty") 

**Note:** This document assumes that all search parameters listed are mandatory and follows the "SHALL" conformance level. If any of these search parameters are optional, the conformance level and description should be adjusted accordingly. 
##  PlanNet Implementation Guide v1.2.0 - Structures: Resource Profiles Requirements Extraction 

This section analyzes the "Structures: Resource Profiles" section of the Da Vinci PDex Plan Net Implementation Guide v1.2.0, focusing on extracting testable requirements related to the defined FHIR resource profiles. 

**Important Note:** This section primarily defines FHIR resource profiles, which act as templates with specific constraints for data exchange. These profiles themselves don't contain explicit SHALL/SHOULD statements to form testable requirements. They define data structures and expectations but don't directly translate into actionable requirements for system behavior. 

Therefore, no explicit, testable requirements can be extracted from this section of the Da Vinci PDex Plan Net Implementation Guide v1.2.0 using the provided guidelines. 

However, these profiles are essential for understanding the data elements and constraints relevant to different healthcare entities and interactions within the PlanNet context. They will be crucial when interpreting requirements in other sections of the implementation guide that deal with specific API interactions or data exchange scenarios. 
## Requirements Extraction: Da Vinci PDex Plan Net Implementation Guide v1.2.0 (Chunk 5/7)

This section focuses on extracting requirements from the "Structures: Extension Definitions" section of the Da Vinci PDex Plan Net Implementation Guide v1.2.0. This section defines various FHIR extension definitions to convey specific information relevant to the implementation guide. 

**Important Note:** This section primarily describes structural definitions and constraints rather than explicit, testable requirements using SHALL, SHOULD, MAY, etc. Therefore, no testable requirements can be extracted in the INCOSE format from this chunk. 

While these structure definitions imply certain functionalities, they are not formulated as testable requirements.  To create testable requirements, we would need additional context on how these structures are intended to be used within specific operations or interactions. 
## Da Vinci PDex Plan Net Implementation Guide v1.2.0: Terminology Requirements Extraction

This section analyzes chunk 6 of 7 from the Da Vinci PDex Plan Net Implementation Guide v1.2.0, focusing on terminology defined by the guide. This chunk primarily documents value sets and code systems but does not contain explicit requirements using SHALL, SHOULD, MAY, MUST, REQUIRED, or similar language. 

Therefore, no testable requirements are extracted from this section. 
## Introduction to Requirements Extracted from Da Vinci PDex Plan Net Implementation Guide v1.2.0, Chunk 7 of 7

This section analyzes "Example Instances" from the Da Vinci PDex Plan Net Implementation Guide v1.2.0 for extractable requirements. This section primarily provides example instances of various FHIR resources and does not contain testable requirements. Therefore, no requirements are extracted from this chunk. 

While this chunk showcases practical applications of the implementation guide's specifications, it doesn't define any rules or behaviors that systems **SHALL**, **SHOULD**, or **MAY** follow. 
