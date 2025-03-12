# Example HealthcareService: HartfordOrthopedicServices

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **HartfordOrthopedicServices**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example HealthcareService: HartfordOrthopedicServices

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "HartfordOrthopedicServices" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

> **Delivery Method**
>
> **value**: Physical  ([Delivery Methods](CodeSystem-DeliveryMethodCS.html)#physical)

**active**: true

**providedBy**: [Organization/HartfordOrthopedics](Organization-HartfordOrthopedics.html) "Hartford Orthopedics Services"

**category**: Medical Provider  ([Healthcare Service Category](CodeSystem-HealthcareServiceCategoryCS.html)#prov)

**specialty**: Orthopaedic Surgery Physician  (provider-taxonomy#207X00000X)

**location**:

* [Location/HospLoc1](Location-HospLoc1.html) "Hartford Hospital Location 1"
* [Location/HospLoc2](Location-HospLoc2.html) "Hartford Hospital Location 2"

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "HealthcareService" |
| id | "HartfordOrthopedicServices" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| extension[0].extension[0].url | "type" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #physical |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS" |
| language | "en-US" |
| category[0].coding[0].code | #prov |
| category[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS" |
| specialty[0].coding[0].code | #207X00000X |
| specialty[0].coding[0].system | "http://nucc.org/provider-taxonomy" |
| specialty[0].coding[0].display | "Orthopaedic Surgery Physician" |
| providedBy.reference | "Organization/HartfordOrthopedics" |
| location[0].reference | "Location/HospLoc1" |
| location[1].reference | "Location/HospLoc2" |