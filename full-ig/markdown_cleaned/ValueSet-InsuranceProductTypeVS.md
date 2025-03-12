# ValueSet: Insurance Product Type VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Insurance Product Type VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Insurance Product Type VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/InsuranceProductTypeVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: InsuranceProductTypeVS |

A distinct package of health insurance coverage benefits that are offered using a particular product network type.

**References**

* [Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsuranceProductTypeCS`](CodeSystem-InsuranceProductTypeCS.html)

### Expansion

This value set contains 22 concepts

Expansion based on [Insurance Product Type v1.1.0 (CodeSystem)](CodeSystem-InsuranceProductTypeCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsuranceProductTypeCS`](CodeSystem-InsuranceProductTypeCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [commppo](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-commppo) | Commercial PPO | Health insurance provided through a Preferred Provider Organization (PPO). |
| [commhdhp](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-commhdhp) | Commercial HDHP | Health insurance provided through a High Deductible Health Plan (HDHP). |
| [commpos](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-commpos) | Commercial POS | Health insurance provided through a Point-of-Service (POS) Plan. |
| [commhmo](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-commhmo) | Commercial HMO | Health insurance provided through a Health Maintenance Organization (HMO). |
| [commepo](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-commepo) | Commercial EPO | Health insurance provided through a Exclusive Provider Organization(EPO). |
| [medi](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-medi) | Medicaid | Health insurance provided to eligible adults and children under the Federal Medicaid program |
| [medihmo](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-medihmo) | Medicaid HMO | Health insurance provided to eligible adults and children under the Federal Medicaid program through a Health Maintenance Organization (HMO). |
| [mediadv](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-mediadv) | Medicare Advantage | Health insurance provided by a private company that contracts with Medicare to provide all Medicare Part A and Part B benefits. |
| [mediadvhmo](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-mediadvhmo) | Medicare Advantage HMO | Health insurance offered by a private company that contracts with Medicare to provide all Medicare Part A and Part B benefits through a Health Maintenance Organization (HMO). |
| [media](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-media) | Medicare Part A | Health insurance provided under the Federal Medicare program covering inpatient hospital stays, care in a skilled nursing facility, hospice care, and some home health care. |
| [medib](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-medib) | Medicare Part B | Health insurance provided under the Federal Medicfare program covering certain doctors' services, outpatient care, medical supplies, and preventive services. |
| [medid](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-medid) | Medicare Part D | Health insurance provided under the Federal Medicare program covering prescription drugs. |
| [mediab](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-mediab) | Medicare A/B | Health insurance provided under the Federal Medicare program covering inpatient hospital stays, care in a skilled nursing facility, hospice care, some home health care, certain doctors' services, outpatient care, medical supplies, and preventive services. |
| [qhp](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-qhp) | Qualified Health Plan | Health insurance provided through and certified by the Health Insurance Marketplace that provides essential health benefits (EHBs), follows established limits on cost sharing, and meets other requirements outlined within the application process. |
| [ihs](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-ihs) | Indian Health Service | Health care program provided to United States American Indians and Alaska Natives. |
| [fep](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-fep) | Federal Employee Program | Health insurance provided to employees of the Federal government. |
| [tri](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-tri) | TRICARE | Health care program provided to uniformed service members, retirees, and their families around the world. |
| [va](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-va) | Veterans Affairs Plan | Health care program provided to eligible veterans. |
| [dent](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-dent) | Dental Plan | Health insurance provided to cover services related to the study, diagnosis, prevention, and treatment of diseases, disorders, and conditions of the oral cavity. |
| [denthmo](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-denthmo) | Dental HMO | Health insurance provided to cover services related to the study, diagnosis, prevention, and treatment of diseases, disorders, and conditions of the oral cavity provided through a Health Maintenance Organization (HMO). |
| [vis](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-vis) | Vision Plan | Health insurance provided to cover services related to the study, diagnosis, prevention, and treatment of diseases, disorders, and conditions of the eyes. |
| [vishmo](CodeSystem-InsuranceProductTypeCS.html#InsuranceProductTypeCS-vishmo) | Vision HMO | Health insurance provided to cover services related to the study, diagnosis, prevention, and treatment of diseases, disorders, and conditions of the eyes provided through a Health Maintenance Organization (HMO). |

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