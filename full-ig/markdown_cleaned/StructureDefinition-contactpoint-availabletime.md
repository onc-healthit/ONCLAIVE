# Extension: Contactpoint Availabletime

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Contactpoint Availabletime**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-contactpoint-availabletime-definitions.html)
* [Mappings](StructureDefinition-contactpoint-availabletime-mappings.html)

## Extension: Contactpoint Availabletime

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: ContactPointAvailableTime |

An extension representing the days and times a contact point is available

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html), [Plan-Net Location](StructureDefinition-plannet-Location.html), [Plan-Net Network](StructureDefinition-plannet-Network.html), [Plan-Net Organization](StructureDefinition-plannet-Organization.html), [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html), [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)
* Examples for this Extension: [Cancer Clinic](Location-CancerClinicLoc.html), [OrgA CT Location 1](Location-HansSoloClinic.html), [Hartford Hospital Location 1](Location-HospLoc1.html), [Hartford Hospital Location 2](Location-HospLoc2.html), [OrgA CT Location 1](Location-PharmLoc1.html), [OrgA CT Location 2](Location-PharmLoc2.html), [OrgA MA Location 1](Location-PharmLoc3.html), [OrgA MA Location 2](Location-PharmLoc4.html), [Acme of CT](Organization-Acme.html), [Big Box Retailer](Organization-BigBox.html), [Hartford Orthopedics Services](Organization-HartfordOrthopedics.html), [Pharm Chain](Organization-PharmChain.html)

### Formal Views of Extension Content

[Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://hl7.org/fhir/R4/profiling.html#representation).

* [Text Summary](#tabs-summ)
* [Differential Table](#tabs-diff)
* [Snapshot Table](#tabs-snap)

* [All](#tabs-all)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Must-Support: 4 elements  
 Fixed Value: 5 elements  
 Prohibited: 5 elements

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

* The element Extension.extension.value[x] is sliced based on the value of type:$this

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension "An extension representing the days and times a contact point is available") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Contactpoint Availabletime |
| ... [extension:daysOfWeek](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek "Slice daysOfWeek") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "daysOfWeek" |
| .... [Slices for value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.value[x]) |  | 0..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Open by type:$this |
| .... [valueCode](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.valueCode) |  | 0..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:allDay](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay "Slice allDay") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "allDay" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.value[x]) |  | 0..1 | [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | Value of extension |
| ... [extension:availableStartTime](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime "Slice availableStartTime") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "availableStartTime" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.value[x]) |  | 0..1 | [time](http://hl7.org/fhir/R4/datatypes.html#time) | Value of extension |
| ... [extension:availableEndTime](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime "Slice availableEndTime") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "availableEndTime" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.value[x]) |  | 0..1 | [time](http://hl7.org/fhir/R4/datatypes.html#time) | Value of extension |
| ... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension "An extension representing the days and times a contact point is available") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Contactpoint Availabletime |
| ... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Additional content defined by implementations Slice: Unordered, Open by value:url |
| ... [extension:daysOfWeek](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek "Slice daysOfWeek: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "daysOfWeek" |
| .... [Slices for value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Closed by type:$this |
| ..... [value[x]:valueCode](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.value[x]:valueCode "Slice valueCode: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:allDay](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay "Slice allDay: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "allDay" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | Value of extension |
| ... [extension:availableStartTime](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime "Slice availableStartTime: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "availableStartTime" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [time](http://hl7.org/fhir/R4/datatypes.html#time) | Value of extension |
| ... [extension:availableEndTime](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime "Slice availableEndTime: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "availableEndTime" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [time](http://hl7.org/fhir/R4/datatypes.html#time) | Value of extension |
| ... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Must-Support: 4 elements  
 Fixed Value: 5 elements  
 Prohibited: 5 elements

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

* The element Extension.extension.value[x] is sliced based on the value of type:$this

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension "An extension representing the days and times a contact point is available") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Contactpoint Availabletime |
| ... [extension:daysOfWeek](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek "Slice daysOfWeek") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "daysOfWeek" |
| .... [Slices for value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.value[x]) |  | 0..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Open by type:$this |
| .... [valueCode](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.valueCode) |  | 0..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:allDay](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay "Slice allDay") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "allDay" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.value[x]) |  | 0..1 | [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | Value of extension |
| ... [extension:availableStartTime](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime "Slice availableStartTime") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "availableStartTime" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.value[x]) |  | 0..1 | [time](http://hl7.org/fhir/R4/datatypes.html#time) | Value of extension |
| ... [extension:availableEndTime](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime "Slice availableEndTime") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... extension |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "availableEndTime" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.value[x]) |  | 0..1 | [time](http://hl7.org/fhir/R4/datatypes.html#time) | Value of extension |
| ... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| ... value[x] |  | 0..0 |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension "An extension representing the days and times a contact point is available") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Contactpoint Availabletime |
| ... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Additional content defined by implementations Slice: Unordered, Open by value:url |
| ... [extension:daysOfWeek](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek "Slice daysOfWeek: An Extension") | S | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "daysOfWeek" |
| .... [Slices for value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Slice: Unordered, Closed by type:$this |
| ..... [value[x]:valueCode](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:daysOfWeek.value[x]:valueCode "Slice valueCode: Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [code](http://hl7.org/fhir/R4/datatypes.html#code) | Value of extension Binding: [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [extension:allDay](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay "Slice allDay: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "allDay" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:allDay.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | Value of extension |
| ... [extension:availableStartTime](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime "Slice availableStartTime: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "availableStartTime" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableStartTime.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [time](http://hl7.org/fhir/R4/datatypes.html#time) | Value of extension |
| ... [extension:availableEndTime](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime "Slice availableEndTime: An Extension") | S | 0..1 | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |
| .... [id](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| .... [Slices for extension](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.extension "An Extension") |  | 0..0 |  |  |
| .... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "availableEndTime" |
| .... [value[x]](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.extension:availableEndTime.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") |  | 0..1 | [time](http://hl7.org/fhir/R4/datatypes.html#time) | Value of extension |
| ... [url](StructureDefinition-contactpoint-availabletime-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime" |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-contactpoint-availabletime.csv), [Excel](StructureDefinition-contactpoint-availabletime.xlsx), [Schematron](StructureDefinition-contactpoint-availabletime.sch)

#### Terminology Bindings

|  |  |  |
| --- | --- | --- |
| **Path** | **Conformance** | **ValueSet** |
| Extension.extension:daysOfWeek.value[x]:valueCode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html) |