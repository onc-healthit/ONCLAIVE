---
# REQ-SERVER-SHALL-NOT-01
**Summary**: Prohibit authentication requirements for Plan-Net service access
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes - Privacy Considerations
---
---
# REQ-SERVER-SHALL-NOT-02
**Summary**: Prohibit directory apps from sending consumer identifying information for queries
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes - Privacy Considerations
---
---
# REQ-CLIENT-SHALL-NOT-01
**Summary**: Prohibit directory apps from sending consumer identifiable information in queries
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Test
**Actor**: Client (Directory Mobile Application)
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes - Privacy Considerations
---
---
# REQ-SERVER-SHALL-01
**Summary**: Populate all Must Support data elements in query results
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Server (Health Plan API)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Health Plan API Requirements
---
---
# REQ-SERVER-SHALL-NOT-03
**Summary**: Exclude data elements with minimum cardinality 0 when information is not present
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0 , the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Actor**: Server (Health Plan API)
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes - Must Support - Health Plan API Requirements
---
---
# REQ-SERVER-SHALL-04
**Summary**: Provide reason for missing information for Must Support data elements with minimum cardinality > 0
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Actor**: Server (Health Plan API)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Health Plan API Requirements
---
---
# REQ-CLIENT-SHALL-02
**Summary**: Process resource instances containing Must Support data elements without errors
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Client (Application)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Application Requirements
---
---
# REQ-CLIENT-SHOULD-01
**Summary**: Display or store Must Support data elements for human use
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Actor**: Client (Application)
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes - Must Support - Application Requirements
---
---
# REQ-CLIENT-SHALL-03
**Summary**: Interpret missing Must Support data elements as not present in the Health Plan API system
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Actor**: Client (Application)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Application Requirements
---
---
# REQ-CLIENT-SHALL-04
**Summary**: Process resource instances containing Must Support data elements asserting missing information
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Actor**: Client (Consumer App)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Application Requirements
---
---
# REQ-CLIENT-SHOULD-02
**Summary**: Utilize lastUpdate timestamp for tracking directory content updates
**Description**: "Clients that cache query results can track additions or modifications to directory content through queries that filter content using the _lastUpdated search parameter."
**Verification**: Test
**Actor**: Client
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes - Client Detection of Updates Directory Content
---
---
# REQ-CLIENT-SHOULD-03
**Summary**: Periodically verify cached data existence using _id queries
**Description**: "Clients should periodically check that data cached from past queries has not been deleted by querying for the same elements by _id."
**Verification**: Test
**Actor**: Client
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes - Client Detection of Updates Directory Content
---
---
# REQ-SERVER-SHALL-01
**Summary**: Support HealthcareService instances for service discovery.
**Description**: "All organizations that provide service should define an appropriate set of HealthcareServices to facilitate search."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService Section
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Associate HealthcareServices with an Organization.
**Description**: "HealthcareServices are typically provided by an organization, except in the case of a Practitioner that is not associated with an organization (see the solo practitioner example)..."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService Section
---
---
# REQ-SERVER-SHOULD-02
**Summary**: Link Practitioners and Organizations to Networks through PractitionerRole and OrganizationAffiliation.
**Description**: "Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Insurance Plan and Network Section
---
---
# REQ-SERVER-SHOULD-03
**Summary**: Utilize PractitionerRole and OrganizationAffiliation to associate Practitioners and Organizations with HealthcareServices, Organizations, Networks, and Locations.
**Description**: "PractitionerRole and OrganizationAffiliation instances are what tie Practitioners and Organizations to HealthcareServices, Organizations, Networks and Locations."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Insurance Plan and Network Section
---
---
# REQ-SERVER-MAY-01
**Summary**: Represent regions using Location instances with GeoJSON.
**Description**: "Locations can also be used to represent regions using an associated or attached GeoJSON object."
**Verification**: Inspection
**Actor**: Server
**Conformance**: MAY
**Conditional**: False
**Source**: Location Section 
---
---
# REQ-SERVER-SHALL-01
**Summary**: Support all defined profiles
**Description**: "The Plan-Net Server **SHALL**: 
1. Support all profiles defined in this Implementation Guide."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-02
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
# REQ-SERVER-SHALL-03
**Summary**: Return specific response classes
**Description**: "The Plan-Net Server **SHALL**: 
3. Return the following response classes:
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
**Summary**: Support JSON format for interactions
**Description**: "The Plan-Net Server **SHALL**: 
4. Support json source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-05
**Summary**: Identify supported Plan-Net profiles in `meta.profile` attribute
**Description**: "The Plan-Net Server **SHALL**: 
5. Identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-06
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
# REQ-SERVER-SHALL-07
**Summary**: Support forward and reverse chaining for specific search parameters
**Description**: "The Plan-Net Server **SHALL**: 
1.Support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Support XML format for interactions
**Description**: "The Plan-Net Server **SHOULD**: 
1. Support xml source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities
---
---
# REQ-SERVER-SHALL-08
**Summary**: Reject unauthorized requests with HTTP 401
**Description**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, Security
---
---
# REQ-SERVER-SHALL-01
**Summary**: Support search-type and read interactions for Endpoint
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Profile Interaction Summary
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Support vread interaction for Endpoint
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Endpoint - Profile Interaction Summary
---
---
# REQ-SERVER-SHALL-02
**Summary**: Return Endpoint resource by ID
**Description**: "A Server SHALL be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-02
**Summary**: Return Endpoint resource by ID and version
**Description**: "A Server SHOULD be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-03
**Summary**: Support _include for Endpoint:organization
**Description**: "A Server SHALL be capable of supporting the following _includes: Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-04
**Summary**: Support search by organization for Endpoint
**Description**: "SHALL [support] [organization](SearchParameter-endpoint-organization.html) reference `GET [base]/Endpoint?organization=[organization]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-05
**Summary**: Support search by _id for Endpoint
**Description**: "SHALL [support] [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/Endpoint?_id=[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-06
**Summary**: Support search by _lastUpdated for Endpoint
**Description**: "SHALL [support] [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/Endpoint?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-07
**Summary**: Support search-type and read interactions for HealthcareService
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Profile Interaction Summary
---
---
# REQ-SERVER-SHOULD-03
**Summary**: Support vread interaction for HealthcareService
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService - Profile Interaction Summary
---
---
# REQ-SERVER-SHALL-08
**Summary**: Return HealthcareService resource by ID
**Description**: "A Server SHALL be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-04
**Summary**: Return HealthcareService resource by ID and version
**Description**: "A Server SHOULD be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-09
**Summary**: Support _includes for HealthcareService
**Description**: "A Server SHALL be capable of supporting the following _includes: HealthcareService:location - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:location` HealthcareService:coverage-area - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:coverage-area` HealthcareService:organization - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:organization` HealthcareService:endpoint - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:endpoint`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-10
**Summary**: Support _revincludes for HealthcareService
**Description**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=PractitionerRole:service` OrganizationAffiliation:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=OrganizationAffiliation:service`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-11
**Summary**: Support search by location for HealthcareService
**Description**: "SHALL [support] [location](SearchParameter-healthcareservice-location.html) reference `GET [base]/HealthcareService?location=[location]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-12
**Summary**: Support search by coverage-area for HealthcareService
**Description**: "SHALL [support] [coverage-area](SearchParameter-healthcareservice-coverage-area.html) reference `GET [base]/HealthcareService?coverage-area=[coverage-area]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-13
**Summary**: Support search by organization for HealthcareService
**Description**: "SHALL [support] [organization](SearchParameter-healthcareservice-organization.html) reference `GET [base]/HealthcareService?organization=[organization]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-14
**Summary**: Support search by endpoint for HealthcareService
**Description**: "SHALL [support] [endpoint](SearchParameter-healthcareservice-endpoint.html) reference `GET [base]/HealthcareService?endpoint=[endpoint]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-15
**Summary**: Support search by name for HealthcareService
**Description**: "SHALL [support] [name](SearchParameter-healthcareservice-name.html) string `GET [base]/HealthcareService?name=[name]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-16
**Summary**: Support search by service-category for HealthcareService
**Description**: "SHALL [support] [service-category](SearchParameter-healthcareservice-service-category.html) token `GET [base]/HealthcareService?service-category=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-17
**Summary**: Support search by service-type for HealthcareService
**Description**: "SHALL [support] [service-type](SearchParameter-healthcareservice-service-type.html) token `GET [base]/HealthcareService?service-type=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-18
**Summary**: Support search by specialty for HealthcareService
**Description**: "SHALL [support] [specialty](SearchParameter-healthcareservice-specialty.html) token `GET [base]/HealthcareService?specialty=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-19
**Summary**: Support search by _id for HealthcareService
**Description**: "SHALL [support] [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/HealthcareService?_id=[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-20
**Summary**: Support search by _lastUpdated for HealthcareService
**Description**: "SHALL [support] [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/HealthcareService?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-21
**Summary**: Support search-type and read interactions for InsurancePlan
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Profile Interaction Summary
---
---
# REQ-SERVER-SHOULD-05
**Summary**: Support vread interaction for InsurancePlan
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: InsurancePlan - Profile Interaction Summary
---
---
# REQ-SERVER-SHALL-22
**Summary**: Return InsurancePlan resource by ID
**Description**: "A Server SHALL be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-06
**Summary**: Return InsurancePlan resource by ID and version
**Description**: "A Server SHOULD be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: InsurancePlan - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-23
**Summary**: Support _includes for InsurancePlan
**Description**: "A Server SHALL be capable of supporting the following _includes: InsurancePlan:administered-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:administered-by` InsurancePlan:owned-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:owned-by` InsurancePlan:coverage-area - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:coverage-area`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-24
**Summary**: Support search by administered-by for InsurancePlan
**Description**: "SHALL [support] [administered-by](SearchParameter-insuranceplan-administered-by.html) reference `GET [base]/InsurancePlan?administered-by=[administered-by]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-25
**Summary**: Support search by owned-by for InsurancePlan
**Description**: "SHALL [support] [owned-by](SearchParameter-insuranceplan-owned-by.html) reference `GET [base]/InsurancePlan?owned-by=[owned-by]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-26
**Summary**: Support search by coverage-area for InsurancePlan
**Description**: "SHALL [support] [coverage-area](SearchParameter-insuranceplan-coverage-area.html) reference `GET [base]/InsurancePlan?coverage-area=[coverage-area]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-27
**Summary**: Support search by name for InsurancePlan
**Description**: "SHALL [support] [name](SearchParameter-insuranceplan-name.html) string `GET [base]/InsurancePlan?name=[name]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-28
**Summary**: Support search by plan-type for InsurancePlan
**Description**: "SHALL [support] [plan-type](SearchParameter-insuranceplan-plan-type.html) token `GET [base]/InsurancePlan?plan-type=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-29
**Summary**: Support search by identifier for InsurancePlan
**Description**: "SHALL [support] [identifier](SearchParameter-insuranceplan-identifier.html) token `GET [base]/InsurancePlan?identifier=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-30
**Summary**: Support search by _id for InsurancePlan
**Description**: "SHALL [support] [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/InsurancePlan?_id=[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-31
**Summary**: Support search by _lastUpdated for InsurancePlan
**Description**: "SHALL [support] [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/InsurancePlan?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-32
**Summary**: Support search by type for InsurancePlan
**Description**: "SHALL [support] [type](SearchParameter-insuranceplan-type.html) token `GET [base]/InsurancePlan?type=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary
---
---
# REQ-SERVER-SHALL-01
**Summary**: Support Location resource profile
**Description**: "Conformance Expectation: **SHALL** Supported Profiles: [Plan-Net Location](StructureDefinition-plannet-Location.html)"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section
---
---
# REQ-SERVER-SHALL-02
**Summary**: Support Location search-type and read interactions
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Profile Interaction Summary
---
---
# REQ-SERVER-SHOULD-01
**Summary**: Support Location vread interaction
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Location Section, Profile Interaction Summary
---
---
# REQ-SERVER-SHALL-03
**Summary**: Return Location resource by ID
**Description**: "A Server **SHALL** be capable of returning a Location resource using: `GET [base]/Location/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-02
**Summary**: Return Location resource history by version ID
**Description**: "A Server **SHOULD** be capable of returning a Location resource using: `GET [base]/Location/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-04
**Summary**: Support Location _includes
**Description**: "A Server **SHALL** be capable of supporting the following _includes: Location:endpoint - `GET [base]/Location?[parameter=value]&_include=Location:endpoint` Location:organization - `GET [base]/Location?[parameter=value]&_include=Location:organization` Location:partof - `GET [base]/Location?[parameter=value]&_include=Location:partof`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-05
**Summary**: Support Location _revincludes
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes: HealthcareService:location - `GET [base]/Location?[parameter=value]&_revinclude=HealthcareService:location` InsurancePlan:coverage-area - `GET [base]/Location?[parameter=value]&_revinclude=InsurancePlan:coverage-area` OrganizationAffiliation:location - `GET [base]/Location?[parameter=value]&_revinclude=OrganizationAffiliation:location` PractitionerRole:location - `GET [base]/Location?[parameter=value]&_revinclude=PractitionerRole:location`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-06
**Summary**: Support all Location search parameters
**Description**: "Conformance Parameter Type Example **SHALL** [partof](SearchParameter-location-partof.html) reference `GET [base]/Location?partof=[partof]` **SHALL** [organization](SearchParameter-location-organization.html) reference `GET [base]/Location?organization=[organization]` **SHALL** [endpoint](SearchParameter-location-endpoint.html) reference `GET [base]/Location?endpoint=[endpoint]` **SHALL** [address-city](SearchParameter-location-address-city.html) string `GET [base]/Location?address-city=[address-city]` **SHALL** [address-state](SearchParameter-location-address-state.html) string `GET [base]/Location?address-state=[address-state]` **SHALL** [address-postalcode](SearchParameter-location-address-postalcode.html) string `GET [base]/Location?address-postalcode=[address-postalcode]` **SHALL** [address](SearchParameter-location-address.html) string `GET [base]/Location?address=[address]` **SHALL** [type](SearchParameter-location-type.html) token `GET [base]/Location?type=[system] [code]` **SHALL** [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/Location?_id=[id]` **SHALL** [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/Location?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary
---
---
# REQ-SERVER-SHALL-07
**Summary**: Support Organization resource profiles
**Description**: "Conformance Expectation: **SHALL** Supported Profiles: [Plan-Net Network](StructureDefinition-plannet-Network.html), [Plan-Net Organization](StructureDefinition-plannet-Organization.html)"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section
---
---
# REQ-SERVER-SHALL-08
**Summary**: Support Organization search-type and read interactions
**Description**: "**SHALL** support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Profile Interaction Summary
---
---
# REQ-SERVER-SHOULD-03
**Summary**: Support Organization vread interaction
**Description**: "**SHOULD** support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Organization Section, Profile Interaction Summary
---
---
# REQ-SERVER-SHALL-09
**Summary**: Return Organization resource by ID
**Description**: "A Server **SHALL** be capable of returning a Organization resource using: `GET [base]/Organization/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHOULD-04
**Summary**: Return Organization resource history by version ID
**Description**: "A Server **SHOULD** be capable of returning a Organization resource using: `GET [base]/Organization/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-10
**Summary**: Support Organization _includes
**Description**: "A Server **SHALL** be capable of supporting the following _includes: Organization:partof - `GET [base]/Organization?[parameter=value]&_include=Organization:partof` Organization:endpoint - `GET [base]/Organization?[parameter=value]&_include=Organization:endpoint` Organization:coverage-area - `GET [base]/Organization?[parameter=value]&_include=Organization:coverage-area`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria
---
---
# REQ-SERVER-SHALL-11
**Summary**: Support Organization _revincludes
**Description**: "A Server **SHALL** be capable of supporting the following _revincludes: Endpoint:organization - `GET [base]/Organization?[parameter=value]&_revinclude=Endpoint:organization` HealthcareService:organization - `GET [base]/Organization?[parameter=value]&_revinclude=HealthcareService:organization` InsurancePlan:administered-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:administered-by` InsurancePlan:owned-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:owned-by` OrganizationAffiliation:primary-organization - `GET [base]/Organization?[parameter=value]&_revinclude=Organization