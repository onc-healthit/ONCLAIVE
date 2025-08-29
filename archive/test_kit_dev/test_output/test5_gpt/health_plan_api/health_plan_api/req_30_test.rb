module Test5Gpt
  class LastUpdateTimestampTestGroup < Inferno::TestGroup
    id :req_30_last_update_timestamp
    title 'LastUpdate Timestamp Requirement'
    description %(
      This test group verifies that each profile in the Health Plan API
      includes a `lastUpdate` timestamp as part of the profile's data content.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :last_update_timestamp_test
      title 'Verify lastUpdate timestamp is present'
      description %(
        This test checks that the `lastUpdate` timestamp is present in the
        data content of each profile returned by the Health Plan API.
      )
      input :resource_type, title: 'FHIR Resource Type', description: 'The type of FHIR resource to check for lastUpdate timestamp'
      input :resource_id, title: 'Resource ID', description: 'The ID of the FHIR resource to check'

      run do
        fhir_read(resource_type.to_sym, resource_id)
        
        assert_response_status(200)
        assert_valid_resource

        last_update = resource.meta&.lastUpdated
        assert last_update.present?, "The `lastUpdate` timestamp is missing from the #{resource_type} resource with ID #{resource_id}."
      end
    end
  end
end