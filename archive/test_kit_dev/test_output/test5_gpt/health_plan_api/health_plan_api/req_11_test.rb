module Test5Gpt
  class RestfulBehaviorTestGroup < Inferno::TestGroup
    id :req_11_restful_behavior
    title 'RESTful Behavior Implementation'
    description %(
      This test group verifies that the Health Plan API implements the RESTful behavior
      according to the FHIR specification as required by REQ-11.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :req_11_restful_behavior_test
      title 'Verify RESTful behavior implementation'
      description %(
        This test checks that the Health Plan API supports basic RESTful operations
        such as read, search, create, update, and delete for a given resource type.
      )
      input :resource_type, :resource_id, :server_url, :access_token

      run do
        # Test Read Operation
        read_response = fhir_read(resource_type, resource_id)
        assert_response_status(200, read_response)
        assert_resource_type(resource_type, read_response)
        assert_valid_resource(read_response)

        # Test Search Operation
        search_response = fhir_search(resource_type, params: { _id: resource_id })
        assert_response_status(200, search_response)
        assert search_response.resource.entry.any?, 'Expected at least one resource in search results'

        # Test Create Operation
        new_resource = FHIR.const_get(resource_type.capitalize).new
        create_response = fhir_create(new_resource)
        assert_response_status(201, create_response)
        created_resource = create_response.resource
        assert created_resource.id.present?, 'Expected created resource to have an ID'

        # Test Update Operation
        updated_resource = created_resource.dup
        update_response = fhir_update(updated_resource)
        assert_response_status(200, update_response)

        # Test Delete Operation
        delete_response = fhir_delete(resource_type, created_resource.id)
        assert_response_status(204, delete_response)
      end
    end
  end
end