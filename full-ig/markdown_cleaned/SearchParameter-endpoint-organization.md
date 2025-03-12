# SearchParameter: Plannet\_sp\_endpoint\_organization

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_endpoint\_organization**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_endpoint\_organization

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/endpoint-organization | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_endpoint\_organization |

Select Endpoints managed by the specified organization

**Generated Narrative**

Resource "endpoint-organization"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/endpoint-organization`

**version**: 1.1.0

**name**: Plannet\_sp\_endpoint\_organization

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Endpoint-organization>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Endpoints managed by the specified organization

**jurisdiction**: United States of America  (unknown#US)

**code**: organization

**base**: Endpoint

**type**: reference

**expression**: Endpoint.managingOrganization

**target**: Organization

**multipleOr**: true

**multipleAnd**: true

**chain**: name, address, partof, type