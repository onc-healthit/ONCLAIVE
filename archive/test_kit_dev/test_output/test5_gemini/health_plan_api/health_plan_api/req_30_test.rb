module Test5Gemini
  class LastUpdateTimestampRequirementTest < Inferno::TestGroup
    id :req_30_last_update_timestamp_requirement
    title 'REQ-30: lastUpdate Timestamp Requirement'
    description %(
      Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content.
    )

    test do
      id :req_30_last_update_timestamp_present
      title 'LastUpdate timestamp is present in all profiles'
      description %(
        Verify that the lastUpdate timestamp is present in all profiles.
      )
      input :resource_type,
           title: 'Resource Type',
           description: 'The type of resource to test',
           default: 'Patient'

      run do
        fhir_read(resource_type, resource_id)
        assert_response_status(200)
        assert_resource_type(resource_type)

        assert resource.meta&.lastUpdated,
               "LastUpdate timestamp is missing for #{resource_type} with ID: #{resource_id}"
      end
    end
  end
end