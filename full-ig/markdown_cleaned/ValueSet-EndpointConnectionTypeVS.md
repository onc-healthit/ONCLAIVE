# ValueSet: Endpoint Connection Types VS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Endpoint Connection Types VS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Endpoint Connection Types VS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/EndpointConnectionTypeVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: EndpointConnectionTypeVS |

Endpoint Connection Types

**References**

* [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)

### Logical Definition (CLD)

This value set includes codes based on the following rules:

* Include all codes defined in [`http://terminology.hl7.org/CodeSystem/endpoint-connection-type`](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html)
* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/EndpointConnectionTypeCS`](CodeSystem-EndpointConnectionTypeCS.html)

### Expansion

This value set contains 16 concepts

Expansion based on:

* [Endpoint Connection Type v0.1.0 (CodeSystem)](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html)
* [Endpoint Connection Types (additional) v1.1.0 (CodeSystem)](CodeSystem-EndpointConnectionTypeCS.html)

|  |  |  |  |
| --- | --- | --- | --- |
| **Code** | **System** | **Display** | **Definition** |
| [ihe-xcpd](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-ihe-xcpd) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | IHE XCPD | IHE Cross Community Patient Discovery Profile (XCPD) - http://wiki.ihe.net/index.php/Cross-Community\_Patient\_Discovery |
| [ihe-xca](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-ihe-xca) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | IHE XCA | IHE Cross Community Access Profile (XCA) - http://wiki.ihe.net/index.php/Cross-Community\_Access |
| [ihe-xdr](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-ihe-xdr) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | IHE XDR | IHE Cross-Enterprise Document Reliable Exchange (XDR) - http://wiki.ihe.net/index.php/Cross-enterprise\_Document\_Reliable\_Interchange |
| [ihe-xds](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-ihe-xds) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | IHE XDS | IHE Cross-Enterprise Document Sharing (XDS) - http://wiki.ihe.net/index.php/Cross-Enterprise\_Document\_Sharing |
| [ihe-iid](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-ihe-iid) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | IHE IID | IHE Invoke Image Display (IID) - http://wiki.ihe.net/index.php/Invoke\_Image\_Display |
| [dicom-wado-rs](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-dicom-wado-rs) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | DICOM WADO-RS | DICOMweb RESTful Image Retrieve - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect\_6.5.html |
| [dicom-qido-rs](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-dicom-qido-rs) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | DICOM QIDO-RS | DICOMweb RESTful Image query - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect\_6.7.html |
| [dicom-stow-rs](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-dicom-stow-rs) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | DICOM STOW-RS | DICOMweb RESTful image sending and storage - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect\_6.6.html |
| [dicom-wado-uri](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-dicom-wado-uri) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | DICOM WADO-URI | DICOMweb Image Retrieve - http://dicom.nema.org/dicom/2013/output/chtml/part18/sect\_6.3.html |
| [hl7-fhir-rest](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-rest) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | HL7 FHIR | Interact with the server interface using FHIR's RESTful interface. For details on its version/capabilities you should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement. |
| [hl7-fhir-msg](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-msg) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | HL7 FHIR Messaging | Use the servers FHIR Messaging interface. Details can be found on the messaging.html page in the FHIR Specification. The FHIR server's base address is specified in the Endpoint.address property. |
| [hl7v2-mllp](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7v2-mllp) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | HL7 v2 MLLP | HL7v2 messages over an LLP TCP connection |
| [secure-email](http://terminology.hl7.org/3.1.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-secure-email) | http://terminology.hl7.org/CodeSystem/endpoint-connection-type | Secure email | Email delivery using a digital certificate to encrypt the content using the public key, receiver must have the private key to decrypt the content |
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