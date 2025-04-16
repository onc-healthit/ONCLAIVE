---
# REQ-01
**Summary**: Prohibit requirement of consumer identifying information for Plan-Net service access.
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations

---
# REQ-02
**Summary**: Prohibit Plan-Net service from requiring consumer identifying information from directory mobile applications.
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations

---
# REQ-03
**Summary**: Prohibit directory mobile applications from sending consumer identifiable information when querying Plan-Net services.
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Test
**Actor**: Directory Mobile Application
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations

---
# REQ-04
**Summary**: Mandate Health Plan API actors to populate all Must Support data elements for query results.
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

---
# REQ-05
**Summary**: Mandate Health Plan API actors to omit data elements with minimum cardinality 0 when information is not present. 
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: True (Minimum cardinality of data element must be 0)
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

---
# REQ-06
**Summary**: Mandate Health Plan API actors to provide reason for missing information for Must Support data elements with minimum cardinality greater than 0.
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: True (Minimum cardinality of data element must be > 0)
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

---
# REQ-07
**Summary**: Mandate Application actors to process resource instances containing Must Support data elements without errors.
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements

---
# REQ-08
**Summary**: Recommend Application actors to display or store data elements for human use or other purposes.
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Actor**: Application
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements

---
# REQ-09
**Summary**: Mandate Application actors to interpret missing Must Support data elements as not present in the Health Plan API system.
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements

---
# REQ-10
**Summary**: Mandate Consumer App actors to process resource instances containing Must Support data elements asserting missing information. 
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Actor**: Consumer App
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements

---
# REQ-11
**Summary**: Mandate profiles to include lastUpdate timestamp.
**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Client Detection of Updates Directory Content

---
# REQ-12
**Summary**: Organizations shall define HealthcareServices for service search.
**Description**: "All organizations that provide service should define an appropriate set of HealthcareServices to facilitate search."
**Verification**: Inspection
**Actor**: Organization
**Conformance**: SHALL 
**Source**: HealthcareService Section

---
# REQ-13
**Summary**: PractitionerRole/OrganizationAffiliation shall link to Networks.
**Description**: "Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively."
**Verification**: Inspection
**Actor**: System
**Conformance**: SHALL
**Source**: Insurance Plan and Network Section

---
# REQ-14
**Summary**: PractitionerRole/OrganizationAffiliation shall link Practitioners/Organizations to HealthcareServices, Organizations, Networks, and Locations.
**Description**: "PractitionerRole and OrganizationAffiliation instances are what tie Practitioners and Organizations to HealthcareServices, Organizations, Networks and Locations."
**Verification**: Inspection
**Actor**: System
**Conformance**: SHALL
**Source**: Insurance Plan and Network Section

---
# REQ-15
**Summary**: Location instances shall include contact information, address, accessibility, hours of operation, contact, and position.
**Description**: "Location instances provide information about location where service is provided, including contact information, address, accessibility, hours of operation and contact, as well as position (lattitude and longitude)."
**Verification**: Inspection
**Actor**: System
**Conformance**: SHALL
**Source**: Location Section

---
# REQ-16
**Summary**: Location instances may represent regions using associated or attached GeoJSON.
**Description**: "Locations can also be used to represent regions using an associated or attached GeoJSON object."
**Verification**: Inspection
**Actor**: System
**Conformance**: MAY
**Source**: Location Section 

---
# REQ-17
**Summary**: Support all defined profiles
**Description**: "The Plan-Net Server **SHALL**:
1. Support all profiles defined in this Implementation Guide."
**Verification**: Inspection
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

---
# REQ-18
**Summary**: Implement FHIR-compliant RESTful behavior
**Description**: "The Plan-Net Server **SHALL**:
2. Implement the RESTful behavior according to the FHIR specification."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

---
# REQ-19
**Summary**: Return specific response classes
**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 400): invalid parameter
* (Status 401/4xx): unauthorized request
* (Status 403): insufficient scope
* (Status 404): unknown resource
* (Status 410): deleted resource."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

---
# REQ-20
**Summary**: Support JSON source format
**Description**: "The Plan-Net Server **SHALL**:
4. Support json source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

---
# REQ-21
**Summary**: Identify supported Plan-Net profiles in metadata
**Description**: "The Plan-Net Server **SHALL**:
5. Identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance."
**Verification**: Inspection
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

