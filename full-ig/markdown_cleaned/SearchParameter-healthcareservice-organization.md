# SearchParameter: Plannet\_sp\_healthcareservice\_organization

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_healthcareservice\_organization**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_healthcareservice\_organization

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/healthcareservice-organization | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_healthcareservice\_organization |

Select HealthcareServices provided by the specified organization

**Generated Narrative**

Resource "healthcareservice-organization"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/healthcareservice-organization`

**version**: 1.1.0

**name**: Plannet\_sp\_healthcareservice\_organization

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/HealthcareService-organization>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select HealthcareServices provided by the specified organization

**jurisdiction**: United States of America  (unknown#US)

**code**: organization

**base**: HealthcareService

**type**: reference

**expression**: HealthcareService.providedBy

**target**: Organization

**multipleOr**: true

**multipleAnd**: true

**chain**: name, address, partof, type