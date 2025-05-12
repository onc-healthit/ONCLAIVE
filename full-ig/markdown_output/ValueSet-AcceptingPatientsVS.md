xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Accepting Patients Codes VS - FHIR v4.0.1

[![Visit the HL7 website](assets/images/hl7-logo-header.png)](http://hl7.org)

[![Visit the FHIR website](assets/images/fhir-logo-www.png)](http://hl7.org/fhir)

[![Search FHIR](assets/images/search.png)](searchform.html)

[![Visit the Da Vinci website](assets/images/da-vinci_logo.jpg)](http://hl7.org/about/davinci)

DaVinci PDEX Plan Net

1.1.0 - STU 1.1
US

[FHIR](http://hl7.org/fhir/R4/index.html)

* [Home](index.html)
* [Implementation](#)
  + [Implementation](implementation.html)
  + [Representing Provider Directories in Plan Net](implementation.html#Representing)
* [FHIR Artifacts](#)
  + [Profiles](artifacts.html#3)
  + [Extensions](artifacts.html#4)
  + [Search Parameters](artifacts.html#2)
  + [Terminology](artifacts.html#5)
  + [Capability Statement](artifacts.html#1)
* [Examples](artifacts.html#7)
* [Downloads](downloads.html)
* [Change History](ChangeHistory.html)
* [History](http://www.hl7.org/fhir/us/davinci-pdex-plan-net/history.cfml)

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

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)