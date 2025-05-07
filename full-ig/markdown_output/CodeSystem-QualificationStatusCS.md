xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Qualification Status - FHIR v4.0.1

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

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)