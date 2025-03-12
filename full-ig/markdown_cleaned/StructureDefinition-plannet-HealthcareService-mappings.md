# Resource Profile: PlannetHealthcareService - Mappings

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net HealthcareService**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-HealthcareService.html)
* [Detailed Descriptions](StructureDefinition-plannet-HealthcareService-definitions.html)
* [Mappings](#)
* [Examples](StructureDefinition-plannet-HealthcareService-examples.html)

## Resource Profile: PlannetHealthcareService - Mappings

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Mappings for the plannet-HealthcareService resource profile.

### Mappings for RIM Mapping ([http://hl7.org/v3](http://hl7.org/comparison-v3.html))

|  |  |  |
| --- | --- | --- |
| **PlannetHealthcareService** | | |
| HealthcareService | Entity. Role, or Act, act[classCode=ACT][moodCode=DEF] |
| meta |  |
| id | n/a |
| extension | n/a |
| text | Act.text? |
| contained | N/A |
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
| providedBy | .scopingRole.Organization |
| category | .code |
| type | .actrelationship[typeCode=COMP.act[classCode=ACT][moodCode=DEF].code |
| specialty | .actrelationship[typeCode=COMP.act[classCode=ACT][moodCode=DEF].code |
| location | .location.role[classCode=SDLOC] |
| name | .name |
| comment | .location.role[classCode=SDLOC].desc |
| extraDetails | .actrelationship[typeCode=COMP.act[classCode=ACT][moodCode=DEF].text |
| photo | .actrelationship[typeCode=SBJ].observation.value |
| telecom | .telecom |
| id | n/a |
| extension | n/a |
| system | ./scheme |
| value | ./url |
| use | unique(./use) |
| rank | n/a |
| period | ./usablePeriod[type="IVL<TS>"] |
| coverageArea | .location.role[classCode=SDLOC].subjectOf.A\_SpatialCoordinate |
| serviceProvisionCode | .actrelationship[typeCode=PRCN].observation[moodCode=EVN.CRT] |
| eligibility |  |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| code | .actrelationship[typeCode=PRCN].observation[moodCode=EVN.CRT] |
| comment | .actrelationship[typeCode=PRCN].observation[moodCode=EVN.CRT].text |
| program | .actrelationship[typeCode=PERT].observation |
| characteristic | .actrelationship[typeCode=PERT].observation |
| referralMethod | .actrelationship[typeCode=PERT].observation |
| appointmentRequired | .actrelationship[typeCode=PERT].observation |
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

### Mappings for FiveWs Pattern Mapping (http://hl7.org/fhir/fivews)

|  |  |  |
| --- | --- | --- |
| **PlannetHealthcareService** | | |
| HealthcareService |  |
| identifier | FiveWs.identifier |
| active | FiveWs.status |
| category | FiveWs.class |
| location | FiveWs.where[x] |