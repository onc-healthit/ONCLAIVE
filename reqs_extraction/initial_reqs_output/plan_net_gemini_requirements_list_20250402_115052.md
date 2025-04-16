---
# REQ-001-000-01
**Summary**: Plan-Net service shall not require authentication.
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes - Privacy Considerations

---
# REQ-001-000-02
**Summary**: Plan-Net service shall not store consumer identifiable information.
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes - Privacy Considerations

---
# REQ-001-000-03
**Summary**: Directory mobile application shall not send consumer identifiable information.
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Inspection
**Actor**: Application
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes - Privacy Considerations

---
# REQ-001-000-04
**Summary**: Health Plan API actors shall populate all Must Support data elements in query results.
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Server (Health Plan API)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Health Plan API Requirements

---
# REQ-001-000-05
**Summary**: Health Plan API actors shall not include missing Must Support data elements with minimum cardinality 0.
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0 , the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Actor**: Server (Health Plan API)
**Conformance**: SHALL NOT
**Conditional**: True (Minimum cardinality is 0)
**Source**: Implementation Notes - Must Support - Health Plan API Requirements

---
# REQ-001-000-06
**Summary**: Health Plan API actors shall send reason for missing Must Support data elements with minimum cardinality > 0.
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Actor**: Server (Health Plan API)
**Conformance**: SHALL
**Conditional**: True (Minimum cardinality is > 0)
**Source**: Implementation Notes - Must Support - Health Plan API Requirements

---
# REQ-001-000-07
**Summary**: Application actors shall process resource instances containing Must Support data elements without errors.
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Application Requirements

---
# REQ-001-000-08
**Summary**: Application actors should be able to display or store Must Support data elements.
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Actor**: Application
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes - Must Support - Application Requirements

---
# REQ-001-000-09
**Summary**: Application actors shall interpret missing Must Support data elements as data not present.
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Application Requirements

---
# REQ-001-000-10
**Summary**: Consumer App actors shall process resource instances containing Must Support data elements with missing information.
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Actor**: Application (Consumer App)
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Must Support - Application Requirements

---
# REQ-001-000-11
**Summary**: Profiles shall provide the lastUpdate timestamp.
**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."
**Verification**: Inspection
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes - Client Detection of Updates Directory Content

---
# REQ-001-000-12
**Summary**: Clients should track content changes using the _lastUpdated search parameter.
**Description**: "Clients that cache query results can track additions or modifications to directory content through queries that filter content using the _lastUpdated search parameter."
**Verification**: Test
**Actor**: Application
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes - Client Detection of Updates Directory Content

---
# REQ-001-000-13
**Summary**: Clients should periodically check for deleted data using the _id search parameter.
**Description**: "Clients should periodically check that data cached from past queries has not been deleted by querying for the same elements by _id."
**Verification**: Test
**Actor**: Application
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes - Client Detection of Updates Directory Content 
