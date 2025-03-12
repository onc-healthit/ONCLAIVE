# Extension: Endpoint Usecase

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Endpoint Usecase**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-endpoint-usecase-definitions.html)
* [Mappings](StructureDefinition-endpoint-usecase-mappings.html)

## Extension: Endpoint Usecase

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: EndpointUsecase |

EndpointUseCase is an enumeration of the specific use cases (service descriptions) supported by the endpoint

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)
* Examples for this Extension: [Endpoint for Acme of CT Portal](Endpoint-AcmeOfCTPortalEndpoint.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 3 elements (1 nested mandatory element)  
 Must-Support: 2 elements  
 Fixed Value: 3 elements  
 Prohibited: 3 elements

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-endpoint-usecase-definitions.html#Extension "EndpointUseCase is an enumeration of the specific use cases (service descriptions) supported by the endpoint") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Endpoint Usecase |
| ... [extension](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension) |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:type](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type "Slice type") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | An indication of the type of services supported by the endpoint |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "type" |
| .... [value[x]](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Endpoint Usecases VS](ValueSet-EndpointUsecaseVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [extension:standard](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard "Slice standard") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | A URI to a published standard describing the services supported by the endpoint (e.g. an HL7 implementation guide) |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "standard" |
| .... [value[x]](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.value[x]) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | Value of extension |
| ... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-endpoint-usecase-definitions.html#Extension "EndpointUseCase is an enumeration of the specific use cases (service descriptions) supported by the endpoint") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Endpoint Usecase |
| ... [id](StructureDefinition-endpoint-usecase-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension "An Extension") |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:type](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type "Slice type: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | An indication of the type of services supported by the endpoint |
| .... [id](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "type" |
| .... [value[x]](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Endpoint Usecases VS](ValueSet-EndpointUsecaseVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [extension:standard](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard "Slice standard: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | A URI to a published standard describing the services supported by the endpoint (e.g. an HL7 implementation guide) |
| .... [id](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "standard" |
| .... [value[x]](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | Value of extension |
| ... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 3 elements (1 nested mandatory element)  
 Must-Support: 2 elements  
 Fixed Value: 3 elements  
 Prohibited: 3 elements

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-endpoint-usecase-definitions.html#Extension "EndpointUseCase is an enumeration of the specific use cases (service descriptions) supported by the endpoint") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Endpoint Usecase |
| ... [extension](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension) |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:type](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type "Slice type") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | An indication of the type of services supported by the endpoint |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "type" |
| .... [value[x]](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Endpoint Usecases VS](ValueSet-EndpointUsecaseVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [extension:standard](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard "Slice standard") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | A URI to a published standard describing the services supported by the endpoint (e.g. an HL7 implementation guide) |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "standard" |
| .... [value[x]](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.value[x]) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | Value of extension |
| ... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-endpoint-usecase-definitions.html#Extension "EndpointUseCase is an enumeration of the specific use cases (service descriptions) supported by the endpoint") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Endpoint Usecase |
| ... [id](StructureDefinition-endpoint-usecase-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension "An Extension") |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:type](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type "Slice type: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | An indication of the type of services supported by the endpoint |
| .... [id](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "type" |
| .... [value[x]](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:type.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Endpoint Usecases VS](ValueSet-EndpointUsecaseVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [extension:standard](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard "Slice standard: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | A URI to a published standard describing the services supported by the endpoint (e.g. an HL7 implementation guide) |
| .... [id](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "standard" |
| .... [value[x]](StructureDefinition-endpoint-usecase-definitions.html#Extension.extension:standard.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | Value of extension |
| ... [url](StructureDefinition-endpoint-usecase-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-endpoint-usecase.csv), [Excel](StructureDefinition-endpoint-usecase.xlsx), [Schematron](StructureDefinition-endpoint-usecase.sch)

#### Terminology Bindings

|  |  |  |
| --- | --- | --- |
| **Path** | **Conformance** | **ValueSet** |
| Extension.extension:type.value[x] | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [EndpointUsecaseVS](ValueSet-EndpointUsecaseVS.html) |