# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

# REQ-001
**ID**: 01
**Summary**: Support for primary-organization search parameter on OrganizationAffiliation
**Requirement**: "Parameter `primary-organization`:`reference` [shall be supported to] Select roles offered by the specified organization [on OrganizationAffiliation resource with Expression `OrganizationAffiliation.organization`]"
**Context**: The Plan-Net Implementation Guide defines a search parameter 'primary-organization' for the OrganizationAffiliation resource. This parameter enables searching for organization affiliations based on the primary organization. The search uses a reference type parameter with the expression `OrganizationAffiliation.organization` and targets Organization resources. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple values where at least one must be true) semantics. Allowed chains include: type, address, name, partof.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.34.1 SearchParameter: Plannet_sp_organizationaffiliation_primary_organization
**Grouping**: OrganizationAffiliation

---

# REQ-002
**ID**: 02
**Summary**: Support for participating-organization search parameter on OrganizationAffiliation
**Requirement**: "Parameter `participating-organization`:`reference` [shall be supported to] Select roles filled by the specified organization [on OrganizationAffiliation resource with Expression `OrganizationAffiliation.participatingOrganization`]"
**Context**: The Plan-Net Implementation Guide defines a search parameter 'participating-organization' for the OrganizationAffiliation resource. This parameter enables searching for organization affiliations based on the participating organization. The search uses a reference type parameter with the expression `OrganizationAffiliation.participatingOrganization` and targets Organization resources. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (multiple values where at least one must be true) semantics. Allowed chains include: type, address, name, partof.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.32.1 SearchParameter: Plannet_sp_organizationaffiliation_participating_organization
**Grouping**: OrganizationAffiliation

---

# REQ-003
**ID**: 03
**Summary**: Plan-Net Server SHALL support search-type and read interactions on OrganizationAffiliation resource
**Requirement**: "A Server SHALL support search-type, read [on OrganizationAffiliation resource]."
**Context**: This requirement mandates that the server must support the ability to search for OrganizationAffiliation resources and read individual OrganizationAffiliation resources by their logical ID.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: OrganizationAffiliation

---

# REQ-004
**ID**: 04
**Summary**: Plan-Net Server SHOULD support vread interaction on OrganizationAffiliation resource
**Requirement**: "A Server SHOULD support vread [on OrganizationAffiliation resource]."
**Context**: This requirement recommends that the server should support retrieving specific historical versions of an OrganizationAffiliation resource using the version-aware read (vread) operation.
**Conformance**: "SHOULD"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: OrganizationAffiliation

---

# REQ-005
**ID**: 05
**Summary**: Plan-Net Server SHALL support reading OrganizationAffiliation resource by id
**Requirement**: "A Server SHALL be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]`"
**Context**: This requirement mandates that the server must support retrieving a specific OrganizationAffiliation resource using its logical ID via a GET operation.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: OrganizationAffiliation

---

# REQ-006
**ID**: 06
**Summary**: Plan-Net Server SHOULD support vread on OrganizationAffiliation resource by id and version
**Requirement**: "A Server SHOULD be capable of returning a OrganizationAffiliation resource using: `GET [base]/OrganizationAffiliation/[id]/_history/vid`"
**Context**: This requirement recommends that the server should support retrieving a specific version of an OrganizationAffiliation resource using its logical ID and version ID.
**Conformance**: "SHOULD"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: OrganizationAffiliation

---

# REQ-007
**ID**: 07
**Summary**: Plan-Net Server SHALL support _include parameters for OrganizationAffiliation resource
**Requirement**: "A Server SHALL be capable of supporting the following _includes: OrganizationAffiliation:primary-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:primary-organization`; OrganizationAffiliation:participating-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:participating-organization`; OrganizationAffiliation:location - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:location`; OrganizationAffiliation:service - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:service`; OrganizationAffiliation:endpoint - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:endpoint`; OrganizationAffiliation:network - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:network`"
**Context**: This requirement mandates that the server must support including referenced Organization (primary and participating), Location, HealthcareService, Endpoint, and Network resources when searching for OrganizationAffiliation resources using the _include parameter.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: OrganizationAffiliation

---

# REQ-008
**ID**: 08
**Summary**: Plan-Net Server SHALL support search parameters on OrganizationAffiliation resource
**Requirement**: "A Server SHALL support the following search parameters on OrganizationAffiliation: primary-organization, participating-organization, location, service, network, endpoint, role, specialty, _id, _lastUpdated"
**Context**: This requirement mandates that the server must support searching for OrganizationAffiliation resources using the specified reference parameters (primary-organization, participating-organization, location, service, network, endpoint), token parameters (role, specialty), and standard parameters (_id, _lastUpdated).
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.6 OrganizationAffiliation
**Grouping**: OrganizationAffiliation
