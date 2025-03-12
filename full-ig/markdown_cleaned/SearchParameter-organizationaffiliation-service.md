# SearchParameter: Plannet\_sp\_organizationaffiliation\_service

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_organizationaffiliation\_service**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_organizationaffiliation\_service

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organizationaffiliation-service | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_organizationaffiliation\_service |

Select OrganizationAffiliations providing the specified service

**Generated Narrative**

Resource "organizationaffiliation-service"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organizationaffiliation-service`

**version**: 1.1.0

**name**: Plannet\_sp\_organizationaffiliation\_service

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/OrganizationAffiliation-service>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select OrganizationAffiliations providing the specified service

**jurisdiction**: United States of America  (unknown#US)

**code**: service

**base**: OrganizationAffiliation

**type**: reference

**expression**: OrganizationAffiliation.healthcareService

**target**: HealthcareService

**multipleOr**: true

**multipleAnd**: true

**chain**: service-category, organization, location