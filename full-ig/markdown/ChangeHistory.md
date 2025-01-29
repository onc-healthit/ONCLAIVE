xml version\="1\.0" encoding\="UTF\-8"?

HL7\.FHIR.US.DAVINCI\-PDEX\-PLAN\-NET\\Change History \- FHIR v4\.0\.1

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
* **Change History**

This page is part of the DaVinci PDEX Plan Net (v1\.1\.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1\) based on [FHIR R4](http://hl7.org/fhir/R4). This is the current published version. For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html)

## Change History

### PDEX Payer Network Implementation Guide

#### Changes Since v1\.0\.0

* Fixed names of 3 search parameter files based on improved IG publisher error checking: healthcareservice\-service\-category, location\-address\-postalcode and location\-address\-state. All of these were mismatched with the search parameter name, so the file couldn't be found.
* Updated Taxonomy Codes (Jira tickets [FHIR 31494](https://jira.hl7.org/browse/FHIR-33206?filter=14707)  \- [FHIR 31499](https://jira.hl7.org/browse/FHIR-33206?filter=14707) )
* Make HealthcareService Delivery Method optional (Jira ticket [FHIR 34140](https://jira.hl7.org/browse/FHIR-34140?filter=14707))
* Change Organization.type binding from OrganizationType to NetworkType (Jira ticket [FHIR 28919](https://jira.hl7.org/browse/FHIR-28919?filter=14707))
* Added 'catastrophic' options to Insurance Plan Types (Jira ticket [FHIR 33205](https://jira.hl7.org/browse/FHIR-33205filter=14707))
* Ability to manage Provider Directory List for incoming/outgoing providers (Jira ticket [FHIR 33206](https://jira.hl7.org/browse/FHIR-33206?filter=14707))
* Update Resource Relationships Diagram (Jira ticket [FHIR 34289](https://jira.hl7.org/browse/FHIR-34289?filter=14707))
* Fix Spelling (Jira ticket [FHIR 33140](https://jira.hl7.org/browse/FHIR-33140?filter=14707))
* Transitioned IG to Sushi 1\.0\.0 directory structure

 IG © 2022\+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7\.fhir.us.davinci\-pdex\-plan\-net\#1\.1\.0 based on [FHIR 4\.0\.1](http://hl7.org/fhir/R4/). Generated 2022\-04\-04

 Links: [Table of Contents](toc.html) \|
 [QA Report](qa.html)

 \| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) \|
 [![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) \|

[Propose a change](http://hl7.org/fhir-issues)