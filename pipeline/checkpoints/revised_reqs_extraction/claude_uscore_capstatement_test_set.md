---
# REQ-018
**Summary**: Server SHALL support search-type and read interactions for Condition
**Text**: "**SHALL** support `search-type`, `read`."
**Context**: Required interactions for Condition resource in US Core Server
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition Profile Interaction Summary
---

---
# REQ-019
**Summary**: Server SHALL support patient search parameter for Condition
**Text**: "**SHALL** [patient](SearchParameter-us-core-condition-patient.html) reference"
**Context**: Required search parameter support for finding Condition resources by patient
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition Search Parameter Summary
---

---
# REQ-020
**Summary**: Server SHALL support patient+category search combination for Condition
**Text**: "**SHALL** [patient](SearchParameter-us-core-condition-patient.html)+ [category](SearchParameter-us-core-condition-category.html) reference+token"
**Context**: Required search parameter combination for Condition resources
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition Search Parameter Combination Summary
---

---
# REQ-021
**Summary**: Server SHALL support Condition.recordedDate
**Text**: "A server **SHALL** support `Condition.recordedDate`."
**Context**: Required support for recorded date element in Condition resources for diagnosis date tracking
**Verification**: Test
**Actor**: US Core Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Section 14.3.3.5 Condition Resource Specific Documentation
---
