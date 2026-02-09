# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Server SHALL support role search parameter on PractitionerRole resource
**Requirement**: "Select PractitionerRoles with the specified role"
**Context**: The Plan-Net Implementation Guide defines a search parameter `role` of type `token` that enables searching for PractitionerRole resources based on their role/code. The expression used is `PractitionerRole.code`. This search parameter supports multipleAnd (the parameter may repeat to specify multiple values that must all be true) and multipleOr (the parameter may have multiple values separated by comma where at least one must be true). The allowed modifier is: text.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.50.1 SearchParameter: Plannet_sp_practitionerrole_role
**Grouping**: PractitionerRole

---
# REQ-002
**ID**: 02
**Summary**: PractitionerRole period search parameter support
**Requirement**: "Select PractitionerRoles available in the specified period [using search parameter `period`:`date` on PractitionerRole resource with Expression `PractitionerRole.period`]"
**Context**: The implementation guide defines a search parameter for PractitionerRole resources that allows searching by period of availability. The parameter supports multipleOr (parameter may have multiple comma-separated values where at least one must be true). It's up to the server whether the parameter may repeat for multipleAnd.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.48.1 SearchParameter: Plannet_sp_practitionerrole_period
**Grouping**: PractitionerRole

---
# REQ-003
**ID**: 03
**Summary**: Health Plan API Actor SHALL support specialty search parameter on PractitionerRole resource
**Requirement**: "Select PractitionerRoles associated with the specified specialty [using] Parameter `specialty`:`token` [with] Expression `PractitionerRole.specialty`"
**Context**: This search parameter allows querying PractitionerRole resources by their specialty using a token-based search. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (comma-separated values where at least one must be true). The text modifier is allowed.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.52.1 SearchParameter: Plannet_sp_practitionerrole_specialty
**Grouping**: PractitionerRole

---
# REQ-004
**ID**: 04
**Summary**: Health Plan API Actor SHALL support searching PractitionerRole by endpoint parameter
**Requirement**: "Select PractitionerRoles with the specified endpoint" using the search parameter `endpoint` of type `reference` on the PractitionerRole resource with expression `PractitionerRole.endpoint` targeting Endpoint resources
**Context**: The SearchParameter definition Plannet_sp_practitionerrole_endpoint specifies that servers must support searching for PractitionerRole resources by the endpoint search parameter. This parameter is of type reference and uses the expression PractitionerRole.endpoint, targeting Endpoint resources. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple comma-separated values where at least one must be true), with chains allowed for organization.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.44.1 SearchParameter: Plannet_sp_practitionerrole_endpoint
**Grouping**: PractitionerRole

---
# REQ-005
**ID**: 05
**Summary**: Server SHALL support search parameter 'service' on PractitionerRole resource
**Requirement**: "Select PractitionerRoles providing the specified service" using search parameter `service` of type `reference` with Expression `PractitionerRole.healthcareService` targeting [HealthcareService] resources with multipleAnd [The parameter may repeat in order to specify multiple values that must all be true] and multipleOr [The parameter may have multiple values (separated by comma) where at least one must be true] capabilities, and allowed chains: service-category, organization, location
**Context**: This search parameter enables querying PractitionerRole resources by the healthcare services they provide. The parameter supports both AND and OR logic for multiple values and allows chaining to related resources.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.51.1 SearchParameter: Plannet_sp_practitionerrole_service
**Grouping**: PractitionerRole

---
# REQ-006
**ID**: 06
**Summary**: Server SHALL support search parameter 'practitioner' on PractitionerRole resource
**Requirement**: "Select roles filled by the specified practitioner" using search parameter `practitioner` of type `reference` with Expression `PractitionerRole.practitioner` targeting [Practitioner] resources with multipleAnd [The parameter may repeat in order to specify multiple values that must all be true] and multipleOr [The parameter may have multiple values (separated by comma) where at least one must be true] capabilities, and allowed chain: name
**Context**: This search parameter enables querying PractitionerRole resources by the practitioner who fills the role. The parameter supports both AND and OR logic for multiple values and allows chaining to the practitioner's name.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.49.1 SearchParameter: Plannet_sp_practitionerrole_practitioner
**Grouping**: PractitionerRole

