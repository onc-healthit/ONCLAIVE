module Test5Gpt
  class SupportForAllProfilesTestGroup < Inferno::TestGroup
    id :req_12_support_for_all_profiles
    title 'Support for All Implementation Guide Profiles'
    description %(
      This test verifies that the Health Plan API supports all profiles defined in the Implementation Guide.
      The server SHALL conform to all profiles by returning valid resources for each profile.
    )

    # Define a test for each profile in the Implementation Guide
    # Assuming profiles are defined in an array for demonstration purposes
    profiles = [
      'http://example.org/fhir/StructureDefinition/example-profile-1',
      'http://example.org/fhir/StructureDefinition/example-profile-2'
      # Add more profiles as needed
    ]

    profiles.each do |profile_url|
      test do
        id :"support_for_#{profile_url.split('/').last}_test"
        title "Support for #{profile_url.split('/').last}"
        description %(
          Verify that the server supports the #{profile_url.split('/').last} profile by returning a valid resource conforming to this profile.
        )
        input :resource_id, :server_url, :access_token

        fhir_client do
          url :server_url
          bearer_token :access_token
        end

        run do
          fhir_read(:resource, resource_id)

          assert_response_status(200)
          assert_valid_resource(profile_url: profile_url)

          resource = resource()
          assert resource.meta.profile.include?(profile_url), "Expected resource to conform to profile #{profile_url}, but it did not."
        end
      end
    end
  end
end