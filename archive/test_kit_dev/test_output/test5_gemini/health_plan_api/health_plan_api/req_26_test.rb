module Test5_gemini
  class VreadInteractionTest < Inferno::TestGroup
    id :req_26_vread_interaction
    title 'REQ-26: Support for vread interaction'
    description %(
      For each resource type and profile, a Plan Net server SHOULD support the vread interaction.
    )

    test do
      id :patient_vread_test
      title 'Server supports Patient vread interaction'
      description %(
        Verify that the server supports reading a Patient resource using the vread interaction.
      )
      input :patient_id, :version_id
      
      run do
        fhir_vread(:patient, patient_id, version_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource

        patient = resource
        assert patient.id == patient_id, "Expected Patient id to be #{patient_id} but was #{patient.id}"
        assert patient.meta&.versionId == version_id, "Expected version id to be #{version_id} but was #{patient.meta&.versionId}"
      end
    end

    # Additional tests for other resource types...
  end
end
