# ValueSet: Accepting Patients Codes VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Accepting Patients Codes VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Accepting Patients Codes VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/AcceptingPatientsVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: AcceptingPatientsVS |

Codes to identify if the practice is accepting new patients

**References**

* [New Patients](StructureDefinition-newpatients.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AcceptingPatientsCS`](CodeSystem-AcceptingPatientsCS.html)

### Expansion

This value set contains 4 concepts

Expansion based on [Accepting Patients Codes v1.1.0 (CodeSystem)](CodeSystem-AcceptingPatientsCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AcceptingPatientsCS`](CodeSystem-AcceptingPatientsCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [nopt](CodeSystem-AcceptingPatientsCS.html#AcceptingPatientsCS-nopt) | Not Accepting | Not accepting patients |
| [newpt](CodeSystem-AcceptingPatientsCS.html#AcceptingPatientsCS-newpt) | Accepting | Accepting patients |
| [existptonly](CodeSystem-AcceptingPatientsCS.html#AcceptingPatientsCS-existptonly) | Accepting existing patients | Accepting existing patients |
| [existptfam](CodeSystem-AcceptingPatientsCS.html#AcceptingPatientsCS-existptfam) | Accepting existing patients and their families | Accepting existing patients and members of their families |

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