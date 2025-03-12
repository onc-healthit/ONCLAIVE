# ValueSet: Minimum Endpoint Connection Types VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Minimum Endpoint Connection Types VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Minimum Endpoint Connection Types VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/MinEndpointConnectionTypeVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: MinEndpointConnectionTypeVS |

Minimum Endpoint Connection Types

**References**

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

### Logical Definition (CLD)

This value set includes codes based on the following rules:

* Include these codes as defined in [`http://terminology.hl7.org/CodeSystem/endpoint-connection-type`](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html)

  |  |  |  |
  | --- | --- | --- |
  | **Code** | **Display** | **Definition** |
  | [hl7-fhir-rest](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-rest) | HL7 FHIR | Interact with the server interface using FHIR's RESTful interface. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement. |
  | [hl7-fhir-msg](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-msg) | HL7 FHIR Messaging | Use the servers FHIR Messaging interface. Details can be found on the messaging.html page in the FHIR Specification. The FHIR server's base address is specified in the Endpoint.address property. |
  | [direct-project](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-direct-project) | Direct Project | Direct Project information - http://wiki.directproject.org/ |
* Include these codes as defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointConnectionTypeCS`](CodeSystem-EndpointConnectionTypeCS.html)

  |  |  |  |
  | --- | --- | --- |
  | **Code** | **Display** | **Definition** |
  | [hl7-fhir-opn](CodeSystem-EndpointConnectionTypeCS.html#EndpointConnectionTypeCS-hl7-fhir-opn) | HL7 FHIR Operation | Interact with a FHIR server interface using FHIR's RESTful interface using an operation other than messaging. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement. |
  | [rest-non-fhir](CodeSystem-EndpointConnectionTypeCS.html#EndpointConnectionTypeCS-rest-non-fhir) | REST (not FHIR) | Interact with a server using HTTP/REST but not FHIR. Should be used for web portals. |

### Expansion

This value set contains 5 concepts

Expansion based on:

* [Endpoint Connection Type v0.1.0 (CodeSystem)](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html)
* [Endpoint Connection Types (additional) v1.1.0 (CodeSystem)](CodeSystem-EndpointConnectionTypeCS.html)

|  |  |  |  |
| --- | --- | --- | --- |
| **Code** | **System** | **Display** | **Definition** |
| [hl7-fhir-rest](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-rest) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | HL7 FHIR | Interact with the server interface using FHIR's RESTful interface. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement. |
| [hl7-fhir-msg](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-msg) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | HL7 FHIR Messaging | Use the servers FHIR Messaging interface. Details can be found on the messaging.html page in the FHIR Specification. The FHIR server's base address is specified in the Endpoint.address property. |
| [direct-project](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-direct-project) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | Direct Project | Direct Project information - http://wiki.directproject.org/ |
| [hl7-fhir-opn](CodeSystem-EndpointConnectionTypeCS.html#EndpointConnectionTypeCS-hl7-fhir-opn) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointConnectionTypeCS | HL7 FHIR Operation | Interact with a FHIR server interface using FHIR's RESTful interface using an operation other than messaging. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement. |
| [rest-non-fhir](CodeSystem-EndpointConnectionTypeCS.html#EndpointConnectionTypeCS-rest-non-fhir) | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointConnectionTypeCS | REST (not FHIR) | Interact with a server using HTTP/REST but not FHIR. Should be used for web portals. |

---

Explanation of the columns that may appear on this page:

|  |  |
| --- | --- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the *display* element of a [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |