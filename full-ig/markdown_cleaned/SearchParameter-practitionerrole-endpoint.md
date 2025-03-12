# SearchParameter: Plannet\_sp\_practitionerrole\_endpoint

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_practitionerrole\_endpoint**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_practitionerrole\_endpoint

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-endpoint | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_practitionerrole\_endpoint |

Select PractitionerRoles with the specified endpoint

**Generated Narrative**

Resource "practitionerrole-endpoint"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-endpoint`

**version**: 1.1.0

**name**: Plannet\_sp\_practitionerrole\_endpoint

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/PractitionerRole-endpoint>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select PractitionerRoles with the specified endpoint

**jurisdiction**: United States of America  (unknown#US)

**code**: endpoint

**base**: PractitionerRole

**type**: reference

**expression**: PractitionerRole.endpoint

**target**: Endpoint

**multipleOr**: true

**multipleAnd**: true

**chain**: organization