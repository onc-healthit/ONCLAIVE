# frozen_string_literal: true

# This example consolidates groups into one file for brevity.
# In a real Test Kit, groups are typically in separate files under a `lib/<test_kit_name>/` directory.

module MyTestKit
  # Example TestGroup for Patient resource tests
  class PatientGroup < Inferno::TestGroup
    id :patient_tests_group # Actual ID to be referenced by 'group from:'
    title 'Patient Resource Tests'
    description 'Tests for the FHIR Patient resource, demonstrating correct practices.'

    # Group-level input, inherited by tests in this group unless overridden
    input :patient_id,
          title: 'Patient ID for Group Tests',
          description: 'The ID of the patient to be used in this group of tests.',
          type: :text # Valid input type: 'text'

    test do
      id :patient_read_test
      title 'Read Patient Resource'
      description 'Verify that a Patient resource can be read using its ID.'
      # This test inherits 'patient_id' from the group.
      # It also implicitly uses 'server_url' and 'access_token' from the TestSuite for fhir_read.

      # 'makes_request' allows this request's details to be used by subsequent tests via 'uses_request'.
      makes_request :patient_read_operation

      run do
        # Correct: Using Inferno DSL for FHIR read operation.
        # 'patient_id' is resolved from the declared inputs.
        fhir_read(:patient, patient_id, name: :patient_read_operation)

        # Correct: Using hash syntax for response access (e.g., response[:status]).
        assert response[:status] == 200, "Expected HTTP 200 OK, but received #{response[:status]}"
        # 'resource' is automatically populated with the FHIR resource from the response body.
        assert resource.is_a?(FHIR::Patient), "Expected FHIR::Patient resource, but received #{resource.class}"
        assert resource.id == patient_id, "Requested resource with ID '#{patient_id}', but received resource with ID '#{resource.id}'"

        # Correct: Assertions are used for verifying conditions, not exceptions.
      end
    end

    test do
      id :patient_validation_test
      title 'Validate Patient Resource'
      description 'Verify that the fetched Patient resource is valid FHIR and conforms to a profile.'
      # This test also inherits 'patient_id'.

      # Correct: 'uses_request' references a request made by a previous test.
      # The 'response' and 'resource' for this test will be from the 'patient_read_operation' request.
      uses_request :patient_read_operation

      run do
        assert_response_status(200) # Verifies the status from the used request.
        assert_resource_type(:patient) # Verifies the resource type from the used request.

        # Correct: Using built-in assertion for FHIR resource validation.
        # No 'rescue StandardError' blocks should be used for error handling in tests.
        assert_valid_resource(profile_url: 'http://hl7.org/fhir/StructureDefinition/Patient')

        pass 'Patient resource is valid.'
      end
    end
  end

  # Example TestGroup for CapabilityStatement tests
  class CapabilityStatementGroup < Inferno::TestGroup
    id :capability_statement_group # Actual ID for 'group from:'
    title 'Capability Statement Tests'
    description 'Tests related to the server CapabilityStatement.'

    test do
      id :fetch_and_validate_capability_statement
      title 'Fetch and Validate Server CapabilityStatement'
      description 'Verify that the server provides a valid CapabilityStatement at the /metadata endpoint.'
      # Inputs 'server_url' and 'access_token' are declared at TestSuite level and available here.

      run do
        # Correct: Using Inferno DSL for fetching CapabilityStatement.
        # Not using direct HTTP 'get' or manual FHIR client 'get' methods.
        fhir_get_capability_statement

        assert_response_status(200)
        assert_resource_type(:capability_statement)
        assert_valid_resource # Validates against base FHIR specification.

        # Correct: Accessing response headers using response[:headers] and iterating.
        # Avoid patterns like response.headers['some-header'].
        content_type_header = response[:headers].find { |h| h[:name].downcase == 'content-type' }
        assert content_type_header.present? && content_type_header[:value].include?('application/fhir+json'),
               "CapabilityStatement Content-Type should include 'application/fhir+json'."

        # The 'response' variable is automatically created by Inferno and should NEVER be redefined by test logic.
        pass 'CapabilityStatement fetched and validated successfully.'
      end
    end
  end

  # Main TestSuite definition
  class MyCorrectedSuite < Inferno::TestSuite
    id :my_corrected_suite
    title 'Corrected Inferno Test Suite Example'
    description 'A suite demonstrating corrected common issues and best practices as per guidelines.'

    # Correct: 'links' property can ONLY be used in a TestSuite.
    links [
      {
        label: 'Relevant Implementation Guide',
        url: 'http://example.com/ig/documentation'
      },
      {
        label: 'FHIR Specification R4',
        url: 'http://hl7.org/fhir/R4'
      }
    ]

    # Correct: Inputs declared at TestSuite level are available to all child groups and tests.
    # Ensure all used inputs like 'server_url' and 'access_token' are explicitly declared.
    input :server_url,
          title: 'FHIR Server Base URL',
          description: 'The URL of the FHIR server (e.g., https://fhir.example.com/r4).',
          type: :text # Valid input type. Others: textarea, radio, checkbox, oauth_credentials.

    input :access_token,
          title: 'OAuth Access Token',
          description: 'Bearer token for servers requiring OAuth2 authentication.',
          type: :text,
          optional: true # Marks this input as optional.

    # Correct: FHIR client is configured using the Inferno DSL 'fhir_client' block.
    # Never create FHIR clients manually with 'FHIR::Client.new()'.
    fhir_client do
      url :server_url
      bearer_token :access_token
      # Do not use non-existent methods like 'use_additional_headers='.
      # Custom headers are typically added per-request if needed via options in fhir_* methods.
    end

    # Correct: Use 'group from:' for TestGroup objects, referencing the group's defined 'id'.
    # Ensure referenced IDs match those defined in the respective group files/classes.
    # Do not reference filename-based IDs (e.g., :capability_group_file).
    group from: :capability_statement_group # References ID from CapabilityStatementGroup class.

    group from: :patient_tests_group # References ID from PatientGroup class.

    # Note on 'test from:':
    # To include an individual test (e.g., if CapabilityStatementGroup had a test with id :specific_cap_test),
    # you would use:
    #   test from: :specific_cap_test
    # This is for individual Test objects, not TestGroup objects.

    # Note on Resource Testing:
    # This suite is structured to test CapabilityStatement and Patient resources.
    # Only test resources specified in the test plan. Do not add tests for resources
    # not mentioned or out of scope for the specific testing scenario.
  end
end