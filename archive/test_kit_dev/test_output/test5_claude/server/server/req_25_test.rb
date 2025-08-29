module Test5_claude
  class ReadInteractionSupportGroup < Inferno::TestGroup
    id :read_interaction_support_group
    title 'REQ-25: Support for read interaction'
    description %(
      Verify that the Plan Net server supports the read interaction for each 
      resource type and profile as required.

      For each resource type and profile, a Plan Net server SHALL support the read 
      interaction.
    )

    RESOURCE_TYPES = [
      'Organization', 
      'Location',
      'Practitioner',
      'PractitionerRole',
      'HealthcareService',
      'Network',
      'Endpoint'
    ]

    RESOURCE_TYPES.each do |resource_type|
      test do
        id "read_#{resource_type.downcase}"
        title "Server supports read interaction for #{resource_type}"
        description "Verify that the server properly supports reading a #{resource_type} resource by id"
        
        input :resource_id, 
              title: "#{resource_type} ID",
              description: "ID of an existing #{resource_type} resource on the server"

        run do
          fhir_operation = fhir_read(resource_type.to_sym, resource_id)

          assert_response_status(200)
          
          resource = fhir_operation.resource
          assert_resource_type(resource_type)
          assert resource.id == resource_id, "Expected #{resource_type} id to be #{resource_id} but found #{resource.id}"
          
          assert_valid_resource
          
          # Test 404 for non-existent resource
          fhir_read(resource_type.to_sym, 'NONEXISTENT')
          assert_response_status(404)
        end
      end
    end

    test do
      id :read_invalid_resource_type
      title 'Server returns error for invalid resource type'
      description 'Verify server returns appropriate error for read attempt with invalid resource type'

      run do
        fhir_read(:InvalidResourceType, 'test-id')
        assert_response_status([400, 404])
      end
    end

  end
end