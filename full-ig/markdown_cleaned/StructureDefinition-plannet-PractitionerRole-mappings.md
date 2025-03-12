# Resource Profile: PlannetPractitionerRole - Mappings

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net PractitionerRole**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-PractitionerRole.html)
* [Detailed Descriptions](StructureDefinition-plannet-PractitionerRole-definitions.html)
* [Mappings](#)
* [Examples](StructureDefinition-plannet-PractitionerRole-examples.html)

## Resource Profile: PlannetPractitionerRole - Mappings

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Mappings for the plannet-PractitionerRole resource profile.

### Mappings for HL7 v2 Mapping ([http://hl7.org/v2](http://hl7.org/comparison-v2.html))

|  |  |  |
| --- | --- | --- |
| **PlannetPractitionerRole** | | |
| PractitionerRole | PRD (as one example) |
| identifier | PRD-7 (or XCN.1) |
| use | N/A |
| type | CX.5 |
| system | CX.4 / EI-2-4 |
| value | CX.1 / EI.1 |
| period | CX.7 + CX.8 |
| assigner | CX.4 / (CX.4,CX.9,CX.10) |
| active | STF-7 |
| period | PRD-8/9 / PRA-5.4 |
| code | PRD-1 / STF-18 / PRA-3 / PRT-4 / ROL-3 / ORC-12 / OBR-16 / PV1-7 / PV1-8 / PV1-9 / PV1-17 |
| specialty | PRA-5 |
| healthcareService | EDU-2 / AFF-3 |
| telecom |  |
| system | XTN.3 |
| value | XTN.1 (or XTN.12) |
| use | XTN.2 - but often indicated by field |
| rank | n/a |
| period | N/A |

### Mappings for RIM Mapping ([http://hl7.org/v3](http://hl7.org/comparison-v3.html))

|  |  |  |
| --- | --- | --- |
| **PlannetPractitionerRole** | | |
| PractitionerRole | Entity. Role, or Act, Role |
| meta |  |
| id | n/a |
| extension | n/a |
| text | Act.text? |
| contained | N/A |
| extension |  |
| extension (newpatients) |  |
| extension (network-reference) |  |
| extension (qualification) |  |
| id | n/a |
| extension |  |
| extension (identifier) |  |
| id | n/a |
| url | N/A |
| value[x] | N/A |
| extension (code) |  |
| id | n/a |
| url | N/A |
| value[x] | N/A |
| extension (issuer) |  |
| id | n/a |
| url | N/A |
| value[x] | N/A |
| extension (status) |  |
| id | n/a |
| url | N/A |
| value[x] | N/A |
| value[x] (valueCode) | N/A |
| extension (period) |  |
| id | n/a |
| url | N/A |
| value[x] | N/A |
| extension (whereValid) |  |
| id | n/a |
| url | N/A |
| value[x] | N/A |
| url | N/A |
| modifierExtension | N/A |
| identifier | .id |
| id | n/a |
| extension | n/a |
| use | Role.code or implied by context |
| type | Role.code or implied by context |
| system | II.root or Role.id.root |
| value | II.extension or II.root if system indicates OID or GUID (Or Role.id.extension or root) |
| period | Role.effectiveTime or implied by context |
| assigner | II.assigningAuthorityName but note that this is an improper use by the definition of the field. Also Role.scoper |
| active | .statusCode |
| period | .performance[@typeCode <= 'PPRF'].ActDefinitionOrEvent.effectiveTime |
| practitioner | .player |
| organization | .scoper |
| code | .code |
| specialty | .player.HealthCareProvider[@classCode = 'PROV'].code |
| location | .performance.ActDefinitionOrEvent.ServiceDeliveryLocation[@classCode = 'SDLOC'] |
| healthcareService | .player.QualifiedEntity[@classCode = 'QUAL'].code |
| telecom | .telecom |
| id | n/a |
| extension | n/a |
| system | ./scheme |
| value | ./url |
| use | unique(./use) |
| rank | n/a |
| period | ./usablePeriod[type="IVL<TS>"] |
| availableTime | .effectiveTime |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| daysOfWeek | .effectiveTime |
| allDay | .effectiveTime |
| availableStartTime | .effectiveTime |
| availableEndTime | .effectiveTime |
| notAvailable | .effectiveTime |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| description | n/a |
| during | .effectiveTime |
| availabilityExceptions | .effectiveTime |
| endpoint | n/a |

### Mappings for ServD (<http://www.omg.org/spec/ServD/1.0/>)

|  |  |  |
| --- | --- | --- |
| **PlannetPractitionerRole** | | |
| PractitionerRole | ServiceSiteProvider |
| identifier | ./Identifiers |
| system | ./IdentifierType |
| value | ./Value |
| period | ./StartDate and ./EndDate |
| assigner | ./IdentifierIssuingAuthority |
| period | (ServD maps Practitioners and Organizations via another entity, so this concept is not available) |
| code | (ServD maps Practitioners and Organizations via another entity, so this concept is not available) |
| specialty | ./Specialty |
| location | (ServD maps Practitioners and Organizations via another entity, so this concept is not available)<br/> However these are accessed via the Site.ServiceSite.ServiceSiteProvider record. (The Site has the location) |
| telecom |  |
| system | ./ContactPointType |
| value | ./Value |
| use | ./ContactPointPurpose |
| period | ./StartDate and ./EndDate |

### Mappings for FiveWs Pattern Mapping (http://hl7.org/fhir/fivews)

|  |  |  |
| --- | --- | --- |
| **PlannetPractitionerRole** | | |
| PractitionerRole |  |
| identifier | FiveWs.identifier |
| active | FiveWs.status |
| period | FiveWs.done[x] |
| location | FiveWs.where[x] |