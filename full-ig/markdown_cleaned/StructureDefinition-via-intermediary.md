# Extension: Via Intermediary

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Via Intermediary**

Publication Build: This will be filled in by the publication tooling

* [Content](#)
* [Detailed Descriptions](StructureDefinition-via-intermediary-definitions.html)
* [Mappings](StructureDefinition-via-intermediary-mappings.html)

## Extension: Via Intermediary

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: ViaIntermediary |

A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization

**Context of Use**

This extension may be used on the following element(s):

* Element

**Usage info**

**Usage:**

* Use this Extension: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html), [Plan-Net Location](StructureDefinition-plannet-Location.html), [Plan-Net Network](StructureDefinition-plannet-Network.html), [Plan-Net Organization](StructureDefinition-plannet-Organization.html), [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html), [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)
* Examples for this Extension: [Compounding Pharmacy by OrgA](HealthcareService-PharmChainCompService.html), [Pharmacy by PharmChain](HealthcareService-PharmChainRetailService.html), [ACME CT Premium Preferred Provider Network](Organization-AcmeofCTPremNet.html), [ACME CT Preferred Provider Network](Organization-AcmeofCTStdNet.html)

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

* [Plan-Net PractitionerRole (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole)](StructureDefinition-plannet-PractitionerRole.html)
* [Plan-Net OrganizationAffiliation (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation)](StructureDefinition-plannet-OrganizationAffiliation.html)
* [Plan-Net Location (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location)](StructureDefinition-plannet-Location.html)
* [Plan-Net Organization (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization)](StructureDefinition-plannet-Organization.html)

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-via-intermediary-definitions.html#Extension "A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Via Intermediary |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-via-intermediary-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |
| ... [value[x]](StructureDefinition-via-intermediary-definitions.html#Extension.value[x]) | S | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html) | [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) | [Plan-Net Location](StructureDefinition-plannet-Location.html) | [Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-via-intermediary-definitions.html#Extension "A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Via Intermediary |
| ... [id](StructureDefinition-via-intermediary-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-via-intermediary-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-via-intermediary-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |
| ... [value[x]](StructureDefinition-via-intermediary-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") | S | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html) | [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) | [Plan-Net Location](StructureDefinition-plannet-Location.html) | [Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

**Summary**

Mandatory: 1 element  
 Must-Support: 1 element  
 Fixed Value: 1 element  
 Prohibited: 1 element

**Structures**

This structure refers to these other structures:

* [Plan-Net PractitionerRole (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole)](StructureDefinition-plannet-PractitionerRole.html)
* [Plan-Net OrganizationAffiliation (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation)](StructureDefinition-plannet-OrganizationAffiliation.html)
* [Plan-Net Location (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location)](StructureDefinition-plannet-Location.html)
* [Plan-Net Organization (http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization)](StructureDefinition-plannet-Organization.html)

**Differential View**

This structure is derived from [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-via-intermediary-definitions.html#Extension "A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Via Intermediary |
| ... extension |  | 0..0 |  |  |
| ... [url](StructureDefinition-via-intermediary-definitions.html#Extension.url) |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |
| ... [value[x]](StructureDefinition-via-intermediary-definitions.html#Extension.value[x]) | S | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html) | [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) | [Plan-Net Location](StructureDefinition-plannet-Location.html) | [Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

**Snapshot View**

| [Name](http://hl7.org/fhir/R4/formats.html#table "The logical name of the element") | [Flags](http://hl7.org/fhir/R4/formats.html#table "Information about the use of the element") | [Card.](http://hl7.org/fhir/R4/formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](http://hl7.org/fhir/R4/formats.html#table "Reference to the type of the element") | [Description & Constraints](http://hl7.org/fhir/R4/formats.html#table "Additional information about the element")[doco](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Extension](StructureDefinition-via-intermediary-definitions.html#Extension "A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization") |  | 0..\* | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | Via Intermediary |
| ... [id](StructureDefinition-via-intermediary-definitions.html#Extension.id "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.") |  | 0..1 | [string](http://hl7.org/fhir/R4/datatypes.html#string) | Unique id for inter-element referencing |
| ... [Slices for extension](StructureDefinition-via-intermediary-definitions.html#Extension.extension "An Extension") |  | 0..0 |  |  |
| ... [url](StructureDefinition-via-intermediary-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary" |
| ... [value[x]](StructureDefinition-via-intermediary-definitions.html#Extension.value[x] "Value of extension - must be one of a constrained set of the data types (see [Extensibility](http://hl7.org/fhir/R4/extensibility.html) for a list).") | S | 1..1 | [Reference](http://hl7.org/fhir/R4/references.html)([Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html) | [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) | [Plan-Net Location](StructureDefinition-plannet-Location.html) | [Plan-Net Organization](StructureDefinition-plannet-Organization.html)) | Value of extension |
| [doco Documentation for this format](http://hl7.org/fhir/R4/formats.html#table "Legend for this format") | | | | |

Other representations of profile: [CSV](StructureDefinition-via-intermediary.csv), [Excel](StructureDefinition-via-intermediary.xlsx), [Schematron](StructureDefinition-via-intermediary.sch)