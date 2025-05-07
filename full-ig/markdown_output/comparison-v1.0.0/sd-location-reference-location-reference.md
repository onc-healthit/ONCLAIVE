

location-reference vs location-reference

## Profile Comparison between http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference vs http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference

|  |  |
| --- | --- |
| Left: | Location Reference (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference) |
| Right: | Location Reference (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference) |

### Messages

|  |  |  |
| --- | --- | --- |
| Error | StructureDefinition.version | Values for version differ: '1.0.0' vs '1.1.0' |
| Information | StructureDefinition.date | Values for date differ: '2020-12-07T21:58:00+00:00' vs '2022-04-04T14:04:34+00:00' |
| Warning | Extension | Elements differ in short: 'Extension' vs 'Location Reference' |
| Warning | Extension | Elements differ in definition: 'An Extension' vs 'A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network' |
| Error | Extension.value[x] | Type Mismatch: Reference([CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location]]) vs Reference([CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location]]) |

### Metadata

| Name | Value | | Comments |
| --- | --- | --- | --- |
| .abstract | false | |  |
| .baseDefinition | http://hl7.org/fhir/StructureDefinition/Extension | |  |
| .copyright |  | |  |
| .date | 2020-12-07T21:58:00+00:00 | 2022-04-04T14:04:34+00:00 | * Values Differ |
| .description | A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network | |  |
| .experimental |  | |  |
| .fhirVersion | 4.0.1 | |  |
| .jurisdiction |  | |  |
| ..jurisdiction[0] | urn:iso:std:iso:3166#US | |  |
| .kind | complex-type | |  |
| .name | LocationReference | |  |
| .publisher | HL7 Financial Management Working Group | |  |
| .purpose |  | |  |
| .status | active | |  |
| .title | Location Reference | |  |
| .type | Extension | |  |
| .url | http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference | |  |
| .version | 1.0.0 | 1.1.0 | * Values Differ |

### Structure

| [Name](http://hl7.org/fhir/formats.html#table "The logical name of the element") | [L Flags](http://hl7.org/fhir/formats.html#table "Information about the use of the element - Left Structure") | [L Card.](http://hl7.org/fhir/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance - Left Structure") | [L Type](http://hl7.org/fhir/formats.html#table "Reference to the type of the element - Left Structure") | [L Description & Constraints](http://hl7.org/fhir/formats.html#table "Additional information about the element - Left Structure") | [R Flags](http://hl7.org/fhir/formats.html#table "Information about the use of the element - Left Structure") | [R Card.](http://hl7.org/fhir/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance - Left Structure") | [L Type](http://hl7.org/fhir/formats.html#table "Reference to the type of the element - Left Structure") | [L Description & Constraints](http://hl7.org/fhir/formats.html#table "Additional information about the element - Left Structure") | [Comments](http://hl7.org/fhir/formats.html#table "Comments about the comparison")[doco](http://hl7.org/fhir/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .. Extension |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Location Reference | * Elements differ in short: 'Extension' vs 'Location Reference' * Elements differ in definition: 'An Extension' vs 'A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network' |
| ... id |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |  |
| ... Slices for extension |  | 0..0 |  |  |  | 0..0 |  |  |  |
| ... url |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference" |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference" |  |
| ... value[x] | S | 1..1 | [Reference](http://hl7.org/fhirreferences.html)([Plan-Net Location](StructureDefinition-plannet-Location.html)) | Value of extension | S | 1..1 | [Reference](http://hl7.org/fhirreferences.html)([Plan-Net Location](StructureDefinition-plannet-Location.html)) | Value of extension | * Type Mismatch: Reference([CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location]]) vs Reference([CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location]]) |
| [doco Documentation for this format](http://hl7.org/fhir/formats.html#table "Legend for this format") | | | | | | | | | |