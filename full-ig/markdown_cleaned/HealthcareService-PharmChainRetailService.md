# Example HealthcareService: PharmChainRetailService

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **PharmChainRetailService**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example HealthcareService: PharmChainRetailService

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "PharmChainRetailService" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

> **Delivery Method**
>
> **value**: Physical  ([Delivery Methods](CodeSystem-DeliveryMethodCS.html)#physical)

> **New Patients**
>
> **value**: Accepting existing patients  ([Accepting Patients Codes](CodeSystem-AcceptingPatientsCS.html)#existptonly)
>
> **value**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

**active**: true

**providedBy**: [Organization/PharmChain](Organization-PharmChain.html) "Pharm Chain"

**category**: Pharmacy  ([Healthcare Service Category](CodeSystem-HealthcareServiceCategoryCS.html)#pharm)

**specialty**: Community/Retail Pharmacy  (provider-taxonomy#3336C0003X)

**location**:

* [Location/PharmLoc1](Location-PharmLoc1.html) "OrgA CT Location 1"
* [Location/PharmLoc2](Location-PharmLoc2.html) "OrgA CT Location 2"
* [Location/PharmLoc3](Location-PharmLoc3.html) "OrgA MA Location 1"
* [Location/PharmLoc4](Location-PharmLoc4.html) "OrgA MA Location 2"

**name**: Pharmacy by PharmChain

**telecom**: -unknown-

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "HealthcareService" |
| id | "PharmChainRetailService" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| extension[0].extension[0].url | "type" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #physical |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS" |
| extension[1].extension[0].url | "acceptingPatients" |
| extension[1].extension[0].valueCodeableConcept.coding[0].code | #existptonly |
| extension[1].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AcceptingPatientsCS" |
| extension[1].extension[1].url | "fromNetwork" |
| extension[1].extension[1].valueReference.reference | "Organization/AcmeofCTStdNet" |
| extension[1].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients" |
| telecom[0].extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |
| telecom[0].extension[0].valueReference.reference | "Organization/PharmChain" |
| language | "en-US" |
| name | "Pharmacy by PharmChain" |
| category[0].coding[0].code | #pharm |
| category[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS" |
| category[0].coding[0].display | "Pharmacy" |
| specialty[0].coding[0].code | #3336C0003X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Community/Retail Pharmacy" |
| providedBy.reference | "Organization/PharmChain" |
| location[0].reference | "Location/PharmLoc1" |
| location[1].reference | "Location/PharmLoc2" |
| location[2].reference | "Location/PharmLoc3" |
| location[3].reference | "Location/PharmLoc4" |