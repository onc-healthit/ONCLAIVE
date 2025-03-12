# Example HealthcareService: VirtualCounselService

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **VirtualCounselService**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example HealthcareService: VirtualCounselService

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "VirtualCounselService" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

> **Delivery Method**
>
> **value**: Virtual  ([Delivery Methods](CodeSystem-DeliveryMethodCS.html)#virtual)
>
> **value**: Website  ([Virtual Modalities](CodeSystem-VirtualModalitiesCS.html)#web)
>
> **value**: App  ([Virtual Modalities](CodeSystem-VirtualModalitiesCS.html)#app)
>
> **value**: TDD  ([Virtual Modalities](CodeSystem-VirtualModalitiesCS.html)#tdd)
>
> **value**: phone  ([Virtual Modalities](CodeSystem-VirtualModalitiesCS.html)#phone)

**active**: true

**category**: Medical Provider  ([Healthcare Service Category](CodeSystem-HealthcareServiceCategoryCS.html)#prov)

**specialty**: Professional Counselor  (provider-taxonomy#101YP2500X)

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "HealthcareService" |
| id | "VirtualCounselService" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| extension[0].extension[0].url | "type" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #virtual |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS" |
| extension[0].extension[1].url | "virtualModalities" |
| extension[0].extension[1].valueCodeableConcept.coding[0].code | #web |
| extension[0].extension[1].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/VirtualModalitiesCS" |
| extension[0].extension[2].url | "virtualModalities" |
| extension[0].extension[2].valueCodeableConcept.coding[0].code | #app |
| extension[0].extension[2].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/VirtualModalitiesCS" |
| extension[0].extension[3].url | "virtualModalities" |
| extension[0].extension[3].valueCodeableConcept.coding[0].code | #tdd |
| extension[0].extension[3].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/VirtualModalitiesCS" |
| extension[0].extension[4].url | "virtualModalities" |
| extension[0].extension[4].valueCodeableConcept.coding[0].code | #phone |
| extension[0].extension[4].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/VirtualModalitiesCS" |
| language | "en-US" |
| category[0].coding[0].code | #prov |
| category[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS" |
| category[0].coding[0].display | "Medical Provider" |
| specialty[0].coding[0].code | #101YP2500X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Professional Counselor" |