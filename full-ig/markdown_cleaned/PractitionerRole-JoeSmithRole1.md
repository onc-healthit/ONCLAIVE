# Example PractitionerRole: JoeSmithRole1

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **JoeSmithRole1**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example PractitionerRole: JoeSmithRole1

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "JoeSmithRole1" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)

**Network Reference**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**active**: true

**practitioner**: [Practitioner/JoeSmith](Practitioner-JoeSmith.html) " SMITH"

**organization**: [Organization/Hospital](Organization-Hospital.html) "Hartford General Hospital"

**code**: Physician  ([Provider Role Codes](CodeSystem-ProviderRoleCS.html)#ph)

**specialty**: Internal Medicine Physician  (provider-taxonomy#207R00000X)

**location**: [Location/HospLoc1](Location-HospLoc1.html) "Hartford Hospital Location 1"

**healthcareService**: [HealthcareService/HospERService](HealthcareService-HospERService.html)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "PractitionerRole" |
| id | "JoeSmithRole1" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network-reference" |
| extension[0].valueReference.reference | "Organization/AcmeofCTStdNet" |
| language | "en-US" |
| code[0].coding[0].code | #ph |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS" |
| practitioner.reference | "Practitioner/JoeSmith" |
| healthcareService[0].reference | "HealthcareService/HospERService" |
| location[0].reference | "Location/HospLoc1" |
| specialty[0].coding[0].code | #207R00000X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Internal Medicine Physician" |
| organization.reference | "Organization/Hospital" |