# Guidance Document for Developing Inferno Tests using Inferno Domain Specific Language

## Introduction to Inferno Domain Specific Language

The Inferno DSL is a Domain Specific Language (DSL) that test writers use to define the tests in an Inferno Test Kit. The DSL provides built-in functionality that is useful in testing FHIR APIs, such as a FHIR client and built-in assertion libraries. Tests should be written using the Inferno DSL.

The Inferno DSL operates within specialized execution contexts using `instance_eval`. This means you must use framework-specific methods and patterns rather than standard Ruby object-oriented programming approaches. Do not use generic HTTP clients, standard Ruby error handling patterns, or assume normal Ruby method resolution.

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
- US Core Condition Group (TestGroup)
- Server supports Condition Read Interaction (Test)
- Server supports Condition Search by Patient (Test)

### Basic Structure Example

```ruby
module YourTestKit
  class YourTestSuite < Inferno::TestSuite
    id :your_test_suite  # MANDATORY - always include this
    title 'Your Test Suite Title'
    description 'Detailed description'

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

Create external test group files for better organization when developing complex test suites. Give tests and groups unique identifiers with the `id` property and use the `from` property to reference tests and groups defined elsewhere. This approach keeps code modular and maintainable.

Mandatory Configuration: Every TestSuite MUST include an `id` property. Failure to include this will cause initialization errors. Always include `id :unique_identifier` as the first line in your TestSuite class definition.

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

Organizing multiple requirements: Keep related tests in a single cohesive TestSuite rather than creating multiple unrelated TestSuites. Group requirements logically within the same TestSuite using TestGroups.

Here is an example suite.rb file from the Inferno test template:

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

In addition to using the `from` property when referencing tests and groups defined in other files, you must include a `require_relative` statement at the top of the file that references the relative path of the file that contains the test or group that you wish to include. Here is an example of a Test Kit directory structure:

```bash
lib
├── us_core_test_kit.rb
├── us_core_test_kit
│   ├── us_core_patient_group.rb
│   ├── us_core_condition_group.rb
```

If you want to include the `us_core_patient_group` and `us_core_condition_group` in our main `lib/us_core_test_kit.rb` file, you must specify the correct file path.

Incorrect:

```ruby
# File: lib/us_core_test_kit.rb
require_relative 'us_core_patient_group' # Incorrect file path
require_relative 'us_core_condition_group' # Incorrect file path
```

Correct:

```ruby
require_relative 'us_core_test_kit/us_core_patient_group' # Correct file path
require_relative 'us_core_test_kit/us_core_condition_group' # Correct file path
```

### 2. Test and Group Properties

Use the required and common properties appropriately:

- **Required Properties**:
  - `title`: Human-readable title displayed in UI
  - `run` block: For tests, contains actual test logic
- **Common Properties**:
  - `description`: Markdown-supported detailed description
  - `optional`/`required`: Mark test/group as optional or required
  - `short_title`: Abbreviated title for UI display

### 3. Inputs and Outputs

Inputs and outputs provide a structured mechanism for passing information between tests. Consider these strategies when implementing input and output management:

Use appropriate input types (text, textarea, radio, checkbox, oauth_credentials) based on the data being collected. Set default values where appropriate to minimize user input. Lock inputs when you want to force values from previous outputs. Use the input_order method to control the display sequence of inputs in the UI. Ensure inputs are declared at the appropriate level (TestSuite, TestGroup, or Test) and that FHIR clients reference the correct input names. Avoid declaring inputs that are not actually used in the test logic.

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
  - locked: - (default: false) whether the user can alter the input's value. Locking an input can force it to use a value from a previous test's output, or the default value.

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

Input validation with `skip_if` MUST occur inside the `run` block, never outside it.

Example:

```ruby
test do
  input :parameter_name

  run do
    skip_if !parameter_name.present?, 'Parameter not provided'
    # test logic here
  end
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

#### FHIR Client Inheritance (CRITICAL)

