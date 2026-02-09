# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Conformance to Da Vinci HRex Security Guidelines
**Requirement**: "Users of this implementation guide SHALL conform to the Da Vinci HRex guidelines on privacy, safety, and security."
**Context**: This requirement establishes that all implementations of the Plan-Net Implementation Guide must adhere to the security, privacy, and safety guidelines defined in the Da Vinci HRex specification STU1.1. This ensures a consistent baseline of security practices across Da Vinci implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: Da Vinci HRex STU1.1 Security Requirements
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 10 Security
**Grouping**: Security
---

---
# REQ-002
**ID**: 02
**Summary**: Plan-Net Server SHALL reject unauthorized requests with HTTP 401
**Requirement**: "A server SHALL reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."
**Context**: This security requirement mandates that the server must return an HTTP 401 status code when rejecting requests that lack proper authorization credentials.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.1 FHIR RESTful Capabilities
**Grouping**: Security
---

---
# REQ-003
**ID**: 03
**Summary**: InsurancePlan contained resource SHALL NOT have security label
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label"
**Context**: This is a base FHIR constraint (dom-5) preventing security labels on contained resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Only applies when the InsurancePlan resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.59.1 Resource Profile: PlannetInsurancePlan - Detailed Descriptions, Invariant dom-5
**Grouping**: Security
---
