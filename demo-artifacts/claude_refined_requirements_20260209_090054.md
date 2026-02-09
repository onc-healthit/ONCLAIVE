# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Plan-Net service SHALL NOT require consumer identifying information
**Requirement**: "A conformant Plan-Net service SHALL NOT require a directory mobile application to send consumer identifying information in order to query content."
**Context**: As part of privacy considerations, the Plan-Net service must not impose requirements on directory mobile applications that would force them to send consumer identifying information when querying directory content. This protects consumer privacy by ensuring queries can be made anonymously.
**Conformance**: "SHALL NOT"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 7.1.2 Privacy Considerations
**Grouping**: Privacy
---

---
# REQ-002
**ID**: 02
**Summary**: Directory mobile application SHALL NOT send consumer identifiable information
**Requirement**: "A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service."
**Context**: As part of privacy considerations, directory mobile applications must not send any information that could identify the consumer when making queries to a Plan-Net service. This is a client-side requirement that complements the server-side requirement to not require such information.
**Conformance**: "SHALL NOT"
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Attestation"
**Section**: 7.1.2 Privacy Considerations
**Grouping**: Privacy
---
