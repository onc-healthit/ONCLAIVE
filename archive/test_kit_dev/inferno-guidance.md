# LLM Guidance Document for Developing Inferno Tests

## Introduction to Inferno Testing Framework

Inferno is a specialized testing framework for FHIR implementations that uses a structured, hierarchical approach to organize tests. Understanding the core components and patterns is essential for generating effective tests.

The Inferno DSL is a Domain Specific Language (DSL) that test writers use to define the tests in an Inferno Test Kit. The DSL provides built-in functionality that is useful in testing FHIR APIs, such as a FHIR client and built-in assertion libraries. Tests should be written using the Inferno DSL.

An Inferno Test Kit is a distributable set of tests and tools built and packaged using Inferno to help testers evaluate the conformance of a system to base FHIR specification requirements, relevant FHIR Implementation Guides, and any additional requirements. Test Kits are primarily composed of one or more Test Suites, but may include other tools such as FHIR resource validators or reference implementations.

An Inferno Test Group is a set of related tests within a Test Suite. Test authors can use groups to run subsets of tests without needing to run an entire Test Suite, or for skipping optional test functionality.

An Inferno Test Suite is an executable set of tests provided within an Inferno Test Kit that allows testers to evaluate the conformance of a system. They can import tests from other Test Kits. Each Test Suite also defines how to interpret failures at the test level and in aggregate. For example, a Test Suite may define that a conformant system will pass all provided tests, or that the system may fail some tests.

Inferno Test Kits are valid Ruby gems, which are packaged applications or libraries written in Ruby, allowing them to be easily added to other Ruby applications or libraries, such as another Inferno Test Kit.

Inferno Test Kits are organized like Ruby gems to enable them to be easily distributed. Tests must live in the lib folder. The lib folder should contain only one file, which is the main entrypoint for your Test Suite. The name of this file should be your_test_kit_name.rb, and this is what other Test Kits will require in order to load your tests. All other test files should live in a subdirectory in lib, and the convention is to have this subdirectory have the same name as the single file in lib, minus the extension. 


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