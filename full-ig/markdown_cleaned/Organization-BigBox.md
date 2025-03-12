# Example Organization: BigBox

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **BigBox**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Organization: BigBox

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "BigBox" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Organization](StructureDefinition-plannet-Organization.html)

**active**: true

**type**: Non-Healthcare Business  ([Organization Type](CodeSystem-OrgTypeCS.html)#bus)

**name**: Big Box Retailer

**telecom**: ph: (111)-222-3333, <https://www.bixboxretailer.com>

**address**: 456 Main Street Norwalk CT 00014-1234

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Organization" |
| id | "BigBox" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
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
| telecom[0].extension[0].extension[5].url | "availableStartTime" |
| telecom[0].extension[0].extension[5].valueTime | "08:00:00" |
| telecom[0].extension[0].extension[6].url | "availableEndTime" |
| telecom[0].extension[0].extension[6].valueTime | "17:00:00" |
| telecom[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| telecom[0].system | "phone" |
| telecom[0].value | (111)-222-3333 |
| telecom[0].rank | "2" |
| telecom[1].system | "url" |
| telecom[1].value | https://www.bixboxretailer.com |
| telecom[1].rank | "1" |
| language | "en-US" |
| name | "Big Box Retailer" |
| type[0].coding[0].code | #bus |
| type[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS" |
| type[0].coding[0].display | "Non-Healthcare Business" |
| address[0].line[0] | "456 Main Street" |
| address[0].city | "Norwalk" |
| address[0].state | "CT" |
| address[0].postalCode | "00014-1234" |