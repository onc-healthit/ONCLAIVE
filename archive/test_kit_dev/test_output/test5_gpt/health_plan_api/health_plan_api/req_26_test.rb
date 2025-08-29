module Test5Gpt
  class VreadInteractionTestGroup < Inferno::TestGroup
    id :req_26_vread_interaction
    title 'Vread Interaction Support'
    description %(
      Verify that the Plan Net server supports the vread interaction for each resource type and profile.
      This test checks that the server can retrieve a specific version of a resource.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :vread_patient_test
      title 'Server supports Patient vread interaction'
      description 'Verify that the server supports retrieving a specific version of a Patient resource by its id and version id.'
      input :patient_id, :patient_version_id

      run do
        skip_if patient_id.nil? || patient_version_id.nil?, 'Patient ID and version ID must be provided to test vread interaction.'

        response = fhir_vread(:patient, patient_id, patient_version_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource

        patient = resource
        assert patient.id == patient_id, "Expected Patient id to be #{patient_id} but was #{patient.id}"
        assert patient.meta.versionId == patient_version_id, "Expected Patient version id to be #{patient_version_id} but was #{patient.meta.versionId}"
      end
    end

    # Additional tests for other resource types and profiles can be added here.
  end
end