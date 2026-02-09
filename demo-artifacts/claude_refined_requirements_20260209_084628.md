# Refined FHIR Implementation Guide Requirements

This document contains the refined, testable requirements extracted from the FHIR Implementation Guide.

Generated using batch processing to handle large requirement sets efficiently.



---
# GROUP: Ungrouped
---

---
# REQ-001
**ID**: 01
**Summary**: Location search parameter support for address
**Requirement**: "Select Locations with the specified address using Parameter `address`:`string` [with] Expression `Location.address`"
**Context**: This requirement defines a search parameter for the Location resource that allows searching by address. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple values separated by comma where at least one must be true). Allowed modifiers are exact and contains.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.20.1 SearchParameter: Plannet_sp_location_address
**Grouping**: Location
---

---
# REQ-002
**ID**: 02
**Summary**: Server SHALL support address-city search parameter on Location resource
**Requirement**: "Select Locations with the specified address.city"
**Context**: The Plan-Net Implementation Guide defines a search parameter `address-city` of type `string` that enables searching for Location resources based on the city component of their address. The expression used is `Location.address.city`. This search parameter supports multipleAnd (the parameter may repeat to specify multiple values that must all be true) and multipleOr (the parameter may have multiple values separated by comma where at least one must be true). The allowed modifiers are: exact, contains.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.21.1 SearchParameter: Plannet_sp_location_address_city
**Grouping**: Location
---

---
# REQ-003
**ID**: 03
**Summary**: Server SHALL support endpoint search parameter on Location resource
**Requirement**: "Select Locations with the specified endpoint"
**Context**: The Plan-Net Implementation Guide defines a search parameter `endpoint` of type `reference` that enables searching for Location resources based on their associated endpoint. The expression used is `Location.endpoint` with target resource type of Endpoint. This search parameter supports multipleAnd (the parameter may repeat to specify multiple values that must all be true) and multipleOr (the parameter may have multiple values separated by comma where at least one must be true). The allowed chain is: organization.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.24.1 SearchParameter: Plannet_sp_location_endpoint
**Grouping**: Location
---

---
# REQ-004
**ID**: 04
**Summary**: Server SHALL support search by address state on Location resource
**Requirement**: "Select Locations with the specified address.state [using parameter `address-state`:`string` with Expression `Location.address.state`]"
**Context**: The Plannet_sp_location_address_state search parameter enables searching for Location resources by the state component of the address. The search supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). The exact and contains modifiers are allowed.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.23.1 SearchParameter: Plannet_sp_location_address_state
**Grouping**: Location
---

---
# REQ-005
**ID**: 05
**Summary**: Server SHALL support search by partof reference on Location resource
**Requirement**: "Select Locations that are part of the specified location [using parameter `partof`:`reference` with Expression `Location.partOf` targeting Location resources]"
**Context**: The Plannet_sp_location_partof search parameter enables searching for Location resources that are part of another specified location. The search supports multipleOr (parameter may have multiple comma-separated values where at least one must be true). It is up to the server whether multipleAnd is supported. Chain searches are allowed on type, address, and organization.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.26.1 SearchParameter: Plannet_sp_location_partof
**Grouping**: Location
---

---
# REQ-006
**ID**: 06
**Summary**: Health Plan API Actor SHALL support searching Locations by address-postalcode parameter
**Requirement**: "Select Locations with the specified address" using Parameter `address-postalcode`:`string` with Expression `Location.address.postalCode`
**Context**: The SearchParameter Plannet_sp_location_address_postalcode enables searching for Location resources by postal code in the address. The parameter supports multipleAnd (parameter may repeat to specify multiple values that must all be true) and multipleOr (parameter may have multiple comma-separated values where at least one must be true). Allowed modifiers are: exact, contains.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.22.1 SearchParameter: Plannet_sp_location_address_postalcode
**Grouping**: Location
---

---
# REQ-007
**ID**: 07
**Summary**: Health Plan API Actor SHALL support organization search parameter on Location resource
**Requirement**: "Select Locations managed by the specified organization [using] Parameter `organization`:`reference` [with] Expression `Location.managingOrganization`"
**Context**: This search parameter allows querying Location resources by their managing organization using a reference-based search. The parameter supports multipleAnd (multiple values that must all be true) and multipleOr (comma-separated values where at least one must be true). Allowed chains include: name, address, partof, type.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.25.1 SearchParameter: Plannet_sp_location_organization
**Grouping**: Location
---

