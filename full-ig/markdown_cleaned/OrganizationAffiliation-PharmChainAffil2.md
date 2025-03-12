# Example OrganizationAffiliation: PharmChainAffil2

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **PharmChainAffil2**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example OrganizationAffiliation: PharmChainAffil2

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "PharmChainAffil2" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

**active**: true

**participatingOrganization**: [Organization/PharmChain](Organization-PharmChain.html) "Pharm Chain"

**network**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**code**: Pharmacy  ([Organization Affiliation Role](CodeSystem-OrganizationAffiliationRoleCS.html)#pharmacy)

**specialty**: Compounding Pharmacy  (provider-taxonomy#3336C0004X)

**location**: [Location/PharmLoc1](Location-PharmLoc1.html) "OrgA CT Location 1"

**healthcareService**: [HealthcareService/PharmChainCompService](HealthcareService-PharmChainCompService.html) "Compounding Pharmacy by OrgA"

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "OrganizationAffiliation" |
| id | "PharmChainAffil2" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| language | "en-US" |
| network[0].reference | "Organization/AcmeofCTStdNet" |
| specialty[0].coding[0].code | #3336C0004X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Compounding Pharmacy" |
| participatingOrganization.reference | "Organization/PharmChain" |
| healthcareService[0].reference | "HealthcareService/PharmChainCompService" |
| location[0].reference | "Location/PharmLoc1" |
| code[0].coding[0].code | #pharmacy |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS" |