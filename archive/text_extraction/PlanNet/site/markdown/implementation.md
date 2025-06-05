xml version="1.0" encoding="UTF-8"?

Implementation - Da Vinci PDex Plan Net v1.2.0

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
* **Implementation**
[<prev](examples.html) |
[bottom](#bottom)
| [next>](project.html)

This page is part of the DaVinci PDEX Plan Net (v1.2.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1) based on [FHIR (HL7® FHIR® Standard) R4](http://hl7.org/fhir/R4). This is the current published version. For a full list of available versions, see the [Directory of published versions](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html)

## Implementation

| *Page standards status:* [Informative](http://hl7.org/fhir/R4/versions.html#std-process "Standard Status") |
| --- |

* [Bulk Data](#bulk-data)
### Implementation Notes

This page contains miscellaneous information on FHIR implementation. The content is primarily directed at implementers of Plan-Net.

#### Conformance Requirements

The conformance verbs (**SHALL**, **SHALL NOT,****SHOULD**, **MAY**) used in this guide are defined in [FHIR Conformance Rules](http://hl7.org/fhir/R4/conformance-rules.html).

#### Privacy Considerations

Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried.

A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content.

A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service.

#### Client Detection of Updates Directory Content

Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content.  Clients that cache query results can track additions or modifications to directory content through queries that filter content using the \_lastUpdated search parameter.  Clients should periodically check that data cached from past queries has not been deleted by querying for the same elements by \_id.

#### General Security Considerations

**NO CONTENT**

### Representing and Searching Provider Directory Data

It is important for payers to use the Plan-Net profiles consistently in order to achieve true interoperability of directory information among payers. The intent of this section is to provide examples of the canonical use of the profiles provided in this IG that will guide implementers towards the consistent use of these profiles that will enable 3rd party applications to search the data.  The Plan-Net design is based around the following types of searches.

| **Search** | **Example** | **Focal  Resource and Field** | **Qualifications of Search** |
| --- | --- | --- | --- |
| General Search | Pharmacy | HealthcareService.category, HealthcareService.specialty | Location, network |
| Provider by Name | Joe Smith | Practitioner.name | Location, network, specialty, role/privileges |
| Organization by Name | Montgomery Cardiology or CVS | Organization.name | Location, network, specialty |
| Provider by Specialty | Cardiologist | PractitionerRole.specialty | Location, network, name |
| Organization by Specialty | Compounding Pharmacy | OrganizationAffiliation.specialty | Location, network, name |

The content in this section of the IG is based on the [examples](artifacts.html) provided and on the patterns provided [here](patterns.pptx).  
Specific examples are referenced in the text below.

#### Searching for active Practictioners and Organizations

Sample query to search for currently active Practitioners (replace date in query with current date):  

http://davinci-plan-net-ri.logicahealth.org/fhir/PractitionerRole?\_include=PractitionerRole:date=ge2021-10-25   

Sample query to search for currently active Organizations (replace date in query with current date):   

http://davinci-plan-net-ri.logicahealth.org/fhir/OrganizationAffiliation?\_include=OrganizationAffiliation:date=ge2021-10-25   

To search for Practitioners or Organizations that will be active at a future time, change the date to a future date.  

If no period is provided, then it is assumend the role is active with no expiration date.

#### HealthcareService

The first type of search starts from HealthcareService.category and HealthcareService.specialty, so it is essential that each provider's service be supported by appropriate set of HealthcareService instances.  HealthcareServices are typically provided by an organization, except in the case of a Practitioner that is not associated with an organization (see the solo practitioner example), and can be linked to a set of locations where service is provided, or identified as virtual services through an indicated set of virtual modalities.   The examples illustrate this with an organization that provides three distinct Pharmacy services -- retail, compounding, and mail-order -- across its locations.  All organizations that provide service should define an appropriate set. of HealthcareServices to facilitate search.  The HealthcareService category, specialty and type fields are the highest level of organization of the services provided by the provider's network.

Relevant examples:

| Scenario | Example Instances |
| --- | --- |
| Retail Pharmacy Chain | [PharmChainRetailService](HealthcareService-PharmChainRetailService.html "HealthcareService/PharmChainRetailService") |
| Compounding Pharmacy | [PharmChainCompService](HealthcareService-PharmChainCompService.html "HealthcareService/PharmChainCompService") |
| Mail Order Pharmacy (virtual service with no physical location) | [PharmChainMailService](HealthcareService-PharmChainMailService.html "HealthcareService/PharmChainMailService") |
| Provider Group | [HartfordOrthopedicServices](HealthcareService-HartfordOrthopedicServices.html "HealthcareService/HartfordOrthopedicServices") |
| Emergency Room | [HospERService](HealthcareService-HospERService.html "HealthcareService/HospERService") |
| Cancer Clinic | [CancerClinicService](HealthcareService-CancerClinicService.html "HealthcareService/CancerClinicService") |
| Virtual Counseling Service | [VirtualCounselService](HealthcareService-VirtualCounselService.html) |
| Solo Family Practitioner | [HansSoloService](HealthcareService-HansSoloService.html) |

#### Insurance Plan and Network

Each payer will offer one or more products -- Insurance Plans -- and each plan is associated with one or more Networks.  Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively.   PractitionerRole and OrganizationAffiliation instances are what tie Practitioners and Organizations to HealthcareServices, Organizations, Networks and Locations.

The examples demonstrate the use of the InsurancePlan profile to represent two distinct Qualified Health Plan products covering the state of Connecticut, using a pair of Networks.  The practitioners and organizations in the examples participate in one or both of these networks.

Relevant examples:

| Scenario | Example Instances |
| --- | --- |
| Insurance Company | [Acme](Organization-Acme.html "Organization/Acme") |
| QHP Gold Plan with two networks | [AcmeQHPGold](InsurancePlan-AcmeQHPGold.html "InsurancePlan/AcmeQHPGold") |
| QHP Bronze plan with one network | [AcmeQHPBronze](InsurancePlan-AcmeQHPBronze.html "InsurancePlan/AcmeQHPBronze") |
| Standard Network | [AcmeofCTStdNet](Organization-AcmeofCTStdNet.html "Organization/AcmeofCTStdNet") |
| Premium Network | [AcmeofCTPremNet](Organization-AcmeofCTPremNet.html "Organization/AcmeofCTPremNet") |

#### Location

Location instances provide information about location where service is provided, including contact information, address, accessibility, hours of operation and contact, as well as position (lattitude and longitude).   Locations can also be used to represent regions using an associated or attached GeoJSON object.

Relevant examples:

| Scenario | Example Instances |
| --- | --- |
| Hospital Location #1 | [HospLoc1](Location-HospLoc1.html "Location/HospLoc1") |
| Hospital Location #2 | [HospLoc2](Location-HospLoc2.html "Location/HospLoc2") |
| Pharmacy Location #1 .  Shows newpatient,accessibliity, and contactpoint-availabletime extensions | [PharmLoc1](Location-PharmLoc1.html "Location/PharmLoc1") |
| Pharmacy Location #2 | [PharmLoc2](Location-PharmLoc2.html "Location/PharmLoc2") |
| Location used as CoverageArea | [StateOfCTLocation](Location-StateOfCTLocation.html "Location/StateOfCTLocation") |

#### Practitioners and PractitionerRoles

Practitioner instances provide information about a specific person, including name, gender, languages spoken, and qualifications.   PractitionerRole defines a role for a particular practitioner, and associates it with locations, specialties, an organization, and networks.

| Scenario | Example Instances |
| --- | --- |
| Solo Practitioner (no organization) | [HansSolo](Practitioner-HansSolo.html "Practitioner/HansSolo"), [HansSoloRole1](PractitionerRole-HansSoloRole1.html "PractitionerRole/HansSoloRole1"), [HansSoloService](HealthcareService-HansSoloService.html "HealthcareService/HansSoloService") |
| Anonymous role (not associated with a specific practitioner) | [AnonRole](PractitionerRole-AnonRole.html "PractitionerRole/AnonRole") |
| Physician working at a provider group | [JoeSmith](Practitioner-JoeSmith.html "Practitioner/JoeSmith")[, JoeSmithRole2](PractitionerRole-JoeSmithRole2.html "PractitionerRole/JoeSmithRole2") |
| Physician with admitting privileges | [JoeSmith](Practitioner-JoeSmith.html "Practitioner/JoeSmith")[, JoeSmithRole3](PractitionerRole-JoeSmithRole3.html "PractitionerRole/JoeSmithRole3") |
| Physician working at a hospital | [JoeSmith](Practitioner-JoeSmith.html "Practitioner/JoeSmith")[, JoeSmithRole1](PractitionerRole-JoeSmithRole1.html "PractitionerRole/JoeSmithRole1") |
| Counselor working virtually | [CounselorRole1](PractitionerRole-CounselorRole1.html) |

#### Organizations and Organization Affiliations

Organization instances provide information about a specific organization and organizational hierarchies, including organization name, specialty, type, address and contact information.  Organization Affiliation instances describe a role, and link a participating organization that provides or performs the role, with an organization where that role is available, and also links the participating organization to a HealthcareServices and networks.  OrganizationalAffiliation can also be used to associate a HealthcareService provided by an organization with networks.

| Scenario | Example Instances |
| --- | --- |
| Pharmacy services are associated with a specific provider network | [PharmChain](Organization-PharmChain.html "Organization/PharmChain"), [PharmChainAffil1](OrganizationAffiliation-PharmChainAffil1.html "OrganizationAffiliation/PharmChainAffil1"), [PharmChainAffil1](OrganizationAffiliation-PharmChainAffil2.html "OrganizationAffiliation/PharmChainAffil2"), [PharmChainAffil1](OrganizationAffiliation-PharmChainAffil3.html "OrganizationAffiliation/PharmChainAffil3") |
| Clinic Providing Service to a Hospital | [BurrClinic](Organization-BurrClinic.html "Organization/BurrClinic"), [BurrClinicAffil,](OrganizationAffiliation-BurrClinicAffil.html "OrganizationAffiliation/BurrClinicAffil")[Hospital](Organization-Hospital.html "Organization/Hospital") |
| Clinic that is part of a Hospital | [HamiltonClinic](Organization-HamiltonClinic.html "Organization/HamiltonClinic"), [HamiltonClinicAffil,](OrganizationAffiliation-HamiltonClinicAffil.html "OrganizationAffiliation/HamiltonClinicAffil")[Hospital](Organization-Hospital.html "Organization/Hospital") |
| Specialty group providing service to a network at hospital | [HartfordOrthopedics](Organization-HartfordOrthopedics.html "Organization/HartfordOrthopedics"), [HartfordOrthopedicAffil,](OrganizationAffiliation-HartfordOrthopedicAffil.html "OrganizationAffiliation/HartfordOrthopedicAffil")[Hospital](Organization-Hospital.html "Organization/Hospital") |
| Clinic that is a member of a regional HIE | [BurrClinic](Organization-BurrClinic.html "Organization/BurrClinic"), [ConnHIE](Organization-ConnHIE.html "Organization/ConnHIE"), [ConnHIEAffil](OrganizationAffiliation-ConnHIEAffil.html "OrganizationAffiliation/ConnHIEAffil") |

#### Endpoints

An Endpoint instance provides  technical details of an endpoint that can be used for electronic services, such as a portal or FHIR REST services, messaging or operations, or DIRECT messaging.

| Scenario | Example Instances |
| --- | --- |
| Payer Portal | [AcmeOfCTPortalEndpoint](Endpoint-AcmeOfCTPortalEndpoint.html "Endpoint/AcmeOfCTPortalEndpoint") |

### Bulk Data

Bulk data guidance in this version of the IG is draft only. It has not appeared in ballot and has not been fully tested.</i></b>

A server **MAY** support [Bulk Data IG](http://hl7.org/fhir/uv/bulkdata/index.html) for the retrieval of directory data.
If and how authorization is supported is not defined by this specification, however, the Bulk IG does provide guidance on SMART Backend Service Authorization.

In the future, this IG will likely align bulk data support with the [National Directory Bulk Data implementation section](https://build.fhir.org/ig/HL7/fhir-us-ndh/ndapi-ig.html#bulk-data-export-of-the-national-directory), but that is currently unpublished.

| [<prev](examples.html) | [top](#top) | [next>](project.html) |
| --- | --- | --- |

IG © 2025+ [HL7 International / Financial Management](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.2.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2025-02-25

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |

[Propose a change](http://hl7.org/fhir-issues)