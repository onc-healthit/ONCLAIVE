# Extension: ContactPointAvailableTime - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Contactpoint Availabletime**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-contactpoint-availabletime.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-contactpoint-availabletime-mappings.html)

## Extension: ContactPointAvailableTime - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the contactpoint-availabletime extension.

|  |  |
| --- | --- |
| 1. **Extension** | |
| Definition | An extension representing the days and times a contact point is available |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 2. **Extension.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 3. **Extension.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 4. **Extension.extension:daysOfWeek** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | daysOfWeek |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 5. **Extension.extension:daysOfWeek.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 6. **Extension.extension:daysOfWeek.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 7. **Extension.extension:daysOfWeek.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | daysOfWeek |
| 8. **Extension.extension:daysOfWeek.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.value[x]. The slices are unordered and Closed, and can be differentiated using the following discriminators:  * type @ $this |
| 9. **Extension.extension:daysOfWeek.value[x]:valueCode** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | valueCode |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html) |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 10. **Extension.extension:allDay** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | allDay |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 11. **Extension.extension:allDay.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 12. **Extension.extension:allDay.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 13. **Extension.extension:allDay.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | allDay |
| 14. **Extension.extension:allDay.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 15. **Extension.extension:availableStartTime** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | availableStartTime |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 16. **Extension.extension:availableStartTime.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 17. **Extension.extension:availableStartTime.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 18. **Extension.extension:availableStartTime.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | availableStartTime |
| 19. **Extension.extension:availableStartTime.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [time](http://hl7.org/fhir/R4/datatypes.html#time) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 20. **Extension.extension:availableEndTime** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | availableEndTime |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 21. **Extension.extension:availableEndTime.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 22. **Extension.extension:availableEndTime.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 23. **Extension.extension:availableEndTime.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | availableEndTime |
| 24. **Extension.extension:availableEndTime.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [time](http://hl7.org/fhir/R4/datatypes.html#time) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 25. **Extension.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime |
| 26. **Extension.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | Choice of: [base64Binary](http://hl7.org/fhir/R4/datatypes.html#base64Binary), [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean), [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical), [code](http://hl7.org/fhir/R4/datatypes.html#code), [date](http://hl7.org/fhir/R4/datatypes.html#date), [dateTime](http://hl7.org/fhir/R4/datatypes.html#dateTime), [decimal](http://hl7.org/fhir/R4/datatypes.html#decimal), [id](http://hl7.org/fhir/R4/datatypes.html#id), [instant](http://hl7.org/fhir/R4/datatypes.html#instant), [integer](http://hl7.org/fhir/R4/datatypes.html#integer), [markdown](http://hl7.org/fhir/R4/datatypes.html#markdown), [oid](http://hl7.org/fhir/R4/datatypes.html#oid), [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt), [string](http://hl7.org/fhir/R4/datatypes.html#string), [time](http://hl7.org/fhir/R4/datatypes.html#time), [unsignedInt](http://hl7.org/fhir/R4/datatypes.html#unsignedInt), [uri](http://hl7.org/fhir/R4/datatypes.html#uri), [url](http://hl7.org/fhir/R4/datatypes.html#url), [uuid](http://hl7.org/fhir/R4/datatypes.html#uuid), [Address](http://hl7.org/fhir/R4/datatypes.html#Address), [Age](http://hl7.org/fhir/R4/datatypes.html#Age), [Annotation](http://hl7.org/fhir/R4/datatypes.html#Annotation), [Attachment](http://hl7.org/fhir/R4/datatypes.html#Attachment), [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept), [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding), [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint), [Count](http://hl7.org/fhir/R4/datatypes.html#Count), [Distance](http://hl7.org/fhir/R4/datatypes.html#Distance), [Duration](http://hl7.org/fhir/R4/datatypes.html#Duration), [HumanName](http://hl7.org/fhir/R4/datatypes.html#HumanName), [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier), [Money](http://hl7.org/fhir/R4/datatypes.html#Money), [Period](http://hl7.org/fhir/R4/datatypes.html#Period), [Quantity](http://hl7.org/fhir/R4/datatypes.html#Quantity), [Range](http://hl7.org/fhir/R4/datatypes.html#Range), [Ratio](http://hl7.org/fhir/R4/datatypes.html#Ratio), [Reference](http://hl7.org/fhir/R4/references.html#Reference), [SampledData](http://hl7.org/fhir/R4/datatypes.html#SampledData), [Signature](http://hl7.org/fhir/R4/datatypes.html#Signature), [Timing](http://hl7.org/fhir/R4/datatypes.html#Timing), [ContactDetail](http://hl7.org/fhir/R4/metadatatypes.html#ContactDetail), [Contributor](http://hl7.org/fhir/R4/metadatatypes.html#Contributor), [DataRequirement](http://hl7.org/fhir/R4/metadatatypes.html#DataRequirement), [Expression](http://hl7.org/fhir/R4/datatypes.html#Expression), [ParameterDefinition](http://hl7.org/fhir/R4/metadatatypes.html#ParameterDefinition), [RelatedArtifact](http://hl7.org/fhir/R4/metadatatypes.html#RelatedArtifact), [TriggerDefinition](http://hl7.org/fhir/R4/metadatatypes.html#TriggerDefinition), [UsageContext](http://hl7.org/fhir/R4/metadatatypes.html#UsageContext), [Dosage](http://hl7.org/fhir/R4/datatypes.html#Dosage), [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |