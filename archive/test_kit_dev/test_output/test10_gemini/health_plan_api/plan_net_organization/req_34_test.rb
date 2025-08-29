module Test10_gemini
  class REQ34OrganizationSearchGroup < Inferno::TestGroup
    id :req_34_organization_search_group
    title 'REQ-34: Organization Search by Name and Qualifications'
    description %(
      This test group verifies the server's ability to search for Organization resources
      by name and various qualifying parameters as specified in REQ-34 of the Plan-Net design.
      
      The Plan-Net design is based around the following types of searches:
      - Organization by Name (e.g., "Montgomery Cardiology" or "CVS")
      - Focal Resource and Field: Organization.name
      - Qualifications of Search: Location, network, specialty.
      
      This group includes tests for:
      1. Searching Organization by `name`.
      2. Searching Organization by `name` combined with `address:city`.
      3. Searching Organization by `name` combined with `address:state`.
      4. Verifying if the server's CapabilityStatement declares support for `network` and `specialty` search parameters on Organization.
    )

    # Inputs for the tests. Assuming 'url' and 'credentials' are provided by the parent TestSuite.
    input :organization_name_search_param,
          title: 'Organization Name for Search',
          description: 'A name (or part of a name) of an Organization to search for (e.g., "Montgomery" or "CVS").',
          type: :text,
          default: 'CVS' # Provide a reasonable default for testing
    input :organization_city_search_param,
          title: 'Organization City for Search',
          description: 'A city name to qualify the Organization search (e.g., "Boston"). This input is optional.',
          type: :text,
          optional: true
    input :organization_state_search_param,
          title: 'Organization State for Search',
          description: 'A state name (or abbreviation) to qualify the Organization search (e.g., "MA"). This input is optional.',
          type: :text,
          optional: true

    # Test 1: Search by name
    test do
      id :req_34_organization_search_by_name
      title 'Search Organization by name'
      description %(
        This test verifies that the server can successfully search for Organization resources
        using the `name` search parameter.
        
        The test expects:
        - A 200 OK HTTP response.
        - The response body to be a FHIR Bundle resource.
        - The Bundle to contain at least one Organization resource.
        - All resources in the Bundle entries to be of type 'Organization'.
      )
      # Declare inputs used by this specific test
      input :organization_name_search_param
      
      run do
        skip_if organization_name_search_param.blank?, 'No organization name provided to search. Skipping this test.'

        fhir_search(:organization, params: { name: organization_name_search_param })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        assert resource.entry.present?, "No Organization resources found for name: '#{organization_name_search_param}'. Expected at least one."
        
        # Validate that all returned resources in the bundle are Organization type
        resource.entry.each_with_index do |entry, index|
          assert entry.resource.resourceType == 'Organization', 
                 "Expected resourceType 'Organization' for entry #{index}, but found '#{entry.resource.resourceType}'."
        end
      end
    end

    # Test 2: Search by name and address:city
    test do
      id :req_34_organization_search_by_name_and_city
      title 'Search Organization by name and address:city'
      description %(
        This test verifies that the server can successfully search for Organization resources
        using a combination of `name` and `address:city` search parameters.
        
        The test expects:
        - A 200 OK HTTP response.
        - The response body to be a FHIR Bundle resource.
        - The Bundle to contain at least one Organization resource matching both criteria.
        - All returned Organization resources to have an address that includes the specified city.
      )
      # Declare inputs used by this specific test
      input :organization_name_search_param, :organization_city_search_param

      run do
        skip_if organization_name_search_param.blank?, 'No organization name provided to search. Skipping this test.'
        skip_if organization_city_search_param.blank?, 'No organization city provided to qualify search. Skipping this test.'

        fhir_search(:organization, params: { name: organization_name_search_param, 'address:city': organization_city_search_param })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        assert resource.entry.present?, "No Organization resources found for name: '#{organization_name_search_param}' and city: '#{organization_city_search_param}'. Expected at least one."
        
        # Validate that all returned resources are Organization type and match the city
        resource.entry.each_with_index do |entry, index|
          assert entry.resource.resourceType == 'Organization', 
                 "Expected resourceType 'Organization' for entry #{index}, but found '#{entry.resource.resourceType}'."
          
          # Check if the returned organization's address actually contains the specified city (case-insensitive)
          found_city = entry.resource.address.any? { |addr| addr.city&.downcase == organization_city_search_param.downcase }
          assert found_city, "Returned Organization (ID: #{entry.resource.id}) from entry #{index} does not have an address in city: '#{organization_city_search_param}'."
        end
      end
    end

    # Test 3: Search by name and address:state
    test do
      id :req_34_organization_search_by_name_and_state
      title 'Search Organization by name and address:state'
      description %(
        This test verifies that the server can successfully search for Organization resources
        using a combination of `name` and `address:state` search parameters.
        
        The test expects:
        - A 200 OK HTTP response.
        - The response body to be a FHIR Bundle resource.
        - The Bundle to contain at least one Organization resource matching both criteria.
        - All returned Organization resources to have an address that includes the specified state.
      )
      # Declare inputs used by this specific test
      input :organization_name_search_param, :organization_state_search_param

      run do
        skip_if organization_name_search_param.blank?, 'No organization name provided to search. Skipping this test.'
        skip_if organization_state_search_param.blank?, 'No organization state provided to qualify search. Skipping this test.'

        fhir_search(:organization, params: { name: organization_name_search_param, 'address:state': organization_state_search_param })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        assert resource.entry.present?, "No Organization resources found for name: '#{organization_name_search_param}' and state: '#{organization_state_search_param}'. Expected at least one."
        
        # Validate that all returned resources are Organization type and match the state
        resource.entry.each_with_index do |entry, index|
          assert entry.resource.resourceType == 'Organization', 
                 "Expected resourceType 'Organization' for entry #{index}, but found '#{entry.resource.resourceType}'."
          
          # Check if the returned organization's address actually contains the specified state (case-insensitive)
          found_state = entry.resource.address.any? { |addr| addr.state&.downcase == organization_state_search_param.downcase }
          assert found_state, "Returned Organization (ID: #{entry.resource.id}) from entry #{index} does not have an address in state: '#{organization_state_search_param}'."
        end
      end
    end

    # Test 4: Verify CapabilityStatement support for network and specialty search parameters
    test do
      id :req_34_organization_capability_statement_search_params
      title 'Verify CapabilityStatement declares support for network and specialty search parameters on Organization'
      description %(
        This test verifies that the server's CapabilityStatement declares support for
        the `network` and `specialty` search parameters for the Organization resource,
        as required by REQ-34 of the Plan-Net design.
        
        The test expects:
        - A 200 OK HTTP response from the /metadata endpoint.
        - The response body to be a FHIR CapabilityStatement resource.
        - The CapabilityStatement to declare support for the Organization resource.
        - The Organization resource definition within the CapabilityStatement to list
          `network` and `specialty` as supported search parameters.
      )
      
      run do
        fhir_get_capability_statement

        assert_response_status(200)
        assert_resource_type(:capability_statement)
        
        # Find the Organization resource in the CapabilityStatement
        organization_resource_capability = resource.rest&.first&.resource&.find { |r| r.type == 'Organization' }
        
        assert organization_resource_capability.present?, 
               'CapabilityStatement does not declare support for the Organization resource.'
        
        # Check for 'network' search parameter
        network_param_supported = organization_resource_capability.searchParam&.any? { |param| param.name == 'network' }
        assert network_param_supported, 
               'CapabilityStatement for Organization resource does not declare support for the "network" search parameter.'
        
        # Check for 'specialty' search parameter
        specialty_param_supported = organization_resource_capability.searchParam&.any? { |param| param.name == 'specialty' }
        assert specialty_param_supported, 
               'CapabilityStatement for Organization resource does not declare support for the "specialty" search parameter.'
      end
    end
  end
end