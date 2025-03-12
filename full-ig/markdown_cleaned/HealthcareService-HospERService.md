# Example HealthcareService: HospERService

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **HospERService**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example HealthcareService: HospERService

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HospERService" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

> **Delivery Method**
>
> **value**: Physical  ([Delivery Methods](CodeSystem-DeliveryMethodCS.html)#physical)

**active**: true

**providedBy**: [Organization/Hospital](Organization-Hospital.html) "Hartford General Hospital"

**category**: Emergency care  ([Healthcare Service Category](CodeSystem-HealthcareServiceCategoryCS.html)#emerg)

**specialty**: Emergency Medicine Physician  (provider-taxonomy#207P00000X)

**location**: [Location/HospLoc1](Location-HospLoc1.html) "Hartford Hospital Location 1"

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "HealthcareService" |
| id | "HospERService" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| extension[0].extension[0].url | "type" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #physical |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS" |
| language | "en-US" |
| category[0].coding[0].code | #emerg |
| category[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS" |
| specialty[0].coding[0].code | #207P00000X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Emergency Medicine Physician" |
| providedBy.reference | "Organization/Hospital" |
| location[0].reference | "Location/HospLoc1" |