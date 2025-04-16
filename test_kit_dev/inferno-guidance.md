# LLM Guidance Document for Developing Inferno Tests

## Introduction to Inferno Testing Framework

Inferno is a specialized testing framework for FHIR implementations that uses a structured, hierarchical approach to organize tests. Understanding the core components and patterns is essential for generating effective tests.

## Core Inferno Test Structure

### Test Hierarchy
- **TestSuite**: Top-level container that houses multiple TestGroups
- **TestGroup**: Logical grouping of related tests; can contain other TestGroups or individual Tests
- **Test**: Individual test case containing a `run` block that defines test execution logic

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

### 4. Making FHIR Requests
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

- **Assigning Results**:
```ruby
run do
  skip_if condition, 'Skip message'
  omit_if condition, 'Omit message'
  pass 'Pass message'
end
```

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

## Best Practices for Inferno Test Development

1. **Follow Progressive Testing Pattern**:
   - Start with basic connectivity tests
   - Test resource retrieval before complex operations
   - Test search parameters individually before combinations

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

Test Plan Requirement:
```
REQ-25: Support for read interaction
Description: "For each resource type and profile, a Plan Net server SHALL support the read interaction."
```

Inferno Test:
```ruby
module PlanNetTestKit
  class ReadInteractionTest < Inferno::TestGroup
    id :plan_net_read_interaction
    title 'Read Interaction Support'
    description 'Verify that the server supports the read interaction for each resource type and profile.'
    
    # Test for Patient resource read
    test do
      id :patient_read_test
      title 'Server supports Patient read interaction'
      description 'Verify that the server supports reading a Patient resource by its id.'
      input :patient_id
      
      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource
        
        patient = resource
        assert patient.id == patient_id, "Expected Patient id to be #{patient_id} but was #{patient.id}"
      end
    end
    
    # Additional tests for other resource types...
  end
end
```