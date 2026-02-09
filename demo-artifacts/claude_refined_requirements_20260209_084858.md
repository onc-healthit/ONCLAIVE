# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Organization search parameter support for type
**Requirement**: "Select Organizations of the specified type using Parameter `type`:`token` [with] Expression `Organization.type`"
**Context**: This requirement defines a search parameter for the Organization resource that allows searching by organization type. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple values separated by comma where at least one must be true). Allowed modifier is text.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.43.1 SearchParameter: Plannet_sp_organization_type
**Grouping**: Organization
---

---
# REQ-002
**ID**: 02
**Summary**: Support for Organization name search parameter
**Requirement**: "Select Organizations with the specified name [using Parameter `name`:`string` on Resource Organization with Expression `Organization.name | Organization.alias`]"
**Context**: This search parameter allows filtering of Organization resources by their name or alias elements. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The exact and contains modifiers are allowed.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.40.1 SearchParameter: Plannet_sp_organization_name
**Grouping**: Organization
---

---
# REQ-003
**ID**: 03
**Summary**: Organization endpoint search parameter support
**Requirement**: "Select Organizations with the specified endpoint [using search parameter `endpoint`:`reference` on Organization resource with Expression `Organization.endpoint` targeting Endpoint resources]"
**Context**: The implementation guide defines a search parameter for Organization resources that allows searching by associated endpoint. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The allowed chain is organization.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.39.1 SearchParameter: Plannet_sp_organization_endpoint
**Grouping**: Organization
---

---
# REQ-004
**ID**: 04
**Summary**: Health Plan API Actor SHALL support searching Organizations by period parameter
**Requirement**: "Select Organization entries available during the specified period" using Parameter `period`:`date` with Expression `Organization.extension.where(url='http://hl7.org/fhir/StructureDefinition/organization-period').value`
**Context**: The SearchParameter Plannet_sp_organization_period enables searching for Organization resources based on the period during which they are available. The parameter supports multipleOr (parameter may have multiple comma-separated values where at least one must be true). For multipleAnd, it's up to the server whether the parameter may repeat to specify multiple values that must all be true.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.42.1 SearchParameter: Plannet_sp_organization_period
**Grouping**: Organization
---

---
# REQ-005
**ID**: 05
**Summary**: Health Plan API Actor SHALL support searching Organizations by partof parameter
**Requirement**: "Select Organizations that are part of the specified organization" using Parameter `partof`:`reference` with Expression `Organization.partOf`
**Context**: The SearchParameter Plannet_sp_organization_partof enables searching for Organization resources that are part of a specified organization. Target Resources are Organization. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). Allowed chains are: name, address, type.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.41.1 SearchParameter: Plannet_sp_organization_partof
**Grouping**: Organization
---

---
# REQ-006
**ID**: 06
**Summary**: Health Plan API Actor SHALL support searching Organization by address parameter
**Requirement**: "Select organizations with the specified address (matches any of the string elements of an address)" using the search parameter `address` of type `string` on the Organization resource with expression `Organization.address`
**Context**: The SearchParameter definition Plannet_sp_organization_address specifies that servers must support searching for Organization resources by the address search parameter. This parameter is of type string and uses the expression Organization.address. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple comma-separated values where at least one must be true), with the exact and contains modifiers allowed.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.38.1 SearchParameter: Plannet_sp_organization_address
**Grouping**: Organization
---

