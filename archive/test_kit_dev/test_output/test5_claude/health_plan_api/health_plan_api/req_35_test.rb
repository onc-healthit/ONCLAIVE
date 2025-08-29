module Test5_claude
  class ProviderSpecialtySearchGroup < Inferno::TestGroup
    id :provider_specialty_search
    title 'Provider Search by Specialty'
    description %(
      Verify that the server supports searching for providers by specialty using 
      PractitionerRole.specialty, including optional refinements by location and 
      network.

      This test focuses on searching PractitionerRole resources filtered by specialty
      codes to find providers with specific qualifications.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    input :url,
          title: 'FHIR Server URL',
          description: 'The base URL for the FHIR server'

    input :bearer_token,
          title: 'Bearer Token',
          description: 'Bearer token for server authentication'

    test do
      id :basic_specialty_search
      title 'Server supports basic PractitionerRole search by specialty'
      description %(
        Verify that the server supports searching PractitionerRole resources
        by specialty using the specialty search parameter.
      )

      run do
        # Search for cardiologists using standard specialty code
        specialty_code = '207RC0000X' # NUCC code for Cardiovascular Disease
        search_params = { specialty: specialty_code }
        
        fhir_search(:practitionerrole, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.present?, 'No PractitionerRole resources returned'
        
        bundle.entry.each do |entry|
          assert entry.resource.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } },
                "Returned PractitionerRole does not have specified specialty code #{specialty_code}"
        end
      end
    end

    test do
      id :specialty_search_with_location
      title 'Server supports PractitionerRole specialty search refined by location'
      description %(
        Verify that the server supports searching PractitionerRole resources
        by specialty with additional location filtering.
      )

      run do
        specialty_code = '207RC0000X'
        location_state = 'CA'
        
        search_params = {
          specialty: specialty_code,
          'location.address-state': location_state
        }

        fhir_search(:practitionerrole, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource

        skip_if bundle.entry.empty?, 'No results found for specialty+location search'

        bundle.entry.each do |entry|
          role = entry.resource
          assert role.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } },
                'Returned PractitionerRole does not have specified specialty'
                
          assert role.location.any? { |loc_ref| 
            location = fhir_read(:location, loc_ref.reference.split('/').last).resource
            location.address&.state == location_state
          }, 'Returned PractitionerRole not associated with specified state'
        end
      end
    end

    test do
      id :specialty_search_with_network
      title 'Server supports PractitionerRole specialty search refined by network'
      description %(
        Verify that the server supports searching PractitionerRole resources
        by specialty with additional network filtering.
      )

      run do
        specialty_code = '207RC0000X'
        search_params = {
          specialty: specialty_code,
          network: 'network-id' # Example network identifier
        }

        fhir_search(:practitionerrole, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource

        skip_if bundle.entry.empty?, 'No results found for specialty+network search'

        bundle.entry.each do |entry|
          role = entry.resource
          assert role.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } },
                'Returned PractitionerRole does not have specified specialty'
          
          assert role.network.present?, 
                'Returned PractitionerRole does not have network information'
        end
      end
    end
  end
end