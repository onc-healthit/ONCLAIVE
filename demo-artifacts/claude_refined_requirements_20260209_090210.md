# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Endpoint extension:type sub-extension cardinality requirement
**Requirement**: "Extension.extension:type [cardinality] 1..1"
**Context**: The endpoint-usecase extension is a complex extension that may be used on Endpoint resources to enumerate specific use cases (service descriptions) supported by the endpoint. The type sub-extension is mandatory and indicates the type of services supported by the endpoint.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used on an Endpoint resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: Endpoint Usecase
**Grouping**: Endpoint

---
# REQ-002
**ID**: 02
**Summary**: Endpoint extension:type value binding to Endpoint Usecases ValueSet
**Requirement**: "Extension.extension:type.value[x] [Binding:] [Endpoint Usecases VS](ValueSet-EndpointUsecaseVS.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)): To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated."
**Context**: When the type sub-extension of the endpoint-usecase extension is used, its value must be bound to the Endpoint Usecases ValueSet with extensible conformance, meaning the concept SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension with type sub-extension is used on an Endpoint resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: Endpoint Usecase
**Grouping**: Endpoint

---
# REQ-003
**ID**: 03
**Summary**: Endpoint extension:standard sub-extension cardinality requirement
**Requirement**: "Extension.extension:standard [cardinality] 0..1"
**Context**: The endpoint-usecase extension includes an optional standard sub-extension that provides a URI to a published standard describing the services supported by the endpoint (e.g., an HL7 implementation guide). This sub-extension has a cardinality of 0..1, meaning it is optional but can appear at most once.
**Conformance**: MAY
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used on an Endpoint resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: Endpoint Usecase
**Grouping**: Endpoint

---
# REQ-004
**ID**: 04
**Summary**: Plan-Net Server SHALL support search-type and read interactions on Endpoint resource
**Requirement**: "A Server SHALL support search-type, read [on Endpoint resource]."
**Context**: This requirement mandates that the server must support the ability to search for Endpoint resources and read individual Endpoint resources by their logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-005
**ID**: 05
**Summary**: Plan-Net Server SHOULD support vread interaction on Endpoint resource
**Requirement**: "A Server SHOULD support vread [on Endpoint resource]."
**Context**: This requirement recommends that the server should support retrieving specific historical versions of an Endpoint resource using the version-aware read (vread) operation.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-006
**ID**: 06
**Summary**: Plan-Net Server SHALL support reading Endpoint resource by id
**Requirement**: "A Server SHALL be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]`"
**Context**: This requirement mandates that the server must support retrieving a specific Endpoint resource using its logical ID via a GET operation.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-007
**ID**: 07
**Summary**: Plan-Net Server SHOULD support vread on Endpoint resource by id and version
**Requirement**: "A Server SHOULD be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]/_history/vid`"
**Context**: This requirement recommends that the server should support retrieving a specific version of an Endpoint resource using its logical ID and version ID.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-008
**ID**: 08
**Summary**: Plan-Net Server SHALL support _include for Endpoint:organization
**Requirement**: "A Server SHALL be capable of supporting the following _includes: Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"
**Context**: This requirement mandates that the server must support including referenced Organization resources when searching for Endpoint resources using the _include parameter.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-009
**ID**: 09
**Summary**: Plan-Net Server SHALL support search parameters on Endpoint resource
**Requirement**: "A Server SHALL support the following search parameters on Endpoint: organization, _id, _lastUpdated"
**Context**: This requirement mandates that the server must support searching for Endpoint resources using the organization reference parameter, the _id token parameter, and the _lastUpdated date parameter.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.1 Endpoint
**Grouping**: Endpoint

