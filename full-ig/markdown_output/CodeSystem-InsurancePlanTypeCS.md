xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Insurance Plan Type - FHIR v4.0.1

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
* [**Artifacts Summary**](artifacts.html)
* **Insurance Plan Type**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## CodeSystem: Insurance Plan Type

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsurancePlanTypeCS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: InsurancePlanTypeCS |

Categories of cost-sharing used by plans

This Code system is referenced in the content logical definition of the following value sets:

* [InsurancePlanTypeVS](ValueSet-InsurancePlanTypeVS.html)

This code system http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsurancePlanTypeCS defines the following codes:

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| platinum | Platinum-QHP | Plan with highest monthly premium and lowest costs when you need care A Qualified Health Plan with the highest monthly premiums and smallest out-of-pocket costs for the member in comparison to other metal-category plans |
| gold | Gold-QHP | Plan with high monthly premium and low costs when you need care A Qualified Health Plan with the higher monthly premiums and smaller out-of-pocket costs for the member in comparison to other metal-category plans |
| silver | Silver-QHP | Plan with moderate monthly premium and moderate costs when you need care A Qualified Health Plan with the lower monthly premiums and larger out-of-pocket costs for the member in comparison to other metal-category plans |
| bronze | Bronze-QHP | Plan with lowest monthly premium and highest costs when you need care A Qualified Health Plan with the lowest monthly premiums and largest out-of-pocket costs for the member in comparison to other metal-category plans |
| catastrophic | Catastrophic-QHP | A plan with low monthly premiums and very high deductibles and are available only to those under 30 or with certain special exemptions. |
| lowdeductible | Low Deductible | A plan that requires the insured to pay out of pocket a smaller proportion of incurred health care costs than a traditional insurance plan. |
| highdeductible | High Deductible | A plan that requires the insured to pay out of pocket a larger proportion of incurred health care costs than a traditional insurance plan. |
| catastrophicplan | Catastrophic Plan | A plan that requires the insured to pay out of pocket a much larger proportion of incurred health care costs than a traditional insurance plan. |

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)