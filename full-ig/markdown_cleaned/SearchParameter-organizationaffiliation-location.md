# SearchParameter: Plannet\_sp\_organizationaffiliation\_location

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_organizationaffiliation\_location**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_organizationaffiliation\_location

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organizationaffiliation-location | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_organizationaffiliation\_location |

Select OrganizationAffiliations available at the specified location

**Generated Narrative**

Resource "organizationaffiliation-location"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organizationaffiliation-location`

**version**: 1.1.0

**name**: Plannet\_sp\_organizationaffiliation\_location

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/OrganizationAffiliation-location>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select OrganizationAffiliations available at the specified location

**jurisdiction**: United States of America  (unknown#US)

**code**: location

**base**: OrganizationAffiliation

**type**: reference

**expression**: OrganizationAffiliation.location

**target**: Location

**multipleOr**: true

**multipleAnd**: true

**chain**: address, address-postalcode, address-city, address-state, organization, type