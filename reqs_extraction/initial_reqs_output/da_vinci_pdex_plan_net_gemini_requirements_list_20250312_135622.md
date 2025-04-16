---
# REQ-SERVER-SHALL-01
**Summary**: Prohibit requirement of consumer identifying information for content query.
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations
---
---
# REQ-CLIENT-SHALL-01
**Summary**: Prohibit sending consumer identifiable information when querying Plan-Net service.
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Test
**Actor**: Client (Directory mobile application)
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations
---
---
# REQ-SERVER-SHALL-02
**Summary**: Populate all Must Support data elements for query results.
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Server (Health Plan API actor)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements
---
---
# REQ-SERVER-SHALL-03
**Summary**:  Omit data elements with minimum cardinality 0 when information is not present.
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Actor**: Server (Health Plan API actor)
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements
---
---
# REQ-SERVER-SHALL-04
**Summary**: Provide reason for missing information for Must Support data elements with minimum cardinality > 0.
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Actor**: Server (Health Plan API actor)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements
---
---
# REQ-CLIENT-SHALL-02
**Summary**: Process resource instances containing Must Support data elements without errors.
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Client (Application actor)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements
---
---
# REQ-CLIENT-SHOULD-01
**Summary**: Display or store Must Support data elements for human use.
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Actor**: Client (Application actor)
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements
---
---
# REQ-CLIENT-SHALL-03
**Summary**: Interpret missing Must Support data elements as not present in the Health Plan API system.
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Actor**: Client (Application actor)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements
---
---
# REQ-CLIENT-SHALL-04
**Summary**: Process resource instances containing Must Support data elements with missing information.
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Actor**: Client (Consumer App actor)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Support HealthcareService search by category and specialty
**Description**: "The first type of search starts from HealthcareService.category and HealthcareService.specialty, so it is essential that each provider's service be supported by appropriate set of HealthcareService instances."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD (derived from "essential")
**Conditional**: False
**Source**: HealthcareService Section
---
---
# REQ-SERVER-SHOULD-02
**Summary**: Define HealthcareServices for service organization
**Description**: "All organizations that provide service should define an appropriate set of HealthcareServices to facilitate search."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService Section
---
---
# REQ-SERVER-SHOULD-03
**Summary**: Represent Insurance Plans and associated Networks
**Description**: "Each payer will offer one or more products -- Insurance Plans -- and each plan is associated with one or more Networks."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD (derived from "will")
**Conditional**: False
**Source**: Insurance Plan and Network Section
---
---
# REQ-SERVER-SHOULD-04
**Summary**: Link Practitioners and Organizations to Networks
**Description**: "Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD (derived from "indicate")
**Conditional**: False
**Source**: Insurance Plan and Network Section
---
---
# REQ-SERVER-SHOULD-05
**Summary**: Associate PractitionerRole and OrganizationAffiliation with HealthcareServices, Organizations, Networks, and Locations
**Description**: "PractitionerRole and OrganizationAffiliation instances are what tie Practitioners and Organizations to HealthcareServices, Organizations, Networks and Locations."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD (derived from "are what tie")
**Conditional**: False
**Source**: Insurance Plan and Network Section
---
---
# REQ-SERVER-SHOULD-06
**Summary**: Provide Location information for service provision
**Description**: "Location instances provide information about location where service is provided, including contact information, address, accessibility, hours of operation and contact, as well as position (latitude and longitude)."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD (derived from "provide")
**Conditional**: False
**Source**: Location Section
---
---
# REQ-SERVER-MAY-01
**Summary**: Represent regions using Location with GeoJSON
**Description**: "Locations can also be used to represent regions using an associated or attached GeoJSON object."
**Verification**: Inspection
**Actor**: Server
**Conformance**: MAY
**Conditional**: False
**Source**: Location Section
---
---
# REQ-SERVER-SHOULD-07
**Summary**: Provide Practitioner information
**Description**: "Practitioner instances provide information about a specific person, including name, gender, languages spoken, and qualifications."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD (derived from "provide")
**Conditional**: False
**Source**: Practitioners and PractitionerRoles Section
---
---
# REQ-SERVER-SHOULD-08
**Summary**: Define PractitionerRole and associate with relevant information
**Description**: "PractitionerRole defines a role for a particular practitioner, and associates it with locations, specialties, an organization, and networks."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD (derived from "defines" and "associates")
**Conditional**: False
**Source**: Practitioners and PractitionerRoles Section
---
---
# REQ-SERVER-SHALL-01
**Summary**: Support all defined profiles.
**Description**: "The Plan-Net Server **SHALL**: 1. Support all profiles defined in this Implementation Guide."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-02
**Summary**: Implement RESTful behavior according to FHIR specification.
**Description**: "The Plan-Net Server **SHALL**: 2. Implement the RESTful behavior according to the FHIR specification."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-03
**Summary**: Return specific response classes.
**Description**: "The Plan-Net Server **SHALL**: 3. Return the following response classes:
* (Status 400): invalid parameter
* (Status 401/4xx): unauthorized request
* (Status 403): insufficient scope
* (Status 404): unknown resource
* (Status 410): deleted resource."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-04
**Summary**: Support JSON format for Plan-Net interactions.
**Description**: "The Plan-Net Server **SHALL**: 4. Support json source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-05
**Summary**: Identify supported Plan-Net profiles using meta.profile attribute.
**Description**: "The Plan-Net Server **SHALL**: 5. Identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-06
**Summary**: Support searchParameters individually and in combination.
**Description**: "The Plan-Net Server **SHALL**: 6. Support the searchParameters on each profile individually and in combination."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-07
**Summary**: Support forward and reverse chaining for search parameters with 'chain' property.
**Description**: "The Plan-Net Server **SHALL**: 7. Support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Support XML format for Plan-Net interactions.
**Description**: "The Plan-Net Server **SHOULD**: 1. Support xml source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-08
**Summary**: Reject unauthorized requests with HTTP 401.
**Description**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, Security
---
---
# REQ-SERVER-SHALL-01
**Summary**: Support Plan-Net Endpoint profile and search-type, read interactions.
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)
Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint Section
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Support vread interaction for Endpoint resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Endpoint Section
---
---
# REQ-SERVER-SHALL-02
**Summary**: Return Endpoint resource using ID.
**Description**: "A Server **SHALL** be capable of returning a Endpoint resource using:
`GET [base]/Endpoint/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-02
**Summary**: Return Endpoint resource using ID and version ID.
**Description**: "A Server **SHOULD** be capable of returning a Endpoint resource using:
`GET [base]/Endpoint/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Endpoint Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-03
**Summary**: Support _include for Endpoint:organization.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-04
**Summary**: Support search by organization, _id, and _lastUpdated for Endpoint.
**Description**: "Search Parameter Summary:
Conformance   Parameter   Type   Example
**SHALL**   [organization](SearchParameter-endpoint-organization.html)   reference   `GET [base]/Endpoint?organization=[organization]`
**SHALL**   [_id](http://hl7.org/fhir/R4/search.html)   token   `GET [base]/Endpoint?_id=[id]`
**SHALL**   [_lastUpdated](http://hl7.org/fhir/R4/search.html)   date   `GET [base]/Endpoint?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint Section - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-05
**Summary**: Support Plan-Net HealthcareService profile and search-type, read interactions.
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)
Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService Section
---
---
# REQ-SERVER-SHOULD-03
**Summary**: Support vread interaction for HealthcareService resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService Section
---
---
# REQ-SERVER-SHALL-06
**Summary**: Return HealthcareService resource using ID.
**Description**: "A Server **SHALL** be capable of returning a HealthcareService resource using:
`GET [base]/HealthcareService/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-04
**Summary**: Return HealthcareService resource using ID and version ID.
**Description**: "A Server **SHOULD** be capable of returning a HealthcareService resource using:
`GET [base]/HealthcareService/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-07
**Summary**: Support _includes for HealthcareService:location, :coverage-area, :organization, and :endpoint.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
HealthcareService:location - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:location`
HealthcareService:coverage-area - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:coverage-area`
HealthcareService:organization - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:organization`
HealthcareService:endpoint - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:endpoint`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-08
**Summary**: Support _revincludes for PractitionerRole:service and OrganizationAffiliation:service.
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes:
PractitionerRole:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=PractitionerRole:service`
OrganizationAffiliation:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=OrganizationAffiliation:service`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-09
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
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService Section - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-10
**Summary**: Support Plan-Net InsurancePlan profile and search-type, read interactions.
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html)
Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan Section
---
---
# REQ-SERVER-SHOULD-05
**Summary**: Support vread interaction for InsurancePlan resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: InsurancePlan Section
---
---
# REQ-SERVER-SHALL-11
**Summary**: Return InsurancePlan resource using ID.
**Description**: "A Server **SHALL** be capable of returning a InsurancePlan resource using:
`GET [base]/InsurancePlan/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-06
**Summary**: Return InsurancePlan resource using ID and version ID.
**Description**: "A Server **SHOULD** be capable of returning a InsurancePlan resource using:
`GET [base]/InsurancePlan/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: InsurancePlan Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-12
**Summary**: Support _includes for InsurancePlan:administered-by, :owned-by, and :coverage-area.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
InsurancePlan:administered-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:administered-by`
InsurancePlan:owned-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:owned-by`
InsurancePlan:coverage-area - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:coverage-area`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan Section - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-13
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
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan Section - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-01
**Summary**: Support Location Resource with Plan-Net Profile
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net Location](StructureDefinition-plannet-Location.html)"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section
---
---
# REQ-SERVER-SHALL-02
**Summary**: Support search-type and read interactions for Location resource.
**Description**: "Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Support vread interaction for Location resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Location Section
---
---
# REQ-SERVER-SHALL-03
**Summary**: Return Location resource by ID.
**Description**: "A Server **SHALL** be capable of returning a Location resource using:
`GET [base]/Location/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-02
**Summary**: Return Location resource by ID and version.
**Description**: "A Server **SHOULD** be capable of returning a Location resource using:
`GET [base]/Location/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-04
**Summary**: Support _include for Location resource.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
Location:endpoint - `GET [base]/Location?[parameter=value]&_include=Location:endpoint`
Location:organization - `GET [base]/Location?[parameter=value]&_include=Location:organization`
Location:partof - `GET [base]/Location?[parameter=value]&_include=Location:partof`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-05
**Summary**: Support _revinclude for Location resource.
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes:
HealthcareService:location - `GET [base]/Location?[parameter=value]&_revinclude=HealthcareService:location`
InsurancePlan:coverage-area - `GET [base]/Location?[parameter=value]&_revinclude=InsurancePlan:coverage-area`
OrganizationAffiliation:location - `GET [base]/Location?[parameter=value]&_revinclude=OrganizationAffiliation:location`
PractitionerRole:location - `GET [base]/Location?[parameter=value]&_revinclude=PractitionerRole:location`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-06
**Summary**: Support all SHALL search parameters for Location resource.
**Description**: "Search Parameter Summary - Conformance column: **SHALL**"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary.  Note: This requirement consolidates all SHALL requirements for search parameters within the Location section. Individual requirements can be created for each parameter if desired.
---
---
# REQ-SERVER-SHALL-07
**Summary**: Support Organization Resource with Plan-Net Profiles
**Description**: "Conformance Expectation: **SHALL**
Supported Profiles:
[Plan-Net Network](StructureDefinition-plannet-Network.html),
[Plan-Net Organization](StructureDefinition-plannet-Organization.html)"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section
---
---
# REQ-SERVER-SHALL-08
**Summary**: Support search-type and read interactions for Organization resource.
**Description**: "Profile Interaction Summary:
* **SHALL** support
`search-type`,
`read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section
---
---
# REQ-SERVER-SHOULD-03
**Summary**: Support vread interaction for Organization resource.
**Description**: "Profile Interaction Summary:
* **SHOULD** support
`vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Organization Section
---
---
# REQ-SERVER-SHALL-09
**Summary**: Return Organization resource by ID.
**Description**: "A Server **SHALL** be capable of returning a Organization resource using:
`GET [base]/Organization/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-04
**Summary**: Return Organization resource by ID and version.
**Description**: "A Server **SHOULD** be capable of returning a Organization resource using:
`GET [base]/Organization/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-10
**Summary**: Support _include for Organization resource.
**Description**: "A Server **SHALL** be capable of supporting the following _includes:
Organization:partof - `GET [base]/Organization?[parameter=value]&_include=Organization:partof`
Organization:endpoint - `GET [base]/Organization?[parameter=value]&_include=Organization:endpoint`
Organization:coverage-area - `GET [base]/Organization?[parameter=value]&_include=Organization:coverage-area`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-11
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
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-12
**Summary**: Support all SHALL search parameters for Organization resource.
**Description**: "Search Parameter Summary - Conformance column: **SHALL**"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Search Parameter Summary.  Note: This requirement consolidates all SHALL requirements for search parameters within the Organization section. Individual requirements can be created for each parameter if desired.
---
---
# REQ-SERVER-SHALL-01
**Summary**: Support OrganizationAffiliation Resource
**Description**: "Conformance Expectation: **SHALL**"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: OrganizationAffiliation Section
---
---
# REQ-SERVER-SHALL-02
**Summary**: Support OrganizationAffiliation Profile
**Description**: "Supported Profiles: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: OrganizationAffiliation Section
---
---
# REQ-SERVER-SHALL-03
**Summary**: Implement OrganizationAffiliation resolves Reference Policy
**Description**: "Reference Policy: `resolves`"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: OrganizationAffiliation Section
---
---
# REQ-SERVER-SHALL-04
**Summary**: Support OrganizationAffiliation search-type and read interactions
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: OrganizationAffiliation, Profile Interaction Summary Section
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Support OrganizationAffiliation vread interaction
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: OrganizationAffiliation, Profile Interaction Summary Section
---
---
# REQ-SERVER-SHALL-05
**Summary**: Return OrganizationAffiliation using ID
**Description**: "A Server **SHALL** be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: OrganizationAffiliation, Fetch and Search Criteria Section
---
---
# REQ-SERVER-SHOULD-02
**Summary**: Return OrganizationAffiliation history using ID and version ID
**Description**: "A Server **SHOULD** be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: OrganizationAffiliation, Fetch and Search Criteria Section
---
---
# REQ-SERVER-SHALL-06
**Summary**: Support OrganizationAffiliation includes
**Description**: "A Server **SHALL** be capable of supporting the following _includes: 
OrganizationAffiliation:primary-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:primary-organization`
OrganizationAffiliation:participating-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:participating-organization`
OrganizationAffiliation