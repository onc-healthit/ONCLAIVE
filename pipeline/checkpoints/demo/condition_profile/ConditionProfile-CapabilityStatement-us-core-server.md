# 14.3 CapabilityStatement: US Core Server CapabilityStatement

## 14.3 CapabilityStatement: US Core Server CapabilityStatement

 #### 14.3.3.5 Condition

Conformance Expectation: **SHALL**

Resource Specific Documentation:

> * For Encounter Diagnosis use the *US Core Condition Encounter Diagnosis Profile*.
>   + When `Condition.category` is "encounter-diagnosis" the encounter, **SHOULD** be referenced in `Condition.encounter`.
> * For Problems and Health Concerns use the *US Core Condition Problems and Health Concerns Profile*.
>   + When `Condition.category` is a "problems-list-item", the `Condition.clinicalStatus **SHOULD** be present.
>   + There is no single element in Condition that represents the date of diagnosis. It may be the assertedDate Extension, `Condition.onsetDateTime`, or `Condition.recordedDate`.
>     - Although all three are marked as must support, the server is not required to support all.
>     - A server **SHALL** support `Condition.recordedDate`.
>       * A server **SHALL** support at least one of the assertedDate Extension and `Condition.onsetDateTime`. A server may support both, which means they support all three elements.
>       * The client application **SHALL** support all three elements.
>   + See the US Core General Guidance page for [Searching Using lastUpdated](general-guidance.html#searching-using-lastupdated). Updates to `Condition.meta.lastUpdated` **SHOULD** reflect:
>     - New problems and health concerns
>     - Changes in the clinical status or verifications status of problems or health concern

Supported Profiles:

* **SHALL** support: [US Core Condition Encounter Diagnosis Profile](StructureDefinition-us-core-condition-encounter-diagnosis.html)
* **SHALL** support: [US Core Condition Problems and Health Concerns Profile](StructureDefinition-us-core-condition-problems-health-concerns.html)

Profile Interaction Summary:

* **SHALL** support `search-type`, `read`.
* **SHOULD** support `vread`, `history-instance`.
* **MAY** support `create`, `update`, `patch`, `delete`, `history-type`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a Condition resource using: `GET [base]/Condition/[id]`
* A Server **SHALL** be capable of supporting the following \_revincludes: Provenance:target - `GET [base]/Condition?[parameter=value]&_revinclude=Provenance:target`

Search Parameter Summary:

| Conformance | Parameter | Type |
| --- | --- | --- |
| **SHALL** | [patient](SearchParameter-us-core-condition-patient.html) | reference |

Search Parameter Combination Summary:

| Conformance | Parameter Combination | Types |
| --- | --- | --- |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [category](SearchParameter-us-core-condition-category.html)+  [encounter](SearchParameter-us-core-condition-encounter.html) | reference+token+reference |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [recorded-date](SearchParameter-us-core-condition-recorded-date.html) | reference+date |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [\_lastUpdated](SearchParameter-us-core-condition-lastupdated.html) | reference+date |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [category](SearchParameter-us-core-condition-category.html)+  [clinical-status](SearchParameter-us-core-condition-clinical-status.html) | reference+token+token |
| **SHALL** | [patient](SearchParameter-us-core-condition-patient.html)+  [category](SearchParameter-us-core-condition-category.html) | reference+token |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [onset-date](SearchParameter-us-core-condition-onset-date.html) | reference+date |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [code](SearchParameter-us-core-condition-code.html) | reference+token |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [clinical-status](SearchParameter-us-core-condition-clinical-status.html) | reference+token |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [asserted-date](SearchParameter-us-core-condition-asserted-date.html) | reference+date |
| **SHOULD** | [patient](SearchParameter-us-core-condition-patient.html)+  [abatement-date](SearchParameter-us-core-condition-abatement-date.html) | reference+date |

Search Parameter Requirements (When Used Alone or in Combination):

* [abatement-date](SearchParameter-us-core-condition-abatement-date.html) (date):

  A client **SHALL** provide a value precise to the *second + time offset*.

  A server **SHALL** support a value precise to the *second + time offset*.
* [asserted-date](SearchParameter-us-core-condition-asserted-date.html) (date):

  A client **SHALL** provide a value precise to the *second + time offset*.

  A server **SHALL** support a value precise to the *second + time offset*.
* [category](SearchParameter-us-core-condition-category.html) (token):

  The client **SHALL** provide at least a code value and **MAY** provide both the system and code values.

  The server **SHALL** support both.
* [clinical-status](SearchParameter-us-core-condition-clinical-status.html) (token):

  The client **SHALL** provide at least a code value and **MAY** provide both the system and code values.

  The server **SHALL** support both.
* [code](SearchParameter-us-core-condition-code.html) (token):

  The client **SHALL** provide at least a code value and **MAY** provide both the system and code values.

  The server **SHALL** support both.
* [encounter](SearchParameter-us-core-condition-encounter.html) (reference):

  The client **SHALL** provide at least a id value and **MAY** provide both the Type and id values.

  The server **SHALL** support both.
* [onset-date](SearchParameter-us-core-condition-onset-date.html) (date):

  A client **SHALL** provide a value precise to the *second + time offset*.

  A server **SHALL** support a value precise to the *second + time offset*.
* [patient](SearchParameter-us-core-condition-patient.html) (reference):

  The client **SHALL** provide at least a id value and **MAY** provide both the Type and id values.

  The server **SHALL** support both.
* [recorded-date](SearchParameter-us-core-condition-recorded-date.html) (date):

  A client **SHALL** provide a value precise to the *second + time offset*.

  A server **SHALL** support a value precise to the *second + time offset*.
* [\_lastUpdated](SearchParameter-us-core-condition-lastupdated.html) (date):

  A server **SHALL** document the types of changes that can be detected using this parameter.

  A client **SHALL** provide a value precise to the *second + time offset*.

  A server **SHALL** support a value precise to the *second + time offset*.

---
