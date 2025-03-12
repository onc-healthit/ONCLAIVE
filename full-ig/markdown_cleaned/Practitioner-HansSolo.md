# Example Practitioner: HansSolo

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **HansSolo**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Practitioner: HansSolo

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HansSolo" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html)

**Communication Proficiency**: General professional proficiency  ([Language Proficiency CS](CodeSystem-LanguageProficiencyCS.html)#30)

**identifier**: id: NPI3233

**active**: true

**name**: Hans Solo, MD

> **qualification**
>
> > **Practitioner Qualification**
> >
> > **value**: active
> >
> > **value**: Illinois  (#IL)
>
> **code**: MD  ([degreeLicenseCertificate](http://terminology.hl7.org/3.1.0/CodeSystem-v2-0360.html)#MD)
>
> **issuer**: : State of Illinois

> **qualification**
>
> > **Practitioner Qualification**
> >
> > **value**: active
> >
> > **value**: Illinois  (#IL)
>
> **code**: Board Certified Internal Medicine  (provider-taxonomy#207R00000X "Internal Medicine Physician")
>
> **issuer**: : American Board of Internal Medicine

> **qualification**
>
> > **Practitioner Qualification**
> >
> > **value**: active
> >
> > **value**: Illinois  (#IL)
>
> **code**: Board Certified Cardiovascular Disease  (provider-taxonomy#207RC0000X "Cardiovascular Disease Physician")
>
> **issuer**: : American Board of Internal Medicine

**communication**: Japanese  ([Tags for the Identification of Languages](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ietf3066.html)#ja)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Practitioner" |
| id | "HansSolo" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Practitioner" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| identifier[0].system | "http://hl7.org/fhir/sid/us-npi" |
| identifier[0].value | NPI3233 |
| qualification[0].extension[0].extension[0].url | "status" |
| qualification[0].extension[0].extension[0].valueCode | "active" |
| qualification[0].extension[0].extension[1].url | "whereValid" |
| qualification[0].extension[0].extension[1].valueCodeableConcept.coding[0].code | #IL |
| qualification[0].extension[0].extension[1].valueCodeableConcept.coding[0].system | "https://www.usps.com/" |
| qualification[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification" |
| qualification[0].code.coding[0].code | #MD |
| qualification[0].code.coding[0].system | "http://terminology.hl7.org/CodeSystem/v2-0360" |
| qualification[0].code.text | "MD" |
| qualification[0].issuer.display | "State of Illinois" |
| qualification[1].extension[0].extension[0].url | "status" |
| qualification[1].extension[0].extension[0].valueCode | "active" |
| qualification[1].extension[0].extension[1].url | "whereValid" |
| qualification[1].extension[0].extension[1].valueCodeableConcept.coding[0].code | #IL |
| qualification[1].extension[0].extension[1].valueCodeableConcept.coding[0].system | "https://www.usps.com/" |
| qualification[1].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification" |
| qualification[1].code.coding[0].code | #207R00000X |
| qualification[1].code.coding[0].system | "http://nucc.org/provider-taxonomy" |
| qualification[1].code.coding[0].display | "Internal Medicine Physician" |
| qualification[1].code.text | "Board Certified Internal Medicine" |
| qualification[1].issuer.display | "American Board of Internal Medicine" |
| qualification[2].extension[0].extension[0].url | "status" |
| qualification[2].extension[0].extension[0].valueCode | "active" |
| qualification[2].extension[0].extension[1].url | "whereValid" |
| qualification[2].extension[0].extension[1].valueCodeableConcept.coding[0].code | #IL |
| qualification[2].extension[0].extension[1].valueCodeableConcept.coding[0].system | "https://www.usps.com/" |
| qualification[2].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification" |
| qualification[2].code.coding[0].code | #207RC0000X |
| qualification[2].code.coding[0].system | "http://nucc.org/provider-taxonomy" |
| qualification[2].code.coding[0].display | "Cardiovascular Disease Physician" |
| qualification[2].code.text | "Board Certified Cardiovascular Disease" |
| qualification[2].issuer.display | "American Board of Internal Medicine" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency" |
| extension[0].valueCodeableConcept.coding[0].code | #30 |
| extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/LanguageProficiencyCS" |
| language | "en-US" |
| name[0].text | "Hans Solo, MD" |
| name[0].family | "Solo" |
| name[0].given[0] | "Hans" |
| communication[0].coding[0].code | #ja |
| communication[0].coding[0].system | "urn:ietf:bcp:47" |