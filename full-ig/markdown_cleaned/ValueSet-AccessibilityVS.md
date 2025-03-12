# ValueSet: Accessibility VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Accessibility VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Accessibility VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/AccessibilityVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: AccessibilityVS |

Codes for documenting general categories of accommodations available.

**References**

* [Accessibility](StructureDefinition-accessibility.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AccessibilityCS`](CodeSystem-AccessibilityCS.html)

### Expansion

This value set contains 7 concepts

Expansion based on [Accessibility CS v1.1.0 (CodeSystem)](CodeSystem-AccessibilityCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/AccessibilityCS`](CodeSystem-AccessibilityCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [cultcomp](CodeSystem-AccessibilityCS.html#AccessibilityCS-cultcomp) | Cultural competence | Provides services that meet the social, cultural, and linguistic needs of persons. |
| [handiaccess](CodeSystem-AccessibilityCS.html#AccessibilityCS-handiaccess) | handicap accessible | Provides access to persons with disabilities. |
| [adacomp](CodeSystem-AccessibilityCS.html#AccessibilityCS-adacomp) | ADA compliant | Provides access which complies with the Americans with Disabilities Act and/or amendments. |
| [pubtrans](CodeSystem-AccessibilityCS.html#AccessibilityCS-pubtrans) | public transit options | Provides access using public transportation modes. |
| [anssrvc](CodeSystem-AccessibilityCS.html#AccessibilityCS-anssrvc) | answering service | Provides capability to communicate when intended recipient is not immediately available. |
| [cognitive](CodeSystem-AccessibilityCS.html#AccessibilityCS-cognitive) | cognitive | Provides services for cognitively impaired persons. |
| [mobility](CodeSystem-AccessibilityCS.html#AccessibilityCS-mobility) | mobility | Provides services for mobility impaired persons. |

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