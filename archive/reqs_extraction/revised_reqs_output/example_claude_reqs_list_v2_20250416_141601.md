---
# REQ-01
**Summary**: No authentication requirement
**Description**: "Health Plan API SHALL NOT require authentication for Plan-Net service access"
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Privacy Considerations Section
---

# REQ-02
**Summary**: No consumer identification requirement
**Description**: "Health Plan API SHALL NOT require directory mobile applications to send consumer identifying information in queries"
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Privacy Considerations Section
---

# REQ-03
**Summary**: No consumer information in queries
**Description**: "Application Actor SHALL NOT send consumer identifiable information when querying a Plan-Net service"
**Verification**: Test
**Actor**: Application Actor
**Conformance**: SHALL NOT
**Conditional**: False
**Source**: Privacy Considerations Section
---

# REQ-04
**Summary**: Must Support elements population
**Description**: "Health Plan API SHALL populate all Must Support data elements in query results"
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section
---

# REQ-05
**Summary**: Optional Must Support elements handling
**Description**: "Health Plan API SHALL NOT include Must Support data elements in resource instances when information is not present and minimum cardinality is 0"
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL NOT
**Conditional**: True
**Source**: Must Support Section
---

# REQ-06
**Summary**: Required Must Support elements handling
**Description**: "Health Plan API SHALL provide reason for missing information using nullFlavors or dataAbsentReason extension when Must Support element is absent and minimum cardinality is >0"
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: True
**Source**: Must Support Section
---

# REQ-07
**Summary**: Must Support elements processing
**Description**: "Application Actor SHALL process resource instances containing Must Support data elements without errors or application failure"
**Verification**: Test
**Actor**: Application Actor
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section
---

# REQ-08
**Summary**: Must Support elements display
**Description**: "Application Actor SHOULD display Must Support data elements for human use or store for other purposes"
**Verification**: Test
**Actor**: Application Actor
**Conformance**: SHOULD
**Conditional**: False
**Source**: Must Support Section
---

# REQ-09
**Summary**: Missing Must Support interpretation
**Description**: "Application Actor SHALL interpret missing Must Support data elements as data not present in Health Plan API system"
**Verification**: Test
**Actor**: Application Actor
**Conformance**: SHALL
**Conditional**: False
**Source**: Must Support Section
---

# REQ-10
**Summary**: Network documentation for practitioners
**Description**: "Health Plan API SHALL document practitioner network participation using PractitionerRole instances linked to Networks"
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Insurance Plan and Network Section
---

# REQ-11
**Summary**: Network documentation for organizations
**Description**: "Health Plan API SHALL document organization network participation using OrganizationAffiliation instances linked to Networks"
**Verification**: Test
**Actor**: Health Plan API
**Conformance**: SHALL
**Conditional**: False
**Source**: Insurance Plan and Network Section
---