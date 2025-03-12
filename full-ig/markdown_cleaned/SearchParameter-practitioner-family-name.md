# SearchParameter: Plannet\_sp\_practitioner\_family\_name

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_practitioner\_family\_name**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_practitioner\_family\_name

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitioner-family-name | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_practitioner\_family\_name |

Select Practitioners with the specified family name

**Generated Narrative**

Resource "practitioner-family-name"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitioner-family-name`

**version**: 1.1.0

**name**: Plannet\_sp\_practitioner\_family\_name

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/individual-family>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Practitioners with the specified family name

**jurisdiction**: United States of America  (unknown#US)

**code**: family

**base**: Practitioner

**type**: string

**expression**: Practitioner.name.family

**multipleOr**: true

**multipleAnd**: true

**modifier**: exact