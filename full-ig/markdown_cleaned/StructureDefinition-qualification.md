# Extension: Qualification

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Qualification**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-qualification-definitions.html)
* [Mappings](StructureDefinition-qualification-mappings.html)

## Extension: Qualification

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/qualification | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: Qualification |

An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances).

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net Organization](StructureDefinition-plannet-Organization.html), [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html), [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)
* Examples for this Extension: [PractitionerRole/HansSoloRole1](PractitionerRole-HansSoloRole1.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 5 elements (4 nested mandatory elements)  
 Must-Support: 6 elements  
 Fixed Value: 8 elements  
 Prohibited: 7 elements

**Structures**

This structure refers to these other structures:

* [Plan-Net Organization (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization)](StructureDefinition-plannet-Organization.html)
* [Plan-Net Location (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location)](StructureDefinition-plannet-Location.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

* The element Extension.extension.value[x] is sliced based on the value of type:$this

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-qualification-definitions.html#Extension "An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances).") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Qualification |
| ... [extension](StructureDefinition-qualification-definitions.html#Extension.extension) |  | 2..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:identifier](StructureDefinition-qualification-definitions.html#Extension.extension:identifier "Slice identifier") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "identifier" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.value[x]) |  | 1..1 | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | Value of extension |
| ... [extension:code](StructureDefinition-qualification-definitions.html#Extension.extension:code "Slice code") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:code.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "code" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:code.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [extension:issuer](StructureDefinition-qualification-definitions.html#Extension.extension:issuer "Slice issuer") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "issuer" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.value[x]) |  | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension |
| ... [extension:status](StructureDefinition-qualification-definitions.html#Extension.extension:status "Slice status") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:status.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "status" |
| .... [Slices for value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:status.value[x]) |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Open by type:$this |
| .... [valueCode](StructureDefinition-qualification-definitions.html#Extension.extension:status.valueCode) |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) Fixed Value: active |
| ... [extension:period](StructureDefinition-qualification-definitions.html#Extension.extension:period "Slice period") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:period.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "period" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:period.value[x]) |  | 1..1 | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) | Value of extension |
| ... [extension:whereValid](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid "Slice whereValid") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "whereValid" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.value[x]) |  | 1..1 |  | Value of extension Binding: [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... valueCodeableConcept |  |  | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |  |
| ..... valueReference |  |  | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Plan-Net Location](StructureDefinition-plannet-Location.html)) |  |
| ... [url](StructureDefinition-qualification-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/qualification" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-qualification-definitions.html#Extension "An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances).") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Qualification |
| ... [id](StructureDefinition-qualification-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension "An Extension") |  | 2..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:identifier](StructureDefinition-qualification-definitions.html#Extension.extension:identifier "Slice identifier: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "identifier" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | Value of extension |
| ... [extension:code](StructureDefinition-qualification-definitions.html#Extension.extension:code "Slice code: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:code.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:code.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:code.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "code" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:code.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [extension:issuer](StructureDefinition-qualification-definitions.html#Extension.extension:issuer "Slice issuer: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "issuer" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension |
| ... [extension:status](StructureDefinition-qualification-definitions.html#Extension.extension:status "Slice status: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:status.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:status.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:status.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "status" |
| .... [Slices for value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:status.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Closed by type:$this |
| ..... [value[x]:valueCode](StructureDefinition-qualification-definitions.html#Extension.extension:status.value[x]:valueCode "Slice valueCode: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) Fixed Value: active |
| ... [extension:period](StructureDefinition-qualification-definitions.html#Extension.extension:period "Slice period: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:period.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:period.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:period.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "period" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:period.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) | Value of extension |
| ... [extension:whereValid](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid "Slice whereValid: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "whereValid" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 |  | Value of extension Binding: [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... valueCodeableConcept |  |  | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |  |
| ..... valueReference |  |  | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Plan-Net Location](StructureDefinition-plannet-Location.html)) |  |
| ... [url](StructureDefinition-qualification-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/qualification" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 5 elements (4 nested mandatory elements)  
 Must-Support: 6 elements  
 Fixed Value: 8 elements  
 Prohibited: 7 elements

**Structures**

This structure refers to these other structures:

* [Plan-Net Organization (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization)](StructureDefinition-plannet-Organization.html)
* [Plan-Net Location (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location)](StructureDefinition-plannet-Location.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

* The element Extension.extension.value[x] is sliced based on the value of type:$this

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-qualification-definitions.html#Extension "An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances).") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Qualification |
| ... [extension](StructureDefinition-qualification-definitions.html#Extension.extension) |  | 2..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:identifier](StructureDefinition-qualification-definitions.html#Extension.extension:identifier "Slice identifier") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "identifier" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.value[x]) |  | 1..1 | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | Value of extension |
| ... [extension:code](StructureDefinition-qualification-definitions.html#Extension.extension:code "Slice code") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:code.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "code" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:code.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [extension:issuer](StructureDefinition-qualification-definitions.html#Extension.extension:issuer "Slice issuer") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "issuer" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.value[x]) |  | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension |
| ... [extension:status](StructureDefinition-qualification-definitions.html#Extension.extension:status "Slice status") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:status.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "status" |
| .... [Slices for value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:status.value[x]) |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Open by type:$this |
| .... [valueCode](StructureDefinition-qualification-definitions.html#Extension.extension:status.valueCode) |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) Fixed Value: active |
| ... [extension:period](StructureDefinition-qualification-definitions.html#Extension.extension:period "Slice period") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:period.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "period" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:period.value[x]) |  | 1..1 | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) | Value of extension |
| ... [extension:whereValid](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid "Slice whereValid") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "whereValid" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.value[x]) |  | 1..1 |  | Value of extension Binding: [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... valueCodeableConcept |  |  | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |  |
| ..... valueReference |  |  | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Plan-Net Location](StructureDefinition-plannet-Location.html)) |  |
| ... [url](StructureDefinition-qualification-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/qualification" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-qualification-definitions.html#Extension "An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances).") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Qualification |
| ... [id](StructureDefinition-qualification-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension "An Extension") |  | 2..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:identifier](StructureDefinition-qualification-definitions.html#Extension.extension:identifier "Slice identifier: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "identifier" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:identifier.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | Value of extension |
| ... [extension:code](StructureDefinition-qualification-definitions.html#Extension.extension:code "Slice code: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:code.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:code.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:code.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "code" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:code.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [extension:issuer](StructureDefinition-qualification-definitions.html#Extension.extension:issuer "Slice issuer: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "issuer" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:issuer.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension |
| ... [extension:status](StructureDefinition-qualification-definitions.html#Extension.extension:status "Slice status: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:status.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:status.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:status.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "status" |
| .... [Slices for value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:status.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Closed by type:$this |
| ..... [value[x]:valueCode](StructureDefinition-qualification-definitions.html#Extension.extension:status.value[x]:valueCode "Slice valueCode: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [Qualification Status VS](ValueSet-QualificationStatusVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) Fixed Value: active |
| ... [extension:period](StructureDefinition-qualification-definitions.html#Extension.extension:period "Slice period: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:period.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:period.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:period.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "period" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:period.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) | Value of extension |
| ... [extension:whereValid](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid "Slice whereValid: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "whereValid" |
| .... [value[x]](StructureDefinition-qualification-definitions.html#Extension.extension:whereValid.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 |  | Value of extension Binding: [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... valueCodeableConcept |  |  | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |  |
| ..... valueReference |  |  | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Plan-Net Location](StructureDefinition-plannet-Location.html)) |  |
| ... [url](StructureDefinition-qualification-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/qualification" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-qualification.csv), [Excel](StructureDefinition-qualification.xlsx), [Schematron](StructureDefinition-qualification.sch)

#### Terminology Bindings

|  |  |  |
| --- | --- | --- |
| **Path** | **Conformance** | **ValueSet / Code** |
| Extension.extension:code.value[x] | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [SpecialtyAndDegreeLicenseCertificateVS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html) |
| Extension.extension:status.value[x]:valueCode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: active |
| Extension.extension:whereValid.value[x] | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [UspsTwoLetterAlphabeticCodes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html) |