module Test6_claude
  class LastUpdateRequirementGroup < Inferno::TestGroup
    id :last_update_requirement
    title 'Last Update Timestamp Requirement'
    description %(
      Validates that each profile includes a lastUpdate timestamp as required.
      
      Requirement REQ-30: Each profile in this guide requires that the lastUpdate 
      timestamp be provided as part of the profile's data content.
    )

    test do
      id :verify_last_update_timestamp
      title 'Verify lastUpdate timestamp is present'
      description %(
        This test verifies that a lastUpdate timestamp is present in the profile data.
        The timestamp must be populated with a valid date/time value.
      )
      
      input :profile_id
      
      run do
        fhir_read(:basic, profile_id)
        
        assert_response_status(200)
        assert_resource_type(:basic)
        
        profile = resource
        
        assert profile.meta&.lastUpdated.present?, 
          'Profile must include meta.lastUpdated timestamp'
          
        begin
          DateTime.parse(profile.meta.lastUpdated)
        rescue ArgumentError
          assert false, 'lastUpdated timestamp must be a valid date/time value'
        end

        assert DateTime.parse(profile.meta.lastUpdated) <= DateTime.now,
          'lastUpdated timestamp cannot be in the future'
      end
    end

    test do
      id :verify_last_update_format
      title 'Verify lastUpdate timestamp format'
      description %(
        This test verifies that the lastUpdate timestamp follows the 
        FHIR instant format (YYYY-MM-DDThh:mm:ss.sss+zz:zz).
      )

      input :profile_id
      
      run do
        fhir_read(:basic, profile_id)
        
        assert_response_status(200)
        profile = resource
        
        timestamp = profile.meta&.lastUpdated
        
        assert timestamp.present?, 'Profile must include meta.lastUpdated timestamp'
        
        timestamp_regex = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$/
        
        assert timestamp.match?(timestamp_regex),
          'lastUpdated timestamp must follow FHIR instant format (YYYY-MM-DDThh:mm:ss.sss+zz:zz)'
      end
    end
  end
end