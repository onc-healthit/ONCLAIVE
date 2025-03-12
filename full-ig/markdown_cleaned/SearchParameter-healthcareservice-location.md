# SearchParameter: Plannet\_sp\_healthcareservice\_location

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_healthcareservice\_location**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_healthcareservice\_location

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/healthcareservice-location | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_healthcareservice\_location |

Select HealthcareServices available at the specified location

**Generated Narrative**

Resource "healthcareservice-location"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/healthcareservice-location`

**version**: 1.1.0

**name**: Plannet\_sp\_healthcareservice\_location

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/HealthcareService-location>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select HealthcareServices available at the specified location

**jurisdiction**: United States of America  (unknown#US)

**code**: location

**base**: HealthcareService

**type**: reference

**expression**: HealthcareService.location

**target**: Location

**multipleOr**: true

**multipleAnd**: true

**chain**: address, address-postalcode, address-city, address-state, organization, type