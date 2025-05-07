xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Plan-Net Organization - Mappings - FHIR v4.0.1

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
* **Plan-Net Organization**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-Organization.html)
* [Detailed Descriptions](StructureDefinition-plannet-Organization-definitions.html)
* [Mappings](#)
* [Examples](StructureDefinition-plannet-Organization-examples.html)

## Resource Profile: PlannetOrganization - Mappings

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Mappings for the plannet-Organization resource profile.

### Mappings for ServD (<http://www.omg.org/spec/ServD/1.0/>)

|  |  |  |
| --- | --- | --- |
| **PlannetOrganization** | | |
| Organization | Organization |
| identifier | ./Identifiers, n/a |
| system | ./IdentifierType |
| value | ./Value |
| period | ./StartDate and ./EndDate |
| assigner | ./IdentifierIssuingAuthority |
| identifier (NPI) | ./Identifiers, n/a |
| identifier (CLIA) | ./Identifiers, n/a |
| active | ./Status (however this concept in ServD more covers why the organization is active or not, could be delisted, deregistered, not operational yet) this could alternatively be derived from ./StartDate and ./EndDate and given a context date. |
| type | n/a |
| name | .PreferredName/Name, ./PrimaryAddress and ./OtherAddresses |
| telecom | ./ContactPoints |
| system | ./ContactPointType |
| value | ./Value |
| use | ./ContactPointPurpose |
| period | ./StartDate and ./EndDate |
| address | ./PrimaryAddress and ./OtherAddresses, n/a |
| use | ./AddressPurpose |
| line | ./StreetAddress (newline delimitted) |
| city | ./Jurisdiction |
| state | ./Region, ./Sites |
| postalCode | ./PostalIdentificationCode |
| country | ./Country |
| period | ./StartDate and ./EndDate |
| partOf | n/a |
| contact |  |
| telecom |  |
| system | ./ContactPointType |
| value | ./Value |
| use | ./ContactPointPurpose |
| period | ./StartDate and ./EndDate |

### Mappings for HL7 v2 Mapping ([http://hl7.org/v2](http://hl7.org/comparison-v2.html))

|  |  |  |
| --- | --- | --- |
| **PlannetOrganization** | | |
| Organization | (also see master files messages) |
| identifier | XON.10 / XON.3 |
| use | N/A |
| type | CX.5 |
| system | CX.4 / EI-2-4 |
| value | CX.1 / EI.1 |
| period | CX.7 + CX.8 |
| assigner | CX.4 / (CX.4,CX.9,CX.10) |
| identifier (NPI) | XON.10 / XON.3 |
| identifier (CLIA) | XON.10 / XON.3 |
| active | No equivalent in HL7 v2 |
| type | No equivalent in v2 |
| name | XON.1 |
| telecom | ORC-22? |
| system | XTN.3 |
| value | XTN.1 (or XTN.12) |
| use | XTN.2 - but often indicated by field |
| rank | n/a |
| period | N/A |
| address | ORC-23? |
| use | XAD.7 |
| type | XAD.18 |
| text | XAD.1 + XAD.2 + XAD.3 + XAD.4 + XAD.5 + XAD.6 |
| line | XAD.1 + XAD.2 (note: XAD.1 and XAD.2 have different meanings for a company address than for a person address) |
| city | XAD.3 |
| district | XAD.9 |
| state | XAD.4 |
| postalCode | XAD.5 |
| country | XAD.6 |
| period | XAD.12 / XAD.13 + XAD.14 |
| partOf | No equivalent in HL7 v2 |
| contact |  |
| name | PID-5, PID-9 |
| telecom | PID-13, PID-14 |
| system | XTN.3 |
| value | XTN.1 (or XTN.12) |
| use | XTN.2 - but often indicated by field |
| rank | n/a |
| period | N/A |
| address | PID-11 |

### Mappings for RIM Mapping ([http://hl7.org/v3](http://hl7.org/comparison-v3.html))

|  |  |  |
| --- | --- | --- |
| **PlannetOrganization** | | |
| Organization | Entity. Role, or Act, Organization(classCode=ORG, determinerCode=INST) |
| meta |  |
| id | n/a |
| extension | n/a |
| text | Act.text? |
| contained | N/A |
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
| identifier (NPI) | .scopes[Role](classCode=IDENT) |
| identifier (CLIA) | .scopes[Role](classCode=IDENT) |
| active | .status |
| type | .code |
| name | .name |
| alias | .name |
| telecom | .telecom |
| id | n/a |
| extension | n/a |
| system | ./scheme |
| value | ./url |
| use | unique(./use) |
| rank | n/a |
| period | ./usablePeriod[type="IVL<TS>"] |
| address | .address |
| id | n/a |
| extension | n/a |
| use | unique(./use) |
| type | unique(./use) |
| text | ./formatted |
| line | AD.part[parttype = AL] |
| city | AD.part[parttype = CTY] |
| district | AD.part[parttype = CNT | CPA] |
| state | AD.part[parttype = STA] |
| postalCode | AD.part[parttype = ZIP] |
| country | AD.part[parttype = CNT] |
| period | ./usablePeriod[type="IVL<TS>"] |
| partOf | .playedBy[classCode=Part].scoper |
| contact | .contactParty |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| purpose | ./type |
| name | ./name |
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

### Mappings for FiveWs Pattern Mapping (http://hl7.org/fhir/fivews)

|  |  |  |
| --- | --- | --- |
| **PlannetOrganization** | | |
| Organization |  |
| identifier | FiveWs.identifier |
| identifier (NPI) | FiveWs.identifier |
| identifier (CLIA) | FiveWs.identifier |
| active | FiveWs.status |
| type | FiveWs.class |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)