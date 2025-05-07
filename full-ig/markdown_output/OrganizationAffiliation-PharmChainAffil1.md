xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\PharmChainAffil1 - FHIR v4.0.1

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
* **PharmChainAffil1**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example OrganizationAffiliation: PharmChainAffil1

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "PharmChainAffil1" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

**active**: true

**participatingOrganization**: [Organization/PharmChain](Organization-PharmChain.html) "Pharm Chain"

**network**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**code**: Pharmacy  ([Organization Affiliation Role](CodeSystem-OrganizationAffiliationRoleCS.html)#pharmacy)

**specialty**: Community/Retail Pharmacy  (provider-taxonomy#3336C0003X)

**location**:

* [Location/PharmLoc1](Location-PharmLoc1.html) "OrgA CT Location 1"
* [Location/PharmLoc2](Location-PharmLoc2.html) "OrgA CT Location 2"

**healthcareService**: [HealthcareService/PharmChainRetailService](HealthcareService-PharmChainRetailService.html) "Pharmacy by PharmChain"

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "OrganizationAffiliation" |
| id | "PharmChainAffil1" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| language | "en-US" |
| network[0].reference | "Organization/AcmeofCTStdNet" |
| participatingOrganization.reference | "Organization/PharmChain" |
| healthcareService[0].reference | "HealthcareService/PharmChainRetailService" |
| location[0].reference | "Location/PharmLoc1" |
| location[1].reference | "Location/PharmLoc2" |
| code[0].coding[0].code | #pharmacy |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS" |
| specialty[0].coding[0].code | #3336C0003X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Community/Retail Pharmacy" |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)