---
# REQ-007
**ID**: 07
**Summary**: Server SHALL support search parameter 'location' on PractitionerRole resource
**Requirement**: "Select PractitionerRoles available at the specified location" using search parameter `location` of type `reference` with Expression `PractitionerRole.location` targeting [Location] resources with multipleAnd [The parameter may repeat in order to specify multiple values that must all be true] and multipleOr [The parameter may have multiple values (separated by comma) where at least one must be true] capabilities, and allowed chains: address, address-postalcode, address-city, address-state, organization, type
**Context**: This search parameter enables querying PractitionerRole resources by the location where the practitioner performs the role. The parameter supports both AND and OR logic for multiple values and allows chaining to location-related attributes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.45.1 SearchParameter: Plannet_sp_practitionerrole_location
**Grouping**: PractitionerRole

---
# REQ-008
**ID**: 08
**Summary**: Plan-Net Server SHALL support search parameter 'organization' on PractitionerRole resource
**Requirement**: "Parameter `organization`:`reference` - Select PractitionerRoles available at the specified organization. Resource [PractitionerRole]. Expression `PractitionerRole.organization`. The parameter may repeat in order to specify multiple values that must all be true (multipleAnd). The parameter may have multiple values (separated by comma) where at least one must be true (multipleOr). Chains Allowed: name, address, partof, type"
**Context**: This search parameter enables querying PractitionerRole resources by their associated organization reference. The parameter supports both multipleAnd and multipleOr semantics, and allows chaining to search by organization characteristics such as name, address, partof, and type.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.47.1 SearchParameter: Plannet_sp_practitionerrole_organization
**Grouping**: PractitionerRole

---
# REQ-009
**ID**: 09
**Summary**: Support for network search parameter on PractitionerRole resource
**Requirement**: "Parameter `network`:`reference` - Select roles where the practitioner is a member of the specified health insurance provider network. Expression: `PractitionerRole.extension.where(url='http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network-reference')`. The parameter may repeat in order to specify multiple values that must all be true (multipleAnd). The parameter may have multiple values (separated by comma) where at least one must be true (multipleOr). Chains Allowed: name, address, partof, type"
**Context**: This search parameter enables searching PractitionerRole resources by the health insurance provider network to which the practitioner belongs. The network is specified via an extension on the PractitionerRole resource. The search supports both AND and OR combinations of multiple values, as well as chained searches on related Organization attributes.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.46.1 SearchParameter: Plannet_sp_practitionerrole_network
**Grouping**: PractitionerRole

---
# REQ-010
**ID**: 10
**Summary**: NetworkReference Extension Invariant ext-1
**Requirement**: "Must have either extensions or value[x], not both (extension.exists() != value.exists())"
**Context**: This is a base FHIR invariant (ext-1) that applies to the NetworkReference extension structure. An extension element must contain either nested extensions or a value[x] element, but not both simultaneously. This ensures proper extension structure according to FHIR specifications.
**Conformance**: SHALL
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.72.1 Extension: NetworkReference - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-011
**ID**: 11
**Summary**: Plan-Net Server SHALL support search-type and read interactions on PractitionerRole resource
**Requirement**: "A Server SHALL support search-type, read [on PractitionerRole resource]."
**Context**: This requirement mandates that the server must support the ability to search for PractitionerRole resources and read individual PractitionerRole resources by their logical ID.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-012
**ID**: 12
**Summary**: Plan-Net Server SHOULD support vread interaction on PractitionerRole resource
**Requirement**: "A Server SHOULD support vread [on PractitionerRole resource]."
**Context**: This requirement recommends that the server should support retrieving specific historical versions of a PractitionerRole resource using the version-aware read (vread) operation.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-013
**ID**: 13
**Summary**: Plan-Net Server SHALL support reading PractitionerRole resource by id
**Requirement**: "A Server SHALL be capable of returning a PractitionerRole resource using: `GET [base]/PractitionerRole/[id]`"
**Context**: This requirement mandates that the server must support retrieving a specific PractitionerRole resource using its logical ID via a GET operation.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-014
**ID**: 14
**Summary**: Plan-Net Server SHOULD support vread on PractitionerRole resource by id and version
**Requirement**: "A Server SHOULD be capable of returning a PractitionerRole resource using: `GET [base]/PractitionerRole/[id]/_history/vid`"
**Context**: This requirement recommends that the server should support retrieving a specific version of a PractitionerRole resource using its logical ID and version ID.
**Conformance**: SHOULD
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-015
**ID**: 15
**Summary**: Plan-Net Server SHALL support _include parameters for PractitionerRole resource
**Requirement**: "A Server SHALL be capable of supporting the following _includes: PractitionerRole:practitioner - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:practitioner`; PractitionerRole:organization - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:organization`; PractitionerRole:location - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:location`; PractitionerRole:service - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:service`; PractitionerRole:network - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:network`; PractitionerRole:endpoint - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:endpoint`"
**Context**: This requirement mandates that the server must support including referenced Practitioner, Organization, Location, HealthcareService, Network, and Endpoint resources when searching for PractitionerRole resources using the _include parameter.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-016
**ID**: 16
**Summary**: Plan-Net Server SHALL support search parameters on PractitionerRole resource
**Requirement**: "A Server SHALL support the following search parameters on PractitionerRole: practitioner, organization, location, service, network, endpoint, role, specialty, _id, _lastUpdated"
**Context**: This requirement mandates that the server must support searching for PractitionerRole resources using the specified reference parameters (practitioner, organization, location, service, network, endpoint), token parameters (role, specialty), and standard parameters (_id, _lastUpdated).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.1.1.2.8 PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-017
**ID**: 17
**Summary**: NewPatients Extension acceptingPatients sub-extension SHALL use required binding to AcceptingPatientsVS
**Requirement**: "The codes SHALL be taken from [Accepting Patients Codes VS](ValueSet-AcceptingPatientsVS.html)([required](http://hl7.org/fhir/R4/terminologies.html#required) to `http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/AcceptingPatientsVS`)"
**Context**: The NewPatients extension is used in PractitionerRole, HealthcareService, and Location profiles to indicate whether new patients are being accepted. The acceptingPatients sub-extension uses a CodeableConcept value that must be bound to the AcceptingPatientsVS value set with required binding strength, meaning only codes from this value set are permitted.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions, Element 10 (Extension.extension:acceptingPatients.value[x])
**Grouping**: PractitionerRole

