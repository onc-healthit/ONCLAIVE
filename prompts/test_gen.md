Convert the following FHIR test specification into executable Ruby code using the Inferno testing framework.

Test Specification:
{test_specification}

Create an Inferno test implementation that:
1. Follows the Inferno structure (TestGroup containing one or more tests)
2. Implements the test logic described in the specification
3. Implements test for all components outlined in the test specification- do not develop tests for only one part
4. Makes appropriate FHIR API calls
5. Includes proper assertions to validate the requirements
6. Handles both success and error cases appropriately

Naming conventions:
- Use underscored lowercase names for files (e.g., patient_read_test.rb)
- Use CamelCase for class names (e.g., PatientReadTest)
- Class names should end with 'Test' or 'Group'
- Give each test a unique ID that's descriptive and related to the requirement

The test should be comprehensive but focused on exactly what's described in the specification.
Include proper documentation in the code and follow Inferno best practices.

Requirement ID: {requirement_id}
Module Name: {module_name}

CRITICAL REQUIREMENTS:
1. INPUTS AND CLIENTS:
   - ALWAYS declare all inputs that a test will use
   - Always use valid input types (see inferno guidance; e.g., text, textarea, radio, checkbox, oauth_credentials)
   - NEVER reference inputs outside the `run` block. All input validation must occur INSIDE the run block

2. MAKING REQUESTS:
   - ALWAYS use the Inferno DSL methods (fhir_read, fhir_search, etc.)
   - NEVER use direct HTTP methods like 'get', 'post'
   - NEVER redefine the 'response' variable

3. HANDLING RESPONSES:
   - ALWAYS use hash syntax: response[:code], response[:body], response[:headers]
   - NEVER use dot notation: response.code, response.body, etc.
   - For header access, iterate through response[:headers]

4. ERROR HANDLING:
   - NEVER use rescue blocks for test failures - use assertions
   - AVOID rescuing StandardError in test implementations

5. REQUEST MANAGEMENT:
   - When using 'uses_request', ensure there is a corresponding 'makes_request'
   - For placeholder tests, use 'skip' instead of 'pass'

6. RESOURCES:
   - ONLY test resources explicitly mentioned in the test specification

7. ID ALIGNMENT:
   - NEVER reference a file by its filename in 'test from:' or 'group from:' statements
   - ALWAYS use the actual ID defined inside the file (e.g., what follows 'id :' in the file)
   - Example: If req_XX_test.rb defines `id :example_text`, use 'group from: :example_text'

When developing the test:

1. Define a TestGroup with a descriptive ID based on the requirement
2. Create individual test cases within the group for each specific aspect to test
3. Include detailed documentation in the description fields
4. Use proper assertions that directly validate the requirement
5. Provide meaningful error and success messages
6. Consider both positive and negative test scenarios
7. Add appropriate inputs for configurable test parameters

All tests should be written in accordance with this guidance on the Inferno domain specific language (note: there are example tests in this guidance for use cases that should NOT be found in the IG you are reviewing. Do not use those use cases to develop tests for this IG- only use the test structure and example use of the Inferno dsl as context to inform your approach):
{dsl_guidance}

Follow this pattern for the TestGroup structure:
```ruby
module {module_name}
  class YourTestGroup < Inferno::TestGroup
    id :your_unique_id
    title 'Clear Requirement Title'
    description %(
      Detailed description of what this test validates, including:
      - The specific requirement being tested
      - How the test works
      - What conformance is being verified
    )
    
    # Tests go here
  end
end
```
   
Return only the Ruby code for the test implementation, with no additional explanation.
