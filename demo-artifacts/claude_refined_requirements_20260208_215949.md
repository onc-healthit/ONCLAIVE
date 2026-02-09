# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.

I have carefully analyzed all the provided FHIR Implementation Guide text chunks. Based on my review, here are the testable requirements extracted from the content:

---
# REQ-001
**ID**: 01
**Summary**: Conformance to Da Vinci HRex Security Guidelines
**Requirement**: "Users of this implementation guide **SHALL** conform to the Da Vinci HRex guidelines on privacy, safety, and security."
**Context**: This requirement establishes that all implementers of the Plan-Net Implementation Guide must adhere to the security, privacy, and safety guidelines specified in the Da Vinci HRex Implementation Guide (STU1.1). This creates a dependency on the HRex security framework and ensures consistent security practices across Da Vinci implementation guides.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: Da Vinci HRex STU1.1 Security Requirements
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Attestation
**Section**: 10 Security
**Grouping**: Security

---
# REQ-002
**ID**: 02
**Summary**: Conformance to HRex Conformance Expectations
**Requirement**: "All systems claiming conformance to this guide SHALL conform to the requirements listed in [the Health Record Exchange (Hrex) Conformance Expectations] section."
**Context**: This requirement establishes that all systems implementing the Plan-Net IG must also meet the conformance expectations defined in the Da Vinci HRex IG. This creates a dependency on the HRex conformance requirements and ensures consistency across Da Vinci implementation guides.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: HRex Conformance Expectations (external reference)
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Attestation
**Section**: 4.1 Conformance Expectations
**Grouping**: General/Cross-Resource

---
# REQ-003
**ID**: 03
**Summary**: Server CapabilityStatement Requirements
**Requirement**: "Server systems claiming conformance to this guide SHALL meet the capability statement expectation requirements identified in the [Plan-Net CapabilityStatement](CapabilityStatement-plan-net.html) and SHALL have a CapabilityStatement that has a CapabilityStatement.instantiates with a URL of http://hl7.org/fhir/us/davinci-drug-formulary/CapabilityStatement/usdf-server or a URL to the appropriate version of the CapabilityStatement."
**Context**: Server systems must publish a CapabilityStatement resource that demonstrates conformance to the Plan-Net capabilities and includes a specific instantiates URL. This allows clients to verify server capabilities programmatically.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 4.1 Conformance Expectations
**Grouping**: Capability Statement

---
# REQ-004
**ID**: 04
**Summary**: Health Plan API Must Support - Population of Data Elements
**Requirement**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."
**Context**: When responding to queries, Health Plan API servers must be able to populate all data elements marked as Must Support in the Plan-Net profiles. This ensures that required data is available when present in the system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.1 Health Plan API Requirements
**Grouping**: General/Cross-Resource

---
# REQ-005
**ID**: 05
**Summary**: Health Plan API Must Support - Omission of Missing Data (Cardinality 0)
**Requirement**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors SHALL NOT include the data elements in the resource instance returned as part of the query results."
**Context**: When a Must Support element with minimum cardinality of 0 has no data available, servers must omit the element entirely from the response rather than including it with a null or empty value.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when information on a particular Must Support data element is not present and the minimum cardinality is 0
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.1 Health Plan API Requirements
**Grouping**: General/Cross-Resource

---
# REQ-006
**ID**: 06
**Summary**: Health Plan API Must Support - Handling Missing Required Data (Cardinality >0)
**Requirement**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 [the Health Plan API actor] SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Context**: When a Must Support element with minimum cardinality greater than 0 has no data available, servers must include the element and provide a reason for the absence using appropriate codes or the dataAbsentReason extension. This ensures required elements are always present even when data is unavailable.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when information on a particular data element is not present and the minimum cardinality is >0
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.1 Health Plan API Requirements
**Grouping**: General/Cross-Resource

---
# REQ-007
**ID**: 07
**Summary**: Application Actor Must Support - Processing Without Error
**Requirement**: "Application actors SHALL be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Context**: Client applications must be able to successfully parse and process all Must Support data elements in responses from Plan-Net servers without application failures or errors. This ensures robust client implementations.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.2 Application Requirements
**Grouping**: General/Cross-Resource

---
# REQ-008
**ID**: 08
**Summary**: Application Actor Must Support - Display or Storage
**Requirement**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."
**Context**: While not mandatory, client applications should have the ability to either present Must Support data elements to users or persist them for future use. This recommendation supports meaningful use of the data.
**Conformance**: SHOULD
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Attestation
**Section**: 4.2.2 Application Requirements
**Grouping**: General/Cross-Resource

---
# REQ-009
**ID**: 09
**Summary**: Application Actor Must Support - Interpretation of Missing Data
**Requirement**: "When querying Health Plan API actors, Application actors SHALL interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Context**: Client applications must understand that when a Must Support element is absent from a response (where cardinality permits), it indicates the data is not available in the server system, not that there was an error or the element was overlooked.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when querying Health Plan API actors
**Verifiable**: Yes
**Verifiability Details**: Attestation
**Section**: 4.2.2 Application Requirements
**Grouping**: General/Cross-Resource

---
# REQ-010
**ID**: 10
**Summary**: Application Actor Must Support - Processing Missing Information Assertions
**Requirement**: "Consumer App actors SHALL be able to process resource instances containing Must Support data elements asserting missing information."
**Context**: Client applications must be able to handle Must Support elements that explicitly indicate missing data (e.g., through dataAbsentReason or null flavors) without errors. This complements the requirement for handling absent elements.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 4.2.2 Application Requirements
**Grouping**: General/Cross-Resource

---
# REQ-011
**ID**: 11
**Summary**: Plan-Net service SHALL NOT require consumer identifying information
**Requirement**: "A conformant Plan-Net service SHALL NOT require a directory mobile application to send consumer identifying information in order to query content."
**Context**: This requirement addresses privacy considerations for the Plan-Net service. The service must be accessible without authentication and must not collect consumer identifying information during queries. This protects consumer privacy by ensuring anonymous access to directory information.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 7.1.2 Privacy Considerations
**Grouping**: Privacy

---
# REQ-012
**ID**: 12
**Summary**: Directory mobile application SHALL NOT send consumer identifiable information
**Requirement**: "A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service."
**Context**: This requirement constrains the behavior of client applications that query the Plan-Net service. Applications must not transmit any information that could identify individual consumers when making queries to the directory service. This is a complementary privacy protection to REQ-11, ensuring privacy from the client side.
**Conformance**: SHALL NOT
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 7.1.2 Privacy Considerations
**Grouping**: Privacy

---
# REQ-013
**ID**: 13
**Summary**: Server MAY support Bulk Data IG
**Requirement**: "A server MAY support [Bulk Data IG](http://hl7.org/fhir/uv/bulkdata/index.html) for the retrieval of directory data."
**Context**: This requirement allows but does not mandate servers to implement the Bulk Data IG for retrieving directory information. The bulk data guidance is noted as draft-only and has not been fully tested. Support for bulk data operations is optional for conformant Plan-Net servers.
**Conformance**: MAY
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 7.3 Bulk Data
**Grouping**: Capability Statement

---
# REQ-014
**ID**: 14
**Summary**: Plan-Net Server SHALL support all profiles defined in Implementation Guide
**Requirement**: "The Plan-Net Server SHALL: Support all profiles defined in this Implementation Guide."
**Context**: This requirement establishes that a Plan-Net Server must implement support for every profile specified within the DaVinci PDEX Plan-Net Implementation Guide to be conformant.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement

---
# REQ-015
**ID**: 15
**Summary**: Plan-Net Server SHALL implement RESTful behavior according to FHIR specification
**Requirement**: "The Plan-Net Server SHALL: Implement the RESTful behavior according to the FHIR specification."
**Context**: This requirement mandates that the server's RESTful API operations must conform to the FHIR specification standards for RESTful interactions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement

---
# REQ-016
**ID**: 16
**Summary**: Plan-Net Server SHALL return specified HTTP response classes
**Requirement**: "The Plan-Net Server SHALL: Return the following response classes: (Status 400): invalid parameter; (Status 401/4xx): unauthorized request; (Status 403): insufficient scope; (Status 404): unknown resource; (Status 410): deleted resource."
**Context**: This requirement specifies the HTTP status codes that must be returned by the server for various error conditions to ensure standardized error handling.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement

---
# REQ-017
**ID**: 17
**Summary**: Plan-Net Server SHALL support json source formats
**Requirement**: "The Plan-Net Server SHALL: Support json source formats for all Plan-Net interactions."
**Context**: This requirement mandates that the server must be capable of accepting and returning JSON formatted FHIR resources for all interactions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement

---
# REQ-018
**ID**: 18
**Summary**: Plan-Net Server SHALL support searchParameters individually and in combination
**Requirement**: "The Plan-Net Server SHALL: Support the searchParameters on each profile individually and in combination."
**Context**: This requirement establishes that the server must support both individual search parameters and combinations of search parameters for querying resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement

---
# REQ-019
**ID**: 19
**Summary**: Plan-Net Server SHALL support forward and reverse chaining
**Requirement**: "The Plan-Net Server SHALL: Support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Context**: This requirement mandates support for chained searches, allowing clients to search across resource references in both forward and reverse directions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement

---
# REQ-020
**ID**: 20
**Summary**: Plan-Net Server SHOULD support xml source formats
**Requirement**: "The Plan-Net Server SHOULD: Support xml source formats for all Plan-Net interactions."
**Context**: This is a recommended capability for the server to accept and return XML formatted FHIR resources for all interactions.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement

---
# REQ-021
**ID**: 21
**Summary**: Plan-Net Server SHALL reject unauthorized requests with HTTP 401
**Requirement**: "A server SHALL reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Context**: This security requirement mandates that servers must return an HTTP 401 status code when rejecting requests that lack proper authorization credentials.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Security

---
# REQ-022
**ID**: 22
**Summary**: Server SHALL support search-type and read interactions for Endpoint
**Requirement**: "[Server] SHALL support `search-type`, `read` [for Endpoint resource]"
**Context**: This requirement mandates that the server must support both search-type operations to query for Endpoint resources and read operations to retrieve specific Endpoint resources by ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-023
**ID**: 23
**Summary**: Server SHOULD support vread interaction for Endpoint
**Requirement**: "[Server] SHOULD support `vread` [for Endpoint resource]"
**Context**: This is a recommended capability for the server to support version-specific read operations on Endpoint resources.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-024
**ID**: 24
**Summary**: Server SHALL support read by ID for Endpoint
**Requirement**: "A Server SHALL be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]`"
**Context**: This requirement mandates that the server must support retrieval of a specific Endpoint resource by its logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-025
**ID**: 25
**Summary**: Server SHOULD support vread for Endpoint
**Requirement**: "A Server SHOULD be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]/_history/vid`"
**Context**: This is a recommended capability for the server to support retrieval of a specific version of an Endpoint resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-026
**ID**: 26
**Summary**: Server SHALL support _include for Endpoint:organization
**Requirement**: "A Server SHALL be capable of supporting the following _includes: Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Context**: This requirement mandates that the server must support the _include parameter to return Organization resources referenced by Endpoint resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-027
**ID**: 27
**Summary**: Server SHALL support search parameters for Endpoint
**Requirement**: "[Server] SHALL [support search by] organization [reference] `GET [base]/Endpoint?organization=[organization]`; _id [token] `GET [base]/Endpoint?_id=[id]`; _lastUpdated [date] `GET [base]/Endpoint?_lastUpdated=[_lastUpdated]`"
**Context**: This requirement mandates that the server must support searching Endpoint resources by organization reference, _id token, and _lastUpdated date parameters.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-028
**ID**: 28
**Summary**: Server SHALL support search-type and read interactions for HealthcareService
**Requirement**: "[Server] SHALL support `search-type`, `read` [for HealthcareService resource]"
**Context**: This requirement mandates that the server must support both search-type operations to query for HealthcareService resources and read operations to retrieve specific HealthcareService resources by ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: General/Cross-Resource

---
# REQ-029
**ID**: 29
**Summary**: Server SHOULD support vread interaction for HealthcareService
**Requirement**: "[Server] SHOULD support `vread` [for HealthcareService resource]"
**Context**: This is a recommended capability for the server to support version-specific read operations on HealthcareService resources.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: General/Cross-Resource

---
# REQ-030
**ID**: 30
**Summary**: Server SHALL support read by ID for HealthcareService
**Requirement**: "A Server SHALL be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]`"
**Context**: This requirement mandates that the server must support retrieval of a specific HealthcareService resource by its logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: General/Cross-Resource

---
# REQ-031
**ID**: 31
**Summary**: Server SHOULD support vread for HealthcareService
**Requirement**: "A Server SHOULD be capable of returning a HealthcareService resource using: `GET [base]/HealthcareService/[id]/_history/vid`"
**Context**: This is a recommended capability for the server to support retrieval of a specific version of a HealthcareService resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: General/Cross-Resource

---
# REQ-032
**ID**: 32
**Summary**: Server SHALL support _includes for HealthcareService
**Requirement**: "A Server SHALL be capable of supporting the following _includes: HealthcareService:location - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:location`; HealthcareService:coverage-area - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:coverage-area`; HealthcareService:organization - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:organization`; HealthcareService:endpoint - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:endpoint`"
**Context**: This requirement mandates that the server must support the _include parameter to return Location, coverage-area, Organization, and Endpoint resources referenced by HealthcareService resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: General/Cross-Resource

---
# REQ-033
**ID**: 33
**Summary**: Server SHALL support _revincludes for HealthcareService
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=PractitionerRole:service`; OrganizationAffiliation:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=OrganizationAffiliation:service`"
**Context**: This requirement mandates that the server must support the _revinclude parameter to return PractitionerRole and OrganizationAffiliation resources that reference the HealthcareService resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: General/Cross-Resource

---
# REQ-034
**ID**: 34
**Summary**: Server SHALL support search parameters for HealthcareService
**Requirement**: "[Server] SHALL [support search by] location [reference] `GET [base]/HealthcareService?location=[location]`; coverage-area [reference] `GET [base]/HealthcareService?coverage-area=[coverage-area]`; organization [reference] `GET [base]/HealthcareService?organization=[organization]`; endpoint [reference] `GET [base]/HealthcareService?endpoint=[endpoint]`; name [string] `GET [base]/HealthcareService?name=[name]`; service-category [token] `GET [base]/HealthcareService?service-category=[system] [code]`; service-type [token] `GET [base]/HealthcareService?service-type=[system] [code]`; specialty [token] `GET [base]/HealthcareService?specialty=[system] [code]`; _id [token] `GET [base]/HealthcareService?_id=[id]`; _lastUpdated [date] `GET [base]/HealthcareService?_lastUpdated=[_lastUpdated]`"
**Context**: This requirement mandates that the server must support searching HealthcareService resources by location, coverage-area, organization, endpoint, name, service-category, service-type, specialty, _id, and _lastUpdated parameters.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.2 HealthcareService
**Grouping**: General/Cross-Resource

---
# REQ-035
**ID**: 35
**Summary**: Server SHALL support search-type and read interactions for InsurancePlan
**Requirement**: "[Server] SHALL support `search-type`, `read` [for InsurancePlan resource]"
**Context**: This requirement mandates that the server must support both search-type operations to query for InsurancePlan resources and read operations to retrieve specific InsurancePlan resources by ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: Coverage

---
# REQ-036
**ID**: 36
**Summary**: Server SHOULD support vread interaction for InsurancePlan
**Requirement**: "[Server] SHOULD support `vread` [for InsurancePlan resource]"
**Context**: This is a recommended capability for the server to support version-specific read operations on InsurancePlan resources.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: Coverage

---
# REQ-037
**ID**: 37
**Summary**: Server SHALL support read by ID for InsurancePlan
**Requirement**: "A Server SHALL be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]`"
**Context**: This requirement mandates that the server must support retrieval of a specific InsurancePlan resource by its logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: Coverage

---
# REQ-038
**ID**: 38
**Summary**: Server SHOULD support vread for InsurancePlan
**Requirement**: "A Server SHOULD be capable of returning a InsurancePlan resource using: `GET [base]/InsurancePlan/[id]/_history/vid`"
**Context**: This is a recommended capability for the server to support retrieval of a specific version of an InsurancePlan resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: Coverage

---
# REQ-039
**ID**: 39
**Summary**: Server SHALL support _includes for InsurancePlan
**Requirement**: "A Server SHALL be capable of supporting the following _includes: InsurancePlan:administered-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:administered-by`; InsurancePlan:owned-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:owned-by`; InsurancePlan:coverage-area - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:coverage-area`"
**Context**: This requirement mandates that the server must support the _include parameter to return administered-by, owned-by, and coverage-area resources referenced by InsurancePlan resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: Coverage

---
# REQ-040
**ID**: 40
**Summary**: Server SHALL support search parameters for InsurancePlan
**Requirement**: "[Server] SHALL [support search by] administered-by [reference] `GET [base]/InsurancePlan?administered-by=[administered-by]`; owned-by [reference] `GET [base]/InsurancePlan?owned-by=[owned-by]`; coverage-area [reference] `GET [base]/InsurancePlan?coverage-area=[coverage-area]`; name [string] `GET [base]/InsurancePlan?name=[name]`; plan-type [token] `GET [base]/InsurancePlan?plan-type=[system] [code]`; identifier [token] `GET [base]/InsurancePlan?identifier=[system] [code]`; _id [token] `GET [base]/InsurancePlan?_id=[id]`; _lastUpdated [date] `GET [base]/InsurancePlan?_lastUpdated=[_lastUpdated]`; type [token] `GET [base]/InsurancePlan?type=[system] [code]`"
**Context**: This requirement mandates that the server must support searching InsurancePlan resources by administered-by, owned-by, coverage-area, name, plan-type, identifier, _id, _lastUpdated, and type parameters.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.3 InsurancePlan
**Grouping**: Coverage

---
# REQ-041
**ID**: 41
**Summary**: Server SHALL support search-type and read interactions for Location
**Requirement**: "[Server] SHALL support `search-type`, `read` [for Location resource]"
**Context**: This requirement mandates that the server must support both search-type operations to query for Location resources and read operations to retrieve specific Location resources by ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.4 Location
**Grouping**: Location

---
# REQ-042
**ID**: 42
**Summary**: Server SHOULD support vread interaction for Location
**Requirement**: "[Server] SHOULD support `vread` [for Location resource]"
**Context**: This is a recommended capability for the server to support version-specific read operations on Location resources.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.4 Location
**Grouping**: Location

---
# REQ-043
**ID**: 43
**Summary**: Server SHALL support read by ID for Location
**Requirement**: "A Server SHALL be capable of returning a Location resource using: `GET [base]/Location/[id]`"
**Context**: This requirement mandates that the server must support retrieval of a specific Location resource by its logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.4 Location
**Grouping**: Location

---
# REQ-044
**ID**: 44
**Summary**: Server SHOULD support vread for Location
**Requirement**: "A Server SHOULD be capable of returning a Location resource using: `GET [base]/Location/[id]/_history/vid`"
**Context**: This is a recommended capability for the server to support retrieval of a specific version of a Location resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.4 Location
**Grouping**: Location

---
# REQ-045
**ID**: 45
**Summary**: Server SHALL support _includes for Location
**Requirement**: "A Server SHALL be capable of supporting the following _includes: Location:endpoint - `GET [base]/Location?[parameter=value]&_include=Location:endpoint`; Location:organization - `GET [base]/Location?[parameter=value]&_include=Location:organization`; Location:partof - `GET [base]/Location?[parameter=value]&_include=Location:partof`"
**Context**: This requirement mandates that the server must support the _include parameter to return endpoint, organization, and partof resources referenced by Location resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.4 Location
**Grouping**: Location

---
# REQ-046
**ID**: 46
**Summary**: Server SHALL support _revincludes for Location
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: HealthcareService:location - `GET [base]/Location?[parameter=value]&_revinclude=HealthcareService:location`; InsurancePlan:coverage-area - `GET [base]/Location?[parameter=value]&_revinclude=InsurancePlan:coverage-area`; OrganizationAffiliation:location - `GET [base]/Location?[parameter=value]&_revinclude=OrganizationAffiliation:location`; PractitionerRole:location - `GET [base]/Location?[parameter=value]&_revinclude=PractitionerRole:location`"
**Context**: This requirement mandates that the server must support the _revinclude parameter to return HealthcareService, InsurancePlan, OrganizationAffiliation, and PractitionerRole resources that reference the Location resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.4 Location
**Grouping**: Location

---
# REQ-047
**ID**: 47
**Summary**: Server SHALL support search parameters for Location
**Requirement**: "[Server] SHALL [support search by] partof [reference] `GET [base]/Location?partof=[partof]`; organization [reference] `GET [base]/Location?organization=[organization]`; endpoint [reference] `GET [base]/Location?endpoint=[endpoint]`; address-city [string] `GET [base]/Location?address-city=[address-city]`; address-state [string] `GET [base]/Location?address-state=[address-state]`; address-postalcode [string] `GET [base]/Location?address-postalcode=[address-postalcode]`; address [string] `GET [base]/Location?address=[address]`; type [token] `GET [base]/Location?type=[system] [code]`; _id [token] `GET [base]/Location?_id=[id]`; _lastUpdated [date] `GET [base]/Location?_lastUpdated=[_lastUpdated]`"
**Context**: This requirement mandates that the server must support searching Location resources by partof, organization, endpoint, address-city, address-state, address-postalcode, address, type, _id, and _lastUpdated parameters.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.4 Location
**Grouping**: Location

