xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\HansSoloService - FHIR v4.0.1

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
* **HansSoloService**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example HealthcareService: HansSoloService

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HansSoloService" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

> **Delivery Method**
>
> **value**: Physical  ([Delivery Methods](CodeSystem-DeliveryMethodCS.html)#physical)

**active**: true

**category**: Clinic or Outpatient Facility  ([Healthcare Service Category](CodeSystem-HealthcareServiceCategoryCS.html)#outpat)

**specialty**: Family Medicine Physician  (provider-taxonomy#207Q00000X)

**location**: [Location/HansSoloClinic](Location-HansSoloClinic.html) "OrgA CT Location 1"

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "HealthcareService" |
| id | "HansSoloService" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| extension[0].extension[0].url | "type" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #physical |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS" |
| language | "en-US" |
| category[0].coding[0].code | #outpat |
| category[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS" |
| specialty[0].coding[0].code | #207Q00000X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Family Medicine Physician" |
| location[0].reference | "Location/HansSoloClinic" |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)