---
# REQ-007
**ID**: 07
**Summary**: Server SHALL support search parameter 'period' on OrganizationAffiliation resource
**Requirement**: "Select Organization Affiliations available in the specified period" using search parameter `period` of type `date` with Expression `OrganizationAffiliation.period` with multipleAnd [It's up to the server whether the parameter may repeat in order to specify multiple values that must all be true] and multipleOr [The parameter may have multiple values (separated by comma) where at least one must be true] capabilities
**Context**: This search parameter enables querying OrganizationAffiliation resources by the time period during which the affiliation is active. The parameter supports OR logic for multiple values and optionally AND logic at server discretion.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.33.1 SearchParameter: Plannet_sp_organizationaffiliation_period
**Grouping**: Organization
---

---
# REQ-008
**ID**: 08
**Summary**: Server SHALL support search parameter 'specialty' on OrganizationAffiliation resource
**Requirement**: "Select OrganizationAffiliations associated with the specified specialty" using search parameter `specialty` of type `token` with Expression `OrganizationAffiliation.specialty` with multipleAnd [The parameter may repeat in order to specify multiple values that must all be true] and multipleOr [The parameter may have multiple values (separated by comma) where at least one must be true] capabilities, and allowed modifier: text
**Context**: This search parameter enables querying OrganizationAffiliation resources by the specialty associated with the affiliation. The parameter supports both AND and OR logic for multiple values and allows text-based searching with the text modifier.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.37.1 SearchParameter: Plannet_sp_organizationaffiliation_specialty
**Grouping**: Organization
---

---
# REQ-009
**ID**: 09
**Summary**: Server SHALL support coverage-area search parameter on Organization resource
**Requirement**: "Select health insurance provider networks available in a region described by the specified location [using the coverage-area search parameter on Organization resource]"
**Context**: The Plannet_sp_network_coverage_area search parameter enables searching for Organization resources (specifically health insurance provider networks) by coverage area. The parameter is of type reference and uses the expression `Organization.extension.where(url='http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/location-reference')` to target Location resources. The parameter supports both multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true).
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.28.1 SearchParameter: Plannet_sp_network_coverage_area
**Grouping**: Organization
---

---
# REQ-010
**ID**: 10
**Summary**: Extension URL SHALL be fixed value for org-description extension
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement specifies that the Extension.url element for the org-description extension must be a URI pointing to the Structure Definition. The fixed value is specified as `http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/org-description`.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization
---

---
# REQ-011
**ID**: 11
**Summary**: Extension value[x] must be present with cardinality 1..1
**Requirement**: "Extension.value[x] [Control]: 1.1"
**Context**: The org-description extension requires that the value[x] element be present with a cardinality of 1..1 (exactly one occurrence). This value should be of type string to provide the human-readable description of an organization. The element is marked as Must Support.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization
---

---
# REQ-012
**ID**: 12
**Summary**: Extension must satisfy ext-1 invariant requiring either extensions or value[x], not both
**Requirement**: "Must have either extensions or value[x], not both (`extension.exists() != value.exists()`)"
**Context**: The org-description extension must conform to the ext-1 invariant, which states that an extension must have either nested extensions or a value[x], but not both. This ensures proper structure of the extension.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization
---

---
# REQ-013
**ID**: 13
**Summary**: All FHIR elements must satisfy ele-1 invariant
**Requirement**: "All FHIR elements must have a @value or children (`hasValue() or (children().count() > id.count())`)"
**Context**: The org-description extension and its sub-elements must conform to the ele-1 invariant, which requires that all FHIR elements have either a value or children elements (excluding the id element). This ensures that elements are not empty.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.74.1 Extension: OrgDescription - Detailed Descriptions
**Grouping**: Organization
---

---
# REQ-014
**ID**: 14
**Summary**: Plan-Net Server SHALL support search-type and read interactions on Organization resource
**Requirement**: "A Server SHALL support search-type, read [on Organization resource]."
**Context**: This requirement mandates that the server must support the ability to search for Organization resources and read individual Organization resources by their logical ID.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization
---

---
# REQ-015
**ID**: 15
**Summary**: Plan-Net Server SHOULD support vread interaction on Organization resource
**Requirement**: "A Server SHOULD support vread [on Organization resource]."
**Context**: This requirement recommends that the server should support retrieving specific historical versions of an Organization resource using the version-aware read (vread) operation.
**Conformance**: "SHOULD"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization
---

---
# REQ-016
**ID**: 16
**Summary**: Plan-Net Server SHALL support reading Organization resource by id
**Requirement**: "A Server SHALL be capable of returning a Organization resource using: `GET [base]/Organization/[id]`"
**Context**: This requirement mandates that the server must support retrieving a specific Organization resource using its logical ID via a GET operation.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization
---

---
# REQ-017
**ID**: 17
**Summary**: Plan-Net Server SHOULD support vread on Organization resource by id and version
**Requirement**: "A Server SHOULD be capable of returning a Organization resource using: `GET [base]/Organization/[id]/_history/vid`"
**Context**: This requirement recommends that the server should support retrieving a specific version of an Organization resource using its logical ID and version ID.
**Conformance**: "SHOULD"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization
---

