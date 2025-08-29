module Test5_claude
  class ProfileSupportTestGroup < Inferno::TestGroup
    id :profile_support_test_group
    title 'Support for Implementation Guide Profiles'
    description %(
      Verify that the server supports all profiles defined in this Implementation Guide.
      The server SHALL demonstrate support for each profile through proper resource 
      validation and conformance to profile requirements.
    )

    CONFIG_PROFILES = [
      {
        resource_type: 'Patient',
        profile_url: 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient'
      },
      {
        resource_type: 'Coverage', 
        profile_url: 'http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-Coverage'
      }
      # Additional profiles would be listed here
    ]

    CONFIG_PROFILES.each do |profile_config|
      test do
        id "profile_support_#{profile_config[:resource_type].downcase}"
        title "Server supports #{profile_config[:resource_type]} profile"
        description %(
          Verify that the server properly supports the #{profile_config[:resource_type]}
          profile defined in the Implementation Guide.
        )

        run do
          # Search for resources of this type
          fhir_search(profile_config[:resource_type].to_sym)
          assert_response_status(200)
          assert_resource_type(profile_config[:resource_type].to_sym)

          # Get first resource for validation
          resource = resource_in_bundle.first
          assert resource.present?, "No #{profile_config[:resource_type]} resources found"

          # Validate resource against profile
          assert_valid_resource(profile_url: profile_config[:profile_url])

          # Check meta.profile
          profiles = resource.meta&.profile
          assert profiles.present?, "Resource must declare profile conformance in meta.profile"
          assert profiles.include?(profile_config[:profile_url]), 
                 "Resource must declare conformance to #{profile_config[:profile_url]}"

          # Verify required elements per profile
          validate_required_elements(resource, profile_config[:profile_url])
        end
      end
    end

    def validate_required_elements(resource, profile_url)
      profile = FHIR.from_contents(load_profile(profile_url))
      required_elements = profile.snapshot.element.select { |e| e.min > 0 }

      required_elements.each do |element|
        path = element.path
        assert resource.send(path).present?,
               "Required element #{path} is missing"
      end
    end

    def load_profile(url)
      # Implementation would load profile definition from server or local cache
      # Simplified for example
      "{}" 
    end
  end
end