# Extension: Communication Proficiency

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Communication Proficiency**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-communication-proficiency-definitions.html)
* [Mappings](StructureDefinition-communication-proficiency-mappings.html)

## Extension: Communication Proficiency

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: CommunicationProficiency |

An extension to express a practitioner’s spoken proficiency with the language indicated in practitioner.communication.

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html)
* Examples for this Extension: [Practitioner/Counselor](Practitioner-Counselor.html), [Practitioner/HansSolo](Practitioner-HansSolo.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 2 elements  
 Fixed Value: 1 element  
 Prohibited: 1 element

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

* The element Extension.value[x] is sliced based on the value of type:$this

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-communication-proficiency-definitions.html#Extension "An extension to express a practitioner’s spoken proficiency with the language indicated in practitioner.communication.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Communication Proficiency |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-communication-proficiency-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency" |
| ... [Slices for value[x]](StructureDefinition-communication-proficiency-definitions.html#Extension.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Slice: Unordered, Open by type:$this |
| ... [valueCodeableConcept](StructureDefinition-communication-proficiency-definitions.html#Extension.valueCodeableConcept) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Language Proficiency VS](ValueSet-LanguageProficiencyVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-communication-proficiency-definitions.html#Extension "An extension to express a practitioner’s spoken proficiency with the language indicated in practitioner.communication.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Communication Proficiency |
| ... [id](StructureDefinition-communication-proficiency-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-communication-proficiency-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-communication-proficiency-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency" |
| ... [Slices for value[x]](StructureDefinition-communication-proficiency-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Slice: Unordered, Closed by type:$this |
| .... [value[x]:valueCodeableConcept](StructureDefinition-communication-proficiency-definitions.html#Extension.value[x]:valueCodeableConcept "Slice valueCodeableConcept: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Language Proficiency VS](ValueSet-LanguageProficiencyVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 2 elements  
 Fixed Value: 1 element  
 Prohibited: 1 element

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

* The element Extension.value[x] is sliced based on the value of type:$this

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-communication-proficiency-definitions.html#Extension "An extension to express a practitioner’s spoken proficiency with the language indicated in practitioner.communication.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Communication Proficiency |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-communication-proficiency-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency" |
| ... [Slices for value[x]](StructureDefinition-communication-proficiency-definitions.html#Extension.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Slice: Unordered, Open by type:$this |
| ... [valueCodeableConcept](StructureDefinition-communication-proficiency-definitions.html#Extension.valueCodeableConcept) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Language Proficiency VS](ValueSet-LanguageProficiencyVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-communication-proficiency-definitions.html#Extension "An extension to express a practitioner’s spoken proficiency with the language indicated in practitioner.communication.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Communication Proficiency |
| ... [id](StructureDefinition-communication-proficiency-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-communication-proficiency-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-communication-proficiency-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency" |
| ... [Slices for value[x]](StructureDefinition-communication-proficiency-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Slice: Unordered, Closed by type:$this |
| .... [value[x]:valueCodeableConcept](StructureDefinition-communication-proficiency-definitions.html#Extension.value[x]:valueCodeableConcept "Slice valueCodeableConcept: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Language Proficiency VS](ValueSet-LanguageProficiencyVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-communication-proficiency.csv), [Excel](StructureDefinition-communication-proficiency.xlsx), [Schematron](StructureDefinition-communication-proficiency.sch)

#### Terminology Bindings

|  |  |  |
| --- | --- | --- |
| **Path** | **Conformance** | **ValueSet** |
| Extension.value[x]:valueCodeableConcept | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [LanguageProficiencyVS](ValueSet-LanguageProficiencyVS.html) |