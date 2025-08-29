module Test5Gpt
  class DeletedResourceResponseTestGroup < Inferno::TestGroup
    id :req_17_deleted_resource_response
    title 'Deleted Resource Response'
    description %(
      This test group verifies that the Health Plan API returns a 410 status code
      when a request is made to a deleted resource, as required by REQ-17.
    )

    input :resource_type, :resource_id, :server_url, :access_token

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :deleted_resource_response_test
      title 'Server returns 410 for deleted resource'
      description %(
        This test ensures that the server returns a 410 status code when a request
        is made to access a resource that has been deleted.
      )

      run do
        # Attempt to delete the resource first to ensure it is deleted
        delete_response = fhir_delete(resource_type.to_sym, resource_id)
        assert_response_status(204, delete_response)

        # Attempt to access the deleted resource
        response = fhir_read(resource_type.to_sym, resource_id)

        # Assert that the response status is 410
        assert_response_status(410, response)
      end
    end
  end
end