**TestGroups and Tests automatically inherit FHIR client configuration from their parent TestSuite.** This is a fundamental principle of Inferno test organization.

### DO NOT Repeat Client Configuration

**WRONG - Causes duplicate input prompts:**

```ruby
# TestSuite level
class MyTestSuite < Inferno::TestSuite
  input :url, title: 'FHIR Server URL'
  fhir_client do
    url :url
  end
end

# TestGroup level - WRONG!
class MyTestGroup < Inferno::TestGroup
  input :url, title: 'FHIR Server URL'  # Duplicate input!
  fhir_client do                        # Unnecessary redefinition!
    url :url
  end
end
```

**CORRECT - Single input, inherited by all:**

```ruby
# TestSuite level - Define once
class MyTestSuite < Inferno::TestSuite
  input :url, title: 'FHIR Server URL'
  fhir_client do
    url :url
  end
end

# TestGroup level - Inherits automatically
class MyTestGroup < Inferno::TestGroup
  # No URL input needed - inherits from parent
  # No fhir_client needed - inherits from parent

  input :patient_id,  # Only declare inputs specific to this group
        title: 'Patient ID'
end
```

### When to Define FHIR Client in TestGroup

Only define a new `fhir_client` in a TestGroup when you need:

- Different authentication credentials
- Different base URL
- Different headers or configuration

Example of legitimate TestGroup client override:

```ruby
class SecureTestGroup < Inferno::TestGroup
  input :admin_token, title: 'Admin Access Token'

  # Override client for admin-only tests
  fhir_client do
    url :url  # Still use inherited URL
    bearer_token :admin_token  # But different auth
  end
end
```

### Input Declaration Rules

1. **URL inputs**: Declare ONLY in TestSuite
2. **OAuth credentials**: Declare ONLY in TestSuite unless specific tests need different credentials
3. **Resource IDs**: Declare in TestGroup or Test as needed
4. **Search parameters**: Declare in TestGroup or Test as needed

### Template for Clean Test Organization

```ruby
# Main TestSuite file
class MyTestSuite < Inferno::TestSuite
  id :my_test_suite

  # Shared inputs declared once
  input :url, title: 'FHIR Server URL'
  input :credentials, type: :oauth_credentials, optional: true

  # Shared FHIR client
  fhir_client do
    url :url
    oauth_credentials :credentials
  end

  group from: :patient_tests
  group from: :organization_tests
end

# Individual test group files
class PatientTestGroup < Inferno::TestGroup
  id :patient_tests

  # Only declare inputs specific to patient testing
  input :patient_id, title: 'Patient ID'

  # No fhir_client block needed - inherits from suite
end
```

### 4. Making FHIR Requests

Inferno provides support for making FHIR requests as well as generic HTTP requests. Always use Inferno's FHIR client methods instead of generic HTTP libraries like Net::HTTP or RestClient. The following methods are currently available for making FHIR requests:

- fhir_read(resource_type, id, client: :default, name: nil) - Read operations
- fhir_search(resource_type, params: {}, search_method: :get) - Search operations
- fhir_create(resource, client: :default) - Create new resources
- fhir_update(resource, id, client: :default) - Update existing resources
- fhir_delete(resource_type, id, client: :default) - Delete operations
- fhir_operation(path, body: nil, operation_method: :post) - Custom operations
- fhir_get_capability_statement(client: :default) - Capability statements
- fhir_history
- fhir_patch
- fhir_transaction
- fhir_vread

After making a FHIR or HTTP request, information about it is made available via several methods:

- request - returns a Request object which contains all of the information about the request and the response.
- response - returns a Hash containing the status, headers, and body of the response.
- resource - returns the response body as a FHIR model.

When accessing response data, use object methods like `response[:status]` and `response[:headers]`, not dot notation like `response.status`. For headers, use object methods like `header.name` and `header.value`, not hash-style access like `header[:name]`.

Best practices for making requests:

When accessing response data, use object methods like response[:status] and response[:headers], not dot notation like response.status. For headers, use object methods like header.name and header.value, not hash-style access like header[:name].

Establish consistent patterns for making FHIR requests by setting up FHIR clients at the group level to be inherited by all tests. Use input variables for server URLs and bearer tokens to avoid hardcoding. Name requests that need to be referenced in later tests and use tags to organize collections of related requests. Implement proper error handling for FHIR responses.

When a TestSuite defines a FHIR client, TestGroups and Tests within that suite automatically inherit it. Do not redefine FHIR clients unnecessarily in child groups unless you need different configuration.

When using 'uses_request', ensure a previous test has declared 'makes_request' with the same name and has actually made a FHIR request. Never redefine the 'response' variable which is automatically created by the Inferno DSL. Use the proper Inferno DSL methods for FHIR operations (fhir_search, fhir_read, etc.) rather than calling methods directly on a client object.

When testing multiple endpoints or complex workflows, name different FHIR clients when testing multiple servers, use OAuth credentials with refresh token support for extended tests, tag related requests to group them for later analysis, and access previous request data using the requests collection after loading with load_tagged_requests.

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

**FHIR Resource Type Names**: Use correct FHIR resource type casing. Use `PractitionerRole` or `:practitioner_role`, not `:practitionerrole`. Use `OrganizationAffiliation` or `:organization_affiliation`, not `:organizationaffiliation`.

**FHIR Search Parameters**: Use correct FHIR search parameter names as defined in the FHIR specification and the capability statement. For example, for OrganizationAffiliation searches, use `primary-organization` or `participating-organization`, not `organization`. For chaining parameters, use proper syntax like `primary-organization.name`.

### 5. Assertions and Test Results

Structure assertions to provide clear feedback and actionable information. Use descriptive messages in assertions to explain why a test failed. Include relevant context in error messages to aid debugging. Add info and warning messages for important notes that don't constitute failures. Group related assertions together for logical test flow.

- **Basic Assertions**:

```ruby
run do
  assert condition, 'Failure message'
  assert_response_status(200)
  assert_resource_type(:patient)
  assert_valid_resource
end
```

Use `assert_response_status(200)` instead of manually checking `request[:response][:status] == 200`. Use framework-provided assertion methods rather than generic assertions.

Handle different result types appropriately:

- **Result Types**:
  - `pass`: Test verified correct behavior
  - `fail`: Test verified incorrect behavior
  - `skip`: Test could not verify behavior
  - `omit`: Test not needed based on implementation
  - `error`: Unexpected error in test execution
  - `wait`: Test waiting to receive an incoming request

Use pass when behavior is verified as correct. Use fail when behavior is verified as incorrect. Use skip when behavior cannot be verified (but may be correct). Use omit when a test is not applicable based on implementation choices. Use conditional skipping/omitting with skip_if and omit_if to create adaptive tests. Tests that are just placeholders should use 'skip' instead of 'pass' with an appropriate message indicating why the test is skipped or what needs to be implemented.

- **Assigning Results**:

```ruby
run do
  skip_if condition, 'Skip message'
  omit_if condition, 'Omit message'
  pass 'Pass message'
end
```

### 6. FHIR Resource Validation

Implement thorough FHIR resource validation by configuring validators to use specific implementation guide packages. Validate resources against both base FHIR definitions and specific profiles. Filter validation messages to focus on relevant issues. Add custom validation logic with perform_additional_validation.

```ruby
run do
  fhir_read(:patient, patient_id)

  # Validate against base FHIR
  assert_valid_resource

  # Validate against a specific profile
  assert_valid_resource(profile_url: 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient')
end
```

Example of custom validation:

```ruby
fhir_resource_validator do
  perform_additional_validation do |resource, profile_url|
    if resource.is_a?(FHIR::Patient) && resource.name.empty?
      { type: 'error', message: 'Patient resource must have at least one name element' }
    end
  end
end
```