---
# REQ-048
**ID**: 48
**Summary**: Server SHALL support search-type and read interactions for Organization
**Requirement**: "[Server] SHALL support `search-type`, `read` [for Organization resource]"
**Context**: This requirement mandates that the server must support both search-type operations to query for Organization resources and read operations to retrieve specific Organization resources by ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---
# REQ-049
**ID**: 49
**Summary**: Server SHOULD support vread interaction for Organization
**Requirement**: "[Server] SHOULD support `vread` [for Organization resource]"
**Context**: This is a recommended capability for the server to support version-specific read operations on Organization resources.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---
# REQ-050
**ID**: 50
**Summary**: Server SHALL support read by ID for Organization
**Requirement**: "A Server SHALL be capable of returning a Organization resource using: `GET [base]/Organization/[id]`"
**Context**: This requirement mandates that the server must support retrieval of a specific Organization resource by its logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---
# REQ-051
**ID**: 51
**Summary**: Server SHOULD support vread for Organization
**Requirement**: "A Server SHOULD be capable of returning a Organization resource using: `GET [base]/Organization/[id]/_history/vid`"
**Context**: This is a recommended capability for the server to support retrieval of a specific version of an Organization resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---
# REQ-052
**ID**: 52
**Summary**: Server SHALL support _includes for Organization
**Requirement**: "A Server SHALL be capable of supporting the following _includes: Organization:partof - `GET [base]/Organization?[parameter=value]&_include=Organization:partof`; Organization:endpoint - `GET [base]/Organization?[parameter=value]&_include=Organization:endpoint`; Organization:coverage-area - `GET [base]/Organization?[parameter=value]&_include=Organization:coverage-area`"
**Context**: This requirement mandates that the server must support the _include parameter to return partof, endpoint, and coverage-area resources referenced by Organization resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---
# REQ-053
**ID**: 53
**Summary**: Server SHALL support _revincludes for Organization
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: Endpoint:organization - `GET [base]/Organization?[parameter=value]&_revinclude=Endpoint:organization`; HealthcareService:organization - `GET [base]/Organization?[parameter=value]&_revinclude=HealthcareService:organization`; InsurancePlan:administered-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:administered-by`; InsurancePlan:owned-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:owned-by`; OrganizationAffiliation:primary-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:primary-organization`; PractitionerRole:organization - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:organization`; PractitionerRole:network - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:network`; OrganizationAffiliation:participating-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:participating-organization`"
**Context**: This requirement mandates that the server must support the _revinclude parameter to return Endpoint, HealthcareService, InsurancePlan, OrganizationAffiliation, and PractitionerRole resources that reference the Organization resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---
# REQ-054
**ID**: 54
**Summary**: Server SHALL support search parameters for Organization
**Requirement**: "[Server] SHALL [support search by] partof [reference] `GET [base]/Organization?partof=[partof]`; endpoint [reference] `GET [base]/Organization?endpoint=[endpoint]`; address [string] `GET [base]/Organization?address=[address]`; name [string] `GET [base]/Organization?name=[name]`; _id [token] `GET [base]/Organization?_id=[id]`; _lastUpdated [date] `GET [base]/Organization?_lastUpdated=[_lastUpdated]`; type [token] `GET [base]/Organization?type=[system] [code]`; coverage-area [reference] `GET [base]/Organization?coverage-area=[coverage-area]`"
**Context**: This requirement mandates that the server must support searching Organization resources by partof, endpoint, address, name, _id, _lastUpdated, type, and coverage-area parameters.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization

---
# REQ-055
**ID**: 55
**Summary**: Server SHALL support search-type and read interactions for OrganizationAffiliation
**Requirement**: "[Server] SHALL support `search-type`, `read` [for OrganizationAffiliation resource]"
**Context**: This requirement mandates that the server must support both search-type operations to query for OrganizationAffiliation resources and read operations to retrieve specific OrganizationAffiliation resources by ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: General/Cross-Resource

---
# REQ-056
**ID**: 56
**Summary**: Server SHOULD support vread interaction for OrganizationAffiliation
**Requirement**: "[Server] SHOULD support `vread` [for OrganizationAffiliation resource]"
**Context**: This is a recommended capability for the server to support version-specific read operations on OrganizationAffiliation resources.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: General/Cross-Resource

---
# REQ-057
**ID**: 57
**Summary**: Server SHALL support read by ID for OrganizationAffiliation
**Requirement**: "A Server SHALL be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]`"
**Context**: This requirement mandates that the server must support retrieval of a specific OrganizationAffiliation resource by its logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: General/Cross-Resource

---
# REQ-058
**ID**: 58
**Summary**: Server SHOULD support vread for OrganizationAffiliation
**Requirement**: "A Server SHOULD be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]/_history/vid`"
**Context**: This is a recommended capability for the server to support retrieval of a specific version of an OrganizationAffiliation resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: General/Cross-Resource

---
# REQ-059
**ID**: 59
**Summary**: Server SHALL support _includes for OrganizationAffiliation
**Requirement**: "A Server SHALL be capable of supporting the following _includes: OrganizationAffiliation:primary-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:primary-organization`; OrganizationAffiliation:participating-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:participating-organization`; OrganizationAffiliation:location - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:location`; OrganizationAffiliation:service - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:service`; OrganizationAffiliation:endpoint - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:endpoint`; OrganizationAffiliation:network - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:network`"
**Context**: This requirement mandates that the server must support the _include parameter to return primary-organization, participating-organization, location, service, endpoint, and network resources referenced by OrganizationAffiliation resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: General/Cross-Resource

---
# REQ-060
**ID**: 60
**Summary**: Server SHALL support search parameters for OrganizationAffiliation
**Requirement**: "[Server] SHALL [support search by] primary-organization [reference] `GET [base]/OrganizationAffiliation?primary-organization=[primary-organization]`; participating-organization [reference] `GET [base]/OrganizationAffiliation?participating-organization=[participating-organization]`; location [reference] `GET [base]/OrganizationAffiliation?location=[location]`; service [reference] `GET [base]/OrganizationAffiliation?service=[service]`; network [reference] `GET [base]/OrganizationAffiliation?network=[network]`; endpoint [reference] `GET [base]/OrganizationAffiliation?endpoint=[endpoint]`; role [token] `GET [base]/OrganizationAffiliation?role=[system] [code]`; specialty [token] `GET [base]/OrganizationAffiliation?specialty=[system] [code]`; _id [token] `GET [base]/OrganizationAffiliation?_id=[id]`; _lastUpdated [date] `GET [base]/OrganizationAffiliation?_lastUpdated=[_lastUpdated]`"
**Context**: This requirement mandates that the server must support searching OrganizationAffiliation resources by primary-organization, participating-organization, location, service, network, endpoint, role, specialty, _id, and _lastUpdated parameters.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: General/Cross-Resource

---
# REQ-061
**ID**: 61
**Summary**: Server SHALL support search-type and read interactions for Practitioner
**Requirement**: "[Server] SHALL support `search-type`, `read` [for Practitioner resource]"
**Context**: This requirement mandates that the server must support both search-type operations to query for Practitioner resources and read operations to retrieve specific Practitioner resources by ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-062
**ID**: 62
**Summary**: Server SHOULD support vread interaction for Practitioner
**Requirement**: "[Server] SHOULD support `vread` [for Practitioner resource]"
**Context**: This is a recommended capability for the server to support version-specific read operations on Practitioner resources.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-063
**ID**: 63
**Summary**: Server SHALL support read by ID for Practitioner
**Requirement**: "A Server SHALL be capable of returning a Practitioner resource using: `GET [base]/Practitioner/[id]`"
**Context**: This requirement mandates that the server must support retrieval of a specific Practitioner resource by its logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-064
**ID**: 64
**Summary**: Server SHOULD support vread for Practitioner
**Requirement**: "A Server SHOULD be capable of returning a Practitioner resource using: `GET [base]/Practitioner/[id]/_history/vid`"
**Context**: This is a recommended capability for the server to support retrieval of a specific version of a Practitioner resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-065
**ID**: 65
**Summary**: Server SHALL support _revincludes for Practitioner
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: PractitionerRole:practitioner - `GET [base]/Practitioner?[parameter=value]&_revinclude=PractitionerRole:practitioner`"
**Context**: This requirement mandates that the server must support the _revinclude parameter to return PractitionerRole resources that reference the Practitioner resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-066
**ID**: 66
**Summary**: Server SHALL support search parameters for Practitioner
**Requirement**: "[Server] SHALL [support search by] name [string] `GET [base]/Practitioner?name=[name]`; _id [token] `GET [base]/Practitioner?_id=[id]`; _lastUpdated [date] `GET [base]/Practitioner?_lastUpdated=[_lastUpdated]`; family [string] `GET [base]/Practitioner?family=[family]`; given [string] `GET [base]/Practitioner?given=[given]`"
**Context**: This requirement mandates that the server must support searching Practitioner resources by name, _id, _lastUpdated, family, and given parameters.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.7 Practitioner
**Grouping**: Practitioner

---
# REQ-067
**ID**: 67
**Summary**: Server SHALL support search-type and read interactions for PractitionerRole
**Requirement**: "[Server] SHALL support `search-type`, `read` [for PractitionerRole resource]"
**Context**: This requirement mandates that the server must support both search-type operations to query for PractitionerRole resources and read operations to retrieve specific PractitionerRole resources by ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-068
**ID**: 68
**Summary**: Server SHOULD support vread interaction for PractitionerRole
**Requirement**: "[Server] SHOULD support `vread` [for PractitionerRole resource]"
**Context**: This is a recommended capability for the server to support version-specific read operations on PractitionerRole resources.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-069
**ID**: 69
**Summary**: Server SHALL support read by ID for PractitionerRole
**Requirement**: "A Server SHALL be capable of returning a PractitionerRole resource using: `GET [base]/PractitionerRole/[id]`"
**Context**: This requirement mandates that the server must support retrieval of a specific PractitionerRole resource by its logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-070
**ID**: 70
**Summary**: Server SHOULD support vread for PractitionerRole
**Requirement**: "A Server SHOULD be capable of returning a PractitionerRole resource using: `GET [base]/PractitionerRole/[id]/_history/vid`"
**Context**: This is a recommended capability for the server to support retrieval of a specific version of a PractitionerRole resource.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-071
**ID**: 71
**Summary**: Server SHALL support _includes for PractitionerRole
**Requirement**: "A Server SHALL be capable of supporting the following _includes: PractitionerRole:practitioner - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:practitioner`; PractitionerRole:organization - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:organization`; PractitionerRole:location - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:location`; PractitionerRole:service - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:service`; PractitionerRole:network - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:network`; PractitionerRole:endpoint - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:endpoint`"
**Context**: This requirement mandates that the server must support the _include parameter to return practitioner, organization, location, service, network, and endpoint resources referenced by PractitionerRole resources in search results.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-072
**ID**: 72
**Summary**: Server SHALL support search parameters for PractitionerRole
**Requirement**: "[Server] SHALL [support search by] practitioner [reference] `GET [base]/PractitionerRole?practitioner=[practitioner]`; organization [reference] `GET [base]/PractitionerRole?organization=[organization]`; location [reference] `GET [base]/PractitionerRole?location=[location]`; service [reference] `GET [base]/PractitionerRole?service=[service]`; network [reference] `GET [base]/PractitionerRole?network=[network]`; endpoint [reference] `GET [base]/PractitionerRole?endpoint=[endpoint]`; role [token] `GET [base]/PractitionerRole?role=[system] [code]`; specialty [token] `GET [base]/PractitionerRole?specialty=[system] [code]`; _id [token] `GET [base]/PractitionerRole?_id=[id]`; _lastUpdated [date] `GET [base]/PractitionerRole?_lastUpdated=[_lastUpdated]`"
**Context**: This requirement mandates that the server must support searching PractitionerRole resources by practitioner, organization, location, service, network, endpoint, role, specialty, _id, and _lastUpdated parameters.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-073
**ID**: 73
**Summary**: Org Description Extension URL Constraint
**Requirement**: "[The org-description extension] url [SHALL be] 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description'"
**Context**: The org-description extension defines a standardized way to provide a human-readable description of an organization within the Plan-Net Implementation Guide. The extension has a fixed URL that must be used when the extension is included in an Organization resource. The cardinality constraint of 1..1 on the url element indicates this is a mandatory, singular value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the org-description extension is used on an Organization resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: Org Description - Differential View / Snapshot View
**Grouping**: Organization

---
# REQ-074
**ID**: 74
**Summary**: Org Description Extension Value Constraint
**Requirement**: "[The org-description extension] value[x] [SHALL have cardinality] 1..1 [and type] string"
**Context**: The org-description extension requires exactly one value element of type string to carry the human-readable description of the organization. The cardinality of 1..1 makes this a mandatory element when the extension is present, ensuring that every use of the extension provides actual descriptive content.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the org-description extension is used on an Organization resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: Org Description - Differential View / Snapshot View
**Grouping**: Organization

---
# REQ-075
**ID**: 75
**Summary**: Org Description Extension Nested Extension Prohibition
**Requirement**: "[The org-description extension] extension [SHALL have cardinality] 0..0"
**Context**: The org-description extension is defined as a simple extension that does not support nested extensions. The cardinality constraint of 0..0 on the extension element explicitly prohibits the inclusion of any nested extensions within the org-description extension structure.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the org-description extension is used on an Organization resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: Org Description - Differential View / Snapshot View
**Grouping**: Organization

---
# REQ-076
**ID**: 76
**Summary**: Network Reference Extension - value[x] cardinality requirement
**Requirement**: "value[x] [SHALL have cardinality] 1..1 [and be of type] Reference([Plan-Net Network])"
**Context**: The Network Reference extension is used on PractitionerRole resources to reference healthcare provider insurance networks (plannet-Network) that a practitioner participates in through their role. The value element of this extension must contain exactly one reference to a Plan-Net Network resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Network Reference extension is used on a PractitionerRole resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: Network Reference - Differential View
**Grouping**: PractitionerRole

---
# REQ-077
**ID**: 77
**Summary**: Network Reference Extension - url element requirement
**Requirement**: "url [SHALL have cardinality] 1..1 [and SHALL have fixed value] 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network-reference'"
**Context**: The Network Reference extension requires that the url element contain the canonical URL identifying this extension definition. This ensures proper identification and validation of the extension when used in FHIR resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Network Reference extension is used on a PractitionerRole resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: Network Reference - Differential View
**Grouping**: PractitionerRole

---
# REQ-078
**ID**: 78
**Summary**: Network Reference Extension - extension element prohibition
**Requirement**: "extension [SHALL have cardinality] 0..0"
**Context**: The Network Reference extension is defined as a simple extension that does not support nested extensions. The extension element within this extension must not be present, ensuring the extension maintains its simple structure with only the required url and value elements.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Network Reference extension is used on a PractitionerRole resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: Network Reference - Differential View
**Grouping**: PractitionerRole

---
# REQ-079
**ID**: 79
**Summary**: Communication Proficiency Extension Value Binding Requirement
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [Language Proficiency VS]"
**Context**: The communication-proficiency extension is used on Practitioner.communication to express a practitioner's spoken proficiency with the indicated language. The value[x] element of this extension must be a CodeableConcept that is bound to the Language Proficiency VS value set with required binding strength, meaning any concept used must come from this value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.67.1.1.1 Terminology Bindings
**Grouping**: Practitioner

---
# REQ-080
**ID**: 80
**Summary**: Accessibility Extension Value Binding Conformance
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [AccessibilityVS] if any of the codes within the value set can apply to the concept being communicated."
**Context**: The Accessibility extension is used to describe accessibility options offered by a practitioner or at a location within the Plan-Net Location profile. The extension's value[x] element has cardinality 1..1 and type CodeableConcept. This requirement constrains the vocabulary used to describe accessibility options, requiring that if an applicable code exists in the AccessibilityVS value set, it must be used. If the value set does not cover the concept, alternate codings or text may be included instead (extensible binding).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies only if any of the codes within the AccessibilityVS value set can apply to the concept being communicated about accessibility options.
**Verifiable**: Yes
**Verifiability Details**: Automation - Validate that when the Accessibility extension is present on a Location resource, the value[x] element contains a CodeableConcept with a code from the AccessibilityVS value set when applicable codes exist for the accessibility concept being communicated.
**Section**: 11.66.1.1.1 Terminology Bindings
**Grouping**: Location

---
# REQ-081
**ID**: 81
**Summary**: PractitionerPeriod Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the PractitionerPeriod extension's URL element, which must contain the specific URI that identifies this extension definition within the DaVinci PDex Plan-Net Implementation Guide.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-082
**ID**: 82
**Summary**: PractitionerPeriod Extension Must Support Value Element
**Requirement**: "Extension.value[x] [Must Support] true"
**Context**: The value element of the PractitionerPeriod extension, which indicates when a Practitioner entry is or was active, must be supported by implementations. This element has a cardinality of 1..1 in the snapshot view and contains a Period or other data type value.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-083
**ID**: 83
**Summary**: PractitionerPeriod Extension Must Have Either Extensions or Value
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: This invariant (ext-1) applies to the PractitionerPeriod extension and ensures that the extension contains either nested extensions or a value, but not both simultaneously. This is a fundamental FHIR extension constraint.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-084
**ID**: 84
**Summary**: PractitionerPeriod Extension Elements Must Have Value or Children
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: This invariant (ele-1) applies to all elements within the PractitionerPeriod extension, ensuring that each element either contains a value attribute or has child elements, maintaining FHIR's requirement that elements must contain content.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.75.1 Extension: PractitionerPeriod - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-085
**ID**: 85
**Summary**: NetworkReference Extension url SHALL be fixed value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The network-reference extension is used to reference healthcare provider insurance networks (plannet-Network) that a practitioner participates in through their role. The Extension.url element must be set to the fixed value identifying this specific extension definition.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: NetworkReference - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-086
**ID**: 86
**Summary**: NetworkReference Extension value[x] cardinality requirement
**Requirement**: "[Extension.value[x] Control: 1.1] Value of extension - must be one of a constrained set of the data types"
**Context**: The network-reference extension must include exactly one value element that references a Plan-Net Network resource. This is indicated by the cardinality of 1..1 and the Must Support flag being true for this element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: NetworkReference - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-087
**ID**: 87
**Summary**: NetworkReference Extension Must Support value[x]
**Requirement**: "[Extension.value[x]] Must Support: true"
**Context**: The value[x] element of the network-reference extension, which contains the Reference to the Plan-Net Network resource, must be supported by implementations. This ensures that systems can properly exchange network reference information for practitioners.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: NetworkReference - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-088
**ID**: 88
**Summary**: LocationReference Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The location-reference extension is used to reference a Location resource (plannet-Location) defining the coverage area of a health insurance provider network. The extension URL must be fixed to the specific URI that identifies this extension definition.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.71.1 Extension: LocationReference - Detailed Descriptions
**Grouping**: Location

---
# REQ-089
**ID**: 89
**Summary**: LocationReference Extension Must Support value[x] Element
**Requirement**: "Extension.value[x] [Must Support] true"
**Context**: The location-reference extension requires the value[x] element to be Must Support. This element contains the actual reference to the Plan-Net Location resource. The value[x] element has a cardinality of 1..1 and must be of type Reference(Plan-Net Location).
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.71.1 Extension: LocationReference - Detailed Descriptions
**Grouping**: Location

---
# REQ-090
**ID**: 90
**Summary**: LocationReference Extension Invariant ele-1
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: This invariant applies to the Extension element and its child elements (Extension.extension, Extension.value[x]). It ensures that each FHIR element contains either a value or child elements beyond just an id.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.71.1 Extension: LocationReference - Detailed Descriptions
**Grouping**: Location

---
# REQ-091
**ID**: 91
**Summary**: LocationReference Extension Invariant ext-1
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: This invariant applies to the Extension element and ensures that an extension either has nested extensions or a value, but not both simultaneously. This maintains the proper structure of FHIR extensions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.71.1 Extension: LocationReference - Detailed Descriptions
**Grouping**: Location

---
# REQ-092
**ID**: 92
**Summary**: OrgDescription Extension Must Support value[x] Element
**Requirement**: "Extension.value[x] [Must Support] true"
**Context**: The org-description extension defines a human-readable description of an organization. The value[x] element, which contains the actual description value, is marked as Must Support, indicating that implementers must be capable of processing and storing this element when present in received resources, and should populate it in resources they create when the information is available.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Attestation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---
# REQ-093
**ID**: 93
**Summary**: OrgDescription Extension URL Fixed Value
**Requirement**: "Extension.url [Fixed Value] `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description`"
**Context**: The url element of the org-description extension must have a fixed value that identifies the extension definition. This ensures proper identification and interpretation of the extension across all implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---
# REQ-094
**ID**: 94
**Summary**: OrgDescription Extension value[x] Cardinality
**Requirement**: "Extension.value[x] [Control] 1.1"
**Context**: The value[x] element of the org-description extension has a cardinality of 1..1, meaning it is required and must appear exactly once. This ensures that when the org-description extension is used, it always contains a description value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---
# REQ-095
**ID**: 95
**Summary**: OrgDescription Extension value[x] Type Constraint
**Requirement**: "Extension.value[x] [Type] [string]"
**Context**: In the snapshot view of the org-description extension, the value[x] element is constrained to be of type string only, rather than the full range of data types typically allowed for extension values. This ensures the organization description is provided as a simple string value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---
# REQ-096
**ID**: 96
**Summary**: Extension Must Have Either Extensions or value[x]
**Requirement**: "Must have either extensions or value[x], not both (`extension.exists() != value.exists()`)"
**Context**: This is a standard FHIR invariant (ext-1) that applies to all extensions. An extension must contain either nested extensions or a value, but not both simultaneously. This maintains the structural integrity of extension definitions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---
# REQ-097
**ID**: 97
**Summary**: Extension URL Must Be URI for Structure Definition
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The url element that identifies an extension must be a URI that points to the StructureDefinition resource that formally defines the extension. This ensures that extensions can be properly validated and interpreted according to their formal definitions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---
# REQ-098
**ID**: 98
**Summary**: Extension Governance Requirements
**Requirement**: "To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: FHIR extensions must follow governance requirements to ensure interoperability and safety. While implementers have flexibility to define extensions, they must adhere to specified requirements for extension definition to maintain consistency across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Attestation
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization

