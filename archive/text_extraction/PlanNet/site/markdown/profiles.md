xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Profiles - FHIR v4.0.1

[![Visit the HL7 website](assets/images/hl7-logo-header.png)](http://hl7.org)

[![Visit the FHIR website](assets/images/fhir-logo-www.png)](http://hl7.org/fhir) 

[![Search FHIR](assets/images/search.png)](searchform.html)

[![Visit the Da Vinci website](assets/images/da-vinci_logo.jpg)](http://hl7.org/about/davinci) 

DaVinci PDEX Plan Net

1.1.0 - STU 1.1
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
* **Profiles**

This page is part of the DaVinci PDEX Plan Net (v1.1.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1) based on [FHIR R4](http://hl7.org/fhir/R4). This is the current published version. For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html)

## Profiles

### Profiles defined as part of this Implementation Guide

| **Name** | **Based On** | **Definition** |
| --- | --- | --- |
| [PlannetEndpoint](StructureDefinition-plannet-Endpoint.html) | [Endpoint (R4)](http://hl7.org/fhir/R4/endpoint.html) | The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information. |
| [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) | [HealthcareService (R4)](http://hl7.org/fhir/R4/healthcareservice.html) | The HealthCareService resource typically describes services offered by an organization/practitioner at a location. The resource may be used to encompass a variety of services covering the entire healthcare spectrum, including promotion, prevention, diagnostics, hospital and ambulatory care, home care, long-term care, and other health-related and community services. |
| [PlannetInsurancePlan](StructureDefinition-plannet-InsurancePlan.html) | [InsurancePlan (R4)](http://hl7.org/fhir/R4/insuranceplan.html) | An InsurancePlan is a discrete package of health insurance coverage benefits that are offered under a particular network type. A given payer’s products typically differ by network type and/or covered benefits. A plan pairs a product’s covered benefits with the particular cost sharing structure offered to a consumer. A given product may comprise multiple plans (i.e. each plan offers different cost sharing requirements for the same set of covered benefits).  InsurancePlan describes a health insurance offering comprised of a list of covered benefits (i.e. the product), costs associated with those benefits (i.e. the plan), and additional information about the offering, such as who it is owned and administered by, a coverage area, contact information, etc. |
| [PlannetLocation](StructureDefinition-plannet-Location.html) | [Location (US Core)](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-location.html) | A Location is the physical place where healthcare services are provided, practitioners are employed, organizations are based, etc. Locations can range in scope from a room in a building to a geographic region/area. |
| [PlannetNetwork](StructureDefinition-plannet-Network.html) | [Organization (US Core)](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-organization.html) | A Network refers to a healthcare provider insurance network. A healthcare provider insurance network is an aggregation of organizations and individuals that deliver a set of services across a geography through health insurance products/plans. A network is typically owned by a payer.  In the PlanNet IG, individuals and organizations are represented as participants in a PLan-Net Network through the practitionerRole and Plan-Net-organizationAffiliation resources, respectively. |
| [PlannetOrganization](StructureDefinition-plannet-Organization.html) | [Organization (US Core)](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-organization.html) | An organization is a formal or informal grouping of people or organizations with a common purpose, such as a company, institution, corporation, community group, or healthcare practice. |
| [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) | [OrganizationAffiliation (R4)](http://hl7.org/fhir/R4/organizationaffiliation.html) | The OrganizationAffiliation resource describes relationships between two or more organizations, including the services one organization provides another, the location(s) where they provide services, the availability of those services, electronic endpoints, and other relevant information. |
| [PlannetPractitioner](StructureDefinition-plannet-Practitioner.html) | [Practitioner (US Core)](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-practitioner.html) | Practitioner is a person who is directly or indirectly involved in the provisioning of healthcare. |
| [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html) | [PractitionerRole (R4)](http://hl7.org/fhir/R4/practitionerrole.html) | PractitionerRole describes the role a practitioner plays at an organization, including the services they provide, the location(s) where they work, and their availability, electronic endpoints, and other relevant information. |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |

[Propose a change](http://hl7.org/fhir-issues)