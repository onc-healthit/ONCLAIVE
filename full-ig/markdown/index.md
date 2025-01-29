xml version\="1\.0" encoding\="UTF\-8"?

HL7\.FHIR.US.DAVINCI\-PDEX\-PLAN\-NET\\Home \- FHIR v4\.0\.1

[![Visit the HL7 website](assets/images/hl7-logo-header.png)](http://hl7.org)

[![Visit the FHIR website](assets/images/fhir-logo-www.png)](http://hl7.org/fhir) 

[![Search FHIR](assets/images/search.png)](searchform.html)

[![Visit the Da Vinci website](assets/images/da-vinci_logo.jpg)](http://hl7.org/about/davinci) 

DaVinci PDEX Plan Net

1\.1\.0 \- STU 1\.1

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
* **Home**

This page is part of the DaVinci PDEX Plan Net (v1\.1\.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1\) based on [FHIR R4](http://hl7.org/fhir/R4). This is the current published version. For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html)

## Home

| *Official URL*: http://hl7\.org/fhir/us/davinci\-pdex\-plan\-net/ImplementationGuide/hl7\.fhir.us.davinci\-pdex\-plan\-net | | | | *Version*:  1\.1\.0 |
| --- | --- | --- | --- | --- |
| Active    as of 2022\-04\-04 | | | | *Computable Name*: DaVinciPDEXPlanNet |

### PDEX Payer Network Implementation Guide

#### Introduction

This implementation guide defines a FHIR interface to a health insurer’s insurance plans, their associated networks, and the organizations and providers that participate in these networks. Publication of this data through a standard FHIR\-based API will enable third parties to develop applications through which consumers and providers can query the participants in a payer’s network that may provide services that address their health care needs. Although there are multiple types and sources of providers’ directories, including provider organizations (i.e., a hospital listing all its physicians), government (i.e., listing of providers in Medicare), payers (i.e., a health plan’s provider network), and third\-party entities (such as vendors that maintain provider directories), the focus of this implementation guide is on Payer Provider Directories.

The PDEX Payer Network (or Plan\-Net) Implementation Guide is based conceptually on the [Validated Healthcare Directory Implementation Guide (VHDir IG)](http://hl7.org/fhir/uv/vhdir/2018Sep/index.html), an international standard. The VHDir IG is based on [FHIR Version 4\.0](http://hl7.org/fhir/R4/index.html). It was developed in cooperation with the [Office of the National Coordinator for Health Information Technology (ONC)](http://www.healthit.gov/newsroom/about-onc) and [Federal Health Architecture (FHA)](https://www.healthit.gov/policy-researchers-implementers/federal-health-architecture-fha) with guidance from HL7 International, the Patient Administration Workgroup, and the HL7 US Realm Steering Committee.

The use of VhDir as the conceptual base for the profiles and extensions in the PDEX Payer Network Implementation Guide is intended to protect implementers of the Plan\-Net IG from rework/remapping when the VHDir concept reaches implementation, and becomes a source of data for the PDEX Payer Network. The primary changes from the VHDir IG are to:

1. remove the validation and restriction resources
2. use US Core for R4 as the base suite of profiles where possible
3. eliminate extensions that are not necessary for this use case
4. introduce additional constraints (e.g. search criteria, cardinality, value\-set bindings and MustSupport) where appropriate.

The diagram below depicts the scope of this implementation guide (IG). The IG defines the API that exposes a payer’s provider network (including pharmacy locations where appropriate) for access by a consumer or provider application. This is a query only API (GET) and does not support PUT or POST.

![](Bob3.png)

#### Relation to US Core and other IGs

This implementation guide was written for a US audience and profiles resources from [US Core STU 4](http://hl7.org/fhir/us/core/STU3.1.1/index.html), where available (Practitioner, Organization and Location), and otherwise from R4 (OrganizationAffiliation, PractitionerRole, HealthCareService, Endpoint). The PractitionerRole profile from US Core was not used because it is over\-constrained for use in a Provider Directory based on Payer information. The Network profile is based on USCore Organization, since there was no contradiction between the USCore profile and the Plan\-Net requirements. However, the NPI and CLIA identifier types, which are Must\-Support, are clearly intended for provider organizations only and are not expected to be populated for other organization types. Alignment with VhDir is maintained by adapting VhDir content, where possible.

#### Disclaimers and Assumptions

* **PDEX Payer Network is based conceptually on VhDir**: The PDEX Payer Network implementation guide is based conceptually on the VhDir implementation guide, which is still a work in progress. Plan\-net will need to track changes to VhDir to fulfill its goal of minimizing rework.
* **The PDEX Payer Network endpoint is known to the client**: This implementation guide assumes that the directory endpoint is known to the client. There is an overarching system architecture issue that is critical to resolve \-\- how does the client discover the FHIR endpoint of interest. For the purposes of this IG, we consider that problem out of scope.

#### Background

Provider directories play a critical role in enabling identification of individual providers and provider organizations, as well as characteristics about them. Provider directories support a variety of use cases, including:

* Patient/Payer focused
+ Find provider accessibility information (specialty, office hours, languages spoken, taking patients) \- enables individuals and consumers to find contact and other accessibility information for individual healthcare providers and/or healthcare organizations
+ Relationship between provider and insurance plan (insurance accepted) or plan and provider (network) \- enables individual healthcare providers, organizations, and payers to discover the relationships between providers, organizations, and payers, as well as additional details about the relationships and entities involved

* Basic Information Exchange
+ Enable electronic exchange (e.g. discovery of electronic endpoints such as IHE/EHR endpoints, FHIR server URLs, Direct addresses) \- enables the electronic exchange of health information by supporting the ability to discover electronic service information including electronic endpoints or electronic addresses
+ Find an individual and/or organization (even if no electronic endpoint is available) \- enables users to find contact and other identifying information about healthcare organizations and individual healthcare providers

This IG addresses two actors:

* Health Plan API Actor: A payer publishing a directory of its provider networks through a FHIR endpoint.
* Application Actor: A third party using the API published by a payer to provide useful views of the payer's provider networks for end users.

For anticipated query use cases, please see [Representing and Searching Provider Data](implementation.html#Representing).

#### Overview of Payer Directory \- Resource Relationships

Note: the following diagrams provide a high\-level view of the relationships between resources used in this IG. They do not necessarily reflect all of the relationships/references between resources.

![Key Relationships Among Payer Directory Resources](Slide2.png)
![Relationships Between Payer Directory Resources -- Endpoints](Slide3.png)

#### Credits

This IG was developed by the MITRE Corporation under the direction of the authors using [FHIR Shorthand syntax](https://build.fhir.org/ig/HL7/fhir-shorthand/) and the [SUSHI tookit](https://github.com/FHIR/sushi), a free, open source toolchain from the MITRE Corporation. Generous guidance on FHIR Shorthand and SUSHI was provided by Chris Moesel. The capability statements were developed with support of tools and generous guidance from Eric Haas, and benefited from critical review by Yengibar Manasyan.

#### Authors

| Name | Email |
| --- | --- |
| Troy Bergstrand | Troy.Bergstrand@bcidaho.com |
| Laurie Burckhardt | Laurie.Burckhardt@wpsic.com |
| Bob Dieterle | rdieterle@enablecare.us |
| Gail Kocher | Gail.Kocher@bcbsa.com |
| Saul A. Kravitz | saul@mitre.org |
| Robert McClure MD | rmcclure@mdpartners.com |
| Mary Kay McDaniel | MaryKay.McDaniel@cognosante.com |
| Sean Mahoney | smahoney@mitre.org |
| Corey Spears | cspears@mitre.org |

 IG © 2022\+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7\.fhir.us.davinci\-pdex\-plan\-net\#1\.1\.0 based on [FHIR 4\.0\.1](http://hl7.org/fhir/R4/). Generated 2022\-04\-04

 Links: [Table of Contents](toc.html) \|
 [QA Report](qa.html)

 \| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) \|
 [![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) \|

[Propose a change](http://hl7.org/fhir-issues)