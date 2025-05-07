

via-intermediary vs via-intermediary

## Profile Comparison between http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary vs http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary

|  |  |
| --- | --- |
| Left: | Via Intermediary (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary) |
| Right: | Via Intermediary (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary) |

### Messages

|  |  |  |
| --- | --- | --- |
| Error | StructureDefinition.version | Values for version differ: '1.0.0' vs '1.1.0' |
| Information | StructureDefinition.date | Values for date differ: '2020-12-07T21:58:00+00:00' vs '2022-04-04T14:04:34+00:00' |
| Warning | Extension | Elements differ in short: 'Extension' vs 'Via Intermediary' |
| Warning | Extension | Elements differ in definition: 'An Extension' vs 'A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization' |
| Error | Extension.value[x] | Type Mismatch: Reference([CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization]]) vs Reference([CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization]]) |

### Metadata

| Name | Value | | Comments |
| --- | --- | --- | --- |
| .abstract | false | |  |
| .baseDefinition | http://hl7.org/fhir/StructureDefinition/Extension | |  |
| .copyright |  | |  |
| .date | 2020-12-07T21:58:00+00:00 | 2022-04-04T14:04:34+00:00 | * Values Differ |
| .description | A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization | |  |
| .experimental |  | |  |
| .fhirVersion | 4.0.1 | |  |
| .jurisdiction |  | |  |
| ..jurisdiction[0] | urn:iso:std:iso:3166#US | |  |
| .kind | complex-type | |  |
| .name | ViaIntermediary | |  |
| .publisher | HL7 Financial Management Working Group | |  |
| .purpose |  | |  |
| .status | active | |  |
| .title | Via Intermediary | |  |
| .type | Extension | |  |
| .url | http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary | |  |
| .version | 1.0.0 | 1.1.0 | * Values Differ |

### Structure

| [Name](http://hl7.org/fhir/formats.html#table "The logical name of the element") | [L Flags](http://hl7.org/fhir/formats.html#table "Information about the use of the element - Left Structure") | [L Card.](http://hl7.org/fhir/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance - Left Structure") | [L Type](http://hl7.org/fhir/formats.html#table "Reference to the type of the element - Left Structure") | [L Description & Constraints](http://hl7.org/fhir/formats.html#table "Additional information about the element - Left Structure") | [R Flags](http://hl7.org/fhir/formats.html#table "Information about the use of the element - Left Structure") | [R Card.](http://hl7.org/fhir/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance - Left Structure") | [L Type](http://hl7.org/fhir/formats.html#table "Reference to the type of the element - Left Structure") | [L Description & Constraints](http://hl7.org/fhir/formats.html#table "Additional information about the element - Left Structure") | [Comments](http://hl7.org/fhir/formats.html#table "Comments about the comparison")[doco](http://hl7.org/fhir/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .. Extension |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Extension |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Via Intermediary | * Elements differ in short: 'Extension' vs 'Via Intermediary' * Elements differ in definition: 'An Extension' vs 'A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization' |
| ... id |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |  |
| ... Slices for extension |  | 0..0 |  |  |  | 0..0 |  |  |  |
| ... url |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |  |
| ... value[x] | S | 1..1 | [Reference](http://hl7.org/fhirreferences.html)([Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html) | [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) | [Plan-Net Location](StructureDefinition-plannet-Location.html) | [Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension | S | 1..1 | [Reference](http://hl7.org/fhirreferences.html)([Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html) | [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) | [Plan-Net Location](StructureDefinition-plannet-Location.html) | [Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension | * Type Mismatch: Reference([CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization]]) vs Reference([CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location], CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization]]) |
| [doco Documentation for this format](http://hl7.org/fhir/formats.html#table "Legend for this format") | | | | | | | | | |