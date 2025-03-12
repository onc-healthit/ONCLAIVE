# Extension: Org Description

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Org Description**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-org-description-definitions.html)
* [Mappings](StructureDefinition-org-description-mappings.html)

## Extension: Org Description

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: OrgDescription |

An extension to provide a human-readable description of an organization.

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net Organization](StructureDefinition-plannet-Organization.html)
* Examples for this Extension: [Acme of CT](Organization-Acme.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 1 element  
 Must-Support: 1 element  
 Fixed Value: 1 element  
 Prohibited: 1 element

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-org-description-definitions.html#Extension "An extension to provide a human-readable description of an organization.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Org Description |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-org-description-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description" |
| ... [value[x]](StructureDefinition-org-description-definitions.html#Extension.value[x]) | S | 1..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-org-description-definitions.html#Extension "An extension to provide a human-readable description of an organization.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Org Description |
| ... [id](StructureDefinition-org-description-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-org-description-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-org-description-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description" |
| ... [value[x]](StructureDefinition-org-description-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") | S | 1..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 1 element  
 Must-Support: 1 element  
 Fixed Value: 1 element  
 Prohibited: 1 element

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-org-description-definitions.html#Extension "An extension to provide a human-readable description of an organization.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Org Description |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-org-description-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description" |
| ... [value[x]](StructureDefinition-org-description-definitions.html#Extension.value[x]) | S | 1..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-org-description-definitions.html#Extension "An extension to provide a human-readable description of an organization.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Org Description |
| ... [id](StructureDefinition-org-description-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-org-description-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-org-description-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description" |
| ... [value[x]](StructureDefinition-org-description-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") | S | 1..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-org-description.csv), [Excel](StructureDefinition-org-description.xlsx), [Schematron](StructureDefinition-org-description.sch)