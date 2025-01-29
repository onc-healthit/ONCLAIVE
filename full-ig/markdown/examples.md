xml version\="1\.0" encoding\="UTF\-8"?

HL7\.FHIR.US.DAVINCI\-PDEX\-PLAN\-NET\\Examples \- FHIR v4\.0\.1

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
* **Examples**

This page is part of the DaVinci PDEX Plan Net (v1\.1\.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1\) based on [FHIR R4](http://hl7.org/fhir/R4). This is the current published version. For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html)

## Examples

### Examples Table

| **Example** | **ResourceType** | **Profiles** |
| --- | --- | --- |
| [AcmeOfCTPortalEndpoint](Endpoint-AcmeOfCTPortalEndpoint.html) | [Endpoint](http://hl7.org/fhir/R4/endpoint.html) | [PlannetEndpoint](StructureDefinition-plannet-Endpoint.html) |
| [BurrClinicServices](HealthcareService-BurrClinicServices.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [CancerClinicService](HealthcareService-CancerClinicService.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [HamiltonClinicServices](HealthcareService-HamiltonClinicServices.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [HansSoloService](HealthcareService-HansSoloService.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [HartfordOrthopedicServices](HealthcareService-HartfordOrthopedicServices.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [HospERService](HealthcareService-HospERService.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [PharmChainCompService](HealthcareService-PharmChainCompService.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [PharmChainMailService](HealthcareService-PharmChainMailService.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [PharmChainRetailService](HealthcareService-PharmChainRetailService.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [VirtualCounselService](HealthcareService-VirtualCounselService.html) | [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html) | [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html) |
| [AcmeQHPBronze](InsurancePlan-AcmeQHPBronze.html) | [InsurancePlan](http://hl7.org/fhir/R4/insuranceplan.html) | [PlannetInsurancePlan](StructureDefinition-plannet-InsurancePlan.html) |
| [AcmeQHPGold](InsurancePlan-AcmeQHPGold.html) | [InsurancePlan](http://hl7.org/fhir/R4/insuranceplan.html) | [PlannetInsurancePlan](StructureDefinition-plannet-InsurancePlan.html) |
| [CancerClinicLoc](Location-CancerClinicLoc.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [HansSoloClinic](Location-HansSoloClinic.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [HospLoc1](Location-HospLoc1.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [HospLoc2](Location-HospLoc2.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [PharmLoc1](Location-PharmLoc1.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [PharmLoc2](Location-PharmLoc2.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [PharmLoc3](Location-PharmLoc3.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [PharmLoc4](Location-PharmLoc4.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [StateOfCTLocation](Location-StateOfCTLocation.html) | [Location](http://hl7.org/fhir/R4/location.html) | [PlannetLocation](StructureDefinition-plannet-Location.html) |
| [AcmeofCTPremNet](Organization-AcmeofCTPremNet.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetNetwork](StructureDefinition-plannet-Network.html) |
| [AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetNetwork](StructureDefinition-plannet-Network.html) |
| [Acme](Organization-Acme.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [BigBox](Organization-BigBox.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [BurrClinic](Organization-BurrClinic.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [CancerClinic](Organization-CancerClinic.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [ConnHIE](Organization-ConnHIE.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [HamiltonClinic](Organization-HamiltonClinic.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [HartfordOrthopedics](Organization-HartfordOrthopedics.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [Hospital](Organization-Hospital.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [PharmChain](Organization-PharmChain.html) | [Organization](http://hl7.org/fhir/R4/organization.html) | [PlannetOrganization](StructureDefinition-plannet-Organization.html) |
| [BurrClinicAffil](OrganizationAffiliation-BurrClinicAffil.html) | [OrganizationAffiliation](http://hl7.org/fhir/R4/organizationaffiliation.html) | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) |
| [ConnHIEAffil](OrganizationAffiliation-ConnHIEAffil.html) | [OrganizationAffiliation](http://hl7.org/fhir/R4/organizationaffiliation.html) | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) |
| [HamiltonClinicAffil](OrganizationAffiliation-HamiltonClinicAffil.html) | [OrganizationAffiliation](http://hl7.org/fhir/R4/organizationaffiliation.html) | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) |
| [HartfordOrthopedicAffil](OrganizationAffiliation-HartfordOrthopedicAffil.html) | [OrganizationAffiliation](http://hl7.org/fhir/R4/organizationaffiliation.html) | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) |
| [PharmChainAffil1](OrganizationAffiliation-PharmChainAffil1.html) | [OrganizationAffiliation](http://hl7.org/fhir/R4/organizationaffiliation.html) | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) |
| [PharmChainAffil2](OrganizationAffiliation-PharmChainAffil2.html) | [OrganizationAffiliation](http://hl7.org/fhir/R4/organizationaffiliation.html) | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) |
| [PharmChainAffil3](OrganizationAffiliation-PharmChainAffil3.html) | [OrganizationAffiliation](http://hl7.org/fhir/R4/organizationaffiliation.html) | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) |
| [Counselor](Practitioner-Counselor.html) | [Practitioner](http://hl7.org/fhir/R4/practitioner.html) | [PlannetPractitioner](StructureDefinition-plannet-Practitioner.html) |
| [HansSolo](Practitioner-HansSolo.html) | [Practitioner](http://hl7.org/fhir/R4/practitioner.html) | [PlannetPractitioner](StructureDefinition-plannet-Practitioner.html) |
| [JoeSmith](Practitioner-JoeSmith.html) | [Practitioner](http://hl7.org/fhir/R4/practitioner.html) | [PlannetPractitioner](StructureDefinition-plannet-Practitioner.html) |
| [AnonRole](PractitionerRole-AnonRole.html) | [PractitionerRole](http://hl7.org/fhir/R4/practitionerrole.html) | [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html) |
| [CounselorRole1](PractitionerRole-CounselorRole1.html) | [PractitionerRole](http://hl7.org/fhir/R4/practitionerrole.html) | [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html) |
| [HansSoloRole1](PractitionerRole-HansSoloRole1.html) | [PractitionerRole](http://hl7.org/fhir/R4/practitionerrole.html) | [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html) |
| [JoeSmithRole1](PractitionerRole-JoeSmithRole1.html) | [PractitionerRole](http://hl7.org/fhir/R4/practitionerrole.html) | [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html) |
| [JoeSmithRole2](PractitionerRole-JoeSmithRole2.html) | [PractitionerRole](http://hl7.org/fhir/R4/practitionerrole.html) | [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html) |
| [JoeSmithRole3](PractitionerRole-JoeSmithRole3.html) | [PractitionerRole](http://hl7.org/fhir/R4/practitionerrole.html) | [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html) |

 IG © 2022\+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7\.fhir.us.davinci\-pdex\-plan\-net\#1\.1\.0 based on [FHIR 4\.0\.1](http://hl7.org/fhir/R4/). Generated 2022\-04\-04

 Links: [Table of Contents](toc.html) \|
 [QA Report](qa.html)

 \| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) \|
 [![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) \|

[Propose a change](http://hl7.org/fhir-issues)