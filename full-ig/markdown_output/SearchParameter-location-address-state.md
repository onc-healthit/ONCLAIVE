xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Plannet\_sp\_location\_address\_state - FHIR v4.0.1

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
* **Plannet\_sp\_location\_address\_state**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_location\_address\_state

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-address-state | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_location\_address\_state |

Select Locations with the specified address.state

**Generated Narrative**

Resource "location-address-state"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-address-state`

**version**: 1.1.0

**name**: Plannet\_sp\_location\_address\_state

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Location-address-state>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Locations with the specified address.state

**jurisdiction**: United States of America  (unknown#US)

**code**: address-state

**base**: Location

**type**: string

**expression**: Location.address.state

**multipleOr**: true

**multipleAnd**: true

**modifier**: exact, contains

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)