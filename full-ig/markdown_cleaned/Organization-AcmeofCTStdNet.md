# Example Organization: AcmeofCTStdNet

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **AcmeofCTStdNet**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Organization: AcmeofCTStdNet

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "AcmeofCTStdNet" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Network](StructureDefinition-plannet-Network.html)

**active**: true

**type**: Network  ([Organization Type](CodeSystem-OrgTypeCS.html)#ntwk)

**name**: ACME CT Preferred Provider Network

**partOf**: [Organization/Acme](Organization-Acme.html) "Acme of CT"

### Contacts

|  |  |  |
| --- | --- | --- |
| - | **Name** | **Telecom** |
| \* | Jane Kawasaki | -unknown- |

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Organization" |
| id | "AcmeofCTStdNet" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| contact[0].telecom[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |
| contact[0].telecom[0].extension[0].valueReference.reference | "Organization/Acme" |
| contact[0].name.family | "Kawasaki" |
| contact[0].name.given[0] | "Jane" |
| language | "en-US" |
| partOf.reference | "Organization/Acme" |
| type[0].coding[0].code | #ntwk |
| type[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS" |
| type[0].coding[0].display | "Network" |
| name | "ACME CT Preferred Provider Network" |