---
# REQ-22
**Summary**: Support searchParameters individually and combined
**Description**: "The Plan-Net Server **SHALL**:
6. Support the searchParameters on each profile individually and in combination."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

---
# REQ-23
**Summary**: Support forward and reverse chaining for chained search parameters
**Description**: "The Plan-Net Server **SHALL**:
1.Support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

---
# REQ-24
**Summary**: Support XML source format
**Description**: "The Plan-Net Server **SHOULD**:
1. Support xml source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, FHIR RESTful Capabilities

---
# REQ-25
**Summary**: Reject unauthorized requests with HTTP 401
**Description**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: CapabilityStatement: Plan-Net CapabilityStatement, Security

---
# REQ-26
**Summary**: Support Endpoint search-type and read interactions
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Profile Interaction Summary

---
# REQ-27
**Summary**: Support Endpoint vread interaction
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Endpoint - Profile Interaction Summary

---
# REQ-28
**Summary**: Return Endpoint resource using ID
**Description**: "A Server SHALL be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria

---
# REQ-29
**Summary**: Return Endpoint resource using ID and version ID
**Description**: "A Server SHOULD be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria

---
# REQ-30
**Summary**: Support Endpoint _include for organization
**Description**: "A Server SHALL be capable of supporting the following _includes: Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Fetch and Search Criteria

---
# REQ-31
**Summary**: Support Endpoint search by organization
**Description**: "SHALL [organization](SearchParameter-endpoint-organization.html) reference `GET [base]/Endpoint?organization=[organization]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Search Parameter Summary

---
# REQ-32
**Summary**: Support Endpoint search by _id
**Description**: "SHALL [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/Endpoint?_id=[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Search Parameter Summary

---
# REQ-33
**Summary**: Support Endpoint search by _lastUpdated
**Description**: "SHALL [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/Endpoint?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Endpoint - Search Parameter Summary

---
# REQ-34
**Summary**: Support HealthcareService search-type and read interactions
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Profile Interaction Summary

---
# REQ-35
**Summary**: Support HealthcareService vread interaction
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService - Profile Interaction Summary

---
# REQ-36
**Summary**: Return HealthcareService resource using ID
**Description**: "A Server SHALL be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria

---
# REQ-37
**Summary**: Return HealthcareService resource using ID and version ID
**Description**: "A Server SHOULD be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria

---
# REQ-38
**Summary**: Support HealthcareService _includes for location, coverage-area, organization, endpoint
**Description**: "A Server SHALL be capable of supporting the following _includes: 
HealthcareService:location - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:location`
HealthcareService:coverage-area - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:coverage-area`
HealthcareService:organization - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:organization`
HealthcareService:endpoint - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:endpoint`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria

---
# REQ-39
**Summary**: Support HealthcareService _revincludes for PractitionerRole:service and OrganizationAffiliation:service
**Description**: "A Server SHALL be capable of supporting the following _revincludes:
PractitionerRole:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=PractitionerRole:service`
OrganizationAffiliation:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=OrganizationAffiliation:service`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Fetch and Search Criteria

---
# REQ-40
**Summary**: Support HealthcareService search by location
**Description**: "SHALL [location](SearchParameter-healthcareservice-location.html) reference `GET [base]/HealthcareService?location=[location]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-41
**Summary**: Support HealthcareService search by coverage-area
**Description**: "SHALL [coverage-area](SearchParameter-healthcareservice-coverage-area.html) reference `GET [base]/HealthcareService?coverage-area=[coverage-area]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-42
**Summary**: Support HealthcareService search by organization
**Description**: "SHALL [organization](SearchParameter-healthcareservice-organization.html) reference `GET [base]/HealthcareService?organization=[organization]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-43
**Summary**: Support HealthcareService search by endpoint
**Description**: "SHALL [endpoint](SearchParameter-healthcareservice-endpoint.html) reference `GET [base]/HealthcareService?endpoint=[endpoint]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-44
**Summary**: Support HealthcareService search by name
**Description**: "SHALL [name](SearchParameter-healthcareservice-name.html) string `GET [base]/HealthcareService?name=[name]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-45
**Summary**: Support HealthcareService search by service-category
**Description**: "SHALL [service-category](SearchParameter-healthcareservice-service-category.html) token `GET [base]/HealthcareService?service-category=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-46
**Summary**: Support HealthcareService search by service-type
**Description**: "SHALL [service-type](SearchParameter-healthcareservice-service-type.html) token `GET [base]/HealthcareService?service-type=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-47
**Summary**: Support HealthcareService search by specialty
**Description**: "SHALL [specialty](SearchParameter-healthcareservice-specialty.html) token `GET [base]/HealthcareService?specialty=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-48
**Summary**: Support HealthcareService search by _id
**Description**: "SHALL [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/HealthcareService?_id=[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-49
**Summary**: Support HealthcareService search by _lastUpdated
**Description**: "SHALL [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/HealthcareService?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService - Search Parameter Summary

