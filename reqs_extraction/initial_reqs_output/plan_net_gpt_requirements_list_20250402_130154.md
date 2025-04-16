---
# REQ-01
**Summary**: Support for Location representation
**Description**: "A Location is the physical place where healthcare services are provided, practitioners are employed, organizations are based, etc. Locations can range in scope from a room in a building to a geographic region/area."
**Verification**: Inspection
**Actor**: System
**Conformance**: SHALL
**Conditional**: False
**Source**: [PlannetLocation](StructureDefinition-plannet-Location.html)
---

---
# REQ-02
**Summary**: Network representation in healthcare provider insurance
**Description**: "A Network refers to a healthcare provider insurance network. A healthcare provider insurance network is an aggregation of organizations and individuals that deliver a set of services across a geography through health insurance products/plans."
**Verification**: Test
**Actor**: System
**Conformance**: SHALL
**Conditional**: False
**Source**: [PlannetNetwork](StructureDefinition-plannet-Network.html)
---

---
# REQ-03
**Summary**: Organization representation
**Description**: "An organization is a formal or informal grouping of people or organizations with a common purpose, such as a company, institution, corporation, community group, or healthcare practice."
**Verification**: Inspection
**Actor**: System
**Conformance**: SHALL
**Conditional**: False
**Source**: [PlannetOrganization](StructureDefinition-plannet-Organization.html)
---

---
# REQ-04
**Summary**: Describe relationships between organizations
**Description**: "The OrganizationAffiliation resource describes relationships between two or more organizations, including the services one organization provides another, the location(s) where they provide services, the availability of those services, electronic endpoints, and other relevant information."
**Verification**: Analysis
**Actor**: System
**Conformance**: SHALL
**Conditional**: False
**Source**: [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html)
---

---
# REQ-05
**Summary**: Representation of Practitioners
**Description**: "Practitioner is a person who is directly or indirectly involved in the provisioning of healthcare."
**Verification**: Inspection
**Actor**: System
**Conformance**: SHALL
**Conditional**: False
**Source**: [PlannetPractitioner](StructureDefinition-plannet-Practitioner.html)
---

---
# REQ-06
**Summary**: Define PractitionerRole
**Description**: "PractitionerRole describes the role a practitioner plays at an organization, including the services they provide, the location(s) where they work, and their availability, electronic endpoints, and other relevant information."
**Verification**: Test
**Actor**: System
**Conformance**: SHALL
**Conditional**: False
**Source**: [PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html)
---