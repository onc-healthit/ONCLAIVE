# CodeSystem: Endpoint Connection Types (additional)

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Endpoint Connection Types (additional)**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## CodeSystem: Endpoint Connection Types (additional)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointConnectionTypeCS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: EndpointConnectionTypeCS |

Extension codes for http://terminology.hl7.org/CodeSystem/endpoint-connection-type

This Code system is referenced in the content logical definition of the following value sets:

* [EndpointConnectionTypeVS](ValueSet-EndpointConnectionTypeVS.html)
* [MinEndpointConnectionTypeVS](ValueSet-MinEndpointConnectionTypeVS.html)

This code system http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointConnectionTypeCS defines the following codes:

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| hl7-fhir-opn | HL7 FHIR Operation | Interact with a FHIR server interface using FHIR's RESTful interface using an operation other than messaging. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement. |
| rest-non-fhir | REST (not FHIR) | Interact with a server using HTTP/REST but not FHIR. Should be used for web portals. |