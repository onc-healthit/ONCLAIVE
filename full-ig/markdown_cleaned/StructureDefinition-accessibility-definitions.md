# Extension: Accessibility - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Accessibility**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-accessibility.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-accessibility-mappings.html)

## Extension: Accessibility - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the accessibility extension.

|  |  |
| --- | --- |
| 1. **Extension** | |
| Definition | An extension to describe accessibility options offered by a practitioner or at a location. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 2. **Extension.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 3. **Extension.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Extension.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 4. **Extension.url** | |
| Definition | Source of the definition for the extension code - a logical name or a URL. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | The definition may point directly to a computable or human-readable definition of the extensibility codes, or it may be a logical URI as declared in some other specification. The definition SHALL be a URI for the Structure Definition defining the extension. |
| Fixed Value | http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility |
| 5. **Extension.value[x]** | |
| Definition | Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Accessibility VS](ValueSet-AccessibilityVS.html); other codes may be used where these codes are not suitable |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [x] Note | See [Choice of Data Types](http://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x] |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |