---
# REQ-01-01
**Summary**: Plan-Net service must not require authentication to access
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Test/Inspection
**Actor**: Server
**Conformance**: SHOULD
**Conditional**: False
**Source**: Privacy Considerations Section
---

# REQ-01-02
**Summary**: Plan-Net service must not require consumer identifying information
**Description**: "A conformant Plan-Net service SHALL NOT require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Privacy Considerations Section
---

# REQ-01-03
**Summary**: Directory applications must not send consumer identifiable information
**Description**: "A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service."
**Verification**: Test
**Actor**: Client Application
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Privacy Considerations Section
---

# REQ-01-04
**Summary**: Health Plan API must populate all Must Support data elements
**Description**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section
---

# REQ-01-05
**Summary**: Health Plan API must exclude empty optional data elements
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors SHALL NOT include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: True
**Source**: Must Support Section
---

# REQ-01-06
**Summary**: Health Plan API must provide reason for missing required data elements
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 [Health Plan API actors] SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: True
**Source**: Must Support Section
---

# REQ-01-07
**Summary**: Applications must process resources with Must Support elements
**Description**: "Application actors SHALL be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section
---

# REQ-01-08
**Summary**: Applications should display Must Support data elements
**Description**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Test/Demonstration
**Actor**: Application
**Conformance**: SHOULD
**Conditional**: False
**Source**: Must Support Section
---

# REQ-01-09
**Summary**: Applications must interpret missing Must Support elements as data not present
**Description**: "When querying Health Plan API actors, Application actors SHALL interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Actor**: Application
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section
---

# REQ-01-10
**Summary**: Consumer applications must process resources with missing information indicators
**Description**: "Consumer App actors SHALL be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Actor**: Consumer App
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section
---