---
# REQ-008
**ID**: 08
**Summary**: Accessibility Extension Value Binding Conformance
**Requirement**: "To be conformant, the concept in this element SHALL be from the specified value set [AccessibilityVS] if any of the codes within the value set can apply to the concept being communicated."
**Context**: The accessibility extension is used to describe accessibility options offered by a practitioner or at a location. When populating the value[x] element of this extension with a CodeableConcept, the value must conform to extensible binding rules with the AccessibilityVS value set.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies if any of the codes within the AccessibilityVS value set can apply to the concept being communicated.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.66.1.1.1 Terminology Bindings
**Grouping**: Location
---

---
# REQ-009
**ID**: 09
**Summary**: LocationReference Extension URL Fixed Value
**Requirement**: "The definition SHALL be a URI for the Structure Definition defining the extension."
**Context**: This requirement applies to the location-reference extension. The extension URL must be fixed to the canonical URI that identifies this extension structure definition. This ensures proper identification and processing of the extension across systems.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.71.1 Extension: LocationReference - Detailed Descriptions
**Grouping**: Location
---

---
# REQ-010
**ID**: 10
**Summary**: LocationReference Extension Must Support value[x] Element
**Requirement**: "[The Extension.value[x] element] Must Support [is] true"
**Context**: The location-reference extension defines a reference to a Location resource (plannet-Location) that defines the coverage area of a health insurance provider network. The value[x] element of this extension must be supported by implementers, meaning systems claiming to support this extension must be capable of populating and processing this element when present.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Attestation"
**Section**: 11.71.1 Extension: LocationReference - Detailed Descriptions
**Grouping**: Location
---

---
# REQ-011
**ID**: 11
**Summary**: LocationReference Extension value[x] Cardinality
**Requirement**: "[Extension.value[x]] Control [cardinality is] 1.1"
**Context**: The value[x] element in the location-reference extension must be present exactly once. This element contains the reference to the Plan-Net Location resource and is required for the extension to be valid.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor, Application Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.71.1 Extension: LocationReference - Detailed Descriptions
**Grouping**: Location
---

---
# REQ-012
**ID**: 12
**Summary**: Plan-Net Server SHALL support search-type and read interactions on Location resource
**Requirement**: "A Server SHALL support search-type, read [on Location resource]."
**Context**: This requirement mandates that the server must support the ability to search for Location resources and read individual Location resources by their logical ID.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.4 Location
**Grouping**: Location
---

---
# REQ-013
**ID**: 13
**Summary**: Plan-Net Server SHOULD support vread interaction on Location resource
**Requirement**: "A Server SHOULD support vread [on Location resource]."
**Context**: This requirement recommends that the server should support retrieving specific historical versions of a Location resource using the version-aware read (vread) operation.
**Conformance**: "SHOULD"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.4 Location
**Grouping**: Location
---

---
# REQ-014
**ID**: 14
**Summary**: Plan-Net Server SHALL support reading Location resource by id
**Requirement**: "A Server SHALL be capable of returning a Location resource using: `GET [base]/Location/[id]`"
**Context**: This requirement mandates that the server must support retrieving a specific Location resource using its logical ID via a GET operation.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.4 Location
**Grouping**: Location
---

---
# REQ-015
**ID**: 15
**Summary**: Plan-Net Server SHOULD support vread on Location resource by id and version
**Requirement**: "A Server SHOULD be capable of returning a Location resource using: `GET [base]/Location/[id]/_history/vid`"
**Context**: This requirement recommends that the server should support retrieving a specific version of a Location resource using its logical ID and version ID.
**Conformance**: "SHOULD"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.4 Location
**Grouping**: Location
---

---
# REQ-016
**ID**: 16
**Summary**: Plan-Net Server SHALL support _include parameters for Location resource
**Requirement**: "A Server SHALL be capable of supporting the following _includes: Location:endpoint - `GET [base]/Location?[parameter=value]&_include=Location:endpoint`; Location:organization - `GET [base]/Location?[parameter=value]&_include=Location:organization`; Location:partof - `GET [base]/Location?[parameter=value]&_include=Location:partof`"
**Context**: This requirement mandates that the server must support including referenced Endpoint, Organization, and parent Location resources when searching for Location resources using the _include parameter.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.4 Location
**Grouping**: Location
---

