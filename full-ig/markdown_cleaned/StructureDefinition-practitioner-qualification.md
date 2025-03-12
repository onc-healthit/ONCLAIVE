# Extension: Practitioner Qualification

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Practitioner Qualification**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-practitioner-qualification-definitions.html)
* [Mappings](StructureDefinition-practitioner-qualification-mappings.html)

## Extension: Practitioner Qualification

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: PractitionerQualification |

An extension to add status and whereValid elements to a practitioner’s qualifications.

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html)
* Examples for this Extension: [Practitioner/Counselor](Practitioner-Counselor.html), [Practitioner/HansSolo](Practitioner-HansSolo.html), [Practitioner/JoeSmith](Practitioner-JoeSmith.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 4 elements (1 nested mandatory element)  
 Must-Support: 2 elements  
 Fixed Value: 4 elements  
 Prohibited: 3 elements

**Structures**

This structure refers to these other structures:

* [Plan-Net Location (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location)](StructureDefinition-plannet-Location.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

* The element Extension.extension.value[x] is sliced based on the value of type:$this

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-practitioner-qualification-definitions.html#Extension "An extension to add status and whereValid elements to a practitioner’s qualifications.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Practitioner Qualification |
| ... [extension](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension) |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:status](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status "Slice status") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Status |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "status" |
| .... [Slices for value[x]](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.value[x]) |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Open by type:$this |
| .... [valueCode](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.valueCode) |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) Fixed Value: active |
| ... [extension:whereValid](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid "Slice whereValid") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Where the qualification is valid |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "whereValid" |
| .... [Slices for value[x]](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.value[x]) |  | 1..1 |  | Value of extension Slice: Unordered, Open by type:$this |
| ..... valueCodeableConcept |  |  | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |  |
| ..... valueReference |  |  | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Plan-Net Location](StructureDefinition-plannet-Location.html)) |  |
| .... [valueCodeableConcept](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.valueCodeableConcept) |  | 0..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-practitioner-qualification-definitions.html#Extension "An extension to add status and whereValid elements to a practitioner’s qualifications.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Practitioner Qualification |
| ... [id](StructureDefinition-practitioner-qualification-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension "An Extension") |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:status](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status "Slice status: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Status |
| .... [id](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "status" |
| .... [Slices for value[x]](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Closed by type:$this |
| ..... [value[x]:valueCode](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.value[x]:valueCode "Slice valueCode: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) Fixed Value: active |
| ... [extension:whereValid](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid "Slice whereValid: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Where the qualification is valid |
| .... [id](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "whereValid" |
| .... [Slices for value[x]](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Slice: Unordered, Closed by type:$this |
| ..... [value[x]:valueCodeableConcept](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.value[x]:valueCodeableConcept "Slice valueCodeableConcept: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 4 elements (1 nested mandatory element)  
 Must-Support: 2 elements  
 Fixed Value: 4 elements  
 Prohibited: 3 elements

**Structures**

This structure refers to these other structures:

* [Plan-Net Location (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location)](StructureDefinition-plannet-Location.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

* The element Extension.extension.value[x] is sliced based on the value of type:$this

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-practitioner-qualification-definitions.html#Extension "An extension to add status and whereValid elements to a practitioner’s qualifications.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Practitioner Qualification |
| ... [extension](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension) |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:status](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status "Slice status") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Status |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "status" |
| .... [Slices for value[x]](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.value[x]) |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Open by type:$this |
| .... [valueCode](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.valueCode) |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) Fixed Value: active |
| ... [extension:whereValid](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid "Slice whereValid") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Where the qualification is valid |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "whereValid" |
| .... [Slices for value[x]](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.value[x]) |  | 1..1 |  | Value of extension Slice: Unordered, Open by type:$this |
| ..... valueCodeableConcept |  |  | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |  |
| ..... valueReference |  |  | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Plan-Net Location](StructureDefinition-plannet-Location.html)) |  |
| .... [valueCodeableConcept](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.valueCodeableConcept) |  | 0..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-practitioner-qualification-definitions.html#Extension "An extension to add status and whereValid elements to a practitioner’s qualifications.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Practitioner Qualification |
| ... [id](StructureDefinition-practitioner-qualification-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension "An Extension") |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:status](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status "Slice status: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Status |
| .... [id](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "status" |
| .... [Slices for value[x]](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Closed by type:$this |
| ..... [value[x]:valueCode](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:status.value[x]:valueCode "Slice valueCode: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) Fixed Value: active |
| ... [extension:whereValid](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid "Slice whereValid: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Where the qualification is valid |
| .... [id](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "whereValid" |
| .... [Slices for value[x]](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Slice: Unordered, Closed by type:$this |
| ..... [value[x]:valueCodeableConcept](StructureDefinition-practitioner-qualification-definitions.html#Extension.extension:whereValid.value[x]:valueCodeableConcept "Slice valueCodeableConcept: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [url](StructureDefinition-practitioner-qualification-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-practitioner-qualification.csv), [Excel](StructureDefinition-practitioner-qualification.xlsx), [Schematron](StructureDefinition-practitioner-qualification.sch)

#### Terminology Bindings

|  |  |  |
| --- | --- | --- |
| **Path** | **Conformance** | **ValueSet / Code** |
| Extension.extension:status.value[x]:valueCode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: active |
| Extension.extension:whereValid.value[x]:valueCodeableConcept | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [UspsTwoLetterAlphabeticCodes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) |