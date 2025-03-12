# Example InsurancePlan: AcmeQHPBronze

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **AcmeQHPBronze**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example InsurancePlan: AcmeQHPBronze

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "AcmeQHPBronze" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html)

**status**: active

**type**: Qualified Health Plan  ([Insurance Product Type](CodeSystem-InsuranceProductTypeCS.html)#qhp)

**name**: Acme of CT QHP Bronze

**ownedBy**: [Organization/Acme](Organization-Acme.html) "Acme of CT"

**administeredBy**: [Organization/Acme](Organization-Acme.html) "Acme of CT"

**coverageArea**: [Location/StateOfCTLocation](Location-StateOfCTLocation.html) "State of CT Area"

**endpoint**: [Endpoint/AcmeOfCTPortalEndpoint](Endpoint-AcmeOfCTPortalEndpoint.html) "Endpoint for Acme of CT Portal"

**network**: [Organization/AcmeofCTStdNet](Organization-AcmeofCTStdNet.html) "ACME CT Preferred Provider Network"

### Plans

|  |  |
| --- | --- |
| - | **Type** |
| \* | Bronze-QHP  ([Insurance Plan Type](CodeSystem-InsurancePlanTypeCS.html)#bronze) |

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "InsurancePlan" |
| id | "AcmeQHPBronze" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-InsurancePlan" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| status | "active" |
| language | "en-US" |
| name | "Acme of CT QHP Bronze" |
| type[0].coding[0].code | #qhp |
| type[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsuranceProductTypeCS" |
| type[0].coding[0].display | "Qualified Health Plan" |
| plan[0].type.coding[0].code | #bronze |
| plan[0].type.coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsurancePlanTypeCS" |
| plan[0].type.coding[0].display | "Bronze-QHP" |
| ownedBy.reference | "Organization/Acme" |
| administeredBy.reference | "Organization/Acme" |
| network[0].reference | "Organization/AcmeofCTStdNet" |
| coverageArea[0].reference | "Location/StateOfCTLocation" |
| endpoint[0].reference | "Endpoint/AcmeOfCTPortalEndpoint" |