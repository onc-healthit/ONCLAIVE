# SearchParameter: Plannet\_sp\_organizationaffiliation\_network

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_organizationaffiliation\_network**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_organizationaffiliation\_network

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organizationaffiliation-network | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_organizationaffiliation\_network |

Select roles where the organization is a member of the specified health insurance provider network

**Generated Narrative**

Resource "organizationaffiliation-network"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/organizationaffiliation-network`

**version**: 1.1.0

**name**: Plannet\_sp\_organizationaffiliation\_network

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/OrganizationAffiliation-network>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select roles where the organization is a member of the specified health insurance provider network

**jurisdiction**: United States of America  (unknown#US)

**code**: network

**base**: OrganizationAffiliation

**type**: reference

**expression**: OrganizationAffiliation.network

**target**: Organization

**multipleOr**: true

**multipleAnd**: true

**chain**: name, partof