### 7. DSL Variable Usage

- Variables `request`, `response`, and `resource` only exist within test `run` blocks
  - Helper methods CANNOT directly access these variables
  - If helper methods need these variables, they must be passed as parameters
  - Assertions in helper methods must receive context: assert_response_status(200, request: request, response: response)
  - NEVER define helper methods that use `response`, `request`, or `resource` without parameters

Examples of INCORRECT usage to fix:

Incorrect:

```ruby
def validate_search_results(expected_code)
assert_response_status(200) # response not available here
assert_resource_type(:bundle) # resource not available here
end
```

Correct:

```ruby
def validate_search_results(request, response, resource, expected_code)
assert_response_status(200, request: request, response: response)
assert_resource_type(:bundle, resource: resource)
end
```

Incorrect Calling:

```ruby
validate_search_results(specialty_code)
```

Correct Calling:

```ruby
validate_search_results(request, response, resource, specialty_code)
```

### 8. DSL Method Usage

#### DSL FHIR Methods

It is important to only use Inferno DSL FHIR methods (i.e., `fhir_read`, `fhir_search`etc.) with their named parameters. Parameters with defaults are optional, not required.

`fhir_read` Parameters:

- **resource_type**: String, Symbol, Class
- **id**: String
- **client**: Symbol (defaults to: `:default`)
- **name**: Symbol (defaults to: `nil`)
- **tags**: Array<String> (defaults to: `[]`)

Example:

```ruby
# INCORRECT
fhir_read(resource: resource_type, id: resource_type) # naming of parameters is in correct and not required

# CORRECT
fhir_read(resource_type, resource_id) # simply pass in the parameters
```

`fhir_search` Parameters:

- **resource_type**: String, Symbol, Class (defaults to: `nil`)
- **client**: Symbol (defaults to: `:default`)
- **params**: Hash (defaults to: `{}`)
- **name**: Symbol (defaults to: `nil`)
- **search_method**: Symbol (defaults to: `:get`)
- **tags**: Array<String> (defaults to: `[]`)

Example:

```ruby
# INCORRECT
fhir_search(:Practitioner, params: { name: 'Smith'}, url: base_url) # url is NOT a parameter for fhir_search

# CORRECT
fhir_search(:Practitioner, params: { name: 'Smith' })
```

#### DSL Assertion Methods

`assert_valid_json` Parameters:

- **maybe_json_string**: String
- **message**: String (defaults to: `''`)

```ruby
# CORRECT
# Both of these are correct examples of assert_valid_json
assert_valid_json(must_support_resource_json) # message not passed in, defaults to ''
assert_valid_json(must_support_resource_json, 'Must have valid JSON') # optional message passed in
```

`assert_valid_resource` Parameters:

- **resource**: `FHIR::Model` (defaults to: `self.resource`)
- **profile_url**: String (defaults to: `nil`)
- **validator**: Symbol (defaults to: `:default`)

```ruby
# CORRECT
assert_valid_resource(resource: patient_with_missing_data, profile_url: 'http://hl7.org/fhir/StructureDefinition/Patient')
```

`assert_resource_type` Parameters:

- **resource_type**: String, Symbol, Class
- **resource**: `FHIR::Model` (defaults to: `self.resource`)

```ruby
# CORRECT
# All of these are correct examples of assert_resource_type
assert_resource_type(:capability_statement) # Symbol
assert_resource_type('CapabilityStatement') # String
assert_resource_type(FHIR::CapabilityStatement) # FHIR::Model
```

`assert_response_status` Parameters:

- **status**: Integer, Array<Integer>
- **request**: `Inferno::Entities::Request` (defaults to: `self.request`)
- **response**: Hash (defaults to: `nil`)

```ruby
# INCORRECT
assert_response_ok # Not a method! Use assert_response_status()
assert_response_status(:created) # Incorrect parameter type! Need status code Integer or Array of Integers
assert_response_status(:ok) # Incorrect parameter type! Need status code Integer or Array of Integers

# CORRECT
assert_response_status(200)
assert_response_status(201)
```