---
# REQ-017
**ID**: 17
**Summary**: Plan-Net Server SHALL support _revinclude parameters for Location resource
**Requirement**: "A Server SHALL be capable of supporting the following _revincludes: HealthcareService:location - `GET [base]/Location?[parameter=value]&_revinclude=HealthcareService:location`; InsurancePlan:coverage-area - `GET [base]/Location?[parameter=value]&_revinclude=InsurancePlan:coverage-area`; OrganizationAffiliation:location - `GET [base]/Location?[parameter=value]&_revinclude=OrganizationAffiliation:location`; PractitionerRole:location - `GET [base]/Location?[parameter=value]&_revinclude=PractitionerRole:location`"
**Context**: This requirement mandates that the server must support reverse includes to retrieve HealthcareService, InsurancePlan, OrganizationAffiliation, and PractitionerRole resources that reference the Location resources in the search results.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.4 Location
**Grouping**: Location
---

---
# REQ-018
**ID**: 18
**Summary**: Plan-Net Server SHALL support search parameters on Location resource
**Requirement**: "A Server SHALL support the following search parameters on Location: partof, organization, endpoint, address-city, address-state, address-postalcode, address, type, _id, _lastUpdated"
**Context**: This requirement mandates that the server must support searching for Location resources using the specified reference parameters (partof, organization, endpoint), string parameters (address-city, address-state, address-postalcode, address), token parameter (type), and standard parameters (_id, _lastUpdated).
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: NA
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.1.1.2.4 Location
**Grouping**: Location
---

---
# REQ-019
**ID**: 19
**Summary**: Plan-Net Location status SHALL be fixed to 'active'
**Requirement**: "The status property SHALL have a fixed value of 'active'"
**Context**: The Location.status element in the Plan-Net Location profile is constrained to only allow the value 'active', indicating that all Location resources conforming to this profile must represent currently active locations. This is a mandatory constraint on the base FHIR Location resource.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.status element (field 22, 42)
**Grouping**: Location
---

---
# REQ-020
**ID**: 20
**Summary**: Plan-Net Location name is required and must be supported
**Requirement**: "Location.name [has cardinality] 1..1 [and] Must Support [is] true"
**Context**: The Location.name element is mandatory in the Plan-Net Location profile and must be supported by implementations. This field contains the name by which a facility or location is known to humans.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.name element (field 24, 46)
**Grouping**: Location
---

---
# REQ-021
**ID**: 21
**Summary**: Plan-Net Location mode cardinality SHALL be 0..0
**Requirement**: "Location.mode [Control] 0..0"
**Context**: The Location.mode element is prohibited in the Plan-Net Location profile, with a cardinality of 0..0. This means that Plan-Net Location resources cannot include the mode element which would normally indicate whether a resource represents a specific location or a class of locations.
**Conformance**: "SHALL NOT"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.mode element (field 30, 52)
**Grouping**: Location
---

---
# REQ-022
**ID**: 22
**Summary**: Plan-Net Location SHALL support identifier with type and value
**Requirement**: "Location.identifier [Must Support is] true, Location.identifier.type [Must Support is] true, Location.identifier.value [Must Support is] true"
**Context**: The Location.identifier element and its sub-elements type and value must be supported in Plan-Net Location implementations. This allows for unique business identifiers for facilities or locations to be provided and processed.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.identifier elements (fields 14, 18, 20, 24, 32, 36)
**Grouping**: Location
---

---
# REQ-023
**ID**: 23
**Summary**: Plan-Net Location SHALL support alias
**Requirement**: "Location.alias [Must Support is] true"
**Context**: The Location.alias element must be supported to allow for alternate names that the location is known as, or was known as in the past. This assists in searching so that older names can still result in identifying the location.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.alias element (field 26, 48)
**Grouping**: Location
---

---
# REQ-024
**ID**: 24
**Summary**: Plan-Net Location SHALL support description
**Requirement**: "Location.description [Must Support is] true"
**Context**: The Location.description element must be supported to provide additional details about the location that could be displayed as further information to identify the location beyond its name.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.description element (field 28, 50)
**Grouping**: Location
---

---
# REQ-025
**ID**: 25
**Summary**: Plan-Net Location SHALL support type
**Requirement**: "Location.type [Must Support is] true"
**Context**: The Location.type element must be supported to indicate the category of service or resource available in a location. It describes the type of function performed at the location.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.type element (field 32, 54)
**Grouping**: Location
---

---
# REQ-026
**ID**: 26
**Summary**: Plan-Net Location SHALL support telecom with required sub-elements
**Requirement**: "Location.telecom [Must Support is] true, Location.telecom.system [Must Support is] true, Location.telecom.value [Must Support is] true"
**Context**: The Location.telecom element and its sub-elements system and value must be supported to provide contact details of communication devices available at the location, including phone numbers, fax numbers, mobile numbers, email addresses and web sites.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.telecom elements (fields 34, 40, 42, 56, 66, 68)
**Grouping**: Location
---

