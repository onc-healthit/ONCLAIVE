# ValueSet: Organization Type VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Organization Type VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Organization Type VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/OrgTypeVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: OrgTypeVS |

Categories of organizations based on criteria in provider directories.

**References**

* [Plan-Net Organization](StructureDefinition-plannet-Organization.html)

### Logical Definition (CLD)

This value set includes codes based on the following rules:

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS`](CodeSystem-OrgTypeCS.html)

This value set excludes codes based on the following rules:

* Exclude these codes as defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS`](CodeSystem-OrgTypeCS.html)

  |  |  |  |
  | --- | --- | --- |
  | **Code** | **Display** | **Definition** |
  | [ntwk](CodeSystem-OrgTypeCS.html#OrgTypeCS-ntwk) | Network | A healthcare provider insurance network |

### Expansion

This value set contains 5 concepts

Expansion based on [Organization Type v1.1.0 (CodeSystem)](CodeSystem-OrgTypeCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS`](CodeSystem-OrgTypeCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [fac](CodeSystem-OrgTypeCS.html#OrgTypeCS-fac) | Facility | A physical healthcare facility. |
| [prvgrp](CodeSystem-OrgTypeCS.html#OrgTypeCS-prvgrp) | Provider Group | A healthcare provider entity |
| [payer](CodeSystem-OrgTypeCS.html#OrgTypeCS-payer) | Payer | A healthcare payer. |
| [atyprv](CodeSystem-OrgTypeCS.html#OrgTypeCS-atyprv) | Atypical Provider | Providers that do not provide healthcare |
| [bus](CodeSystem-OrgTypeCS.html#OrgTypeCS-bus) | Non-Healthcare Business | An organization that does not meet the definitions of a Healthcare or Atypical Provider, and is not a payer or healthcare facility |

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