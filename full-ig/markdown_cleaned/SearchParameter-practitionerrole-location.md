# SearchParameter: Plannet\_sp\_practitionerrole\_location

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_practitionerrole\_location**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_practitionerrole\_location

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-location | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_practitionerrole\_location |

Select PractitionerRoles available at the specified location

**Generated Narrative**

Resource "practitionerrole-location"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/practitionerrole-location`

**version**: 1.1.0

**name**: Plannet\_sp\_practitionerrole\_location

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/PractitionerRole-location>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select PractitionerRoles available at the specified location

**jurisdiction**: United States of America  (unknown#US)

**code**: location

**base**: PractitionerRole

**type**: reference

**expression**: PractitionerRole.location

**target**: Location

**multipleOr**: true

**multipleAnd**: true

**chain**: address, address-postalcode, address-city, address-state, organization, type