module Test6_claude
  class ReadInteractionSupportGroup < Inferno::TestGroup
    id :read_interaction_support
    title 'REQ-25: Support for Read Interaction'
    description %(
      Verify that the Plan Net server supports the read interaction for each resource type and profile.
      
      The server SHALL support reading resources by their logical ID for all supported resource types.
      
      Conformance: SHALL support read operations
    )

    RESOURCE_TYPES = [
      'Organization', 
      'OrganizationAffiliation',
      'Location',
      'HealthcareService',
      'Practitioner',
      'PractitionerRole',
      'Network',
      'Endpoint'
    ]

    RESOURCE_TYPES.each do |resource_type|
      test do
        id "read_#{resource_type.downcase}"
        title "Server supports read interaction for #{resource_type}"
        description "Verify that the server properly supports reading a #{resource_type} resource by its id"
        
        input :resource_id,
              title: "#{resource_type} ID",
              description: "The logical ID of an existing #{resource_type} resource on the server"

        run do
          fhir_operation = fhir_read(resource_type.to_sym, resource_id)

          assert_response_status(200)
          assert_resource_type(resource_type)
          assert_valid_resource

          resource = fhir_operation.resource
          assert resource.id == resource_id, 
                 "Expected #{resource_type} id to be #{resource_id} but found #{resource.id}"

          # Test Not Found scenario
          fhir_read(resource_type.to_sym, 'INVALID_ID')
          assert_response_status(404)
        end
      end
    end
  end
end