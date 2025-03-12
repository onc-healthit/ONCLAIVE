# SearchParameter: Plannet\_sp\_location\_partof

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_location\_partof**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_location\_partof

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-partof | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_location\_partof |

Select Locations that are part of the specified location

**Generated Narrative**

Resource "location-partof"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-partof`

**version**: 1.1.0

**name**: Plannet\_sp\_location\_partof

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Location-partof>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Locations that are part of the specified location

**jurisdiction**: United States of America  (unknown#US)

**code**: partof

**base**: Location

**type**: reference

**expression**: Location.partOf

**target**: Location

**multipleOr**: true

**chain**: type, address, organization