# SearchParameter: Plannet\_sp\_organization\_name

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_organization\_name**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_organization\_name

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organization-name | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_organization\_name |

Select Organizations with the specified name

**Generated Narrative**

Resource "organization-name"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organization-name`

**version**: 1.1.0

**name**: Plannet\_sp\_organization\_name

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Organization-name>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Organizations with the specified name

**jurisdiction**: United States of America  (unknown#US)

**code**: name

**base**: Organization

**type**: string

**expression**: Organization.name | Organization.alias

**multipleOr**: true

**multipleAnd**: true

**modifier**: exact, contains