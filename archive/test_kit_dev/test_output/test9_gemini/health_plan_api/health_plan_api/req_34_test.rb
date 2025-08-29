module ExampleTestKit
  class ExampleTestSuite < Inferno::TestSuite
    id :example_test_suite
    title 'Example Inferno Test Suite'
    description 'A suite demonstrating common Inferno patterns and fixes for common issues.'

    # Property usage:
    # - 'links' property can ONLY be used in a TestSuite
    links [
      {
        label: 'Example Implementation Guide',
        url: 'http://example.com/ig'
      }
    ]

    # Input declarations:
    # - Ensure each test explicitly declares all inputs it uses with the `input` method
    # - Don't use server_url or access_token without declaring them as inputs
    # - Use valid input types
    input :server_url,
          title: 'FHIR Server Base URL',
          description: 'The URL of the FHIR server to be tested.',
          type: :text # Valid input type: text

    input :access_token,
          title: 'OAuth Access Token',
          description: 'Bearer token for OAuth 2.0 protected endpoints.',
          type: :text, # Valid input type: text (or :oauth_credentials for complex object)
          optional: true

    # FHIR client usage:
    # - Always use the Inferno DSL's 'fhir_client' block
    # - Never create FHIR clients manually with 'FHIR::Client.new()'
    # - Do not use non-existent methods like 'use_additional_headers='
    fhir_client do
      url :server_url
      bearer_token :access_token # Correctly uses declared input
    end

    # Example of a group defined inline
    group do
      id :basic_operations_group
      title 'Basic FHIR Operations'
      description 'Tests for basic FHIR interactions like read and search.'

      # Property usage:
      # - 'links' property CANNOT be used in TestGroups (it's only for TestSuite)

      test do
        id :patient_read_test
        title 'Read Patient Resource'
        description 'Verify that a Patient resource can be read from the server.'

        # Input declarations:
        # - Ensure each test explicitly declares all inputs it uses
        input :patient_id,
              title: 'Patient ID',
              description: 'The ID of the patient to read.',
              type: :text # Valid input type

        # Request management:
        # - When using 'uses_request', ensure a previous test has declared 'makes_request'
        makes_request :patient_read_request # Named request

        run do
          # HTTP and FHIR requests:
          # - Never use direct HTTP methods like 'get', 'post', etc. - use the Inferno DSL methods instead
          # - Use proper FHIR client methods - 'fhir_get_capability_statement' instead of 'get capability_statement_url'
          # - NEVER redefine the 'response' variable which is automatically created by Inferno
          fhir_read(:patient, patient_id, name: :patient_read_request)

          # Response handling:
          # - Use hash syntax for response access: response[:status], response[:body], etc.
          # - Don't use dot notation like response.code or response.body
          assert_response_status(200) # Preferred way to check status

          # Example of accessing response body if needed (resource is preferred for FHIR objects)
          # parsed_body = JSON.parse(response[:body]) rescue nil
          # assert parsed_body&.[]('resourceType') == 'Patient', "Response body is not a Patient resource"

          assert_resource_type(:patient) # Preferred way to check resource type

          # Example of accessing headers:
          # - For headers, use response[:headers] and iterate through the array of headers
          # - Fix patterns like 'response.headers['www-authenticate']' to use proper header access
          # response[:headers] is an array of hashes like [{name: 'Content-Type', value: 'application/fhir+json'}]
          content_type_header = response[:headers].find { |h| h[:name].casecmp('content-type').zero? }
          assert content_type_header, "Content-Type header not found."
          assert content_type_header[:value].include?('application/fhir+json'),
                 "Expected Content-Type header to include 'application/fhir+json', but found '#{content_type_header[:value]}'"

          # Assertion patterns:
          # - Use assertions instead of exceptions for failures
          # - Do not use rescue blocks for error handling in tests
          # - Never rescue StandardError in test implementations
          assert resource.id == patient_id,
                 "Requested resource with id '#{patient_id}', but received resource with id '#{resource.id}'"
        end
      end

      test do
        id :patient_search_test
        title 'Search Patient Resource by Name'
        description 'Verify that Patient resources can be searched by name.'

        input :search_name,
              title: 'Patient Name for Search',
              description: 'A name to use for searching Patient resources.',
              type: :text

        makes_request :patient_search_request

        run do
          fhir_search(:patient, params: { name: search_name }, name: :patient_search_request)

          assert_response_status(200)
          assert_resource_type(:bundle) # Search typically returns a Bundle

          assert resource.entry.present?, "Search for Patient with name '#{search_name}' returned no results."
        end
      end
    end

    # ID references:
    # - Ensure test/group IDs match those in the referenced files
    # - Don't reference filename-based IDs, but use the actual defined ID in the referenced file
    # - Example: If 'req_XX_test.rb' contains a group with ID `:example_group_id_from_file`,
    #   reference that ID, not `:req_XX_test`

    # Property usage:
    # - Check proper use of 'test from:' vs 'group from:':
    #   * Use 'test from:' only for individual Test objects
    #   * Use 'group from:' for TestGroup objects

    # --- Example of referencing from other files (these files would need to exist) ---
    # Assume 'lib/example_test_kit/another_group.rb' defines:
    # class AnotherGroup < Inferno::TestGroup
    #   id :actual_group_id_from_file
    #   # ...
    # end
    # group from: :actual_group_id_from_file # Correct: 'group from:' for TestGroup object

    # Assume 'lib/example_test_kit/utility_test_definitions.rb' defines:
    # class ASingleTest < Inferno::Test
    #   id :actual_test_id_from_file
    #   # ...
    # end
    # test from: :actual_test_id_from_file # Correct: 'test from:' for Test object
    # --- End of example references ---

    group do
      id :request_dependency_group
      title 'Request Dependency Demonstration'
      description 'Tests demonstrating `uses_request`.'

      test do
        id :use_patient_read_data
        title 'Validate Patient Resource from Previous Read Test'
        description 'Uses the request made in the patient_read_test (named :patient_read_request).'

        # Request management:
        # - When using 'uses_request', ensure a previous test has declared 'makes_request' with the same name
        uses_request :patient_read_request # References the named request from 'patient_read_test'

        run do
          # 'request' variable now holds the details of the 'patient_read_request'
          assert request, "The 'patient_read_request' was not found. Ensure the 'Read Patient Resource' test ran and made the request."
          assert request[:response][:status] == 200,
                 "Expected status 200 for the 'patient_read_request', but got #{request[:response][:status]}"

          # 'resource' is automatically populated from the 'patient_read_request' response
          assert resource.is_a?(FHIR::Patient),
                 "Expected resource from 'patient_read_request' to be FHIR::Patient, but got #{resource.class}"

          # Example of validating the resource (could be against a profile)
          assert_valid_resource # Validates against base FHIR specification
          # To validate against a specific profile:
          # assert_valid_resource(profile_url: 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient')
        end
      end
    end

    # Resources:
    # - Only test resources specified in the test plan - don't add tests for resources not mentioned
    # (This principle is applied by designing tests around the plan; e.g., only Patient tests here if only Patient is in scope)
  end
end