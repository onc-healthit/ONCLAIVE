# Extension: New Patients

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **New Patients**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-newpatients-definitions.html)
* [Mappings](StructureDefinition-newpatients-mappings.html)

## Extension: New Patients

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: NewPatients |

New Patients indicates whether new patients are being accepted in general, or from a specific network.   
This extension is included in the PractitionerRole, HealthcareService, and Location profiles.  
This provides needed flexibility for specifying whether a provider accepts new patients by location and network.

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html), [Plan-Net Location](StructureDefinition-plannet-Location.html), [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)
* Examples for this Extension: [Pharmacy by PharmChain](HealthcareService-PharmChainRetailService.html), [OrgA CT Location 1](Location-HansSoloClinic.html), [OrgA CT Location 1](Location-PharmLoc1.html), [OrgA CT Location 2](Location-PharmLoc2.html), [OrgA MA Location 1](Location-PharmLoc3.html), [OrgA MA Location 2](Location-PharmLoc4.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 3 elements (2 nested mandatory elements)  
 Must-Support: 3 elements  
 Fixed Value: 4 elements  
 Prohibited: 4 elements

**Structures**

This structure refers to these other structures:

* [Plan-Net Network (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network)](StructureDefinition-plannet-Network.html)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-newpatients-definitions.html#Extension "New Patients indicates whether new patients are being accepted in general, or from a specific network.                  This extension is included in the PractitionerRole, HealthcareService, and Location profiles.                 This provides needed flexibility for specifying whether a provider accepts new patients by location and network.") | I | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | New Patients new-patients-characteristics: If no new patients are accepted, no characteristics are allowed |
| ... [extension](StructureDefinition-newpatients-definitions.html#Extension.extension) |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:acceptingPatients](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients "Slice acceptingPatients") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Accepting Patients |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "acceptingPatients" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Accepting Patients Codes VS](ValueSet-AcceptingPatientsVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:fromNetwork](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork "Slice fromNetwork") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | From Network |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "fromNetwork" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.value[x]) |  | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Network](StructureDefinition-plannet-Network.html)) | Value of extension |
| ... [extension:characteristics](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics "Slice characteristics") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Characteristics of accepted patients |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "characteristics" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.value[x]) |  | 1..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Value of extension |
| ... [url](StructureDefinition-newpatients-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-newpatients-definitions.html#Extension "New Patients indicates whether new patients are being accepted in general, or from a specific network.                  This extension is included in the PractitionerRole, HealthcareService, and Location profiles.                 This provides needed flexibility for specifying whether a provider accepts new patients by location and network.") | I | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | New Patients new-patients-characteristics: If no new patients are accepted, no characteristics are allowed |
| ... [id](StructureDefinition-newpatients-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-newpatients-definitions.html#Extension.extension "An Extension") |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:acceptingPatients](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients "Slice acceptingPatients: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Accepting Patients |
| .... [id](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "acceptingPatients" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Accepting Patients Codes VS](ValueSet-AcceptingPatientsVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:fromNetwork](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork "Slice fromNetwork: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | From Network |
| .... [id](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "fromNetwork" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Network](StructureDefinition-plannet-Network.html)) | Value of extension |
| ... [extension:characteristics](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics "Slice characteristics: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Characteristics of accepted patients |
| .... [id](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "characteristics" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Value of extension |
| ... [url](StructureDefinition-newpatients-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 3 elements (2 nested mandatory elements)  
 Must-Support: 3 elements  
 Fixed Value: 4 elements  
 Prohibited: 4 elements

**Structures**

This structure refers to these other structures:

* [Plan-Net Network (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network)](StructureDefinition-plannet-Network.html)

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-newpatients-definitions.html#Extension "New Patients indicates whether new patients are being accepted in general, or from a specific network.                  This extension is included in the PractitionerRole, HealthcareService, and Location profiles.                 This provides needed flexibility for specifying whether a provider accepts new patients by location and network.") | I | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | New Patients new-patients-characteristics: If no new patients are accepted, no characteristics are allowed |
| ... [extension](StructureDefinition-newpatients-definitions.html#Extension.extension) |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| ... [extension:acceptingPatients](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients "Slice acceptingPatients") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Accepting Patients |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "acceptingPatients" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.value[x]) |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Accepting Patients Codes VS](ValueSet-AcceptingPatientsVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:fromNetwork](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork "Slice fromNetwork") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | From Network |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "fromNetwork" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.value[x]) |  | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Network](StructureDefinition-plannet-Network.html)) | Value of extension |
| ... [extension:characteristics](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics "Slice characteristics") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Characteristics of accepted patients |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "characteristics" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.value[x]) |  | 1..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Value of extension |
| ... [url](StructureDefinition-newpatients-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-newpatients-definitions.html#Extension "New Patients indicates whether new patients are being accepted in general, or from a specific network.                  This extension is included in the PractitionerRole, HealthcareService, and Location profiles.                 This provides needed flexibility for specifying whether a provider accepts new patients by location and network.") | I | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | New Patients new-patients-characteristics: If no new patients are accepted, no characteristics are allowed |
| ... [id](StructureDefinition-newpatients-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-newpatients-definitions.html#Extension.extension "An Extension") |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |
| ... [extension:acceptingPatients](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients "Slice acceptingPatients: An Extension") | S | 1..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Accepting Patients |
| .... [id](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "acceptingPatients" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:acceptingPatients.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | Value of extension Binding: [Accepting Patients Codes VS](ValueSet-AcceptingPatientsVS.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:fromNetwork](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork "Slice fromNetwork: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | From Network |
| .... [id](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "fromNetwork" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:fromNetwork.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net Network](StructureDefinition-plannet-Network.html)) | Value of extension |
| ... [extension:characteristics](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics "Slice characteristics: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Characteristics of accepted patients |
| .... [id](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "characteristics" |
| .... [value[x]](StructureDefinition-newpatients-definitions.html#Extension.extension:characteristics.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 1..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Value of extension |
| ... [url](StructureDefinition-newpatients-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-newpatients.csv), [Excel](StructureDefinition-newpatients.xlsx), [Schematron](StructureDefinition-newpatients.sch)

#### Terminology Bindings

|  |  |  |
| --- | --- | --- |
| **Path** | **Conformance** | **ValueSet** |
| Extension.extension:acceptingPatients.value[x] | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [AcceptingPatientsVS](ValueSet-AcceptingPatientsVS.html) |

#### Constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Id** | **Grade** | **Path** | **Details** | **Requirements** |
| new-patients-characteristics | error | Extension | If no new patients are accepted, no characteristics are allowed : extension('acceptingPatients').valueCodeableConcept.coding.exists(code = 'no') implies extension('characteristics').empty() |  |