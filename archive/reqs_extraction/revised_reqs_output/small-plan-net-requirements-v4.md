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
