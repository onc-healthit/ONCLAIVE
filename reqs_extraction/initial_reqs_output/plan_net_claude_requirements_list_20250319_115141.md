---
# REQ-01-01
**Summary**: Directory service access shall not require authentication
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Inspection
**Actor**: Server (Plan-Net service implementer)
**Conformance**: SHOULD
**Conditional**: False
**Source**: Privacy Considerations Section
---

---
# REQ-02-01
**Summary**: Plan-Net service shall not require consumer identifying information
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Test
**Actor**: Server (Plan-Net service implementer)
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Privacy Considerations Section
---

---
# REQ-03-01
**Summary**: Directory applications shall not send consumer identifiable information
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Test
**Actor**: Client (Directory mobile application implementer)
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Must Support Section
---

---
# REQ-04-01
**Summary**: Health Plan API actors shall populate all Must Support elements
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section, Health Plan API Requirements
---

---
# REQ-05-01
**Summary**: Health Plan API actors shall not include optional Must Support elements when information is absent
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: True (applies when information is not present and minimum cardinality is 0)
**Source**: Must Support Section, Health Plan API Requirements
---

---
# REQ-06-01
**Summary**: Health Plan API actors shall provide reason for missing required Must Support elements
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: True (applies when information is not present and minimum cardinality is >0)
**Source**: Must Support Section, Health Plan API Requirements
---

---
# REQ-07-01
**Summary**: Applications shall process Must Support elements without error
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section, Application Requirements
---

---
# REQ-08-01
**Summary**: Applications should display or store Must Support elements
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Test/Demonstration
**Actor**: Application
**Conformance**: SHOULD
**Conditional**: False
**Source**: Must Support Section, Application Requirements
---

---
# REQ-09-01
**Summary**: Applications shall interpret missing Must Support elements correctly
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section, Application Requirements
---

---
# REQ-10-01
**Summary**: Consumer applications shall process Must Support elements with missing information
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Actor**: Consumer App
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section, Application Requirements
---

---
# REQ-11-01
**Summary**: Profiles shall include lastUpdate timestamp
**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."
**Verification**: Inspection
**Actor**: Server (Profile implementer)
**Conformance**: SHALL
**Conditional**: False
**Source**: Client Detection of Updates Directory Content Section
---

---
# REQ-01-02
**Summary**: Support all profiles defined in the Implementation Guide
**Description**: "The Plan-Net Server **SHALL** support all profiles defined in this Implementation Guide."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section
---

---
# REQ-02-02
**Summary**: Implement RESTful behavior according to FHIR specification
**Description**: "The Plan-Net Server **SHALL** implement the RESTful behavior according to the FHIR specification."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section
---

---
# REQ-03-02
**Summary**: Return specific response classes
**Description**: "The Plan-Net Server **SHALL** return the following response classes: * (Status 400): invalid parameter * (Status 401/4xx): unauthorized request * (Status 403): insufficient scope * (Status 404): unknown resource * (Status 410): deleted resource."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section
---

---
# REQ-04-02
**Summary**: Support JSON source formats
**Description**: "The Plan-Net Server **SHALL** support json source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section
---

---
# REQ-05-02
**Summary**: Identify supported profiles in meta.profile attribute
**Description**: "The Plan-Net Server **SHALL** identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance."
**Verification**: Inspection
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section
---

---
# REQ-06-02
**Summary**: Support searchParameters individually and in combination
**Description**: "The Plan-Net Server **SHALL** support the searchParameters on each profile individually and in combination."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section
---

---
# REQ-07-02
**Summary**: Support forward and reverse chaining on search parameters
**Description**: "The Plan-Net Server **SHALL** support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section
---

---
# REQ-08-02
**Summary**: Support XML source formats
**Description**: "The Plan-Net Server **SHOULD** support xml source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section
---

---
# REQ-09-02
**Summary**: Reject unauthorized requests
**Description**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities Section, Security
---

---
# REQ-10-02
**Summary**: Support Endpoint resource profile
**Description**: "Conformance Expectation: **SHALL** Supported Profiles: [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)"
**Verification**: Inspection
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section
---

---
# REQ-11-02
**Summary**: Support specific Endpoint interactions
**Description**: "Profile Interaction Summary: **SHALL** support `search-type`, `read`."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section
---

---
# REQ-12-02
**Summary**: Support vread on Endpoint
**Description**: "Profile Interaction Summary: **SHOULD** support `vread`."
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section
---

---
# REQ-13-02
**Summary**: Support retrieval of Endpoint by ID
**Description**: "A Server **SHALL** be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]`"
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section
---

---
# REQ-14-02
**Summary**: Support retrieval of Endpoint version
**Description**: "A Server **SHOULD** be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]/_history/vid`"
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section
---

---
# REQ-15-02
**Summary**: Support Endpoint _include operation
**Description**: "A Server **SHALL** be capable of supporting the following _includes: Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section
---

---
# REQ-16-02
**Summary**: Support Endpoint search by organization
**Description**: "A Server **SHALL** support search parameter: [organization](SearchParameter-endpoint-organization.html)"
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section, Search Parameter Summary
---

---
# REQ-17-02
**Summary**: Support Endpoint search by _id
**Description**: "A Server **SHALL** support search parameter: [_id](http://hl7.org/fhir/R4/search.html)"
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section, Search Parameter Summary
---

---
# REQ-18-02
**Summary**: Support Endpoint search by _lastUpdated
**Description**: "A Server **SHALL** support search parameter: [_lastUpdated](http://hl7.org/fhir/R4/search.html)"
**Verification**: Test
**Actor**: Plan-Net Server
**Conformance**: SHALL
**Conditional**: False
**Source**: RESTful Capabilities by Resource/Profile, Endpoint Section, Search Parameter Summary
---