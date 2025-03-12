# ValueSet: Qualification Status VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Qualification Status VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Qualification Status VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/QualificationStatusVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: QualificationStatusVS |

The state indicating if a qualification is currently valid.

**References**

* [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)
* [Practitioner Qualification](StructureDefinition-practitioner-qualification.html)
* [Qualification](StructureDefinition-qualification.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/QualificationStatusCS`](CodeSystem-QualificationStatusCS.html)

### Expansion

This value set contains 6 concepts

Expansion based on [Qualification Status v1.1.0 (CodeSystem)](CodeSystem-QualificationStatusCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/QualificationStatusCS`](CodeSystem-QualificationStatusCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [active](CodeSystem-QualificationStatusCS.html#QualificationStatusCS-active) | active | The credential may be considered valid for use. |
| [inactive](CodeSystem-QualificationStatusCS.html#QualificationStatusCS-inactive) | inactive | The credential may not be considered valid for use. |
| [issiner](CodeSystem-QualificationStatusCS.html#QualificationStatusCS-issiner) | issued in error | The credential was mistakenly assigned and should not be considered valid for use. |
| [revoked](CodeSystem-QualificationStatusCS.html#QualificationStatusCS-revoked) | revoked | The credential was revoked by the issuing organization and should not be considered valid for use. |
| [pending](CodeSystem-QualificationStatusCS.html#QualificationStatusCS-pending) | pending | The credential has not been officially assigned. It may or may not be considered valid for use. |
| [unknown](CodeSystem-QualificationStatusCS.html#QualificationStatusCS-unknown) | unknown | The status of this credential is unknown. It may or may not be considered valid for use. |

---

Explanation of the columns that may appear on this page:

|  |  |
| --- | --- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the *display* element of a [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |