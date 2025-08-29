module Test6_claude
  class VreadInteractionGroup < Inferno::TestGroup
    id :plan_net_vread_interaction
    title 'Version Read (vread) Interaction Support'
    description %(
      Verify that the server supports the vread interaction for each resource type
      and profile as specified in REQ-26.
      
      For each resource type and profile, a Plan Net server SHOULD support the 
      vread interaction to retrieve specific versions of resources.
    )

    test do
      id :vread_organization_test
      title 'Server supports Organization vread interaction'
      description %(
        Verify that the server properly supports the vread interaction for
        Organization resources by:
        1. Creating a new Organization
        2. Updating it to create a new version
        3. Reading specific versions using vread
      )
      
      input :bearer_token
      makes_request :vread

      run do
        skip_if bearer_token.blank?, 'Bearer token is required for vread tests'

        fhir_client.set_bearer_token(bearer_token)

        # Create initial organization
        org = FHIR::Organization.new(
          name: 'Test Organization',
          active: true
        )
        create_response = fhir_client.create(org)
        assert_response_status(create_response, 201)
        org_id = create_response.resource.id
        
        # Update to create new version
        org.name = 'Updated Organization'
        update_response = fhir_client.update(org, org_id)
        assert_response_status(update_response, 200)

        # Get version history
        history_response = fhir_client.history(versioned_resource_class: FHIR::Organization, id: org_id)
        assert_response_status(history_response, 200)
        versions = history_response.resource.entry

        assert versions.length >= 2, 'Expected at least 2 versions of resource'
        first_version = versions.first.resource.meta.versionId

        # Perform vread for specific version
        vread_response = fhir_client.vread(versioned_resource_class: FHIR::Organization, 
                                         id: org_id, 
                                         version_id: first_version)
        
        assert_response_status(vread_response, 200)
        assert_resource_type(vread_response.resource, 'Organization')
        assert vread_response.resource.meta.versionId == first_version, 
               "Expected version #{first_version} but got #{vread_response.resource.meta.versionId}"
        assert vread_response.resource.name == 'Test Organization',
               'Expected original resource name in first version'

        # Clean up
        fhir_client.destroy(FHIR::Organization, org_id)
      end
    end

    test do
      id :vread_error_test  
      title 'Server returns appropriate errors for invalid vread requests'
      description %(
        Verify that the server returns appropriate error responses when:
        - Requesting non-existent resource versions
        - Using invalid version ids
      )

      input :bearer_token
      makes_request :vread

      run do
        skip_if bearer_token.blank?, 'Bearer token is required for vread tests'

        fhir_client.set_bearer_token(bearer_token)

        # Test non-existent resource
        bad_response = fhir_client.vread(versioned_resource_class: FHIR::Organization, 
                                       id: 'non-existent', 
                                       version_id: '1')
        
        assert [404, 410].include?(bad_response.response[:code].to_i),
               'Expected 404 Not Found or 410 Gone for non-existent resource version'

        # Test invalid version id
        invalid_response = fhir_client.vread(versioned_resource_class: FHIR::Organization,
                                           id: 'test',
                                           version_id: 'invalid')
        
        assert_response_status(invalid_response, 404)
      end
    end
  end
end