---
# REQ-018
**ID**: 18
**Summary**: Plan-Net Server SHALL support _include parameters for Organization resource
**Requirement**: "A Server SHALL be capable of supporting the following _includes: Organization:partof - `GET [base]/Organization?[parameter=value]&_include=Organization:partof`; Organization:endpoint - `GET [base]/Organization?[parameter=value]&_include=Organization:endpoint`; Organization:coverage-area - `GET [base]/Organization?[parameter=value]&_include=Organization:coverage-area`"
**Context**: This requirement mandates that the server must support including referenced parent Organization, Endpoint, and coverage-area Location resources when searching for Organization resources using the _include parameter.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization
---

---
# REQ-019
**ID**: 19
**Summary**: Plan-Net Server SHALL support _revinclude parameters for Organization resource
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: Endpoint:organization - `GET [base]/Organization?[parameter=value]&_revinclude=Endpoint:organization`; HealthcareService:organization - `GET [base]/Organization?[parameter=value]&_revinclude=HealthcareService:organization`; InsurancePlan:administered-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:administered-by`; InsurancePlan:owned-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:owned-by`; OrganizationAffiliation:primary-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:primary-organization`; PractitionerRole:organization - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:organization`; PractitionerRole:network - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:network`; OrganizationAffiliation:participating-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:participating-organization`"
**Context**: This requirement mandates that the server must support reverse includes to retrieve Endpoint, HealthcareService, InsurancePlan, OrganizationAffiliation, and PractitionerRole resources that reference the Organization resources in the search results.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization
---

---
# REQ-020
**ID**: 20
**Summary**: Plan-Net Server SHALL support search parameters on Organization resource
**Requirement**: "A Server SHALL support the following search parameters on Organization: partof, endpoint, address, name, _id, _lastUpdated, type, coverage-area"
**Context**: This requirement mandates that the server must support searching for Organization resources using the specified reference parameters (partof, endpoint, coverage-area), string parameters (address, name), token parameter (type), and standard parameters (_id, _lastUpdated).
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.5 Organization
**Grouping**: Organization
---

---
# REQ-021
**ID**: 21
**Summary**: Organization resource SHALL have at least a name or identifier
**Requirement**: "The organization SHALL at least have a name or an identifier, and possibly more than one"
**Context**: This is a fundamental validation rule (invariant org-1) for the Organization resource in the Plan-Net Network profile, ensuring that every organization can be uniquely identified or referenced.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization.identifier, Organization.name
**Grouping**: Organization
---

---
# REQ-022
**ID**: 22
**Summary**: Contained Organization resource SHALL NOT contain nested Resources
**Requirement**: "If the resource is contained in another resource, it SHALL NOT contain nested Resources"
**Context**: This is invariant dom-2 that prevents nested containment of resources, which is not permitted in FHIR resource containment patterns.
**Conformance**: "SHALL NOT"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Only applies if the Organization resource is contained in another resource
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization
**Grouping**: Organization
---

---
# REQ-023
**ID**: 23
**Summary**: Contained Organization resource SHALL be referred to or refer to containing resource
**Requirement**: "If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource"
**Context**: This is invariant dom-3 ensuring that contained resources are properly referenced within the containing resource structure.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Only applies if the Organization resource is contained in another resource
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization
**Grouping**: Organization
---

---
# REQ-024
**ID**: 24
**Summary**: Contained Organization resource SHALL NOT have meta.versionId or meta.lastUpdated
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated"
**Context**: This is invariant dom-4 that restricts metadata versioning information on contained resources.
**Conformance**: "SHALL NOT"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Only applies if the Organization resource is contained in another resource
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization
**Grouping**: Organization
---

---
# REQ-025
**ID**: 25
**Summary**: Contained Organization resource SHALL NOT have security label
**Requirement**: "If a resource is contained in another resource, it SHALL NOT have a security label"
**Context**: This is invariant dom-5 that prevents security labels on contained resources.
**Conformance**: "SHALL NOT"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Only applies if the Organization resource is contained in another resource
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization
**Grouping**: Organization
---

