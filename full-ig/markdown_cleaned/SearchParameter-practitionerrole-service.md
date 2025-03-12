# SearchParameter: Plannet\_sp\_practitionerrole\_service

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_practitionerrole\_service**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_practitionerrole\_service

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-service | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_practitionerrole\_service |

Select PractitionerRoles providing the specified service

**Generated Narrative**

Resource "practitionerrole-service"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-service`

**version**: 1.1.0

**name**: Plannet\_sp\_practitionerrole\_service

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/PractitionerRole-service>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select PractitionerRoles providing the specified service

**jurisdiction**: United States of America  (unknown#US)

**code**: service

**base**: PractitionerRole

**type**: reference

**expression**: PractitionerRole.healthcareService

**target**: HealthcareService

**multipleOr**: true

**multipleAnd**: true

**chain**: service-category, organization, location