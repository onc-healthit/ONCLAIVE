module Test5_claude
  class ImplementationGuideProfilesGroup < Inferno::TestGroup
    id :implementation_guide_profiles_support
    title 'Implementation Guide Profiles Support'
    description %(
      Verify that the server supports all profiles defined in this Implementation Guide.
      The server SHALL demonstrate support for each profile through proper resource 
      validation and conformance to profile requirements.
    )

    PROFILES = [
      {
        resource_type: 'Patient',
        profile_url: 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient'
      },
      {
        resource_type: 'Practitioner',
        profile_url: 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner'
      }
      # Additional profiles would be listed here
    ]

    PROFILES.each do |profile|
      test do
        id "profile_support_#{profile[:resource_type].downcase}"
        title "Server supports #{profile[:resource_type]} profile"
        description %(
          Verify that the server properly supports the #{profile[:resource_type]} profile
          defined in the Implementation Guide.
        )

        run do
          # Search for resources of this type
          fhir_search(profile[:resource_type].to_sym)
          assert_response_status(200)
          assert_resource_type(profile[:resource_type].to_sym)

          # Get first resource for validation
          resource = resource_from_response.first
          assert resource.present?, "No #{profile[:resource_type]} resources found"

          # Validate resource against profile
          assert_valid_resource(profile_url: profile[:profile_url])

          # Check capability statement for profile declaration
          capability_statement = fhir_read_and_verify(:capability_statement, @capability_statement_id).resource
          
          rest = capability_statement.rest.find { |r| r.mode == 'server' }
          assert rest.present?, 'No server mode rest section found in capability statement'
          
          resource_stmnt = rest.resource.find { |r| r.type == profile[:resource_type] }
          assert resource_stmnt.present?, "No #{profile[:resource_type]} resource section in capability statement"
          
          supported_profile = resource_stmnt.supportedProfile&.include?(profile[:profile_url])
          assert supported_profile, "Profile #{profile[:profile_url]} not declared in capability statement"

          pass "Server successfully demonstrated support for #{profile[:resource_type]} profile"
        end
      end
    end
  end
end