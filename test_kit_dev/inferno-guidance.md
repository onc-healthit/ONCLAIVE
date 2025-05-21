# LLM Guidance Document for Developing Inferno Tests

## Introduction to Inferno Testing Framework

Inferno is a specialized testing framework for FHIR implementations that uses a structured, hierarchical approach to organize tests. Understanding the core components and patterns is essential for generating effective tests.

The Inferno DSL is a Domain Specific Language (DSL) that test writers use to define the tests in an Inferno Test Kit. The DSL provides built-in functionality that is useful in testing FHIR APIs, such as a FHIR client and built-in assertion libraries. Tests should be written using the Inferno DSL.

An Inferno Test Kit is a distributable set of tests and tools built and packaged using Inferno to help testers evaluate the conformance of a system to base FHIR specification requirements, relevant FHIR Implementation Guides, and any additional requirements. Test Kits are primarily composed of one or more Test Suites, but may include other tools such as FHIR resource validators or reference implementations.

An Inferno Test Group is a set of related tests within a Test Suite. Test authors can use groups to run subsets of tests without needing to run an entire Test Suite, or for skipping optional test functionality.

An Inferno Test Suite is an executable set of tests provided within an Inferno Test Kit that allows testers to evaluate the conformance of a system. They can import tests from other Test Kits. Each Test Suite also defines how to interpret failures at the test level and in aggregate. For example, a Test Suite may define that a conformant system will pass all provided tests, or that the system may fail some tests.

Inferno Test Kits are valid Ruby gems, which are packaged applications or libraries written in Ruby, allowing them to be easily added to other Ruby applications or libraries, such as another Inferno Test Kit.

Inferno Test Kits are organized like Ruby gems to enable them to be easily distributed. Tests must live in the lib folder. The lib folder should contain only one file, which is the main entrypoint for your Test Suite. The name of this file should be your_test_kit_name.rb, and this is what other Test Kits will require in order to load your tests. All other test files should live in a subdirectory in lib, and the convention is to have this subdirectory have the same name as the single file in lib, minus the extension. 

## Core Inferno Test Structure

### Test Hierarchy
- **TestSuite**: Top-level container that houses multiple TestGroup classes
- **TestGroup**: Logical grouping of related tests; can contain other TestGroup or individual Test classes
- **Test**: Individual test case containing a `run` block that defines test execution logic

For example, a simple US Core test suite might look like this:

US Core (TestSuite)
- US Core Patient Group (TestGroup)
  - Server supports Patient Read Interaction (Test)
  - Server supports Patient Search by id (Test)
-  US Core Condition Group (TestGroup)
  - Server supports Condition Read Interaction (Test)
  - Server supports Condition Search by Patient (Test)

### Basic Structure Example
```ruby
module YourTestKit
  class YourTestSuite < Inferno::TestSuite
    group do
      title 'Group Title'
      description 'Detailed description of this group of tests'
      
      test do
        title 'Test Title'
        description 'Description of what this test verifies'
        input :parameter_name
        
        run do
          # Test logic goes here
          assert condition, 'Failure message'
        end
      end
    end
  end
end
```

## Key Concepts for Inferno Test Development

### 1. Organizing Tests
- Create external test group files for better organization
- Give tests and groups unique identifiers with the `id` property
- Use `from` property to reference tests and groups defined elsewhere

Example:
```ruby
# In main file
group from: :specific_test_group

# In separate file
class SpecificTestGroup < Inferno::TestGroup
  id :specific_test_group
  title 'Specific Tests'
  
  test from: :specific_test
end
```
When developing complex test suites, consider organizing tests in a hierarchical structure with external files for better maintainability:
- Create separate files for test groups to keep code modular
- Use unique identifiers with the id property to reference tests and groups
- Leverage the from property to include tests defined in other files

Example:
```ruby
# In main file
group from: :capability_statement_test_group

# In separate file
class CapabilityStatementTestGroup < Inferno::TestGroup
  id :capability_statement_test_group
  title 'Capability Statement Tests'
  
  test from: :capability_statement_validation
end
```

