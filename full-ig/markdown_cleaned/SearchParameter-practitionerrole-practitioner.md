# SearchParameter: Plannet\_sp\_practitionerrole\_practitioner

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_practitionerrole\_practitioner**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_practitionerrole\_practitioner

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-practitioner | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_practitionerrole\_practitioner |

Select roles filled by the specified practitioner

**Generated Narrative**

Resource "practitionerrole-practitioner"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-practitioner`

**version**: 1.1.0

**name**: Plannet\_sp\_practitionerrole\_practitioner

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/PractitionerRole-practitioner>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select roles filled by the specified practitioner

**jurisdiction**: United States of America  (unknown#US)

**code**: practitioner

**base**: PractitionerRole

**type**: reference

**expression**: PractitionerRole.practitioner

**target**: Practitioner

**multipleOr**: true

**multipleAnd**: true

**chain**: name