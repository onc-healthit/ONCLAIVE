# ValueSet: Delivery Methods VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Delivery Methods VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Delivery Methods VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/DeliveryMethodVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: DeliveryMethodVS |

Codes for documenting delivery methods.

**References**

* [Delivery Method](StructureDefinition-delivery-method.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS`](CodeSystem-DeliveryMethodCS.html)

### Expansion

This value set contains 2 concepts

Expansion based on [Delivery Methods v1.1.0 (CodeSystem)](CodeSystem-DeliveryMethodCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/DeliveryMethodCS`](CodeSystem-DeliveryMethodCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [virtual](CodeSystem-DeliveryMethodCS.html#DeliveryMethodCS-virtual) | Virtual | Delivery not requiring provider and patient to be physically co-located, such as tele-medicine |
| [physical](CodeSystem-DeliveryMethodCS.html#DeliveryMethodCS-physical) | Physical | Traditional delivery requiring provider and patient to be physically co-located. |

---

Explanation of the columns that may appear on this page:

|  |  |
| --- | --- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the *display* element of a [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |