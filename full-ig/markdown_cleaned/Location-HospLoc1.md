# Example Location: HospLoc1

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **HospLoc1**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Location: HospLoc1

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HospLoc1" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Location](StructureDefinition-plannet-Location.html)

**Accessibility**: ADA compliant  ([Accessibility CS](CodeSystem-AccessibilityCS.html)#adacomp)

**Accessibility**: public transit options  ([Accessibility CS](CodeSystem-AccessibilityCS.html)#pubtrans)

**status**: active

**name**: Hartford Hospital Location 1

**type**: Hospital  ([RoleCode](http://terminology.hl7.org/3.1.0/CodeSystem-v3-RoleCode.html)#HOSP)

**telecom**: ph: (111)-222-3333, <https://www.hgh.com>

**address**: 456 Main Street Anytown CT 00014-1234

### Positions

|  |  |  |
| --- | --- | --- |
| - | **Longitude** | **Latitude** |
| \* | 3 | 15 |

**managingOrganization**: [Organization/Hospital](Organization-Hospital.html) "Hartford General Hospital"

### HoursOfOperations

|  |  |  |
| --- | --- | --- |
| - | **DaysOfWeek** | **AllDay** |
| \* | mon, tue, wed, thu, fri, sat, sun | true |

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Location" |
| id | "HospLoc1" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| status | "active" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility" |
| extension[0].valueCodeableConcept.coding[0].code | #adacomp |
| extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AccessibilityCS" |
| extension[1].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility" |
| extension[1].valueCodeableConcept.coding[0].code | #pubtrans |
| extension[1].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AccessibilityCS" |
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
| telecom[0].extension[0].extension[6].url | "daysOfWeek" |
| telecom[0].extension[0].extension[6].valueCode | "sat" |
| telecom[0].extension[0].extension[7].url | "daysOfWeek" |
| telecom[0].extension[0].extension[7].valueCode | "sun" |
| telecom[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| telecom[0].system | "phone" |
| telecom[0].value | (111)-222-3333 |
| telecom[0].rank | "2" |
| telecom[1].system | "url" |
| telecom[1].value | https://www.hgh.com |
| telecom[1].rank | "1" |
| language | "en-US" |
| name | "Hartford Hospital Location 1" |
| type[0].coding[0].code | #HOSP |
| type[0].coding[0].system | "http://terminology.hl7.org/CodeSystem/v3-RoleCode" |
| managingOrganization.reference | "Organization/Hospital" |
| address.line[0] | "456 Main Street" |
| address.city | "Anytown" |
| address.state | "CT" |
| address.postalCode | "00014-1234" |
| position.longitude | "3" |
| position.latitude | "15" |
| hoursOfOperation[0].daysOfWeek[0] | "mon" |
| hoursOfOperation[0].daysOfWeek[1] | "tue" |
| hoursOfOperation[0].daysOfWeek[2] | "wed" |
| hoursOfOperation[0].daysOfWeek[3] | "thu" |
| hoursOfOperation[0].daysOfWeek[4] | "fri" |
| hoursOfOperation[0].daysOfWeek[5] | "sat" |
| hoursOfOperation[0].daysOfWeek[6] | "sun" |
| hoursOfOperation[0].allDay | "true" |