Here is an example suite.rb file from the Inferno test template. 
```ruby
require_relative 'metadata'
require_relative 'patient_group'

module InfernoTemplate
  class Suite < Inferno::TestSuite
    id :inferno_template
    title 'Inferno Template Test Suite'
    description 'Inferno template test suite.'

    # These inputs will be available to all tests in this suite
    input :url,
          title: 'FHIR Server Base Url'

    input :credentials,
          title: 'OAuth Credentials',
          type: :oauth_credentials,
          optional: true

    # All FHIR requests in this suite will use this FHIR client
    fhir_client do
      url :url
      oauth_credentials :credentials
    end

    # All FHIR validation requests will use this FHIR validator
    fhir_resource_validator do
      # igs 'identifier#version' # Use this method for published IGs/versions
      # igs 'igs/filename.tgz'   # Use this otherwise

      exclude_message do |message|
        message.message.match?(/\A\S+: \S+: URL value '.*' does not resolve/)
      end
    end

    # Tests and TestGroups can be defined inline
    group do
      id :capability_statement
      title 'Capability Statement'
      description 'Verify that the server has a CapabilityStatement'

      test do
        id :capability_statement_read
        title 'Read CapabilityStatement'
        description 'Read CapabilityStatement from /metadata endpoint'

        run do
          fhir_get_capability_statement

          assert_response_status(200)
          assert_resource_type(:capability_statement)
        end
      end
    end

    # Tests and TestGroups can be written in separate files and then included
    # using their id
    group from: :patient_group
  end
end
```

### 2. Test and Group Properties
- **Required Properties**:
  - `title`: Human-readable title displayed in UI
  - `run` block: For tests, contains actual test logic
- **Common Properties**:
  - `id`: Unique identifier for referencing
  - `description`: Markdown-supported detailed description
  - `optional`/`required`: Mark test/group as optional or required
  - `short_title`: Abbreviated title for UI display

### 3. Inputs and Outputs
Inputs and outputs provide a structured mechanism for passing information between tests. Consider these strategies:
- Use appropriate input types (text, textarea, radio, checkbox, oauth_credentials) based on the data being collected
- Set default values where appropriate to minimize user input
- Lock inputs when you want to force values from previous outputs
- Use the input_order method to control the display sequence of inputs in the UI

The input method defines an input. input can take several arguments, but only the identifier is required:
- identifier - (required) a name for this input. The input value is available in the run block using this name.
- title: - a title which is displayed in the UI.
- description: - a description which is displayed in the UI.
- type: - controls the type of HTML input element used in the UI. Currently there are 5 possible values:
  - 'text' - (default) a regular input field.
  - 'textarea' - for a text area input field.
  - 'radio' - for a radio button singular selection field.
  - 'checkbox - for a checkbox field. In tests, a checkbox input is represented as an array of the selected values.
  - 'oauth_credentials' - a complex type for storing OAuth2 credentials. When used by a FHIR client, the access token will automatically refresh if possible.
- default: - default value for the input.
- optional: - (default: false) whether the input is optional.
- options: - possible input option formats based on input type.
  - list_options: - options for input formats that require a list of possible values (radio and checkbox). An array of hashes with label and value keys.
  - locked: - (default: false) whether the user can alter the input’s value. Locking an input can force it to use a value from a previous test’s output, or the default value.

- **Inputs**: Define parameters required to run a test
```ruby
test do
  input :server_url, 
        title: 'FHIR Server URL',
        description: 'The base URL for the FHIR server'
  # Multiple inputs can be defined in a single call
  input :patient_id, :token
end
```

- **Outputs**: Store values for use in subsequent tests
```ruby
test do
  output :patient_resource
  
  run do
    output patient_resource: fhir_read(:patient, '123').resource.to_json
  end
end
```
For complex data passing between tests, implement JSON serialization:
```ruby
test do
  output :capability_statement_json
  
  run do
    fhir_get_capability_statement
    output capability_statement_json: resource.to_json
  end
end

test do
  input :capability_statement_json
  
  run do
    capability_statement = JSON.parse(capability_statement_json)
    # Now analyze the capability statement
  end
end
```

