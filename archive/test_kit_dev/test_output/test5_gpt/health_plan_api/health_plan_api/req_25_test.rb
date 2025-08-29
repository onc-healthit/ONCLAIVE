module Test5Gpt
  class ReadInteractionTestGroup < Inferno::TestGroup
    id :req_25_read_interaction
    title 'REQ-25: Support for Read Interaction'
    description %(
      Verify that the Plan Net server supports the read interaction for each resource type and profile.
      This includes reading resources by their ID and ensuring the server responds correctly.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :patient_read_test
      title 'Server supports Patient read interaction'
      description 'Verify that the server supports reading a Patient resource by its id.'
      input :patient_id, title: 'Patient ID', description: 'ID of the Patient resource to read'

      run do
        skip_if patient_id.blank?, 'Patient ID is not provided'

        fhir_read(:patient, patient_id)
        
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource

        patient = resource
        assert patient.id == patient_id, "Expected Patient id to be #{patient_id} but was #{patient.id}"
      end
    end

    # Additional tests for other resource types can be added here
  end
end