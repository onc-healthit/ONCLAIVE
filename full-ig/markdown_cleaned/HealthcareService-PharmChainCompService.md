# Example HealthcareService: PharmChainCompService

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **PharmChainCompService**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example HealthcareService: PharmChainCompService

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "PharmChainCompService" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

> **Delivery Method**
>
> **value**: Physical  ([Delivery Methods](CodeSystem-DeliveryMethodCS.html)#physical)

**active**: true

**providedBy**: [Organization/PharmChain](Organization-PharmChain.html) "Pharm Chain"

**category**: Pharmacy  ([Healthcare Service Category](CodeSystem-HealthcareServiceCategoryCS.html)#pharm)

**specialty**: Compounding Pharmacy  (provider-taxonomy#3336C0004X)

**location**: [Location/PharmLoc1](Location-PharmLoc1.html) "OrgA CT Location 1"

**name**: Compounding Pharmacy by OrgA

**telecom**: -unknown-

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "HealthcareService" |
| id | "PharmChainCompService" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| extension[0].extension[0].url | "type" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #physical |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS" |
| telecom[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |
| telecom[0].extension[0].valueReference.reference | "Location/PharmLoc1" |
| language | "en-US" |
| name | "Compounding Pharmacy by OrgA" |
| category[0].coding[0].code | #pharm |
| category[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS" |
| category[0].coding[0].display | "Pharmacy" |
| specialty[0].coding[0].code | #3336C0004X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Compounding Pharmacy" |
| specialty[0].text | "Compounding Pharmacy" |
| providedBy.reference | "Organization/PharmChain" |
| location[0].reference | "Location/PharmLoc1" |