---
# REQ-099
**ID**: 99
**Summary**: Accessibility Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The accessibility extension must have its URL element set to the canonical URI that identifies this extension definition. This ensures proper identification and validation of the extension when used in resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation - Verify that Extension.url = "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility"
**Section**: 11.66.1 Extension: Accessibility - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-100
**ID**: 100
**Summary**: Accessibility Extension Value Binding
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Accessibility VS]"
**Context**: The value[x] element of the accessibility extension, when populated with a CodeableConcept, must use codes from the Accessibility ValueSet (http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/AccessibilityVS) with extensible binding strength, meaning codes should be from this value set unless no suitable code exists.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when value[x] is populated with a CodeableConcept and a suitable code exists in the value set
**Verifiable**: Yes
**Verifiability Details**: Automation - Validate that CodeableConcept codes are from AccessibilityVS value set when suitable codes exist
**Section**: 11.66.1 Extension: Accessibility - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-101
**ID**: 101
**Summary**: Communication Proficiency Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the communication-proficiency extension, which expresses a practitioner's spoken proficiency with the language indicated in practitioner.communication. The extension URL must be fixed to the specified value to ensure proper identification and processing of the extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation - Verify that Extension.url has fixed value `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency`
**Section**: 11.67.1 Extension: CommunicationProficiency - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-102
**ID**: 102
**Summary**: Communication Proficiency Value Binding
**Requirement**: "The codes SHALL be taken from [Language Proficiency VS](ValueSet-LanguageProficiencyVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/LanguageProficiencyVS`)"
**Context**: This requirement specifies that when the communication-proficiency extension is used to indicate a practitioner's language proficiency level, the value must come from the specified Language Proficiency value set. This ensures standardized representation of proficiency levels across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation - Verify that Extension.value[x] contains codes from the LanguageProficiencyVS value set
**Section**: 11.67.1 Extension: CommunicationProficiency - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-103
**ID**: 103
**Summary**: ViaIntermediary Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the via-intermediary extension which provides a reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for an organization. The extension URL must be fixed to the specified value to properly identify this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation - Verify that Extension.url has the fixed value http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-104
**ID**: 104
**Summary**: ViaIntermediary Extension Must Support value[x] Element
**Requirement**: "Extension.value[x] [Must Support] true"
**Context**: The via-intermediary extension's value[x] element, which contains a reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location), must be supported by implementations. The cardinality is 1..1, making this a required element when the extension is present.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation - Verify that systems support the Extension.value[x] element which references Plan-Net PractitionerRole, OrganizationAffiliation, Location, or Organization profiles
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-105
**ID**: 105
**Summary**: ViaIntermediary Extension Must Have Value or Children
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: This invariant (ele-1) applies to all elements within the via-intermediary extension structure, ensuring that each element either has a value or has child elements (beyond just an id).
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation - Verify that all elements in the via-intermediary extension have either a @value attribute or child elements
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-106
**ID**: 106
**Summary**: ViaIntermediary Extension Must Have Extensions or Value, Not Both
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: This invariant (ext-1) applies to the via-intermediary extension, ensuring that an extension element contains either nested extensions or a value element, but not both simultaneously.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation - Verify that Extension elements have either extension children or value[x], but not both
**Section**: 11.78.1 Extension: ViaIntermediary - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-107
**ID**: 107
**Summary**: Endpoint usecase extension type element cardinality requirement
**Requirement**: "extension:type [SHALL have cardinality] 1.1"
**Context**: The endpoint-usecase extension defines specific use cases (service descriptions) supported by an endpoint. The extension contains two sub-elements: 'type' and 'standard'. The 'type' sub-extension is mandatory and must appear exactly once to indicate the type of services supported by the endpoint.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: Endpoint Usecase - Differential Table
**Grouping**: Endpoint

---
# REQ-108
**ID**: 108
**Summary**: Endpoint usecase extension type value binding requirement
**Requirement**: "extension:type.value[x] [SHALL use] Binding: Endpoint Usecases VS (extensible)"
**Context**: The value element of the type sub-extension in the endpoint-usecase extension must be bound to the Endpoint Usecases VS value set. The binding is extensible, meaning the concept SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept, alternate codings may be included instead.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If any of the codes within the value set can apply to the concept being communicated, the concept SHALL be from the specified value set. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: Endpoint Usecase - Differential Table
**Grouping**: Endpoint

---
# REQ-109
**ID**: 109
**Summary**: Delivery method extension type element SHALL use required value set
**Requirement**: "Extension.extension:type.value[x] [SHALL be] from the specified value set [DeliveryMethodVS]"
**Context**: The delivery-method extension is used on HealthcareService resources to describe the service delivery method. The type sub-extension indicates whether service delivery is physical or virtual and must use a code from the DeliveryMethodVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: Delivery Method - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-110
**ID**: 110
**Summary**: Delivery method extension virtualModalities element SHALL use extensible value set
**Requirement**: "Extension.extension:virtualModalities.value[x] [SHALL] be from the specified value set [VirtualModalitiesVS] if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: The delivery-method extension is used on HealthcareService resources. When service delivery is virtual, the virtualModalities sub-extension specifies the delivery modalities and should use codes from the VirtualModalitiesVS value set when applicable.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when specifying virtual delivery modalities and when codes from the VirtualModalitiesVS value set can apply to the concept being communicated.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: Delivery Method - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-111
**ID**: 111
**Summary**: Practitioner Qualification Extension - Status Element Cardinality
**Requirement**: "The extension:status element SHALL have cardinality 1..1"
**Context**: The Practitioner Qualification extension adds status and whereValid elements to a practitioner's qualifications. The status sub-extension is mandatory and must appear exactly once when the practitioner-qualification extension is used on the Practitioner.qualification element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the practitioner-qualification extension is used on Practitioner.qualification
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: Practitioner Qualification
**Grouping**: Practitioner

---
# REQ-112
**ID**: 112
**Summary**: Practitioner Qualification Extension - Status Value Binding
**Requirement**: "The extension:status.value[x] element SHALL be bound to the Qualification Status VS value set with required binding strength"
**Context**: The status sub-extension within the Practitioner Qualification extension must use a code from the specified Qualification Status ValueSet. This ensures standardized representation of qualification status values across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the practitioner-qualification extension is used on Practitioner.qualification
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: Practitioner Qualification - Terminology Bindings
**Grouping**: Practitioner

---
# REQ-113
**ID**: 113
**Summary**: Practitioner Qualification Extension - WhereValid ValueCodeableConcept Binding
**Requirement**: "The extension:whereValid.value[x]:valueCodeableConcept element SHALL be bound to the USPS Two Letter Alphabetic Codes value set with required binding strength"
**Context**: When the whereValid sub-extension uses a CodeableConcept data type to indicate where a practitioner's qualification is valid, it must use codes from the USPS Two Letter Alphabetic Codes ValueSet to ensure standardized state representation.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the practitioner-qualification extension is used on Practitioner.qualification and the whereValid sub-extension uses valueCodeableConcept
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: Practitioner Qualification - Terminology Bindings
**Grouping**: Practitioner

