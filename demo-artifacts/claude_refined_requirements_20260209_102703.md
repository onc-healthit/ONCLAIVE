# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

# REQ-001
**ID**: 01
**Summary**: Plan-Net service SHALL NOT require consumer identifying information
**Requirement**: "A conformant Plan-Net service SHALL NOT require a directory mobile application to send consumer identifying information in order to query content."
**Context**: Privacy considerations for Plan-Net services require that access to the directory should not require authentication and should not associate consumers with their queries. This requirement ensures that the server does not demand consumer-identifiable information from applications querying the directory.
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

# REQ-002
**ID**: 02
**Summary**: Directory mobile application SHALL NOT send consumer identifiable information
**Requirement**: "A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service."
**Context**: Privacy considerations require that client applications querying Plan-Net services must not transmit any information that could identify the consumer making the query. This protects consumer privacy during directory searches.
**Conformance**: "SHALL NOT"
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 7.1.2 Privacy Considerations
**Grouping**: Privacy
---