---
# REQ-026
**ID**: 26
**Summary**: Organization identifier.value SHALL be urn:ietf:rfc:3986 if full URI
**Requirement**: "If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986"
**Context**: This requirement ensures proper representation of URI-based identifiers in the Organization.identifier.value element.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Only applies if the identifier value is a full URI
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization.identifier.value
**Grouping**: Organization
---

---
# REQ-027
**ID**: 27
**Summary**: NPI identifier SHALL be 10 digits
**Requirement**: "NPI must be 10 digits"
**Context**: This is invariant us-core-16 validating the format of National Provider Identifier (NPI) values in the NPI identifier slice.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization.identifier:NPI
**Grouping**: Organization
---

---
# REQ-028
**ID**: 28
**Summary**: NPI check digit SHALL be valid per Luhn algorithm
**Requirement**: "NPI check digit must be valid (Luhn algorithm check)"
**Context**: This is invariant us-core-17 that validates the check digit of NPI identifiers using the Luhn algorithm.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization.identifier:NPI
**Grouping**: Organization
---

---
# REQ-029
**ID**: 29
**Summary**: CLIA number SHALL be 10 digits with letter D in third position
**Requirement**: "CLIA number must be 10 digits with a letter 'D' in third position"
**Context**: This is invariant us-core-18 validating the format of Clinical Laboratory Improvement Amendments (CLIA) identifier values.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization.identifier:CLIA
**Grouping**: Organization
---

---
# REQ-030
**ID**: 30
**Summary**: NAIC code SHALL be 5 digits
**Requirement**: "NAIC must be 5 digits"
**Context**: This is invariant us-core-19 validating the format of NAIC (National Association of Insurance Commissioners) code identifier values.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization.identifier:NAIC
**Grouping**: Organization
---

---
# REQ-031
**ID**: 31
**Summary**: Organization telecom SHALL NOT use 'home' use code
**Requirement**: "The telecom of an organization can never be of use 'home'"
**Context**: This is invariant org-3 that restricts the use code for organization contact points, as 'home' is not appropriate for organizational contacts.
**Conformance**: "SHALL NOT"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization.telecom
**Grouping**: Organization
---

---
# REQ-032
**ID**: 32
**Summary**: Organization address SHALL NOT use 'home' use code
**Requirement**: "An address of an organization can never be of use 'home'"
**Context**: This is invariant org-2 that restricts the use code for organization addresses, as 'home' is not appropriate for organizational addresses.
**Conformance**: "SHALL NOT"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: PlannetNetwork - Detailed Descriptions - Organization.address
**Grouping**: Organization
---

---
# REQ-033
**ID**: 33
**Summary**: Plan-Net Network Organization active status requirement
**Requirement**: "[The Plan-Net Network Organization] active [element has a] fixed value: true"
**Context**: The Plan-Net Network profile is based on the Organization resource and represents a healthcare provider insurance network. The active element indicates whether the organization's record is still in active use. For Plan-Net Network resources, this element must always be set to true.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: Plan-Net Network
**Grouping**: Organization
---

---
# REQ-034
**ID**: 34
**Summary**: Plan-Net Network Organization type requirement
**Requirement**: "[The Plan-Net Network Organization] type [element has cardinality] 1..1 [and binding to] Network Type VS ([required])"
**Context**: The Plan-Net Network profile requires that the type element be populated with exactly one value from the NetworkTypeVS value set. This element indicates the kind of organization, specifically identifying it as a network type.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: Plan-Net Network
**Grouping**: Organization
---

---
# REQ-035
**ID**: 35
**Summary**: Plan-Net Network Organization name requirement
**Requirement**: "[The Plan-Net Network Organization] name [element has cardinality] 1..1"
**Context**: The Plan-Net Network profile requires that the name element be populated. This element provides the name used for the organization and is mandatory for identification purposes.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: Plan-Net Network
**Grouping**: Organization
---

---
# REQ-036
**ID**: 36
**Summary**: Plan-Net Network Organization partOf requirement
**Requirement**: "[The Plan-Net Network Organization] partOf [element has cardinality] 1..1 [and is a] Reference([Plan-Net Organization])"
**Context**: The Plan-Net Network profile requires that the partOf element reference exactly one Plan-Net Organization. This element identifies the organization that manages the network.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: Plan-Net Network
**Grouping**: Organization
---

