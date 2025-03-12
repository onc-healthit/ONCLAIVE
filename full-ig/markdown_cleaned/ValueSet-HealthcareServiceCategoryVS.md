# ValueSet: Healthcare Service CategoryVS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Healthcare Service CategoryVS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Healthcare Service CategoryVS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/HealthcareServiceCategoryVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: HealthcareServiceCategoryVS |

Broad categories of healthcare services being performed or delivered.

**References**

* [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS`](CodeSystem-HealthcareServiceCategoryCS.html)

### Expansion

This value set contains 15 concepts

Expansion based on [Healthcare Service Category v1.1.0 (CodeSystem)](CodeSystem-HealthcareServiceCategoryCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/HealthcareServiceCategoryCS`](CodeSystem-HealthcareServiceCategoryCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [behav](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-behav) | Behavioral Health | Services related to the promotion of mental health, resilience and wellbeing; the treatment of mental and substance use disorders; and the support of those who experience and/or are in recovery from these conditions, along with their families and communities. |
| [dent](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-dent) | Dental | Services related to the study, diagnosis, prevention, and treatment of diseases, disorders, and conditions of the mouth. |
| [dme](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-dme) | DME/Medical Supplies | Health care consumables or equipments supplied to patients |
| [emerg](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-emerg) | Emergency care | Health care services rendered within a designated emergency care facility, for point-in-time evaluation and/or treatment any medical condition such that a prudent layperson possessing an average knowledge of medicine and health, believes that immediate unscheduled medical care is required. |
| [group](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-group) | Medical Group | Health care services rendered by a group of people, e.g. a group of Physicians. |
| [home](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-home) | Home Health | Health care services delivered to patients within their residence rather than a clinical setting; usually provided by nurses, home health aides, and other professionals on a regularly scheduled visit. |
| [hosp](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-hosp) | Hospital | Health care services rendered within a hospital or other inpatient setting providng patient treatment with specialzed medical and nursing staff and medical equipment. |
| [lab](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-lab) | Laboratory | Pathology and laboratory testing on clinical specimenst to obtain informaion about the health of a paeint to aid in diagnosis, treatment and prevention of disease. |
| [other](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-other) | Other | Other |
| [outpat](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-outpat) | Clinic or Outpatient Facility | Health care services rendered in an outpatient facility, e.g. medical procedures, surgeries, etc. |
| [prov](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-prov) | Medical Provider | Health care services rendered by a person, e.g. Physician. |
| [pharm](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-pharm) | Pharmacy | Services related to the storage, compounding, dispensing and sale of drugs. |
| [trans](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-trans) | Transportation | Services which transport patients to or from a medical facility, e.g., ambulance. |
| [urg](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-urg) | Urgent Care | Unscheduled health care services which provide for point-in-time evaluation or treatment of a non-life-threatening medical condition. |
| [vis](CodeSystem-HealthcareServiceCategoryCS.html#HealthcareServiceCategoryCS-vis) | Vision | Services related to the study, diagnosis, prevention, and treatment of diseases, disorders, and conditions of the eyes. |

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