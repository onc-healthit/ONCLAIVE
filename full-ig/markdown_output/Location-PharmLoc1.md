xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\PharmLoc1 - FHIR v4.0.1

[![Visit the HL7 website](assets/images/hl7-logo-header.png)](http://hl7.org)

[![Visit the FHIR website](assets/images/fhir-logo-www.png)](http://hl7.org/fhir)

[![Search FHIR](assets/images/search.png)](searchform.html)

[![Visit the Da Vinci website](assets/images/da-vinci_logo.jpg)](http://hl7.org/about/davinci)

DaVinci PDEX Plan Net

1.1.0 - STU 1.1
US

[FHIR](http://hl7.org/fhir/R4/index.html)

* [Home](index.html)
* [Implementation](#)
  + [Implementation](implementation.html)
  + [Representing Provider Directories in Plan Net](implementation.html#Representing)
* [FHIR Artifacts](#)
  + [Profiles](artifacts.html#3)
  + [Extensions](artifacts.html#4)
  + [Search Parameters](artifacts.html#2)
  + [Terminology](artifacts.html#5)
  + [Capability Statement](artifacts.html#1)
* [Examples](artifacts.html#7)
* [Downloads](downloads.html)
* [Change History](ChangeHistory.html)
* [History](http://www.hl7.org/fhir/us/davinci-pdex-plan-net/history.cfml)

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **PharmLoc1**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Location: PharmLoc1

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "PharmLoc1" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Location](StructureDefinition-plannet-Location.html)

> **New Patients**
>
> **value**: Accepting existing patients  ([Accepting Patients Codes](CodeSystem-AcceptingPatientsCS.html)#existptonly)
>
> **value**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**Accessibility**: ADA compliant  ([Accessibility CS](CodeSystem-AccessibilityCS.html)#adacomp)

**Accessibility**: public transit options  ([Accessibility CS](CodeSystem-AccessibilityCS.html)#pubtrans)

**status**: active

**name**: OrgA CT Location 1

**type**: outpatient pharmacy  ([RoleCode](http://terminology.hl7.org/3.1.0/CodeSystem-v3-RoleCode.html)#OUTPHARM)

**telecom**: ph: (111)-222-3333, <https://www.orga.com>

**address**: 123 Main Street Anytown CT 00014-1234

### Positions

|  |  |  |
| --- | --- | --- |
| - | **Longitude** | **Latitude** |
| \* | 3 | 15 |

**managingOrganization**: [Organization/BigBox](Organization-BigBox.html) "Big Box Retailer"

> **hoursOfOperation**
>
> **daysOfWeek**: mon, tue, wed, thu, fri
>
> **allDay**: true

> **hoursOfOperation**
>
> **daysOfWeek**: sat, sun
>
> **openingTime**: 08:00:00
>
> **closingTime**: 17:00:00

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Location" |
| id | "PharmLoc1" |
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
| telecom[0].value | (111)-222-3333 |
| telecom[0].rank | "2" |
| telecom[1].system | "url" |
| telecom[1].value | https://www.orga.com |
| telecom[1].rank | "1" |
| language | "en-US" |
| name | "OrgA CT Location 1" |
| type[0].coding[0].code | #OUTPHARM |
| type[0].coding[0].system | "http://terminology.hl7.org/CodeSystem/v3-RoleCode" |
| type[0].coding[0].display | "outpatient pharmacy" |
| managingOrganization.reference | "Organization/BigBox" |
| address.line[0] | "123 Main Street" |
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
| hoursOfOperation[0].allDay | "true" |
| hoursOfOperation[1].daysOfWeek[0] | "sat" |
| hoursOfOperation[1].daysOfWeek[1] | "sun" |
| hoursOfOperation[1].openingTime | "08:00:00" |
| hoursOfOperation[1].closingTime | "17:00:00" |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)