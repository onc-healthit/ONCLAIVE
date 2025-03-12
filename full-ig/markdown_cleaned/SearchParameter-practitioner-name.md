# SearchParameter: Plannet\_sp\_practitioner\_name

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_practitioner\_name**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_practitioner\_name

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitioner-name | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_practitioner\_name |

Select Practitioners with the specified name (matches against any of the elements in the HumanName data type)

**Generated Narrative**

Resource "practitioner-name"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitioner-name`

**version**: 1.1.0

**name**: Plannet\_sp\_practitioner\_name

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Practitioner-name>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Practitioners with the specified name (matches against any of the elements in the HumanName data type)

**jurisdiction**: United States of America  (unknown#US)

**code**: name

**base**: Practitioner

**type**: string

**expression**: Practitioner.name

**multipleOr**: true

**multipleAnd**: true

**modifier**: exact, contains