### 4. Making FHIR Requests
Inferno provides support for making FHIR requests as well as generic HTTP requests. The following methods are currently available for making FHIR requests:
- fhir_create
- fhir_delete
- fhir_get_capability_statement
- fhir_history
- fhir_operation
- fhir_patch
- fhir_read
- fhir_search
- fhir_transaction
- fhir_update
- fhir_vread

After making a FHIR or HTTP request, information about it is made available via several methods:
- request - returns a Request object which contains all of the information about the request and the response.
- response - returns a Hash containing the status, headers, and body of the response.
- resource - returns the response body as a FHIR model.

Best practices for making requests:
1) Establish consistent patterns for making FHIR requests:
- Set up FHIR clients at the group level to be inherited by all tests
- Use input variables for server URLs and bearer tokens to avoid hardcoding
- Name requests that need to be referenced in later tests
- Use tags to organize collections of related requests
- Implement proper error handling for FHIR responses
- When using 'uses_request', ensure a previous test has declared 'makes_request' with the same name
  and has actually made a FHIR request
- Never redefine the 'response' variable which is automatically created by the Inferno DSL.
- Use the proper Inferno DSL methods for FHIR operations (fhir_search, fhir_read, etc.) rather than
  calling methods directly on a client object

2) When testing multiple endpoints or complex workflows:
- Name different FHIR clients when testing multiple servers
- Use OAuth credentials with refresh token support for extended tests
- Tag related requests to group them for later analysis
- Access previous request data using the requests collection after loading with load_tagged_requests

- **FHIR Client Setup**:
```ruby
group do
  fhir_client do
    url :server_url
    bearer_token :access_token
  end
end
```

- **Common FHIR Operations**:
```ruby
run do
  # Read a resource
  fhir_read(:patient, patient_id)
  
  # Search for resources
  fhir_search(:observation, params: { patient: patient_id })
  
  # Create a resource
  fhir_create(FHIR::Patient.new(name: [{given: ['Test'], family: 'Patient'}]))
  
  # Update a resource
  fhir_update(patient_resource)
  
  # Delete a resource
  fhir_delete(:patient, patient_id)
end
```

### 5. Assertions and Test Results
- **Basic Assertions**:
```ruby
run do
  assert condition, 'Failure message'
  assert_response_status(200)
  assert_resource_type(:patient)
  assert_valid_resource
end
```

- **Result Types**:
  - `pass`: Test verified correct behavior
  - `fail`: Test verified incorrect behavior
  - `skip`: Test could not verify behavior
  - `omit`: Test not needed based on implementation
  - `error`: Unexpected error in test execution
  - `wait`: Test waiting to receive an incoming request

- **Assigning Results**:
```ruby
run do
  skip_if condition, 'Skip message'
  omit_if condition, 'Omit message'
  pass 'Pass message'
end
```

Structure assertions to provide clear feedback and actionable information:
- Use descriptive messages in assertions to explain why a test failed
- Include relevant context in error messages to aid debugging
- Add info and warning messages for important notes that don't constitute failures
- Group related assertions together for logical test flow

Handle different result types appropriately:
- Use pass when behavior is verified as correct
- Use fail when behavior is verified as incorrect
- Use skip when behavior cannot be verified (but may be correct)
- Use omit when a test is not applicable based on implementation choices
- Use conditional skipping/omitting with skip_if and omit_if to create adaptive tests
- Tests that are just placeholders should use 'skip' instead of 'pass' with an appropriate message
  indicating why the test is skipped or what needs to be implemented.

### 6. FHIR Resource Validation
```ruby
run do
  fhir_read(:patient, patient_id)
  
  # Validate against base FHIR
  assert_valid_resource
  
  # Validate against a specific profile
  assert_valid_resource(profile_url: 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient')
end
```
Implement thorough FHIR resource validation:
- Configure validators to use specific implementation guide packages
- Validate resources against both base FHIR definitions and specific profiles
- Filter validation messages to focus on relevant issues
- Add custom validation logic with perform_additional_validation