---
# REQ-50
**Summary**: Support InsurancePlan search-type and read interactions
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Profile Interaction Summary

---
# REQ-51
**Summary**: Support InsurancePlan vread interaction
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: InsurancePlan - Profile Interaction Summary

---
# REQ-52
**Summary**: Return InsurancePlan resource using ID
**Description**: "A Server SHALL be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Fetch and Search Criteria

---
# REQ-53
**Summary**: Return InsurancePlan resource using ID and version ID
**Description**: "A Server SHOULD be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: InsurancePlan - Fetch and Search Criteria

---
# REQ-54
**Summary**: Support InsurancePlan _includes for administered-by, owned-by, coverage-area
**Description**: "A Server SHALL be capable of supporting the following _includes:
InsurancePlan:administered-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:administered-by`
InsurancePlan:owned-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:owned-by`
InsurancePlan:coverage-area - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:coverage-area`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Fetch and Search Criteria

---
# REQ-55
**Summary**: Support InsurancePlan search by administered-by
**Description**: "SHALL [administered-by](SearchParameter-insuranceplan-administered-by.html) reference `GET [base]/InsurancePlan?administered-by=[administered-by]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-56
**Summary**: Support InsurancePlan search by owned-by
**Description**: "SHALL [owned-by](SearchParameter-insuranceplan-owned-by.html) reference `GET [base]/InsurancePlan?owned-by=[owned-by]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-57
**Summary**: Support InsurancePlan search by coverage-area
**Description**: "SHALL [coverage-area](SearchParameter-insuranceplan-coverage-area.html) reference `GET [base]/InsurancePlan?coverage-area=[coverage-area]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-58
**Summary**: Support InsurancePlan search by name
**Description**: "SHALL [name](SearchParameter-insuranceplan-name.html) string `GET [base]/InsurancePlan?name=[name]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-59
**Summary**: Support InsurancePlan search by plan-type
**Description**: "SHALL [plan-type](SearchParameter-insuranceplan-plan-type.html) token `GET [base]/InsurancePlan?plan-type=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-60
**Summary**: Support InsurancePlan search by identifier
**Description**: "SHALL [identifier](SearchParameter-insuranceplan-identifier.html) token `GET [base]/InsurancePlan?identifier=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-61
**Summary**: Support InsurancePlan search by _id
**Description**: "SHALL [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/InsurancePlan?_id=[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-62
**Summary**: Support InsurancePlan search by _lastUpdated
**Description**: "SHALL [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/InsurancePlan?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-63
**Summary**: Support InsurancePlan search by type
**Description**: "SHALL [type](SearchParameter-insuranceplan-type.html) token `GET [base]/InsurancePlan?type=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: InsurancePlan - Search Parameter Summary

---
# REQ-64
**Summary**: Support Plan-Net Location profile
**Description**: "Supported Profiles: [Plan-Net Location](StructureDefinition-plannet-Location.html)"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section

---
# REQ-65
**Summary**: Resolve Location resource references
**Description**: "Reference Policy: `resolves`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section

---
# REQ-66
**Summary**: Support Location search-type and read interactions
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Profile Interaction Summary

---
# REQ-67
**Summary**: Support Location vread interaction
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Location Section, Profile Interaction Summary

