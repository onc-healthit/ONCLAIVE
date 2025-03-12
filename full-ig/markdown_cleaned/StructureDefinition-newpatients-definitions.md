# Extension: NewPatients - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **New Patients**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-newpatients.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-newpatients-mappings.html)

## Extension: NewPatients - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the newpatients extension.

|  |  |
| --- | --- |
| 1. **Extension** | |
| Definition | New Patients indicates whether new patients are being accepted in general, or from a specific network.  This extension is included in the PractitionerRole, HealthcareService, and Location profiles.  This provides needed flexibility for specifying whether a provider accepts new patients by location and network. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) **new-patients-characteristics**: If no new patients are accepted, no characteristics are allowed (: extension('acceptingPatients').valueCodeableConcept.coding.exists(code = 'no') implies extension('characteristics').empty()) |
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
| 4. **Extension.extension:acceptingPatients** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | acceptingPatients |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 5. **Extension.extension:acceptingPatients.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 6. **Extension.extension:acceptingPatients.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 7. **Extension.extension:acceptingPatients.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | acceptingPatients |
| 8. **Extension.extension:acceptingPatients.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Accepting Patients Codes VS](ValueSet-AcceptingPatientsVS.html) |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 9. **Extension.extension:fromNetwork** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | fromNetwork |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 10. **Extension.extension:fromNetwork.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 11. **Extension.extension:fromNetwork.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 12. **Extension.extension:fromNetwork.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | fromNetwork |
| 13. **Extension.extension:fromNetwork.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetNetwork](StructureDefinition-plannet-Network.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network")) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 14. **Extension.extension:characteristics** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | characteristics |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 15. **Extension.extension:characteristics.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 16. **Extension.extension:characteristics.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 17. **Extension.extension:characteristics.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | characteristics |
| 18. **Extension.extension:characteristics.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 19. **Extension.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients |
| 20. **Extension.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | Choice of: [base64Binary](http://hl7.org/fhir/R4/datatypes.html#base64Binary), [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean), [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical), [code](http://hl7.org/fhir/R4/datatypes.html#code), [date](http://hl7.org/fhir/R4/datatypes.html#date), [dateTime](http://hl7.org/fhir/R4/datatypes.html#dateTime), [decimal](http://hl7.org/fhir/R4/datatypes.html#decimal), [id](http://hl7.org/fhir/R4/datatypes.html#id), [instant](http://hl7.org/fhir/R4/datatypes.html#instant), [integer](http://hl7.org/fhir/R4/datatypes.html#integer), [markdown](http://hl7.org/fhir/R4/datatypes.html#markdown), [oid](http://hl7.org/fhir/R4/datatypes.html#oid), [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt), [string](http://hl7.org/fhir/R4/datatypes.html#string), [time](http://hl7.org/fhir/R4/datatypes.html#time), [unsignedInt](http://hl7.org/fhir/R4/datatypes.html#unsignedInt), [uri](http://hl7.org/fhir/R4/datatypes.html#uri), [url](http://hl7.org/fhir/R4/datatypes.html#url), [uuid](http://hl7.org/fhir/R4/datatypes.html#uuid), [Address](http://hl7.org/fhir/R4/datatypes.html#Address), [Age](http://hl7.org/fhir/R4/datatypes.html#Age), [Annotation](http://hl7.org/fhir/R4/datatypes.html#Annotation), [Attachment](http://hl7.org/fhir/R4/datatypes.html#Attachment), [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept), [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding), [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint), [Count](http://hl7.org/fhir/R4/datatypes.html#Count), [Distance](http://hl7.org/fhir/R4/datatypes.html#Distance), [Duration](http://hl7.org/fhir/R4/datatypes.html#Duration), [HumanName](http://hl7.org/fhir/R4/datatypes.html#HumanName), [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier), [Money](http://hl7.org/fhir/R4/datatypes.html#Money), [Period](http://hl7.org/fhir/R4/datatypes.html#Period), [Quantity](http://hl7.org/fhir/R4/datatypes.html#Quantity), [Range](http://hl7.org/fhir/R4/datatypes.html#Range), [Ratio](http://hl7.org/fhir/R4/datatypes.html#Ratio), [Reference](http://hl7.org/fhir/R4/references.html#Reference), [SampledData](http://hl7.org/fhir/R4/datatypes.html#SampledData), [Signature](http://hl7.org/fhir/R4/datatypes.html#Signature), [Timing](http://hl7.org/fhir/R4/datatypes.html#Timing), [ContactDetail](http://hl7.org/fhir/R4/metadatatypes.html#ContactDetail), [Contributor](http://hl7.org/fhir/R4/metadatatypes.html#Contributor), [DataRequirement](http://hl7.org/fhir/R4/metadatatypes.html#DataRequirement), [Expression](http://hl7.org/fhir/R4/datatypes.html#Expression), [ParameterDefinition](http://hl7.org/fhir/R4/metadatatypes.html#ParameterDefinition), [RelatedArtifact](http://hl7.org/fhir/R4/metadatatypes.html#RelatedArtifact), [TriggerDefinition](http://hl7.org/fhir/R4/metadatatypes.html#TriggerDefinition), [UsageContext](http://hl7.org/fhir/R4/metadatatypes.html#UsageContext), [Dosage](http://hl7.org/fhir/R4/datatypes.html#Dosage), [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |