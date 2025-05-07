xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\HartfordOrthopedicAffil - FHIR v4.0.1

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
* **HartfordOrthopedicAffil**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example OrganizationAffiliation: HartfordOrthopedicAffil

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HartfordOrthopedicAffil" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

**active**: true

**organization**: [Organization/Hospital](Organization-Hospital.html) "Hartford General Hospital"

**participatingOrganization**: [Organization/HartfordOrthopedics](Organization-HartfordOrthopedics.html) "Hartford Orthopedics Services"

**network**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**code**: Provider  ([Organization Affiliation Role](http://hl7.org/fhir/R4/codesystem-organization-role.html)#provider)

**location**:

* [Location/HospLoc1](Location-HospLoc1.html) "Hartford Hospital Location 1"
* [Location/HospLoc2](Location-HospLoc2.html) "Hartford Hospital Location 2"

**healthcareService**: [HealthcareService/HartfordOrthopedicServices](HealthcareService-HartfordOrthopedicServices.html)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "OrganizationAffiliation" |
| id | "HartfordOrthopedicAffil" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| language | "en-US" |
| code[0].coding[0].code | #provider |
| code[0].coding[0].system | "http://hl7.org/fhir/organization-role" |
| healthcareService[0].reference | "HealthcareService/HartfordOrthopedicServices" |
| participatingOrganization.reference | "Organization/HartfordOrthopedics" |
| organization.reference | "Organization/Hospital" |
| location[0].reference | "Location/HospLoc1" |
| location[1].reference | "Location/HospLoc2" |
| network[0].reference | "Organization/AcmeofCTStdNet" |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)