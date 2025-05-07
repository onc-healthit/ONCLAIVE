Convert the following FHIR test specification into executable Ruby code using the Inferno testing framework.

Test Specification:
{test_specification}

Create an Inferno test implementation that:
1. Follows the Inferno structure (TestGroup containing one or more tests)
2. Implements the test logic described in the specification
3. Makes appropriate FHIR API calls
4. Includes proper assertions to validate the requirements
5. Handles both success and error cases appropriately

Naming conventions:
- Use underscored lowercase names for files (e.g., patient_read_test.rb)
- Use CamelCase for class names (e.g., PatientReadTest)
- Class names should end with 'Test' or 'Group'
- Give each test a unique ID that's descriptive and related to the requirement

The test should be comprehensive but focused on exactly what's described in the specification.
Include proper documentation in the code and follow Inferno best practices.

Requirement ID: {requirement_id}
Module Name: {module_name}

The test should also be developed in accordance with this guidance on Inferno test development:
{inferno_guidance}

When developing the test:

1. Define a TestGroup with a descriptive ID based on the requirement
2. Create individual test cases within the group for each specific aspect to test
3. Include detailed documentation in the description fields
4. Use proper assertions that directly validate the requirement
5. Provide meaningful error and success messages
6. Consider both positive and negative test scenarios
7. Add appropriate inputs for configurable test parameters

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
