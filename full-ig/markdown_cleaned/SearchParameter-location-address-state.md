# SearchParameter: Plannet\_sp\_location\_address\_state

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_location\_address\_state**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_location\_address\_state

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-address-state | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_location\_address\_state |

Select Locations with the specified address.state

**Generated Narrative**

Resource "location-address-state"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-address-state`

**version**: 1.1.0

**name**: Plannet\_sp\_location\_address\_state

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Location-address-state>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Locations with the specified address.state

**jurisdiction**: United States of America  (unknown#US)

**code**: address-state

**base**: Location

**type**: string

**expression**: Location.address.state

**multipleOr**: true

**multipleAnd**: true

**modifier**: exact, contains