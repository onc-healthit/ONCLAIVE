xml version="1.0" encoding="UTF-8"?

Change History - Da Vinci PDex Plan Net v1.2.0

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
* **Change History**
[<prev](background.html) |
[bottom](#bottom)
| [next>](confexpectations.html)

This page is part of the DaVinci PDEX Plan Net (v1.2.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1) based on [FHIR (HL7® FHIR® Standard) R4](http://hl7.org/fhir/R4). This is the current published version. For a full list of available versions, see the [Directory of published versions](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html)

## Change History

| *Page standards status:* [Informative](http://hl7.org/fhir/R4/versions.html#std-process "Standard Status") |
| --- |

* [Changes and Updates for Version 1.2.0](#changes-and-updates-for-version-120)
* [Changes and Updates for Version 1.1.0](#changes-and-updates-for-version-110)
* [Changes and Updates for Version 1.0.0](#changes-and-updates-for-version-100)
* [Changes and Updates for Version 0.1.0](#changes-and-updates-for-version-010)
### Changes and Updates for Version 1.2.0

The following high level changes addressed in this release:

* Updated dependencies to reference to multiple versions of US Core per latest Da Vinci recommendations (7.0.0, 6.1.0, and 3.1.1)
* Updated dependencies to reference Da Vinci HRex version 1.1.0
* Updated IG organization and structure to match the latest Da Vinci recommendations

Specific JIRA tickets applied in this update are listed below:

* [FHIR-46786](https://jira.hl7.org/browse/FHIR-46786) SearchParameter with code `network`
* [FHIR-46353](https://jira.hl7.org/browse/FHIR-46353) Add capabilitystatement-expectation extensions to CapabilityStatement supportedProfile elements
* [FHIR-45635](https://jira.hl7.org/browse/FHIR-45635) DaVinci vs. Da Vinci for IG name/title/narrative
* [FHIR-45300](https://jira.hl7.org/browse/FHIR-45300) Retrieving Inactive or Terminated Provider Data Records through BULK FHIR API
* [FHIR-43796](https://jira.hl7.org/browse/FHIR-43796) PractitionerRole newpatients extension cardinality
* [FHIR-41844](https://jira.hl7.org/browse/FHIR-41844) Remove the requirement of meta.profile
* [FHIR-40923](https://jira.hl7.org/browse/FHIR-40923) Please remove value: 'OTHER' from Extensible Value Set: HealthcareServiceCategoryVS
* [FHIR-40824](https://jira.hl7.org/browse/FHIR-40824) Add operation for bulk export operation to US Da Vinci PDex Plan Net
* [FHIR-40806](https://jira.hl7.org/browse/FHIR-40806) Category shouldn't be constrained to only 1
* [FHIR-40592](https://jira.hl7.org/browse/FHIR-40592) Profile - Practitioner : Practitioner.qualification
* [FHIR-37680](https://jira.hl7.org/browse/FHIR-37680) Descriptive Paragraph on Plan-Net PractitionerRole problematic
* [FHIR-36473](https://jira.hl7.org/browse/FHIR-36473) Update specialty value sets based on changes to the referenced code system
* [FHIR-36472](https://jira.hl7.org/browse/FHIR-36472) Update specialty value sets based on changes to the referenced code system
* [FHIR-34289](https://jira.hl7.org/browse/FHIR-34289) Update Resource Relationship Diagam
* [FHIR-34288](https://jira.hl7.org/browse/FHIR-34288) Upgrade plan-net to US Core 4.0.1
* [FHIR-34140](https://jira.hl7.org/browse/FHIR-34140) HealthcareService delivery-method is too restrictive
* [FHIR-33206](https://jira.hl7.org/browse/FHIR-33206) Ability to manage Provider Directory List for incoming/outgoing providers
* [FHIR-33205](https://jira.hl7.org/browse/FHIR-33205) Expand current options for InsurancePlan Plan Type
* [FHIR-33140](https://jira.hl7.org/browse/FHIR-33140) Spelling error in OrganizationAffiliationRoleCS
* [FHIR-31752](https://jira.hl7.org/browse/FHIR-31752) Missing query for PlannetInsurancePlan Profile
* [FHIR-31570](https://jira.hl7.org/browse/FHIR-31570) Cardinality of Organization.address in Plan-net Network profile
* [FHIR-31499](https://jira.hl7.org/browse/FHIR-31499) Update specialty value sets based on changes to the referenced code system
* [FHIR-31498](https://jira.hl7.org/browse/FHIR-31498) Update specialty value sets based on changes to the referenced code system
* [FHIR-31497](https://jira.hl7.org/browse/FHIR-31497) Update specialty value sets based on changes to the referenced code system
* [FHIR-31496](https://jira.hl7.org/browse/FHIR-31496) Update specialty value sets based on changes to the referenced code system
* [FHIR-31495](https://jira.hl7.org/browse/FHIR-31495) Update specialty value sets based on changes to the referenced code system
* [FHIR-31494](https://jira.hl7.org/browse/FHIR-31494) Update specialty value sets based on changes to the referenced code system
* [FHIR-29767](https://jira.hl7.org/browse/FHIR-29767) Capture Cultural Competency proficiency for Practitioner
* [FHIR-25334](https://jira.hl7.org/browse/FHIR-25334) Suggest adding additional words to simplify and clarify.
* [FHIR-25333](https://jira.hl7.org/browse/FHIR-25333) Suggest removing as redundant with the first sentence.
* [FHIR-25310](https://jira.hl7.org/browse/FHIR-25310) added may
* [FHIR-25309](https://jira.hl7.org/browse/FHIR-25309) As there are many other use case then displayed

### Changes and Updates for Version 1.1.0

* Fixed names of 3 search parameter files based on improved IG publisher error checking: healthcareservice-service-category, location-address-postalcode and location-address-state. All of these were mismatched with the search parameter name, so the file couldn't be found.
* Updated Taxonomy Codes (Jira tickets [FHIR 31494](https://jira.hl7.org/browse/FHIR-33206?filter=14707)  - [FHIR 31499](https://jira.hl7.org/browse/FHIR-33206?filter=14707) )
* Make HealthcareService Delivery Method optional (Jira ticket [FHIR 34140](https://jira.hl7.org/browse/FHIR-34140?filter=14707))
* Change Organization.type binding from OrganizationType to NetworkType (Jira ticket [FHIR 28919](https://jira.hl7.org/browse/FHIR-28919?filter=14707))
* Added 'catastrophic' options to Insurance Plan Types (Jira ticket [FHIR 33205](https://jira.hl7.org/browse/FHIR-33205filter=14707))
* Ability to manage Provider Directory List for incoming/outgoing providers (Jira ticket [FHIR 33206](https://jira.hl7.org/browse/FHIR-33206?filter=14707))
* Update Resource Relationships Diagram (Jira ticket [FHIR 34289](https://jira.hl7.org/browse/FHIR-34289?filter=14707))
* Fix Spelling (Jira ticket [FHIR 33140](https://jira.hl7.org/browse/FHIR-33140?filter=14707))
* Transitioned IG to Sushi 1.0.0 directory structure

### Changes and Updates for Version 1.0.0

* Davinci PDEX Plan Net, Release 1 - US Realm STU

### Changes and Updates for Version 0.1.0

* Davinci pdex Plan Net - STU Ballot

| [<prev](background.html) | [top](#top) | [next>](confexpectations.html) |
| --- | --- | --- |

IG © 2025+ [HL7 International / Financial Management](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.2.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2025-02-25

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |

[Propose a change](http://hl7.org/fhir-issues)