# Example PractitionerRole: AnonRole

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **AnonRole**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example PractitionerRole: AnonRole

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "AnonRole" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)

**Network Reference**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**active**: true

**organization**: [Organization/CancerClinic](Organization-CancerClinic.html) "Hamilton Clinic"

**code**: Physician  ([Provider Role Codes](CodeSystem-ProviderRoleCS.html)#ph)

**specialty**: Internal Medicine Physician  (provider-taxonomy#207R00000X)

**location**: [Location/HospLoc2](Location-HospLoc2.html) "Hartford Hospital Location 2"

**healthcareService**: [HealthcareService/BurrClinicServices](HealthcareService-BurrClinicServices.html)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "PractitionerRole" |
| id | "AnonRole" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network-reference" |
| extension[0].valueReference.reference | "Organization/AcmeofCTStdNet" |
| language | "en-US" |
| code[0].coding[0].code | #ph |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS" |
| healthcareService[0].reference | "HealthcareService/BurrClinicServices" |
| location[0].reference | "Location/HospLoc2" |
| specialty[0].coding[0].code | #207R00000X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Internal Medicine Physician" |
| organization.reference | "Organization/CancerClinic" |