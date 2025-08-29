module Test5_claude
  class ResourceReadSupportGroup < Inferno::TestGroup
    id :resource_read_support
    title 'Resource Read Support Tests'
    description %(
      Verify that the Plan Net server supports the read interaction for each resource 
      type and profile as required by REQ-25.

      For each resource type and profile, a Plan Net server SHALL support the read interaction.
    )

    RESOURCE_TYPES = [
      'Organization',
      'OrganizationAffiliation', 
      'Location',
      'HealthcareService',
      'Practitioner',
      'PractitionerRole',
      'InsurancePlan',
      'Network'
    ]

    RESOURCE_TYPES.each do |resource_type|
      test do
        id "read_#{resource_type.downcase}"
        title "Server supports #{resource_type} read interaction"
        description %(
          Verify that the server properly supports reading a #{resource_type} 
          resource by its id.
        )
        
        input :resource_id, 
              title: "#{resource_type} ID",
              description: "ID of an existing #{resource_type} resource on the server"

        run do
          fhir_read(resource_type.to_sym, resource_id)

          assert_response_status(200)
          assert_resource_type(resource_type)
          assert_valid_resource

          resource = resource_from_response
          assert resource.id == resource_id, 
                 "Expected #{resource_type} id to be #{resource_id} but was #{resource.id}"

          # Verify we can parse the resource
          assert !resource.nil?, "Server returned nil #{resource_type} resource"
        rescue Inferno::AssertionException => e
          fail("Server does not support read interaction for #{resource_type}: #{e.message}")
        end
      end
    end

    test do
      id :read_invalid_id
      title 'Server returns 404 for non-existent resource read'
      description %(
        Verify that the server returns HTTP 404 when reading a resource that does not exist.
      )

      run do
        invalid_id = 'INVALID_RESOURCE_ID_12345'
        fhir_read(:Organization, invalid_id)
        
        assert_response_status(404)
        assert_resource_type('OperationOutcome')
      end
    end
  end
end