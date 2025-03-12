# ValueSet: Virtual Modalities VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Virtual Modalities VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Virtual Modalities VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/VirtualModalitiesVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: VirtualModalitiesVS |

Codes for virtual service delivery modalities .

**References**

* [Delivery Method](StructureDefinition-delivery-method.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/VirtualModalitiesCS`](CodeSystem-VirtualModalitiesCS.html)

### Expansion

This value set contains 6 concepts

Expansion based on [Virtual Modalities v1.1.0 (CodeSystem)](CodeSystem-VirtualModalitiesCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/VirtualModalitiesCS`](CodeSystem-VirtualModalitiesCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [phone](CodeSystem-VirtualModalitiesCS.html#VirtualModalitiesCS-phone) | phone | Voice Telephone |
| [video](CodeSystem-VirtualModalitiesCS.html#VirtualModalitiesCS-video) | video chat | Video Chat |
| [tdd](CodeSystem-VirtualModalitiesCS.html#VirtualModalitiesCS-tdd) | TDD | Telecommunications Device for the Deaf |
| [sms](CodeSystem-VirtualModalitiesCS.html#VirtualModalitiesCS-sms) | SMS | SMS Text Messaging |
| [app](CodeSystem-VirtualModalitiesCS.html#VirtualModalitiesCS-app) | App | Mobile Application |
| [web](CodeSystem-VirtualModalitiesCS.html#VirtualModalitiesCS-web) | Website | Website accessed through browser |

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