---
# REQ-114
**ID**: 114
**Summary**: Extension.extension:type cardinality requirement
**Requirement**: "Extension.extension:type [Control: 1.1]"
**Context**: The endpoint-usecase extension defines an enumeration of specific use cases (service descriptions) supported by the endpoint. The extension has a sub-extension 'type' that provides an indication of the type of services supported by the endpoint. This requirement specifies that the 'type' sub-extension must appear exactly once (cardinality 1..1).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-115
**ID**: 115
**Summary**: Extension.extension:type Must Support requirement
**Requirement**: "Extension.extension:type [Must Support: true]"
**Context**: The 'type' sub-extension within the endpoint-usecase extension is marked as Must Support, meaning systems claiming conformance to this profile must be capable of populating and processing this element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-116
**ID**: 116
**Summary**: Extension.extension:type.value[x] binding requirement
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Endpoint Usecases VS] (extensible to http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/EndpointUsecaseVS)"
**Context**: The value for the 'type' sub-extension must be a CodeableConcept, and the codes used should be taken from the Endpoint Usecases Value Set. The binding strength is extensible, meaning codes from the specified value set should be used unless no suitable code exists, in which case codes from other code systems may be used.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used and unless no suitable code exists in the value set.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-117
**ID**: 117
**Summary**: Extension.extension:standard cardinality requirement
**Requirement**: "Extension.extension:standard [Control: 0.1]"
**Context**: The endpoint-usecase extension has an optional sub-extension 'standard' that provides a URI to a published standard describing the services supported by the endpoint (e.g., an HL7 implementation guide). This requirement specifies that the 'standard' sub-extension may appear at most once (cardinality 0..1).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-118
**ID**: 118
**Summary**: Extension.extension:standard Must Support requirement
**Requirement**: "Extension.extension:standard [Must Support: true]"
**Context**: The 'standard' sub-extension within the endpoint-usecase extension is marked as Must Support, meaning systems claiming conformance to this profile must be capable of populating and processing this element when it is present.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used and the 'standard' sub-extension is present.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-119
**ID**: 119
**Summary**: Extension.url fixed value requirement
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension [Extension.url Fixed Value: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase]"
**Context**: The extension URL for the endpoint-usecase extension must be fixed to the canonical URL http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase. This ensures proper identification of the extension in FHIR resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-120
**ID**: 120
**Summary**: Extension invariant ele-1 requirement
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: This invariant (ele-1) ensures that every FHIR element in the extension has either a value or child elements. This is a fundamental FHIR constraint that must be satisfied for the extension to be valid.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-121
**ID**: 121
**Summary**: Extension invariant ext-1 requirement
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: This invariant (ext-1) ensures that an extension element has either sub-extensions or a value, but not both simultaneously. This is a fundamental FHIR constraint for extension structures.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: EndpointUsecase - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-122
**ID**: 122
**Summary**: Delivery Method Extension Type Value Binding
**Requirement**: "The codes SHALL be taken from [Delivery Methods VS](ValueSet-DeliveryMethodVS.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/DeliveryMethodVS`)"
**Context**: The delivery-method extension includes a 'type' sub-extension that indicates whether service delivery is physical or virtual. The value[x] element of this type sub-extension must use codes from the Delivery Methods Value Set with a required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: DeliveryMethod - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-123
**ID**: 123
**Summary**: Virtual Modalities Extension Value Binding
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Virtual Modalities VS](ValueSet-VirtualModalitiesVS.html)([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/VirtualModalitiesVS`)"
**Context**: The delivery-method extension includes a 'virtualModalities' sub-extension that specifies modalities of virtual delivery when service delivery is virtual. The value[x] element of this virtualModalities sub-extension should use codes from the Virtual Modalities Value Set with an extensible binding strength, allowing other codes if the value set is not suitable.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the codes are suitable for the use case.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: DeliveryMethod - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-124
**ID**: 124
**Summary**: Extension URL Definition Must Be URI
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: The url element within the extension definition must contain a URI that points to the Structure Definition that defines the extension. This applies to the extension itself and its sub-extensions (type and virtualModalities).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.69.1 Extension: DeliveryMethod - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-125
**ID**: 125
**Summary**: Extension Requirements for Definition
**Requirement**: "There is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: When defining any extension within the delivery-method extension structure, there are governance requirements that must be met to ensure safe and manageable use of extensions according to FHIR standards.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Attestation
**Section**: 11.69.1 Extension: DeliveryMethod - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-126
**ID**: 126
**Summary**: PractitionerQualification extension must include status sub-extension
**Requirement**: "Extension.extension:status [Control: 1.1]"
**Context**: The PractitionerQualification extension defines an extension to add status and whereValid elements to a practitioner's qualifications. The status sub-extension has a cardinality of 1..1, meaning it is required to be present exactly once when the PractitionerQualification extension is used.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the PractitionerQualification extension is used.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-127
**ID**: 127
**Summary**: PractitionerQualification status value must be from required ValueSet
**Requirement**: "The codes SHALL be taken from [Qualification Status VS](ValueSet-QualificationStatusVS.html)([required] to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/QualificationStatusVS`)"
**Context**: The status sub-extension within the PractitionerQualification extension must use codes from the specified Qualification Status VS value set with required binding strength. This ensures standardized representation of practitioner qualification status.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the status sub-extension of the PractitionerQualification extension is populated.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-128
**ID**: 128
**Summary**: PractitionerQualification whereValid CodeableConcept must use USPS state codes
**Requirement**: "The codes SHALL be taken from [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU7/ValueSet-us-core-usps-state.html)([required] to `http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state`)"
**Context**: When the whereValid sub-extension of the PractitionerQualification extension uses a CodeableConcept data type to indicate where a practitioner's qualification is valid, the codes must come from the USPS Two Letter Alphabetic Codes value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the whereValid sub-extension uses the valueCodeableConcept choice and is populated.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-129
**ID**: 129
**Summary**: Extension definition must be valid URI for Structure Definition
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: Multiple instances in the detailed descriptions indicate that the definition for extension codes must be a URI pointing to the Structure Definition. This applies to the url elements throughout the extension structure (Extension.extension:status.url, Extension.extension:whereValid.url, Extension.url).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-130
**ID**: 130
**Summary**: Extension must have either extensions or value[x], not both
**Requirement**: "Must have either extensions or value[x], not both (`extension.exists() != value.exists()`)"
**Context**: The ext-1 invariant applies to multiple levels of the PractitionerQualification extension structure, ensuring that an extension element contains either nested extensions or a value, but not both simultaneously. This maintains proper extension structure according to FHIR specifications.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-131
**ID**: 131
**Summary**: ContactPoint AvailableTime Extension - daysOfWeek value binding requirement
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [DaysOfWeek]"
**Context**: The contactpoint-availabletime extension defines days and times when a contact point is available. The daysOfWeek sub-extension must use codes from the required DaysOfWeek value set (http://hl7.org/fhir/ValueSet/days-of-week). This extension may be used on ContactPoint elements within HealthcareService, Location, Network, Organization, Practitioner, and PractitionerRole resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: Contactpoint Availabletime - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-132
**ID**: 132
**Summary**: NewPatients Extension - acceptingPatients element cardinality and type requirement
**Requirement**: "extension:acceptingPatients [SHALL have cardinality] 1..1 [and type] CodeableConcept"
**Context**: The NewPatients extension is used in PractitionerRole, HealthcareService, and Location profiles to indicate whether new patients are being accepted. The acceptingPatients sub-extension is mandatory and must contain exactly one CodeableConcept value indicating the acceptance status.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients
**Grouping**: General/Cross-Resource

---
# REQ-133
**ID**: 133
**Summary**: NewPatients Extension - acceptingPatients value binding requirement
**Requirement**: "extension:acceptingPatients.value[x] [SHALL use] Binding: Accepting Patients Codes VS (required)"
**Context**: The acceptingPatients sub-extension value must be bound to the AcceptingPatientsVS value set with required strength, ensuring only valid codes from the specified code system are used to indicate patient acceptance status.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-134
**ID**: 134
**Summary**: NewPatients Extension - fromNetwork element cardinality and type requirement
**Requirement**: "extension:fromNetwork [SHALL have cardinality] 0..1 [and type] Reference(Plan-Net Network)"
**Context**: The NewPatients extension optionally allows specification of a network from which new patients are being accepted through the fromNetwork sub-extension, which references a Plan-Net Network resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients
**Grouping**: General/Cross-Resource

---
# REQ-135
**ID**: 135
**Summary**: NewPatients Extension - characteristics element cardinality and type requirement
**Requirement**: "extension:characteristics [SHALL have cardinality] 0..* [and type] string"
**Context**: The NewPatients extension allows zero or more characteristics sub-extensions to describe characteristics of accepted patients, each containing a string value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients
**Grouping**: General/Cross-Resource

---
# REQ-136
**ID**: 136
**Summary**: NewPatients Extension - conditional characteristics constraint
**Requirement**: "If no new patients are accepted, no characteristics are allowed: extension.where(url='acceptingPatients').value.ofType(CodeableConcept).coding.where(code = 'no') implies extension.where(url='characteristics').empty()"
**Context**: This constraint ensures logical consistency in the NewPatients extension by preventing the specification of patient characteristics when the provider is not accepting new patients.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If acceptingPatients value indicates 'no', then characteristics extension must be empty
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.73.1 Extension: New Patients - Constraints
**Grouping**: General/Cross-Resource

---
# REQ-137
**ID**: 137
**Summary**: Qualification extension code element SHALL be from SpecialtyAndDegreeLicenseCertificateVS value set
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated."
**Context**: The qualification extension's code element uses an extensible binding to the SpecialtyAndDegreeLicenseCertificateVS value set. When representing qualification codes (e.g., specialties, degrees, licenses, certificates) for organizations or practitioner roles, implementations SHALL use codes from this value set when applicable codes exist within it.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If any of the codes within the value set can apply to the concept being communicated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-138
**ID**: 138
**Summary**: Qualification extension status element SHALL be from QualificationStatusVS value set
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set."
**Context**: The qualification extension's status element has a required binding to the QualificationStatusVS value set with a fixed value of 'active'. All qualification status values must come from this value set, and the default/fixed value is 'active'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-139
**ID**: 139
**Summary**: Qualification extension whereValid element SHALL be from USPS Two Letter Alphabetic Codes value set
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set."
**Context**: The qualification extension's whereValid element has a required binding to the US Core USPS Two Letter Alphabetic Codes value set. This element indicates the geographic location(s) where a qualification is valid, and must use valid USPS state codes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Terminology Bindings
**Grouping**: General/Cross-Resource
---
# REQ-140
**ID**: 01
**Summary**: All FHIR elements must have value or children
**Requirement**: "All FHIR elements must have a @value or children (`hasValue() or (children().count() > id.count())`)"
**Context**: The ele-1 invariant applies throughout the PractitionerQualification extension structure, ensuring that every FHIR element either has a value or has child elements (excluding just the id element). This is a fundamental FHIR requirement for valid resource structure.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.76.1 Extension: PractitionerQualification - Detailed Descriptions
**Grouping**: Practitioner

---
# REQ-141
**ID**: 02
**Summary**: NewPatients Extension - acceptingPatients Sub-Extension Cardinality
**Requirement**: "Extension.extension:acceptingPatients [Control] 1.1"
**Context**: The NewPatients extension defines whether new patients are being accepted in general or from a specific network. This extension is included in the PractitionerRole, HealthcareService, and Location profiles. The acceptingPatients sub-extension has a cardinality of 1..1, meaning it is required and must appear exactly once.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-142
**ID**: 03
**Summary**: NewPatients Extension - acceptingPatients Must Support
**Requirement**: "Extension.extension:acceptingPatients [Must Support] true"
**Context**: The acceptingPatients sub-extension within the NewPatients extension must be supported by implementations. This is a mandatory support requirement for systems implementing this profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-143
**ID**: 04
**Summary**: NewPatients Extension - acceptingPatients Value Binding
**Requirement**: "Extension.extension:acceptingPatients.value[x] [Binding] The codes SHALL be taken from [Accepting Patients Codes VS] (required to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/AcceptingPatientsVS`)"
**Context**: The value for the acceptingPatients sub-extension must use codes from the Accepting Patients Codes value set. This is a required binding, meaning only codes from this specific value set are permitted.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-144
**ID**: 05
**Summary**: NewPatients Extension - acceptingPatients Value Type
**Requirement**: "Extension.extension:acceptingPatients.value[x] [Type] [CodeableConcept]"
**Context**: The value for the acceptingPatients sub-extension must be of type CodeableConcept. This constrains the data type from the broader choice of types available for extension values.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-145
**ID**: 06
**Summary**: NewPatients Extension - fromNetwork Must Support
**Requirement**: "Extension.extension:fromNetwork [Must Support] true"
**Context**: The fromNetwork sub-extension within the NewPatients extension must be supported by implementations. This sub-extension identifies the specific network from which new patients are being accepted.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-146
**ID**: 07
**Summary**: NewPatients Extension - fromNetwork Value Type
**Requirement**: "Extension.extension:fromNetwork.value[x] [Type] [Reference]([Plan-Net Network])"
**Context**: The value for the fromNetwork sub-extension must be a Reference to a Plan-Net Network resource. This constrains the reference target to only the Plan-Net Network profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-147
**ID**: 08
**Summary**: NewPatients Extension - characteristics Must Support
**Requirement**: "Extension.extension:characteristics [Must Support] true"
**Context**: The characteristics sub-extension within the NewPatients extension must be supported by implementations. This sub-extension describes characteristics of accepted patients.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-148
**ID**: 09
**Summary**: NewPatients Extension - characteristics Value Type
**Requirement**: "Extension.extension:characteristics.value[x] [Type] [string]"
**Context**: The value for the characteristics sub-extension must be of type string. This constrains the data type to a simple string representation of patient characteristics.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-149
**ID**: 10
**Summary**: NewPatients Extension - URL Fixed Value
**Requirement**: "Extension.url [Fixed Value] `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients`"
**Context**: The url element of the NewPatients extension must have the fixed value http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients to properly identify this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-150
**ID**: 11
**Summary**: NewPatients Extension - Invariant new-patients-characteristics
**Requirement**: "Invariants **new-patients-characteristics**: If no new patients are accepted, no characteristics are allowed (`extension.where(url='acceptingPatients').value.ofType(CodeableConcept).coding.where(code = 'no') implies extension.where(url='characteristics').empty()`)"
**Context**: This invariant enforces a business rule that if the acceptingPatients value indicates that no new patients are being accepted (code = 'no'), then the characteristics sub-extension must not be present. This ensures logical consistency in the data.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This constraint applies when acceptingPatients has a code value of 'no'
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-151
**ID**: 12
**Summary**: NewPatients Extension - URL Definition SHALL Constraint
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: When defining or referencing the extension code, the definition element must be a URI that points to the StructureDefinition that formally defines the extension. This applies to all url elements within the extension structure.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-152
**ID**: 13
**Summary**: Plan-Net Endpoint status SHALL be fixed to 'active'
**Requirement**: "Endpoint.status [has a] Fixed Value `active`"
**Context**: The Plan-Net Endpoint profile constrains the status element to always have the value 'active'. This means that all Plan-Net Endpoint resources must have an active status and cannot be in suspended, error, off, entered-in-error, or test states.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.status
**Grouping**: Endpoint

---
# REQ-153
**ID**: 14
**Summary**: Plan-Net Endpoint connectionType SHALL use codes from Endpoint Connection Types VS value set
**Requirement**: "Unless not suitable, these codes SHALL be taken from Endpoint Connection Types VS"
**Context**: The connectionType element represents the technical details of the usage of the endpoint (e.g., what protocols should be used). The binding is extensible, meaning implementations should use codes from the specified value set unless they are not suitable for the use case. Additionally, there is a minimum binding that specifies codes that any conformant system SHALL support.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: The requirement applies "unless not suitable" - the codes SHALL be taken from the value set when they are suitable for the implementation
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.connectionType
**Grouping**: Endpoint

---
# REQ-154
**ID**: 15
**Summary**: Plan-Net Endpoint connectionType SHALL support all codes from Minimum Endpoint Connection Types VS
**Requirement**: "Any conformant system SHALL support all these codes [from Minimum Endpoint Connection Types VS]"
**Context**: The connectionType element has an additional minimum binding that defines the minimum allowable value set. This means that while the primary binding is extensible, conformant systems must at a minimum support all codes defined in the Minimum Endpoint Connection Types VS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.connectionType
**Grouping**: Endpoint

---
# REQ-155
**ID**: 16
**Summary**: Plan-Net Endpoint payloadType SHALL use codes from Endpoint Payload Types VS value set
**Requirement**: "Unless not suitable, these codes SHALL be taken from Endpoint Payload Types VS"
**Context**: The payloadType element describes the acceptable content that can be communicated on the endpoint (e.g., XDS Discharge summaries). The binding is extensible with a cardinality of 1..1, meaning at least one payloadType must be specified and should use codes from the specified value set unless they are not suitable.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: The requirement applies "unless not suitable" - the codes SHALL be taken from the value set when they are suitable for the implementation
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.payloadType
**Grouping**: Endpoint

---
# REQ-156
**ID**: 17
**Summary**: Plan-Net Endpoint payloadMimeType SHALL use codes from Mime Types value set
**Requirement**: "The codes SHALL be taken from Mime Types"
**Context**: The payloadMimeType element specifies the mime type to send the payload in (e.g., application/fhir+xml, application/fhir+json). This is a required binding, meaning only codes from the specified Mime Types value set are permitted. If the mime type is not specified, then the sender could send any content depending on the connectionType.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.payloadMimeType
**Grouping**: Endpoint

---
# REQ-157
**ID**: 18
**Summary**: Plan-Net Endpoint contact.system SHALL use codes from ContactPointSystem value set
**Requirement**: "The codes SHALL be taken from ContactPointSystem"
**Context**: When contact details are provided for the endpoint, the contact.system element describes the telecommunications form for the contact point (phone, fax, email, pager, url, sms, other). This is a required binding to the ContactPointSystem value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Endpoint.contact element is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.contact.system
**Grouping**: Endpoint

---
# REQ-158
**ID**: 19
**Summary**: Plan-Net Endpoint contact.use SHALL use codes from ContactPointUse value set
**Requirement**: "The codes SHALL be taken from ContactPointUse"
**Context**: When contact details are provided for the endpoint, the contact.use element identifies the purpose for the contact point (home, work, temp, old, mobile). This is a required binding to the ContactPointUse value set. This element is labeled as a modifier because applications should not mistake a temporary or old contact for a current/permanent one.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Endpoint.contact.use element is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.contact.use
**Grouping**: Endpoint

---
# REQ-159
**ID**: 20
**Summary**: Plan-Net Endpoint status SHALL use codes from EndpointStatus value set
**Requirement**: "The codes SHALL be taken from EndpointStatus"
**Context**: The status element indicates the operational status of the endpoint (active, suspended, error, off, entered-in-error, test). This is a required binding to the EndpointStatus value set. The element is labeled as a modifier because the status 'entered-in-error' means the resource should not be treated as valid. However, in the Plan-Net profile, this element has a fixed value of 'active'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.status
**Grouping**: Endpoint

---
# REQ-160
**ID**: 21
**Summary**: Plan-Net Endpoint contained resources SHALL NOT contain nested Resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources (contained.contained.empty())"
**Context**: This is a FHIR base invariant (dom-2) that applies to the Endpoint resource. It ensures that if an Endpoint resource is contained within another resource, it cannot itself contain other nested resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Endpoint resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint invariants
**Grouping**: Endpoint

---
# REQ-161
**ID**: 22
**Summary**: Plan-Net Endpoint contained resources SHALL be referred to from elsewhere or SHALL refer to containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This is a FHIR base invariant (dom-3) that applies to the Endpoint resource. It ensures that contained resources are actually used - either they are referenced by another element in the containing resource, or they reference the containing resource themselves. This prevents orphaned contained resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Endpoint resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint invariants
**Grouping**: Endpoint

---
# REQ-162
**ID**: 23
**Summary**: Plan-Net Endpoint contained resources SHALL NOT have meta.versionId or meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (contained.meta.versionId.empty() and contained.meta.lastUpdated.empty())"
**Context**: This is a FHIR base invariant (dom-4) that applies to the Endpoint resource. It ensures that contained resources do not have version or timestamp metadata, as these are managed at the containing resource level.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Endpoint resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint invariants
**Grouping**: Endpoint

---
# REQ-163
**ID**: 24
**Summary**: Plan-Net Endpoint contained resources SHALL NOT have security labels
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label (contained.meta.security.empty())"
**Context**: This is a FHIR base invariant (dom-5) that applies to the Endpoint resource. It ensures that contained resources do not have security labels in their metadata, as security is managed at the containing resource level.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the Endpoint resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint invariants
**Grouping**: Endpoint

---
# REQ-164
**ID**: 25
**Summary**: Plan-Net Endpoint modifier extensions SHALL NOT change meaning of Resource or DomainResource elements
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)"
**Context**: This requirement applies to the modifierExtension element of the Endpoint resource. Modifier extensions are expected to modify the meaning or interpretation of the resource, but they have boundaries - they cannot change the meaning of base Resource or DomainResource elements, including the modifierExtension element itself.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when modifierExtension elements are present in the Endpoint resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions - Endpoint.modifierExtension
**Grouping**: Endpoint

---
# REQ-165
**ID**: 26
**Summary**: Extension URL SHALL be a URI for the Structure Definition defining the extension - daysOfWeek
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the daysOfWeek extension within the contactpoint-availabletime extension. The url element must contain a URI that points to the Structure Definition that formally defines this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions, Element 6 (Extension.extension:daysOfWeek.url)
**Grouping**: General/Cross-Resource

---
# REQ-166
**ID**: 27
**Summary**: Extension daysOfWeek value SHALL be taken from DaysOfWeek ValueSet
**Requirement**: "The codes SHALL be taken from For codes, see [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/ValueSet/days-of-week`)"
**Context**: This requirement constrains the value[x] element of the daysOfWeek extension. When providing a value for days of the week, implementations must use codes from the specified DaysOfWeek ValueSet with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions, Element 8 (Extension.extension:daysOfWeek.value[x])
**Grouping**: General/Cross-Resource

---
# REQ-167
**ID**: 28
**Summary**: Extension definition for an extension SHALL be met as part of the extension definition
**Requirement**: "To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: This requirement establishes that all extensions must comply with a governance framework for their definition. It applies broadly to all extensions defined within the contactpoint-availabletime structure, ensuring consistent and safe extension practices.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions, Element 4 (Extension.extension:daysOfWeek.extension), Element 12 (Extension.extension:allDay.extension), Element 20 (Extension.extension:availableStartTime.extension), Element 28 (Extension.extension:availableEndTime.extension)
**Grouping**: General/Cross-Resource

---
# REQ-168
**ID**: 29
**Summary**: Extension URL SHALL be a URI for the Structure Definition defining the extension - allDay
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the allDay extension within the contactpoint-availabletime extension. The url element must contain a URI that points to the Structure Definition that formally defines this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions, Element 14 (Extension.extension:allDay.url)
**Grouping**: General/Cross-Resource

---
# REQ-169
**ID**: 30
**Summary**: Extension URL SHALL be a URI for the Structure Definition defining the extension - availableStartTime
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the availableStartTime extension within the contactpoint-availabletime extension. The url element must contain a URI that points to the Structure Definition that formally defines this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions, Element 22 (Extension.extension:availableStartTime.url)
**Grouping**: General/Cross-Resource

---
# REQ-170
**ID**: 31
**Summary**: Extension URL SHALL be a URI for the Structure Definition defining the extension - availableEndTime
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the availableEndTime extension within the contactpoint-availabletime extension. The url element must contain a URI that points to the Structure Definition that formally defines this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions, Element 30 (Extension.extension:availableEndTime.url)
**Grouping**: General/Cross-Resource

---
# REQ-171
**ID**: 32
**Summary**: Extension URL SHALL be a URI for the Structure Definition defining the extension - main extension
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element of the main contactpoint-availabletime extension. The url element must contain a URI that points to the Structure Definition that formally defines this extension.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.68.1 Extension: ContactPointAvailableTime - Detailed Descriptions, Element 34 (Extension.url)
**Grouping**: General/Cross-Resource

---
# REQ-172
**ID**: 33
**Summary**: Endpoint status SHALL be fixed to 'active'
**Requirement**: "status [SHALL have] Fixed Value: active"
**Context**: The Plan-Net Endpoint profile constrains the status element to always be 'active'. This means that all Endpoint resources conforming to this profile must have their status element set to 'active'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1 - Formal Views of Profile Content
**Grouping**: Endpoint

---
# REQ-173
**ID**: 34
**Summary**: Endpoint connectionType SHALL be present and bound to EndpointConnectionTypeVS
**Requirement**: "connectionType [cardinality] 1.1 [with] Binding: Endpoint Connection Types VS (extensible)"
**Context**: The connectionType element is mandatory (cardinality 1..1) and must be populated with a coded value from the EndpointConnectionTypeVS value set. The binding is extensible, meaning codes from the value set should be used if applicable, but other codes may be used if the value set does not cover the concept. Additionally, there is a minimum binding to MinEndpointConnectionTypeVS that a conformant system SHALL support all codes from.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1 - Formal Views of Profile Content
**Grouping**: Endpoint

---
# REQ-174
**ID**: 35
**Summary**: Endpoint connectionType SHALL support minimum value set codes
**Requirement**: "connectionType [has] Additional Bindings: Minimum Endpoint Connection Types VS [with purpose] Min Binding (The minimum allowable value set - any conformant system SHALL support all these codes)"
**Context**: In addition to the extensible binding to EndpointConnectionTypeVS, systems must support all codes from the MinEndpointConnectionTypeVS as a minimum binding. This ensures baseline interoperability for commonly used connection types.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1.1 - Terminology Bindings
**Grouping**: Endpoint

---
# REQ-175
**ID**: 36
**Summary**: Endpoint payloadType SHALL be present and bound to EndpointPayloadTypeVS
**Requirement**: "payloadType [cardinality] 1.1 [with] Binding: Endpoint Payload Types VS (extensible)"
**Context**: The payloadType element is mandatory (cardinality 1..1) and describes the acceptable content that can be communicated on the endpoint. It must be populated with a CodeableConcept from the EndpointPayloadTypeVS value set. The binding is extensible.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1 - Formal Views of Profile Content
**Grouping**: Endpoint

---
# REQ-176
**ID**: 37
**Summary**: Endpoint address SHALL be present
**Requirement**: "address [cardinality] 1.1 [type] url [description] The technical base address for connecting to this endpoint"
**Context**: The address element is mandatory (cardinality 1..1) and must contain the URI that describes the actual end-point to connect to. This is the technical base address required for electronic communication with the endpoint.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1 - Formal Views of Profile Content
**Grouping**: Endpoint

---
# REQ-177
**ID**: 38
**Summary**: Endpoint contact.system SHALL use required ContactPointSystem value set
**Requirement**: "contact.system [has] Binding: ContactPointSystem (required)"
**Context**: When the contact.system element is populated within the Endpoint.contact element, it must use a code from the required ContactPointSystem value set (phone, fax, email, pager, url, sms, other). This ensures standardized representation of contact mechanisms.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies if contact.system is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1.1 - Terminology Bindings
**Grouping**: Endpoint

---
# REQ-178
**ID**: 39
**Summary**: Endpoint contact.use SHALL use required ContactPointUse value set
**Requirement**: "contact.use [has] Binding: ContactPointUse (required)"
**Context**: When the contact.use element is populated within the Endpoint.contact element, it must use a code from the required ContactPointUse value set (home, work, temp, old, mobile). This identifies the purpose for the contact point.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies if contact.use is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1.1 - Terminology Bindings
**Grouping**: Endpoint

---
# REQ-179
**ID**: 40
**Summary**: Endpoint payloadMimeType SHALL use required Mime Types value set
**Requirement**: "payloadMimeType [has] Binding: Mime Types (required)"
**Context**: When the payloadMimeType element is populated, it must use a valid mime type code from the required Mime Types value set. This specifies the mime type to send the payload in (e.g., application/fhir+xml, application/fhir+json).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies if payloadMimeType is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1.1 - Terminology Bindings
**Grouping**: Endpoint

---
# REQ-180
**ID**: 41
**Summary**: Endpoint managingOrganization SHALL reference Plan-Net Organization if provided
**Requirement**: "managingOrganization [cardinality] 0.1 [type] Reference(Plan-Net Organization)"
**Context**: When the managingOrganization element is populated, it must be a reference to a Plan-Net Organization resource. This identifies the organization that manages the endpoint, even if another organization is hosting it.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies if managingOrganization is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1.1 - Formal Views of Profile Content
**Grouping**: Endpoint

---
# REQ-181
**ID**: 42
**Summary**: OrganizationAffiliation active element must be present and valued as true
**Requirement**: "[OrganizationAffiliation.active] Control 1.1 [with] Pattern Value `true`"
**Context**: The PlannetOrganizationAffiliation profile requires that the active element be present (cardinality 1..1) and have a pattern value of true, indicating that the organization affiliation record must be in active use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 18 (Snapshot), element 38 (Key Elements)
**Grouping**: Organization

---
# REQ-182
**ID**: 43
**Summary**: OrganizationAffiliation must have either organization or participatingOrganization
**Requirement**: "PlannetOrganizationAffiliation.organization or PlannetOrganizationAffiliation.participatingOrganization (`organization.exists() or participatingOrganization.exists()`)"
**Context**: The PlannetOrganizationAffiliation profile includes an invariant constraint (organization-or-participatingOrganization) requiring that at least one of organization or participatingOrganization must be present in the resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, Invariants
**Grouping**: Organization

---
# REQ-183
**ID**: 44
**Summary**: OrganizationAffiliation identifier.type must be supported
**Requirement**: "[OrganizationAffiliation.identifier.type] Must Support true"
**Context**: The identifier.type element, which provides a coded type for the identifier, must be supported in implementations of the PlannetOrganizationAffiliation profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 14 (Key Elements), element 28 (Snapshot)
**Grouping**: Organization

---
# REQ-184
**ID**: 45
**Summary**: OrganizationAffiliation identifier.value must be supported
**Requirement**: "[OrganizationAffiliation.identifier.value] Must Support true"
**Context**: The identifier.value element, which contains the actual unique identifier value, must be supported in implementations of the PlannetOrganizationAffiliation profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 16 (Key Elements), element 32 (Snapshot)
**Grouping**: Organization

---
# REQ-185
**ID**: 46
**Summary**: OrganizationAffiliation period must be supported
**Requirement**: "[OrganizationAffiliation.period] Must Support true"
**Context**: The period element, which defines the time period during which the participatingOrganization is affiliated with the primary organization, must be supported in implementations of the PlannetOrganizationAffiliation profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 20 (Key Elements), element 40 (Snapshot)
**Grouping**: Organization

---
# REQ-186
**ID**: 47
**Summary**: OrganizationAffiliation organization must reference Plan-Net Organization and be supported
**Requirement**: "[OrganizationAffiliation.organization] Type [Reference]([Plan-Net Organization]) [and] Must Support true"
**Context**: The organization element must reference a Plan-Net Organization profile and must be supported in implementations of the PlannetOrganizationAffiliation profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 22 (Key Elements), element 42 (Snapshot)
**Grouping**: Organization

---
# REQ-187
**ID**: 48
**Summary**: OrganizationAffiliation participatingOrganization must reference Plan-Net Organization and be supported
**Requirement**: "[OrganizationAffiliation.participatingOrganization] Type [Reference]([Plan-Net Organization]) [and] Must Support true"
**Context**: The participatingOrganization element must reference a Plan-Net Organization profile and must be supported in implementations of the PlannetOrganizationAffiliation profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 24 (Key Elements), element 44 (Snapshot)
**Grouping**: Organization

---
# REQ-188
**ID**: 49
**Summary**: OrganizationAffiliation network must reference Plan-Net Network and be supported
**Requirement**: "[OrganizationAffiliation.network] Type [Reference]([Plan-Net Network]) [and] Must Support true"
**Context**: The network element, which references the health insurance provider network, must reference a Plan-Net Network profile and must be supported in implementations of the PlannetOrganizationAffiliation profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 26 (Key Elements), element 46 (Snapshot)
**Grouping**: Organization

---
# REQ-189
**ID**: 50
**Summary**: OrganizationAffiliation code must be bound to OrganizationAffiliationRoleVS and be supported
**Requirement**: "[OrganizationAffiliation.code] Unless not suitable, these codes SHALL be taken from [OrganizationAffiliation Roles]([extensible]) [and] Must Support true"
**Context**: The code element, which defines the role the participatingOrganization plays, must use codes from the OrganizationAffiliationRoleVS value set with extensible binding and must be supported in implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 28 (Key Elements), element 48 (Snapshot)
**Grouping**: Organization

---
# REQ-190
**ID**: 51
**Summary**: OrganizationAffiliation specialty must be bound to SpecialtiesVS and be supported
**Requirement**: "[OrganizationAffiliation.specialty] The codes SHALL be taken from [Specialties VS]([required]) [and] Must Support true"
**Context**: The specialty element, which defines the specific specialty of the participatingOrganization in the context of the role, must use codes from the SpecialtiesVS value set with required binding and must be supported in implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 30 (Key Elements), element 50 (Snapshot)
**Grouping**: Organization

---
# REQ-191
**ID**: 52
**Summary**: OrganizationAffiliation location must reference Plan-Net Location and be supported
**Requirement**: "[OrganizationAffiliation.location] Type [Reference]([Plan-Net Location]) [and] Must Support true"
**Context**: The location element, which identifies the locations at which the role occurs, must reference a Plan-Net Location profile and must be supported in implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 32 (Key Elements), element 52 (Snapshot)
**Grouping**: Organization

---
# REQ-192
**ID**: 53
**Summary**: OrganizationAffiliation healthcareService must reference Plan-Net HealthcareService and be supported
**Requirement**: "[OrganizationAffiliation.healthcareService] Type [Reference]([Plan-Net HealthcareService]) [and] Must Support true"
**Context**: The healthcareService element, which identifies healthcare services provided through the role, must reference a Plan-Net HealthcareService profile and must be supported in implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 34 (Key Elements), element 54 (Snapshot)
**Grouping**: Organization

---
# REQ-193
**ID**: 54
**Summary**: OrganizationAffiliation telecom and child elements must be supported
**Requirement**: "[OrganizationAffiliation.telecom, telecom.system, telecom.value, telecom.rank] Must Support true"
**Context**: The telecom element and its child elements (system, value, rank) which provide contact details at the participatingOrganization relevant to the affiliation, must be supported in implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, elements 36-44 (Key Elements), elements 56-68 (Snapshot)
**Grouping**: Organization

---
# REQ-194
**ID**: 55
**Summary**: OrganizationAffiliation endpoint must reference Plan-Net Endpoint and be supported
**Requirement**: "[OrganizationAffiliation.endpoint] Type [Reference]([Plan-Net Endpoint]) [and] Must Support true"
**Context**: The endpoint element, which provides technical endpoints for accessing services operated for this role, must reference a Plan-Net Endpoint profile and must be supported in implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1 Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions, element 46 (Key Elements), element 72 (Snapshot)
**Grouping**: Organization

---
# REQ-195
**ID**: 56
**Summary**: Qualification extension code element binding requirement
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html)([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/SpecialtyAndDegreeLicenseCertificateVS`)"
**Context**: This requirement applies to the code element within the qualification extension. The code value[x] element must use codes from the Specialties, Degrees, Licenses, and Certificates Value Set with extensible binding strength, meaning that if a suitable code exists in the value set, it SHALL be used.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable, the codes SHALL be taken from the specified value set
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-196
**ID**: 57
**Summary**: Qualification extension status element binding requirement
**Requirement**: "The codes SHALL be taken from [Qualification Status VS](ValueSet-QualificationStatusVS.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/QualificationStatusVS`)"
**Context**: This requirement applies to the status element within the qualification extension. The status value[x] element must use codes from the Qualification Status Value Set with required binding strength, meaning codes must come from this value set only.
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
# REQ-197
**ID**: 58
**Summary**: Qualification extension whereValid element binding requirement
**Requirement**: "The codes SHALL be taken from [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU7/ValueSet-us-core-usps-state.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state`)"
**Context**: This requirement applies to the whereValid element within the qualification extension. The whereValid value[x] element, when provided as a CodeableConcept, must use codes from the USPS Two Letter Alphabetic Codes Value Set with required binding strength.
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
# REQ-198
**ID**: 59
**Summary**: Qualification extension definition SHALL requirement
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the url element within the qualification extension and its sub-extensions. Each url element must contain a URI that points to the Structure Definition that defines that particular extension element.
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
# REQ-199
**ID**: 60
**Summary**: Extension governance requirements for definition
**Requirement**: "Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
**Context**: This requirement applies to all extensions, including the qualification extension. Any implementer defining an extension must meet a specific set of requirements as part of the extension definition process, following FHIR governance rules for extensions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.77.1 Extension: Qualification - Detailed Descriptions
**Grouping**: General/Cross-Resource

---
# REQ-200
**ID**: 61
**Summary**: OrganizationAffiliation active element cardinality and pattern requirement
**Requirement**: "OrganizationAffiliation.active [cardinality] 1..1 [with] Required Pattern: true"
**Context**: The Plan-Net OrganizationAffiliation profile requires that the active element must be present (cardinality 1..1) and must have a value of true. This ensures that only active organization affiliation records are represented in conformant instances.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1 - Plan-Net OrganizationAffiliation Profile
**Grouping**: General/Cross-Resource

---
# REQ-201
**ID**: 62
**Summary**: OrganizationAffiliation organization or participatingOrganization constraint
**Requirement**: "PlannetOrganizationAffiliation.organization or PlannetOrganizationAffiliation.participatingOrganization: organization.exists() or participatingOrganization.exists()"
**Context**: This is a constraint (organization-or-participatingOrganization) on the OrganizationAffiliation resource requiring that either the organization element or the participatingOrganization element (or both) must be present. This ensures that the affiliation has at least one organization reference.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.2 - Constraints
**Grouping**: General/Cross-Resource

---
# REQ-202
**ID**: 63
**Summary**: OrganizationAffiliation.identifier.use value set binding
**Requirement**: "OrganizationAffiliation.identifier.use [binding conformance] required [to] IdentifierUse http://hl7.org/fhir/ValueSet/identifier-use"
**Context**: The identifier.use element in OrganizationAffiliation must use a code from the required IdentifierUse value set to indicate the purpose of the identifier.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-203
**ID**: 64
**Summary**: OrganizationAffiliation.identifier.type value set binding
**Requirement**: "OrganizationAffiliation.identifier.type [binding conformance] extensible [to] Identifier Type Codes http://hl7.org/fhir/ValueSet/identifier-type"
**Context**: The identifier.type element should use codes from the Identifier Type Codes value set, but may use other codes if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-204
**ID**: 65
**Summary**: OrganizationAffiliation.code value set binding
**Requirement**: "OrganizationAffiliation.code [binding conformance] extensible [to] OrganizationAffiliationRoleVS http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/OrganizationAffiliationRoleVS"
**Context**: The code element defining the role the participatingOrganization plays should use codes from the OrganizationAffiliationRoleVS value set from this IG, but may use other codes if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-205
**ID**: 66
**Summary**: OrganizationAffiliation.specialty value set binding
**Requirement**: "OrganizationAffiliation.specialty [binding conformance] required [to] SpecialtiesVS http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/SpecialtiesVS"
**Context**: The specialty element indicating the specific specialty of the participatingOrganization must use a code from the required SpecialtiesVS value set from this IG.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-206
**ID**: 67
**Summary**: OrganizationAffiliation.telecom.system value set binding
**Requirement**: "OrganizationAffiliation.telecom.system [binding conformance] required [to] ContactPointSystem http://hl7.org/fhir/ValueSet/contact-point-system"
**Context**: The telecom.system element must use a code from the required ContactPointSystem value set to indicate the telecommunications form.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-207
**ID**: 68
**Summary**: OrganizationAffiliation.telecom.use value set binding
**Requirement**: "OrganizationAffiliation.telecom.use [binding conformance] required [to] ContactPointUse http://hl7.org/fhir/ValueSet/contact-point-use"
**Context**: The telecom.use element must use a code from the required ContactPointUse value set to indicate the purpose of the contact point.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.63.1.1.1 - Terminology Bindings
**Grouping**: General/Cross-Resource

---
# REQ-208
**ID**: 69
**Summary**: Organization SHALL at least have a name or an identifier
**Requirement**: "The organization SHALL at least have a name or an identifier, and possibly more than one"
**Context**: This is a fundamental constraint on the Organization resource profile (plannet-Network). It ensures that every organization instance can be identified either by a name or an identifier (or both). This applies to the base FHIR Organization resource and is inherited by the plannet-Network profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiability**: Yes
**Verifiability Details**: Automation - Validate that Organization resource instances contain at least one identifier or one name element with a value
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization element (invariant org-1)
**Grouping**: Organization

---
# REQ-209
**ID**: 70
**Summary**: If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986
**Requirement**: "If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986"
**Context**: This requirement applies to Organization.identifier.value. When an identifier value is expressed as a full URI, the corresponding identifier.system must be set to the specific URN value indicating RFC 3986 compliance.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when Organization.identifier.value contains a full URI
**Verifiability**: Yes
**Verifiability Details**: Automation - Check if identifier.value is a full URI format and verify system equals "urn:ietf:rfc:3986"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier.value
**Grouping**: Organization

---
# REQ-210
**ID**: 71
**Summary**: Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)"
**Context**: This is a general constraint on the use of modifier extensions within the Organization resource. Modifier extensions are allowed but must not alter the fundamental meaning of standard FHIR elements.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiability**: Yes
**Verifiability Details**: Attestation - Requires review of modifier extension definitions to confirm they do not change core element meanings
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.modifierExtension
**Grouping**: Organization

---
# REQ-211
**ID**: 72
**Summary**: NPI must be 10 digits
**Requirement**: "NPI must be 10 digits"
**Context**: This requirement applies to the Organization.identifier:NPI slice. When an NPI (National Provider Identifier) is provided for an organization, it must conform to the standard 10-digit format. The invariant us-core-16 enforces this with the expression: value.matches('^[0-9]{10}$')
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when Organization.identifier:NPI is present
**Verifiability**: Yes
**Verifiability Details**: Automation - Validate that NPI identifier value matches the regular expression '^[0-9]{10}$'
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier:NPI (invariant us-core-16)
**Grouping**: Organization

---
# REQ-212
**ID**: 73
**Summary**: NPI check digit must be valid (Luhn algorithm check)
**Requirement**: "NPI check digit must be valid (Luhn algorithm check)"
**Context**: This requirement applies to Organization.identifier:NPI. Beyond being 10 digits, the NPI must pass Luhn algorithm validation. The invariant us-core-17 provides the specific calculation formula to verify the check digit.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when Organization.identifier:NPI is present
**Verifiability**: Yes
**Verifiability Details**: Automation - Apply Luhn algorithm to validate NPI check digit using the formula provided in invariant us-core-17
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier:NPI (invariant us-core-17)
**Grouping**: Organization

---
# REQ-213
**ID**: 74
**Summary**: CLIA number must be 10 digits with a letter "D" in third position
**Requirement**: "CLIA number must be 10 digits with a letter 'D' in third position"
**Context**: This requirement applies to Organization.identifier:CLIA (Clinical Laboratory Improvement Amendments identifier). The format must be exactly 10 characters: 2 digits, followed by the letter 'D', followed by 7 digits. The invariant us-core-18 enforces this with the expression: value.matches('^[0-9]{2}D[0-9]{7}$')
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when Organization.identifier:CLIA is present
**Verifiability**: Yes
**Verifiability Details**: Automation - Validate that CLIA identifier value matches the regular expression '^[0-9]{2}D[0-9]{7}$'
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier:CLIA (invariant us-core-18)
**Grouping**: Organization

---
# REQ-214
**ID**: 75
**Summary**: NAIC must be 5 digits
**Requirement**: "NAIC must be 5 digits"
**Context**: This requirement applies to Organization.identifier:NAIC (National Association of Insurance Commissioners code). When a NAIC code is provided for an organization, it must be exactly 5 numeric digits. The invariant us-core-19 enforces this with the expression: value.matches('^[0-9]{5}$')
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when Organization.identifier:NAIC is present
**Verifiability**: Yes
**Verifiability Details**: Automation - Validate that NAIC identifier value matches the regular expression '^[0-9]{5}$'
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.identifier:NAIC (invariant us-core-19)
**Grouping**: Organization

---
# REQ-215
**ID**: 76
**Summary**: Organization active status must be true for plannet-Network
**Requirement**: "[Organization.active has a] Fixed Value `true`"
**Context**: For the plannet-Network profile, the active element is constrained to always be true. This indicates that network organization records in this profile must represent active/current networks, not inactive or historical ones. The cardinality is also set to 1..1, making this element required.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiability**: Yes
**Verifiability Details**: Automation - Verify that Organization.active element exists and has the value true
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.active
**Grouping**: Organization

---
# REQ-216
**ID**: 77
**Summary**: Organization type SHALL be bound to NetworkTypeVS value set
**Requirement**: "The codes SHALL be taken from [Network Type VS]"
**Context**: For the plannet-Network profile, Organization.type is required (cardinality 1..1) and must use codes from the NetworkTypeVS value set with required binding strength. This ensures that network organizations are consistently classified using approved network type codes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiability**: Yes
**Verifiability Details**: Automation - Validate that Organization.type contains a code from the NetworkTypeVS value set
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.type
**Grouping**: Organization

---
# REQ-217
**ID**: 78
**Summary**: The telecom of an organization can never be of use 'home'
**Requirement**: "The telecom of an organization can never be of use 'home'"
**Context**: This constraint (invariant org-3) applies to Organization.telecom elements. Organization contact points should be business-related and cannot have a 'use' code of 'home'. The expression where(use = 'home').empty() enforces this.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when Organization.telecom elements are present
**Verifiability**: Yes
**Verifiability Details**: Automation - Verify that no Organization.telecom element has use='home'
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.telecom (invariant org-3)
**Grouping**: Organization

---
# REQ-218
**ID**: 79
**Summary**: An address of an organization can never be of use 'home'
**Requirement**: "An address of an organization can never be of use 'home'"
**Context**: This constraint (invariant org-2) applies to Organization.address elements. Similar to telecom, organization addresses must be business-related and cannot have a 'use' code of 'home'. The expression where(use = 'home').empty() enforces this.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when Organization.address elements are present
**Verifiability**: Yes
**Verifiability Details**: Automation - Verify that no Organization.address element has use='home'
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.address (invariant org-2)
**Grouping**: Organization

---
# REQ-219
**ID**: 80
**Summary**: Organization partOf is required for plannet-Network and must reference Plan-Net Organization
**Requirement**: "[Organization.partOf has] Control 1.1 [and] Type Reference([Plan-Net Organization])"
**Context**: For the plannet-Network profile, the partOf element is required (cardinality 1..1) and must reference another Plan-Net Organization resource. This represents the organization that manages the network. The reference is constrained to only allow Plan-Net Organization profiles, not the base FHIR Organization.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiability**: Yes
**Verifiability Details**: Automation - Verify that Organization.partOf element is present and references a valid Plan-Net Organization resource
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.partOf
**Grouping**: Organization

---
# REQ-220
**ID**: 81
**Summary**: Organization name is required for plannet-Network
**Requirement**: "[Organization.name has] Control 1..1"
**Context**: For the plannet-Network profile, the name element is required with cardinality 1..1. Every network organization must have exactly one name. This is stricter than the base FHIR Organization which makes name optional (but still requires either name or identifier per invariant org-1).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiability**: Yes
**Verifiability Details**: Automation - Verify that Organization.name element is present and contains a value
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.name
**Grouping**: Organization

---
# REQ-221
**ID**: 82
**Summary**: Organization endpoint must reference Plan-Net Endpoint for plannet-Network
**Requirement**: "[Organization.endpoint has] Type Reference([Plan-Net Endpoint])"
**Context**: For the plannet-Network profile, when Organization.endpoint is provided, it must reference a Plan-Net Endpoint resource (not the base FHIR Endpoint). This constrains the reference to use the specific Plan-Net Endpoint profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when Organization.endpoint is present
**Verifiability**: Yes
**Verifiability Details**: Automation - Verify that any Organization.endpoint reference points to a resource conforming to the Plan-Net Endpoint profile
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions, Organization.endpoint
**Grouping**: Organization

---
# REQ-222
**ID**: 83
**Summary**: HealthcareService active element cardinality requirement
**Requirement**: "HealthcareService.active [Control: 1.1]"
**Context**: The PlanNet HealthcareService profile requires that the active element has a cardinality of 1..1, meaning it must be present and can only appear once. This element indicates whether the HealthcareService record is in active use and has a pattern value of 'true'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 40
**Grouping**: HealthcareService

---
# REQ-223
**ID**: 84
**Summary**: HealthcareService active element pattern value requirement
**Requirement**: "HealthcareService.active [Pattern Value: `true`]"
**Context**: The PlanNet HealthcareService profile specifies that when the active element is present, it must have a value of 'true'. This is a modifier element that can indicate whether a record should be treated as valid.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 40
**Grouping**: HealthcareService

---
# REQ-224
**ID**: 85
**Summary**: HealthcareService category element cardinality requirement
**Requirement**: "HealthcareService.category [Control: 1.*]"
**Context**: The PlanNet HealthcareService profile requires that at least one category element must be present (cardinality 1..*). The category identifies the broad category of service being performed or delivered.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 44
**Grouping**: HealthcareService

---
# REQ-225
**ID**: 86
**Summary**: HealthcareService plan-net-category slice binding requirement
**Requirement**: "HealthcareService.category:plan-net-category [Binding: The codes SHALL be taken from Healthcare Service CategoryVS (required to http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/HealthcareServiceCategoryVS)]"
**Context**: When the plan-net-category slice of the category element is used, codes must be taken from the specified Healthcare Service CategoryVS value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 46
**Grouping**: HealthcareService

---
# REQ-226
**ID**: 87
**Summary**: HealthcareService type element binding requirement
**Requirement**: "HealthcareService.type [Binding: Unless not suitable, these codes SHALL be taken from HealthcareService Types VS (extensible to http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/HealthcareServiceTypeVS)]"
**Context**: The type element describes the specific type of service that may be delivered or performed. Codes should be taken from the HealthcareServiceTypeVS value set unless not suitable, with extensible binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 48
**Grouping**: HealthcareService

---
# REQ-227
**ID**: 88
**Summary**: HealthcareService specialty element binding requirement
**Requirement**: "HealthcareService.specialty [Binding: The codes SHALL be taken from Specialties VS (required to http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/SpecialtiesVS)]"
**Context**: The specialty element represents the collection of specialties handled by the service site. Codes must be taken from the SpecialtiesVS value set with required binding strength.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 50
**Grouping**: HealthcareService

---
# REQ-228
**ID**: 89
**Summary**: HealthcareService notAvailable description element cardinality requirement
**Requirement**: "HealthcareService.notAvailable.description [Control: 1.1]"
**Context**: When the notAvailable element is used to indicate times when the HealthcareService is not available, a description element must be present (cardinality 1..1) explaining the reason to the user.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When notAvailable element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 132
**Grouping**: HealthcareService

---
# REQ-229
**ID**: 90
**Summary**: HealthcareService identifier type must support requirement
**Requirement**: "HealthcareService.identifier.type [Must Support: true]"
**Context**: Implementations must support the identifier.type element, which provides a coded type for the identifier that can be used to determine which identifier to use for a specific purpose.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 30
**Grouping**: HealthcareService

---
# REQ-230
**ID**: 91
**Summary**: HealthcareService identifier value must support requirement
**Requirement**: "HealthcareService.identifier.value [Must Support: true]"
**Context**: Implementations must support the identifier.value element, which contains the portion of the identifier typically relevant to the user and which is unique within the context of the system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 34
**Grouping**: HealthcareService

---
# REQ-231
**ID**: 92
**Summary**: HealthcareService providedBy must support requirement
**Requirement**: "HealthcareService.providedBy [Must Support: true]"
**Context**: Implementations must support the providedBy element, which references the organization that provides this healthcare service.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 42
**Grouping**: HealthcareService

---
# REQ-232
**ID**: 93
**Summary**: HealthcareService category must support requirement
**Requirement**: "HealthcareService.category [Must Support: true]"
**Context**: Implementations must support the category element, which identifies the broad category of service being performed or delivered.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 44
**Grouping**: HealthcareService

---
# REQ-233
**ID**: 94
**Summary**: HealthcareService type must support requirement
**Requirement**: "HealthcareService.type [Must Support: true]"
**Context**: Implementations must support the type element, which describes the specific type of service that may be delivered or performed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 48
**Grouping**: HealthcareService

---
# REQ-234
**ID**: 95
**Summary**: HealthcareService specialty must support requirement
**Requirement**: "HealthcareService.specialty [Must Support: true]"
**Context**: Implementations must support the specialty element, which represents the collection of specialties handled by the service site.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 50
**Grouping**: HealthcareService

---
# REQ-235
**ID**: 96
**Summary**: HealthcareService location must support requirement
**Requirement**: "HealthcareService.location [Must Support: true]"
**Context**: Implementations must support the location element, which references the location(s) where this healthcare service may be provided.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 52
**Grouping**: HealthcareService

---
# REQ-236
**ID**: 97
**Summary**: HealthcareService name must support requirement
**Requirement**: "HealthcareService.name [Must Support: true]"
**Context**: Implementations must support the name element, which provides a description of the service as it would be presented to a consumer while searching.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 54
**Grouping**: HealthcareService

---
# REQ-237
**ID**: 98
**Summary**: HealthcareService comment must support requirement
**Requirement**: "HealthcareService.comment [Must Support: true]"
**Context**: Implementations must support the comment element, which provides additional description and/or any specific issues not covered by other attributes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 56
**Grouping**: HealthcareService

---
# REQ-238
**ID**: 99
**Summary**: HealthcareService telecom must support requirement
**Requirement**: "HealthcareService.telecom [Must Support: true]"
**Context**: Implementations must support the telecom element, which contains contact information related to this specific healthcare service.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 62
**Grouping**: HealthcareService

---
# REQ-239
**ID**: 100
**Summary**: HealthcareService telecom system must support requirement
**Requirement**: "HealthcareService.telecom.system [Must Support: true]"
**Context**: Implementations must support the telecom.system element, which specifies the telecommunications form for the contact point.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 72
**Grouping**: HealthcareService

---
# REQ-240
**ID**: 101
**Summary**: HealthcareService telecom value must support requirement
**Requirement**: "HealthcareService.telecom.value [Must Support: true]"
**Context**: Implementations must support the telecom.value element, which contains the actual contact point details in a form meaningful to the designated communication system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 74
**Grouping**: HealthcareService

---
# REQ-241
**ID**: 102
**Summary**: HealthcareService telecom contactpoint-availabletime extension must support requirement
**Requirement**: "HealthcareService.telecom.extension:contactpoint-availabletime [Must Support: true]"
**Context**: Implementations must support the contactpoint-availabletime extension, which represents the days and times a contact point is available.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 68
**Grouping**: HealthcareService

---
# REQ-242
**ID**: 103
**Summary**: HealthcareService telecom via-intermediary extension must support requirement
**Requirement**: "HealthcareService.telecom.extension:via-intermediary [Must Support: true]"
**Context**: Implementations must support the via-intermediary extension, which provides a reference to an alternative point of contact for this organization.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 70
**Grouping**: HealthcareService

---
# REQ-243
**ID**: 104
**Summary**: HealthcareService coverageArea must support requirement
**Requirement**: "HealthcareService.coverageArea [Must Support: true]"
**Context**: Implementations must support the coverageArea element, which indicates the location(s) that this service is available to (not where the service is provided).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 82
**Grouping**: HealthcareService

---
# REQ-244
**ID**: 105
**Summary**: HealthcareService appointmentRequired must support requirement
**Requirement**: "HealthcareService.appointmentRequired [Must Support: true]"
**Context**: Implementations must support the appointmentRequired element, which indicates whether an appointment is required for access to this service.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 106
**Grouping**: HealthcareService

---
# REQ-245
**ID**: 106
**Summary**: HealthcareService availableTime must support requirement
**Requirement**: "HealthcareService.availableTime [Must Support: true]"
**Context**: Implementations must support the availableTime element, which provides a collection of times that the Service Site is available.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 108
**Grouping**: HealthcareService

---
# REQ-246
**ID**: 107
**Summary**: HealthcareService availableTime daysOfWeek must support requirement
**Requirement**: "HealthcareService.availableTime.daysOfWeek [Must Support: true]"
**Context**: Implementations must support the daysOfWeek element within availableTime, which indicates which days of the week are available between the start and end times.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 116
**Grouping**: HealthcareService

