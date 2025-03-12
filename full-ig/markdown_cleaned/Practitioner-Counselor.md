# Example Practitioner: Counselor

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Counselor**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Practitioner: Counselor

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "Counselor" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html)

**Communication Proficiency**: General professional proficiency  ([Language Proficiency CS](CodeSystem-LanguageProficiencyCS.html)#30)

**identifier**: id: NPI3238

**active**: true

**name**: Susie Smith, LPC

### Qualifications

|  |  |  |  |
| --- | --- | --- | --- |
| - | **Extension** | **Code** | **Issuer** |
| \* |  | IL  ([not stated] "LPC") | : State of Illinois |

**communication**: Russian  ([Tags for the Identification of Languages](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ietf3066.html)#ru)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Practitioner" |
| id | "Counselor" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Practitioner" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| identifier[0].system | "http://hl7.org/fhir/sid/us-npi" |
| identifier[0].value | NPI3238 |
| qualification[0].extension[0].extension[0].url | "status" |
| qualification[0].extension[0].extension[0].valueCode | "active" |
| qualification[0].extension[0].extension[1].url | "whereValid" |
| qualification[0].extension[0].extension[1].valueCodeableConcept.coding[0].code | #IL |
| qualification[0].extension[0].extension[1].valueCodeableConcept.coding[0].system | "https://www.usps.com/" |
| qualification[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification" |
| qualification[0].code.coding[0].display | "LPC" |
| qualification[0].code.text | "IL" |
| qualification[0].issuer.display | "State of Illinois" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency" |
| extension[0].valueCodeableConcept.coding[0].code | #30 |
| extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/LanguageProficiencyCS" |
| language | "en-US" |
| name[0].text | "Susie Smith, LPC" |
| name[0].family | "Smith" |
| name[0].given[0] | "Susie" |
| communication[0].coding[0].code | #ru |
| communication[0].coding[0].system | "urn:ietf:bcp:47" |