# Example Organization: HartfordOrthopedics

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **HartfordOrthopedics**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Organization: HartfordOrthopedics

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HartfordOrthopedics" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Organization](StructureDefinition-plannet-Organization.html)

**identifier**: id: NPI456

**active**: true

**type**: Provider Group  ([Organization Type](CodeSystem-OrgTypeCS.html)#prvgrp)

**name**: Hartford Orthopedics Services

**telecom**: ph: (111)-222-3333, <https://www.orga.com>

**address**: 123 Main Street Anytown CT 00014-1234

### Contacts

|  |  |
| --- | --- |
| - | **Telecom** |
| \* | ph: (111)-222-3333 |

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Organization" |
| id | "HartfordOrthopedics" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| identifier[0].system | "http://hl7.org/fhir/sid/us-npi" |
| identifier[0].value | NPI456 |
| telecom[0].extension[0].extension[0].url | "daysOfWeek" |
| telecom[0].extension[0].extension[0].valueCode | "mon" |
| telecom[0].extension[0].extension[1].url | "daysOfWeek" |
| telecom[0].extension[0].extension[1].valueCode | "tue" |
| telecom[0].extension[0].extension[2].url | "daysOfWeek" |
| telecom[0].extension[0].extension[2].valueCode | "wed" |
| telecom[0].extension[0].extension[3].url | "daysOfWeek" |
| telecom[0].extension[0].extension[3].valueCode | "thu" |
| telecom[0].extension[0].extension[4].url | "daysOfWeek" |
| telecom[0].extension[0].extension[4].valueCode | "fri" |
| telecom[0].extension[0].extension[5].url | "allDay" |
| telecom[0].extension[0].extension[5].valueBoolean | "true" |
| telecom[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| telecom[0].extension[1].extension[0].url | "daysOfWeek" |
| telecom[0].extension[1].extension[0].valueCode | "sat" |
| telecom[0].extension[1].extension[1].url | "daysOfWeek" |
| telecom[0].extension[1].extension[1].valueCode | "sun" |
| telecom[0].extension[1].extension[2].url | "availableStartTime" |
| telecom[0].extension[1].extension[2].valueTime | "08:00:00" |
| telecom[0].extension[1].extension[3].url | "availableEndTime" |
| telecom[0].extension[1].extension[3].valueTime | "17:00:00" |
| telecom[0].extension[1].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| telecom[0].system | "phone" |
| telecom[0].value | (111)-222-3333 |
| telecom[0].rank | "2" |
| telecom[1].system | "url" |
| telecom[1].value | https://www.orga.com |
| telecom[1].rank | "1" |
| contact[0].telecom[0].extension[0].extension[0].url | "daysOfWeek" |
| contact[0].telecom[0].extension[0].extension[0].valueCode | "mon" |
| contact[0].telecom[0].extension[0].extension[1].url | "daysOfWeek" |
| contact[0].telecom[0].extension[0].extension[1].valueCode | "tue" |
| contact[0].telecom[0].extension[0].extension[2].url | "daysOfWeek" |
| contact[0].telecom[0].extension[0].extension[2].valueCode | "wed" |
| contact[0].telecom[0].extension[0].extension[3].url | "daysOfWeek" |
| contact[0].telecom[0].extension[0].extension[3].valueCode | "thu" |
| contact[0].telecom[0].extension[0].extension[4].url | "daysOfWeek" |
| contact[0].telecom[0].extension[0].extension[4].valueCode | "fri" |
| contact[0].telecom[0].extension[0].extension[5].url | "allDay" |
| contact[0].telecom[0].extension[0].extension[5].valueBoolean | "true" |
| contact[0].telecom[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| contact[0].telecom[0].extension[1].extension[0].url | "daysOfWeek" |
| contact[0].telecom[0].extension[1].extension[0].valueCode | "sat" |
| contact[0].telecom[0].extension[1].extension[1].url | "daysOfWeek" |
| contact[0].telecom[0].extension[1].extension[1].valueCode | "sun" |
| contact[0].telecom[0].extension[1].extension[2].url | "availableStartTime" |
| contact[0].telecom[0].extension[1].extension[2].valueTime | "08:00:00" |
| contact[0].telecom[0].extension[1].extension[3].url | "availableEndTime" |
| contact[0].telecom[0].extension[1].extension[3].valueTime | "17:00:00" |
| contact[0].telecom[0].extension[1].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| contact[0].telecom[0].system | "phone" |
| contact[0].telecom[0].value | (111)-222-3333 |
| contact[0].telecom[0].rank | "2" |
| language | "en-US" |
| name | "Hartford Orthopedics Services" |
| type[0].coding[0].code | #prvgrp |
| type[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS" |
| type[0].coding[0].display | "Provider Group" |
| address[0].line[0] | "123 Main Street" |
| address[0].city | "Anytown" |
| address[0].state | "CT" |
| address[0].postalCode | "00014-1234" |