module Test9_claude
  class ProviderSpecialtySearchGroup < Inferno::TestGroup
    id :provider_specialty_search
    title 'Provider Search by Specialty Tests'
    description %(
      Verify that the server supports searching for providers by specialty.
      The Plan-Net design requires support for searching PractitionerRole resources
      by specialty, with optional qualification parameters for location and network.
    )

    input :server_url,
          title: 'FHIR Server URL',
          description: 'Base URL for the FHIR server'

    input :specialty_code,
          title: 'Provider Specialty Code',
          description: 'The specialty code to search for (e.g., "207RC0000X" for Cardiovascular Disease)',
          default: '207RC0000X'

    input :location_id,
          title: 'Location ID',
          description: 'Optional Location ID to filter results',
          optional: true

    input :network_id,
          title: 'Network ID', 
          description: 'Optional Network ID to filter results',
          optional: true

    fhir_client do
      url :server_url
    end

    test do
      id :specialty_search_basic
      title 'Server returns matching providers when searching by specialty'
      description %(
        Verify that the server can return PractitionerRole resources
        matching a specific specialty code.
      )
      
      makes_request :specialty_search
      
      run do
        search_params = { specialty: specialty_code }
        fhir_search(:practitionerrole, params: search_params, name: :specialty_search)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        assert resource.entry.present?, 'No PractitionerRole resources returned for specialty search'
        
        resource.entry.each do |entry|
          assert entry.resource.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } },
                 "Returned PractitionerRole does not contain expected specialty code: #{specialty_code}"
        end
      end
    end

    test do
      id :specialty_search_with_location
      title 'Server supports searching by specialty and location'
      description %(
        Verify that the server can filter provider specialty search results by location.
      )
      
      makes_request :location_search
      
      run do
        skip_if !location_id.present?, 'No location ID provided, skipping location-qualified search'

        search_params = { 
          specialty: specialty_code,
          location: location_id
        }
        
        fhir_search(:practitionerrole, params: search_params, name: :location_search)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        resource.entry.each do |entry|
          assert entry.resource.location.any? { |loc| loc.reference.include?(location_id) },
                 "Returned PractitionerRole not associated with specified location: #{location_id}"
        end
      end
    end

    test do
      id :specialty_search_with_network
      title 'Server supports searching by specialty and network'
      description %(
        Verify that the server can filter provider specialty search results by network.
      )

      makes_request :network_search
      
      run do
        skip_if !network_id.present?, 'No network ID provided, skipping network-qualified search'

        search_params = {
          specialty: specialty_code,
          network: network_id
        }

        fhir_search(:practitionerrole, params: search_params, name: :network_search)

        assert_response_status(200)
        assert_resource_type(:bundle)

        resource.entry.each do |entry|
          assert entry.resource.network.any? { |net| net.reference.include?(network_id) },
                 "Returned PractitionerRole not associated with specified network: #{network_id}"
        end
      end
    end
  end
end