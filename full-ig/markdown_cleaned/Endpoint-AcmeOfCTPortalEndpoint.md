# Example Endpoint: AcmeOfCTPortalEndpoint

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **AcmeOfCTPortalEndpoint**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## Example Endpoint: AcmeOfCTPortalEndpoint

|  |  |
| --- | --- |
|  | |

**Generated Narrative**

Resource "AcmeOfCTPortalEndpoint" Updated "2020-07-07 01:26:22+0000" (Language "en-US")

Profile: [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)

> **Endpoint Usecase**
>
> **value**: healthcare operations  ([ActReason](http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html)#HOPERAT)

**status**: active

**connectionType**: REST (not FHIR) (Details: http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointConnectionTypeCS code rest-non-fhir = 'REST (not FHIR)', stated as 'null')

**name**: Endpoint for Acme of CT Portal

**payloadType**: Not Applicable  ([Endpoint Payload Types](CodeSystem-EndpointPayloadTypeCS.html)#NA)

**address**: <https://urlofportal.acmect.com>

### Notes:

|  |  |
| --- | --- |
| **Field** | **Value** |
| resourceType | "Endpoint" |
| id | "AcmeOfCTPortalEndpoint" |
| meta.profile[0] | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Endpoint" |
| meta.lastUpdated | "2020-07-07T13:26:22.0314215+00:00" |
| status | "active" |
| extension[0].extension[0].url | "type" |
| extension[0].extension[0].valueCodeableConcept.coding[0].code | #HOPERAT |
| extension[0].extension[0].valueCodeableConcept.coding[0].system | "http://terminology.hl7.org/CodeSystem/v3-ActReason" |
| extension[0].url | "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase" |
| language | "en-US" |
| name | "Endpoint for Acme of CT Portal" |
| connectionType.code | #rest-non-fhir |
| connectionType.system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointConnectionTypeCS" |
| payloadType[0].coding[0].code | #NA |
| payloadType[0].coding[0].system | "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointPayloadTypeCS" |
| address | "https://urlofportal.acmect.com" |