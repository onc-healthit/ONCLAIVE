xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Accessibility VS - FHIR v4.0.1

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
* **Accessibility VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Accessibility VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/AccessibilityVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: AccessibilityVS |

Codes for documenting general categories of accommodations available.

**References**

* [Accessibility](StructureDefinition-accessibility.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AccessibilityCS`](CodeSystem-AccessibilityCS.html)

### Expansion

This value set contains 7 concepts

Expansion based on [Accessibility CS v1.1.0 (CodeSystem)](CodeSystem-AccessibilityCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AccessibilityCS`](CodeSystem-AccessibilityCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [cultcomp](CodeSystem-AccessibilityCS.html#AccessibilityCS-cultcomp) | Cultural competence | Provides services that meet the social, cultural, and linguistic needs of persons. |
| [handiaccess](CodeSystem-AccessibilityCS.html#AccessibilityCS-handiaccess) | handicap accessible | Provides access to persons with disabilities. |
| [adacomp](CodeSystem-AccessibilityCS.html#AccessibilityCS-adacomp) | ADA compliant | Provides access which complies with the Americans with Disabilities Act and/or amendments. |
| [pubtrans](CodeSystem-AccessibilityCS.html#AccessibilityCS-pubtrans) | public transit options | Provides access using public transportation modes. |
| [anssrvc](CodeSystem-AccessibilityCS.html#AccessibilityCS-anssrvc) | answering service | Provides capability to communicate when intended recipient is not immediately available. |
| [cognitive](CodeSystem-AccessibilityCS.html#AccessibilityCS-cognitive) | cognitive | Provides services for cognitively impaired persons. |
| [mobility](CodeSystem-AccessibilityCS.html#AccessibilityCS-mobility) | mobility | Provides services for mobility impaired persons. |

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