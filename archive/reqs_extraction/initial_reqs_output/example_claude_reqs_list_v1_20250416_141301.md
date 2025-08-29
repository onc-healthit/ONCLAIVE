## REQ-01

**Summary**: No authentication for Plan-Net service access
**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."
**Verification**: Test
**Notes**: Actor: Health Plan API, Conformance: SHOULD, Conditional: False
**Source**: Privacy Considerations Section

## REQ-02

**Summary**: No consumer identification required
**Description**: "A conformant Plan-Net service SHALL NOT require a directory mobile application to send consumer identifying information in order to query content."
**Verification**: Test
**Notes**: Actor: Health Plan API, Conformance: SHALL NOT, Conditional: False
**Source**: Privacy Considerations Section

## REQ-03

**Summary**: No consumer information sent in queries
**Description**: "A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service."
**Verification**: Test
**Notes**: Actor: Application Actor, Conformance: SHALL NOT, Conditional: False
**Source**: Privacy Considerations Section

## REQ-04

**Summary**: Population of Must Support elements
**Description**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."
**Verification**: Test
**Notes**: Actor: Health Plan API, Conformance: SHALL, Conditional: False
**Source**: Must Support Section

## REQ-05

**Summary**: Handling absent optional Must Support elements
**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors SHALL NOT include the data elements in the resource instance returned as part of the query results."
**Verification**: Test
**Notes**: Actor: Health Plan API, Conformance: SHALL NOT, Conditional: True (when Must Support element is absent and min cardinality is 0)
**Source**: Must Support Section

## REQ-06

**Summary**: Handling absent required Must Support elements
**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."
**Verification**: Test
**Notes**: Actor: Health Plan API, Conformance: SHALL, Conditional: True (when Must Support element is absent and min cardinality > 0)
**Source**: Must Support Section

## REQ-07

**Summary**: Processing Must Support elements
**Description**: "Application actors SHALL be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."
**Verification**: Test
**Notes**: Actor: Application Actor, Conformance: SHALL, Conditional: False
**Source**: Must Support Section

## REQ-08

**Summary**: Display of Must Support elements
**Description**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."
**Verification**: Test
**Notes**: Actor: Application Actor, Conformance: SHOULD, Conditional: False
**Source**: Must Support Section

## REQ-09

**Summary**: Interpretation of missing Must Support elements
**Description**: "When querying Health Plan API actors, Application actors SHALL interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."
**Verification**: Test
**Notes**: Actor: Application Actor, Conformance: SHALL, Conditional: False
**Source**: Must Support Section

## REQ-10

**Summary**: Processing missing Must Support information
**Description**: "Consumer App actors SHALL be able to process resource instances containing Must Support data elements asserting missing information."
**Verification**: Test
**Notes**: Actor: Application Actor, Conformance: SHALL, Conditional: False
**Source**: Must Support Section## REQ-01

**Summary**: Network Participation Documentation - Practitioners
**Description**: "Practitioners indicate participation in a Network with a link to the Network using a PractitionerRole instance"
**Verification**: Inspection
**Notes**: Actor: Health Plan API Actor, Conformance: SHALL (implied), Conditional: False
**Source**: Insurance Plan and Network Section

## REQ-02

**Summary**: Network Participation Documentation - Organizations  
**Description**: "Organizations indicate participation in a Network with a link to the Network using an OrganizationAffiliation instance"
**Verification**: Inspection
**Notes**: Actor: Health Plan API Actor, Conformance: SHALL (implied), Conditional: False
**Source**: Insurance Plan and Network Section

## REQ-03

**Summary**: PractitionerRole Resource Relationships
**Description**: "PractitionerRole instances are what tie Practitioners to HealthcareServices, Organizations, Networks and Locations"
**Verification**: Inspection
**Notes**: Actor: Health Plan API Actor, Conformance: SHALL (implied), Conditional: False
**Source**: Insurance Plan and Network Section

## REQ-04

**Summary**: OrganizationAffiliation Resource Relationships
**Description**: "OrganizationAffiliation instances are what tie Organizations to HealthcareServices, Organizations, Networks and Locations"
**Verification**: Inspection
**Notes**: Actor: Health Plan API Actor, Conformance: SHALL (implied), Conditional: False 
**Source**: Insurance Plan and Network Section