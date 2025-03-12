# SearchParameter: Plannet\_sp\_practitioner\_given\_name

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_practitioner\_given\_name**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_practitioner\_given\_name

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitioner-given-name | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_practitioner\_given\_name |

Select Practitioners with the specified given name

**Generated Narrative**

Resource "practitioner-given-name"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitioner-given-name`

**version**: 1.1.0

**name**: Plannet\_sp\_practitioner\_given\_name

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/individual-given>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Practitioners with the specified given name

**jurisdiction**: United States of America  (unknown#US)

**code**: given

**base**: Practitioner

**type**: string

**expression**: Practitioner.name.given

**multipleOr**: true

**multipleAnd**: true

**modifier**: exact