---
# REQ-037
**ID**: 37
**Summary**: Plan-Net Network Organization telecom prohibition
**Requirement**: "[The Plan-Net Network Organization] telecom [element has cardinality] 0..0"
**Context**: The Plan-Net Network profile prohibits the use of the telecom element at the Organization level. Contact information should be provided through the contact element instead.
**Conformance**: "SHALL NOT"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1 Resource Profile: Plan-Net Network
**Grouping**: Organization
---

---
# REQ-038
**ID**: 38
**Summary**: Plan-Net Network NPI identifier validation - 10 digits
**Requirement**: "NPI must be 10 digits: value.matches('^[0-9]{10}$')"
**Context**: When an NPI identifier is provided for a Plan-Net Network Organization, the value must match the specified regular expression pattern requiring exactly 10 digits. This is constraint us-core-16.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when an NPI identifier is provided for the organization.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization
---

---
# REQ-039
**ID**: 39
**Summary**: Plan-Net Network NPI identifier validation - Luhn algorithm
**Requirement**: "NPI check digit must be valid (Luhn algorithm check): (((select(value.substring(0,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(1,1).toInteger())+(select(value.substring(2,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(3,1).toInteger())+(select(value.substring(4,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(5,1).toInteger())+(select(value.substring(6,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(7,1).toInteger())+(select(value.substring(8,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(9,1).toInteger()) + 24)mod 10=0)"
**Context**: When an NPI identifier is provided for a Plan-Net Network Organization, the check digit must be valid according to the Luhn algorithm. This is constraint us-core-17.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when an NPI identifier is provided for the organization.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization
---

---
# REQ-040
**ID**: 40
**Summary**: Plan-Net Network CLIA identifier validation
**Requirement**: "CLIA number must be 10 digits with a letter \"D\" in third position: value.matches('^[0-9]{2}D[0-9]{7}$')"
**Context**: When a CLIA identifier is provided for a Plan-Net Network Organization, the value must match the specified regular expression pattern requiring 10 characters total with exactly 2 digits, followed by the letter "D", followed by 7 digits. This is constraint us-core-18.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when a CLIA identifier is provided for the organization.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization
---

---
# REQ-041
**ID**: 41
**Summary**: Plan-Net Network NAIC identifier validation
**Requirement**: "NAIC must be 5 digits: value.matches('^[0-9]{5}$')"
**Context**: When a NAIC identifier is provided for a Plan-Net Network Organization, the value must match the specified regular expression pattern requiring exactly 5 digits. This is constraint us-core-19.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when a NAIC identifier is provided for the organization.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.61.1.1.5 Constraints
**Grouping**: Organization
---

---
# REQ-042
**ID**: 42
**Summary**: Organization must have at least one type
**Requirement**: "[Organization.type] [cardinality] SHALL [be] 1..*"
**Context**: The Plan-Net Organization profile requires that organizations specify at least one type from the Organization Type VS value set to classify the kind of organization.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: Plan-Net Organization
**Grouping**: Organization
---

---
# REQ-043
**ID**: 43
**Summary**: Organization must have a name
**Requirement**: "[Organization.name] [cardinality] SHALL [be] 1..1"
**Context**: The Plan-Net Organization profile requires that organizations have a name used to identify the organization.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: Plan-Net Organization
**Grouping**: Organization
---

---
# REQ-044
**ID**: 44
**Summary**: Organization must have at least one address
**Requirement**: "[Organization.address] [cardinality] SHALL [be] 1..*"
**Context**: The Plan-Net Organization profile requires that organizations provide at least one address.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: Plan-Net Organization
**Grouping**: Organization
---

---
# REQ-045
**ID**: 45
**Summary**: Organization NPI identifier must be 10 digits
**Requirement**: "NPI must be 10 digits (`value.matches('^[0-9]{10}$')`)"
**Context**: This invariant (us-core-16) ensures that National Provider Identifier (NPI) values in the NPI identifier slice conform to the standard 10-digit format required by the NPI system.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Applies only when NPI identifier is provided
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions - Organization.identifier:NPI
**Grouping**: Organization
---

