module SampleErrorKit
  class SampleErrorSuite < Inferno::TestSuite
    id :sample_error_suite
    title 'Sample Suite - Corrected'
    description 'This suite demonstrates common Inferno errors, now corrected.'

    # Declare input used by the fhir_client block
    input :fhir_server_url,
          title: 'FHIR Server Base URL',
          description: 'The base URL of the FHIR server to be tested.'
    # Optional: Declare access_token if it were to be used by fhir_client
    # input :access_token, title: 'OAuth Access Token', optional: true

    fhir_client do
      url :fhir_server_url
      # Example if using a bearer token:
      # bearer_token :access_token
    end

    group do
      id :group_corrected
      title 'Group With Corrections'
      # FIX: 'links' property removed from TestGroup as it's only allowed in TestSuite.

      test do
        id :test_with_input_and_fhir_corrections
        title 'Test with Corrected Input and FHIR Usage'
        # FIX: Input type 'string' changed to 'text'.
        input :patient_identifier, title: 'Patient Identifier', type: 'text'
        # Optional: if a custom header was truly needed for a specific request:
        # input :custom_api_key, title: 'Custom API Key', optional: true

        run do
          # FIX: Manual FHIR client creation and direct HTTP GET removed.
          # Using Inferno's fhir_search DSL method instead.
          # The fhir_client defined at the suite level is automatically used.

          # Example of adding a custom header to a specific request, if needed:
          # search_headers = {}
          # search_headers['X-Custom-API-Key'] = custom_api_key if custom_api_key.present?

          fhir_search(:patient, params: { identifier: patient_identifier }) #, headers: search_headers (if custom headers were needed)

          # FIX: 'response' variable is not redefined. Assertions use the implicit 'response'.
          assert_response_status(200)
          assert_resource_type(:bundle) # fhir_search returns a Bundle

          # Example of checking if any patient was found
          assert resource.entry.any? { |e| e.resource.is_a?(FHIR::Patient) },
                 "No Patient resources found for identifier: #{patient_identifier}"

          # FIX: Dot notation for response access removed. Using hash syntax.
          # Example: checking a response header (if relevant)
          # content_type_header = response[:headers].find { |h| h.name.downcase == 'content-type' }
          # assert content_type_header&.value&.include?('application/fhir+json'),
          #        "Response Content-Type should be 'application/fhir+json'."

          # FIX: Rescue StandardError block removed. Assertions handle test failures.
          # If a specific condition needs to lead to a 'skip' or 'omit', use skip_if/omit_if.
          # Example: skip_if patient_identifier == 'skip_case', 'Skipping for specific identifier.'
        end
      end

      test do
        id :maker_test
        title 'Test that makes a request'
        input :patient_id_for_read, title: 'Patient ID for Read', type: 'text'
        makes_request :made_patient_read

        run do
          fhir_read(:patient, patient_id_for_read, name: :made_patient_read)
          assert_response_status(200)
          assert_resource_type(:patient)
          assert resource.id == patient_id_for_read,
                 "Requested resource with id #{patient_id_for_read}, but received resource with id #{resource.id}"
        end
      end

      test do
        id :test_with_corrected_request_usage
        title 'Test with Corrected Request Usage'
        # FIX: 'uses_request' now refers to a request name defined by 'makes_request' in a preceding test.
        uses_request :made_patient_read
        input :expected_patient_id, title: 'Expected Patient ID (should match from read)', type: 'text'

        run do
          # The 'response' and 'resource' here are from the request named :made_patient_read
          assert_response_status(200) # From the used request
          assert_resource_type(:patient) # From the used request

          assert resource.is_a?(FHIR::Patient), "Expected a Patient resource from the used request."
          assert resource.id == expected_patient_id,
                 "Patient ID from used request ('#{resource.id}') does not match expected ID ('#{expected_patient_id}')."
        end
      end
    end

    # FIX: Removed 'group from: :my_awesome_tests_file_rb' which was an invalid filename-based ID reference.
    # If referencing an external group, it would be:
    # group from: :actual_id_of_external_group
    # (Assuming ActualIdOfExternalGroup is defined with 'id :actual_id_of_external_group' elsewhere and loaded)
  end
end