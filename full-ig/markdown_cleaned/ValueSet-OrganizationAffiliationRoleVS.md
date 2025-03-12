# ValueSet: OrganizationAffiliation Roles

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **OrganizationAffiliation Roles**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: OrganizationAffiliation Roles

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/OrganizationAffiliationRoleVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: OrganizationAffiliationRoleVS |

Value Set for Organization Affiliation Roles

**References**

* [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

### Logical Definition (CLD)

This value set includes codes based on the following rules:

* Include all codes defined in [`http://hl7.org/fhir/organization-role`](http://hl7.org/fhir/R4/codesystem-organization-role.html)
* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS`](CodeSystem-OrganizationAffiliationRoleCS.html)

This value set excludes codes based on the following rules:

* Exclude these codes as defined in [`http://hl7.org/fhir/organization-role`](http://hl7.org/fhir/R4/codesystem-organization-role.html)

  |  |  |  |
  | --- | --- | --- |
  | **Code** | **Display** | **Definition** |
  | [member](http://hl7.org/fhir/R4/codesystem-organization-role.html#organization-role-member) | Member | A type of non-ownership relationship between entities (encompasses partnerships, collaboration, joint ventures, etc.) |

### Expansion

This value set contains 24 concepts

Expansion based on:

* [Organization Affiliation Role v4.0.1 (CodeSystem)](http://hl7.org/fhir/R4/codesystem-organization-role.html)
* [Organization Affiliation Role v1.1.0 (CodeSystem)](CodeSystem-OrganizationAffiliationRoleCS.html)

|  |  |  |  |
| --- | --- | --- | --- |
| **Code** | **System** | **Display** | **Definition** |
| [provider](http://hl7.org/fhir/R4/codesystem-organization-role.html#organization-role-provider) | http://hl7.org/fhir/organization-role | Provider |  |
| [agency](http://hl7.org/fhir/R4/codesystem-organization-role.html#organization-role-agency) | http://hl7.org/fhir/organization-role | Agency | An organization such as a public health agency, community/social services provider, etc. |
| [research](http://hl7.org/fhir/R4/codesystem-organization-role.html#organization-role-research) | http://hl7.org/fhir/organization-role | Research | An organization providing research-related services such as conducting research, recruiting research participants, analyzing data, etc. |
| [payer](http://hl7.org/fhir/R4/codesystem-organization-role.html#organization-role-payer) | http://hl7.org/fhir/organization-role | Payer | An organization providing reimbursement, payment, or related services |
| [diagnostics](http://hl7.org/fhir/R4/codesystem-organization-role.html#organization-role-diagnostics) | http://hl7.org/fhir/organization-role | Diagnostics | An organization providing diagnostic testing/laboratory services |
| [supplier](http://hl7.org/fhir/R4/codesystem-organization-role.html#organization-role-supplier) | http://hl7.org/fhir/organization-role | Supplier | An organization that provides medical supplies (e.g. medical devices, equipment, pharmaceutical products, etc.) |
| [HIE/HIO](http://hl7.org/fhir/R4/codesystem-organization-role.html#organization-role-HIE.47HIO) | http://hl7.org/fhir/organization-role | HIE/HIO | An organization that facilitates electronic clinical data exchange between entities |
| [behavioral](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-behavioral) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Outpatient Behavioral Health Provider | Provider of services related to the promotion of mental health, resilience and wellbeing; the treatment of mental and substance use disorders; and the support of those who experience and/or are in recovery from these conditions, along with their families and communities. |
| [bt](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-bt) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Member Of | Has a relationship of participation with. This does NOT represent a member of an insurance plan, but other types of membership such as membership of a hospital in an HIE |
| [dme](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-dme) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | DME/Medical Supplier | Supplier of health care consumables or equipments supplied to patients. |
| [group](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-group) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Medical Group | A group of people, e.g. a group of Physicians, who render health care services. |
| [home](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-home) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Home Health Provider | Provider of health care services delivered to patients within their residence rather than a clinical setting; usually provided by nurses, home health aides, and other professionals on a regularly scheduled visit. |
| [hospital](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-hospital) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Hospital | An inpatient facility, other than long-term care, providng patient treatment with specialzed medical and nursing staff and medical equipment. |
| [laboratory](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-laboratory) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Laboratory | Pathology and laboratory testing on clinical specimenst to obtain informaion about the health of a paeint to aid in diagnosis, treatment and prevention of disease. |
| [other](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-other) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Other | A provider of heatlh care services not otherwise listed in this value set. |
| [outpatient](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-outpatient) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Clinic or Outpatient Facility | An outpatient facility providing patient services, e.g. medical procedures, surgeries, etc. |
| [pharmacy](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-pharmacy) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Pharmacy | An entity which provider services related to the storage, compounding, dispensing and sale of drugs. |
| [transport](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-transport) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Transporation Provider | A provider which transports patients to or from a medical facility, e.g., ambulance. |
| [urgent](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-urgent) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Urgent Care Center | A center in which unscheduled health care services are provided for point-in-time evaluation or treatment of a non-life-threatening medical condition. |
| [hospice](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-hospice) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Hospice | Hospice |
| [nurseCustodial](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-nurseCustodial) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Nursing and Custodial Care Facility | Nursing and Custodial Care Facility |
| [residential](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-residential) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Residential Treatment Facility | Residential Treatment Facility |
| [respite](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-respite) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Respite Care Facility | Respite Care Facility |
| [retail](CodeSystem-OrganizationAffiliationRoleCS.html#OrganizationAffiliationRoleCS-retail) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrganizationAffiliationRoleCS | Retail Health Center | Retail Health Center |

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