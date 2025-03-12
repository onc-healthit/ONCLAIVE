# Example OrganizationAffiliation: BurrClinicAffil

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **BurrClinicAffil**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example OrganizationAffiliation: BurrClinicAffil

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "BurrClinicAffil" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

**active**: true

**organization**: [Organization/Hospital](Organization-Hospital.html) "Hartford General Hospital"

**participatingOrganization**: [Organization/BurrClinic](Organization-BurrClinic.html) "Burr Clinic"

**network**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**code**: Clinic or Outpatient Facility  ([Organization Affiliation Role](CodeSystem-OrganizationAffiliationRoleCS.html)#outpatient)

**location**: [Location/HospLoc2](Location-HospLoc2.html) "Hartford Hospital Location 2"

**healthcareService**: [HealthcareService/BurrClinicServices](HealthcareService-BurrClinicServices.html)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "OrganizationAffiliation" |
| id | "BurrClinicAffil" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| language | "en-US" |
| code[0].coding[0].code | #outpatient |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS" |
| healthcareService[0].reference | "HealthcareService/BurrClinicServices" |
| participatingOrganization.reference | "Organization/BurrClinic" |
| location[0].reference | "Location/HospLoc2" |
| network[0].reference | "Organization/AcmeofCTStdNet" |
| organization.reference | "Organization/Hospital" |