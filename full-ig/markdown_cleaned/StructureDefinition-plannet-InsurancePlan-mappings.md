# Resource Profile: PlannetInsurancePlan - Mappings

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