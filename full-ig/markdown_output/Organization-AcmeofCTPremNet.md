xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\AcmeofCTPremNet - FHIR v4.0.1

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
* **AcmeofCTPremNet**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Organization: AcmeofCTPremNet

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "AcmeofCTPremNet" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Network](StructureDefinition-plannet-Network.html)

**Location Reference**: [Location/StateOfCTLocation](Location-StateOfCTLocation.html) "State of CT Area"

**active**: true

**type**: Network  ([Organization Type](CodeSystem-OrgTypeCS.html)#ntwk)

**name**: ACME CT Premium Preferred Provider Network

**partOf**: [Organization/Acme](Organization-Acme.html) "Acme of CT"

### Contacts

|  |  |  |
| --- | --- | --- |
| - | **Name** | **Telecom** |
| \* | Jane Kawasaki | -unknown- |

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Organization" |
| id | "AcmeofCTPremNet" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| contact[0].telecom[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |
| contact[0].telecom[0].extension[0].valueReference.reference | "Organization/Acme" |
| contact[0].name.family | "Kawasaki" |
| contact[0].name.given[0] | "Jane" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference" |
| extension[0].valueReference.reference | "Location/StateOfCTLocation" |
| language | "en-US" |
| partOf.reference | "Organization/Acme" |
| type[0].coding[0].code | #ntwk |
| type[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS" |
| type[0].coding[0].display | "Network" |
| name | "ACME CT Premium Preferred Provider Network" |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)