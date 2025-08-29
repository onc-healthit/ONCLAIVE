module Test5_claude
  class VreadInteractionTest < Inferno::TestGroup
    id :plan_net_vread_interaction
    title 'Version Read (vread) Interaction Support'
    description %(
      For each resource type and profile, a Plan Net server SHOULD support the vread interaction.
      
      This test verifies that the server properly supports retrieving specific versions of 
      resources using the vread operation.
    )

    test do
      id :vread_patient_test
      title 'Server supports Patient vread interaction'
      description %(
        Verify that the server supports retrieving a specific version of a Patient resource
        using the vread interaction.
      )
      
      input :patient_id
      input :patient_version_id

      run do
        skip_if patient_version_id.nil?, 'No Patient version ID provided'

        fhir_vread(:patient, patient_id, patient_version_id)

        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource

        patient = resource
        assert patient.id == patient_id, 
          "Expected Patient id to be #{patient_id} but was #{patient.id}"
        assert patient.meta.versionId == patient_version_id,
          "Expected version #{patient_version_id} but got #{patient.meta.versionId}"
      end
    end

    test do
      id :vread_not_found_test  
      title 'Server returns appropriate error for non-existent version'
      description %(
        Verify that the server returns a 404 Not Found when attempting to vread 
        a non-existent resource version.
      )

      input :patient_id
      
      run do
        # Attempt to read non-existent version
        fhir_vread(:patient, patient_id, 'non-existent-version')
        
        assert_response_status([404, 410])
        assert_resource_type(:operationoutcome)
      end
    end

    test do
      id :vread_validation_test
      title 'Server validates vread parameters'
      description %(
        Verify that the server properly validates the parameters for vread operations
        and returns appropriate errors for invalid requests.
      )

      run do
        # Test with invalid resource type
        fhir_vread(:invalid_resource, 'id', '1')
        assert_response_status(400)
        assert_resource_type(:operationoutcome)

        # Test with invalid version format
        fhir_vread(:patient, 'test-patient', 'invalid-version-format')
        assert_response_status(400)
        assert_resource_type(:operationoutcome)
      end
    end
  end
end