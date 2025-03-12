# SearchParameter: Plannet\_sp\_location\_address\_postalcode

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_location\_address\_postalcode**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_location\_address\_postalcode

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-address-postalcode | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_location\_address\_postalcode |

Select Locations with the specified address

**Generated Narrative**

Resource "location-address-postalcode"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/location-address-postalcode`

**version**: 1.1.0

**name**: Plannet\_sp\_location\_address\_postalcode

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/Location-address-postalcode>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select Locations with the specified address

**jurisdiction**: United States of America  (unknown#US)

**code**: address-postalcode

**base**: Location

**type**: string

**expression**: Location.address.postalCode

**multipleOr**: true

**multipleAnd**: true

**modifier**: exact, contains