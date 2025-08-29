---
# REQ-34
**Summary**: Organization search by name
**Description**: "The Plan-Net design is based around the following types of searches: Organization by Name - Example: Montgomery Cardiology or CVS - Focal Resource and Field: Organization.name - Qualifications of Search: Location, network, specialty."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Design requirement)
**Conditional**: False
**Source**: Representing and Searching Provider Directory Data (5.2)
---

---
# REQ-35
**Summary**: Provider search by specialty
**Description**: "The Plan-Net design is based around the following types of searches: Provider by Specialty - Example: Cardiologist - Focal Resource and Field: PractitionerRole.specialty - Qualifications of Search: Location, network, name."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Design requirement)
**Conditional**: False
**Source**: Representing and Searching Provider Directory Data (5.2)
---

---
# REQ-36
**Summary**: Organization search by specialty
**Description**: "The Plan-Net design is based around the following types of searches: Organization by specialty - Example: Compounding Pharmacy - Focal Resource and Field: OrganizationAffiliation.specialty - Qualifications of Search: Location, network, name."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Design requirement)
**Conditional**: False
**Source**: Representing and Searching Provider Directory Data (5.2)
---

---
# REQ-37
**Summary**: Search for active practitioners and organizations
**Description**: "Sample query to search for currently active Practitioners (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/PractitionerRole?_include=PractitionerRole:date=ge2021-10-25. Sample query to search for currently active Organizations (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/OrganizationAffiliation?_include=OrganizationAffiliation:date=ge2021-10-25."
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: None (Implementation example)
**Conditional**: False
**Source**: Searching for active Practitioners and Organizations (5.2.1)
---

---
# REQ-38
**Summary**: Network contact handling for departments
**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."
**Verification**: Inspection
**Actor**: Health Plan API
**Conformance**: None (Implementation guidance)
**Conditional**: True
**Source**: Network Implementation Guidance (7.57.1.1)
---
