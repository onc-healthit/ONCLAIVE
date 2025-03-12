# Extension: Delivery Method

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Delivery Method**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-delivery-method-definitions.html)
* [Mappings](StructureDefinition-delivery-method-mappings.html)

## Extension: Delivery Method

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: DeliveryMethod |

An extension describing the service delivery method. If service delivery is virtual, one or more delivery modalities should be specified.

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)
* Examples for this Extension: [HealthcareService/BurrClinicServices](HealthcareService-BurrClinicServices.html), [HealthcareService/CancerClinicService](HealthcareService-CancerClinicService.html), [HealthcareService/HamiltonClinicServices](HealthcareService-HamiltonClinicServices.html), [HealthcareService/HansSoloService](HealthcareService-HansSoloService.html), [HealthcareService/HartfordOrthopedicServices](HealthcareService-HartfordOrthopedicServices.html), [HealthcareService/HospERService](HealthcareService-HospERService.html), [Compounding Pharmacy by OrgA](HealthcareService-PharmChainCompService.html), [Mail Order Pharmacy by OrgA](HealthcareService-PharmChainMailService.html), [Pharmacy by PharmChain](HealthcareService-PharmChainRetailService.html), [HealthcareService/VirtualCounselService](HealthcareService-VirtualCounselService.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 3 elements (1 nested mandatory element)  
 Must-Support: 1 element  
 Fixed Value: 3 elements  
 Prohibited: 3 elements

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-delivery-method-definitions.html#Extension "An extension describing the service delivery method.   If service delivery is virtual, one or more delivery modalities should be specified.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Delivery Method |
| ... [extension](StructureDefinition-delivery-method-definitions.html#Extension.extension) |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:type](StructureDefinition-delivery-method-definitions.html#Extension.extension:type "Slice type") |  | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Physical or Virtual Service Delivery |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "type" |
| .... [value[x]](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Delivery Methods VS](ValueSet-DeliveryMethodVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:virtualModalities](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities "Slice virtualModalities") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Modalities of Virtual Delivery |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "virtualModalities" |
| .... [value[x]](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Virtual Modalities VS](ValueSet-VirtualModalitiesVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [url](StructureDefinition-delivery-method-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-delivery-method-definitions.html#Extension "An extension describing the service delivery method.   If service delivery is virtual, one or more delivery modalities should be specified.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Delivery Method |
| ... [id](StructureDefinition-delivery-method-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-delivery-method-definitions.html#Extension.extension "An Extension") |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:type](StructureDefinition-delivery-method-definitions.html#Extension.extension:type "Slice type: An Extension") |  | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Physical or Virtual Service Delivery |
| .... [id](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "type" |
| .... [value[x]](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Delivery Methods VS](ValueSet-DeliveryMethodVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:virtualModalities](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities "Slice virtualModalities: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Modalities of Virtual Delivery |
| .... [id](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "virtualModalities" |
| .... [value[x]](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Virtual Modalities VS](ValueSet-VirtualModalitiesVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [url](StructureDefinition-delivery-method-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 3 elements (1 nested mandatory element)  
 Must-Support: 1 element  
 Fixed Value: 3 elements  
 Prohibited: 3 elements

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-delivery-method-definitions.html#Extension "An extension describing the service delivery method.   If service delivery is virtual, one or more delivery modalities should be specified.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Delivery Method |
| ... [extension](StructureDefinition-delivery-method-definitions.html#Extension.extension) |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:type](StructureDefinition-delivery-method-definitions.html#Extension.extension:type "Slice type") |  | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Physical or Virtual Service Delivery |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "type" |
| .... [value[x]](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Delivery Methods VS](ValueSet-DeliveryMethodVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:virtualModalities](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities "Slice virtualModalities") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Modalities of Virtual Delivery |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "virtualModalities" |
| .... [value[x]](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Virtual Modalities VS](ValueSet-VirtualModalitiesVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [url](StructureDefinition-delivery-method-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-delivery-method-definitions.html#Extension "An extension describing the service delivery method.   If service delivery is virtual, one or more delivery modalities should be specified.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Delivery Method |
| ... [id](StructureDefinition-delivery-method-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-delivery-method-definitions.html#Extension.extension "An Extension") |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:type](StructureDefinition-delivery-method-definitions.html#Extension.extension:type "Slice type: An Extension") |  | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Physical or Virtual Service Delivery |
| .... [id](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "type" |
| .... [value[x]](StructureDefinition-delivery-method-definitions.html#Extension.extension:type.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Delivery Methods VS](ValueSet-DeliveryMethodVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:virtualModalities](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities "Slice virtualModalities: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Modalities of Virtual Delivery |
| .... [id](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "virtualModalities" |
| .... [value[x]](StructureDefinition-delivery-method-definitions.html#Extension.extension:virtualModalities.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Virtual Modalities VS](ValueSet-VirtualModalitiesVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [url](StructureDefinition-delivery-method-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/delivery-method" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-delivery-method.csv), [Excel](StructureDefinition-delivery-method.xlsx), [Schematron](StructureDefinition-delivery-method.sch)

#### Terminology Bindings

|  |  |  |
| --- | --- | --- |
| **Path** | **Conformance** | **ValueSet** |
| Extension.extension:type.value[x] | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [DeliveryMethodVS](ValueSet-DeliveryMethodVS.html) |
| Extension.extension:virtualModalities.value[x] | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [VirtualModalitiesVS](ValueSet-VirtualModalitiesVS.html) |