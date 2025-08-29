module Test5Gpt
  class ClientTrackingDirectoryContentUpdatesTestGroup < Inferno::TestGroup
    id :req_31_client_tracking_directory_content_updates
    title 'Client Tracking of Directory Content Updates'
    description %(
      Clients that cache query results can track additions or modifications to
      directory content through queries that filter content using the _lastUpdated
      search parameter.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :req_31_last_updated_search_test
      title 'Search for resources using _lastUpdated parameter'
      description %(
        Verify that the server supports searching for resources using the _lastUpdated
        parameter to track additions or modifications to directory content.
      )
      input :resource_type, :last_updated_time

      run do
        # Perform a search using the _lastUpdated parameter
        response = fhir_search(resource_type.to_sym, params: { _lastUpdated: "gt#{last_updated_time}" })

        # Assertions to validate the response
        assert_response_status(200)
        assert_bundle_response

        # Check if the resources returned have a lastUpdated time greater than the specified time
        resources = resource.entry.map(&:resource)
        resources.each do |resource|
          assert resource.meta.lastUpdated > DateTime.parse(last_updated_time),
                 "Resource lastUpdated time #{resource.meta.lastUpdated} is not greater than #{last_updated_time}"
        end
      end
    end
  end
end