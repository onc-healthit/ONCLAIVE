# Resource Profile: PlannetOrganizationAffiliation - Mappings

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net OrganizationAffiliation**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-OrganizationAffiliation.html)
* [Detailed Descriptions](StructureDefinition-plannet-OrganizationAffiliation-definitions.html)
* [Mappings](#)
* [Examples](StructureDefinition-plannet-OrganizationAffiliation-examples.html)

## Resource Profile: PlannetOrganizationAffiliation - Mappings

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Mappings for the plannet-OrganizationAffiliation resource profile.

### Mappings for RIM Mapping ([http://hl7.org/v3](http://hl7.org/comparison-v3.html))

|  |  |  |
| --- | --- | --- |
| **PlannetOrganizationAffiliation** | | |
| OrganizationAffiliation | Entity. Role, or Act, Role |
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
| period | .performance[@typeCode <= 'PPRF'].ActDefinitionOrEvent.effectiveTime |
| organization | .scoper |
| participatingOrganization | .player |
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
| endpoint | n/a |

### Mappings for FiveWs Pattern Mapping (http://hl7.org/fhir/fivews)

|  |  |  |
| --- | --- | --- |
| **PlannetOrganizationAffiliation** | | |
| OrganizationAffiliation |  |
| identifier | FiveWs.identifier |
| active | FiveWs.status |
| period | FiveWs.done[x] |
| location | FiveWs.where[x] |