---
# REQ-046
**ID**: 46
**Summary**: Organization NPI check digit must be valid
**Requirement**: "NPI check digit must be valid (Luhn algorithm check) (`(((select(value.substring(0,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(1,1).toInteger())+(select(value.substring(2,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(3,1).toInteger())+(select(value.substring(4,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(5,1).toInteger())+(select(value.substring(6,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(7,1).toInteger())+(select(value.substring(8,1).toInteger()).select(iif($this<5, $this*2, (($this*2)-9))))+(value.substring(9,1).toInteger()) + 24)mod 10=0)`)"
**Context**: This invariant (us-core-17) validates that the NPI identifier's check digit is mathematically valid according to the Luhn algorithm, which is the standard validation algorithm for NPI numbers.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Applies only when NPI identifier is provided
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions - Organization.identifier:NPI
**Grouping**: Organization
---

---
# REQ-047
**ID**: 47
**Summary**: Organization CLIA number must be 10 digits with letter D in third position
**Requirement**: "CLIA number must be 10 digits with a letter 'D' in third position (`value.matches('^[0-9]{2}D[0-9]{7}$')`)"
**Context**: This invariant (us-core-18) ensures that Clinical Laboratory Improvement Amendments (CLIA) numbers conform to their standard format: two digits, followed by the letter 'D', followed by seven digits.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Applies only when CLIA identifier is provided
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions - Organization.identifier:CLIA
**Grouping**: Organization
---

---
# REQ-048
**ID**: 48
**Summary**: Organization NAIC code must be 5 digits
**Requirement**: "NAIC must be 5 digits (`value.matches('^[0-9]{5}$')`)"
**Context**: This invariant (us-core-19) ensures that NAIC (National Association of Insurance Commissioners) company codes conform to their standard 5-digit format used for identifying insurance payers.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Applies only when NAIC identifier is provided
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions - Organization.identifier:NAIC
**Grouping**: Organization
---

---
# REQ-049
**ID**: 49
**Summary**: Organization address text SHALL not contain content absent from parts
**Requirement**: "Applications updating an address SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part."
**Context**: This requirement ensures data consistency when both structured address parts (line, city, state, etc.) and a text representation are provided. The text should be a rendering of the parts, not contain additional information.
**Conformance**: "SHALL"
**Actor**: Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Applies when both text and address parts are present in an Organization address
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: PlannetOrganization - Detailed Descriptions - Organization.address.text
**Grouping**: Organization
---

---
# REQ-050
**ID**: 50
**Summary**: Organization active status must be true
**Requirement**: "[Organization.active] SHALL [be true]"
**Context**: The Plan-Net Organization profile requires that organizations have an active status set to true, indicating the organization's record is in active use.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: Plan-Net Organization
**Grouping**: Organization
---

---
# REQ-051
**ID**: 51
**Summary**: NPI identifier system must be fixed value
**Requirement**: "[Organization.identifier:NPI.system] SHALL [have Fixed Value]: http://hl7.org/fhir/sid/us-npi"
**Context**: The Plan-Net Organization profile requires that when an NPI identifier is present, its system element must be set to the fixed value http://hl7.org/fhir/sid/us-npi.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Applies when an NPI identifier slice is present
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: Plan-Net Organization
**Grouping**: Organization
---

---
# REQ-052
**ID**: 52
**Summary**: CLIA identifier system must be fixed value
**Requirement**: "[Organization.identifier:CLIA.system] SHALL [have Fixed Value]: urn:oid:2.16.840.1.113883.4.7"
**Context**: The Plan-Net Organization profile requires that when a CLIA identifier is present, its system element must be set to the fixed value urn:oid:2.16.840.1.113883.4.7.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Applies when a CLIA identifier slice is present
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: Plan-Net Organization
**Grouping**: Organization
---

---
# REQ-053
**ID**: 53
**Summary**: NAIC identifier system must be fixed value
**Requirement**: "[Organization.identifier:NAIC.system] SHALL [have Fixed Value]: urn:oid:2.16.840.1.113883.6.300"
**Context**: The Plan-Net Organization profile requires that when a NAIC identifier is present, its system element must be set to the fixed value urn:oid:2.16.840.1.113883.6.300.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: Applies when a NAIC identifier slice is present
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.62.1 Resource Profile: Plan-Net Organization
**Grouping**: Organization
---
