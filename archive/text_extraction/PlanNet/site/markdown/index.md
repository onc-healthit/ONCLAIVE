xml version="1.0" encoding="UTF-8"?

Home - Da Vinci PDex Plan Net v1.2.0

[![Visit the HL7 website](assets/images/hl7-logo-header.png)](http://hl7.org)

[![Visit the FHIR website](assets/images/fhir-logo-www.png)](http://hl7.org/fhir) 

[![Search FHIR](assets/images/search.png)](searchform.html)

[![Visit the Da Vinci website](assets/images/da-vinci_logo.jpg)](http://hl7.org/about/davinci) 

Da Vinci PDex Plan Net

1.2.0 - STU1.2
![United States of America flag](assets/images/usa.svg "United States of America")

[FHIR](http://hl7.org/fhir/R4/index.html)

* [IG Home](index.html)
* [Background](#)
  + [Reading this IG](reading.html)
  + [Use Cases](background.html)
  + [Project and Participants](project.html)
* [Specification](#)
  + [Conformance Expectations](confexpectations.html)
  + [Implementation](implementation.html)
  + [Privacy, Safety, and Security](security.html)
* [FHIR Artifacts](artifacts.html)
* [Base Specs](#)
  + [FHIR R4 Spec](http://hl7.org/fhir/R4/)
  + [HRex 1.1.0](http://hl7.org/fhir/us/davinci-hrex/STU1.1)
  + [US Core 3.1.1](http://hl7.org/fhir/us/core/STU3.1.1/index.html)
  + [US Core 6.1.0](https://hl7.org/fhir/us/core/STU6.1/index.html)
  + [US Core 7.0.0](https://hl7.org/fhir/us/core/STU7/index.html)
* [Support](#)
  + [Discussion Forum](https://chat.fhir.org/#narrow/stream/208874-Da-Vinci-PAS)
  + [Project Page](https://confluence.hl7.org/pages/viewpage.action?pageId=116462616)
  + [Implementer Support](https://confluence.hl7.org/pages/viewpage.action?pageId=116462616)
  + [Specification Dashboard](https://jira.hl7.org/secure/Dashboard.jspa?selectPageId=11903)
  + [Propose a Change](https://jira.hl7.org/secure/CreateIssueDetails!init.jspa?pid=10405&issuetype=10600&customfield_11302=FHIR-us-davinci-pas)
  + [Downloads](downloads.html)
* [Change Log](ChangeHistory.html)
* [History](http://www.hl7.org/fhir/us/davinci-pdex-plan-net/history.cfml)

* [**Table of Contents**](toc.html)
* **Home**
[<prev](toc.html) |
[bottom](#bottom)
| [next>](background.html)

This page is part of the DaVinci PDEX Plan Net (v1.2.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1) based on [FHIR (HL7® FHIR® Standard) R4](http://hl7.org/fhir/R4). This is the current published version. For a full list of available versions, see the [Directory of published versions](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html)

Plain Language Summary Goes Here
## Home

| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ImplementationGuide/hl7.fhir.us.davinci-pdex-plan-net | | | | *Version*: 1.2.0 |
| --- | --- | --- | --- | --- |
| *IG Standards status:* [Trial-use](http://hl7.org/fhir/R4/versions.html#std-process "Standard Status") | | | | *Computable Name*: DaVinciPDEXPlanNet |

* [Introduction](#introduction)
* [Content and Organization](#content-and-organization)
* [Relation to US Core and other IGs](#relation-to-us-core-and-other-igs)
* [Dependencies](#dependencies)
* [Intellectual Property Considerations](#intellectual-property-considerations)
### Introduction

This implementation guide defines a FHIR interface to a health insurer's insurance plans, their associated networks, and the organizations and providers that participate in these networks. Publication of this data through a standard FHIR-based API will enable third parties to develop applications through which consumers and providers can query the participants in a payer's network that may provide services that address their health care needs. Although there are multiple types and sources of providers' directories, including provider organizations (i.e., a hospital listing all its physicians), government (i.e., listing of providers in Medicare), payers (i.e., a health plan's provider network), and third-party entities (such as vendors that maintain provider directories), the focus of this implementation guide is on Payer Provider Directories.

The PDEX Payer Network (or Plan-Net) Implementation Guide is based conceptually on the [Validated Healthcare Directory Implementation Guide (VHDir IG)](http://hl7.org/fhir/uv/vhdir/2018Sep/index.html), an international standard. The VHDir IG is based on [FHIR Version 4.0](http://hl7.org/fhir/R4/index.html). It was developed in cooperation with the [Office of the National Coordinator for Health Information Technology (ONC)](http://www.healthit.gov/newsroom/about-onc) and [Federal Health Architecture (FHA)](https://www.healthit.gov/policy-researchers-implementers/federal-health-architecture-fha) with guidance from HL7 International, the Patient Administration Workgroup, and the HL7 US Realm Steering Committee.

The use of VhDir as the conceptual base for the profiles and extensions in the PDEX Payer Network Implementation Guide is intended to protect implementers of the Plan-Net IG from rework/remapping when the VHDir concept reaches implementation, and becomes a source of data for the PDEX Payer Network. The primary changes from the VHDir IG are to:

1. remove the validation and restriction resources
2. use US Core for R4 as the base suite of profiles where possible
3. eliminate extensions that are not necessary for this use case
4. introduce additional constraints (e.g. search criteria, cardinality, value-set bindings and MustSupport) where appropriate.

The diagram below depicts the scope of this implementation guide (IG). The IG defines the API that exposes a payer’s provider network (including pharmacy locations where appropriate) for access by a consumer or provider application. This is a query only API (GET) and does not support PUT or POST.

![](Bob3.png)

### Content and Organization

The IG is organized into the following sections:

* [Conformance Expectations](confexpectations.html): Conformance rules for this IG.
* [Background](background.html): Provides examples of how this specification can be used healthcare organizations.
* [Implementation](implementation.html): Provides examples of how this specification can be used healthcare organizations.
* [Artifacts](artifacts.html): The computable FHIR artifacts (profiles, value sets, etc.) for this specification.

### Relation to US Core and other IGs

This implementation guide was written for a US audience and profiles resources from [US Core STU 4](/index.html), where available (Practitioner, Organization and Location), and otherwise from R4 (OrganizationAffiliation, PractitionerRole, HealthCareService, Endpoint). The PractitionerRole profile from US Core was not used because it is over-constrained for use in a Provider Directory based on Payer information. The Network profile is based on USCore Organization, since there was no contradiction between the USCore profile and the Plan-Net requirements. However, the NPI and CLIA identifier types, which are Must-Support, are clearly intended for provider organizations only and are not expected to be populated for other organization types. Alignment with VhDir is maintained by adapting VhDir content, where possible.

#### Disclaimers and Assumptions

* **PDEX Payer Network is based conceptually on VhDir**: The PDEX Payer Network implementation guide is based conceptually on the VhDir implementation guide, which is still a work in progress. Plan-net will need to track changes to VhDir to fulfill its goal of minimizing rework.
* **The PDEX Payer Network endpoint is known to the client**: This implementation guide assumes that the directory endpoint is known to the client. There is an overarching system architecture issue that is critical to resolve -- how does the client discover the FHIR endpoint of interest. For the purposes of this IG, we consider that problem out of scope.

#### Background

Provider directories play a critical role in enabling identification of individual providers and provider organizations, as well as characteristics about them. Provider directories support a variety of use cases, including:

* Patient/Payer focused

+ Find provider accessibility information (specialty, office hours, languages spoken, taking patients) - enables individuals and consumers to find contact and other accessibility information for individual healthcare providers and/or healthcare organizations
+ Relationship between provider and insurance plan (insurance accepted) or plan and provider (network) - enables individual healthcare providers, organizations, and payers to discover the relationships between providers, organizations, and payers, as well as additional details about the relationships and entities involved

* Basic Information Exchange

+ Enable electronic exchange (e.g. discovery of electronic endpoints such as IHE/EHR endpoints, FHIR server URLs, Direct addresses) - enables the electronic exchange of health information by supporting the ability to discover electronic service information including electronic endpoints or electronic addresses
+ Find an individual and/or organization (even if no electronic endpoint is available) - enables users to find contact and other identifying information about healthcare organizations and individual healthcare providers

This IG addresses two actors:

* Health Plan API Actor: A payer publishing a directory of its provider networks through a FHIR endpoint.
* Application Actor: A third party using the API published by a payer to provide useful views of the payer's provider networks for end users.

For anticipated query use cases, please see [Representing and Searching Provider Data](implementation.html#Representing).

#### Overview of Payer Directory - Resource Relationships

Note: the following diagrams provide a high-level view of the relationships between resources used in this IG. They do not necessarily reflect all of the relationships/references between resources.

![Key Relationships Among Payer Directory Resources](Slide2.png)
![Relationships Between Payer Directory Resources -- Endpoints](Slide3.png)

#### Credits

This IG was developed by the MITRE Corporation under the direction of the authors using [FHIR Shorthand syntax](https://build.fhir.org/ig/HL7/fhir-shorthand/) and the [SUSHI tookit](https://github.com/FHIR/sushi), a free, open source toolchain from the MITRE Corporation. Generous guidance on FHIR Shorthand and SUSHI was provided by Chris Moesel. The capability statements were developed with support of tools and generous guidance from Eric Haas, and benefited from critical review by Yengibar Manasyan.

### Dependencies

| IG | Package | FHIR | Comment |
| --- | --- | --- | --- |
| .. Da Vinci PDex Plan Net | [hl7.fhir.us.davinci-pdex-plan-net#1.2.0](https://simplifier.net/packages/hl7.fhir.us.davinci-pdex-plan-net/1.2.0) | [R4](http://hl7.org/fhir/R4) |  |
| ... [HL7 Terminology (THO)](http://terminology.hl7.org/6.2.0 "Canonical: http://terminology.hl7.org") | [hl7.terminology.r4#6.2.0](https://simplifier.net/packages/hl7.terminology.r4/6.2.0) | [R4](http://hl7.org/fhir/R4) | Automatically added as a dependency - all IGs depend on HL7 Terminology |
| ... [FHIR Extensions Pack](http://hl7.org/fhir/extensions/5.2.0 "Canonical: http://hl7.org/fhir/extensions") | [hl7.fhir.uv.extensions.r4#5.2.0](https://simplifier.net/packages/hl7.fhir.uv.extensions.r4/5.2.0) | [R4](http://hl7.org/fhir/R4) | Automatically added as a dependency - all IGs depend on the HL7 Extension Pack |
| ... [US Core (Reuse Wrapper)](http://hl7.org/fhir/us/core/STU3.1.1 "Canonical: http://hl7.org/fhir/us/core/v311") | [hl7.fhir.us.core.v311#3.1.1](https://simplifier.net/packages/hl7.fhir.us.core.v311/3.1.1) | [R4](http://hl7.org/fhir/R4) | Needed for systems supporting USCDI v1 |
| .... [US Core](http://hl7.org/fhir/us/core/STU3.1.1 "Canonical: http://hl7.org/fhir/us/core") | [hl7.fhir.us.core#3.1.1](https://simplifier.net/packages/hl7.fhir.us.core/3.1.1) | [R4](http://hl7.org/fhir/R4) |  |
| ... [US Core (Reuse Wrapper)](http://hl7.org/fhir/us/core/STU6.1 "Canonical: http://hl7.org/fhir/us/core/v610") | [hl7.fhir.us.core.v610#6.1.0](https://simplifier.net/packages/hl7.fhir.us.core.v610/6.1.0) | [R4](http://hl7.org/fhir/R4) | Needed for systems supporting USCDI v3 |
| .... [US Core Implementation Guide](http://hl7.org/fhir/us/core/STU6.1 "Canonical: http://hl7.org/fhir/us/core") | [hl7.fhir.us.core#6.1.0](https://simplifier.net/packages/hl7.fhir.us.core/6.1.0) | [R4](http://hl7.org/fhir/R4) |  |
| ..... [HL7 Terminology (THO)](http://terminology.hl7.org/5.0.0 "Canonical: http://terminology.hl7.org") | [hl7.terminology.r4#5.0.0](https://simplifier.net/packages/hl7.terminology.r4/5.0.0) | [R4](http://hl7.org/fhir/R4) |  |
| ..... [FHIR Extensions Pack](http://hl7.org/fhir/extensions/1.0.0 "Canonical: http://hl7.org/fhir/extensions") | [hl7.fhir.uv.extensions.r4#1.0.0](https://simplifier.net/packages/hl7.fhir.uv.extensions.r4/1.0.0) | [R4](http://hl7.org/fhir/R4) |  |
| ..... [Bulk Data Access IG](http://hl7.org/fhir/uv/bulkdata/STU2 "Canonical: http://hl7.org/fhir/uv/bulkdata") | [hl7.fhir.uv.bulkdata#2.0.0](https://simplifier.net/packages/hl7.fhir.uv.bulkdata/2.0.0) | [R4](http://hl7.org/fhir/R4) |  |
| ..... [SMART App Launch](http://hl7.org/fhir/smart-app-launch/STU2.1 "Canonical: http://hl7.org/fhir/smart-app-launch") | [hl7.fhir.uv.smart-app-launch#2.1.0](https://simplifier.net/packages/hl7.fhir.uv.smart-app-launch/2.1.0) | [R4](http://hl7.org/fhir/R4) |  |
| ..... [VSAC](http://fhir.org/packages/us.nlm.vsac "Canonical: http://fhir.org/packages/us.nlm.vsac") | [us.nlm.vsac#0.11.0](https://simplifier.net/packages/us.nlm.vsac/0.11.0) | [R4](http://hl7.org/fhir/R4) |  |
| ..... [Structured Data Capture](http://hl7.org/fhir/uv/sdc/STU3 "Canonical: http://hl7.org/fhir/uv/sdc") | [hl7.fhir.uv.sdc#3.0.0](https://simplifier.net/packages/hl7.fhir.uv.sdc/3.0.0) | [R4](http://hl7.org/fhir/R4) |  |
| ..... [PHINVads](http://fhir.org/packages/us.cdc.phinvads "Canonical: http://fhir.org/packages/us.cdc.phinvads") | [us.cdc.phinvads#0.12.0](https://simplifier.net/packages/us.cdc.phinvads/0.12.0) | [R4](http://hl7.org/fhir/R4) |  |
| ..... [IHE FormatCode Vocabulary](https://profiles.ihe.net/fhir/ihe.formatcode.fhir/1.1.0 "Canonical: https://profiles.ihe.net/fhir/ihe.formatcode.fhir") | [ihe.formatcode.fhir#1.1.0](https://simplifier.net/packages/ihe.formatcode.fhir/1.1.0) | [R4](http://hl7.org/fhir/R4) |  |
| ... [US Core Implementation Guide](http://hl7.org/fhir/us/core/STU7 "Canonical: http://hl7.org/fhir/us/core") | [hl7.fhir.us.core#7.0.0](https://simplifier.net/packages/hl7.fhir.us.core/7.0.0) | [R4](http://hl7.org/fhir/R4) | Needed for systems supporting USCDI v4 |
| .... [HL7 Terminology (THO)](http://terminology.hl7.org/5.5.0 "Canonical: http://terminology.hl7.org") | [hl7.terminology.r4#5.5.0](https://simplifier.net/packages/hl7.terminology.r4/5.5.0) | [R4](http://hl7.org/fhir/R4) |  |
| .... [SMART App Launch](http://hl7.org/fhir/smart-app-launch/STU2 "Canonical: http://hl7.org/fhir/smart-app-launch") | [hl7.fhir.uv.smart-app-launch#2.0.0](https://simplifier.net/packages/hl7.fhir.uv.smart-app-launch/2.0.0) | [R4](http://hl7.org/fhir/R4) |  |
| .... [VSAC](http://fhir.org/packages/us.nlm.vsac "Canonical: http://fhir.org/packages/us.nlm.vsac") | [us.nlm.vsac#0.18.0](https://simplifier.net/packages/us.nlm.vsac/0.18.0) | [R4](http://hl7.org/fhir/R4) |  |
| ... [Da Vinci Health Record Exchange (HRex)](http://hl7.org/fhir/us/davinci-hrex/STU1.1 "Canonical: http://hl7.org/fhir/us/davinci-hrex") | [hl7.fhir.us.davinci-hrex#1.1.0](https://simplifier.net/packages/hl7.fhir.us.davinci-hrex/1.1.0) | [R4](http://hl7.org/fhir/R4) |  |
| .... [HL7 Terminology (THO)](http://terminology.hl7.org/6.1.0 "Canonical: http://terminology.hl7.org") | [hl7.terminology.r4#6.1.0](https://simplifier.net/packages/hl7.terminology.r4/6.1.0) | [R4](http://hl7.org/fhir/R4) |  |
| .... [FHIR Extensions Pack](http://hl7.org/fhir/extensions/5.1.0 "Canonical: http://hl7.org/fhir/extensions") | [hl7.fhir.uv.extensions.r4#5.1.0](https://simplifier.net/packages/hl7.fhir.uv.extensions.r4/5.1.0) | [R4](http://hl7.org/fhir/R4) |  |
| .... [VSAC](http://fhir.org/packages/us.nlm.vsac "Canonical: http://fhir.org/packages/us.nlm.vsac") | [us.nlm.vsac#0.19.0](https://simplifier.net/packages/us.nlm.vsac/0.19.0) | [R4](http://hl7.org/fhir/R4) |  |

| **Package hl7.fhir.uv.extensions.r4#5.2.0**  This IG defines the global extensions - the ones defined for everyone. These extensions are always in scope wherever FHIR is being used (built Mon, Feb 10, 2025 21:45+1100+11:00) |
| --- |

| **Package hl7.fhir.uv.extensions.r4#1.0.0**  This IG defines the global extensions - the ones defined for everyone. These extensions are always in scope wherever FHIR is being used (built Sun, Mar 26, 2023 08:46+1100+11:00) |
| --- |

| **Package hl7.fhir.uv.bulkdata#2.0.0**  FHIR based approach for exporting large data sets from a FHIR server to a client application (built Fri, Nov 26, 2021 05:56+1100+11:00) |
| --- |

| **Package hl7.fhir.uv.sdc#3.0.0**  The SDC specification provides an infrastructure to standardize the capture and expanded use of patient-level data collected within an EHR.This includes two components:\* Support more sophisticated questionnaire/form use-cases such as those needed for research, oncology, pathology and other clinical domains.\*Support pre-population and auto-population of EHR data into forms/questionnaires for uses outside direct clinical care (patient safety, adverse event reporting, public health reporting, etc.). (built Tue, Mar 8, 2022 18:32+0000+00:00) |
| --- |

| **Package ihe.formatcode.fhir#1.1.0**  Implementation Guide for IHE defined FormatCode vocabulary. (built Thu, Feb 24, 2022 16:55-0600-06:00) |
| --- |

| **Package hl7.fhir.us.core#6.1.0**  The US Core Implementation Guide is based on FHIR Version R4 and defines the minimum conformance requirements for accessing patient data. The Argonaut pilot implementations, ONC 2015 Edition Common Clinical Data Set (CCDS), and ONC U.S. Core Data for Interoperability (USCDI) v1 provided the requirements for this guide. The prior Argonaut search and vocabulary requirements, based on FHIR DSTU2, are updated in this guide to support FHIR Version R4. This guide was used as the basis for further testing and guidance by the Argonaut Project Team to provide additional content and guidance specific to Data Query Access for purpose of ONC Certification testing. These profiles are the foundation for future US Realm FHIR implementation guides. In addition to Argonaut, they are used by DAF-Research, QI-Core, and CIMI. Under the guidance of HL7 and the HL7 US Realm Steering Committee, the content will expand in future versions to meet the needs specific to the US Realm. These requirements were originally developed, balloted, and published in FHIR DSTU2 as part of the Office of the National Coordinator for Health Information Technology (ONC) sponsored Data Access Framework (DAF) project. For more information on how DAF became US Core see the US Core change notes. (built Fri, Jun 30, 2023 14:02+0000+00:00) |
| --- |

| **Package hl7.fhir.us.core#7.0.0**  The US Core Implementation Guide is based on FHIR Version R4 and defines the minimum conformance requirements for accessing patient data. The Argonaut pilot implementations, ONC 2015 Edition Common Clinical Data Set (CCDS), and ONC U.S. Core Data for Interoperability (USCDI) v1 provided the requirements for this guide. The prior Argonaut search and vocabulary requirements, based on FHIR DSTU2, are updated in this guide to support FHIR Version R4. This guide was used as the basis for further testing and guidance by the Argonaut Project Team to provide additional content and guidance specific to Data Query Access for purpose of ONC Certification testing. These profiles are the foundation for future US Realm FHIR implementation guides. In addition to Argonaut, they are used by DAF-Research, QI-Core, and CIMI. Under the guidance of HL7 and the HL7 US Realm Steering Committee, the content will expand in future versions to meet the needs specific to the US Realm. These requirements were originally developed, balloted, and published in FHIR DSTU2 as part of the Office of the National Coordinator for Health Information Technology (ONC) sponsored Data Access Framework (DAF) project. For more information on how DAF became US Core see the US Core change notes. (built Wed, May 8, 2024 15:33+0000+00:00) |
| --- |

| **Package hl7.fhir.uv.extensions.r4#5.1.0**  This IG defines the global extensions - the ones defined for everyone. These extensions are always in scope wherever FHIR is being used (built Sat, Apr 27, 2024 18:39+1000+10:00) |
| --- |

| **Package hl7.fhir.us.davinci-hrex#1.1.0**  The Da Vinci Payer Health Record exchange (HRex) Framework/library specifies the FHIR elements used in multiple Da Vinci implementation guides. This includes FHIR profiles, functions, operations, and constraints on other specifications such as CDS-Hooks and other aspects of Da Vinci Use Cases that are common across more than a single use case.\n\nDa Vinci HRex Implementation Guide (IG) will make use of US Core profiles that are based on the FHIR R4 specification wherever practical. The HRex IG will use the HL7 FHIR Release 4/US Core STU3 specification as its base but will provide additional guidance and documentation to support implementations that follow the HL7 FHIR STU3/US Core STU2 and HL7 FHIR DSTU2/Argonaut specifications.\n\nThe HRex profiles documented in this IG will be used to exchange data between providers systems (e.g. EHRs) and other providers, payers, and third-party applications where appropriate. In addition, exchanges from payer systems to providers, other payers, and third-party applications are supported by the HRex profiles and operations.\n\nHRex may define new extensions, profiles, value sets, constraints/extension to other specification (e.g. specific CDS-Hooks) that are specific Da Vinci requirements. Where appropriate these Da Vinci specific artifacts will be promoted for incorporation into the future versions of existing standards (e.g. R4 US Core profiles) and deprecated in this guide on publication in the updated standard. (built Tue, Dec 10, 2024 16:17+0000+00:00) |
| --- |

### Intellectual Property Considerations

This implementation guide and the underlying FHIR specification are licensed as public domain under the [FHIR license](http://hl7.org/fhir/R4/license.html#license). The license page also describes rules for the use of the FHIR name and logo.

This publication includes IP covered under the following statements.

* Copyright HL7. Licensed under creative commons public domain Show Usage
  + [degreeLicenseCertificate](http://terminology.hl7.org/5.0.0/CodeSystem-v2-0360.html): [IndividualSpecialtyAndDegreeLicenseCertificateVS](ValueSet-IndividualSpecialtyAndDegreeLicenseCertificateVS.html), [NonIndividualSpecialtyAndDegreeLicenseCertificateVS](ValueSet-NonIndividualSpecialtyAndDegreeLicenseCertificateVS.html)... Show 6 more, [PlannetPractitioner](StructureDefinition-plannet-Practitioner.html), [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html), [Practitioner/HansSolo](Practitioner-HansSolo.html), [Practitioner/JoeSmith](Practitioner-JoeSmith.html), [Qualification](StructureDefinition-qualification.html) and [SpecialtyAndDegreeLicenseCertificateVS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html)
* ISO maintains the copyright on the country codes, and controls its use carefully. For further details see the ISO 3166 web page: <https://www.iso.org/iso-3166-country-codes.html> Show Usage
  + [ISO 3166-1 Codes for the representation of names of countries and their subdivisions — Part 1: Country code](http://terminology.hl7.org/6.1.0/CodeSystem-ISO3166Part1.html): [AcceptingPatientsCS](CodeSystem-AcceptingPatientsCS.html), [AcceptingPatientsVS](ValueSet-AcceptingPatientsVS.html)... Show 115 more, [Accessibility](StructureDefinition-accessibility.html), [AccessibilityCS](CodeSystem-AccessibilityCS.html), [AccessibilityVS](ValueSet-AccessibilityVS.html), [CommunicationProficiency](StructureDefinition-communication-proficiency.html), [ContactPointAvailableTime](StructureDefinition-contactpoint-availabletime.html), DaVinciPDEXPlanNet, [DavinciPdexPlanNetCapabilityStatement](CapabilityStatement-plan-net.html), [DeliveryMethod](StructureDefinition-delivery-method.html), [DeliveryMethodCS](CodeSystem-DeliveryMethodCS.html), [DeliveryMethodVS](ValueSet-DeliveryMethodVS.html), [EndpointConnectionTypeCS](CodeSystem-EndpointConnectionTypeCS.html), [EndpointConnectionTypeVS](ValueSet-EndpointConnectionTypeVS.html), [EndpointPayloadTypeCS](CodeSystem-EndpointPayloadTypeCS.html), [EndpointPayloadTypeVS](ValueSet-EndpointPayloadTypeVS.html), [EndpointUsecase](StructureDefinition-endpoint-usecase.html), [EndpointUsecaseVS](ValueSet-EndpointUsecaseVS.html), [HealthcareServiceCategoryCS](CodeSystem-HealthcareServiceCategoryCS.html), [HealthcareServiceCategoryVS](ValueSet-HealthcareServiceCategoryVS.html), [HealthcareServiceTypeVS](ValueSet-HealthcareServiceTypeVS.html), [IndividualAndGroupSpecialtiesVS](ValueSet-IndividualAndGroupSpecialtiesVS.html), [IndividualSpecialtyAndDegreeLicenseCertificateVS](ValueSet-IndividualSpecialtyAndDegreeLicenseCertificateVS.html), [InsurancePlanTypeCS](CodeSystem-InsurancePlanTypeCS.html), [InsurancePlanTypeVS](ValueSet-InsurancePlanTypeVS.html), [InsuranceProductTypeCS](CodeSystem-InsuranceProductTypeCS.html), [InsuranceProductTypeVS](ValueSet-InsuranceProductTypeVS.html), [LanguageProficiencyCS](CodeSystem-LanguageProficiencyCS.html), [LanguageProficiencyVS](ValueSet-LanguageProficiencyVS.html), [LocationReference](StructureDefinition-location-reference.html), [MinEndpointConnectionTypeVS](ValueSet-MinEndpointConnectionTypeVS.html), [NetworkReference](StructureDefinition-network-reference.html), [NetworkTypeVS](ValueSet-NetworkTypeVS.html), [NewPatients](StructureDefinition-newpatients.html), [NonIndividualSpecialtiesVS](ValueSet-NonIndividualSpecialtiesVS.html), [NonIndividualSpecialtyAndDegreeLicenseCertificateVS](ValueSet-NonIndividualSpecialtyAndDegreeLicenseCertificateVS.html), [OrgDescription](StructureDefinition-org-description.html), [OrgTypeCS](CodeSystem-OrgTypeCS.html), [OrgTypeVS](ValueSet-OrgTypeVS.html), [OrganizationAffiliationRoleCS](CodeSystem-OrganizationAffiliationRoleCS.html), [OrganizationAffiliationRoleVS](ValueSet-OrganizationAffiliationRoleVS.html), [PlannetEndpoint](StructureDefinition-plannet-Endpoint.html), [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html), [PlannetInsurancePlan](StructureDefinition-plannet-InsurancePlan.html), [PlannetLocation](StructureDefinition-plannet-Location.html), [PlannetNetwork](StructureDefinition-plannet-Network.html), [PlannetOrganization](StructureDefinition-plannet-Organization.html), [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html), [PlannetPractitioner](StructureDefinition-plannet-Practitioner.html), [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html), [Plannet\_sp\_endpoint\_organization](SearchParameter-endpoint-organization.html), [Plannet\_sp\_healthcareservice\_category](SearchParameter-healthcareservice-service-category.html), [Plannet\_sp\_healthcareservice\_coverage\_area](SearchParameter-healthcareservice-coverage-area.html), [Plannet\_sp\_healthcareservice\_delivery\_method](SearchParameter-healthcareservice-delivery-method.html), [Plannet\_sp\_healthcareservice\_endpoint](SearchParameter-healthcareservice-endpoint.html), [Plannet\_sp\_healthcareservice\_location](SearchParameter-healthcareservice-location.html), [Plannet\_sp\_healthcareservice\_name](SearchParameter-healthcareservice-name.html), [Plannet\_sp\_healthcareservice\_organization](SearchParameter-healthcareservice-organization.html), [Plannet\_sp\_healthcareservice\_specialty](SearchParameter-healthcareservice-specialty.html), [Plannet\_sp\_healthcareservice\_type](SearchParameter-healthcareservice-service-type.html), [Plannet\_sp\_insuranceplan\_administered\_by](SearchParameter-insuranceplan-administered-by.html), [Plannet\_sp\_insuranceplan\_coverage\_area](SearchParameter-insuranceplan-coverage-area.html), [Plannet\_sp\_insuranceplan\_identifier](SearchParameter-insuranceplan-identifier.html), [Plannet\_sp\_insuranceplan\_name](SearchParameter-insuranceplan-name.html), [Plannet\_sp\_insuranceplan\_network](SearchParameter-insuranceplan-network.html), [Plannet\_sp\_insuranceplan\_owned\_by](SearchParameter-insuranceplan-owned-by.html), [Plannet\_sp\_insuranceplan\_plan\_type](SearchParameter-insuranceplan-plan-type.html), [Plannet\_sp\_insuranceplan\_type](SearchParameter-insuranceplan-type.html), [Plannet\_sp\_location\_address](SearchParameter-location-address.html), [Plannet\_sp\_location\_address\_city](SearchParameter-location-address-city.html), [Plannet\_sp\_location\_address\_postalcode](SearchParameter-location-address-postalcode.html), [Plannet\_sp\_location\_address\_state](SearchParameter-location-address-state.html), [Plannet\_sp\_location\_endpoint](SearchParameter-location-endpoint.html), [Plannet\_sp\_location\_organization](SearchParameter-location-organization.html), [Plannet\_sp\_location\_partof](SearchParameter-location-partof.html), [Plannet\_sp\_location\_type](SearchParameter-location-type.html), [Plannet\_sp\_network\_coverage\_area](SearchParameter-organization-coverage-area.html), [Plannet\_sp\_organization\_address](SearchParameter-organization-address.html), [Plannet\_sp\_organization\_endpoint](SearchParameter-organization-endpoint.html), [Plannet\_sp\_organization\_name](SearchParameter-organization-name.html), [Plannet\_sp\_organization\_partof](SearchParameter-organization-partof.html), [Plannet\_sp\_organization\_period](SearchParameter-organization-period.html), [Plannet\_sp\_organization\_type](SearchParameter-organization-type.html), [Plannet\_sp\_organizationaffiliation\_endpoint](SearchParameter-organizationaffiliation-endpoint.html), [Plannet\_sp\_organizationaffiliation\_location](SearchParameter-organizationaffiliation-location.html), [Plannet\_sp\_organizationaffiliation\_network](SearchParameter-organizationaffiliation-network.html), [Plannet\_sp\_organizationaffiliation\_participating\_organization](SearchParameter-organizationaffiliation-participating-organization.html), [Plannet\_sp\_organizationaffiliation\_period](SearchParameter-organizationaffiliation-period.html), [Plannet\_sp\_organizationaffiliation\_primary\_organization](SearchParameter-organizationaffiliation-primary-organization.html), [Plannet\_sp\_organizationaffiliation\_role](SearchParameter-organizationaffiliation-role.html), [Plannet\_sp\_organizationaffiliation\_service](SearchParameter-organizationaffiliation-service.html), [Plannet\_sp\_organizationaffiliation\_specialty](SearchParameter-organizationaffiliation-specialty.html), [Plannet\_sp\_practitioner\_family\_name](SearchParameter-practitioner-family-name.html), [Plannet\_sp\_practitioner\_given\_name](SearchParameter-practitioner-given-name.html), [Plannet\_sp\_practitioner\_name](SearchParameter-practitioner-name.html), [Plannet\_sp\_practitioner\_period](SearchParameter-practitioner-period.html), [Plannet\_sp\_practitionerrole\_endpoint](SearchParameter-practitionerrole-endpoint.html), [Plannet\_sp\_practitionerrole\_location](SearchParameter-practitionerrole-location.html), [Plannet\_sp\_practitionerrole\_network](SearchParameter-practitionerrole-network.html), [Plannet\_sp\_practitionerrole\_organization](SearchParameter-practitionerrole-organization.html), [Plannet\_sp\_practitionerrole\_period](SearchParameter-practitionerrole-period.html), [Plannet\_sp\_practitionerrole\_practitioner](SearchParameter-practitionerrole-practitioner.html), [Plannet\_sp\_practitionerrole\_role](SearchParameter-practitionerrole-role.html), [Plannet\_sp\_practitionerrole\_service](SearchParameter-practitionerrole-service.html), [Plannet\_sp\_practitionerrole\_specialty](SearchParameter-practitionerrole-specialty.html), [PractitionerPeriod](StructureDefinition-practitioner-period.html), [PractitionerQualification](StructureDefinition-practitioner-qualification.html), [PractitionerRoleVS](ValueSet-PractitionerRoleVS.html), [ProviderRoleCS](CodeSystem-ProviderRoleCS.html), [Qualification](StructureDefinition-qualification.html), [QualificationStatusCS](CodeSystem-QualificationStatusCS.html), [QualificationStatusVS](ValueSet-QualificationStatusVS.html), [SpecialtiesVS](ValueSet-SpecialtiesVS.html), [SpecialtyAndDegreeLicenseCertificateVS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html), [ViaIntermediary](StructureDefinition-via-intermediary.html), [VirtualModalitiesCS](CodeSystem-VirtualModalitiesCS.html) and [VirtualModalitiesVS](ValueSet-VirtualModalitiesVS.html)
* This material derives from the HL7 Terminology (THO). THO is copyright ©1989+ Health Level Seven International and is made available under the CC0 designation. For more licensing information see: <https://terminology.hl7.org/license.html> Show Usage
  + [Endpoint Connection Type](http://terminology.hl7.org/6.1.0/CodeSystem-endpoint-connection-type.html): [EndpointConnectionTypeVS](ValueSet-EndpointConnectionTypeVS.html), [MinEndpointConnectionTypeVS](ValueSet-MinEndpointConnectionTypeVS.html) and [PlannetEndpoint](StructureDefinition-plannet-Endpoint.html)
  + [Practitioner role](http://terminology.hl7.org/6.1.0/CodeSystem-practitioner-role.html): [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html) and [PractitionerRoleVS](ValueSet-PractitionerRoleVS.html)
  + [Service type](http://terminology.hl7.org/6.1.0/CodeSystem-service-type.html): [HealthcareServiceTypeVS](ValueSet-HealthcareServiceTypeVS.html) and [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html)
  + [ActReason](http://terminology.hl7.org/6.1.0/CodeSystem-v3-ActReason.html): [Endpoint for Acme of CT Portal](Endpoint-AcmeOfCTPortalEndpoint.html), [EndpointUsecase](StructureDefinition-endpoint-usecase.html) and [EndpointUsecaseVS](ValueSet-EndpointUsecaseVS.html)
  + [RoleCode](http://terminology.hl7.org/6.1.0/CodeSystem-v3-RoleCode.html): [Cancer Clinic](Location-CancerClinicLoc.html), [Hartford Hospital Location 1](Location-HospLoc1.html)... Show 5 more, [Hartford Hospital Location 2](Location-HospLoc2.html), [OrgA CT Location 1](Location-PharmLoc1.html), [OrgA CT Location 2](Location-PharmLoc2.html), [OrgA MA Location 1](Location-PharmLoc3.html) and [OrgA MA Location 2](Location-PharmLoc4.html)

| [<prev](toc.html) | [top](#top) | [next>](background.html) |
| --- | --- | --- |

IG © 2025+ [HL7 International / Financial Management](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.2.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2025-02-25

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |

[Propose a change](http://hl7.org/fhir-issues)