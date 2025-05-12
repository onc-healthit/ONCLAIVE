xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Practitioner Qualification - Definitions - FHIR v4.0.1

[![Visit the HL7 website](assets/images/hl7-logo-header.png)](http://hl7.org)

[![Visit the FHIR website](assets/images/fhir-logo-www.png)](http://hl7.org/fhir)

[![Search FHIR](assets/images/search.png)](searchform.html)

[![Visit the Da Vinci website](assets/images/da-vinci_logo.jpg)](http://hl7.org/about/davinci)

DaVinci PDEX Plan Net

1.1.0 - STU 1.1
US

[FHIR](http://hl7.org/fhir/R4/index.html)

* [Home](index.html)
* [Implementation](#)
  + [Implementation](implementation.html)
  + [Representing Provider Directories in Plan Net](implementation.html#Representing)
* [FHIR Artifacts](#)
  + [Profiles](artifacts.html#3)
  + [Extensions](artifacts.html#4)
  + [Search Parameters](artifacts.html#2)
  + [Terminology](artifacts.html#5)
  + [Capability Statement](artifacts.html#1)
* [Examples](artifacts.html#7)
* [Downloads](downloads.html)
* [Change History](ChangeHistory.html)
* [History](http://www.hl7.org/fhir/us/davinci-pdex-plan-net/history.cfml)

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Practitioner Qualification**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-practitioner-qualification.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-practitioner-qualification-mappings.html)

## Extension: PractitionerQualification - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the practitioner-qualification extension.

|  |  |
| --- | --- |
| 1. **Extension** | |
| Definition | An extension to add status and whereValid elements to a practitioner’s qualifications. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 2. **Extension.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 3. **Extension.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 4. **Extension.extension:status** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | status |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 5. **Extension.extension:status.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 6. **Extension.extension:status.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 7. **Extension.extension:status.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | status |
| 8. **Extension.extension:status.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.value[x]. The slices are unordered and Closed, and can be differentiated using the following discriminators:  * type @ $this |
| 9. **Extension.extension:status.value[x]:valueCode** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | valueCode |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Qualification Status VS](ValueSet-QualificationStatusVS.html) |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Fixed Value | active |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 10. **Extension.extension:whereValid** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | whereValid |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 11. **Extension.extension:whereValid.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 12. **Extension.extension:whereValid.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 13. **Extension.extension:whereValid.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | whereValid |
| 14. **Extension.extension:whereValid.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.value[x]. The slices are unordered and Closed, and can be differentiated using the following discriminators:  * type @ $this |
| 15. **Extension.extension:whereValid.value[x]:valueCodeableConcept** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | valueCodeableConcept |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 16. **Extension.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification |
| 17. **Extension.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | Choice of: [base64Binary](http://hl7.org/fhir/R4/datatypes.html#base64Binary), [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean), [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical), [code](http://hl7.org/fhir/R4/datatypes.html#code), [date](http://hl7.org/fhir/R4/datatypes.html#date), [dateTime](http://hl7.org/fhir/R4/datatypes.html#dateTime), [decimal](http://hl7.org/fhir/R4/datatypes.html#decimal), [id](http://hl7.org/fhir/R4/datatypes.html#id), [instant](http://hl7.org/fhir/R4/datatypes.html#instant), [integer](http://hl7.org/fhir/R4/datatypes.html#integer), [markdown](http://hl7.org/fhir/R4/datatypes.html#markdown), [oid](http://hl7.org/fhir/R4/datatypes.html#oid), [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt), [string](http://hl7.org/fhir/R4/datatypes.html#string), [time](http://hl7.org/fhir/R4/datatypes.html#time), [unsignedInt](http://hl7.org/fhir/R4/datatypes.html#unsignedInt), [uri](http://hl7.org/fhir/R4/datatypes.html#uri), [url](http://hl7.org/fhir/R4/datatypes.html#url), [uuid](http://hl7.org/fhir/R4/datatypes.html#uuid), [Address](http://hl7.org/fhir/R4/datatypes.html#Address), [Age](http://hl7.org/fhir/R4/datatypes.html#Age), [Annotation](http://hl7.org/fhir/R4/datatypes.html#Annotation), [Attachment](http://hl7.org/fhir/R4/datatypes.html#Attachment), [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept), [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding), [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint), [Count](http://hl7.org/fhir/R4/datatypes.html#Count), [Distance](http://hl7.org/fhir/R4/datatypes.html#Distance), [Duration](http://hl7.org/fhir/R4/datatypes.html#Duration), [HumanName](http://hl7.org/fhir/R4/datatypes.html#HumanName), [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier), [Money](http://hl7.org/fhir/R4/datatypes.html#Money), [Period](http://hl7.org/fhir/R4/datatypes.html#Period), [Quantity](http://hl7.org/fhir/R4/datatypes.html#Quantity), [Range](http://hl7.org/fhir/R4/datatypes.html#Range), [Ratio](http://hl7.org/fhir/R4/datatypes.html#Ratio), [Reference](http://hl7.org/fhir/R4/references.html#Reference), [SampledData](http://hl7.org/fhir/R4/datatypes.html#SampledData), [Signature](http://hl7.org/fhir/R4/datatypes.html#Signature), [Timing](http://hl7.org/fhir/R4/datatypes.html#Timing), [ContactDetail](http://hl7.org/fhir/R4/metadatatypes.html#ContactDetail), [Contributor](http://hl7.org/fhir/R4/metadatatypes.html#Contributor), [DataRequirement](http://hl7.org/fhir/R4/metadatatypes.html#DataRequirement), [Expression](http://hl7.org/fhir/R4/datatypes.html#Expression), [ParameterDefinition](http://hl7.org/fhir/R4/metadatatypes.html#ParameterDefinition), [RelatedArtifact](http://hl7.org/fhir/R4/metadatatypes.html#RelatedArtifact), [TriggerDefinition](http://hl7.org/fhir/R4/metadatatypes.html#TriggerDefinition), [UsageContext](http://hl7.org/fhir/R4/metadatatypes.html#UsageContext), [Dosage](http://hl7.org/fhir/R4/datatypes.html#Dosage), [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)