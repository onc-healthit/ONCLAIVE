xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Plan-Net InsurancePlan - Mappings - FHIR v4.0.1

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
* **Plan-Net InsurancePlan**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-InsurancePlan.html)
* [Detailed Descriptions](StructureDefinition-plannet-InsurancePlan-definitions.html)
* [Mappings](#)
* [Examples](StructureDefinition-plannet-InsurancePlan-examples.html)

## Resource Profile: PlannetInsurancePlan - Mappings

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Mappings for the plannet-InsurancePlan resource profile.

### Mappings for FiveWs Pattern Mapping (http://hl7.org/fhir/fivews)

|  |  |  |
| --- | --- | --- |
| **PlannetInsurancePlan** | | |
| InsurancePlan |  |
| identifier | FiveWs.identifier |
| status | FiveWs.status |
| type | FiveWs.class |
| plan |  |
| identifier | FiveWs.identifier |

### Mappings for RIM Mapping ([http://hl7.org/v3](http://hl7.org/comparison-v3.html))

|  |  |  |
| --- | --- | --- |
| **PlannetInsurancePlan** | | |
| InsurancePlan | Entity. Role, or Act |
| meta |  |
| id | n/a |
| extension | n/a |
| text | Act.text? |
| contained | N/A |
| extension | N/A |
| modifierExtension | N/A |
| identifier | .scopes[Role](classCode=IDENT) |
| id | n/a |
| extension | n/a |
| use | Role.code or implied by context |
| type | Role.code or implied by context |
| system | II.root or Role.id.root |
| value | II.extension or II.root if system indicates OID or GUID (Or Role.id.extension or root) |
| period | Role.effectiveTime or implied by context |
| assigner | II.assigningAuthorityName but note that this is an improper use by the definition of the field. Also Role.scoper |
| status | .status |
| type | .code |
| name | .name |
| alias | .name |
| contact | .contactParty |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| purpose | ./type |
| name | ./name |
| id | n/a |
| extension | n/a |
| use | unique(./use) |
| text | ./formatted |
| family | ./part[partType = FAM] |
| given | ./part[partType = GIV] |
| prefix | ./part[partType = PFX] |
| suffix | ./part[partType = SFX] |
| period | ./usablePeriod[type="IVL<TS>"] |
| telecom | ./telecom |
| id | n/a |
| extension | n/a |
| system | ./scheme |
| value | ./url |
| use | unique(./use) |
| rank | n/a |
| period | ./usablePeriod[type="IVL<TS>"] |
| address | ./addr |
| endpoint | n/a |
| coverage |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| benefit |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| limit |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| plan |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| identifier | .scopes[Role](classCode=IDENT) |
| generalCost |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| specificCost |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| benefit |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| cost |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)