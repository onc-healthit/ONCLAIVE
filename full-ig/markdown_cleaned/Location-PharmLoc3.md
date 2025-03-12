# Example Location: PharmLoc3

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **PharmLoc3**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Location: PharmLoc3

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "PharmLoc3" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Location](StructureDefinition-plannet-Location.html)

> **New Patients**
>
> **value**: Accepting existing patients  ([Accepting Patients Codes](CodeSystem-AcceptingPatientsCS.html)#existptonly)
>
> **value**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**Accessibility**: ADA compliant  ([Accessibility CS](CodeSystem-AccessibilityCS.html)#adacomp)

**Accessibility**: public transit options  ([Accessibility CS](CodeSystem-AccessibilityCS.html)#pubtrans)

**status**: active

**name**: OrgA MA Location 1

**type**: outpatient pharmacy  ([RoleCode](http://terminology.hl7.org/3.1.0/CodeSystem-v3-RoleCode.html)#OUTPHARM)

**telecom**: ph: (444)-555-666, <https://www.orga.com>

**address**: 456 Main Street Somewhere CT 00014-1234

### Positions

|  |  |  |
| --- | --- | --- |
| - | **Longitude** | **Latitude** |
| \* | 7 | 12 |

**managingOrganization**: [Organization/BigBox](Organization-BigBox.html) "Big Box Retailer"

> **hoursOfOperation**
>
> **daysOfWeek**: mon, tue, wed, thu
>
> **allDay**: true

> **hoursOfOperation**
>
> **daysOfWeek**: sun
>
> **openingTime**: 08:00:00
>
> **closingTime**: 17:00:00

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Location" |
| id | "PharmLoc3" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| status | "active" |
| extension[0].extension[0].url | "acceptingPatients" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #existptonly |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AcceptingPatientsCS" |
| extension[0].extension[1].url | "fromNetwork" |
| extension[0].extension[1].valueReference.reference | "Organization/AcmeofCTStdNet" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients" |
| extension[1].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility" |
| extension[1].valueCodeableConcept.coding[0].code | #adacomp |
| extension[1].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AccessibilityCS" |
| extension[2].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility" |
| extension[2].valueCodeableConcept.coding[0].code | #pubtrans |
| extension[2].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AccessibilityCS" |
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
| telecom[0].value | (444)-555-666 |
| telecom[0].rank | "2" |
| telecom[1].system | "url" |
| telecom[1].value | https://www.orga.com |
| telecom[1].rank | "1" |
| language | "en-US" |
| name | "OrgA MA Location 1" |
| type[0].coding[0].code | #OUTPHARM |
| type[0].coding[0].system | "http://terminology.hl7.org/CodeSystem/v3-RoleCode" |
| type[0].coding[0].display | "outpatient pharmacy" |
| managingOrganization.reference | "Organization/BigBox" |
| address.line[0] | "456 Main Street" |
| address.city | "Somewhere" |
| address.state | "CT" |
| address.postalCode | "00014-1234" |
| position.longitude | "7" |
| position.latitude | "12" |
| hoursOfOperation[0].daysOfWeek[0] | "mon" |
| hoursOfOperation[0].daysOfWeek[1] | "tue" |
| hoursOfOperation[0].daysOfWeek[2] | "wed" |
| hoursOfOperation[0].daysOfWeek[3] | "thu" |
| hoursOfOperation[0].allDay | "true" |
| hoursOfOperation[1].daysOfWeek[0] | "sun" |
| hoursOfOperation[1].openingTime | "08:00:00" |
| hoursOfOperation[1].closingTime | "17:00:00" |