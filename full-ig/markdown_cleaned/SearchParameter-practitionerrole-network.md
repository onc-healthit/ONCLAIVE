# SearchParameter: Plannet\_sp\_practitionerrole\_network

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_practitionerrole\_network**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_practitionerrole\_network

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-network | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_practitionerrole\_network |

Select roles where the practitioner is a member of the specified health insurance provider network

**Generated Narrative**

Resource "practitionerrole-network"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-network`

**version**: 1.1.0

**name**: Plannet\_sp\_practitionerrole\_network

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select roles where the practitioner is a member of the specified health insurance provider network

**jurisdiction**: United States of America  (unknown#US)

**code**: network

**base**: PractitionerRole

**type**: reference

**expression**: PractitionerRole.extension.where(url='http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network-reference')

**target**: Organization

**multipleOr**: true

**multipleAnd**: true

**chain**: name, address, partof, type