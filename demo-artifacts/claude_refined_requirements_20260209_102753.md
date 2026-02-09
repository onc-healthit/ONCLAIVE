# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Endpoint-usecase extension type element cardinality and binding
**Requirement**: "extension:type [with cardinality] 1.1 [and] value[x] [with cardinality] 1.1 [CodeableConcept bound to] Endpoint Usecases VS (extensible) - To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated."
**Context**: The endpoint-usecase extension defines the type of services supported by an endpoint. The type element is a required sub-extension (cardinality 1..1) that must contain a CodeableConcept value bound to the EndpointUsecaseVS value set with extensible binding. This means implementations must use a code from the value set if applicable, or may use an alternate coding if the value set does not cover the concept.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the endpoint-usecase extension is used on an Endpoint resource. The conformance applies to the value selection when a concept from the value set can apply.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.70.1 Extension: Endpoint Usecase - Differential Table
**Grouping**: Endpoint

---
# REQ-002
**ID**: 02
**Summary**: Server SHALL support search-type and read interactions on Endpoint resource
**Requirement**: "A Server SHALL support search-type, read [on Endpoint resource]."
**Context**: This requirement mandates support for search-type and read operations on the Endpoint resource, which are fundamental interactions for retrieving Endpoint data.
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
# REQ-003
**ID**: 03
**Summary**: Server SHOULD support vread interaction on Endpoint resource
**Requirement**: "A Server SHOULD support vread [on Endpoint resource]."
**Context**: This requirement recommends support for version-specific read (vread) operations on the Endpoint resource, enabling retrieval of historical versions.
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
# REQ-004
**ID**: 04
**Summary**: Server SHALL support returning Endpoint resource by id
**Requirement**: "A Server SHALL be capable of returning a Endpoint resource using: GET [base]/Endpoint/[id]"
**Context**: This requirement mandates the ability to retrieve a specific Endpoint resource by its logical id using a standard GET request.
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
**Summary**: Server SHOULD support returning Endpoint resource by version id
**Requirement**: "A Server SHOULD be capable of returning a Endpoint resource using: GET [base]/Endpoint/[id]/_history/vid"
**Context**: This requirement recommends the ability to retrieve a specific version of an Endpoint resource using the version-aware history endpoint.
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
**Summary**: Server SHALL support _include for Endpoint:organization
**Requirement**: "A Server SHALL be capable of supporting the following _includes: Endpoint:organization - GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization"
**Context**: This requirement mandates support for including referenced Organization resources when searching for Endpoint resources.
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
**Summary**: Server SHALL support search by organization, _id, and _lastUpdated on Endpoint resource
**Requirement**: "A Server SHALL support the following search parameters on Endpoint: organization, _id, _lastUpdated"
**Context**: This requirement mandates support for searching Endpoint resources by organization reference, logical id, and last updated timestamp. These are the required search parameters for the Endpoint resource.
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
# REQ-008
**ID**: 08
**Summary**: Plan-Net Endpoint status fixed value
**Requirement**: "Endpoint.status [has a] Fixed Value `active`"
**Context**: The Plan-Net Endpoint profile constrains the status element of the Endpoint resource to always have the value 'active'. This means that endpoints conforming to this profile must be in active status.
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
# REQ-009
**ID**: 09
**Summary**: Plan-Net Endpoint connectionType binding requirement
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Endpoint Connection Types VS]"
**Context**: The connectionType element, which represents the technical details of the usage of the endpoint, must use codes from the specified value set unless they are not suitable. Additionally, any conformant system SHALL support all codes from the Minimum Endpoint Connection Types VS as indicated by the Min Binding.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless codes from the value set are not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-010
**ID**: 10
**Summary**: Plan-Net Endpoint connectionType minimum binding requirement
**Requirement**: "[For Endpoint.connectionType, any conformant system] SHALL support all these codes [from Minimum Endpoint Connection Types VS]"
**Context**: This is a minimum binding requirement for the connectionType element. Conformant systems must support all codes defined in the Minimum Endpoint Connection Types VS value set, ensuring baseline interoperability for endpoint connection types.
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
**Summary**: Plan-Net Endpoint payloadType binding requirement
**Requirement**: "Unless not suitable, these codes SHALL be taken from [Endpoint Payload Types VS]"
**Context**: The payloadType element describes the acceptable content that can be communicated on the endpoint. Codes must be taken from the Endpoint Payload Types VS value set unless they are not suitable for the use case.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: Unless codes from the value set are not suitable
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: PlannetEndpoint - Detailed Descriptions
**Grouping**: Endpoint

---
# REQ-012
**ID**: 12
**Summary**: Plan-Net Endpoint contact.system binding requirement
**Requirement**: "The codes SHALL be taken from [ContactPointSystem]"
**Context**: The contact.system element, which identifies the telecommunications form for the contact point, must use codes from the ContactPointSystem value set. This is a required binding.
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
**Summary**: Plan-Net Endpoint contact.use binding requirement
**Requirement**: "The codes SHALL be taken from [ContactPointUse]"
**Context**: The contact.use element, which identifies the purpose for the contact point, must use codes from the ContactPointUse value set. This is a required binding.
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
# REQ-014
**ID**: 14
**Summary**: Plan-Net Endpoint payloadMimeType binding requirement
**Requirement**: "The codes SHALL be taken from [Mime Types]"
**Context**: The payloadMimeType element specifies the mime type to send the payload in (e.g., application/fhir+xml, application/fhir+json). Codes must be taken from the Mime Types value set. This is a required binding.
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
**Summary**: Plan-Net Endpoint modifierExtension requirements
**Requirement**: "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself)."
**Context**: Modifier extensions in the Endpoint resource must not alter the meaning of any elements on the Resource or DomainResource. This ensures that the core semantics of the resource remain intact even when modifier extensions are present.
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
# REQ-016
**ID**: 16
**Summary**: Plan-Net Endpoint contained resource constraints - no nested resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources"
**Context**: This invariant (dom-2) ensures that contained resources within an Endpoint do not themselves contain other resources, preventing excessive nesting that could complicate processing.
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
# REQ-017
**ID**: 17
**Summary**: Plan-Net Endpoint contained resource constraints - reference requirement
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This invariant (dom-3) ensures that contained Endpoint resources are properly referenced, either by being referenced from elsewhere in the containing resource or by referring to the containing resource themselves.
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
# REQ-018
**ID**: 18
**Summary**: Plan-Net Endpoint contained resource constraints - no versionId or lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated"
**Context**: This invariant (dom-4) prevents contained Endpoint resources from having version identifiers or last updated timestamps in their metadata, as these are managed at the containing resource level.
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
# REQ-019
**ID**: 19
**Summary**: Plan-Net Endpoint contained resource constraints - no security label
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label"
**Context**: This invariant (dom-5) ensures that contained Endpoint resources do not have security labels in their metadata, as security is managed at the containing resource level.
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
**Summary**: Endpoint managingOrganization SHALL reference Plan-Net Organization profile
**Requirement**: "managingOrganization [SHALL be a] Reference([Plan-Net Organization])"
**Context**: The managingOrganization element identifies the organization that manages the endpoint. This reference must conform to the Plan-Net Organization profile, ensuring consistency across the Plan-Net directory.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.57.1 Resource Profile: Plan-Net Endpoint
**Grouping**: Endpoint
