# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Server systems SHALL meet Plan-Net CapabilityStatement requirements
**Requirement**: "Server systems claiming conformance to this guide **SHALL** meet the capability statement expectation requirements identified in the [Plan-Net CapabilityStatement](CapabilityStatement-plan-net.html)"
**Context**: This requirement mandates that server systems implementing the Plan-Net IG must satisfy all capability statement expectation requirements defined in the Plan-Net CapabilityStatement resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: Plan-Net CapabilityStatement requirements
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 4.1 Conformance Expectations
**Grouping**: Capability Statement
---

---
# REQ-002
**ID**: 02
**Summary**: Server CapabilityStatement SHALL declare instantiation of Plan-Net CapabilityStatement
**Requirement**: "Server systems claiming conformance to this guide **SHALL** have a CapabilityStatement that has a CapabilityStatement.instantiates with a URL of http://hl7.org/fhir/us/davinci-drug-formulary/CapabilityStatement/usdf-server or a URL to the appropriate version of the CapabilityStatement."
**Context**: This requirement specifies that server systems must declare their conformance to the Plan-Net IG by including the appropriate CapabilityStatement URL in their CapabilityStatement.instantiates element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 4.1 Conformance Expectations
**Grouping**: Capability Statement
---

---
# REQ-003
**ID**: 03
**Summary**: Server MAY support Bulk Data IG for directory data retrieval
**Requirement**: "A server MAY support [Bulk Data IG](http://hl7.org/fhir/uv/bulkdata/index.html) for the retrieval of directory data."
**Context**: The implementation guide allows but does not require servers to support the FHIR Bulk Data IG for retrieval of directory data. This provides an optional mechanism for bulk export of provider directory information. Note that this guidance is draft and has not been balloted or fully tested.
**Conformance**: MAY
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 7.3 Bulk Data
**Grouping**: Capability Statement
---

---
# REQ-004
**ID**: 04
**Summary**: Plan-Net Server SHALL support all profiles defined in this Implementation Guide
**Requirement**: "The Plan-Net Server SHALL: Support all profiles defined in this Implementation Guide."
**Context**: This requirement establishes that the Plan-Net Server must implement all profiles specified within the DaVinci PDEX Plan-Net Implementation Guide to ensure complete conformance with the specification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement
---

---
# REQ-005
**ID**: 05
**Summary**: Plan-Net Server SHALL implement RESTful behavior according to FHIR specification
**Requirement**: "The Plan-Net Server SHALL: Implement the RESTful behavior according to the FHIR specification."
**Context**: This requirement mandates that the server must conform to the RESTful architectural style and behaviors as defined in the FHIR specification, including proper use of HTTP methods, status codes, and resource interactions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement
---

---
# REQ-006
**ID**: 06
**Summary**: Plan-Net Server SHALL return specified HTTP response status codes
**Requirement**: "The Plan-Net Server SHALL: Return the following response classes: (Status 400): invalid parameter; (Status 401/4xx): unauthorized request; (Status 403): insufficient scope; (Status 404): unknown resource; (Status 410): deleted resource."
**Context**: This requirement specifies the mandatory HTTP status codes that must be returned by the server for various error conditions, ensuring consistent error handling across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement
---

---
# REQ-007
**ID**: 07
**Summary**: Plan-Net Server SHALL support json source formats for all interactions
**Requirement**: "The Plan-Net Server SHALL: Support json source formats for all Plan-Net interactions."
**Context**: This requirement mandates that the server must be capable of accepting and returning FHIR resources in JSON format for all supported interactions.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement
---

---
# REQ-008
**ID**: 08
**Summary**: Plan-Net Server SHALL support searchParameters on each profile individually and in combination
**Requirement**: "The Plan-Net Server SHALL: Support the searchParameters on each profile individually and in combination."
**Context**: This requirement establishes that the server must support searching using individual search parameters as well as combining multiple search parameters in a single query for each profile.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement
---

---
# REQ-009
**ID**: 09
**Summary**: Plan-Net Server SHALL support forward and reverse chaining on search parameters
**Requirement**: "The Plan-Net Server SHALL: Support forward and reverse chaining on all search parameters that specify the 'chain' property"
**Context**: This requirement mandates support for chaining search parameters (both forward using dot notation and reverse using _has) on all search parameters that define the chain property, enabling complex queries across resource references.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement
---

---
# REQ-010
**ID**: 10
**Summary**: Plan-Net Server SHOULD support xml source formats for all interactions
**Requirement**: "The Plan-Net Server SHOULD: Support xml source formats for all Plan-Net interactions."
**Context**: This requirement recommends that the server should be capable of accepting and returning FHIR resources in XML format for all supported interactions, though this is not mandatory.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Capability Statement
---

---
# REQ-011
**ID**: 11
**Summary**: Query-Only API Support
**Requirement**: "This is a query only API (GET) and does not support PUT or POST."
**Context**: The Plan-Net API is explicitly designed as a read-only interface. The server SHALL NOT support create or update operations (PUT/POST), only retrieval operations (GET). This is a fundamental constraint on the API's capabilities.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 1.1 Introduction
**Grouping**: Capability Statement
---
