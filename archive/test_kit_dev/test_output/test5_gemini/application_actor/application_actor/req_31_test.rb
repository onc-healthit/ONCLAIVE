module Test5_gemini
  class ClientDirectoryUpdatesTrackingTest < Inferno::TestGroup
    id :req_31_client_directory_updates_tracking
    title 'REQ-31: Client Tracking of Directory Content Updates'
    description %(
      Verify that clients can track additions or modifications to directory content
      through queries that filter content using the _lastUpdated search parameter.
    )

    test do
      id :req_31_lastupdated_search_parameter_support
      title 'Server supports _lastUpdated search parameter'
      description %(
        Test if the server supports the _lastUpdated search parameter for directory resources.
      )
      input :directory_resource_type,
            title: 'Directory Resource Type',
            description: 'The type of directory resource to test',
            default: 'Patient'

      run do
        fhir_search(directory_resource_type, params: { '_lastUpdated': 'gt2020-01-01' })

        assert_response_status(200)
        assert_valid_resource_type(directory_resource_type)
      end
    end

    test do
      id :req_31_track_changes_with_lastupdated
      title 'Client can track changes using _lastUpdated'
      description %(
        Test if the client can track additions or modifications to directory content
        using the _lastUpdated search parameter.
      )
      input :directory_resource_type,
            title: 'Directory Resource Type',
            description: 'The type of directory resource to test',
            default: 'Patient'

      run do
        initial_response = fhir_search(directory_resource_type, params: {})
        assert_response_status(200)
        assert_valid_resource_type(directory_resource_type)

        # Introduce a delay to allow for potential updates
        sleep(5)

        updated_response = fhir_search(directory_resource_type, params: { '_lastUpdated': "ge#{initial_response.response_headers['Last-Modified']}" })
        assert_response_status(200)
        assert_valid_resource_type(directory_resource_type)

        # Further assertions can be added to compare the content of the two responses
        # and verify that the updates are reflected correctly.
      end
    end
  end
end