# SearchParameter: Plannet\_sp\_organization\_address

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_organization\_address**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_organization\_address

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organization-address | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_organization\_address |

Select organizations with the specified address (matches any of the string elements of an address)

**Generated Narrative**

Resource "organization-address"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organization-address`

**version**: 1.1.0

**name**: Plannet\_sp\_organization\_address

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Organization-address>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select organizations with the specified address (matches any of the string elements of an address)

**jurisdiction**: United States of America  (unknown#US)

**code**: address

**base**: Organization

**type**: string

**expression**: Organization.address

**multipleOr**: true

**multipleAnd**: true

**modifier**: exact, contains