---
# REQ-027
**ID**: 27
**Summary**: Plan-Net Location SHALL support address with line, city, state, and postalCode
**Requirement**: "Location.address [Must Support is] true, Location.address.line [Must Support is] true, Location.address.city [Must Support is] true, Location.address.state [Must Support is] true, Location.address.postalCode [Must Support is] true"
**Context**: The Location.address element and its sub-elements line, city, state, and postalCode must be supported to provide the physical location address information necessary for identifying and visiting the location.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.address elements (field 46, 50, 52, 54, 56, 76, 88, 90, 94, 96)
**Grouping**: Location
---

---
# REQ-028
**ID**: 28
**Summary**: Plan-Net Location SHALL support position
**Requirement**: "Location.position [Must Support is] true"
**Context**: The Location.position element must be supported to provide the absolute geographic location of the Location expressed using the WGS84 datum. This is required for mobile applications and automated route-finding.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.position element (field 58, 104)
**Grouping**: Location
---

---
# REQ-029
**ID**: 29
**Summary**: Plan-Net Location SHALL support managingOrganization
**Requirement**: "Location.managingOrganization [Must Support is] true [and Type is] Reference(Plan-Net Organization)"
**Context**: The Location.managingOrganization element must be supported and must reference a Plan-Net Organization resource representing the organization responsible for the provisioning and upkeep of the location.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.managingOrganization element (field 66, 118)
**Grouping**: Location
---

---
# REQ-030
**ID**: 30
**Summary**: Plan-Net Location SHALL support partOf
**Requirement**: "Location.partOf [Must Support is] true [and Type is] Reference(Plan-Net Location)"
**Context**: The Location.partOf element must be supported and must reference another Plan-Net Location resource to indicate that this location is physically a part of another location. This is important for location hierarchy and identification purposes.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.partOf element (field 68, 120)
**Grouping**: Location
---

---
# REQ-031
**ID**: 31
**Summary**: Plan-Net Location SHALL support hoursOfOperation with all sub-elements
**Requirement**: "Location.hoursOfOperation [Must Support is] true, Location.hoursOfOperation.daysOfWeek [Must Support is] true, Location.hoursOfOperation.allDay [Must Support is] true, Location.hoursOfOperation.openingTime [Must Support is] true, Location.hoursOfOperation.closingTime [Must Support is] true"
**Context**: The Location.hoursOfOperation element and all its sub-elements must be supported to describe what days/times during a week the location is usually open. This information is commonly found published in directories and on websites informing customers when the facility is available.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.hoursOfOperation elements (fields 70, 74, 76, 78, 80, 122, 130, 132, 134, 136)
**Grouping**: Location
---

---
# REQ-032
**ID**: 32
**Summary**: Plan-Net Location SHALL support availabilityExceptions
**Requirement**: "Location.availabilityExceptions [Must Support is] true"
**Context**: The Location.availabilityExceptions element must be supported to provide a description of when the location's opening hours are different to normal, such as public holiday availability.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.availabilityExceptions element (field 82, 138)
**Grouping**: Location
---

---
# REQ-033
**ID**: 33
**Summary**: Plan-Net Location SHALL support endpoint
**Requirement**: "Location.endpoint [Must Support is] true [and Type is] Reference(Plan-Net Endpoint)"
**Context**: The Location.endpoint element must be supported and must reference Plan-Net Endpoint resources that provide technical endpoints for accessing services operated for the location. This allows organizations to define different systems at different locations.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.endpoint element (field 84, 140)
**Grouping**: Location
---

---
# REQ-034
**ID**: 34
**Summary**: Plan-Net Location SHALL support newpatients extension
**Requirement**: "Location.extension:newpatients [Must Support is] true"
**Context**: The newpatients extension must be supported to indicate whether new patients are being accepted in general, or from a specific network. This provides needed flexibility for specifying whether a provider accepts new patients by location and network.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.extension:newpatients (fields 6, 16)
**Grouping**: Location
---

---
# REQ-035
**ID**: 35
**Summary**: Plan-Net Location SHALL support accessibility extension
**Requirement**: "Location.extension:accessibility [Must Support is] true"
**Context**: The accessibility extension must be supported to describe accessibility options offered at a location, enabling users to identify locations with appropriate accessibility features.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.extension:accessibility (fields 8, 18)
**Grouping**: Location
---

---
# REQ-036
**ID**: 36
**Summary**: Plan-Net Location SHALL support region extension
**Requirement**: "Location.extension:region [Must Support is] true"
**Context**: The region extension must be supported to provide a boundary shape that represents the outside edge of the location in GeoJSON format. The content format is GeoJSON in both JSON and XML formats with mimetype 'application/geo+json'.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.extension:region (fields 10, 20)
**Grouping**: Location
---

---
# REQ-037
**ID**: 37
**Summary**: Plan-Net Location SHALL support contactpoint-availabletime extension on telecom
**Requirement**: "Location.telecom.extension:contactpoint-availabletime [Must Support is] true"
**Context**: The contactpoint-availabletime extension on Location.telecom must be supported to represent the days and times a contact point is available, providing detailed availability information for communication channels.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.telecom.extension:contactpoint-availabletime (fields 36, 62)
**Grouping**: Location
---

---
# REQ-038
**ID**: 38
**Summary**: Plan-Net Location SHALL support via-intermediary extension on telecom
**Requirement**: "Location.telecom.extension:via-intermediary [Must Support is] true"
**Context**: The via-intermediary extension on Location.telecom must be supported to provide a reference to an alternative point of contact (PractitionerRole, Organization, OrganizationAffiliation, or Location) for this location.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "False"
**Conditionality Details**: **Verifiable**: Yes
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: PlannetLocation - Detailed Descriptions, Location.telecom.extension:via-intermediary (fields 38, 64)
**Grouping**: Location
---

---
# REQ-039
**ID**: 39
**Summary**: Location position longitude is mandatory when position is present
**Requirement**: "Longitude. The value domain and the interpretation are the same as for the text of the longitude element in KML (see notes below). [Cardinality] 1.1"
**Context**: When a Location resource includes position information, the longitude element must be populated to provide the geographic coordinate.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when the Location.position element is present in the resource.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: Plan-Net Location
**Grouping**: Location
---

---
# REQ-040
**ID**: 40
**Summary**: Location position latitude is mandatory when position is present
**Requirement**: "Latitude. The value domain and the interpretation are the same as for the text of the latitude element in KML (see notes below). [Cardinality] 1.1"
**Context**: When a Location resource includes position information, the latitude element must be populated to provide the geographic coordinate.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when the Location.position element is present in the resource.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: Plan-Net Location
**Grouping**: Location
---

---
# REQ-041
**ID**: 41
**Summary**: Location accessibility extension binding constraint
**Requirement**: "accessibility [Extension] URL = http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility [Type] CodeableConcept [Description] Accessibility [Binding] Accessibility VS (extensible): To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: When the accessibility extension is used on a Location resource, the codes used must come from the specified Accessibility VS value set if applicable codes exist in that value set.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when the accessibility extension is present and when codes in the Accessibility VS value set can apply to the concept being communicated.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: Plan-Net Location
**Grouping**: Location
---

---
# REQ-042
**ID**: 42
**Summary**: Location address state binding constraint
**Requirement**: "[Location.address.]state [Description] Sub-unit of country (abbreviations ok) [Binding] USPS Two Letter Alphabetic Codes (extensible): To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: When the state element is used in a Location's address, the codes used must come from the USPS Two Letter Alphabetic Codes value set if applicable codes exist in that value set.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when the Location.address.state element is present and when codes in the USPS Two Letter Alphabetic Codes value set can apply to the concept being communicated.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: Plan-Net Location
**Grouping**: Location
---

---
# REQ-043
**ID**: 43
**Summary**: Location type binding constraint
**Requirement**: "[Location.]type [Description] Category of service or resource available in a location. [Binding] ServiceDeliveryLocationRoleType (extensible): To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: When the type element is used on a Location resource to indicate the type of function performed at the location, the codes used must come from the ServiceDeliveryLocationRoleType value set if applicable codes exist in that value set.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when the Location.type element is present and when codes in the ServiceDeliveryLocationRoleType value set can apply to the concept being communicated.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: Plan-Net Location
**Grouping**: Location
---

---
# REQ-044
**ID**: 44
**Summary**: Location identifier type binding constraint
**Requirement**: "[Location.identifier.]type [Description] Description of identifier [Binding] Identifier Type Codes (extensible): To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead."
**Context**: When the type element is used in a Location's identifier to specify the type of identifier, the codes used must come from the Identifier Type Codes value set if applicable codes exist in that value set.
**Conformance**: "SHALL"
**Actor**: Health Plan API Actor
**Sub-Requirement(s)**: NA
**Conditionality**: "True"
**Conditionality Details**: This requirement applies when the Location.identifier.type element is present and when codes in the Identifier Type Codes value set can apply to the concept being communicated.
**Verifiability**: "Yes"
**Verifiability Details**: "Automation"
**Section**: 11.60.1 Resource Profile: Plan-Net Location
**Grouping**: Location
---
