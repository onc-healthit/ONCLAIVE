# CodeSystem: Qualification Status

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Qualification Status**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## CodeSystem: Qualification Status

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/QualificationStatusCS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: QualificationStatusCS |

The state indicating if a qualification is currently valid.

This Code system is referenced in the content logical definition of the following value sets:

* [QualificationStatusVS](ValueSet-QualificationStatusVS.html)

This code system http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/QualificationStatusCS defines the following codes:

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| active | active | The credential may be considered valid for use. |
| inactive | inactive | The credential may not be considered valid for use. |
| issiner | issued in error | The credential was mistakenly assigned and should not be considered valid for use. |
| revoked | revoked | The credential was revoked by the issuing organization and should not be considered valid for use. |
| pending | pending | The credential has not been officially assigned. It may or may not be considered valid for use. |
| unknown | unknown | The status of this credential is unknown. It may or may not be considered valid for use. |