---
# REQ-010
**ID**: 10
**Summary**: Endpoint status SHALL be fixed to 'active'
**Requirement**: "Endpoint.status [Must Support] Fixed Value `active`"
**Context**: The Plan-Net Endpoint profile constrains the status element to always have the value 'active'. This indicates that endpoints conforming to this profile must be operational and available for use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-011
**ID**: 11
**Summary**: Endpoint connectionType SHALL use codes from Endpoint Connection Types VS
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Endpoint Connection Types VS]"
**Context**: The connectionType element describes the technical details of the usage of the endpoint (e.g., protocol/profile/standard). Systems must use codes from the specified value set unless they are not suitable for the use case. Additionally, there is a minimum binding that requires support for all codes in the Minimum Endpoint Connection Types VS.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-012
**ID**: 12
**Summary**: Endpoint connectionType SHALL support all codes from Minimum Endpoint Connection Types VS
**Requirement**: "Any conformant system SHALL support all these codes [from Minimum Endpoint Connection Types VS]"
**Context**: The connectionType element has a minimum binding that requires all conformant systems to support all codes defined in the Minimum Endpoint Connection Types VS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-013
**ID**: 13
**Summary**: Endpoint payloadType SHALL use codes from Endpoint Payload Types VS
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Endpoint Payload Types VS]"
**Context**: The payloadType element describes the acceptable content that can be communicated on the endpoint (e.g., specific document/schema types like DischargeSummary or CarePlan). Systems must use codes from the specified value set unless they are not suitable for the use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-014
**ID**: 14
**Summary**: Endpoint payloadMimeType SHALL use codes from Mime Types value set
**Requirement**: "The codes SHALL be taken from [Mime Types]"
**Context**: The payloadMimeType element specifies the mime type to send the payload in (e.g., application/fhir+xml, application/fhir+json). Systems must use codes from the FHIR-defined Mime Types value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-015
**ID**: 15
**Summary**: Endpoint contact.system SHALL use codes from ContactPointSystem value set
**Requirement**: "The codes SHALL be taken from [ContactPointSystem]"
**Context**: The contact.system element specifies the telecommunications form for the contact point (e.g., phone, fax, email, pager, url, sms, other). Systems must use codes from the FHIR-defined ContactPointSystem value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-016
**ID**: 16
**Summary**: Endpoint contact.use SHALL use codes from ContactPointUse value set
**Requirement**: "The codes SHALL be taken from [ContactPointUse]"
**Context**: The contact.use element identifies the purpose for the contact point (e.g., home, work, temp, old, mobile). Systems must use codes from the FHIR-defined ContactPointUse value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-017
**ID**: 17
**Summary**: If Endpoint resource is contained, it SHALL NOT contain nested Resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources (contained.contained.empty())"
**Context**: This is a base FHIR invariant (dom-2) that applies to all resources. When an Endpoint resource is contained within another resource, it cannot itself contain other resources.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If the resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-018
**ID**: 18
**Summary**: If Endpoint resource is contained, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This is a base FHIR invariant (dom-3) that ensures contained resources are actually used. A contained Endpoint must either be referenced by another element in the containing resource, or the Endpoint must reference the containing resource.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If the resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-019
**ID**: 19
**Summary**: If Endpoint resource is contained, it SHALL NOT have a meta.versionId or a meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (contained.meta.versionId.empty() and contained.meta.lastUpdated.empty())"
**Context**: This is a base FHIR invariant (dom-4) that applies to contained resources. Contained Endpoint resources must not have versioning metadata.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If a resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-020
**ID**: 20
**Summary**: If Endpoint resource is contained, it SHALL NOT have a security label
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label (contained.meta.security.empty())"
**Context**: This is a base FHIR invariant (dom-5) that applies to contained resources. Contained Endpoint resources must not have security labels in their metadata.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If a resource is contained in another resource
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-021
**ID**: 21
**Summary**: Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)."
**Context**: This requirement ensures that modifier extensions used in the Endpoint resource do not alter the meaning of base resource elements or the modifierExtension element itself. Modifier extensions can only modify understanding of the element that contains them or its descendants.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-022
**ID**: 22
**Summary**: Plan-Net Endpoint connectionType SHALL use extensible binding to EndpointConnectionTypeVS
**Requirement**: "connectionType [cardinality] 1.1 [with] Binding: Endpoint Connection Types VS (extensible)"
**Context**: The connectionType element in the Plan-Net Endpoint profile is required (cardinality 1..1) and uses an extensible binding to the EndpointConnectionTypeVS value set, which describes the protocol/profile/standard to be used with the endpoint connection.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: Plan-Net Endpoint
**Grouping**: Endpoint

---
# REQ-023
**ID**: 23
**Summary**: Plan-Net Endpoint payloadType is required with cardinality 1..1
**Requirement**: "payloadType [cardinality] 1.1 [CodeableConcept] The type of content that may be used at this endpoint (e.g. XDS Discharge summaries) Binding: Endpoint Payload Types VS (extensible)"
**Context**: The payloadType element in the Plan-Net Endpoint profile is required (cardinality 1..1) and describes the acceptable content that can be communicated on the endpoint. It uses an extensible binding to the EndpointPayloadTypeVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: Plan-Net Endpoint
**Grouping**: Endpoint

---
# REQ-024
**ID**: 24
**Summary**: Plan-Net Endpoint address is required with cardinality 1..1
**Requirement**: "address [cardinality] 1.1 [url] The technical base address for connecting to this endpoint"
**Context**: The address element in the Plan-Net Endpoint profile is required (cardinality 1..1) and contains the URI that describes the actual end-point to connect to.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: Plan-Net Endpoint
**Grouping**: Endpoint

---
# REQ-025
**ID**: 25
**Summary**: Plan-Net Endpoint managingOrganization SHALL reference Plan-Net Organization profile when present
**Requirement**: "managingOrganization [cardinality] 0.1 Reference(Plan-Net Organization) Organization that manages this endpoint (might not be the organization that exposes the endpoint)"
**Context**: When the managingOrganization element is present in a Plan-Net Endpoint instance, it SHALL reference a Plan-Net Organization profile. This represents the organization that manages the endpoint, which might not be the organization that exposes the endpoint.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: If the managingOrganization element is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: Plan-Net Endpoint
**Grouping**: Endpoint
