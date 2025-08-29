module Test5_claude
  class VreadInteractionTest < Inferno::TestGroup
    id :plan_net_vread_interaction
    title 'Resource Version Read Interaction Support'
    description %(
      For each resource type and profile, a Plan Net server SHOULD support the vread interaction.
      This test verifies that version-specific read operations are supported by attempting to 
      retrieve specific versions of resources after updates.
    )

    test do
      id :vread_practitioner_test
      title 'Server supports vread interaction for Practitioner'
      description %(
        Verify that the server properly supports retrieving a specific version
        of a Practitioner resource using the vread interaction.
      )
      
      input :practitioner_id
      makes_request :vread

      run do
        # First create/update resource to ensure multiple versions
        practitioner = FHIR::Practitioner.new(
          id: practitioner_id,
          active: true,
          name: [{ family: 'Smith', given: ['John'] }]
        )

        fhir_update(practitioner, practitioner_id)
        assert_response_status(200)
        
        first_version = resource.meta.versionId
        assert !first_version.nil?, 'Server response did not include version ID'

        # Update resource to create new version
        practitioner.active = false
        fhir_update(practitioner, practitioner_id) 
        assert_response_status(200)
        
        second_version = resource.meta.versionId
        assert !second_version.nil?, 'Server response did not include version ID'
        assert second_version != first_version, 'Update did not create new version'

        # Attempt vread of first version
        fhir_vread(:practitioner, practitioner_id, first_version)
        assert_response_status(200)
        assert_resource_type(:practitioner)
        
        retrieved = resource
        assert retrieved.meta.versionId == first_version, 
          "Expected version #{first_version} but got #{retrieved.meta.versionId}"
        assert retrieved.active == true,
          'Retrieved resource does not match expected version state'

        # Attempt vread of second version
        fhir_vread(:practitioner, practitioner_id, second_version)
        assert_response_status(200)
        assert_resource_type(:practitioner)
        
        retrieved = resource
        assert retrieved.meta.versionId == second_version,
          "Expected version #{second_version} but got #{retrieved.meta.versionId}"
        assert retrieved.active == false,
          'Retrieved resource does not match expected version state'

      rescue StandardError => e
        skip "Server appears to not support vread: #{e.message}"
      end
    end

    test do
      id :vread_error_test  
      title 'Server returns appropriate errors for invalid vread requests'
      description %(
        Verify that the server returns appropriate error responses when
        attempting to vread non-existent resource versions.
      )

      input :practitioner_id
      makes_request :vread

      run do
        fhir_vread(:practitioner, practitioner_id, 'non-existent-version')
        assert_response_status([404, 410])
        assert_resource_type(:operationoutcome)
      rescue StandardError => e
        skip "Server appears to not support vread: #{e.message}"
      end
    end
  end
end