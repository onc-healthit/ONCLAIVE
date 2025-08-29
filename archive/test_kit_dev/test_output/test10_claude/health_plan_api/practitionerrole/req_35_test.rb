module Test10_claude
  class ProviderSpecialtySearchGroup < Inferno::TestGroup
    id :provider_specialty_search
    title 'Provider Search by Specialty Tests'
    description %(
      Verify that the system supports searching for providers by specialty via
      PractitionerRole.specialty, including support for location and network filters.
    )

    input :specialty_code,
          title: 'Specialty Code',
          description: 'The specialty code to search for (e.g. "207RC0000X" for Cardiovascular Disease)'
    
    input :location_id,
          title: 'Location ID',
          description: 'Optional Location ID to filter results',
          optional: true

    input :network_id, 
          title: 'Network ID',
          description: 'Optional Network ID to filter results',
          optional: true

    input :url,
          title: 'FHIR Server URL'

    fhir_client do
      url :url
    end

    test do
      id :basic_specialty_search
      title 'Server returns matching providers when searching by specialty'
      description %(
        Verify that searching PractitionerRole by specialty returns appropriate results
      )
      makes_request :basic_specialty_search

      run do
        search_params = {
          specialty: specialty_code
        }

        fhir_search(:practitioner_role, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No PractitionerRole resources returned'

        resource.entry.each do |entry|
          assert entry.resource.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code }},
                "Returned PractitionerRole does not have matching specialty code #{specialty_code}"
        end
      end
    end

    test do
      id :specialty_location_search
      title 'Server supports filtering specialty search by location'
      description %(
        Verify that PractitionerRole specialty search can be filtered by location
      )
      
      uses_request :basic_specialty_search
      
      run do
        skip_if !location_id.present?, 'No location ID provided to test location filtering'

        search_params = {
          specialty: specialty_code,
          location: location_id
        }

        fhir_search(:practitioner_role, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        resource.entry.each do |entry|
          assert entry.resource.location.any? { |loc| loc.reference.include?(location_id) },
                "Returned PractitionerRole is not associated with location #{location_id}"
        end
      end
    end

    test do
      id :specialty_network_search  
      title 'Server supports filtering specialty search by network'
      description %(
        Verify that PractitionerRole specialty search can be filtered by network
      )

      uses_request :basic_specialty_search

      run do
        skip_if !network_id.present?, 'No network ID provided to test network filtering'

        search_params = {
          specialty: specialty_code,
          network: network_id
        }

        fhir_search(:practitioner_role, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)

        resource.entry.each do |entry|
          assert entry.resource.network.any? { |net| net.reference.include?(network_id) },
                "Returned PractitionerRole is not associated with network #{network_id}"
        end
      end
    end
  end
end