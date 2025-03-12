# SearchParameter: Plannet\_sp\_location\_endpoint

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_location\_endpoint**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_location\_endpoint

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-endpoint | | | | *Version*: 1.1.0 |
| Draft as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_location\_endpoint |

Select Locations with the specified endpoint

**Generated Narrative**

Resource "location-endpoint"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-endpoint`

**version**: 1.1.0

**name**: Plannet\_sp\_location\_endpoint

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Location-endpoint>

**status**: draft

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Locations with the specified endpoint

**jurisdiction**: United States of America  (unknown#US)

**code**: endpoint

**base**: Location

**type**: reference

**expression**: Location.endpoint

**target**: Endpoint

**multipleOr**: true

**multipleAnd**: true

**chain**: organization