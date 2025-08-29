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

