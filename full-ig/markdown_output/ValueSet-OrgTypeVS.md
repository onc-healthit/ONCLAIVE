xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Organization Type VS - FHIR v4.0.1

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
* **Organization Type VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Organization Type VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/OrgTypeVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: OrgTypeVS |

Categories of organizations based on criteria in provider directories.

**References**

* [Plan-Net Organization](StructureDefinition-plannet-Organization.html)

### Logical Definition (CLD)

This value set includes codes based on the following rules:

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS`](CodeSystem-OrgTypeCS.html)

This value set excludes codes based on the following rules:

* Exclude these codes as defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS`](CodeSystem-OrgTypeCS.html)

  |  |  |  |
  | --- | --- | --- |
  | **Code** | **Display** | **Definition** |
  | [ntwk](CodeSystem-OrgTypeCS.html#OrgTypeCS-ntwk) | Network | A healthcare provider insurance network |

### Expansion

This value set contains 5 concepts

Expansion based on [Organization Type v1.1.0 (CodeSystem)](CodeSystem-OrgTypeCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS`](CodeSystem-OrgTypeCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [fac](CodeSystem-OrgTypeCS.html#OrgTypeCS-fac) | Facility | A physical healthcare facility. |
| [prvgrp](CodeSystem-OrgTypeCS.html#OrgTypeCS-prvgrp) | Provider Group | A healthcare provider entity |
| [payer](CodeSystem-OrgTypeCS.html#OrgTypeCS-payer) | Payer | A healthcare payer. |
| [atyprv](CodeSystem-OrgTypeCS.html#OrgTypeCS-atyprv) | Atypical Provider | Providers that do not provide healthcare |
| [bus](CodeSystem-OrgTypeCS.html#OrgTypeCS-bus) | Non-Healthcare Business | An organization that does not meet the definitions of a Healthcare or Atypical Provider, and is not a payer or healthcare facility |

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