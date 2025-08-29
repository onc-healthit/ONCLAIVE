require 'securerandom'

module Test7Gemini
  class Req07MustSupportProcessingGroup < Inferno::TestGroup
    id :req_07_must_support_processing
    title 'REQ-07: Must Support Elements Processing'
    description %(
      **Requirement REQ-07**: "Application Actor SHALL process resource instances
      containing Must Support data elements without errors or application failure."

      This test group interprets the "Application Actor" as the FHIR server
      when it is receiving and processing data (e.g., via a `CREATE` or `UPDATE`
      operation).

      The tests verify that the server can successfully process a resource instance
      that contains populated data elements, representative of 'Must Support'
      elements, without errors or application failure. This is assessed by
      attempting to create a new resource (e.g., a Patient) with several common
      elements populated and expecting a successful HTTP response (e.g., 201 Created).
    )
    short_description 'Verify server processing of resources with Must Support elements.'

    # Test 1: Create a resource with representative Must Support elements
    test do
      id :req_07_create_resource_with_must_support_elements
      title 'Server successfully creates a resource containing representative Must Support elements'
      description %(
        This test sends a `POST` request to the server to create a new Patient
        resource. The Patient resource is populated with common elements such as
        `identifier`, `name`, `gender`, and `birthDate`. These elements serve as
        representatives for 'Must Support' data elements that an Application Actor
        (the server, in this context) might receive.

        The test asserts that the server responds with an HTTP `201 Created` status,
        indicating successful processing and creation of the resource. It also
        verifies that the returned resource is a valid FHIR Patient resource.
        Successful completion of this test demonstrates that the server can process
        the resource instance without errors or application failure as per REQ-07.
      )

      # This request will be named so it can be referenced if needed, e.g., for debugging.
      makes_request :create_patient_for_must_support_test

      # Outputs for potential use in subsequent tests or for cleanup.
      output :created_patient_id_for_must_support_test, :created_patient_resource_for_must_support_test

      run do
        # Define a Patient resource. We populate elements that are commonly
        # marked as "Must Support" in various Implementation Guides.
        # A unique identifier is used for each test run to prevent collisions
        # and aid in debugging if cleanup steps fail.
        unique_identifier_value = "ms-test-#{SecureRandom.uuid}"
        patient_to_create = FHIR::Patient.new(
          identifier: [{
            system: 'http://inferno.healthit.gov/test/identifier',
            value: unique_identifier_value
          }],
          name: [{
            family: 'MustSupportTest',
            given: ['Patient', SecureRandom.hex(4)] # Add some randomness to given name
          }],
          gender: 'other', # FHIR R4 values: male, female, other, unknown
          birthDate: '1970-01-01'
        )

        # Perform the FHIR create operation
        fhir_create(patient_to_create, name: :create_patient_for_must_support_test)

        # Assertions for successful creation and processing
        assert_response_status(201)
        assert_resource_type(:patient)

        # Validate that the resource returned by the server is a valid FHIR resource
        # according to the base FHIR specification.
        assert_valid_resource(resource: resource, profile_url: nil)

        assert resource.id.present?, 'Server created Patient but the response did not include an ID.'

        # Store the ID and the full resource for cleanup or other potential uses
        output created_patient_id_for_must_support_test: resource.id
        output created_patient_resource_for_must_support_test: resource.to_json

        info "Successfully created Patient/#{resource.id} (Identifier: #{unique_identifier_value}) " \
             "containing representative Must Support elements. Server processed the request without error " \
             "and returned a valid resource, satisfying REQ-07."
      end
    end

    # Test 2: Cleanup the created resource
    test do
      id :req_07_cleanup_created_resource_with_must_support_elements
      title 'Clean up Patient resource created for Must Support test'
      description %(
        This test attempts to delete the Patient resource that was created in the
        previous test (`req_07_create_resource_with_must_support_elements`).
        This is a cleanup step to remove test data from the server.

        The test will be skipped if no Patient ID was output from the creation test,
        for example, if the creation failed.
      )
      # This test is important for test hygiene. It can be made optional if desired,
      # but is generally good practice to include and require.
      # It implicitly depends on the output of the previous test.

      input :created_patient_id_for_must_support_test,
            title: 'ID of Patient created for Must Support test',
            description: 'The ID of the Patient resource created in the previous test, which will be deleted.',
            optional: true # Marking as optional in case creation failed and ID is not available.

      makes_request :delete_patient_for_must_support_test

      run do
        patient_id_to_delete = created_patient_id_for_must_support_test

        skip_if patient_id_to_delete.blank?,
                "No Patient ID provided from the creation test (created_patient_id_for_must_support_test was blank). " \
                "Skipping cleanup."

        # Perform the FHIR delete operation
        fhir_delete(:patient, patient_id_to_delete, name: :delete_patient_for_must_support_test)

        # A successful DELETE can result in HTTP 200 (OK, often with an OperationOutcome),
        # HTTP 204 (No Content), or HTTP 410 (Gone) if already deleted by other means.
        # We will assert for 200 or 204 as common success codes.
        # If the server returns 404 (Not Found), it could mean it was already deleted,
        # which is acceptable for a cleanup step. For stricter check, one might only allow 200/204.
        assert_response_status([200, 204, 404, 410])

        case response[:status]
        when 200, 204
          info "Successfully deleted Patient/#{patient_id_to_delete} or it was already gone. Response status: #{response[:status]}."
        when 404, 410
          info "Patient/#{patient_id_to_delete} was not found or already gone. Assuming cleanup is effective. Response status: #{response[:status]}."
        else
          # This case should be caught by assert_response_status, but good for info.
          info "Attempted to delete Patient/#{patient_id_to_delete}. Response status: #{response[:status]}."
        end
      end
    end
  end
end