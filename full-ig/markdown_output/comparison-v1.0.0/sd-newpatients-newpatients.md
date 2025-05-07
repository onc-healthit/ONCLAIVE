

newpatients vs newpatients

## Profile Comparison between http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients vs http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients

|  |  |
| --- | --- |
| Left: | New Patients (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients) |
| Right: | New Patients (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients) |

### Messages

|  |  |  |
| --- | --- | --- |
| Error | StructureDefinition.version | Values for version differ: '1.0.0' vs '1.1.0' |
| Information | StructureDefinition.date | Values for date differ: '2020-12-07T21:58:00+00:00' vs '2022-04-04T14:04:34+00:00' |
| Warning | Extension | Elements differ in short: 'Extension' vs 'New Patients' |
| Warning | Extension | Elements differ in definition: 'An Extension' vs 'New Patients indicates whether new patients are being accepted in general, or from a specific network. This extension is included in the PractitionerRole, HealthcareService, and Location profiles. This provides needed flexibility for specifying whether a provider accepts new patients by location and network.' |

### Metadata

| Name | Value | | Comments |
| --- | --- | --- | --- |
| .abstract | false | |  |
| .baseDefinition | http://hl7.org/fhir/StructureDefinition/Extension | |  |
| .copyright |  | |  |
| .date | 2020-12-07T21:58:00+00:00 | 2022-04-04T14:04:34+00:00 | * Values Differ |
| .description | New Patients indicates whether new patients are being accepted in general, or from a specific network. This extension is included in the PractitionerRole, HealthcareService, and Location profiles. This provides needed flexibility for specifying whether a provider accepts new patients by location and network. | |  |
| .experimental |  | |  |
| .fhirVersion | 4.0.1 | |  |
| .jurisdiction |  | |  |
| ..jurisdiction[0] | urn:iso:std:iso:3166#US | |  |
| .kind | complex-type | |  |
| .name | NewPatients | |  |
| .publisher | HL7 Financial Management Working Group | |  |
| .purpose |  | |  |
| .status | active | |  |
| .title | New Patients | |  |
| .type | Extension | |  |
| .url | http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients | |  |
| .version | 1.0.0 | 1.1.0 | * Values Differ |

### Structure

| [Name](http://hl7.org/fhir/formats.html#table "The logical name of the element") | [L Flags](http://hl7.org/fhir/formats.html#table "Information about the use of the element - Left Structure") | [L Card.](http://hl7.org/fhir/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance - Left Structure") | [L Type](http://hl7.org/fhir/formats.html#table "Reference to the type of the element - Left Structure") | [L Description & Constraints](http://hl7.org/fhir/formats.html#table "Additional information about the element - Left Structure") | [R Flags](http://hl7.org/fhir/formats.html#table "Information about the use of the element - Left Structure") | [R Card.](http://hl7.org/fhir/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance - Left Structure") | [L Type](http://hl7.org/fhir/formats.html#table "Reference to the type of the element - Left Structure") | [L Description & Constraints](http://hl7.org/fhir/formats.html#table "Additional information about the element - Left Structure") | [Comments](http://hl7.org/fhir/formats.html#table "Comments about the comparison")[doco](http://hl7.org/fhir/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .. Extension | I | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension new-patients-characteristics: If no new patients are accepted, no characteristics are allowed | I | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | New Patients new-patients-characteristics: If no new patients are accepted, no characteristics are allowed | * Elements differ in short: 'Extension' vs 'New Patients' * Elements differ in definition: 'An Extension' vs 'New Patients indicates whether new patients are being accepted in general, or from a specific network.   This extension is included in the PractitionerRole, HealthcareService, and Location profiles.   This provides needed flexibility for specifying whether a provider accepts new patients by location and network.' |
| ... id |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |  |
| ... Slices for extension |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |  | 1..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension Slice: Unordered, Open by value:url |  |
| ... url |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients" |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients" |  |
| ... value[x] |  | 0..0 |  |  |  | 0..0 |  |  |  |
| [doco Documentation for this format](http://hl7.org/fhir/formats.html#table "Legend for this format") | | | | | | | | | |