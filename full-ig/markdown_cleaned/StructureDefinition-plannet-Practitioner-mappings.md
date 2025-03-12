# Resource Profile: PlannetPractitioner - Mappings

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net Practitioner**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-Practitioner.html)
* [Detailed Descriptions](StructureDefinition-plannet-Practitioner-definitions.html)
* [Mappings](#)
* [Examples](StructureDefinition-plannet-Practitioner-examples.html)

## Resource Profile: PlannetPractitioner - Mappings

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Mappings for the plannet-Practitioner resource profile.

### Mappings for HL7 v2 Mapping ([http://hl7.org/v2](http://hl7.org/comparison-v2.html))

|  |  |  |
| --- | --- | --- |
| **PlannetPractitioner** | | |
| Practitioner | PRD (as one example) |
| identifier | PRD-7 (or XCN.1) |
| use | N/A |
| type | CX.5 |
| system | CX.4 / EI-2-4 |
| value | CX.1 / EI.1 |
| period | CX.7 + CX.8 |
| assigner | CX.4 / (CX.4,CX.9,CX.10) |
| identifier (NPI) | PRD-7 (or XCN.1) |
| name | XCN Components |
| use | XPN.7, but often indicated by which field contains the name |
| text | implied by XPN.11 |
| family | XPN.1/FN.1 |
| given | XPN.2 + XPN.3 |
| prefix | XPN.5 |
| suffix | XPN/4 |
| period | XPN.13 + XPN.14 |
| telecom | PRT-15, STF-10, ROL-12 |
| system | XTN.3 |
| value | XTN.1 (or XTN.12) |
| use | XTN.2 - but often indicated by field |
| rank | n/a |
| period | N/A |
| address | ORC-24, STF-11, ROL-11, PRT-14 |
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
| gender | STF-5 |
| birthDate | STF-6 |
| qualification | CER? |
| communication | PID-15, NK1-20, LAN-2 |
| coding | C\*E.1-8, C\*E.10-22 |
| text | C\*E.9. But note many systems use C\*E.2 for this |

### Mappings for RIM Mapping ([http://hl7.org/v3](http://hl7.org/comparison-v3.html))

|  |  |  |
| --- | --- | --- |
| **PlannetPractitioner** | | |
| Practitioner | Entity. Role, or Act, Role |
| meta |  |
| id | n/a |
| extension | n/a |
| text | Act.text? |
| contained | N/A |
| extension | N/A |
| modifierExtension | N/A |
| identifier | ./id |
| id | n/a |
| extension | n/a |
| use | Role.code or implied by context |
| type | Role.code or implied by context |
| system | II.root or Role.id.root |
| value | II.extension or II.root if system indicates OID or GUID (Or Role.id.extension or root) |
| period | Role.effectiveTime or implied by context |
| assigner | II.assigningAuthorityName but note that this is an improper use by the definition of the field. Also Role.scoper |
| identifier (NPI) | ./id |
| active | ./statusCode |
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
| gender | ./administrativeGender |
| birthDate | ./birthTime |
| photo | ./subjectOf/ObservationEvent[code="photo"]/value |
| qualification | .playingEntity.playingRole[classCode=QUAL].code |
| id | n/a |
| modifierExtension | N/A |
| identifier | .playingEntity.playingRole[classCode=QUAL].id |
| code | .playingEntity.playingRole[classCode=QUAL].code |
| period | .playingEntity.playingRole[classCode=QUAL].effectiveTime |
| issuer | .playingEntity.playingRole[classCode=QUAL].scoper |
| communication | ./languageCommunication |
| id | n/a |
| extension | n/a |
| coding | union(., ./translation) |
| text | ./originalText[mediaType/code="text/plain"]/data |

### Mappings for ServD (<http://www.omg.org/spec/ServD/1.0/>)

|  |  |  |
| --- | --- | --- |
| **PlannetPractitioner** | | |
| Practitioner | Provider |
| identifier | ./Identifiers |
| system | ./IdentifierType |
| value | ./Value |
| period | ./StartDate and ./EndDate |
| assigner | ./IdentifierIssuingAuthority |
| identifier (NPI) | ./Identifiers |
| name | ./PreferredName (GivenNames, FamilyName, TitleCode) |
| use | ./NamePurpose |
| family | ./FamilyName |
| given | ./GivenNames |
| prefix | ./TitleCode |
| period | ./StartDate and ./EndDate |
| telecom | ./ContactPoints |
| system | ./ContactPointType |
| value | ./Value |
| use | ./ContactPointPurpose |
| period | ./StartDate and ./EndDate |
| address | ./Addresses |
| use | ./AddressPurpose |
| line | ./StreetAddress (newline delimitted) |
| city | ./Jurisdiction |
| state | ./Region |
| postalCode | ./PostalIdentificationCode |
| country | ./Country |
| period | ./StartDate and ./EndDate |
| gender | ./GenderCode |
| birthDate | (not represented in ServD) |
| photo | ./ImageURI (only supports the URI reference) |
| qualification | ./Qualifications |
| code | ./Qualifications.Value |
| period | ./Qualifications.StartDate and ./Qualifications.EndDate |
| communication | ./Languages.LanguageSpokenCode |

### Mappings for FiveWs Pattern Mapping (http://hl7.org/fhir/fivews)

|  |  |  |
| --- | --- | --- |
| **PlannetPractitioner** | | |
| Practitioner |  |
| identifier | FiveWs.identifier |
| identifier (NPI) | FiveWs.identifier |
| active | FiveWs.status |