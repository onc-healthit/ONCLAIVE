Analyze the following requirement from a FHIR Implementation Guide and identify the most appropriate category or group it belongs to.

Requirement:
{requirement}

Group the requirements by the resource profiles that make up the implementation guide from which these requirements were extracted:
Endpoint, HealthcareService, InsurancePlan, Location, Network, Organization, OrganizationAffiliation, Practitioner, and PractionerRole

If the requirement does not belong to any of the specific resource profiles listed, use one of the following categories instead:
- General/Cross-Resource
- Security
- Privacy

Or generate a more appropriate group title not listed.

Descriptions of the specific resource profiles are below:
- Plan-Net Endpoint: The technical details of an endpoint that can be used for electronic services, such as a portal or FHIR REST services, messaging or operations, or DIRECT messaging.
- Plan-Net HealthcareService: The HealthCareService resource typically describes services offered by an organization/practitioner at a location. The resource may be used to encompass a variety of services covering the entire healthcare spectrum, including promotion, prevention, diagnostics, pharmacy, hospital and ambulatory care, home care, long-term care, and other health-related and community services.
- Plan-Net InsurancePlan: An InsurancePlan is a discrete package of health insurance coverage benefits that are offered under a particular network type. A given payer’s products typically differ by network type and/or covered benefits. A plan pairs a product’s covered benefits with the particular cost sharing structure offered to a consumer. A given product may comprise multiple plans (i.e. each plan offers different cost sharing requirements for the same set of covered benefits). InsurancePlan describes a health insurance offering comprised of a list of covered benefits (i.e. the product), costs associated with those benefits (i.e. the plan), and additional information about the offering, such as who it is owned and administered by, a coverage area, contact information, etc.
- Plan-Net Location: A Location is the physical place where healthcare services are provided, practitioners are employed, organizations are based, etc. Locations can range in scope from a room in a building to a geographic region/area.
- Plan-Net Network: A Network refers to a healthcare provider insurance network. A healthcare provider insurance network is an aggregation of organizations and individuals that deliver a set of services across a geography through health insurance products/plans. A network is typically owned by a payer. In the PlanNet IG, individuals and organizations are represented as participants in a PLan-Net Network through the practitionerRole and Plan-Net-organizationAffiliation resources, respectively.
- Plan-Net Organization: An organization is a formal or informal grouping of people or organizations with a common purpose, such as a company, institution, corporation, community group, or healthcare practice. Guidance: When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text
- Plan-Net OrganizationAffiliation: The OrganizationAffiliation resource describes relationships between two or more organizations, including the services one organization provides another, the location(s) where they provide services, the availability of those services, electronic endpoints, and other relevant information.
- Plan-Net Practitioner: Practitioner is a person who is directly or indirectly involved in the provisioning of healthcare.
- Plan-Net PractitionerRole: PractitionerRole typically describes details about a provider. When the provider is a practitioner, there may be a relationship to an organization. A provider renders services to patients at a location. Practitioner participation in healthcare provider insurance networks may be direct or through their role at an organization. PractitionerRole involves either the actual or potential (hence the optionality on Practitioner) of an individual to play this role on behalf of or under the auspices of an organization. The absence of a Practitioner resource does not imply that the Organization itself is playing the role of a Practitioner, instead it implies that that role has been established by the Organization and MAY apply that to a specific Practitioner. 

Return only the category name that best represents this requirement's grouping, with no additional text or explanation.