---
# REQ-247
**ID**: 108
**Summary**: HealthcareService availableTime allDay must support requirement
**Requirement**: "HealthcareService.availableTime.allDay [Must Support: true]"
**Context**: Implementations must support the allDay element within availableTime, which indicates if the service is always available (e.g., 24 hour service).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 118
**Grouping**: HealthcareService

---
# REQ-248
**ID**: 109
**Summary**: HealthcareService availableTime availableStartTime must support requirement
**Requirement**: "HealthcareService.availableTime.availableStartTime [Must Support: true]"
**Context**: Implementations must support the availableStartTime element within availableTime, which indicates the opening time of day (ignored if allDay = true).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 120
**Grouping**: HealthcareService

---
# REQ-249
**ID**: 110
**Summary**: HealthcareService availableTime availableEndTime must support requirement
**Requirement**: "HealthcareService.availableTime.availableEndTime [Must Support: true]"
**Context**: Implementations must support the availableEndTime element within availableTime, which indicates the closing time of day (ignored if allDay = true).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 122
**Grouping**: HealthcareService

---
# REQ-250
**ID**: 111
**Summary**: HealthcareService notAvailable must support requirement
**Requirement**: "HealthcareService.notAvailable [Must Support: true]"
**Context**: Implementations must support the notAvailable element, which indicates when the HealthcareService is not available during a period of time due to the provided reason.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 124
**Grouping**: HealthcareService

---
# REQ-251
**ID**: 112
**Summary**: HealthcareService notAvailable description must support requirement
**Requirement**: "HealthcareService.notAvailable.description [Must Support: true]"
**Context**: Implementations must support the description element within notAvailable, which provides the reason that can be presented to the user as to why this time is not available.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 132
**Grouping**: HealthcareService

---
# REQ-252
**ID**: 113
**Summary**: HealthcareService notAvailable during must support requirement
**Requirement**: "HealthcareService.notAvailable.during [Must Support: true]"
**Context**: Implementations must support the during element within notAvailable, which indicates the period when the service is not available (seasonally or for a public holiday).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 134
**Grouping**: HealthcareService

---
# REQ-253
**ID**: 114
**Summary**: HealthcareService availabilityExceptions must support requirement
**Requirement**: "HealthcareService.availabilityExceptions [Must Support: true]"
**Context**: Implementations must support the availabilityExceptions element, which provides a description of site availability exceptions (e.g., public holiday availability).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 136
**Grouping**: HealthcareService

---
# REQ-254
**ID**: 115
**Summary**: HealthcareService endpoint must support requirement
**Requirement**: "HealthcareService.endpoint [Must Support: true]"
**Context**: Implementations must support the endpoint element, which provides technical endpoints providing access to services operated for the specific healthcare services.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 138
**Grouping**: HealthcareService

---
# REQ-255
**ID**: 116
**Summary**: HealthcareService newpatients extension must support requirement
**Requirement**: "HealthcareService.extension:newpatients [Must Support: true]"
**Context**: Implementations must support the newpatients extension, which indicates whether new patients are being accepted in general or from a specific network.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 16
**Grouping**: HealthcareService

---
# REQ-256
**ID**: 117
**Summary**: HealthcareService deliverymethod extension must support requirement
**Requirement**: "HealthcareService.extension:deliverymethod [Must Support: true]"
**Context**: Implementations must support the deliverymethod extension, which describes the service delivery method (e.g., if service delivery is virtual, one or more delivery modalities should be specified).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: PlannetHealthcareService - Detailed Descriptions - Element 18
**Grouping**: HealthcareService

---
# REQ-257
**ID**: 118
**Summary**: Practitioner identifier cardinality requirement
**Requirement**: "An identifier that applies to this person in this role. [Control: 1.0.*]"
**Context**: The Practitioner resource profile specifies that at least one identifier must be present for the practitioner. This is a required element with minimum cardinality of 1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.identifier
**Grouping**: Practitioner

---
# REQ-258
**ID**: 119
**Summary**: NPI identifier system requirement
**Requirement**: "NPI must be supported as the identifier system in the US"
**Context**: For Practitioner identifiers in US implementations, the National Provider Identifier (NPI) must be supported as one of the identifier systems. This is documented in the comments section of the identifier element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When operating in the US jurisdiction
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.identifier
**Grouping**: Practitioner

---
# REQ-259
**ID**: 120
**Summary**: Practitioner identifier system cardinality requirement
**Requirement**: "Establishes the namespace for the value - that is, a URL that describes a set values that are unique. [Control: 1.1]"
**Context**: The system element of Practitioner.identifier must be present with cardinality 1..1, establishing the namespace for the identifier value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.identifier.system
**Grouping**: Practitioner

---
# REQ-260
**ID**: 121
**Summary**: Practitioner identifier value cardinality requirement
**Requirement**: "The portion of the identifier typically relevant to the user and which is unique within the context of the system. [Control: 1.1]"
**Context**: The value element of Practitioner.identifier must be present with cardinality 1..1, providing the unique identifier value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.identifier.value
**Grouping**: Practitioner

---
# REQ-261
**ID**: 122
**Summary**: Practitioner identifier value case sensitivity requirement
**Requirement**: "Identifier.value is to be treated as case sensitive unless knowledge of the Identifier.system allows the processer to be confident that non-case-sensitive processing is safe."
**Context**: Systems processing Practitioner identifiers must treat the identifier value as case sensitive by default.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless knowledge of the Identifier.system allows the processor to be confident that non-case-sensitive processing is safe
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.identifier.value
**Grouping**: Practitioner

---
# REQ-262
**ID**: 123
**Summary**: Practitioner identifier full URI system requirement
**Requirement**: "If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986."
**Context**: When the identifier value is expressed as a full URI, the system element must be set to urn:ietf:rfc:3986.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If the value is a full URI
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.identifier.value
**Grouping**: Practitioner

---
# REQ-263
**ID**: 124
**Summary**: NPI identifier format validation requirement
**Requirement**: "NPI must be 10 digits (`value.matches('^[0-9]{10}$')`)"
**Context**: National Provider Identifier (NPI) values in the NPI slice must conform to the 10-digit format requirement specified in the us-core-16 invariant.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When using the NPI identifier slice
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.identifier:NPI
**Grouping**: Practitioner

---
# REQ-264
**ID**: 125
**Summary**: NPI identifier Luhn algorithm check digit validation requirement
**Requirement**: "NPI check digit must be valid (Luhn algorithm check)"
**Context**: National Provider Identifier (NPI) values must pass the Luhn algorithm check digit validation as specified in the us-core-17 invariant.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When using the NPI identifier slice
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.identifier:NPI
**Grouping**: Practitioner

---
# REQ-265
**ID**: 126
**Summary**: Practitioner active status cardinality requirement
**Requirement**: "Whether this practitioner's record is in active use. [Control: 1.1]"
**Context**: The active element must be present in the Practitioner resource with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.active
**Grouping**: Practitioner

---
# REQ-266
**ID**: 127
**Summary**: Practitioner name cardinality requirement
**Requirement**: "The name(s) associated with the practitioner. [Control: 1.*]"
**Context**: The Practitioner resource must include at least one name element, with minimum cardinality of 1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.name
**Grouping**: Practitioner

---
# REQ-267
**ID**: 128
**Summary**: Practitioner name family element cardinality requirement
**Requirement**: "The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father. [Control: 1.1]"
**Context**: The family name element within Practitioner.name must be present with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.name.family
**Grouping**: Practitioner

---
# REQ-268
**ID**: 129
**Summary**: Practitioner name text and parts synchronization requirement
**Requirement**: "Applications updating a name SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part."
**Context**: When updating a Practitioner's name, if both the text representation and individual name parts are provided, applications must ensure the text does not contain content not found in the parts.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When both text and parts are present in the name element
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.name.text
**Grouping**: Practitioner

---
# REQ-269
**ID**: 130
**Summary**: Practitioner qualification code cardinality requirement
**Requirement**: "Coded representation of the qualification. [Control: 1.1]"
**Context**: The code element within Practitioner.qualification must be present with cardinality 1..1, providing a coded representation of the qualification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.qualification.code
**Grouping**: Practitioner

---
# REQ-270
**ID**: 131
**Summary**: Contained resource nested containment prohibition
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources (contained.contained.empty())"
**Context**: When a Practitioner resource is contained within another resource, it must not contain any nested contained resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If the resource is contained in another resource
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner (dom-2 invariant)
**Grouping**: Practitioner

---
# REQ-271
**ID**: 132
**Summary**: Contained resource reference requirement
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: Contained Practitioner resources must either be referenced from elsewhere in the containing resource or must themselves reference the containing resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If the resource is contained in another resource
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner (dom-3 invariant)
**Grouping**: Practitioner

---
# REQ-272
**ID**: 133
**Summary**: Contained resource meta.versionId and meta.lastUpdated prohibition
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (contained.meta.versionId.empty() and contained.meta.lastUpdated.empty())"
**Context**: Contained Practitioner resources must not include meta.versionId or meta.lastUpdated elements.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If a resource is contained in another resource
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner (dom-4 invariant)
**Grouping**: Practitioner

---
# REQ-273
**ID**: 134
**Summary**: Contained resource security label prohibition
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label (contained.meta.security.empty())"
**Context**: Contained Practitioner resources must not include security labels in the meta.security element.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If a resource is contained in another resource
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner (dom-5 invariant)
**Grouping**: Practitioner

---
# REQ-274
**ID**: 135
**Summary**: Modifier extensions meaning preservation requirement
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)."
**Context**: Any modifier extensions used in the Practitioner resource or its sub-elements must not alter the meaning of standard Resource or DomainResource elements.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.modifierExtension
**Grouping**: Practitioner

---
# REQ-275
**ID**: 136
**Summary**: Address text and parts synchronization requirement
**Requirement**: "Applications updating an address SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part."
**Context**: When updating a Practitioner's address, if both the text representation and individual address parts are provided, applications must ensure the text does not contain content not found in the parts.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When both text and parts are present in the address element
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile: PlannetPractitioner - Detailed Descriptions, Practitioner.address.text
**Grouping**: Practitioner

---
# REQ-276
**ID**: 137
**Summary**: Plan-Net Network organization active status must be true
**Requirement**: "Whether the organization's record is still in active use. [The] active [element has a] Fixed Value: true"
**Context**: The Plan-Net Network profile constrains the Organization resource to represent healthcare provider insurance networks. The active element is mandatory and must always be set to true, indicating that the network record is currently in active use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile
**Grouping**: Organization

---
# REQ-277
**ID**: 138
**Summary**: Plan-Net Network organization type must be from NetworkTypeVS value set
**Requirement**: "The kind(s) of organization that this is. [Organization.type has] Binding: Network Type VS (required)"
**Context**: The Plan-Net Network profile requires that the type element, which identifies the kind of organization, must be bound to the NetworkTypeVS value set with required conformance strength. This is a mandatory element (cardinality 1..1).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile
**Grouping**: Organization

---
# REQ-278
**ID**: 139
**Summary**: Plan-Net Network must have a name
**Requirement**: "A name associated with the organization. [Organization.name has cardinality] 1..1"
**Context**: The Plan-Net Network profile requires that each network organization must have a name. This is a mandatory element that identifies the network.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile
**Grouping**: Organization

---
# REQ-279
**ID**: 140
**Summary**: Plan-Net Network must reference the managing organization
**Requirement**: "The organization of which this organization forms a part. [Organization.partOf has cardinality] 1..1 [and type] Reference(Plan-Net Organization) [representing] The organization that manages this network"
**Context**: The Plan-Net Network profile requires that each network must reference the parent organization that manages the network through the partOf element. This is a mandatory reference to a Plan-Net Organization resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile
**Grouping**: Organization

---
# REQ-280
**ID**: 141
**Summary**: Plan-Net Network NPI identifier must be 10 digits
**Requirement**: "NPI must be 10 digits: value.matches('^[0-9]{10}$')"
**Context**: The Plan-Net Network profile includes an optional NPI identifier slice. When the NPI identifier is provided, it must conform to the constraint that the value must be exactly 10 digits.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If an NPI identifier is provided for the network organization
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization

---
# REQ-281
**ID**: 142
**Summary**: Plan-Net Network NPI identifier check digit must be valid
**Requirement**: "NPI check digit must be valid (Luhn algorithm check): (((select(value.substring(0,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(1,1).toInteger())+(select(value.substring(2,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(3,1).toInteger())+(select(value.substring(4,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(5,1).toInteger())+(select(value.substring(6,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(7,1).toInteger())+(select(value.substring(8,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(9,1).toInteger()) + 24)mod 10=0)"
**Context**: The Plan-Net Network profile includes an optional NPI identifier slice. When the NPI identifier is provided, it must pass the Luhn algorithm check to validate the check digit.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If an NPI identifier is provided for the network organization
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization

---
# REQ-282
**ID**: 143
**Summary**: Plan-Net Network CLIA identifier must be 10 digits with letter D in third position
**Requirement**: "CLIA number must be 10 digits with a letter 'D' in third position: value.matches('^[0-9]{2}D[0-9]{7}$')"
**Context**: The Plan-Net Network profile includes an optional CLIA identifier slice for laboratories. When the CLIA identifier is provided, it must conform to the constraint that requires exactly 10 characters with the letter 'D' in the third position.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If a CLIA identifier is provided for the network organization
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization

---
# REQ-283
**ID**: 144
**Summary**: Plan-Net Network NAIC identifier must be 5 digits
**Requirement**: "NAIC must be 5 digits: value.matches('^[0-9]{5}$')"
**Context**: The Plan-Net Network profile includes an optional NAIC identifier slice. When the NAIC identifier is provided, it must conform to the constraint that the value must be exactly 5 digits.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If a NAIC identifier is provided for the network organization
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization

---
# REQ-284
**ID**: 145
**Summary**: Plan-Net Network organization address use cannot be home
**Requirement**: "An address of an organization can never be of use 'home'"
**Context**: The Plan-Net Network profile constrains the address element such that if an address is provided, the use element cannot have the value 'home' as this is inappropriate for organizational addresses.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If an address is provided for the network organization
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1 Resource Profile
**Grouping**: Organization

---
# REQ-285
**ID**: 146
**Summary**: Plan-Net Network must have at least a name or identifier
**Requirement**: "The organization SHALL at least have a name or an identifier, and possibly more than one"
**Context**: The Plan-Net Network profile inherits the org-1 constraint from the base Organization resource, requiring that each network organization must have at least one name or identifier to ensure the organization can be identified.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization

---
# REQ-286
**ID**: 147
**Summary**: Location resource SHALL have status fixed to 'active'
**Requirement**: "Location.status [Control: 1.1] Fixed Value: `active`"
**Context**: The PlanNet Location profile constrains the Location resource to only allow an active status. This is a fixed value constraint meaning all Location resources conforming to this profile must have status='active'. This ensures only currently active locations are represented in the Plan-Net directory.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-287
**ID**: 148
**Summary**: Location resource SHALL include name element
**Requirement**: "Location.name [Control: 1.1] [Must Support: true] - Name of the location as used by humans. Does not need to be unique."
**Context**: The PlanNet Location profile requires that Location resources include a name element with cardinality 1..1 (required) and marked as Must Support. This ensures locations have a human-readable name that can be used for display and search purposes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-288
**ID**: 149
**Summary**: Location resource SHALL support identifier element
**Requirement**: "Location.identifier [Control: 0.*] [Must Support: true] - Unique code or number identifying the location to its users."
**Context**: The PlanNet Location profile marks the identifier element as Must Support, indicating that systems must be capable of processing location identifiers. Identifiers provide a unique business identifier for facilities or locations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-289
**ID**: 150
**Summary**: Location resource SHALL support identifier.type element
**Requirement**: "Location.identifier.type [Control: 0.1] [Must Support: true] - A coded type for the identifier that can be used to determine which identifier to use for a specific purpose."
**Context**: The PlanNet Location profile requires support for the identifier type element to allow systems to distinguish between different types of identifiers (e.g., official, temporary, secondary).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-290
**ID**: 151
**Summary**: Location resource SHALL support identifier.value element
**Requirement**: "Location.identifier.value [Control: 0.1] [Must Support: true] - The portion of the identifier typically relevant to the user and which is unique within the context of the system."
**Context**: The PlanNet Location profile requires support for the identifier value element to capture the actual identifier value that uniquely identifies the location within its system context.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-291
**ID**: 152
**Summary**: Location resource SHALL support alias element
**Requirement**: "Location.alias [Control: 0.*] [Must Support: true] - A list of alternate names that the location is known as, or was known as, in the past."
**Context**: The PlanNet Location profile requires support for location aliases to enable searching by previous or alternative names. This helps locate facilities that may have changed names over time.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-292
**ID**: 153
**Summary**: Location resource SHALL support description element
**Requirement**: "Location.description [Control: 0.1] [Must Support: true] - Description of the Location, which helps in finding or referencing the place."
**Context**: The PlanNet Location profile requires support for the description element to provide additional details about the location beyond its name for identification purposes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-293
**ID**: 154
**Summary**: Location resource SHALL support type element
**Requirement**: "Location.type [Control: 0.*] [Must Support: true] - Indicates the type of function performed at the location."
**Context**: The PlanNet Location profile requires support for the type element to categorize locations by the type of service or resource available (e.g., hospital, clinic, pharmacy). The binding is extensible to ServiceDeliveryLocationRoleType value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-294
**ID**: 155
**Summary**: Location resource SHALL support telecom element with specific extensions
**Requirement**: "Location.telecom [Control: 0.*] [Must Support: true] - The contact details of communication devices available at the location."
**Context**: The PlanNet Location profile requires support for telecom elements to capture phone numbers, fax numbers, email addresses and websites for the location. This includes support for contactpoint-availabletime and via-intermediary extensions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-295
**ID**: 156
**Summary**: Location resource SHALL support telecom.system element
**Requirement**: "Location.telecom.system [Control: 0.1] [Must Support: true] - Telecommunications form for contact point - what communications system is required to make use of the contact."
**Context**: The PlanNet Location profile requires support for the telecom.system element to specify the type of contact point (phone, fax, email, etc.).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-296
**ID**: 157
**Summary**: Location resource SHALL support telecom.value element
**Requirement**: "Location.telecom.value [Control: 0.1] [Must Support: true] - The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address)."
**Context**: The PlanNet Location profile requires support for the telecom.value element to capture the actual contact information value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-297
**ID**: 158
**Summary**: Location resource SHALL support address element with specific sub-elements
**Requirement**: "Location.address [Control: 0.1] [Must Support: true] - Physical location."
**Context**: The PlanNet Location profile requires support for the address element including line, city, state, and postalCode sub-elements (all marked as Must Support) to capture the physical location address.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-298
**ID**: 159
**Summary**: Location resource SHALL support position element
**Requirement**: "Location.position [Control: 0.1] [Must Support: true] - The absolute geographic location of the Location, expressed using the WGS84 datum."
**Context**: The PlanNet Location profile requires support for the position element to capture geographic coordinates (longitude and latitude) for mobile applications and automated route-finding. The position element requires both longitude and latitude with cardinality 1..1 each.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-299
**ID**: 160
**Summary**: Location resource SHALL support managingOrganization element referencing Plan-Net Organization
**Requirement**: "Location.managingOrganization [Control: 0.1] [Type: Reference(Plan-Net Organization)] [Must Support: true] - The organization responsible for the provisioning and upkeep of the location."
**Context**: The PlanNet Location profile requires support for the managingOrganization element which must reference a Plan-Net Organization profile to identify the organization responsible for the location.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-300
**ID**: 161
**Summary**: Location resource SHALL support partOf element referencing Plan-Net Location
**Requirement**: "Location.partOf [Control: 0.1] [Type: Reference(Plan-Net Location)] [Must Support: true] - Another Location of which this Location is physically a part of."
**Context**: The PlanNet Location profile requires support for the partOf element which must reference another Plan-Net Location to represent hierarchical location relationships.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-301
**ID**: 162
**Summary**: Location resource SHALL support hoursOfOperation element with specific sub-elements
**Requirement**: "Location.hoursOfOperation [Control: 0.*] [Must Support: true] - What days/times during a week is this location usually open. [Sub-elements daysOfWeek, allDay, openingTime, closingTime all marked Must Support: true]"
**Context**: The PlanNet Location profile requires support for the hoursOfOperation element and its sub-elements to capture the days and times when the location is open, including days of week, whether open all day, and opening/closing times.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-302
**ID**: 163
**Summary**: Location resource SHALL support availabilityExceptions element
**Requirement**: "Location.availabilityExceptions [Control: 0.1] [Must Support: true] - A description of when the locations opening ours are different to normal, e.g. public holiday availability."
**Context**: The PlanNet Location profile requires support for the availabilityExceptions element to describe exceptions to normal opening hours such as public holidays.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-303
**ID**: 164
**Summary**: Location resource SHALL support endpoint element referencing Plan-Net Endpoint
**Requirement**: "Location.endpoint [Control: 0.*] [Type: Reference(Plan-Net Endpoint)] [Must Support: true] - Technical endpoints providing access to services operated for the location."
**Context**: The PlanNet Location profile requires support for the endpoint element which must reference Plan-Net Endpoint resources to capture technical connection details for systems at the location.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-304
**ID**: 165
**Summary**: Location resource SHALL support newpatients extension
**Requirement**: "Location.extension:newpatients [Control: 0.*] [Must Support: true] - New Patients indicates whether new patients are being accepted in general, or from a specific network."
**Context**: The PlanNet Location profile requires support for the newpatients extension to indicate whether the location accepts new patients, providing flexibility for specifying acceptance by network.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-305
**ID**: 166
**Summary**: Location resource SHALL support accessibility extension
**Requirement**: "Location.extension:accessibility [Control: 0.*] [Must Support: true] - An extension to describe accessibility options offered by a practitioner or at a location."
**Context**: The PlanNet Location profile requires support for the accessibility extension to describe accessibility options available at the location for patients with disabilities or special needs.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-306
**ID**: 167
**Summary**: Location resource SHALL support region extension for GeoJSON boundary
**Requirement**: "Location.extension:region [Control: 0.1] [Must Support: true] - A boundary shape that represents the outside edge of the location (in GeoJSON format). The format of the content is GeoJSON in both the JSON and XML formats. The mimetype to be used will be 'application/geo+json'."
**Context**: The PlanNet Location profile requires support for the region extension to capture geographic boundaries of the location using the GeoJSON format, enabling representation of service areas or geographic regions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-307
**ID**: 168
**Summary**: Location resource SHALL support contactpoint-availabletime extension on telecom
**Requirement**: "Location.telecom.extension:contactpoint-availabletime [Control: 0.*] [Must Support: true] - An extension representing the days and times a contact point is available."
**Context**: The PlanNet Location profile requires support for the contactpoint-availabletime extension on telecom elements to specify when specific contact points are available for use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-308
**ID**: 169
**Summary**: Location resource SHALL support via-intermediary extension on telecom
**Requirement**: "Location.telecom.extension:via-intermediary [Control: 0.*] [Must Support: true] - A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization."
**Context**: The PlanNet Location profile requires support for the via-intermediary extension on telecom elements to reference alternative contact points through intermediary resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-309
**ID**: 170
**Summary**: Location resource SHALL NOT contain nested contained resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources (contained.contained.empty())"
**Context**: The Location resource profile enforces FHIR invariant dom-2 which prohibits contained resources from themselves containing other resources, preventing deep nesting of resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement only applies if the Location resource is contained within another resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-310
**ID**: 171
**Summary**: Contained Location resource SHALL be referenced or refer to containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource (contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty())"
**Context**: The Location resource profile enforces FHIR invariant dom-3 which requires that contained resources must be referenced from somewhere in the containing resource or must reference the containing resource, ensuring contained resources serve a purpose.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement only applies if the Location resource is contained within another resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-311
**ID**: 172
**Summary**: Contained Location resource SHALL NOT have meta.versionId or meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (contained.meta.versionId.empty() and contained.meta.lastUpdated.empty())"
**Context**: The Location resource profile enforces FHIR invariant dom-4 which prohibits contained resources from having version or timestamp metadata, as they are managed as part of the containing resource.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement only applies if the Location resource is contained within another resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-312
**ID**: 173
**Summary**: Contained Location resource SHALL NOT have security labels
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label (contained.meta.security.empty())"
**Context**: The Location resource profile enforces FHIR invariant dom-5 which prohibits contained resources from having their own security labels, as security is managed at the containing resource level.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement only applies if the Location resource is contained within another resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions
**Grouping**: Location

