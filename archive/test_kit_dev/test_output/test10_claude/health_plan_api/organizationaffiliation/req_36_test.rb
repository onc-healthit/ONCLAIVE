module Test10_claude
  class OrganizationSpecialtySearchGroup < Inferno::TestGroup
    id :organization_specialty_search
    title 'Organization Search by Specialty'
    description %(
      Verify that the server supports searching for Organizations by specialty via 
      OrganizationAffiliation.specialty, including support for filtering by location 
      and network, and searching by name.
    )

    input :url,
          title: 'FHIR Server Base URL',
          description: 'Base URL of FHIR server'

    input :org_specialty,
          title: 'Organization Specialty Code',
          description: 'The specialty code to search for (e.g. "compounding-pharmacy")',
          default: 'compounding-pharmacy'

    input :location_id,
          title: 'Location ID',
          description: 'ID of a Location resource to filter results',
          optional: true

    input :network_id, 
          title: 'Network ID',
          description: 'ID of a Network resource to filter results',
          optional: true

    input :org_name,
          title: 'Organization Name',
          description: 'Organization name to search for',
          optional: true

    fhir_client do
      url :url
    end

    test do
      id :search_by_specialty
      title 'Server returns matching organizations when searching by specialty'
      description %(
        Test that the server can find organizations with a specific specialty
        by searching OrganizationAffiliation.specialty
      )

      run do
        fhir_search(:organization_affiliation, params: { specialty: org_specialty })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, "No OrganizationAffiliation resources returned for specialty: #{org_specialty}"
      end
    end

    test do
      id :search_by_specialty_and_location
      title 'Server supports filtering organization specialty search by location'
      description %(
        Test that organization specialty search results can be filtered by location
      )
      
      skip_if !location_id.present?, 'No location ID provided to test location filtering'

      run do
        search_params = { 
          specialty: org_specialty,
          location: location_id
        }
        fhir_search(:organization_affiliation, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.all? { |entry| entry.resource.location.any? { |loc| loc.reference.include?(location_id) } },
               "Not all results are associated with the specified location"
      end
    end

    test do
      id :search_by_specialty_and_network  
      title 'Server supports filtering organization specialty search by network'
      description %(
        Test that organization specialty search results can be filtered by network
      )

      skip_if !network_id.present?, 'No network ID provided to test network filtering'

      run do
        search_params = {
          specialty: org_specialty,
          network: network_id
        }
        fhir_search(:organization_affiliation, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.all? { |entry| entry.resource.network.any? { |net| net.reference.include?(network_id) } },
               "Not all results are associated with the specified network"
      end
    end

    test do
      id :search_by_specialty_and_name
      title 'Server supports filtering organization specialty search by name'
      description %(
        Test that organization specialty search results can be filtered by organization name
      )

      skip_if !org_name.present?, 'No organization name provided to test name filtering'

      run do
        search_params = {
          specialty: org_specialty,
          'primary-organization.name': org_name
        }
        fhir_search(:organization_affiliation, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        org_refs = resource.entry.map { |e| e.resource.organization.reference }
        
        org_refs.each do |ref|
          fhir_read(:organization, ref.split('/').last)
          assert resource.name.downcase.include?(org_name.downcase),
                 "Organization #{ref} name does not match search criteria"
        end
      end
    end
  end
end