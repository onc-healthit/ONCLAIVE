# Example OrganizationAffiliation: ConnHIEAffil

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **ConnHIEAffil**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example OrganizationAffiliation: ConnHIEAffil

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "ConnHIEAffil" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

**active**: true

**organization**: [Organization/ConnHIE](Organization-ConnHIE.html) "Connecticut HIE"

**participatingOrganization**: [Organization/BurrClinic](Organization-BurrClinic.html) "Burr Clinic"

**code**: Member Of  ([Organization Affiliation Role](CodeSystem-OrganizationAffiliationRoleCS.html)#bt)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "OrganizationAffiliation" |
| id | "ConnHIEAffil" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| language | "en-US" |
| code[0].coding[0].code | #bt |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS" |
| participatingOrganization.reference | "Organization/BurrClinic" |
| organization.reference | "Organization/ConnHIE" |