## Error Prevention

### Framework-specific methods vs generic Ruby

#### Required Inferno DSL methods

These Inferno-specific methods must be used instead of generic Ruby approaches:

| **Inferno DSL Method**           | **Ruby Alternative (Don't Use)**    |
| -------------------------------- | ----------------------------------- |
| `fhir_read(:patient, id)`        | `Net::HTTP.get(uri)`                |
| `assert_response_status(200)`    | `raise unless response.code == 200` |
| `assert_resource_type(:patient)` | `JSON.parse(body)['resourceType']`  |
| `assert_valid_resource`          | Custom validation logic             |
| `resource.id`                    | `JSON.parse(response)['id']`        |
| `request, response`              | Manual response handling            |

### FHIR client vs generic HTTP

The framework's FHIR client provides automatic resource parsing, validation integration, and request tracking:

```ruby
# CORRECT: Inferno FHIR client
fhir_read(:patient, patient_id)
# Automatically provides: request, response, resource objects

# WRONG: Generic HTTP client
uri = URI("#{base_url}/Patient/#{patient_id}")
response = Net::HTTP.get_response(uri)
patient = JSON.parse(response.body)
```

### Other Errors to Avoid

**Missing Suite ID**: Always include `id :unique_identifier` as the first property in TestSuite definitions. This is mandatory and will cause initialization failures if omitted.

**CodeableConcept Validation**: When validating CodeableConcept fields, validate against the `code` and `system` properties, not the `text` or `display` fields. Search parameters match against code values, not display text.

**Incorrect Response Access Patterns**:

- Use `response[:status]` not `response.status`
- Use `header.name` and `header.value` not `header[:name]` and `header[:value]`
- Use `assert_response_status(200)` not manual status checking

**FHIR Client Inheritance Issues**:
When a TestSuite defines a FHIR client, TestGroups and Tests within that suite automatically inherit it. Do not redefine FHIR clients unnecessarily in child groups unless you need different configuration.

- Define FHIR clients at the TestSuite level when possible
- Do not redefine clients in TestGroups unless configuration differs
- Ensure input names match between client configuration and input declarations

**Resource Type Naming**:

- Use proper FHIR resource names: `PractitionerRole` not `Practitionerrole`
- Use correct search parameters: `primary-organization` not `organization` for OrganizationAffiliation

**Referencing Declaring Inputs**:

- An `input` is required to have an `identifier` so that the input's value can be access via the `identifier` in the `run` block:

```ruby
test do
  input :url,
        title: 'FHIR Server Url',
        description: 'The base url for the FHIR server'

  run do
    # The input's identifier is :url, so its value is available via `url`
    assert url.start_with?('https'), 'The server must support https'
  end
end
```

**Incorrect Use of Assertion Message**:
The `assert condition, 'Failure message'` logic pattern within tests can only be used with `assert`, not the DSL assertion methods like `assert_response_status`, and `assert_resource_type`.

Example:

```ruby
# INCORRECT
assert_response_status([200, 404]), 'Service should accept anonymous requests (200) or return not found (404) but not require authentication'

# CORRECT
assert_response_status([200, 404])
```

Note that the DSL assertion method `assert_valid_json` does have an optional parameter for message; however, the message must be passed in as a parameter to the method, not outside.

Example:

```ruby
# INCORRECT
assert_valid_json(response[:body]), "Response body is not valid JSON for #{resource_type} read"

# CORRECT
assert_valid_json(response[:body])
```

## Additional Considerations

Do not use rescue blocks for error handling in tests. Use assertions to verify expected behavior. Never rescue StandardError in test implementations as this interferes with Inferno's result tracking.

Only test resources explicitly mentioned in the test plan. Always access response properties using hash syntax: response[:code], response[:body], etc. Never try to access response.code, response.body, or other dot notation on the response object.

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
