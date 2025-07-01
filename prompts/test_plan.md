Analyze the following FHIR Implementation Guide requirement and create a comprehensive test specification, 
taking into account the relevant Capability Statement information. 

For the requirement:
{requirement}

Relevant Capability Statement information for this requirement:
{capability_info}

Create a structured test specification with the following sections:

1. Requirement ID

2. Requirement Analysis:
   - Testability Assessment: Classify as automatically testable, an attestation, or not testable due to being too vague or covered by the validator
   - Complexity: Simple, Moderate, or Complex
   - Prerequisites: Required system configurations, data, or setup

3. Test Implementation Strategy:
   - Required inputs including required FHIR resources and expected outputs for the test
   - Required FHIR Operations: List any specific API calls/operations needed (ensure these are suported in the Capability Statement)
   - Validation Criteria: Specific checks to verify conformance; what assertions or results should there be to indicate passing of a test

Format your response as markdown with clear headers.

Notes: 
1) The test plan should focus on testing for interoperability conformance, not testing for bugs or all edge cases. Write the test plan at an appropriate level to achieve this.
2) The test plan should be written to accommodate a "bring your own data" approach for testing conformance. Do not configure fixtures and ensure that the test plan would outline test cases that could work with whatever data is used by the tester. 