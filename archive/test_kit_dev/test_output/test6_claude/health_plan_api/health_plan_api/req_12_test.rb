module Test6_claude
  class ProfileSupportTestGroup < Inferno::TestGroup
    id :profile_support_req12
    title 'Support for Implementation Guide Profiles'
    description %(
      Verify that the Health Plan API supports all profiles defined in the Implementation Guide.
      
      This test group validates that each profile can be successfully retrieved and 
      conforms to the structural and semantic requirements defined in the IG.
    )

    PROFILES = [
      {
        name: 'HealthPlan',
        url: 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/healthplan',
        resource_type: 'Organization'
      },
      {
        name: 'Network',  
        url: 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network',
        resource_type: 'Organization'
      },
      {
        name: 'InsurancePlan',
        url: 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-InsurancePlan',
        resource_type: 'InsurancePlan'
      }
    ]

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    input :url,
          title: 'Health Plan FHIR Server Base URL',
          description: 'Base URL for the FHIR server'

    input :bearer_token,
          title: 'Bearer Token',
          description: 'Bearer token for accessing the FHIR server'

    PROFILES.each do |profile|
      test do
        id "profile_support_#{profile[:name].downcase}"
        title "Support for #{profile[:name]} Profile"
        description "Verify support for the #{profile[:name]} profile"

        run do
          # Search for resources of this type
          search_response = fhir_search(profile[:resource_type], 
            params: {
              _profile: profile[:url],
              _count: 1
            }
          )

          assert_response_status(200)
          assert_resource_type('Bundle')
          assert search_response.resource.entry.present?, 
            "No #{profile[:resource_type]} resources found conforming to #{profile[:name]} profile"

          # Validate first returned resource against profile
          resource = search_response.resource.entry.first.resource
          assert_valid_resource(profile_url: profile[:url])

          # Try to read the resource directly
          read_response = fhir_read(profile[:resource_type], resource.id)
          assert_response_status(200)
          assert_valid_resource(profile_url: profile[:url])

        rescue Inferno::AssertionException => e
          fail "Profile validation failed for #{profile[:name]}: #{e.message}"
        end
      end
    end

    test do
      id :profile_support_summary
      title 'Profile Support Summary'
      description 'Verify overall profile support requirements'
      
      run do
        skip_count = 0
        fail_count = 0
        
        PROFILES.each do |profile|
          result = test_results.find { |r| r.test_id == "profile_support_#{profile[:name].downcase}" }
          case result&.result
          when 'skip'
            skip_count += 1
          when 'fail' 
            fail_count += 1
          end
        end

        assert fail_count.zero?, "#{fail_count} profile(s) failed validation"
        assert skip_count.zero?, "#{skip_count} profile(s) were skipped"
        pass "All #{PROFILES.length} required profiles are supported"
      end
    end

  end
end