# Example OrganizationAffiliation: HartfordOrthopedicAffil

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