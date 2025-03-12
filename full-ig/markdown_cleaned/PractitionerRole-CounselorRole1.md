# Example PractitionerRole: CounselorRole1

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **CounselorRole1**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example PractitionerRole: CounselorRole1

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "CounselorRole1" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)

**Network Reference**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**active**: true

**practitioner**: [Practitioner/Counselor](Practitioner-Counselor.html) " SMITH"

**code**: Counselor  ([Provider Role Codes](CodeSystem-ProviderRoleCS.html)#co)

**specialty**: Professional Counselor  (provider-taxonomy#101YP2500X)

**healthcareService**: [HealthcareService/VirtualCounselService](HealthcareService-VirtualCounselService.html)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "PractitionerRole" |
| id | "CounselorRole1" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network-reference" |
| extension[0].valueReference.reference | "Organization/AcmeofCTStdNet" |
| language | "en-US" |
| code[0].coding[0].code | #co |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS" |
| code[0].coding[0].display | "Counselor" |
| practitioner.reference | "Practitioner/Counselor" |
| healthcareService[0].reference | "HealthcareService/VirtualCounselService" |
| specialty[0].coding[0].code | #101YP2500X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Professional Counselor" |