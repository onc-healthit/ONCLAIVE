xml version="1.0" encoding="UTF-8"?

HL7.FHIR.US.DAVINCI-PDEX-PLAN-NET\Plan-Net CapabilityStatement - FHIR v4.0.1

[![Visit the HL7 website](assets/images/hl7-logo-header.png)](http://hl7.org)

[![Visit the FHIR website](assets/images/fhir-logo-www.png)](http://hl7.org/fhir)

[![Search FHIR](assets/images/search.png)](searchform.html)

[![Visit the Da Vinci website](assets/images/da-vinci_logo.jpg)](http://hl7.org/about/davinci)

DaVinci PDEX Plan Net

1.1.0 - STU 1.1
US

[FHIR](http://hl7.org/fhir/R4/index.html)

* [Home](index.html)
* [Implementation](#)
  + [Implementation](implementation.html)
  + [Representing Provider Directories in Plan Net](implementation.html#Representing)
* [FHIR Artifacts](#)
  + [Profiles](artifacts.html#3)
  + [Extensions](artifacts.html#4)
  + [Search Parameters](artifacts.html#2)
  + [Terminology](artifacts.html#5)
  + [Capability Statement](artifacts.html#1)
* [Examples](artifacts.html#7)
* [Downloads](downloads.html)
* [Change History](ChangeHistory.html)
* [History](http://www.hl7.org/fhir/us/davinci-pdex-plan-net/history.cfml)

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net CapabilityStatement**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## CapabilityStatement: Plan-Net CapabilityStatement

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/CapabilityStatement/plan-net | | | | *Version*: 1.1.0 |
| Active as of 2022-03-18 | | | | *Computable Name*: DavinciPdexPlanNetCapabilityStatement |

This Section describes the expected capabilities of the Plan-Net Server actor which is responsible for providing responses to the queries submitted by the Plan-Net Requestors. The complete list of FHIR profiles, RESTful operations, and search parameters supported by Plan-Net Servers are defined. Systems implementing this capability statement should meet the CMS FInal Rule requirement for provider directory access. Plan-Net Clients can use the required capabilities to access necessary data based on their local use cases and other contextual requirements.

[Raw OpenAPI-Swagger Definition file](plan-net.openapi.json) | [Download](plan-net.openapi.json)

## Plan-Net CapabilityStatement

* Implementation Guide Version: 1.0.0
* FHIR Version: 4.0.1
* Supported formats: xml, json
* Published: 2022-03-18
* Published by: HL7 Financial Management Working Group (FM WG)

This Section describes the expected capabilities of the Plan-Net Server actor which is responsible for providing responses to the queries submitted by the Plan-Net Requestors. The complete list of FHIR profiles, RESTful operations, and search parameters supported by Plan-Net Servers are defined. Systems implementing this capability statement should meet the CMS FInal Rule requirement for provider directory access. Plan-Net Clients can use the required capabilities to access necessary data based on their local use cases and other contextual requirements.

### FHIR RESTful Capabilities

The Plan-Net Server **SHALL**:

1. Support all profiles defined in this Implementation Guide..
2. Implement the RESTful behavior according to the FHIR specification.
3. Return the following response classes:
   * (Status 400): invalid parameter
   * (Status 401/4xx): unauthorized request
   * (Status 403): insufficient scope
   * (Status 404): unknown resource
   * (Status 410): deleted resource.
4. Support json source formats for all Plan-Net interactions.
5. Identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance.
6. Support the searchParameters on each profile individually and in combination.
   1.Support forward and reverse chaining on all search parameters that specify the 'chain' property

The Plan-Net Server **SHOULD**:

1. Support xml source formats for all Plan-Net interactions.

**Security:**

1. See the [General Security Considerations](implementation.html#general-security-considerations) section for requirements and recommendations.
2. A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code.

### RESTful Capabilities by Resource/Profile:

**Summary of Search Criteria**

| Resource Type | Supported Profiles | Supported Searches | Supported `_includes` | Supported `_revincludes` | Supported Operations |
| --- | --- | --- | --- | --- | --- |
| [Endpoint](#endpoint) | [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html) | organization, \_id, \_lastUpdated | Endpoint:organization |  |  |
| [HealthcareService](#healthcareservice) | [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html) | location, coverage-area, organization, endpoint, name, service-category, service-type, specialty, \_id, \_lastUpdated | HealthcareService:location, HealthcareService:coverage-area, HealthcareService:organization, HealthcareService:endpoint | PractitionerRole:service, OrganizationAffiliation:service |  |
| [InsurancePlan](#insuranceplan) | [Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html) | administered-by, owned-by, coverage-area, name, plan-type, identifier, \_id, \_lastUpdated, type | InsurancePlan:administered-by, InsurancePlan:owned-by, InsurancePlan:coverage-area |  |  |
| [Location](#location) | [Plan-Net Location](StructureDefinition-plannet-Location.html) | partof, organization, endpoint, address-city, address-state, address-postalcode, address, type, \_id, \_lastUpdated | Location:endpoint, Location:organization, Location:partof | HealthcareService:location, InsurancePlan:coverage-area, OrganizationAffiliation:location, PractitionerRole:location |  |
| [Organization](#organization) | [Plan-Net Network](StructureDefinition-plannet-Network.html), [Plan-Net Organization](StructureDefinition-plannet-Organization.html) | partof, endpoint, address, name, \_id, \_lastUpdated, type, coverage-area | Organization:partof, Organization:endpoint, Organization:coverage-area | Endpoint:organization, HealthcareService:organization, InsurancePlan:administered-by, InsurancePlan:owned-by, OrganizationAffiliation:primary-organization, PractitionerRole:organization, PractitionerRole:network, OrganizationAffiliation:participating-organization |  |
| [OrganizationAffiliation](#organizationaffiliation) | [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html) | primary-organization, participating-organization, location, service, network, endpoint, role, specialty, \_id, \_lastUpdated | OrganizationAffiliation:primary-organization, OrganizationAffiliation:participating-organization, OrganizationAffiliation:location, OrganizationAffiliation:service, OrganizationAffiliation:endpoint, OrganizationAffiliation:network |  |  |
| [Practitioner](#practitioner) | [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html) | name, \_id, \_lastUpdated, family, given |  | PractitionerRole:practitioner |  |
| [PractitionerRole](#practitionerrole) | [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html) | practitioner, organization, location, service, network, endpoint, role, specialty, \_id, \_lastUpdated | PractitionerRole:practitioner, PractitionerRole:organization, PractitionerRole:location, PractitionerRole:service, PractitionerRole:network, PractitionerRole:endpoint |  |  |

#### Endpoint

Conformance Expectation: **SHALL**

Supported Profiles:
[Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)

Reference Policy: `resolves`

Profile Interaction Summary:

* **SHALL** support
  `search-type`,
  `read`.
* **SHOULD** support
  `vread`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a Endpoint resource using:

  `GET [base]/Endpoint/[id]`

* A Server **SHOULD** be capable of returning a Endpoint resource using:

  `GET [base]/Endpoint/[id]/_history/vid`

 * A Server **SHALL** be capable of supporting the following \_includes:

  Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`

Search Parameter Summary:

| Conformance | Parameter | Type | Example |
| --- | --- | --- | --- |
| **SHALL** | [organization](SearchParameter-endpoint-organization.html) | reference | `GET [base]/Endpoint?organization=[organization]` |
| **SHALL** | [\_id](http://hl7.org/fhir/R4/search.html) | token | `GET [base]/Endpoint?_id=[id]` |
| **SHALL** | [\_lastUpdated](http://hl7.org/fhir/R4/search.html) | date | `GET [base]/Endpoint?_lastUpdated=[_lastUpdated]` |

---

#### HealthcareService

Conformance Expectation: **SHALL**

Supported Profiles:
[Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)

Reference Policy: `resolves`

Profile Interaction Summary:

* **SHALL** support
  `search-type`,
  `read`.
* **SHOULD** support
  `vread`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a HealthcareService resource using:

  `GET [base]/HealthcareService/[id]`

* A Server **SHOULD** be capable of returning a HealthcareService resource using:

  `GET [base]/HealthcareService/[id]/_history/vid`

 * A Server **SHALL** be capable of supporting the following \_includes:

  HealthcareService:location - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:location`  
  HealthcareService:coverage-area - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:coverage-area`  
  HealthcareService:organization - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:organization`  
  HealthcareService:endpoint - `GET [base]/HealthcareService?[parameter=value]&_include=HealthcareService:endpoint`

 * A Server **SHALL** be capable of supporting the following \_revincludes:

  PractitionerRole:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=PractitionerRole:service`  
  OrganizationAffiliation:service - `GET [base]/HealthcareService?[parameter=value]&_revinclude=OrganizationAffiliation:service`

Search Parameter Summary:

| Conformance | Parameter | Type | Example |
| --- | --- | --- | --- |
| **SHALL** | [location](SearchParameter-healthcareservice-location.html) | reference | `GET [base]/HealthcareService?location=[location]` |
| **SHALL** | [coverage-area](SearchParameter-healthcareservice-coverage-area.html) | reference | `GET [base]/HealthcareService?coverage-area=[coverage-area]` |
| **SHALL** | [organization](SearchParameter-healthcareservice-organization.html) | reference | `GET [base]/HealthcareService?organization=[organization]` |
| **SHALL** | [endpoint](SearchParameter-healthcareservice-endpoint.html) | reference | `GET [base]/HealthcareService?endpoint=[endpoint]` |
| **SHALL** | [name](SearchParameter-healthcareservice-name.html) | string | `GET [base]/HealthcareService?name=[name]` |
| **SHALL** | [service-category](SearchParameter-healthcareservice-service-category.html) | token | `GET [base]/HealthcareService?service-category=[system]|[code]` |
| **SHALL** | [service-type](SearchParameter-healthcareservice-service-type.html) | token | `GET [base]/HealthcareService?service-type=[system]|[code]` |
| **SHALL** | [specialty](SearchParameter-healthcareservice-specialty.html) | token | `GET [base]/HealthcareService?specialty=[system]|[code]` |
| **SHALL** | [\_id](http://hl7.org/fhir/R4/search.html) | token | `GET [base]/HealthcareService?_id=[id]` |
| **SHALL** | [\_lastUpdated](http://hl7.org/fhir/R4/search.html) | date | `GET [base]/HealthcareService?_lastUpdated=[_lastUpdated]` |

---

#### InsurancePlan

Conformance Expectation: **SHALL**

Supported Profiles:
[Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html)

Reference Policy: `resolves`

Profile Interaction Summary:

* **SHALL** support
  `search-type`,
  `read`.
* **SHOULD** support
  `vread`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a InsurancePlan resource using:

  `GET [base]/InsurancePlan/[id]`

* A Server **SHOULD** be capable of returning a InsurancePlan resource using:

  `GET [base]/InsurancePlan/[id]/_history/vid`

 * A Server **SHALL** be capable of supporting the following \_includes:

  InsurancePlan:administered-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:administered-by`  
  InsurancePlan:owned-by - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:owned-by`  
  InsurancePlan:coverage-area - `GET [base]/InsurancePlan?[parameter=value]&_include=InsurancePlan:coverage-area`

Search Parameter Summary:

| Conformance | Parameter | Type | Example |
| --- | --- | --- | --- |
| **SHALL** | [administered-by](SearchParameter-insuranceplan-administered-by.html) | reference | `GET [base]/InsurancePlan?administered-by=[administered-by]` |
| **SHALL** | [owned-by](SearchParameter-insuranceplan-owned-by.html) | reference | `GET [base]/InsurancePlan?owned-by=[owned-by]` |
| **SHALL** | [coverage-area](SearchParameter-insuranceplan-coverage-area.html) | reference | `GET [base]/InsurancePlan?coverage-area=[coverage-area]` |
| **SHALL** | [name](SearchParameter-insuranceplan-name.html) | string | `GET [base]/InsurancePlan?name=[name]` |
| **SHALL** | [plan-type](SearchParameter-insuranceplan-plan-type.html) | token | `GET [base]/InsurancePlan?plan-type=[system]|[code]` |
| **SHALL** | [identifier](SearchParameter-insuranceplan-identifier.html) | token | `GET [base]/InsurancePlan?identifier=[system]|[code]` |
| **SHALL** | [\_id](http://hl7.org/fhir/R4/search.html) | token | `GET [base]/InsurancePlan?_id=[id]` |
| **SHALL** | [\_lastUpdated](http://hl7.org/fhir/R4/search.html) | date | `GET [base]/InsurancePlan?_lastUpdated=[_lastUpdated]` |
| **SHALL** | [type](SearchParameter-insuranceplan-type.html) | token | `GET [base]/InsurancePlan?type=[system]|[code]` |

---

#### Location

Conformance Expectation: **SHALL**

Supported Profiles:
[Plan-Net Location](StructureDefinition-plannet-Location.html)

Reference Policy: `resolves`

Profile Interaction Summary:

* **SHALL** support
  `search-type`,
  `read`.
* **SHOULD** support
  `vread`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a Location resource using:

  `GET [base]/Location/[id]`

* A Server **SHOULD** be capable of returning a Location resource using:

  `GET [base]/Location/[id]/_history/vid`

 * A Server **SHALL** be capable of supporting the following \_includes:

  Location:endpoint - `GET [base]/Location?[parameter=value]&_include=Location:endpoint`  
  Location:organization - `GET [base]/Location?[parameter=value]&_include=Location:organization`  
  Location:partof - `GET [base]/Location?[parameter=value]&_include=Location:partof`

 * A Server **SHALL** be capable of supporting the following \_revincludes:

  HealthcareService:location - `GET [base]/Location?[parameter=value]&_revinclude=HealthcareService:location`  
  InsurancePlan:coverage-area - `GET [base]/Location?[parameter=value]&_revinclude=InsurancePlan:coverage-area`  
  OrganizationAffiliation:location - `GET [base]/Location?[parameter=value]&_revinclude=OrganizationAffiliation:location`  
  PractitionerRole:location - `GET [base]/Location?[parameter=value]&_revinclude=PractitionerRole:location`

Search Parameter Summary:

| Conformance | Parameter | Type | Example |
| --- | --- | --- | --- |
| **SHALL** | [partof](SearchParameter-location-partof.html) | reference | `GET [base]/Location?partof=[partof]` |
| **SHALL** | [organization](SearchParameter-location-organization.html) | reference | `GET [base]/Location?organization=[organization]` |
| **SHALL** | [endpoint](SearchParameter-location-endpoint.html) | reference | `GET [base]/Location?endpoint=[endpoint]` |
| **SHALL** | [address-city](SearchParameter-location-address-city.html) | string | `GET [base]/Location?address-city=[address-city]` |
| **SHALL** | [address-state](SearchParameter-location-address-state.html) | string | `GET [base]/Location?address-state=[address-state]` |
| **SHALL** | [address-postalcode](SearchParameter-location-address-postalcode.html) | string | `GET [base]/Location?address-postalcode=[address-postalcode]` |
| **SHALL** | [address](SearchParameter-location-address.html) | string | `GET [base]/Location?address=[address]` |
| **SHALL** | [type](SearchParameter-location-type.html) | token | `GET [base]/Location?type=[system]|[code]` |
| **SHALL** | [\_id](http://hl7.org/fhir/R4/search.html) | token | `GET [base]/Location?_id=[id]` |
| **SHALL** | [\_lastUpdated](http://hl7.org/fhir/R4/search.html) | date | `GET [base]/Location?_lastUpdated=[_lastUpdated]` |

---

#### Organization

Conformance Expectation: **SHALL**

Supported Profiles:
[Plan-Net Network](StructureDefinition-plannet-Network.html),
[Plan-Net Organization](StructureDefinition-plannet-Organization.html)

Reference Policy: `resolves`

Profile Interaction Summary:

* **SHALL** support
  `search-type`,
  `read`.
* **SHOULD** support
  `vread`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a Organization resource using:

  `GET [base]/Organization/[id]`

* A Server **SHOULD** be capable of returning a Organization resource using:

  `GET [base]/Organization/[id]/_history/vid`

 * A Server **SHALL** be capable of supporting the following \_includes:

  Organization:partof - `GET [base]/Organization?[parameter=value]&_include=Organization:partof`  
  Organization:endpoint - `GET [base]/Organization?[parameter=value]&_include=Organization:endpoint`  
  Organization:coverage-area - `GET [base]/Organization?[parameter=value]&_include=Organization:coverage-area`

 * A Server **SHALL** be capable of supporting the following \_revincludes:

  Endpoint:organization - `GET [base]/Organization?[parameter=value]&_revinclude=Endpoint:organization`  
  HealthcareService:organization - `GET [base]/Organization?[parameter=value]&_revinclude=HealthcareService:organization`  
  InsurancePlan:administered-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:administered-by`  
  InsurancePlan:owned-by - `GET [base]/Organization?[parameter=value]&_revinclude=InsurancePlan:owned-by`  
  OrganizationAffiliation:primary-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:primary-organization`  
  PractitionerRole:organization - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:organization`  
  PractitionerRole:network - `GET [base]/Organization?[parameter=value]&_revinclude=PractitionerRole:network`  
  OrganizationAffiliation:participating-organization - `GET [base]/Organization?[parameter=value]&_revinclude=OrganizationAffiliation:participating-organization`

Search Parameter Summary:

| Conformance | Parameter | Type | Example |
| --- | --- | --- | --- |
| **SHALL** | [partof](SearchParameter-organization-partof.html) | reference | `GET [base]/Organization?partof=[partof]` |
| **SHALL** | [endpoint](SearchParameter-organization-endpoint.html) | reference | `GET [base]/Organization?endpoint=[endpoint]` |
| **SHALL** | [address](SearchParameter-organization-address.html) | string | `GET [base]/Organization?address=[address]` |
| **SHALL** | [name](SearchParameter-organization-name.html) | string | `GET [base]/Organization?name=[name]` |
| **SHALL** | [\_id](http://hl7.org/fhir/R4/search.html) | token | `GET [base]/Organization?_id=[id]` |
| **SHALL** | [\_lastUpdated](http://hl7.org/fhir/R4/search.html) | date | `GET [base]/Organization?_lastUpdated=[_lastUpdated]` |
| **SHALL** | [type](SearchParameter-organization-type.html) | token | `GET [base]/Organization?type=[system]|[code]` |
| **SHALL** | [coverage-area](SearchParameter-organization-coverage-area.html) | reference | `GET [base]/Organization?coverage-area=[coverage-area]` |

---

#### OrganizationAffiliation

Conformance Expectation: **SHALL**

Supported Profiles:
[Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)

Reference Policy: `resolves`

Profile Interaction Summary:

* **SHALL** support
  `search-type`,
  `read`.
* **SHOULD** support
  `vread`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a OrganizationAffiliation resource using:

  `GET [base]/OrganizationAffiliation/[id]`

* A Server **SHOULD** be capable of returning a OrganizationAffiliation resource using:

  `GET [base]/OrganizationAffiliation/[id]/_history/vid`

 * A Server **SHALL** be capable of supporting the following \_includes:

  OrganizationAffiliation:primary-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:primary-organization`  
  OrganizationAffiliation:participating-organization - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:participating-organization`  
  OrganizationAffiliation:location - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:location`  
  OrganizationAffiliation:service - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:service`  
  OrganizationAffiliation:endpoint - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:endpoint`  
  OrganizationAffiliation:network - `GET [base]/OrganizationAffiliation?[parameter=value]&_include=OrganizationAffiliation:network`

Search Parameter Summary:

| Conformance | Parameter | Type | Example |
| --- | --- | --- | --- |
| **SHALL** | [primary-organization](SearchParameter-organizationaffiliation-primary-organization.html) | reference | `GET [base]/OrganizationAffiliation?primary-organization=[primary-organization]` |
| **SHALL** | [participating-organization](SearchParameter-organizationaffiliation-participating-organization.html) | reference | `GET [base]/OrganizationAffiliation?participating-organization=[participating-organization]` |
| **SHALL** | [location](SearchParameter-organizationaffiliation-location.html) | reference | `GET [base]/OrganizationAffiliation?location=[location]` |
| **SHALL** | [service](SearchParameter-organizationaffiliation-service.html) | reference | `GET [base]/OrganizationAffiliation?service=[service]` |
| **SHALL** | [network](SearchParameter-organizationaffiliation-network.html) | reference | `GET [base]/OrganizationAffiliation?network=[network]` |
| **SHALL** | [endpoint](SearchParameter-organizationaffiliation-endpoint.html) | reference | `GET [base]/OrganizationAffiliation?endpoint=[endpoint]` |
| **SHALL** | [role](SearchParameter-organizationaffiliation-role.html) | token | `GET [base]/OrganizationAffiliation?role=[system]|[code]` |
| **SHALL** | [specialty](SearchParameter-organizationaffiliation-specialty.html) | token | `GET [base]/OrganizationAffiliation?specialty=[system]|[code]` |
| **SHALL** | [\_id](http://hl7.org/fhir/R4/search.html) | token | `GET [base]/OrganizationAffiliation?_id=[id]` |
| **SHALL** | [\_lastUpdated](http://hl7.org/fhir/R4/search.html) | date | `GET [base]/OrganizationAffiliation?_lastUpdated=[_lastUpdated]` |

---

#### Practitioner

Conformance Expectation: **SHALL**

Supported Profiles:
[Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html)

Reference Policy: `resolves`

Profile Interaction Summary:

* **SHALL** support
  `search-type`,
  `read`.
* **SHOULD** support
  `vread`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a Practitioner resource using:

  `GET [base]/Practitioner/[id]`

* A Server **SHOULD** be capable of returning a Practitioner resource using:

  `GET [base]/Practitioner/[id]/_history/vid`

  * A Server **SHALL** be capable of supporting the following \_revincludes:

  PractitionerRole:practitioner - `GET [base]/Practitioner?[parameter=value]&_revinclude=PractitionerRole:practitioner`

Search Parameter Summary:

| Conformance | Parameter | Type | Example |
| --- | --- | --- | --- |
| **SHALL** | [name](SearchParameter-practitioner-name.html) | string | `GET [base]/Practitioner?name=[name]` |
| **SHALL** | [\_id](http://hl7.org/fhir/R4/search.html) | token | `GET [base]/Practitioner?_id=[id]` |
| **SHALL** | [\_lastUpdated](http://hl7.org/fhir/R4/search.html) | date | `GET [base]/Practitioner?_lastUpdated=[_lastUpdated]` |
| **SHALL** | [family](SearchParameter-practitioner-family-name.html) | string | `GET [base]/Practitioner?family=[family]` |
| **SHALL** | [given](SearchParameter-practitioner-given-name.html) | string | `GET [base]/Practitioner?given=[given]` |

---

#### PractitionerRole

Conformance Expectation: **SHALL**

Supported Profiles:
[Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html)

Reference Policy: `resolves`

Profile Interaction Summary:

* **SHALL** support
  `search-type`,
  `read`.
* **SHOULD** support
  `vread`.

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a PractitionerRole resource using:

  `GET [base]/PractitionerRole/[id]`

* A Server **SHOULD** be capable of returning a PractitionerRole resource using:

  `GET [base]/PractitionerRole/[id]/_history/vid`

 * A Server **SHALL** be capable of supporting the following \_includes:

  PractitionerRole:practitioner - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:practitioner`  
  PractitionerRole:organization - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:organization`  
  PractitionerRole:location - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:location`  
  PractitionerRole:service - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:service`  
  PractitionerRole:network - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:network`  
  PractitionerRole:endpoint - `GET [base]/PractitionerRole?[parameter=value]&_include=PractitionerRole:endpoint`

Search Parameter Summary:

| Conformance | Parameter | Type | Example |
| --- | --- | --- | --- |
| **SHALL** | [practitioner](SearchParameter-practitionerrole-practitioner.html) | reference | `GET [base]/PractitionerRole?practitioner=[practitioner]` |
| **SHALL** | [organization](SearchParameter-practitionerrole-organization.html) | reference | `GET [base]/PractitionerRole?organization=[organization]` |
| **SHALL** | [location](SearchParameter-practitionerrole-location.html) | reference | `GET [base]/PractitionerRole?location=[location]` |
| **SHALL** | [service](SearchParameter-practitionerrole-service.html) | reference | `GET [base]/PractitionerRole?service=[service]` |
| **SHALL** | [network](SearchParameter-practitionerrole-network.html) | reference | `GET [base]/PractitionerRole?network=[network]` |
| **SHALL** | [endpoint](SearchParameter-practitionerrole-endpoint.html) | reference | `GET [base]/PractitionerRole?endpoint=[endpoint]` |
| **SHALL** | [role](SearchParameter-practitionerrole-role.html) | token | `GET [base]/PractitionerRole?role=[system]|[code]` |
| **SHALL** | [specialty](SearchParameter-practitionerrole-specialty.html) | token | `GET [base]/PractitionerRole?specialty=[system]|[code]` |
| **SHALL** | [\_id](http://hl7.org/fhir/R4/search.html) | token | `GET [base]/PractitionerRole?_id=[id]` |
| **SHALL** | [\_lastUpdated](http://hl7.org/fhir/R4/search.html) | date | `GET [base]/PractitionerRole?_lastUpdated=[_lastUpdated]` |

---

IG © 2022+ [HL7 Financial Management Working Group](http://www.hl7.org/Special/committees/fm). Package hl7.fhir.us.davinci-pdex-plan-net#1.1.0 based on [FHIR 4.0.1](http://hl7.org/fhir/R4/). Generated 2022-04-04

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html) |
[![CC0](cc0.png)](http://hl7.org/fhir/R4/license.html) |
[Propose a change](http://hl7.org/fhir-issues)