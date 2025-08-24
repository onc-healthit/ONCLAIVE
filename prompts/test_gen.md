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
1. MODUlE AND CLASS NAMING:
   - Use module {module_name}, NOT numeric modules like "module 70000"
   - Use proper Ruby class names (CamelCase)
   - Module name must start with uppercase letter

2. INPUTS AND CLIENTS:
   - DO NOT declare URL inputs in TestGroups- they inherit from the parent TestSuite
   - DO NOT define fhir_client blocks in TestGroups unless you need different credentials
   - ALWAYS declare all OTHER inputs that a test will use (excluding URL which comes from parent)
   - Always use valid input types (see inferno guidance; e.g., text, textarea, radio, checkbox, oauth_credentials)
   - NEVER reference inputs outside the `run` block. All input validation must occur INSIDE the run block

3. FHIR CLIENT INHERITANCE:
   - TestGroups automatically inherit the fhir_client configuration from their parent TestSuite
   - Only define a new fhir_client in a TestGRoup if you need different authentication/credentials
   - The URL input is already available from the parent TestSuite

4. MAKING REQUESTS:
   - ALWAYS use the Inferno DSL methods (fhir_read, fhir_search, etc.)
   - NEVER use direct HTTP methods like 'get', 'post'
   - NEVER redefine the 'response' variable

5. HANDLING RESPONSES:
   - ALWAYS use hash syntax: response[:code], response[:body], response[:headers]
   - NEVER use dot notation: response.code, response.body, etc.
   - For header access, iterate through response[:headers]

6. ERROR HANDLING:
   - NEVER use rescue blocks for test failures - use assertions
   - AVOID rescuing StandardError in test implementations

7. REQUEST MANAGEMENT:
   - When using 'uses_request', ensure there is a corresponding 'makes_request'
   - For placeholder tests, use 'skip' instead of 'pass'

8. RESOURCES:
   - ONLY test resources explicitly mentioned in the test specification

9. ID ALIGNMENT:
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
    
    # DO NOT define fhir_client here - it inherits from TestSuite
    # DO NOT declare :url input here - it comes from parent
    
    # Only declare inputs specific to this test group:
    input :specific_parameter,
          title: 'Parameter Title',
          description: 'Parameter description'
    
    # Tests go here
  end
end
```
   
Return only the Ruby code for the test implementation, with no additional explanation.
