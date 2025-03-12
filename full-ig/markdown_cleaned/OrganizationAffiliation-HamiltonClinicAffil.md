# Example OrganizationAffiliation: HamiltonClinicAffil

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **HamiltonClinicAffil**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example OrganizationAffiliation: HamiltonClinicAffil

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HamiltonClinicAffil" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

**active**: true

**participatingOrganization**: [Organization/HamiltonClinic](Organization-HamiltonClinic.html) "Hamilton Clinic"

**network**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**code**: Clinic or Outpatient Facility  ([Organization Affiliation Role](CodeSystem-OrganizationAffiliationRoleCS.html)#outpatient)

**location**: [Location/HospLoc1](Location-HospLoc1.html) "Hartford Hospital Location 1"

**healthcareService**: [HealthcareService/HamiltonClinicServices](HealthcareService-HamiltonClinicServices.html)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "OrganizationAffiliation" |
| id | "HamiltonClinicAffil" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| language | "en-US" |
| code[0].coding[0].code | #outpatient |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS" |
| healthcareService[0].reference | "HealthcareService/HamiltonClinicServices" |
| participatingOrganization.reference | "Organization/HamiltonClinic" |
| location[0].reference | "Location/HospLoc1" |
| network[0].reference | "Organization/AcmeofCTStdNet" |