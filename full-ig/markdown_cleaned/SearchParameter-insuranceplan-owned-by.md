# SearchParameter: Plannet\_sp\_insuranceplan\_owned\_by

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_insuranceplan\_owned\_by**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_insuranceplan\_owned\_by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/insuranceplan-owned-by | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_insuranceplan\_owned\_by |

Select products that are owned by the specified organization

**Generated Narrative**

Resource "insuranceplan-owned-by"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/insuranceplan-owned-by`

**version**: 1.1.0

**name**: Plannet\_sp\_insuranceplan\_owned\_by

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/InsurancePlan-owned-by>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select products that are owned by the specified organization

**jurisdiction**: United States of America  (unknown#US)

**code**: owned-by

**base**: InsurancePlan

**type**: reference

**expression**: InsurancePlan.ownedBy

**target**: Organization

**multipleOr**: true

**multipleAnd**: true

**chain**: name, partof