# Extension: Qualification - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Qualification**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-qualification.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-qualification-mappings.html)

## Extension: Qualification - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the qualification extension.

|  |  |
| --- | --- |
| 1. **Extension** | |
| Definition | An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 2. **Extension.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 3. **Extension.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 2..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 4. **Extension.extension:identifier** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | identifier |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 5. **Extension.extension:identifier.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 6. **Extension.extension:identifier.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 7. **Extension.extension:identifier.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | identifier |
| 8. **Extension.extension:identifier.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 9. **Extension.extension:code** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | code |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 10. **Extension.extension:code.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 11. **Extension.extension:code.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 12. **Extension.extension:code.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | code |
| 13. **Extension.extension:code.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html); other codes may be used where these codes are not suitable |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 14. **Extension.extension:issuer** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | issuer |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 15. **Extension.extension:issuer.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 16. **Extension.extension:issuer.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 17. **Extension.extension:issuer.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | issuer |
| 18. **Extension.extension:issuer.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization")) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 19. **Extension.extension:status** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | status |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 20. **Extension.extension:status.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 21. **Extension.extension:status.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 22. **Extension.extension:status.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | status |
| 23. **Extension.extension:status.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.value[x]. The slices are unordered and Closed, and can be differentiated using the following discriminators:  * type @ $this |
| 24. **Extension.extension:status.value[x]:valueCode** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | valueCode |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Qualification Status VS](ValueSet-QualificationStatusVS.html) |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Fixed Value | active |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 25. **Extension.extension:period** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | period |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 26. **Extension.extension:period.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 27. **Extension.extension:period.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 28. **Extension.extension:period.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | period |
| 29. **Extension.extension:period.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 30. **Extension.extension:whereValid** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | whereValid |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 31. **Extension.extension:whereValid.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 32. **Extension.extension:whereValid.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 33. **Extension.extension:whereValid.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | whereValid |
| 34. **Extension.extension:whereValid.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | Choice of: [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept), [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetLocation](StructureDefinition-plannet-Location.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location")) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 35. **Extension.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/qualification |
| 36. **Extension.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | Choice of: [base64Binary](http://hl7.org/fhir/R4/datatypes.html#base64Binary), [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean), [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical), [code](http://hl7.org/fhir/R4/datatypes.html#code), [date](http://hl7.org/fhir/R4/datatypes.html#date), [dateTime](http://hl7.org/fhir/R4/datatypes.html#dateTime), [decimal](http://hl7.org/fhir/R4/datatypes.html#decimal), [id](http://hl7.org/fhir/R4/datatypes.html#id), [instant](http://hl7.org/fhir/R4/datatypes.html#instant), [integer](http://hl7.org/fhir/R4/datatypes.html#integer), [markdown](http://hl7.org/fhir/R4/datatypes.html#markdown), [oid](http://hl7.org/fhir/R4/datatypes.html#oid), [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt), [string](http://hl7.org/fhir/R4/datatypes.html#string), [time](http://hl7.org/fhir/R4/datatypes.html#time), [unsignedInt](http://hl7.org/fhir/R4/datatypes.html#unsignedInt), [uri](http://hl7.org/fhir/R4/datatypes.html#uri), [url](http://hl7.org/fhir/R4/datatypes.html#url), [uuid](http://hl7.org/fhir/R4/datatypes.html#uuid), [Address](http://hl7.org/fhir/R4/datatypes.html#Address), [Age](http://hl7.org/fhir/R4/datatypes.html#Age), [Annotation](http://hl7.org/fhir/R4/datatypes.html#Annotation), [Attachment](http://hl7.org/fhir/R4/datatypes.html#Attachment), [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept), [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding), [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint), [Count](http://hl7.org/fhir/R4/datatypes.html#Count), [Distance](http://hl7.org/fhir/R4/datatypes.html#Distance), [Duration](http://hl7.org/fhir/R4/datatypes.html#Duration), [HumanName](http://hl7.org/fhir/R4/datatypes.html#HumanName), [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier), [Money](http://hl7.org/fhir/R4/datatypes.html#Money), [Period](http://hl7.org/fhir/R4/datatypes.html#Period), [Quantity](http://hl7.org/fhir/R4/datatypes.html#Quantity), [Range](http://hl7.org/fhir/R4/datatypes.html#Range), [Ratio](http://hl7.org/fhir/R4/datatypes.html#Ratio), [Reference](http://hl7.org/fhir/R4/references.html#Reference), [SampledData](http://hl7.org/fhir/R4/datatypes.html#SampledData), [Signature](http://hl7.org/fhir/R4/datatypes.html#Signature), [Timing](http://hl7.org/fhir/R4/datatypes.html#Timing), [ContactDetail](http://hl7.org/fhir/R4/metadatatypes.html#ContactDetail), [Contributor](http://hl7.org/fhir/R4/metadatatypes.html#Contributor), [DataRequirement](http://hl7.org/fhir/R4/metadatatypes.html#DataRequirement), [Expression](http://hl7.org/fhir/R4/datatypes.html#Expression), [ParameterDefinition](http://hl7.org/fhir/R4/metadatatypes.html#ParameterDefinition), [RelatedArtifact](http://hl7.org/fhir/R4/metadatatypes.html#RelatedArtifact), [TriggerDefinition](http://hl7.org/fhir/R4/metadatatypes.html#TriggerDefinition), [UsageContext](http://hl7.org/fhir/R4/metadatatypes.html#UsageContext), [Dosage](http://hl7.org/fhir/R4/datatypes.html#Dosage), [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |