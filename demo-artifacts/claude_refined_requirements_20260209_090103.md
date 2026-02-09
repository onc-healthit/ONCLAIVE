# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

# REQ-001
**ID**: 01
**Summary**: NetworkReference Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the NetworkReference extension's URL element. The extension URL must be fixed to the canonical URI that identifies the NetworkReference extension structure definition. This ensures consistent identification of the extension across implementations.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: NetworkReference - Detailed Descriptions
**Grouping**: PractitionerRole

---

# REQ-002
**ID**: 02
**Summary**: NetworkReference Extension Must Support value[x] Element
**Requirement**: "Extension.value[x] [Must Support is] true"
**Context**: The NetworkReference extension's value[x] element, which contains a reference to a Plan-Net Network resource, must be supported by implementations. This element is marked as Must Support, indicating that systems claiming conformance must be capable of populating and processing this element.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Attestation
**Section**: 11.72.1 Extension: NetworkReference - Detailed Descriptions
**Grouping**: PractitionerRole

---

# REQ-003
**ID**: 03
**Summary**: NetworkReference Extension value[x] Cardinality
**Requirement**: "Extension.value[x] [Control is] 1.1"
**Context**: The NetworkReference extension's value[x] element has a cardinality of 1..1, meaning it is required and must contain exactly one value. This ensures that when the NetworkReference extension is used, it must contain a reference to a Plan-Net Network resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: NetworkReference - Detailed Descriptions
**Grouping**: PractitionerRole

---

# REQ-004
**ID**: 04
**Summary**: NetworkReference Extension Invariant ele-1
**Requirement**: "All FHIR elements must have a @value or children (hasValue() or (children().count() > id.count()))"
**Context**: This is a base FHIR invariant (ele-1) that applies to all FHIR elements in the NetworkReference extension. Every element must either have a value attribute or have child elements (excluding only the id element). This ensures data integrity and proper FHIR structure.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: NetworkReference - Detailed Descriptions
**Grouping**: PractitionerRole
