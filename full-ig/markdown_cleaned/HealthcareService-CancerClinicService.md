# Example HealthcareService: CancerClinicService

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **CancerClinicService**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example HealthcareService: CancerClinicService

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "CancerClinicService" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

> **Delivery Method**
>
> **value**: Physical  ([Delivery Methods](CodeSystem-DeliveryMethodCS.html)#physical)

**active**: true

**providedBy**: [Organization/CancerClinic](Organization-CancerClinic.html) "Hamilton Clinic"

**category**: Clinic or Outpatient Facility  ([Healthcare Service Category](CodeSystem-HealthcareServiceCategoryCS.html)#outpat)

**specialty**: Medical Oncology Physician  (provider-taxonomy#207RX0202X)

**location**: [Location/CancerClinicLoc](Location-CancerClinicLoc.html) "Cancer Clinic"

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "HealthcareService" |
| id | "CancerClinicService" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| extension[0].extension[0].url | "type" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #physical |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS" |
| language | "en-US" |
| category[0].coding[0].code | #outpat |
| category[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS" |
| providedBy.reference | "Organization/CancerClinic" |
| specialty[0].coding[0].code | #207RX0202X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Medical Oncology Physician" |
| location[0].reference | "Location/CancerClinicLoc" |