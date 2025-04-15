---
# REQ-01
**Summary**: Advertise supported canonical URL for SubscriptionTopic
**Description**: "In order to allow for discovery of supported subscription topics, this guide defines the CapabilityStatement SubscriptionTopic Canonical extension. The extension allows server implementers to advertise the canonical URLs of topics available to clients."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Subscription Discovery Section

---
# REQ-02
**Summary**: Use of network codes
**Description**: "The code system used to define network types is available at:  [http://terminology.hl7.org/CodeSystem/network-type](http://terminology.hl7.org/CodeSystem/network-type)"
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: AcmeofCTPremNet.html

---
# REQ-03
**Summary**: Prohibit consumer identifying information for content queries.
**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations

---
# REQ-04
**Summary**: Prohibit sending consumer identifiable information when querying Plan-Net.
**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Privacy Considerations

---
# REQ-05
**Summary**: Populate all Must Support data elements for Health Plan API query results.
**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

---
# REQ-06
**Summary**: Omit data elements with minimum cardinality 0 when information is not present.
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0 , the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

---
# REQ-07
**Summary**: Provide reason for missing data elements with minimum cardinality > 0.
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Actor**: Server
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Health Plan API Requirements

---
# REQ-08
**Summary**: Process resource instances containing Must Support data elements without errors.
**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements

---
# REQ-09
**Summary**: Display or store Must Support data elements.
**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Inspection
**Actor**: Client
**Conformance**: SHOULD
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements

---
# REQ-10
**Summary**: Interpret missing Must Support data elements as not present in the Health Plan API system.
**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements

---
# REQ-11
**Summary**: Process resource instances containing Must Support data elements asserting missing information.
**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Actor**: Client
**Conformance**: SHALL
**Conditional**: False
**Source**: Implementation Notes/Must Support/Application Requirements

---
# REQ-12
**Summary**: Organizations shall define a set of HealthcareServices.
**Description**: "All organizations that provide service should define an appropriate set. of HealthcareServices to facilitate search."
**Verification**: Inspection
**Actor**: Organization
**Conformance**: SHALL
**Conditional**: False
**Source**: HealthcareService Section

---
# REQ-13
**Summary**: Payers shall offer one or more InsurancePlans.
**Description**: "Each payer will offer one or more products -- Insurance Plans"
**Verification**: Inspection
**Actor**: Payer
**Conformance**: SHALL
**Conditional**: False
**Source**: Insurance Plan and Network Section

---
# REQ-14
**Summary**: Each InsurancePlan shall be associated with one or more Networks.
**Description**: "and each plan is associated with one or more Networks."
**Verification**: Inspection
**Actor**: Payer
**Conformance**: SHALL
**Conditional**: False
**Source**: Insurance Plan and Network Section

---
# REQ-15
**Summary**: Practitioners indicate participation in a Network with a PractitionerRole.
**Description**: "Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively."
**Verification**: Inspection
**Actor**: Practitioner
**Conformance**: SHALL
**Conditional**: False
**Source**: Insurance Plan and Network Section
