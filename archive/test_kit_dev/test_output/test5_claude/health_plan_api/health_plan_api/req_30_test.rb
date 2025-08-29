module Test5_claude
  class LastUpdateTimestampGroup < Inferno::TestGroup
    id :last_update_timestamp_requirement
    title 'LastUpdate Timestamp Requirement'
    description %(
      Validates that each profile in this guide includes a lastUpdate timestamp 
      as part of the profile's data content.

      Requirement: REQ-30 - Each profile in this guide requires that the lastUpdate 
      timestamp be provided as part of the profile's data content.
    )

    test do
      id :verify_last_update_exists
      title 'Verify lastUpdate timestamp exists'
      description %(
        This test verifies that the lastUpdate timestamp element is present
        in each profile's data content.
      )
      
      # Inputs for the profile URLs to test
      input :profile_urls,
            title: 'Profile URLs',
            description: 'Comma-separated list of profile URLs to validate',
            default: 'Profile1,Profile2'

      run do
        profile_url_list = profile_urls.split(',')

        profile_url_list.each do |profile_url|
          fhir_read(:structuredefinition, profile_url)
          assert_response_status(200)
          assert_resource_type(:structuredefinition)

          profile = resource
          
          # Verify lastUpdate element exists and is populated
          assert profile.date.present?, 
                 "Profile #{profile_url} is missing required lastUpdate timestamp"

          # Verify lastUpdate is valid dateTime
          begin
            DateTime.parse(profile.date)
          rescue ArgumentError
            fail "Profile #{profile_url} has invalid lastUpdate timestamp format: #{profile.date}"
          end

          # Verify lastUpdate is not empty/default
          assert profile.date != '1900-01-01T00:00:00Z', 
                 "Profile #{profile_url} has default/empty lastUpdate timestamp"
        end

        pass "All profiles contain valid lastUpdate timestamps"
      end
    end

    test do
      id :verify_last_update_recent 
      title 'Verify lastUpdate timestamp is recent'
      description %(
        This test verifies that the lastUpdate timestamp is relatively recent
        and not overly stale.
      )

      uses_request :verify_last_update_exists

      run do
        profile_url_list = profile_urls.split(',')

        profile_url_list.each do |profile_url|
          fhir_read(:structuredefinition, profile_url)
          
          profile = resource
          last_update = DateTime.parse(profile.date)
          
          # Verify lastUpdate is within last year
          assert last_update > 1.year.ago,
                 "Profile #{profile_url} lastUpdate timestamp is over 1 year old: #{profile.date}"
        end

        pass "All profiles have recent lastUpdate timestamps"
      end
    end
  end
end