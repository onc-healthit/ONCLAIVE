# Example OrganizationAffiliation: PharmChainAffil3

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **PharmChainAffil3**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example OrganizationAffiliation: PharmChainAffil3

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "PharmChainAffil3" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

**active**: true

**participatingOrganization**: [Organization/PharmChain](Organization-PharmChain.html) "Pharm Chain"

**network**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**code**: Pharmacy  ([Organization Affiliation Role](CodeSystem-OrganizationAffiliationRoleCS.html)#pharmacy)

**specialty**: Mail Order Pharmacy  (provider-taxonomy#3336M0002X)

**healthcareService**: [HealthcareService/PharmChainMailService](HealthcareService-PharmChainMailService.html) "Mail Order Pharmacy by OrgA"

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "OrganizationAffiliation" |
| id | "PharmChainAffil3" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| language | "en-US" |
| network[0].reference | "Organization/AcmeofCTStdNet" |
| participatingOrganization.reference | "Organization/PharmChain" |
| healthcareService[0].reference | "HealthcareService/PharmChainMailService" |
| code[0].coding[0].code | #pharmacy |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS" |
| specialty[0].coding[0].code | #3336M0002X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Mail Order Pharmacy" |