Example of custom validation:
```ruby
rubyfhir_resource_validator do
  perform_additional_validation do |resource, profile_url|
    if resource.is_a?(FHIR::Patient) && resource.name.empty?
      { type: 'error', message: 'Patient resource must have at least one name element' }
    end
  end
end
```
## Additional Considerations
Add specific guidance against using rescue blocks:
- Do not use rescue blocks for error handling in tests. Use assertions to verify expected behavior.
- Never rescue StandardError in test implementations as this interferes with Inferno's result tracking.
- Be more explicit about resource limitations:
- Only test resources explicitly mentioned in the test plan.
- Always access response properties using hash syntax: response[:code], response[:body], etc.
- Never try to access response.code, response.body, or other dot notation on the response object.

## Best Practices for Inferno Test Development
1. **Follow Progressive Testing Pattern**:
   - Start with basic connectivity and server readiness tests
   - Test resource retrieval operations before complex operations
   - Test search parameters individually before parameter combinations
   - Validate resource content against required profiles
   - Test edge cases and error conditions

2. **Create Modular, Reusable Tests**:
   - Break complex requirements into smaller, focused tests
   - Use external test definitions for reusable components

3. **Handle Edge Cases**:
   - Test both positive and negative scenarios
   - Include validation for required error responses

4. **Provide Clear Feedback**:
   - Use descriptive assertions that explain why a test failed
   - Include relevant context in error messages

5. **Effective Test Organization**:
   - Group related tests logically
   - Sequence tests to build on previous results

## Converting Test Plans to Inferno Tests

When converting a test plan to Inferno tests:

1. **Analyze the requirement** for testability and complexity
2. **Identify required inputs** based on the test specification
3. **Determine necessary FHIR operations** for the test
4. **Create appropriate assertions** based on validation criteria
5. **Structure tests hierarchically** according to the requirement grouping
6. **Implement the test logic** in the run block according to the test implementation strategy

## Example Translating a Test Plan to Inferno Test
Example conversion from a requirement to test, from the Inferno template:

Test Plan Requirement:
```
REQ-XX: Verify that Patient resources can be read from the server
Description: "Server returns requested Patient resource from the Patient read interaction."
```

Inferno Test:
```ruby
module InfernoTemplate
  class PatientGroup < Inferno::TestGroup
    title 'Patient Tests'
    description 'Verify that the server makes Patient resources available'
    id :patient_group

    test do
      title 'Server returns requested Patient resource from the Patient read interaction'
      description %(
        Verify that Patient resources can be read from the server.
      )

      input :patient_id,
            title: 'Patient ID'

      # Named requests can be used by other tests
      makes_request :patient

      run do
        fhir_read(:patient, patient_id, name: :patient)

        assert_response_status(200)
        assert_resource_type(:patient)
        assert resource.id == patient_id,
               "Requested resource with id #{patient_id}, received resource with id #{resource.id}"
      end
    end

    test do
      title 'Patient resource is valid'
      description %(
        Verify that the Patient resource returned from the server is a valid FHIR resource.
      )
      # This test will use the response from the :patient request in the
      # previous test
      uses_request :patient

      run do
        assert_resource_type(:patient)
        assert_valid_resource
      end
    end
  end
end
```

## Documentation and Descriptive Elements
Provide comprehensive documentation within tests:
- Use descriptive titles and short_titles for clear UI display
- Add detailed descriptions with Markdown formatting to explain test purpose and context
- Use input_instructions to provide guidance on required inputs

Make tests user-friendly with clear guidance:
- Set up contextual input instructions to guide users
- Create logical test groupings with meaningful titles
- Use suite_summary to provide an overview of the test suite
- Add external links to relevant documentation

## Additional Examples of Tests for the US Core Implementation Guide

```ruby
# Example for US Core Patient Must Support Elements testing
test do
  id :us_core_patient_must_support_elements
  title 'Patient must support required elements'
  description %(
    US Core Patient Profile requires that the server must be capable of providing the following elements:
    - name (at least one with both family and given parts)
    - gender
    - birthDate
    - address (at least one with city, state, and postal code)
    
    This test verifies that these elements are present in the returned Patient resource.
  )
  input :patient_id
  
  run do
    fhir_read(:patient, patient_id)
    assert_response_status(200)
    assert_resource_type(:patient)
    
    # Check must support elements are present
    assert resource.name.present? && 
           resource.name.any? { |name| name.family.present? && name.given.present? },
           'Patient.name with family and given parts is required'
    
    assert resource.gender.present?, 'Patient.gender is required'
    assert resource.birthDate.present?, 'Patient.birthDate is required'
    
    assert resource.address.present? && 
           resource.address.any? { |addr| addr.city.present? && 
                                          addr.state.present? && 
                                          addr.postalCode.present? },
           'Patient.address with city, state, and postal code is required'
  end
end
```

