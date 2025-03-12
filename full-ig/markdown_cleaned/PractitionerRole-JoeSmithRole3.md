# Example PractitionerRole: JoeSmithRole3

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **JoeSmithRole3**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example PractitionerRole: JoeSmithRole3

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "JoeSmithRole3" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)

**Network Reference**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**active**: true

**organization**: [Organization/Hospital](Organization-Hospital.html) "Hartford General Hospital"

**code**: Admitting Privileges  ([Provider Role Codes](CodeSystem-ProviderRoleCS.html)#ap)

**specialty**: Internal Medicine Physician  (provider-taxonomy#207R00000X), Cardiovascular Disease Physician  (provider-taxonomy#207RC0000X)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "PractitionerRole" |
| id | "JoeSmithRole3" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network-reference" |
| extension[0].valueReference.reference | "Organization/AcmeofCTStdNet" |
| language | "en-US" |
| code[0].coding[0].code | #ap |
| code[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS" |
| specialty[0].coding[0].code | #207R00000X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Internal Medicine Physician" |
| specialty[1].coding[0].code | #207RC0000X |
| specialty[1].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[1].coding[0].display | "Cardiovascular Disease Physician" |
| organization.reference | "Organization/Hospital" |