---
# REQ-68
**Summary**: Return Location resource by ID
**Description**: "A Server SHALL be capable of returning a Location resource using: `GET [base]/Location/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-69
**Summary**: Return Location resource history by version ID
**Description**: "A Server SHOULD be capable of returning a Location resource using: `GET [base]/Location/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-70
**Summary**: Support Location _include for endpoint
**Description**: "A Server SHALL be capable of supporting the following _includes: Location:endpoint - `GET [base]/Location?[parameter=value]&_include=Location:endpoint`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-71
**Summary**: Support Location _include for organization
**Description**: "A Server SHALL be capable of supporting the following _includes: Location:organization - `GET [base]/Location?[parameter=value]&_include=Location:organization`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-72
**Summary**: Support Location _include for partof
**Description**: "A Server SHALL be capable of supporting the following _includes: Location:partof - `GET [base]/Location?[parameter=value]&_include=Location:partof`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-73
**Summary**: Support Location _revinclude for HealthcareService:location
**Description**: "A Server SHALL be capable of supporting the following _revincludes: HealthcareService:location - `GET [base]/Location?[parameter=value]&_revinclude=HealthcareService:location`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-74
**Summary**: Support Location _revinclude for InsurancePlan:coverage-area
**Description**: "A Server SHALL be capable of supporting the following _revincludes: InsurancePlan:coverage-area - `GET [base]/Location?[parameter=value]&_revinclude=InsurancePlan:coverage-area`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-75
**Summary**: Support Location _revinclude for OrganizationAffiliation:location
**Description**: "A Server SHALL be capable of supporting the following _revincludes: OrganizationAffiliation:location - `GET [base]/Location?[parameter=value]&_revinclude=OrganizationAffiliation:location`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-76
**Summary**: Support Location _revinclude for PractitionerRole:location
**Description**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:location - `GET [base]/Location?[parameter=value]&_revinclude=PractitionerRole:location`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Fetch and Search Criteria

---
# REQ-77
**Summary**: Support Location search by partof
**Description**: "SHALL [partof](SearchParameter-location-partof.html) reference `GET [base]/Location?partof=[partof]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-78
**Summary**: Support Location search by organization
**Description**: "SHALL [organization](SearchParameter-location-organization.html) reference `GET [base]/Location?organization=[organization]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-79
**Summary**: Support Location search by endpoint
**Description**: "SHALL [endpoint](SearchParameter-location-endpoint.html) reference `GET [base]/Location?endpoint=[endpoint]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-80
**Summary**: Support Location search by address-city
**Description**: "SHALL [address-city](SearchParameter-location-address-city.html) string `GET [base]/Location?address-city=[address-city]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-81
**Summary**: Support Location search by address-state
**Description**: "SHALL [address-state](SearchParameter-location-address-state.html) string `GET [base]/Location?address-state=[address-state]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-82
**Summary**: Support Location search by address-postalcode
**Description**: "SHALL [address-postalcode](SearchParameter-location-address-postalcode.html) string `GET [base]/Location?address-postalcode=[address-postalcode]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-83
**Summary**: Support Location search by address
**Description**: "SHALL [address](SearchParameter-location-address.html) string `GET [base]/Location?address=[address]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-84
**Summary**: Support Location search by type
**Description**: "SHALL [type](SearchParameter-location-type.html) token `GET [base]/Location?type=[system] [code]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-85
**Summary**: Support Location search by _id
**Description**: "SHALL [_id](http://hl7.org/fhir/R4/search.html) token `GET [base]/Location?_id=[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-86
**Summary**: Support Location search by _lastUpdated
**Description**: "SHALL [_lastUpdated](http://hl7.org/fhir/R4/search.html) date `GET [base]/Location?_lastUpdated=[_lastUpdated]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Location Section, Search Parameter Summary

---
# REQ-87
**Summary**: Support Plan-Net Network and Organization profiles
**Description**: "Supported Profiles: [Plan-Net Network](StructureDefinition-plannet-Network.html), [Plan-Net Organization](StructureDefinition-plannet-Organization.html)"
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section

---
# REQ-88
**Summary**: Resolve Organization resource references
**Description**: "Reference Policy: `resolves`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section

---
# REQ-89
**Summary**: Support Organization search-type and read interactions
**Description**: "SHALL support `search-type`, `read`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Profile Interaction Summary

---
# REQ-90
**Summary**: Support Organization vread interaction
**Description**: "SHOULD support `vread`."
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Organization Section, Profile Interaction Summary

---
# REQ-91
**Summary**: Return Organization resource by ID
**Description**: "A Server SHALL be capable of returning a Organization resource using: `GET [base]/Organization/[id]`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria

---
# REQ-92
**Summary**: Return Organization resource history by version ID
**Description**: "A Server SHOULD be capable of returning a Organization resource using: `GET [base]/Organization/[id]/_history/vid`"
**Verification**: Test
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Organization Section, Fetch and Search Criteria

---
# REQ-93
**Summary**: Support Organization _include for partof
**Description**: "A Server SHALL be capable of supporting the following _includes: Organization:par