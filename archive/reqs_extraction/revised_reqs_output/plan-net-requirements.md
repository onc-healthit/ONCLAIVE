---
# REQ-01
**Summary**: No PII requirement for directory queries
**Description**: "A conformant Plan-Net service SHALL NOT require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Inspection
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Privacy Considerations (5.1.2)
---

---
# REQ-02
**Summary**: No PII sending by clients
**Description**: "A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service."
**Verification**: Inspection
**Actor**: Application Actor
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Privacy Considerations (5.1.2)
---

---
# REQ-03
**Summary**: Population of Must Support data elements
**Description**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Health Plan API Requirements (5.1.3.1)
---

---
# REQ-04
**Summary**: Not including absent data elements
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors SHALL NOT include the data elements in the resource instance returned as part of the query results."
**Verification**: Inspection
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: True
**Source**: Health Plan API Requirements (5.1.3.1)
---

---
# REQ-05
**Summary**: Using dataAbsentReason for missing required information
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0, SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Inspection
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: True
**Source**: Health Plan API Requirements (5.1.3.1)
---

---
# REQ-06
**Summary**: Client handling of Must Support data elements
**Description**: "Application actors SHALL be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Application Actor
**Conformance**: SHALL
**Conditional**: False
**Source**: Application Requirements (5.1.3.2)
---

---
# REQ-07
**Summary**: Client display of data elements
**Description**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Actor**: Application Actor
**Conformance**: SHOULD
**Conditional**: False
**Source**: Application Requirements (5.1.3.2)
---

---
# REQ-08
**Summary**: Client interpretation of missing Must Support data
**Description**: "When querying Health Plan API actors, Application actors SHALL interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Inspection
**Actor**: Application Actor
**Conformance**: SHALL
**Conditional**: False
**Source**: Application Requirements (5.1.3.2)
---

---
# REQ-09
**Summary**: Client processing of missing information indicators
**Description**: "Consumer App actors SHALL be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Actor**: Application Actor
**Conformance**: SHALL
**Conditional**: False
**Source**: Application Requirements (5.1.3.2)
---

---
# REQ-10
**Summary**: JSON format support
**Description**: "Support json source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-11
**Summary**: RESTful behavior implementation
**Description**: "Implement the RESTful behavior according to the FHIR specification."
**Verification**: Inspection
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-12
**Summary**: Support for all Implementation Guide profiles
**Description**: "Support all profiles defined in this Implementation Guide."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-13
**Summary**: Unauthorized request response
**Description**: "Return the following response classes: (Status 401/4xx): unauthorized request."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-14
**Summary**: Insufficient scope response
**Description**: "Return the following response classes: (Status 403): insufficient scope."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-15
**Summary**: Invalid parameter response
**Description**: "Return the following response classes: (Status 400): invalid parameter."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-16
**Summary**: Unknown resource response
**Description**: "Return the following response classes: (Status 404): unknown resource."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-17
**Summary**: Deleted resource response
**Description**: "Return the following response classes: (Status 410): deleted resource."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-18
**Summary**: Profile identification in meta attribute
**Description**: "Identify the Plan-Net profiles supported as part of the FHIR meta.profile attribute for each instance."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-19
**Summary**: Individual search parameter support
**Description**: "Support the searchParameters on each profile individually."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-20
**Summary**: Combination search parameter support
**Description**: "Support the searchParameters on each profile in combination."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-21
**Summary**: Forward chaining support
**Description**: "Support forward chaining on all search parameters that specify the 'chain' property."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-22
**Summary**: Reverse chaining support
**Description**: "Support reverse chaining on all search parameters that specify the 'chain' property."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-23
**Summary**: XML format support
**Description**: "Support xml source formats for all Plan-Net interactions."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHOULD
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-24
**Summary**: Rejection of unauthorized requests
**Description**: "A server SHALL reject any unauthorized requests by returning an HTTP 401 unauthorized response code."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: FHIR RESTful Capabilities (7.1.2.1)
---

---
# REQ-25
**Summary**: Support for read interaction
**Description**: "For each resource type and profile, a Plan Net server SHALL support the read interaction."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: rest.resource.interaction.where(code='read')
---

---
# REQ-26
**Summary**: Support for vread interaction
**Description**: "For each resource type and profile, a Plan Net server SHOULD support the vread interaction."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHOULD
**Conditional**: False
**Source**: rest.resource.interaction.where(code='vread')
---

---
# REQ-27
**Summary**: Support for _includes
**Description**: "[For each resource] A Server SHALL be capable of supporting the following _includes [list]."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Resource Details (7.1.2.2.X)
---

---
# REQ-28
**Summary**: Support for _revincludes
**Description**: "[For each resource] A Server SHALL be capable of supporting the following _revincludes: [list]."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Resource Details (7.1.2.2.X)
---

---
# REQ-29
**Summary**: Network profile NPI handling
**Description**: "The NPI and CLIA identifier types, which are Must-Support, are clearly intended for provider organizations only and are not expected to be populated for other organization types."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Clarification)
**Conditional**: True
**Source**: Relation to US Core and other IGs (1.1.2)
---

---
# REQ-30
**Summary**: lastUpdate timestamp requirement
**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Requirement)
**Conditional**: False
**Source**: Client Detection of Updates Directory Content (5.1.4)
---

---
# REQ-31
**Summary**: Client tracking of directory content updates
**Description**: "Clients that cache query results can track additions or modifications to directory content through queries that filter content using the _lastUpdated search parameter."
**Verification**: Inspection
**Actor**: Application Actor
**Conformance**: None (Implementation guidance)
**Conditional**: False
**Source**: Client Detection of Updates Directory Content (5.1.4)
---

---
# REQ-32
**Summary**: General Search for Pharmacy
**Description**: "The Plan-Net design is based around the following types of searches: General Search - Example: Pharmacy - Focal Resource and Field: HealthcareService.category, HealthcareService.specialty - Qualifications of Search: Location, network."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Design requirement)
**Conditional**: False
**Source**: Representing and Searching Provider Directory Data (5.2)
---

---
# REQ-33
**Summary**: Provider search by name
**Description**: "The Plan-Net design is based around the following types of searches: Provider by Name - Example: Joe Smith - Focal Resource and Field: Practitioner.name - Qualifications of Search: Location, network, specialty, role/privileges."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Design requirement)
**Conditional**: False
**Source**: Representing and Searching Provider Directory Data (5.2)
---

---
# REQ-34
**Summary**: Organization search by name
**Description**: "The Plan-Net design is based around the following types of searches: Organization by Name - Example: Montgomery Cardiology or CVS - Focal Resource and Field: Organization.name - Qualifications of Search: Location, network, specialty."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Design requirement)
**Conditional**: False
**Source**: Representing and Searching Provider Directory Data (5.2)
---

---
# REQ-35
**Summary**: Provider search by specialty
**Description**: "The Plan-Net design is based around the following types of searches: Provider by Specialty - Example: Cardiologist - Focal Resource and Field: PractitionerRole.specialty - Qualifications of Search: Location, network, name."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Design requirement)
**Conditional**: False
**Source**: Representing and Searching Provider Directory Data (5.2)
---

---
# REQ-36
**Summary**: Organization search by specialty
**Description**: "The Plan-Net design is based around the following types of searches: Organization by specialty - Example: Compounding Pharmacy - Focal Resource and Field: OrganizationAffiliation.specialty - Qualifications of Search: Location, network, name."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Design requirement)
**Conditional**: False
**Source**: Representing and Searching Provider Directory Data (5.2)
---

---
# REQ-37
**Summary**: Search for active practitioners and organizations
**Description**: "Sample query to search for currently active Practitioners (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/PractitionerRole?_include=PractitionerRole:date=ge2021-10-25. Sample query to search for currently active Organizations (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/OrganizationAffiliation?_include=OrganizationAffiliation:date=ge2021-10-25."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Implementation example)
**Conditional**: False
**Source**: Searching for active Practitioners and Organizations (5.2.1)
---

---
# REQ-38
**Summary**: Network contact handling for departments
**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."
**Verification**: Inspection
**Actor**: Health Plan API
**Conformance**: None (Implementation guidance)
**Conditional**: True
**Source**: Network Implementation Guidance (7.57.1.1)
---

---
# REQ-39
**Summary**: Organization contact handling for departments
**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."
**Verification**: Inspection
**Actor**: Health Plan API
**Conformance**: None (Implementation guidance)
**Conditional**: True
**Source**: Organization Implementation Guidance (7.58.1.1)
---

---
# REQ-40
**Summary**: Practitioner qualification coding
**Description**: "When the value set for the coded concept in qualification is insufficient, the qualification can be provided in the text field of the codeableConcept."
**Verification**: Inspection
**Actor**: Health Plan API
**Conformance**: None (Implementation guidance)
**Conditional**: True
**Source**: Practitioner Implementation Guidance (7.60.1.1)
---