---
# REQ-018
**ID**: 18
**Summary**: NewPatients Extension new-patients-characteristics invariant SHALL be satisfied
**Requirement**: "If no new patients are accepted, no characteristics are allowed (`extension.where(url='acceptingPatients').value.ofType(CodeableConcept).coding.where(code = 'no') implies extension.where(url='characteristics').empty()`)"
**Context**: The NewPatients extension enforces a business rule through the new-patients-characteristics invariant: when the acceptingPatients sub-extension has a code value of 'no', the characteristics sub-extension must be empty. This ensures that characteristics of accepted patients are not specified when no new patients are being accepted.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This constraint applies when the acceptingPatients code equals 'no'
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: Extension: NewPatients - Detailed Descriptions, Element 0 (Extension)
**Grouping**: PractitionerRole

---
# REQ-019
**ID**: 19
**Summary**: PractitionerRole active status requirement
**Requirement**: "Whether this practitioner role record is in active use. [PractitionerRole.active] Required Pattern: true"
**Context**: The Plan-Net PractitionerRole profile requires that the active element be present and set to true, indicating that the practitioner role record must be in active use. This is a mandatory field with a required pattern constraint.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-020
**ID**: 20
**Summary**: PractitionerRole qualification status requirement
**Requirement**: "[PractitionerRole.extension:qualification.extension:status.value[x]] Binding: Qualification Status VS (required). Fixed Value: active"
**Context**: The qualification extension's status sub-extension must have a value of "active" from the required QualificationStatusVS value set. This ensures that all qualifications reported are currently active.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification extension is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-021
**ID**: 21
**Summary**: PractitionerRole telecom system requirement
**Requirement**: "[PractitionerRole.telecom.system] 1.1 [code] phone | fax | email | pager | url | sms | other Binding: ContactPointSystem (required)"
**Context**: The telecom system element is mandatory (cardinality 1..1) and must contain a code from the required ContactPointSystem value set specifying the telecommunications form for the contact point.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when telecom information is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-022
**ID**: 22
**Summary**: PractitionerRole telecom value requirement
**Requirement**: "[PractitionerRole.telecom.value] 1.1 [string] The actual contact point details"
**Context**: The telecom value element is mandatory (cardinality 1..1) when contact information is provided, and must contain the actual contact point details in a form meaningful to the designated communication system.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when telecom information is provided
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-023
**ID**: 23
**Summary**: PractitionerRole not available description requirement
**Requirement**: "[PractitionerRole.notAvailable.description] 1.1 [string] Reason presented to the user explaining why time not available"
**Context**: When the notAvailable element is used to indicate times when the practitioner is not available, a description is mandatory (cardinality 1..1) to explain the reason to users.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the notAvailable element is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-024
**ID**: 24
**Summary**: PractitionerRole qualification code requirement
**Requirement**: "[PractitionerRole.extension:qualification.extension:code] 1.1 [Extension] [value[x]] 1.1 [CodeableConcept] Value of extension Binding: Individual Specialties, Degrees, Licenses, and Certificates VS (extensible)"
**Context**: The qualification extension requires a code sub-extension (cardinality 1..1) with a CodeableConcept value bound extensibly to the IndividualSpecialtyAndDegreeLicenseCertificateVS value set to identify the type of qualification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification extension is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-025
**ID**: 25
**Summary**: PractitionerRole must have contact information or endpoint reference
**Requirement**: "pd-1: SHALL have contact information or a reference to an Endpoint"
**Context**: The PractitionerRole profile includes a constraint (pd-1) requiring that either contact information (telecom) or a reference to an Endpoint be present. This ensures that there is a means to contact or access services for the practitioner role.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-026
**ID**: 26
**Summary**: PractitionerRole must reference practitioner, organization, healthcare service, or location
**Requirement**: "practitioner-or-organization-or-healthcareservice-or-location: If PlannetPractitionerRole.practitioner is absent (PlannetPractitionerRole.organization, PlannetPractitionerRole.healthcareservice, PlannetPractitionerRole.location) must be present: practitioner.exists() or (organization.exists() or healthcareService.exists() or location.exists())"
**Context**: The PractitionerRole must reference at least one of: a Practitioner, an Organization, a HealthcareService, or a Location. This constraint ensures that the role is associated with at least one context entity.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-027
**ID**: 27
**Summary**: PractitionerRole code value set binding
**Requirement**: "[PractitionerRole.code] Binding: PractitionerRole Code VS (required)"
**Context**: The code element, which specifies the roles the practitioner is authorized to perform, must use values from the required PractitionerRoleVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the code element is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-028
**ID**: 28
**Summary**: PractitionerRole specialty value set binding
**Requirement**: "[PractitionerRole.specialty] Binding: Individual and Group Specialties (required)"
**Context**: The specialty element, which specifies the practitioner's specialty, must use values from the required IndividualAndGroupSpecialtiesVS value set.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the specialty element is present
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: Plan-Net PractitionerRole
**Grouping**: PractitionerRole

