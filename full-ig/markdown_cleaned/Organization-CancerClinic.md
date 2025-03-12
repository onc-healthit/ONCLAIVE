# Example Organization: CancerClinic

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **CancerClinic**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Organization: CancerClinic

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "CancerClinic" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Organization](StructureDefinition-plannet-Organization.html)

**identifier**: id: NPI788

**active**: true

**type**: Facility  ([Organization Type](CodeSystem-OrgTypeCS.html)#fac)

**name**: Hamilton Clinic

**telecom**: ph: (111)-222-3333, <https://www.Hospital.com>

**address**: 123 Main Street Anytown CT 00014-1234

### Contacts

|  |  |
| --- | --- |
| - | **Telecom** |
| \* | ph: (111)-222-3333 |

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Organization" |
| id | "CancerClinic" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| active | "true" |
| identifier[0].system | "http://hl7.org/fhir/sid/us-npi" |
| identifier[0].value | NPI788 |
| language | "en-US" |
| name | "Hamilton Clinic" |
| telecom[0].system | "phone" |
| telecom[0].value | (111)-222-3333 |
| telecom[0].rank | "2" |
| telecom[1].system | "url" |
| telecom[1].value | https://www.Hospital.com |
| telecom[1].rank | "1" |
| address[0].line[0] | "123 Main Street" |
| address[0].city | "Anytown" |
| address[0].state | "CT" |
| address[0].postalCode | "00014-1234" |
| contact[0].telecom[0].system | "phone" |
| contact[0].telecom[0].value | (111)-222-3333 |
| contact[0].telecom[0].rank | "1" |
| type[0].coding[0].code | #fac |
| type[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/OrgTypeCS" |
| type[0].coding[0].display | "Facility" |