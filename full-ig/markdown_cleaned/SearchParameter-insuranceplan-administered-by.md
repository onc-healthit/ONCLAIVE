# SearchParameter: Plannet\_sp\_insuranceplan\_administered\_by

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plannet\_sp\_insuranceplan\_administered\_by**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## SearchParameter: Plannet\_sp\_insuranceplan\_administered\_by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/insuranceplan-administered-by | | | | *Version*: 1.1.0 |
| Active as of 2018-05-23 | | | | *Computable Name*: Plannet\_sp\_insuranceplan\_administered\_by |

Select products that are administered by the specified organization

**Generated Narrative**

Resource "insuranceplan-administered-by"

**url**: `http://hl7.org/fhir/us/davinci-pdex-plan-net/SearchParameter/insuranceplan-administered-by`

**version**: 1.1.0

**name**: Plannet\_sp\_insuranceplan\_administered\_by

**derivedFrom**: <http://hl7.org/fhir/SearchParameter/InsurancePlan-administered-by>

**status**: active

**date**: 2018-05-23 12:00:00+0000

**publisher**: HL7 Financial Management Working Group

**contact**: HL7 Financial Management Working Group: <http://www.hl7.org/Special/committees/fm>,[fm@lists.HL7.org](mailto:fm@lists.HL7.org)

**description**: Select products that are administered by the specified organization

**jurisdiction**: United States of America  (unknown#US)

**code**: administered-by

**base**: InsurancePlan

**type**: reference

**expression**: InsurancePlan.administeredBy

**target**: Organization

**multipleOr**: true

**multipleAnd**: true

**chain**: name, partof