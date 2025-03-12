# ValueSet: Language Proficiency VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Language Proficiency VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Language Proficiency VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/LanguageProficiencyVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: LanguageProficiencyVS |

Codes for documenting spoken language proficiency based on the Interagency Language Roundtable scale of abilities to communicate in a language.

**References**

* [Communication Proficiency](StructureDefinition-communication-proficiency.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/LanguageProficiencyCS`](CodeSystem-LanguageProficiencyCS.html)

### Expansion

This value set contains 6 concepts

Expansion based on [Language Proficiency CS v1.1.0 (CodeSystem)](CodeSystem-LanguageProficiencyCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/LanguageProficiencyCS`](CodeSystem-LanguageProficiencyCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [00](CodeSystem-LanguageProficiencyCS.html#LanguageProficiencyCS-00) | No proficiency | Unable to function in the spoken language. |
| [10](CodeSystem-LanguageProficiencyCS.html#LanguageProficiencyCS-10) | Elementary proficiency | Able to satisfy minimum courtesy requirements and maintain very simple face-to-face conversations on familiar topics. A native speaker must often use slowed speech, repetition, paraphrase, or a combination of these to be understood by this individual. |
| [20](CodeSystem-LanguageProficiencyCS.html#LanguageProficiencyCS-20) | Limited working proficiency | Able to satisfy routine social demands and limited work requirements. |
| [30](CodeSystem-LanguageProficiencyCS.html#LanguageProficiencyCS-30) | General professional proficiency | Able to speak the language with sufficient structural accuracy and vocabulary to participate effectively in most formal and informal conversations in practical, social and professional topics. |
| [40](CodeSystem-LanguageProficiencyCS.html#LanguageProficiencyCS-40) | Advanced professional proficiency | Able to use the language fluently and accurately on all levels normally pertinent to professional needs. |
| [50](CodeSystem-LanguageProficiencyCS.html#LanguageProficiencyCS-50) | Functional native proficiency | Speaking proficiency is functionally equivalent to that of a highly articulate well-educated native speaker and reflects the cultural standards of the country where the language is natively spoken. |

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