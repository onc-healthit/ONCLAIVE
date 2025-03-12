# Resource Profile: PlannetEndpoint - Mappings

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net Endpoint**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-Endpoint.html)
* [Detailed Descriptions](StructureDefinition-plannet-Endpoint-definitions.html)
* [Mappings](#)
* [Examples](StructureDefinition-plannet-Endpoint-examples.html)

## Resource Profile: PlannetEndpoint - Mappings

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Mappings for the plannet-Endpoint resource profile.

### Mappings for RIM Mapping ([http://hl7.org/v3](http://hl7.org/comparison-v3.html))

|  |  |  |
| --- | --- | --- |
| **PlannetEndpoint** | | |
| Endpoint | Entity. Role, or Act, n/a |
| meta |  |
| id | n/a |
| extension | n/a |
| text | Act.text? |
| contained | N/A |
| modifierExtension | N/A |
| identifier | n/a |
| status | n/a |
| connectionType | n/a |
| name | n/a |
| managingOrganization | n/a |
| contact | n/a |
| id | n/a |
| extension | n/a |
| system | ./scheme |
| value | ./url |
| use | unique(./use) |
| rank | n/a |
| period | ./usablePeriod[type="IVL<TS>"] |
| period | n/a |
| payloadType | n/a |
| payloadMimeType | n/a |
| address | n/a |

### Mappings for FiveWs Pattern Mapping (http://hl7.org/fhir/fivews)

|  |  |  |
| --- | --- | --- |
| **PlannetEndpoint** | | |
| Endpoint |  |
| identifier | FiveWs.identifier |
| status | FiveWs.status |
| connectionType | FiveWs.class |
| name | FiveWs.what[x] |
| period | FiveWs.done[x] |