---
# REQ-029
**ID**: 29
**Summary**: PractitionerRole SHALL NOT contain nested Resources constraint
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources"
**Context**: Invariant constraint on the PractitionerRole resource ensuring that contained resources do not themselves contain other resources, maintaining a flat containment structure.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies only if the PractitionerRole resource is contained in another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-030
**ID**: 30
**Summary**: PractitionerRole SHALL be referred to or refer to containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: Invariant constraint ensuring that contained PractitionerRole resources are properly referenced within the parent resource structure.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies only if the PractitionerRole resource is contained in another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-031
**ID**: 31
**Summary**: Contained PractitionerRole SHALL NOT have meta.versionId or meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated"
**Context**: Invariant constraint preventing contained resources from having versioning metadata.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies only if the PractitionerRole resource is contained in another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-032
**ID**: 32
**Summary**: Contained PractitionerRole SHALL NOT have security label
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label"
**Context**: Invariant constraint ensuring contained resources do not have independent security labeling.
**Conformance**: SHALL NOT
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies only if the PractitionerRole resource is contained in another resource.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-033
**ID**: 33
**Summary**: PractitionerRole SHALL have contact information or Endpoint reference
**Requirement**: "SHALL have contact information or a reference to an Endpoint (telecom.exists() or endpoint.exists())"
**Context**: Business rule requiring that PractitionerRole resources provide either direct contact information via telecom or a reference to an Endpoint resource for technical connectivity.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-034
**ID**: 34
**Summary**: PractitionerRole SHALL have practitioner, organization, healthcare service, or location
**Requirement**: "SHALL have a practitioner, an organization, a healthcare service, or a location. (practitioner.exists() or organization.exists() or healthcareService.exists() or location.exists())"
**Context**: US Core constraint requiring that a PractitionerRole must reference at least one of: a practitioner, an organization, a healthcare service, or a location to provide context for the role.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-035
**ID**: 35
**Summary**: If PractitionerRole.practitioner is absent, other references must be present
**Requirement**: "If PlannetPractitionerRole.practitioner is absent (PlannetPractitionerRole.organization, PlannetPractitionerRole.healthcareservice, PlannetPractitionerRole.location) must be present (practitioner.exists() or (organization.exists() or healthcareService.exists() or location.exists()))"
**Context**: Plan-Net specific constraint ensuring that if no practitioner is referenced, the role must be associated with an organization, healthcare service, or location to provide necessary context.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when PractitionerRole.practitioner is absent.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-036
**ID**: 36
**Summary**: PractitionerRole.active must be true when provided
**Requirement**: "[PractitionerRole.active Pattern Value is] true"
**Context**: The PractitionerRole profile requires that when the active element is populated, it must have a value of true, indicating the role record is in active use.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-037
**ID**: 37
**Summary**: PractitionerRole qualification status must be 'active'
**Requirement**: "[PractitionerRole.extension:qualification.extension:status.value[x] Fixed Value is] active"
**Context**: The qualification extension's status sub-extension must have a fixed value of 'active' to indicate the qualification is currently valid.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: False
**Conditionality Details**: NA
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-038
**ID**: 38
**Summary**: PractitionerRole telecom system is required
**Requirement**: "[PractitionerRole.telecom.system Control is] 1..1"
**Context**: The telecom element must include a system to identify the type of contact point (phone, fax, email, etc.).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when PractitionerRole.telecom is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-039
**ID**: 39
**Summary**: PractitionerRole telecom value is required
**Requirement**: "[PractitionerRole.telecom.value Control is] 1..1"
**Context**: The telecom element must include the actual contact point value (e.g., phone number, email address).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when PractitionerRole.telecom is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-040
**ID**: 40
**Summary**: PractitionerRole notAvailable description is required
**Requirement**: "[PractitionerRole.notAvailable.description Control is] 1..1"
**Context**: When a practitioner is not available, a description explaining the reason must be provided for user understanding.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when PractitionerRole.notAvailable is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-041
**ID**: 41
**Summary**: PractitionerRole qualification code is required
**Requirement**: "[PractitionerRole.extension:qualification.extension:code Control is] 1..1"
**Context**: The qualification extension must include a code identifying the type of qualification (e.g., specialty, degree, license, certificate).
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification extension is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-042
**ID**: 42
**Summary**: PractitionerRole qualification status is required
**Requirement**: "[PractitionerRole.extension:qualification.extension:status Control is] 1..1"
**Context**: The qualification extension must include a status indicating whether the qualification is active, inactive, or has another status.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification extension is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-043
**ID**: 43
**Summary**: PractitionerRole qualification identifier value is required when identifier present
**Requirement**: "[PractitionerRole.extension:qualification.extension:identifier.value[x] Control is] 1..1"
**Context**: When an identifier is provided for a qualification, its value must be populated to uniquely identify the qualification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification identifier extension is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-044
**ID**: 44
**Summary**: PractitionerRole qualification code value is required
**Requirement**: "[PractitionerRole.extension:qualification.extension:code.value[x] Control is] 1..1"
**Context**: The qualification code extension must include a value specifying the qualification type.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification code extension is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-045
**ID**: 45
**Summary**: PractitionerRole qualification issuer value is required when issuer present
**Requirement**: "[PractitionerRole.extension:qualification.extension:issuer.value[x] Control is] 1..1"
**Context**: When an issuer is specified for a qualification, the issuer reference must be populated to identify the organization that issued the qualification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification issuer extension is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-046
**ID**: 46
**Summary**: PractitionerRole qualification status value is required
**Requirement**: "[PractitionerRole.extension:qualification.extension:status.value[x] Control is] 1..1"
**Context**: The qualification status extension must include a value indicating the current status of the qualification.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification status extension is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-047
**ID**: 47
**Summary**: PractitionerRole qualification period value is required when period present
**Requirement**: "[PractitionerRole.extension:qualification.extension:period.value[x] Control is] 1..1"
**Context**: When a period is specified for a qualification, it must include start and/or end dates to define the validity timeframe.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification period extension is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole

---
# REQ-048
**ID**: 48
**Summary**: PractitionerRole qualification whereValid value is required when whereValid present
**Requirement**: "[PractitionerRole.extension:qualification.extension:whereValid.value[x] Control is] 1..1"
**Context**: When whereValid is specified for a qualification, it must include a value indicating the geographic location or jurisdiction where the qualification is valid.
**Conformance**: SHALL
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: True
**Conditionality Details**: This requirement applies when the qualification whereValid extension is present.
**Verifiability**: Yes
**Verifiability Details**: Automation
**Section**: 11.65.1 Resource Profile: PlannetPractitionerRole - Detailed Descriptions
**Grouping**: PractitionerRole
