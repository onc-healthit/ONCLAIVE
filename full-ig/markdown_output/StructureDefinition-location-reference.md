xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Location Reference - FHIR v4.0.1

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
* **Location Reference**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-location-reference-definitions.html)
* [Mappings](StructureDefinition-location-reference-mappings.html)

## Extension: Location Reference

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: LocationReference |

A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net Network](StructureDefinition-plannet-Network.html)
* Examples for this Extension: [ACME CT Premium Preferred Provider Network](Organization-AcmeofCTPremNet.html)

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

**Structures**

This structure refers to these other structures:

* [Plan-Net Location (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location)](StructureDefinition-plannet-Location.html)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-location-reference-definitions.html#Extension "A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Location Reference |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-location-reference-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference" |
| ... [value[x]](StructureDefinition-location-reference-definitions.html#Extension.value[x]) | S | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Location](StructureDefinition-plannet-Location.html)) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-location-reference-definitions.html#Extension "A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Location Reference |
| ... [id](StructureDefinition-location-reference-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-location-reference-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-location-reference-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference" |
| ... [value[x]](StructureDefinition-location-reference-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") | S | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Location](StructureDefinition-plannet-Location.html)) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 1 element  
 Must-Support: 1 element  
 Fixed Value: 1 element  
 Prohibited: 1 element

**Structures**

This structure refers to these other structures:

* [Plan-Net Location (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location)](StructureDefinition-plannet-Location.html)

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-location-reference-definitions.html#Extension "A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Location Reference |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-location-reference-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference" |
| ... [value[x]](StructureDefinition-location-reference-definitions.html#Extension.value[x]) | S | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Location](StructureDefinition-plannet-Location.html)) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-location-reference-definitions.html#Extension "A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Location Reference |
| ... [id](StructureDefinition-location-reference-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-location-reference-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-location-reference-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference" |
| ... [value[x]](StructureDefinition-location-reference-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") | S | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Location](StructureDefinition-plannet-Location.html)) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-location-reference.csv), [Excel](StructureDefinition-location-reference.xlsx), [Schematron](StructureDefinition-location-reference.sch)

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)