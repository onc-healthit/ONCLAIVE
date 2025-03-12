# SearchParameter: Plannet\_sp\_healthcareservice\_coverage\_area

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_healthcareservice\_coverage\_area**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_healthcareservice\_coverage\_area

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/healthcareservice-coverage-area | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_healthcareservice\_coverage\_area |

Select services available in a region described by the specified location

**Generated Narrative**

Resource "healthcareservice-coverage-area"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/healthcareservice-coverage-area`

**version**: 1.1.0

**name**: Plannet\_sp\_healthcareservice\_coverage\_area

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/HealthcareService-coverage-area>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select services available in a region described by the specified location

**jurisdiction**: United States of America  (unknown#US)

**code**: coverage-area

**base**: HealthcareService

**type**: reference

**expression**: HealthcareService.coverageArea

**target**: Location

**multipleOr**: true

**multipleAnd**: true