---
# REQ-313
**ID**: 174
**Summary**: Location status must be 'active'
**Requirement**: "The status property covers the general availability of the resource, not the current value which may be covered by the operationStatus, or by a schedule/slots if they are configured for the location. [Location.status has a] Fixed Value: active"
**Context**: The Plan-Net Location profile requires that all Location resources have their status element set to the fixed value 'active'. This ensures that only active locations are represented in the provider directory.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - status element
**Grouping**: Location

---
# REQ-314
**ID**: 175
**Summary**: Location name is mandatory
**Requirement**: "Name of the location as used by humans. Does not need to be unique. [Cardinality: 1..1]"
**Context**: The Plan-Net Location profile requires that every Location resource include a name element with cardinality 1..1, making it a mandatory field.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - name element
**Grouping**: Location

---
# REQ-315
**ID**: 176
**Summary**: Location position longitude is mandatory when position is provided
**Requirement**: "Longitude. The value domain and the interpretation are the same as for the text of the longitude element in KML (see notes below). [Cardinality: 1..1]"
**Context**: When a Location resource includes a position element, the longitude sub-element is mandatory with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.position is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - position.longitude element
**Grouping**: Location

---
# REQ-316
**ID**: 177
**Summary**: Location position latitude is mandatory when position is provided
**Requirement**: "Latitude. The value domain and the interpretation are the same as for the text of the latitude element in KML (see notes below). [Cardinality: 1..1]"
**Context**: When a Location resource includes a position element, the latitude sub-element is mandatory with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.position is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - position.latitude element
**Grouping**: Location

---
# REQ-317
**ID**: 178
**Summary**: Location identifier.use binding is required
**Requirement**: "The purpose of this identifier. [Binding: IdentifierUse (required)]"
**Context**: The Location.identifier.use element must draw its value from the required IdentifierUse value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.identifier.use is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - identifier.use element
**Grouping**: Location

---
# REQ-318
**ID**: 179
**Summary**: Location identifier.type binding is extensible
**Requirement**: "A coded type for the identifier that can be used to determine which identifier to use for a specific purpose. [Binding: Identifier Type Codes (extensible)] To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: The Location.identifier.type element should draw its value from the extensible Identifier Type Codes value set, but may use alternate codes if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.identifier.type is present and a code from the value set applies to the concept being communicated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - identifier.type element
**Grouping**: Location

---
# REQ-319
**ID**: 180
**Summary**: Location status binding is required
**Requirement**: "The status property covers the general availability of the resource. [Binding: LocationStatus (required)] To be conformant, the concept in this element SHALL be from the specified value set."
**Context**: The Location.status element must draw its value from the required LocationStatus value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - status element
**Grouping**: Location

---
# REQ-320
**ID**: 181
**Summary**: Location type binding is extensible
**Requirement**: "Indicates the type of function performed at the location. [Binding: ServiceDeliveryLocationRoleType (extensible)] To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: The Location.type element should draw its value from the extensible ServiceDeliveryLocationRoleType value set, but may use alternate codes if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.type is present and a code from the value set applies to the concept being communicated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - type element
**Grouping**: Location

---
# REQ-321
**ID**: 182
**Summary**: Location telecom.system binding is required
**Requirement**: "Telecommunications form for contact point - what communications system is required to make use of the contact. [Binding: ContactPointSystem (required)] To be conformant, the concept in this element SHALL be from the specified value set."
**Context**: The Location.telecom.system element must draw its value from the required ContactPointSystem value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.telecom.system is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - telecom.system element
**Grouping**: Location

---
# REQ-322
**ID**: 183
**Summary**: Location telecom.use binding is required
**Requirement**: "Identifies the purpose for the contact point. [Binding: ContactPointUse (required)] To be conformant, the concept in this element SHALL be from the specified value set."
**Context**: The Location.telecom.use element must draw its value from the required ContactPointUse value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.telecom.use is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - telecom.use element
**Grouping**: Location

---
# REQ-323
**ID**: 184
**Summary**: Location address.use binding is required
**Requirement**: "The purpose of this address. [Binding: AddressUse (required)] To be conformant, the concept in this element SHALL be from the specified value set."
**Context**: The Location.address.use element must draw its value from the required AddressUse value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.address.use is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - address.use element
**Grouping**: Location

---
# REQ-324
**ID**: 185
**Summary**: Location address.state binding is extensible
**Requirement**: "Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes). [Binding: USPS Two Letter Alphabetic Codes (extensible)] To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: The Location.address.state element should draw its value from the extensible USPS Two Letter Alphabetic Codes value set, but may use alternate codes if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.address.state is present and a code from the value set applies to the concept being communicated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - address.state element
**Grouping**: Location

---
# REQ-325
**ID**: 186
**Summary**: Location hoursOfOperation.daysOfWeek binding is required
**Requirement**: "Indicates which days of the week are available between the start and end Times. [Binding: DaysOfWeek (required)] To be conformant, the concept in this element SHALL be from the specified value set."
**Context**: The Location.hoursOfOperation.daysOfWeek element must draw its value from the required DaysOfWeek value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.hoursOfOperation.daysOfWeek is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - hoursOfOperation.daysOfWeek element
**Grouping**: Location

---
# REQ-326
**ID**: 187
**Summary**: Location accessibility extension binding is extensible
**Requirement**: "Extension URL = http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility [Binding: Accessibility VS (extensible)] To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: The Location.extension:accessibility element should draw its value from the extensible Accessibility VS value set, but may use alternate codes if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when Location.extension:accessibility is present and a code from the value set applies to the concept being communicated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.60.1 Resource Profile: Plan-Net Location - extension:accessibility element
**Grouping**: Location

---
# REQ-327
**ID**: 188
**Summary**: Plan-Net Organization active status requirement
**Requirement**: "The [Plan-Net Organization] active [element] SHALL have a value of true, indicating the organization's record is still in active use."
**Context**: This requirement applies to the Plan-Net Organization profile, mandating that the active element must be present with a required pattern value of true. The cardinality is 1..1, making this a mandatory element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-328
**ID**: 189
**Summary**: Plan-Net Organization type requirement
**Requirement**: "The [Plan-Net Organization] type [element] SHALL be present with cardinality 1..*, indicating the kind(s) of organization."
**Context**: The type element is mandatory and must contain at least one value from the OrgTypeVS value set (extensible binding). This identifies the kind of organization such as payer, provider, or other organization types defined in the value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-329
**ID**: 190
**Summary**: Plan-Net Organization name requirement
**Requirement**: "The [Plan-Net Organization] name [element] SHALL be present with cardinality 1..1, providing the name used for the organization."
**Context**: The name element is mandatory and must contain the name associated with the organization. This, along with identifier, satisfies the constraint org-1 that requires at least a name or identifier.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-330
**ID**: 191
**Summary**: Plan-Net Organization address requirement
**Requirement**: "The [Plan-Net Organization] address [element] SHALL be present with cardinality 1..*, providing an address for the organization."
**Context**: At least one address must be provided for the organization. The address must never be of use 'home' (constraint org-2). This is a mandatory element with Must-Support flag.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: 
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-331
**ID**: 192
**Summary**: Plan-Net Organization telecom use constraint
**Requirement**: "The telecom of an [Plan-Net] organization [SHALL NOT] be of use 'home'."
**Context**: This is constraint org-3 applied to the telecom element. When telecom contact details are provided for the organization, the use element must not have the value 'home'.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when Organization.telecom is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-332
**ID**: 193
**Summary**: Plan-Net Organization address use constraint
**Requirement**: "An address of an [Plan-Net] organization [SHALL NOT] be of use 'home'."
**Context**: This is constraint org-2 applied to the address element. When addresses are provided for the organization, the use element must not have the value 'home'.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when Organization.address is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-333
**ID**: 194
**Summary**: Plan-Net Organization NPI identifier format validation
**Requirement**: "NPI [identifier value for Plan-Net Organization] must be 10 digits: value.matches('^[0-9]{10}$')"
**Context**: This is constraint us-core-16 applied to the identifier:NPI slice. When an NPI identifier is provided, the value must be exactly 10 numeric digits.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when Organization.identifier:NPI is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-334
**ID**: 195
**Summary**: Plan-Net Organization NPI check digit validation
**Requirement**: "NPI check digit [for Plan-Net Organization] must be valid (Luhn algorithm check): (((select(value.substring(0,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(1,1).toInteger())+(select(value.substring(2,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(3,1).toInteger())+(select(value.substring(4,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(5,1).toInteger())+(select(value.substring(6,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(7,1).toInteger())+(select(value.substring(8,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(9,1).toInteger()) + 24)mod 10=0)"
**Context**: This is constraint us-core-17 applied to the identifier:NPI slice. When an NPI identifier is provided, the check digit must be valid according to the Luhn algorithm.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when Organization.identifier:NPI is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-335
**ID**: 196
**Summary**: Plan-Net Organization CLIA identifier format validation
**Requirement**: "CLIA number [for Plan-Net Organization] must be 10 digits with a letter 'D' in third position: value.matches('^[0-9]{2}D[0-9]{7}$')"
**Context**: This is constraint us-core-18 applied to the identifier:CLIA slice. When a CLIA identifier is provided for laboratories, it must follow the format of 2 digits, letter 'D', then 7 digits.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when Organization.identifier:CLIA is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-336
**ID**: 197
**Summary**: Plan-Net Organization NAIC identifier format validation
**Requirement**: "NAIC [identifier value for Plan-Net Organization] must be 5 digits: value.matches('^[0-9]{5}$')"
**Context**: This is constraint us-core-19 applied to the identifier:NAIC slice. When a NAIC identifier is provided, the value must be exactly 5 numeric digits.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when Organization.identifier:NAIC is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-337
**ID**: 198
**Summary**: Plan-Net Organization address text and parts synchronization requirement
**Requirement**: "Applications updating an address SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part."
**Context**: When an Organization.address includes both the text element and structured parts (line, city, state, etc.), the text representation must not contain information that is not also present in the structured parts.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when both address.text and address parts are present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.62.1 Resource Profile - Plan-Net Organization
**Grouping**: Organization

---
# REQ-338
**ID**: 199
**Summary**: Practitioner resource SHALL have at least one identifier
**Requirement**: "identifier [Practitioner.identifier] ... 1..* [cardinality]"
**Context**: The Plan-Net Practitioner profile requires that at least one identifier be present for a practitioner resource. This is a constraint on the base US Core Practitioner Profile which also requires 1..* identifiers.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile
**Grouping**: Practitioner

---
# REQ-339
**ID**: 200
**Summary**: Practitioner identifier system SHALL be populated
**Requirement**: "system [Practitioner.identifier.system] ... 1.1 [cardinality]"
**Context**: Each identifier for a practitioner must include the system element which establishes the namespace for the identifier value.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile
**Grouping**: Practitioner

---
# REQ-340
**ID**: 201
**Summary**: Practitioner identifier value SHALL be populated
**Requirement**: "value [Practitioner.identifier.value] ... 1.1 [cardinality]"
**Context**: Each identifier for a practitioner must include the value element which contains the unique identifier string within the specified system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile
**Grouping**: Practitioner

---
# REQ-341
**ID**: 202
**Summary**: NPI identifier SHALL be 10 digits
**Requirement**: "NPI must be 10 digits: value.matches('^[0-9]{10}$')"
**Context**: When an NPI identifier is provided (identifier:NPI slice), the value must match the pattern of exactly 10 numeric digits as specified in the us-core-16 constraint.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when NPI identifier slice is populated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1.1.7 Constraints
**Grouping**: Practitioner

---
# REQ-342
**ID**: 203
**Summary**: NPI identifier check digit SHALL be valid
**Requirement**: "NPI check digit must be valid (Luhn algorithm check): (((select(value.substring(0,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(1,1).toInteger())+(select(value.substring(2,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(3,1).toInteger())+(select(value.substring(4,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(5,1).toInteger())+(select(value.substring(6,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(7,1).toInteger())+(select(value.substring(8,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(9,1).toInteger()) + 24)mod 10=0)"
**Context**: When an NPI identifier is provided, the check digit must be valid according to the Luhn algorithm as specified in the us-core-17 constraint.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when NPI identifier slice is populated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1.1.7 Constraints
**Grouping**: Practitioner

---
# REQ-343
**ID**: 204
**Summary**: NPI identifier system SHALL be fixed value
**Requirement**: "system [identifier:NPI.system] ... Fixed Value: http://hl7.org/fhir/sid/us-npi"
**Context**: When an NPI identifier slice is used, the system element must be set to the fixed value of http://hl7.org/fhir/sid/us-npi to indicate this is a US National Provider Identifier.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when NPI identifier slice is populated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile
**Grouping**: Practitioner

---
# REQ-344
**ID**: 205
**Summary**: Practitioner active status SHALL be true
**Requirement**: "active [Practitioner.active] ... 1.1 [cardinality] ... Required Pattern: true"
**Context**: The Practitioner profile requires that the active element be present with a value of true, indicating that the practitioner's record is in active use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile
**Grouping**: Practitioner

---
# REQ-345
**ID**: 206
**Summary**: Practitioner SHALL have at least one name
**Requirement**: "name [Practitioner.name] ... 1..* [cardinality]"
**Context**: The practitioner resource must include at least one name element to identify the practitioner.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile
**Grouping**: Practitioner

---
# REQ-346
**ID**: 207
**Summary**: Practitioner name SHALL have family name
**Requirement**: "family [Practitioner.name.family] ... 1.1 [cardinality]"
**Context**: Each practitioner name must include the family (surname) element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile
**Grouping**: Practitioner

---
# REQ-347
**ID**: 208
**Summary**: Practitioner qualification code SHALL be populated
**Requirement**: "code [Practitioner.qualification.code] ... 1.1 [cardinality]"
**Context**: When a qualification element is present, the code element must be populated with a coded representation of the qualification, bound to the Individual Specialties, Degrees, Licenses, and Certificates VS value set with extensible binding.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when qualification element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.64.1 Resource Profile
**Grouping**: Practitioner

---
# REQ-348
**ID**: 209
**Summary**: InsurancePlan resource SHALL contain nested resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources"
**Context**: This is an invariant (dom-2) that applies to InsurancePlan resources when they are contained within another resource. It ensures that contained resources do not themselves contain other resources, maintaining a flat containment structure.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the InsurancePlan resource is contained in another resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant dom-2
**Grouping**: General/Cross-Resource

---
# REQ-349
**ID**: 210
**Summary**: Contained InsurancePlan resource SHALL be referenced or refer to containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This is an invariant (dom-3) that applies to InsurancePlan resources when they are contained within another resource. It ensures that contained resources are properly referenced within the parent resource structure.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the InsurancePlan resource is contained in another resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant dom-3
**Grouping**: General/Cross-Resource

---
# REQ-350
**ID**: 211
**Summary**: Contained InsurancePlan resource SHALL NOT have meta.versionId or meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated"
**Context**: This is an invariant (dom-4) that applies to InsurancePlan resources when they are contained within another resource. It prevents versioning metadata from being included in contained resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the InsurancePlan resource is contained in another resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant dom-4
**Grouping**: General/Cross-Resource

---
# REQ-351
**ID**: 212
**Summary**: Contained InsurancePlan resource SHALL NOT have security label
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label"
**Context**: This is an invariant (dom-5) that applies to InsurancePlan resources when they are contained within another resource. It prevents security labels from being applied to contained resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the InsurancePlan resource is contained in another resource.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant dom-5
**Grouping**: General/Cross-Resource

---
# REQ-352
**ID**: 213
**Summary**: InsurancePlan SHALL have name or identifier
**Requirement**: "The organization SHALL at least have a name or an idendtifier, and possibly more than one"
**Context**: This is an invariant (ipn-1) that requires InsurancePlan resources to include either a name element or an identifier element, or both. This ensures minimal identifying information is present.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant ipn-1
**Grouping**: Coverage

---
# REQ-353
**ID**: 214
**Summary**: InsurancePlan SHALL define network at plan or product level
**Requirement**: "If an insuranceplan does not define a network, then each plan must define one"
**Context**: This is an invariant (network-or-plan-Network) that ensures network information is present either at the InsurancePlan level or at each individual plan level. At least one location must specify the network.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the InsurancePlan does not define a network at the product level.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant network-or-plan-Network
**Grouping**: Coverage

---
# REQ-354
**ID**: 215
**Summary**: InsurancePlan.plan.type SHALL be distinct
**Requirement**: "Each InsurancePlan.plan should have a distinct plan.type."
**Context**: This is an invariant (plan-type-is-distinct) that ensures each plan within an InsurancePlan has a unique plan type code. This prevents duplicate plan type entries.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant plan-type-is-distinct
**Grouping**: Coverage

