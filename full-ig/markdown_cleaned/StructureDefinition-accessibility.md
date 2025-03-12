# Extension: Accessibility

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Accessibility**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-accessibility-definitions.html)
* [Mappings](StructureDefinition-accessibility-mappings.html)

## Extension: Accessibility

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: Accessibility |

An extension to describe accessibility options offered by a practitioner or at a location.

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net Location](StructureDefinition-plannet-Location.html)
* Examples for this Extension: [Cancer Clinic](Location-CancerClinicLoc.html), [OrgA CT Location 1](Location-HansSoloClinic.html), [Hartford Hospital Location 1](Location-HospLoc1.html), [Hartford Hospital Location 2](Location-HospLoc2.html), [OrgA CT Location 1](Location-PharmLoc1.html), [OrgA CT Location 2](Location-PharmLoc2.html), [OrgA MA Location 1](Location-PharmLoc3.html), [OrgA MA Location 2](Location-PharmLoc4.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 1 element  
 Fixed Value: 1 element  
 Prohibited: 1 element

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-accessibility-definitions.html#Extension "An extension to describe accessibility options offered by a practitioner or at a location.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Accessibility |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-accessibility-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility" |
| ... [value[x]](StructureDefinition-accessibility-definitions.html#Extension.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Accessibility VS](ValueSet-AccessibilityVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-accessibility-definitions.html#Extension "An extension to describe accessibility options offered by a practitioner or at a location.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Accessibility |
| ... [id](StructureDefinition-accessibility-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-accessibility-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-accessibility-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility" |
| ... [value[x]](StructureDefinition-accessibility-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Accessibility VS](ValueSet-AccessibilityVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 1 element  
 Fixed Value: 1 element  
 Prohibited: 1 element

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-accessibility-definitions.html#Extension "An extension to describe accessibility options offered by a practitioner or at a location.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Accessibility |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-accessibility-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility" |
| ... [value[x]](StructureDefinition-accessibility-definitions.html#Extension.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Accessibility VS](ValueSet-AccessibilityVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-accessibility-definitions.html#Extension "An extension to describe accessibility options offered by a practitioner or at a location.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Accessibility |
| ... [id](StructureDefinition-accessibility-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-accessibility-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-accessibility-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility" |
| ... [value[x]](StructureDefinition-accessibility-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Accessibility VS](ValueSet-AccessibilityVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-accessibility.csv), [Excel](StructureDefinition-accessibility.xlsx), [Schematron](StructureDefinition-accessibility.sch)

#### Terminology Bindings

|  |  |  |
| --- | --- | --- |
| **Path** | **Conformance** | **ValueSet** |
| Extension.value[x] | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [AccessibilityVS](ValueSet-AccessibilityVS.html) |