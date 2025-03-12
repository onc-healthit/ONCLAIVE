# Artifacts Summary
This page is part of the DaVinci PDEX Plan Net (v1.1.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1\) based on [FHIR R4](http://hl7.org/fhir/R4). This is the current published version. For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/us/davinci-pdex-plan-net/history.html)
## Artifacts Summary
Contents:
* [Behavior: Capability Statements](#1)
* [Behavior: Search Parameters](#2)
* [Structures: Resource Profiles](#3)
* [Structures: Extension Definitions](#4)
* [Terminology: Value Sets](#5)
* [Terminology: Code Systems](#6)
* [Example: Example Instances](#7)
This page provides a list of the FHIR artifacts defined as part of this implementation guide.
### Behavior: Capability Statements
The following artifacts define the specific capabilities that different types of systems are expected to have in order to comply with this implementation guide. Systems conforming to this implementation guide are expected to declare conformance to one or more of the following capability statements.
| [Plan-Net CapabilityStatement](CapabilityStatement-plan-net.html "CapabilityStatement/plan-net") | This Section describes the expected capabilities of the Plan-Net Server actor which is responsible for providing responses to the queries submitted by the Plan-Net Requestors. The complete list of FHIR profiles, RESTful operations, and search parameters supported by Plan-Net Servers are defined. Systems implementing this capability statement should meet the CMS FInal Rule requirement for provider directory access. Plan-Net Clients can use the required capabilities to access necessary data based on their local use cases and other contextual requirements. |
| --- | --- |
### Behavior: Search Parameters
These define the properties by which a RESTful server can be searched. They can also be used for sorting and including related resources.
| [Plannet\_sp\_endpoint\_organization](SearchParameter-endpoint-organization.html "SearchParameter/endpoint-organization") | Select Endpoints managed by the specified organization |
| --- | --- |
| [Plannet\_sp\_healthcareservice\_coverage\_area](SearchParameter-healthcareservice-coverage-area.html "SearchParameter/healthcareservice-coverage-area") | Select services available in a region described by the specified location |
| [Plannet\_sp\_healthcareservice\_organization](SearchParameter-healthcareservice-organization.html "SearchParameter/healthcareservice-organization") | Select HealthcareServices provided by the specified organization |
| [Plannet\_sp\_healthcareservice\_endpoint](SearchParameter-healthcareservice-endpoint.html "SearchParameter/healthcareservice-endpoint") | Select HealthcareServices with the specified endpoint |
| [Plannet\_sp\_healthcareservice\_location](SearchParameter-healthcareservice-location.html "SearchParameter/healthcareservice-location") | Select HealthcareServices available at the specified location |
| [Plannet\_sp\_healthcareservice\_name](SearchParameter-healthcareservice-name.html "SearchParameter/healthcareservice-name") | Select HealthcareServices with the specified name |
| [Plannet\_sp\_healthcareservice\_category](SearchParameter-healthcareservice-service-category.html "SearchParameter/healthcareservice-service-category") | Select HealthcareServices providing the specified category of services |
| [Plannet\_sp\_healthcareservice\_type](SearchParameter-healthcareservice-service-type.html "SearchParameter/healthcareservice-service-type") | Select HealthcareServices of the specified type |
| [Plannet\_sp\_healthcareservice\_specialty](SearchParameter-healthcareservice-specialty.html "SearchParameter/healthcareservice-specialty") | Select services associated with the specified specialty |
| [Plannet\_sp\_insuranceplan\_administered\_by](SearchParameter-insuranceplan-administered-by.html "SearchParameter/insuranceplan-administered-by") | Select products that are administered by the specified organization |
| [Plannet\_sp\_insuranceplan\_coverage\_area](SearchParameter-insuranceplan-coverage-area.html "SearchParameter/insuranceplan-coverage-area") | Select products that are offered in the specified location |
| [Plannet\_sp\_insuranceplan\_identifier](SearchParameter-insuranceplan-identifier.html "SearchParameter/insuranceplan-identifier") | Select products with the specified identifier |
| [Plannet\_sp\_insuranceplan\_name](SearchParameter-insuranceplan-name.html "SearchParameter/insuranceplan-name") | Select products with the specified name |
| [Plannet\_sp\_insuranceplan\_owned\_by](SearchParameter-insuranceplan-owned-by.html "SearchParameter/insuranceplan-owned-by") | Select products that are owned by the specified organization |
| [Plannet\_sp\_insuranceplan\_plan\_type](SearchParameter-insuranceplan-plan-type.html "SearchParameter/insuranceplan-plan-type") | Select plans of the specified type |
| [Plannet\_sp\_insuranceplan\_type](SearchParameter-insuranceplan-type.html "SearchParameter/insuranceplan-type") | Select insurance plans of the specified type |
| [Plannet\_sp\_location\_address\_city](SearchParameter-location-address-city.html "SearchParameter/location-address-city") | Select Locations with the specified address.city |
| [Plannet\_sp\_location\_address\_postalcode](SearchParameter-location-address-postalcode.html "SearchParameter/location-address-postalcode") | Select Locations with the specified address |
| [Plannet\_sp\_location\_address\_state](SearchParameter-location-address-state.html "SearchParameter/location-address-state") | Select Locations with the specified address.state |
| [Plannet\_sp\_location\_address](SearchParameter-location-address.html "SearchParameter/location-address") | Select Locations with the specified address |
| [Plannet\_sp\_location\_endpoint](SearchParameter-location-endpoint.html "SearchParameter/location-endpoint") | Select Locations with the specified endpoint |
| [Plannet\_sp\_location\_organization](SearchParameter-location-organization.html "SearchParameter/location-organization") | Select Locations managed by the specified organization |
| [Plannet\_sp\_location\_partof](SearchParameter-location-partof.html "SearchParameter/location-partof") | Select Locations that are part of the specified location |
| [Plannet\_sp\_location\_type](SearchParameter-location-type.html "SearchParameter/location-type") | Select Locations of the specified type |
| [Plannet\_sp\_organization\_address](SearchParameter-organization-address.html "SearchParameter/organization-address") | Select organizations with the specified address (matches any of the string elements of an address) |
| [Plannet\_sp\_network\_coverage\_area](SearchParameter-organization-coverage-area.html "SearchParameter/organization-coverage-area") | Select health insurance provider networks available in a region described by the specified location |
| [Plannet\_sp\_organization\_endpoint](SearchParameter-organization-endpoint.html "SearchParameter/organization-endpoint") | Select Organizations with the specified endpoint |
| [Plannet\_sp\_organization\_name](SearchParameter-organization-name.html "SearchParameter/organization-name") | Select Organizations with the specified name |
| [Plannet\_sp\_organization\_partof](SearchParameter-organization-partof.html "SearchParameter/organization-partof") | Select Organizations that are part of the specified organization |
| [Plannet\_sp\_organization\_type](SearchParameter-organization-type.html "SearchParameter/organization-type") | Select Organizations of the specified type |
| [Plannet\_sp\_organizationaffiliation\_endpoint](SearchParameter-organizationaffiliation-endpoint.html "SearchParameter/organizationaffiliation-endpoint") | Select OrganizationAffiliations with the specified endpoint |
| [Plannet\_sp\_organizationaffiliation\_location](SearchParameter-organizationaffiliation-location.html "SearchParameter/organizationaffiliation-location") | Select OrganizationAffiliations available at the specified location |
| [Plannet\_sp\_organizationaffiliation\_network](SearchParameter-organizationaffiliation-network.html "SearchParameter/organizationaffiliation-network") | Select roles where the organization is a member of the specified health insurance provider network |
| [Plannet\_sp\_organizationaffiliation\_participating\_organization](SearchParameter-organizationaffiliation-participating-organization.html "SearchParameter/organizationaffiliation-participating-organization") | Select roles filled by the specified organization |
| [Plannet\_sp\_organizationaffiliation\_period](SearchParameter-organizationaffiliation-period.html "SearchParameter/organizationaffiliation-period") | Select Organization Affiliations available in the specified period |
| [Plannet\_sp\_organizationaffiliation\_primary\_organization](SearchParameter-organizationaffiliation-primary-organization.html "SearchParameter/organizationaffiliation-primary-organization") | Select roles offered by the specified organization |
| [Plannet\_sp\_organizationaffiliation\_role](SearchParameter-organizationaffiliation-role.html "SearchParameter/organizationaffiliation-role") | Select OrganizationAffiliations with the specified role |
| [Plannet\_sp\_organizationaffiliation\_service](SearchParameter-organizationaffiliation-service.html "SearchParameter/organizationaffiliation-service") | Select OrganizationAffiliations providing the specified service |
| [Plannet\_sp\_organizationaffiliation\_specialty](SearchParameter-organizationaffiliation-specialty.html "SearchParameter/organizationaffiliation-specialty") | Select OrganizationAffiliations associated with the specified specialty |
| [Plannet\_sp\_practitioner\_family\_name](SearchParameter-practitioner-family-name.html "SearchParameter/practitioner-family-name") | Select Practitioners with the specified family name |
| [Plannet\_sp\_practitioner\_given\_name](SearchParameter-practitioner-given-name.html "SearchParameter/practitioner-given-name") | Select Practitioners with the specified given name |
| [Plannet\_sp\_practitioner\_name](SearchParameter-practitioner-name.html "SearchParameter/practitioner-name") | Select Practitioners with the specified name (matches against any of the elements in the HumanName data type) |
| [Plannet\_sp\_practitionerrole\_endpoint](SearchParameter-practitionerrole-endpoint.html "SearchParameter/practitionerrole-endpoint") | Select PractitionerRoles with the specified endpoint |
| [Plannet\_sp\_practitionerrole\_location](SearchParameter-practitionerrole-location.html "SearchParameter/practitionerrole-location") | Select PractitionerRoles available at the specified location |
| [Plannet\_sp\_practitionerrole\_network](SearchParameter-practitionerrole-network.html "SearchParameter/practitionerrole-network") | Select roles where the practitioner is a member of the specified health insurance provider network |
| [Plannet\_sp\_practitionerrole\_organization](SearchParameter-practitionerrole-organization.html "SearchParameter/practitionerrole-organization") | Select PractitionerRoles available at the specified organization |
| [Plannet\_sp\_practitionerrole\_period](SearchParameter-practitionerrole-period.html "SearchParameter/practitionerrole-period") | Select PractitionerRoles available in the specified period |
| [Plannet\_sp\_practitionerrole\_practitioner](SearchParameter-practitionerrole-practitioner.html "SearchParameter/practitionerrole-practitioner") | Select roles filled by the specified practitioner |
| [Plannet\_sp\_practitionerrole\_role](SearchParameter-practitionerrole-role.html "SearchParameter/practitionerrole-role") | Select PractitionerRoles with the specified role |
| [Plannet\_sp\_practitionerrole\_service](SearchParameter-practitionerrole-service.html "SearchParameter/practitionerrole-service") | Select PractitionerRoles providing the specified service |
| [Plannet\_sp\_practitionerrole\_specialty](SearchParameter-practitionerrole-specialty.html "SearchParameter/practitionerrole-specialty") | Select PractitionerRoles associated with the specified specialty |
### Structures: Resource Profiles
These define constraints on FHIR resources for systems conforming to this implementation guide
| [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html "StructureDefinition/plannet-Endpoint") | The technical details of an endpoint that can be used for electronic services, such as a portal or FHIR REST services, messaging or operations, or DIRECT messaging. |
| --- | --- |
| [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html "StructureDefinition/plannet-HealthcareService") | The HealthCareService resource typically describes services offered by an organization/practitioner at a location. The resource may be used to encompass a variety of services covering the entire healthcare spectrum, including promotion, prevention, diagnostics, pharmacy, hospital and ambulatory care, home care, long-term care, and other health-related and community services. |
| [Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html "StructureDefinition/plannet-InsurancePlan") | An InsurancePlan is a discrete package of health insurance coverage benefits that are offered under a particular network type. A given payer’s products typically differ by network type and/or covered benefits. A plan pairs a product’s covered benefits with the particular cost sharing structure offered to a consumer. A given product may comprise multiple plans (i.e. each plan offers different cost sharing requirements for the same set of covered benefits). InsurancePlan describes a health insurance offering comprised of a list of covered benefits (i.e. the product), costs associated with those benefits (i.e. the plan), and additional information about the offering, such as who it is owned and administered by, a coverage area, contact information, etc. |
| [Plan-Net Location](StructureDefinition-plannet-Location.html "StructureDefinition/plannet-Location") | A Location is the physical place where healthcare services are provided, practitioners are employed,   organizations are based, etc. Locations can range in scope from a room in a building to a geographic region/area. |
| [Plan-Net Network](StructureDefinition-plannet-Network.html "StructureDefinition/plannet-Network") | A Network refers to a healthcare provider insurance network. A healthcare provider insurance network is an aggregation of organizations and individuals that deliver a set of services across a geography through health insurance products/plans. A network is typically owned by a payer. In the PlanNet IG, individuals and organizations are represented as participants in a PLan-Net Network through the practitionerRole and Plan-Net-organizationAffiliation resources, respectively. |
| [Plan-Net Organization](StructureDefinition-plannet-Organization.html "StructureDefinition/plannet-Organization") | An organization is a formal or informal grouping of people or organizations with a common purpose, such as a company, institution, corporation, community group, or healthcare practice. Guidance: When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text |
| [Plan-Net OrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html "StructureDefinition/plannet-OrganizationAffiliation") | The OrganizationAffiliation resource describes relationships between two or more organizations, including the services one organization provides another, the location(s) where they provide services, the availability of those services, electronic endpoints, and other relevant information. |
| [Plan-Net Practitioner](StructureDefinition-plannet-Practitioner.html "StructureDefinition/plannet-Practitioner") | Practitioner is a person who is directly or indirectly involved in the provisioning of healthcare. |
| [Plan-Net PractitionerRole](StructureDefinition-plannet-PractitionerRole.html "StructureDefinition/plannet-PractitionerRole") | PractionerRole describes details about a provider, which can be a practitioner or an organization. When the provider is a practitioner,  there may be a relationship to an organization. A provider renders services to patients at a location. When the provider is a practitioner, there may also  be a relationship to an organization. Practitioner participation in healthcare provider insurance networks may be direct or through their role at an organization. |
### Structures: Extension Definitions
These define constraints on FHIR data types for systems conforming to this implementation guide
| [Accessibility](StructureDefinition-accessibility.html "StructureDefinition/accessibility") | An extension to describe accessibility options offered by a practitioner or at a location. |
| --- | --- |
| [Communication Proficiency](StructureDefinition-communication-proficiency.html "StructureDefinition/communication-proficiency") | An extension to express a practitioner’s spoken proficiency with the language indicated in practitioner.communication. |
| [Contactpoint Availabletime](StructureDefinition-contactpoint-availabletime.html "StructureDefinition/contactpoint-availabletime") | An extension representing the days and times a contact point is available |
| [Delivery Method](StructureDefinition-delivery-method.html "StructureDefinition/delivery-method") | An extension describing the service delivery method. If service delivery is virtual, one or more delivery modalities should be specified. |
| [Endpoint Usecase](StructureDefinition-endpoint-usecase.html "StructureDefinition/endpoint-usecase") | EndpointUseCase is an enumeration of the specific use cases (service descriptions) supported by the endpoint |
| [Location Reference](StructureDefinition-location-reference.html "StructureDefinition/location-reference") | A reference to a Location resource (plannet-Location) defining the coverage area of a health insurance provider network |
| [Network Reference](StructureDefinition-network-reference.html "StructureDefinition/network-reference") | A reference to the healthcare provider insurance networks (plannet-Network) the practitioner participates in through their role |
| [New Patients](StructureDefinition-newpatients.html "StructureDefinition/newpatients") | New Patients indicates whether new patients are being accepted in general, or from a specific network.   This extension is included in the PractitionerRole, HealthcareService, and Location profiles.  This provides needed flexibility for specifying whether a provider accepts new patients by location and network. |
| [Org Description](StructureDefinition-org-description.html "StructureDefinition/org-description") | An extension to provide a human-readable description of an organization. |
| [Practitioner Qualification](StructureDefinition-practitioner-qualification.html "StructureDefinition/practitioner-qualification") | An extension to add status and whereValid elements to a practitioner’s qualifications. |
| [Qualification](StructureDefinition-qualification.html "StructureDefinition/qualification") | An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances). |
| [Via Intermediary](StructureDefinition-via-intermediary.html "StructureDefinition/via-intermediary") | A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization |
### Terminology: Value Sets
These define sets of codes used by systems conforming to this implementation guide
| [Accepting Patients Codes VS](ValueSet-AcceptingPatientsVS.html "ValueSet/AcceptingPatientsVS") | Codes to identify if the practice is accepting new patients |
| --- | --- |
| [Accessibility VS](ValueSet-AccessibilityVS.html "ValueSet/AccessibilityVS") | Codes for documenting general categories of accommodations available. |
| [Delivery Methods VS](ValueSet-DeliveryMethodVS.html "ValueSet/DeliveryMethodVS") | Codes for documenting delivery methods. |
| [Endpoint Connection Types VS](ValueSet-EndpointConnectionTypeVS.html "ValueSet/EndpointConnectionTypeVS") | Endpoint Connection Types |
| [Endpoint Payload Types VS](ValueSet-EndpointPayloadTypeVS.html "ValueSet/EndpointPayloadTypeVS") | Endpoint Payload Types are constrained to NA (Not Applicable) as part of this IG |
| [Endpoint Usecases VS](ValueSet-EndpointUsecaseVS.html "ValueSet/EndpointUsecaseVS") | Codes for documenting business use case by a general grouping by business area. |
| [Healthcare Service CategoryVS](ValueSet-HealthcareServiceCategoryVS.html "ValueSet/HealthcareServiceCategoryVS") | Broad categories of healthcare services being performed or delivered. |
| [HealthcareService Types VS](ValueSet-HealthcareServiceTypeVS.html "ValueSet/HealthcareServiceTypeVS") | Valueset for HealthCareService type |
| [Individual and Group Specialties](ValueSet-IndividualAndGroupSpecialtiesVS.html "ValueSet/IndividualAndGroupSpecialtiesVS") | Individual and Group Specialties from National Uniform Claim Committee (NUCC) Health Care Provider Taxonomy code set. |
| [Individual Specialties, Degrees, Licenses, and Certificates VS](ValueSet-IndividualSpecialtyAndDegreeLicenseCertificateVS.html "ValueSet/IndividualSpecialtyAndDegreeLicenseCertificateVS") | Individual Specialties, Degrees, Licenses, and Certificates |
| [Insurance Plan TypeVS](ValueSet-InsurancePlanTypeVS.html "ValueSet/InsurancePlanTypeVS") | Categories of cost-sharing used by plans. |
| [Insurance Product Type VS](ValueSet-InsuranceProductTypeVS.html "ValueSet/InsuranceProductTypeVS") | A distinct package of health insurance coverage benefits that are offered using a particular product network type. |
| [Language Proficiency VS](ValueSet-LanguageProficiencyVS.html "ValueSet/LanguageProficiencyVS") | Codes for documenting spoken language proficiency based on the Interagency Language Roundtable scale of abilities to communicate in a language. |
| [Minimum Endpoint Connection Types VS](ValueSet-MinEndpointConnectionTypeVS.html "ValueSet/MinEndpointConnectionTypeVS") | Minimum Endpoint Connection Types |
| [Network Type VS](ValueSet-NetworkTypeVS.html "ValueSet/NetworkTypeVS") | Single value describing networks. |
| [Non-Individual Specialties](ValueSet-NonIndividualSpecialtiesVS.html "ValueSet/NonIndividualSpecialtiesVS") | Non-Individual Specialties from National Uniform Claim Committee (NUCC) Health Care Provider Taxonomy code set. |
| [Non-Individual Specialties, Degrees, Licenses, and Certificates VS](ValueSet-NonIndividualSpecialtyAndDegreeLicenseCertificateVS.html "ValueSet/NonIndividualSpecialtyAndDegreeLicenseCertificateVS") | Non-Individual Specialties, Degrees, Licenses, and Certificates |
| [Organization Type VS](ValueSet-OrgTypeVS.html "ValueSet/OrgTypeVS") | Categories of organizations based on criteria in provider directories. |
| [OrganizationAffiliation Roles](ValueSet-OrganizationAffiliationRoleVS.html "ValueSet/OrganizationAffiliationRoleVS") | Value Set for Organization Affiliation Roles |
| [PractitionerRole Code VS](ValueSet-PractitionerRoleVS.html "ValueSet/PractitionerRoleVS") | Codes for the capabilities that an individual, group, or organization is acknowledged to have in a payer network, including general codes from the HL7 PractitionerRole Code System. |
| [Qualification Status VS](ValueSet-QualificationStatusVS.html "ValueSet/QualificationStatusVS") | The state indicating if a qualification is currently valid. |
| [Specialties VS](ValueSet-SpecialtiesVS.html "ValueSet/SpecialtiesVS") | Specialties value set based on National Uniform Claim Committee (NUCC) Health Care Provider Taxonomy code set. |
| [Specialties, Degrees, Licenses, and Certificates VS](ValueSet-SpecialtyAndDegreeLicenseCertificateVS.html "ValueSet/SpecialtyAndDegreeLicenseCertificateVS") | Specialties and Degree License and Certificates |
| [Virtual Modalities VS](ValueSet-VirtualModalitiesVS.html "ValueSet/VirtualModalitiesVS") | Codes for virtual service delivery modalities . |
### Terminology: Code Systems
These define new code systems used by systems conforming to this implementation guide
| [Accepting Patients Codes](CodeSystem-AcceptingPatientsCS.html "CodeSystem/AcceptingPatientsCS") | Codes to identify if the practice is accepting new patients |
| --- | --- |
| [Accessibility CS](CodeSystem-AccessibilityCS.html "CodeSystem/AccessibilityCS") | General categories of accommodations available. |
| [Delivery Methods](CodeSystem-DeliveryMethodCS.html "CodeSystem/DeliveryMethodCS") | Categories of healthcare service delivery methods. |
| [Endpoint Connection Types (additional)](CodeSystem-EndpointConnectionTypeCS.html "CodeSystem/EndpointConnectionTypeCS") | Extension codes for http://terminology.hl7.org/CodeSystem/endpoint-connection-type |
| [Endpoint Payload Types](CodeSystem-EndpointPayloadTypeCS.html "CodeSystem/EndpointPayloadTypeCS") | Endpoint Payload Types are constrained to NA (Not Applicable) as part of this IG |
| [Healthcare Service Category](CodeSystem-HealthcareServiceCategoryCS.html "CodeSystem/HealthcareServiceCategoryCS") | Broad categories of healthcare services being performed or delivered |
| [Insurance Plan Type](CodeSystem-InsurancePlanTypeCS.html "CodeSystem/InsurancePlanTypeCS") | Categories of cost-sharing used by plans |
| [Insurance Product Type](CodeSystem-InsuranceProductTypeCS.html "CodeSystem/InsuranceProductTypeCS") | A distinct package of health insurance coverage benefits that are offered using a particular product network type. |
| [Language Proficiency CS](CodeSystem-LanguageProficiencyCS.html "CodeSystem/LanguageProficiencyCS") | Codes for documenting spoken language proficiency based on the Interagency Language Roundtable scale of abilities to communicate in a language. |
| [Organization Type](CodeSystem-OrgTypeCS.html "CodeSystem/OrgTypeCS") | Categories of organizations based on criteria in provider directories. |
| [Organization Affiliation Role](CodeSystem-OrganizationAffiliationRoleCS.html "CodeSystem/OrganizationAffiliationRoleCS") | Codes For Organization Affiliation Role |
| [Provider Role Codes](CodeSystem-ProviderRoleCS.html "CodeSystem/ProviderRoleCS") | A capability that an individual, group, or organization is acknowledged to have in a payer network. |
| [Qualification Status](CodeSystem-QualificationStatusCS.html "CodeSystem/QualificationStatusCS") | The state indicating if a qualification is currently valid. |
| [Virtual Modalities](CodeSystem-VirtualModalitiesCS.html "CodeSystem/VirtualModalitiesCS") | Categories of virtual service delivery modalities. |
### Example: Example Instances
These are example instances that show what data produced and consumed by systems conforming with this implementation guide might look like
| [Acme](Organization-Acme.html "Organization/Acme") | Payer Organization |
| --- | --- |
| [AcmeOfCTPortalEndpoint](Endpoint-AcmeOfCTPortalEndpoint.html "Endpoint/AcmeOfCTPortalEndpoint") | Endpoint for Acme of CT Portal |
| [AcmeQHPBronze](InsurancePlan-AcmeQHPBronze.html "InsurancePlan/AcmeQHPBronze") | Acme of CT QHP Bronze Plan |
| [AcmeQHPGold](InsurancePlan-AcmeQHPGold.html "InsurancePlan/AcmeQHPGold") | Acme of CT QHP Gold Plan |
| [AcmeofCTPremNet](Organization-AcmeofCTPremNet.html "Organization/AcmeofCTPremNet") | Acme of CT Premium Premium Network |
| [AcmeofCTStdNet](Organization-AcmeofCTStdNet.html "Organization/AcmeofCTStdNet") | Acme of CT Standard Network |
| [AnonRole](PractitionerRole-AnonRole.html "PractitionerRole/AnonRole") | Practitioner role that doesn’t refer to a specific practitioner |
| [BigBox](Organization-BigBox.html "Organization/BigBox") | Organization that Manages 2 of PharmChain’s pharmacies |
| [BurrClinic](Organization-BurrClinic.html "Organization/BurrClinic") | Burr Clinic provides service to Hartford Hospital |
| [BurrClinicAffil](OrganizationAffiliation-BurrClinicAffil.html "OrganizationAffiliation/BurrClinicAffil") | Burr Clinic’s affiliation with Acme of CT Provider Network and Hartford General Hospital |
| [BurrClinicServices](HealthcareService-BurrClinicServices.html "HealthcareService/BurrClinicServices") | Burr Clinic Services |
| [CancerClinic](Organization-CancerClinic.html "Organization/CancerClinic") | HartfordCancerClinicLLC |
| [CancerClinicLoc](Location-CancerClinicLoc.html "Location/CancerClinicLoc") | Location1 of Cancer Clinic |
| [CancerClinicService](HealthcareService-CancerClinicService.html "HealthcareService/CancerClinicService") | Cancer Clinic Services |
| [ConnHIE](Organization-ConnHIE.html "Organization/ConnHIE") | Connecticut HIE |
| [ConnHIEAffil](OrganizationAffiliation-ConnHIEAffil.html "OrganizationAffiliation/ConnHIEAffil") | Burr Clinic’s affiliation with Conn HIE |
| [Counselor](Practitioner-Counselor.html "Practitioner/Counselor") | Counselor Susie Smith |
| [CounselorRole1](PractitionerRole-CounselorRole1.html "PractitionerRole/CounselorRole1") | Susie Smith is a counselor via Telemedicine |
| [HamiltonClinic](Organization-HamiltonClinic.html "Organization/HamiltonClinic") | Hamilton Clinic (a Division of Hartford Hospital) |
| [HamiltonClinicAffil](OrganizationAffiliation-HamiltonClinicAffil.html "OrganizationAffiliation/HamiltonClinicAffil") | Hamilton Clinic’s affiliation with Acme of CT Provider Network and Hartford General Hospital |
| [HamiltonClinicServices](HealthcareService-HamiltonClinicServices.html "HealthcareService/HamiltonClinicServices") | Hamilton Clinic Services |
| [HansSolo](Practitioner-HansSolo.html "Practitioner/HansSolo") | Solo Practitioner Hans Solo |
| [HansSoloClinic](Location-HansSoloClinic.html "Location/HansSoloClinic") | Location of Hans Solo’s clinic |
| [HansSoloRole1](PractitionerRole-HansSoloRole1.html "PractitionerRole/HansSoloRole1") | Hans Solo is a solo practitioner |
| [HansSoloService](HealthcareService-HansSoloService.html "HealthcareService/HansSoloService") | Hans Solo Services |
| [HartfordOrthopedicAffil](OrganizationAffiliation-HartfordOrthopedicAffil.html "OrganizationAffiliation/HartfordOrthopedicAffil") | Hartford Orthopedic Services affiliation with Acme of CT Provider Network and Hartford General Hospital |
| [HartfordOrthopedicServices](HealthcareService-HartfordOrthopedicServices.html "HealthcareService/HartfordOrthopedicServices") | Hartford Orthopedic Services |
| [HartfordOrthopedics](Organization-HartfordOrthopedics.html "Organization/HartfordOrthopedics") | Hartford Orthpedic Services is a group providing Orthpods for Acme of CT at Hartford General Hospital |
| [HospERService](HealthcareService-HospERService.html "HealthcareService/HospERService") | Hartford General Hospital ER |
| [HospLoc1](Location-HospLoc1.html "Location/HospLoc1") | Location1 of Hartford Hospital |
| [HospLoc2](Location-HospLoc2.html "Location/HospLoc2") | Location2 of Hartford Hospital |
| [Hospital](Organization-Hospital.html "Organization/Hospital") | Hartford General Hospital |
| [JoeSmith](Practitioner-JoeSmith.html "Practitioner/JoeSmith") | Practitioner Dr Joe Smith |
| [JoeSmithRole1](PractitionerRole-JoeSmithRole1.html "PractitionerRole/JoeSmithRole1") | Dr Smith moonlighting as ER Doc at Hartford Hospital |
| [JoeSmithRole2](PractitionerRole-JoeSmithRole2.html "PractitionerRole/JoeSmithRole2") | Dr Smith Internal Medicine at Burr Clinic |
| [JoeSmithRole3](PractitionerRole-JoeSmithRole3.html "PractitionerRole/JoeSmithRole3") | Dr Smith Admitting Privileges at Hartford General |
| [PharmChain](Organization-PharmChain.html "Organization/PharmChain") | Organization that Provides Pharmacy Services |
| [PharmChainAffil1](OrganizationAffiliation-PharmChainAffil1.html "OrganizationAffiliation/PharmChainAffil1") | Organization Affiliation for PharmChain (Retail) |
| [PharmChainAffil2](OrganizationAffiliation-PharmChainAffil2.html "OrganizationAffiliation/PharmChainAffil2") | Organization Affiliation for PharmChain (Compounding) |
| [PharmChainAffil3](OrganizationAffiliation-PharmChainAffil3.html "OrganizationAffiliation/PharmChainAffil3") | Organization Affiliation for PharmChain (MailOrder) |
| [PharmChainCompService](HealthcareService-PharmChainCompService.html "HealthcareService/PharmChainCompService") | Compound Pharmacy Service provided by PharmacyOrganization A |
| [PharmChainMailService](HealthcareService-PharmChainMailService.html "HealthcareService/PharmChainMailService") | Mail Order Pharmacy Service provided by PharmacyOrganization A |
| [PharmChainRetailService](HealthcareService-PharmChainRetailService.html "HealthcareService/PharmChainRetailService") | Pharmacy Service provided by PharmChain |
| [PharmLoc1](Location-PharmLoc1.html "Location/PharmLoc1") | Location of Pharmacy1 in PharmChain’s network |
| [PharmLoc2](Location-PharmLoc2.html "Location/PharmLoc2") | Location of Pharmacy2 in PharmChain’s network |
| [PharmLoc3](Location-PharmLoc3.html "Location/PharmLoc3") | Location of Pharmacy3 in PharmChain’s network |
| [PharmLoc4](Location-PharmLoc4.html "Location/PharmLoc4") | Location of Pharmacy4 in PharmChain’s network |
| [StateOfCTLocation](Location-StateOfCTLocation.html "Location/StateOfCTLocation") | State of CT Area |
| [VirtualCounselService](HealthcareService-VirtualCounselService.html "HealthcareService/VirtualCounselService") | Virtual Counseling Service |