---
# REQ-355
**ID**: 216
**Summary**: InsurancePlan identifier.use codes SHALL be from IdentifierUse value set
**Requirement**: "The codes SHALL be taken from IdentifierUse"
**Context**: The identifier.use element in InsurancePlan must use codes from the required IdentifierUse value set (http://hl7.org/fhir/ValueSet/identifier-use). This ensures consistent coding of identifier purpose.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 8 InsurancePlan.identifier.use
**Grouping**: Coverage

---
# REQ-356
**ID**: 217
**Summary**: InsurancePlan identifier.type codes SHALL be from Identifier Type Codes unless not suitable
**Requirement**: "Unless not suitable, these codes SHALL be taken from Identifier Type Codes"
**Context**: The identifier.type element in InsurancePlan should use codes from the extensible Identifier Type Codes value set (http://hl7.org/fhir/ValueSet/identifier-type). This provides standard coding for identifier types while allowing other codes when necessary.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies unless the Identifier Type Codes value set is not suitable for the use case.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 10 InsurancePlan.identifier.type
**Grouping**: Coverage

---
# REQ-357
**ID**: 218
**Summary**: InsurancePlan identifier.value SHALL be urn:ietf:rfc:3986 if full URI
**Requirement**: "If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986"
**Context**: When the identifier.value element in InsurancePlan contains a full URI, the identifier.system must be set to urn:ietf:rfc:3986. This ensures proper identification of URI-based identifiers.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the identifier.value is a full URI.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 12 InsurancePlan.identifier.value
**Grouping**: Coverage

---
# REQ-358
**ID**: 219
**Summary**: InsurancePlan status codes SHALL be from PublicationStatus value set
**Requirement**: "The codes SHALL be taken from PublicationStatus"
**Context**: The status element in InsurancePlan must use codes from the required PublicationStatus value set (http://hl7.org/fhir/ValueSet/publication-status). This ensures consistent coding of resource lifecycle status. The fixed value for Plan-Net InsurancePlan is 'active'.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 16 InsurancePlan.status
**Grouping**: Coverage

---
# REQ-359
**ID**: 220
**Summary**: InsurancePlan type codes SHALL be from Insurance Product Type VS unless not suitable
**Requirement**: "Unless not suitable, these codes SHALL be taken from Insurance Product Type VS"
**Context**: The type element in InsurancePlan should use codes from the extensible Insurance Product Type VS value set (http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/InsuranceProductTypeVS). This provides standard coding for insurance product types while allowing other codes when necessary. This element has cardinality 1..1 in the Plan-Net profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies unless the Insurance Product Type VS value set is not suitable for the use case.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 18 InsurancePlan.type
**Grouping**: Coverage

---
# REQ-360
**ID**: 221
**Summary**: InsurancePlan contact.name.use codes SHALL be from NameUse value set
**Requirement**: "The codes SHALL be taken from NameUse"
**Context**: The contact.name.use element in InsurancePlan must use codes from the required NameUse value set (http://hl7.org/fhir/ValueSet/name-use). This ensures consistent coding of name usage context.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 38 InsurancePlan.contact.name.use
**Grouping**: Coverage

---
# REQ-361
**ID**: 222
**Summary**: InsurancePlan contact.name.text SHALL ensure content is in parts when both present
**Requirement**: "Applications updating a name SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part"
**Context**: When updating InsurancePlan contact.name, if both the text element and name parts (family, given, etc.) are present, applications must ensure the text representation doesn't contain information not reflected in the structured parts. This maintains data consistency.
**Conformance**: SHALL
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when both text and name parts are present in the contact.name element.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 40 InsurancePlan.contact.name.text
**Grouping**: Coverage

---
# REQ-362
**ID**: 223
**Summary**: InsurancePlan contact.telecom.system codes SHALL be from ContactPointSystem value set
**Requirement**: "The codes SHALL be taken from ContactPointSystem"
**Context**: The contact.telecom.system element in InsurancePlan must use codes from the required ContactPointSystem value set (http://hl7.org/fhir/ValueSet/contact-point-system). This ensures consistent coding of telecommunications form.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 44 InsurancePlan.contact.telecom.system
**Grouping**: Coverage

---
# REQ-363
**ID**: 224
**Summary**: InsurancePlan contact.telecom.use codes SHALL be from ContactPointUse value set
**Requirement**: "The codes SHALL be taken from ContactPointUse"
**Context**: The contact.telecom.use element in InsurancePlan must use codes from the required ContactPointUse value set (http://hl7.org/fhir/ValueSet/contact-point-use). This ensures consistent coding of contact point usage purpose.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 48 InsurancePlan.contact.telecom.use
**Grouping**: Coverage

---
# REQ-364
**ID**: 225
**Summary**: InsurancePlan plan.type codes SHALL be from Insurance Plan TypeVS unless not suitable
**Requirement**: "Unless not suitable, these codes SHALL be taken from Insurance Plan TypeVS"
**Context**: The plan.type element in InsurancePlan should use codes from the extensible Insurance Plan TypeVS value set (http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/InsurancePlanTypeVS). This provides standard coding for plan categorization while allowing other codes when necessary.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies unless the Insurance Plan TypeVS value set is not suitable for the use case.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 58 InsurancePlan.plan.type
**Grouping**: Coverage

---
# REQ-365
**ID**: 226
**Summary**: InsurancePlan plan.specificCost.benefit.cost.applicability codes SHALL be from BenefitCostApplicability value set
**Requirement**: "The codes SHALL be taken from BenefitCostApplicability"
**Context**: The plan.specificCost.benefit.cost.applicability element in InsurancePlan must use codes from the required BenefitCostApplicability value set (http://hl7.org/fhir/ValueSet/insuranceplan-applicability). This ensures consistent coding of whether costs apply to in-network or out-of-network providers.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Element 202 InsurancePlan.plan.specificCost.benefit.cost.applicability
**Grouping**: Coverage

---
# REQ-366
**ID**: 227
**Summary**: HealthcareService active status requirement
**Requirement**: "This flag is used to mark the record to not be used. This is not used when a center is closed for maintenance, or for holidays, the notAvailable period is to be used for this." [The HealthcareService.active element SHALL be set to true for active records]
**Context**: The active flag indicates whether the HealthcareService record is in active use. The cardinality is 1..1 with a required pattern of true, meaning all HealthcareService instances must have active=true.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-367
**ID**: 228
**Summary**: HealthcareService category cardinality requirement
**Requirement**: "[HealthcareService.category] Identifies the broad category of service being performed or delivered." [Cardinality 1..*]
**Context**: At least one category element must be present to identify the broad category of service. The category uses a required binding to HealthcareServiceCategoryVS for the plan-net-category slice.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-368
**ID**: 229
**Summary**: HealthcareService category binding requirement
**Requirement**: "[HealthcareService.category:plan-net-category] Broad category of service being performed or delivered" [SHALL use codes from HealthcareServiceCategoryVS value set (required binding)]
**Context**: The plan-net-category slice of the category element must use codes from the specified value set to ensure consistent categorization of healthcare services across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-369
**ID**: 230
**Summary**: HealthcareService type binding requirement
**Requirement**: "[HealthcareService.type] The specific type of service that may be delivered or performed." [SHALL use codes from HealthcareServiceTypeVS value set if any of the codes within the value set can apply (extensible binding)]
**Context**: The type element specifies the specific type of service and uses an extensible binding, meaning implementations must use codes from the specified value set when applicable, but may use alternate codes if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when codes within the HealthcareServiceTypeVS value set can apply to the concept being communicated
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-370
**ID**: 231
**Summary**: HealthcareService specialty binding requirement
**Requirement**: "[HealthcareService.specialty] Collection of specialties handled by the service site." [SHALL use codes from SpecialtiesVS value set (required binding)]
**Context**: The specialty element describes medical specialties handled by the healthcare service and must use codes from the specified required value set to ensure interoperability.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-371
**ID**: 232
**Summary**: HealthcareService notAvailable description requirement
**Requirement**: "[HealthcareService.notAvailable.description] The reason that can be presented to the user as to why this time is not available." [Cardinality 1..1]
**Context**: When the notAvailable element is used to indicate service unavailability, a description must be provided explaining the reason to users. This is a mandatory element within the notAvailable backbone element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when HealthcareService.notAvailable is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-372
**ID**: 233
**Summary**: HealthcareService reference to Plan-Net Organization
**Requirement**: "[HealthcareService.providedBy] The organization that provides this healthcare service." [SHALL reference Plan-Net Organization profile]
**Context**: When specifying the organization providing the healthcare service, the reference must conform to the Plan-Net Organization profile to ensure consistent representation of organizational data.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when providedBy element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-373
**ID**: 234
**Summary**: HealthcareService reference to Plan-Net Location
**Requirement**: "[HealthcareService.location] The location(s) where this healthcare service may be provided." [SHALL reference Plan-Net Location profile]
**Context**: Location references must conform to the Plan-Net Location profile to maintain consistency in location data representation across the implementation guide.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when location element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-374
**ID**: 235
**Summary**: HealthcareService reference to Plan-Net Endpoint
**Requirement**: "[HealthcareService.endpoint] Technical endpoints providing access to services operated for the specific healthcare services defined at this resource." [SHALL reference Plan-Net Endpoint profile]
**Context**: Endpoint references must conform to the Plan-Net Endpoint profile to ensure consistent representation of technical service access points.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when endpoint element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-375
**ID**: 236
**Summary**: HealthcareService coverageArea reference to Plan-Net Location
**Requirement**: "[HealthcareService.coverageArea] The location(s) that this service is available to (not where the service is provided)." [SHALL reference Plan-Net Location profile]
**Context**: Coverage area references indicate service availability regions and must conform to the Plan-Net Location profile for consistency in geographic representation.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Required when coverageArea element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.58.1 Resource Profile: Plan-Net HealthcareService
**Grouping**: HealthcareService

---
# REQ-376
**ID**: 237
**Summary**: InsurancePlan status must be active
**Requirement**: "The current state of the health insurance product [status] SHALL be [active]"
**Context**: The Plan-Net InsurancePlan profile constrains the status element to a fixed value of "active". This means all InsurancePlan resources conforming to this profile must have their status set to active.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource

---
# REQ-377
**ID**: 238
**Summary**: InsurancePlan type is mandatory
**Requirement**: "The kind of health insurance product [type] SHALL be present with cardinality 1..1"
**Context**: The type element describes the kind of health insurance product and is mandatory in the Plan-Net InsurancePlan profile. It uses an extensible binding to the InsuranceProductTypeVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource

---
# REQ-378
**ID**: 239
**Summary**: InsurancePlan ownedBy is mandatory
**Requirement**: "The entity that is providing the health insurance product and underwriting the risk [ownedBy] SHALL be present with cardinality 1..1 and SHALL reference a Plan-Net Organization"
**Context**: The ownedBy element identifies the insurance carrier or payer providing and underwriting the insurance product. This is a mandatory reference to a Plan-Net Organization profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource

---
# REQ-379
**ID**: 240
**Summary**: InsurancePlan administeredBy is mandatory
**Requirement**: "An organization which administer other services such as underwriting, customer service and/or claims processing on behalf of the health insurance product owner [administeredBy] SHALL be present with cardinality 1..1 and SHALL reference a Plan-Net Organization"
**Context**: The administeredBy element identifies the organization that administers the insurance product on behalf of the owner. This is a mandatory reference to a Plan-Net Organization profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: Plan-Net InsurancePlan
**Grouping**: General/Cross-Resource

---
# REQ-380
**ID**: 241
**Summary**: InsurancePlan must define network or plan network
**Requirement**: "If an insuranceplan does not define a network, then each plan must define one: network.exists() or plan.network.exists()"
**Context**: This constraint (network-or-plan-Network) ensures that network information is provided either at the InsurancePlan level or at the individual plan level. At least one must be specified to indicate which networks are associated with the insurance product or its plans.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If the InsurancePlan does not define a network element, then each plan within the InsurancePlan must define a network element.
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1.1.2 Constraints
**Grouping**: General/Cross-Resource

---
# REQ-381
**ID**: 242
**Summary**: Each InsurancePlan.plan must have distinct plan type
**Requirement**: "Each InsurancePlan.plan should have a distinct plan.type: plan.type.coding.code.isDistinct()"
**Context**: This constraint (plan-type-is-distinct) ensures that within a single InsurancePlan resource, each plan has a unique plan type. This prevents duplication of plan types within the same insurance product.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1.1.2 Constraints
**Grouping**: General/Cross-Resource

---
# REQ-382
**ID**: 243
**Summary**: PractitionerRole resource SHALL satisfy the practitioner-or-organization-or-healthcareservice-or-location invariant
**Requirement**: "If PlannetPractitionerRole.practitioner is absent ( PlannetPractitionerRole.organization, PlannetPractitionerRole.healthcareservice, PlannetPractitionerRole.location) must be present (`practitioner.exists() or (organization.exists() or healthcareService.exists() or location.exists())`)"
**Context**: This is an invariant constraint on the PractitionerRole resource profile. It ensures that at least one of the key references (practitioner, organization, healthcareService, or location) is present to make the PractitionerRole resource meaningful and valid.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement is only enforced when the practitioner element is absent
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-383
**ID**: 244
**Summary**: PractitionerRole SHALL have contact information or reference to Endpoint
**Requirement**: "SHALL have contact information or a reference to an Endpoint (`telecom.exists() or endpoint.exists()`)"
**Context**: This is the pd-1 invariant that ensures the PractitionerRole resource has sufficient contact information, either through direct telecom details or through a reference to an Endpoint resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-384
**ID**: 245
**Summary**: PractitionerRole SHALL have practitioner, organization, healthcare service, or location
**Requirement**: "SHALL have a practitioner, an organization, a healthcare service, or a location. (`practitioner.exists() or organization.exists() or healthcareService.exists() or location.exists()`)"
**Context**: This is the us-core-13 invariant that ensures at least one core reference element is present in the PractitionerRole resource to establish the role's context.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-385
**ID**: 246
**Summary**: PractitionerRole qualification extension status SHALL be 'active'
**Requirement**: "Value of extension [for qualification status] [SHALL have] Fixed Value `active`"
**Context**: Within the qualification extension, the status sub-extension must have a fixed value of 'active'. This ensures that only active qualifications are represented in the PractitionerRole.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification extension is used and the status sub-extension is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.extension:qualification.extension:status.value[x]
**Grouping**: PractitionerRole

---
# REQ-386
**ID**: 247
**Summary**: PractitionerRole active element SHALL be true
**Requirement**: "Whether this practitioner role record is in active use [SHALL have] Pattern Value `true`"
**Context**: The active element in PractitionerRole must have a pattern value of true, indicating that practitioner role records in this implementation guide should represent active roles.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.active
**Grouping**: PractitionerRole

---
# REQ-387
**ID**: 248
**Summary**: PractitionerRole telecom system SHALL be present
**Requirement**: "[PractitionerRole.telecom.system] Telecommunications form for contact point - what communications system is required to make use of the contact [Control: 1.1]"
**Context**: When telecom information is provided for a PractitionerRole, the system element (indicating phone, fax, email, etc.) must be present with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when telecom element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.telecom.system
**Grouping**: PractitionerRole

---
# REQ-388
**ID**: 249
**Summary**: PractitionerRole telecom value SHALL be present
**Requirement**: "[PractitionerRole.telecom.value] The actual contact point details, in a form that is meaningful to the designated communication system [Control: 1.1]"
**Context**: When telecom information is provided for a PractitionerRole, the value element (the actual contact details) must be present with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when telecom element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.telecom.value
**Grouping**: PractitionerRole

---
# REQ-389
**ID**: 250
**Summary**: PractitionerRole qualification code SHALL use extensible binding to IndividualSpecialtyAndDegreeLicenseCertificateVS
**Requirement**: "[PractitionerRole.extension:qualification.extension:code.value[x]] Unless not suitable, these codes SHALL be taken from [Individual Specialties, Degrees, Licenses, and Certificates VS]([extensible] to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/IndividualSpecialtyAndDegreeLicenseCertificateVS`)"
**Context**: The qualification code within the qualification extension must use codes from the specified value set with extensible binding strength, allowing other codes when necessary.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when qualification extension code is present; extensible binding allows other codes when suitable codes are not available
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.extension:qualification.extension:code.value[x]
**Grouping**: PractitionerRole

---
# REQ-390
**ID**: 251
**Summary**: PractitionerRole qualification status SHALL use required binding to QualificationStatusVS
**Requirement**: "[PractitionerRole.extension:qualification.extension:status.value[x]] The codes SHALL be taken from [Qualification Status VS]([required] to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/QualificationStatusVS`)"
**Context**: The qualification status must use codes from the QualificationStatusVS value set with required binding strength, meaning only codes from this value set are permitted.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when qualification extension status is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.extension:qualification.extension:status.value[x]
**Grouping**: PractitionerRole

---
# REQ-391
**ID**: 252
**Summary**: PractitionerRole qualification whereValid SHALL use required binding to USPS state codes
**Requirement**: "[PractitionerRole.extension:qualification.extension:whereValid.value[x]] The codes SHALL be taken from [USPS Two Letter Alphabetic Codes]([required] to `http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state`)"
**Context**: The whereValid sub-extension within qualification must use codes from the US Core USPS state value set with required binding when using CodeableConcept data type.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when qualification whereValid extension is present and uses CodeableConcept data type
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.extension:qualification.extension:whereValid.value[x]
**Grouping**: PractitionerRole

---
# REQ-392
**ID**: 253
**Summary**: PractitionerRole code SHALL use required binding to PractitionerRoleVS
**Requirement**: "[PractitionerRole.code] The codes SHALL be taken from [PractitionerRole Code VS]([required] to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/PractitionerRoleVS`)"
**Context**: The code element describing the roles a practitioner may perform must use codes from the PractitionerRoleVS value set with required binding.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when code element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.code
**Grouping**: PractitionerRole

---
# REQ-393
**ID**: 254
**Summary**: PractitionerRole specialty SHALL use required binding to IndividualAndGroupSpecialtiesVS
**Requirement**: "[PractitionerRole.specialty] The codes SHALL be taken from [Individual and Group Specialties]([required] to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/IndividualAndGroupSpecialtiesVS`)"
**Context**: The specialty element describing specific specialties of the practitioner must use codes from the IndividualAndGroupSpecialtiesVS value set with required binding.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when specialty element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.specialty
**Grouping**: PractitionerRole

---
# REQ-394
**ID**: 255
**Summary**: PractitionerRole notAvailable description SHALL be present
**Requirement**: "[PractitionerRole.notAvailable.description] The reason that can be presented to the user as to why this time is not available [Control: 1.1]"
**Context**: When the notAvailable element is used to indicate times the practitioner is not available, the description sub-element explaining the reason must be present with cardinality 1..1.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Applies when notAvailable element is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: Resource Profile: PlannetPractitionerRole - Detailed Descriptions, PractitionerRole.notAvailable.description
**Grouping**: PractitionerRole

---
# REQ-395
**ID**: 256
**Summary**: PractitionerRole must be true
**Requirement**: "Whether this practitioner role record is in active use [SHALL have] Required Pattern: true"
**Context**: The Plan-Net PractitionerRole profile constrains the active element to always be true. This means all PractitionerRole resources conforming to this profile must have their active element set to true.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-396
**ID**: 257
**Summary**: PractitionerRole must have contact information or endpoint reference
**Requirement**: "pd-1: SHALL have contact information or a reference to an Endpoint"
**Context**: The Plan-Net PractitionerRole must include either telecom contact information or a reference to an Endpoint resource to ensure the practitioner can be contacted or their services accessed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-397
**ID**: 258
**Summary**: PractitionerRole must have practitioner, organization, healthcare service, or location
**Requirement**: "us-core-13: SHALL have a practitioner, an organization, a healthcare service, or a location"
**Context**: The PractitionerRole must reference at least one of the following: a Practitioner resource, an Organization resource, a HealthcareService resource, or a Location resource. This constraint ensures that the role is properly associated with an entity.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-398
**ID**: 259
**Summary**: PractitionerRole must have organization, healthcare service, or location if practitioner is absent
**Requirement**: "practitioner-or-organization-or-healthcareservice-or-location: If PlannetPractitionerRole.practitioner is absent (PlannetPractitionerRole.organization, PlannetPractitionerRole.healthcareservice, PlannetPractitionerRole.location) must be present"
**Context**: When the PractitionerRole does not reference a specific Practitioner, it must reference at least one of Organization, HealthcareService, or Location. This ensures the role is associated with an organizational context even when a specific practitioner is not identified.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If PractitionerRole.practitioner is absent
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-399
**ID**: 260
**Summary**: PractitionerRole qualification extension status must be active
**Requirement**: "PractitionerRole.extension:qualification.extension:status.value[x] [SHALL have] Fixed Value: active"
**Context**: The status sub-extension within the qualification extension is mandatory (cardinality 1..1) and must have a fixed value of 'active', indicating the qualification is currently active.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When qualification extension is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-400
**ID**: 261
**Summary**: PractitionerRole telecom system element is mandatory
**Requirement**: "PractitionerRole.telecom.system [cardinality] 1.1"
**Context**: When telecom contact information is provided in the PractitionerRole, the system element (indicating the type of contact point such as phone, email, etc.) is mandatory.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When PractitionerRole.telecom is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-401
**ID**: 262
**Summary**: PractitionerRole telecom value element is mandatory
**Requirement**: "PractitionerRole.telecom.value [cardinality] 1.1"
**Context**: When telecom contact information is provided in the PractitionerRole, the value element (containing the actual contact point details) is mandatory.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When PractitionerRole.telecom is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-402
**ID**: 263
**Summary**: PractitionerRole notAvailable description element is mandatory
**Requirement**: "PractitionerRole.notAvailable.description [cardinality] 1.1"
**Context**: When the notAvailable element is used to indicate the practitioner is not available during a period of time, a description explaining the reason must be provided.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When PractitionerRole.notAvailable is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-403
**ID**: 264
**Summary**: PractitionerRole code must use required value set
**Requirement**: "PractitionerRole.code [Binding:] PractitionerRoleVS (required)"
**Context**: The code element, which describes the roles the practitioner may perform, must use codes from the required PractitionerRoleVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When PractitionerRole.code is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-404
**ID**: 265
**Summary**: PractitionerRole specialty must use required value set
**Requirement**: "PractitionerRole.specialty [Binding:] IndividualAndGroupSpecialtiesVS (required)"
**Context**: The specialty element, which describes the specific specialty of the practitioner, must use codes from the required IndividualAndGroupSpecialtiesVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When PractitionerRole.specialty is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-405
**ID**: 266
**Summary**: PractitionerRole qualification code extension is mandatory
**Requirement**: "PractitionerRole.extension:qualification.extension:code [cardinality] 1.1"
**Context**: When the qualification extension is used, the code sub-extension identifying the type of qualification is mandatory.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When PractitionerRole.extension:qualification is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole

---
# REQ-406
**ID**: 267
**Summary**: PractitionerRole qualification status extension is mandatory
**Requirement**: "PractitionerRole.extension:qualification.extension:status [cardinality] 1.1"
**Context**: When the qualification extension is used, the status sub-extension indicating the status of the qualification is mandatory.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: When PractitionerRole.extension:qualification is present
**Verifiable**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile
**Grouping**: PractitionerRole
