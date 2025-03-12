# ValueSet: Endpoint Usecases VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Endpoint Usecases VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Endpoint Usecases VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/EndpointUsecaseVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: EndpointUsecaseVS |

Codes for documenting business use case by a general grouping by business area.

**References**

* [Endpoint Usecase](StructureDefinition-endpoint-usecase.html)

### Logical Definition (CLD)

* Include these codes as defined in [`http://terminology.hl7.org/CodeSystem/v3-ActReason`](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html)

  |  |  |  |
  | --- | --- | --- |
  | **Code** | **Display** | **Definition** |
  | [TREAT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-TREAT) | treatment | To perform one or more operations on information for provision of health care. |
  | [HPAYMT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-HPAYMT) | healthcare payment | To perform one or more operations on information for conducting financial or contractual activities related to payment for provision of health care. |
  | [COC](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-COC) | coordination of care | To perform one or more actions on information in order to organize the provision and case management of an individualâ€™s healthcare, including: Monitoring a person's goals, needs, and preferences; acting as the communication link between two or more participants concerned with a person's health and wellness; organizing and facilitating care activities and promoting self-management by advocating for, empowering, and educating a person; and ensuring safe, appropriate, non-duplicative, and effective integrated care.  \*Usage Note:\* Use when describing these functions: 1. Monitoring a personâ€™s goals, needs, and preferences. 2. Acting as the communication link between two or more participants concerned with a person's health and wellness. 3. Organizing and facilitating care activities and promoting self-management by advocating for, empowering, and educating a person. 4. Ensuring safe, appropriate, non-duplicative, and effective integrated care.  The goal is to clearly differentiate this type of coordination of care from HIPAA Operations by specifying that these actions on information are undertaken in the provision of healthcare treatment.  For similar uses of this concept, see SAMHSA Confidentiality of Substance Use Disorder Patient Records Supplemental notice of proposed rulemaking, which differentiates concepts of care coordination and case management for the provision of treatment as specifically distinct from activities related to health care delivery management and the operations of organizational entities involved in the delivery of healthcare.  \*Map:\* Maps to ISO 14265 Classification Terms: "Support of care activities within the provider organisation for an individual subject of care" described as "To inform persons or processes enabling others to provide health care services to the subject of care." "Subject of Care Uses" described as "To inform the subject of care in support of his or her own interests." |
  | [COVERAGE](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-COVERAGE) | eligibility verification and determination | To perform one or more operations on information for conducting activities related to coverage under a program or policy. |
  | [HOPERAT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-HOPERAT) | healthcare operations | To perform one or more operations on information used for conducting administrative and contractual activities related to the provision of health care. |
  | [PUBHLTH](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-PUBHLTH) | public health | To perform one or more operations on information for conducting public health activities, such as the reporting of notifiable conditions. |
  | [HRESCH](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-HRESCH) | healthcare research | To perform one or more operations on information for conducting scientific investigations to obtain health care knowledge. Use of the data iincludes basic and applied research such as biomedical, population origin or ancestry, translational research, and disease, discipline, specialty specific healthcare research and clinical trial research. |
  | [ETREAT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-ETREAT) | emergency treatment | To perform one or more operations on information for provision of immediately needed health care for an emergent condition. |
  | [PATRQT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-PATRQT) | patient requested | To perform one or more operations on information in response to a patient's request. |

### Expansion

This value set contains 9 concepts

Expansion based on [ActReason v2.1.0 (CodeSystem)](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html)

All codes in this table are from the system [`http://terminology.hl7.org/CodeSystem/v3-ActReason`](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [TREAT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-TREAT) | treatment | To perform one or more operations on information for provision of health care. |
| [HPAYMT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-HPAYMT) | healthcare payment | To perform one or more operations on information for conducting financial or contractual activities related to payment for provision of health care. |
| [COC](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-COC) | coordination of care | To perform one or more actions on information in order to organize the provision and case management of an individualâ€™s healthcare, including: Monitoring a person's goals, needs, and preferences; acting as the communication link between two or more participants concerned with a person's health and wellness; organizing and facilitating care activities and promoting self-management by advocating for, empowering, and educating a person; and ensuring safe, appropriate, non-duplicative, and effective integrated care. \*Usage Note:\* Use when describing these functions: 1. Monitoring a personâ€™s goals, needs, and preferences. 2. Acting as the communication link between two or more participants concerned with a person's health and wellness. 3. Organizing and facilitating care activities and promoting self-management by advocating for, empowering, and educating a person. 4. Ensuring safe, appropriate, non-duplicative, and effective integrated care. The goal is to clearly differentiate this type of coordination of care from HIPAA Operations by specifying that these actions on information are undertaken in the provision of healthcare treatment. For similar uses of this concept, see SAMHSA Confidentiality of Substance Use Disorder Patient Records Supplemental notice of proposed rulemaking, which differentiates concepts of care coordination and case management for the provision of treatment as specifically distinct from activities related to health care delivery management and the operations of organizational entities involved in the delivery of healthcare. \*Map:\* Maps to ISO 14265 Classification Terms: "Support of care activities within the provider organisation for an individual subject of care" described as "To inform persons or processes enabling others to provide health care services to the subject of care." "Subject of Care Uses" described as "To inform the subject of care in support of his or her own interests." |
| [COVERAGE](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-COVERAGE) | eligibility verification and determination | To perform one or more operations on information for conducting activities related to coverage under a program or policy. |
| [HOPERAT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-HOPERAT) | healthcare operations | To perform one or more operations on information used for conducting administrative and contractual activities related to the provision of health care. |
| [PUBHLTH](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-PUBHLTH) | public health | To perform one or more operations on information for conducting public health activities, such as the reporting of notifiable conditions. |
| [HRESCH](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-HRESCH) | healthcare research | To perform one or more operations on information for conducting scientific investigations to obtain health care knowledge. Use of the data iincludes basic and applied research such as biomedical, population origin or ancestry, translational research, and disease, discipline, specialty specific healthcare research and clinical trial research. |
| [ETREAT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-ETREAT) | emergency treatment | To perform one or more operations on information for provision of immediately needed health care for an emergent condition. |
| [PATRQT](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html#v3-ActReason-PATRQT) | patient requested | To perform one or more operations on information in response to a patient's request. |

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