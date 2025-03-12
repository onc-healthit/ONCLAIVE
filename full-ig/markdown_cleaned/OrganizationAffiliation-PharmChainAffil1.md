# Example OrganizationAffiliation: PharmChainAffil1

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