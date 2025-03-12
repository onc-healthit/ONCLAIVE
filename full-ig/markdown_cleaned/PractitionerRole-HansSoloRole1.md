# Example PractitionerRole: HansSoloRole1

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **HansSoloRole1**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example PractitionerRole: HansSoloRole1

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HansSoloRole1" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)

**Network Reference**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

> **Qualification**
>
> **value**: Internal Medicine Physician  (provider-taxonomy#207R00000X)
>
> **value**: active
>
> **value**: : American Board of Internal Medicine

**active**: true

**practitioner**: [Practitioner/HansSolo](Practitioner-HansSolo.html) " SOLO"

**code**: Physician  ([Provider Role Codes](CodeSystem-ProviderRoleCS.html)#ph)

**specialty**: Internal Medicine Physician  (provider-taxonomy#207R00000X)

**location**: [Location/HansSoloClinic](Location-HansSoloClinic.html) "OrgA CT Location 1"

**healthcareService**: [HealthcareService/HansSoloService](HealthcareService-HansSoloService.html)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "PractitionerRole" |
| id | "HansSoloRole1" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network-reference" |
| extension[0].valueReference.reference | "Organization/AcmeofCTStdNet" |
| extension[1].extension[0].url | "code" |
| extension[1].extension[0].valueCodeableConcept.coding[0].code | #207R00000X |
| extension[1].extension[0].valueCodeableConcept.coding[0].system | "http://nucc.org/provider-taxonomy" |
| extension[1].extension[1].url | "status" |
| extension[1].extension[1].valueCode | "active" |
| extension[1].extension[2].url | "issuer" |
| extension[1].extension[2].valueReference.display | "American Board of Internal Medicine" |
| extension[1].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/qualification" |
| language | "en-US" |
| code[0].coding[0].code | #ph |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS" |
| practitioner.reference | "Practitioner/HansSolo" |
| healthcareService[0].reference | "HealthcareService/HansSoloService" |
| location[0].reference | "Location/HansSoloClinic" |
| specialty[0].coding[0].code | #207R00000X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Internal Medicine Physician" |