```ruby
# Example on testing against a server's capability statement
test do
  id :verify_capability_statement_patient_interaction
  title 'CapabilityStatement declares support for Patient read operation'
  description %(
    The server's CapabilityStatement must declare support for the read operation
    on Patient resources as required by the US Core Implementation Guide.
  )
  
  run do
    fhir_get_capability_statement
    assert_response_status(200)
    assert_resource_type(:capability_statement)
    
    patient_resource = resource.rest&.first&.resource&.find { |r| r.type == 'Patient' }
    assert patient_resource.present?, 'CapabilityStatement does not declare support for Patient resources'
    
    read_interaction = patient_resource.interaction&.find { |i| i.code == 'read' }
    assert read_interaction.present?, 'CapabilityStatement does not declare support for Patient read interaction'
  end
end
```

```ruby
# Example of test data generation and cleanup
group do
  title 'Test Data Management'
  
  test do
    title 'Create test data for US Core Patient tests'
    id :create_test_data
    
    run do
      # Create a test patient
      test_patient = FHIR::Patient.new(
        name: [{ given: ['Test'], family: 'InfernoTestPatient' }],
        gender: 'male',
        birthDate: '1970-01-01',
        identifier: [{ system: 'http://example.org/fhir/identifier/mrn', value: "TEST-#{Time.now.to_i}" }]
      )
      
      fhir_create(test_patient)
      assert_response_status(201)
      output test_patient_id: resource.id
      
      # Tag this test data for cleanup later
      output test_resources: [{ resource_type: 'Patient', id: resource.id }].to_json
    end
  end
  
  # More test data creation here...
  
  test do
    title 'Clean up test data'
    id :cleanup_test_data
    description 'Remove test data created during this test run'
    input :test_resources
    
    run do
      resources = JSON.parse(test_resources)
      resources.each do |resource_info|
        fhir_delete(resource_info['resource_type'], resource_info['id'])
        info "Deleted #{resource_info['resource_type']}/#{resource_info['id']}"
      end
    end
  end
end
```

```ruby
# Example for complex search parameter testing
test do
  id :us_core_patient_name_search
  title 'Server returns valid results for Patient search by name'
  description %(
    A server SHALL support searching by name on the Patient resource.
    This test verifies that the server is capable of searching for patients by name
    using both exact and partial matching strategies.
  )
  input :patient_name
  
  run do
    # Test exact match
    fhir_search(:patient, params: { name: patient_name })
    assert_response_status(200)
    assert_resource_type(:bundle)
    
    assert resource.entry.present?, "No Patient resources returned for exact name search: #{patient_name}"
    
    # Test partial match
    partial_name = patient_name.split(/\s+/).first
    fhir_search(:patient, params: { name: partial_name })
    assert_response_status(200)
    
    assert resource.entry.present?, "No Patient resources returned for partial name search: #{partial_name}"
    
    # Test combined parameters
    fhir_search(:patient, params: { name: patient_name, _count: 5 })
    assert_response_status(200)
    assert resource.entry.length <= 5, "Server did not honor _count parameter"
  end
end
```

```ruby
# Example of test dependencies
test do
  title 'Create a test Patient'
  id :create_test_patient
  
  run do
    test_patient = FHIR::Patient.new(
      name: [{ given: ['Test'], family: 'Patient' }],
      gender: 'male',
      birthDate: '1970-01-01'
    )
    
    fhir_create(test_patient)
    assert_response_status(201)
    
    # Store the ID for use in subsequent tests
    output patient_id: resource.id
  end
end

test do
  title 'Read the created Patient'
  id :read_test_patient
  
  # This test depends on the previous test succeeding
  depends_on :create_test_patient
  input :patient_id
  
  run do
    fhir_read(:patient, patient_id)
    assert_response_status(200)
    assert_resource_type(:patient)
  end
end
```