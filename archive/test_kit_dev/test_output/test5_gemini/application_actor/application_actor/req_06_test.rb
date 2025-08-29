module Test5_gemini
  class MustSupportElementsTest < Inferno::TestGroup
    id :req_06_must_support_elements
    title 'REQ-06: Client Handling of Must Support Data Elements'
    description %(
      Verify that the application can process resources containing Must Support data elements without errors.
    )

    test do
      id :patient_must_support_test
      title 'Application processes Patient resources with Must Support elements'
      description %(
        Create a Patient resource with all Must Support elements populated, then read the resource.
      )

      run do
        # Construct a Patient resource with all Must Support elements populated
        patient = FHIR::Patient.new(
          # ... (Populate all Must Support elements for Patient)
        )

        # Create the Patient resource on the server
        created_patient = fhir_create(patient)
        assert_response_status(201)

        # Read the created Patient resource
        read_patient = fhir_read(:patient, created_patient.id)
        assert_response_status(200)

        # Assert that the read resource matches the created resource
        assert_equal created_patient.resource.to_json, read_patient.resource.to_json
      end
    end

    # Add similar tests for other relevant resources (e.g., Observation, Encounter, etc.)
  end
end
