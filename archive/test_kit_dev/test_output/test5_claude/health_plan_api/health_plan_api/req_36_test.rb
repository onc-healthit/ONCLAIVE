module Test5_claude
  class OrganizationSpecialtySearchTest < Inferno::TestGroup
    id :organization_specialty_search
    title 'Organization Search by Specialty'
    description %(
      Verify that the server supports searching for Organizations by specialty via
      OrganizationAffiliation.specialty, with optional qualification by location, 
      network, and name parameters.
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
          description: 'The bearer token for accessing the FHIR server'

    test do
      id :organization_specialty_search_basic
      title 'Server handles basic Organization search by specialty'
      description %(
        Verify that the server properly handles a basic Organization search
        filtered by specialty via OrganizationAffiliation.specialty
      )

      run do
        # Search for pharmacy specialty organizations
        specialty_code = '183500000X' # Pharmacy code from NUCC
        search_params = { 'specialty' => specialty_code }
        
        fhir_search(:organization, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert bundle.entry.length.positive?, 'No Organizations returned'
        
        bundle.entry.each do |entry|
          assert_valid_resource(entry.resource)
          assert entry.resource.resourceType == 'Organization', 
                 "Expected Organization resources but found #{entry.resource.resourceType}"
        end
      end
    end

    test do
      id :organization_specialty_search_qualified
      title 'Server handles qualified Organization specialty search'
      description %(
        Verify that the server properly handles Organization specialty search
        with additional qualifying parameters for location, network and name
      )

      run do
        specialty_code = '183500000X' # Pharmacy code
        search_params = {
          'specialty' => specialty_code,
          'location' => 'MA', # Example location qualifier
          'network' => 'NETWORK123', # Example network qualifier  
          'name' => 'pharmacy' # Example name qualifier
        }

        fhir_search(:organization, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)

        if bundle.entry.present?
          bundle.entry.each do |entry|
            assert_valid_resource(entry.resource)
            assert entry.resource.resourceType == 'Organization',
                   "Expected Organization resources but found #{entry.resource.resourceType}"
            
            # Verify name filter was applied if results returned
            if entry.resource.name.present?
              assert entry.resource.name.downcase.include?('pharmacy'),
                     "Organization name #{entry.resource.name} does not match search criteria"
            end
          end
        end
      end
    end

    test do
      id :organization_specialty_search_invalid
      title 'Server handles invalid specialty search appropriately' 
      description %(
        Verify that the server returns appropriate error responses for
        invalid specialty search parameters
      )

      run do
        invalid_specialty = 'INVALID_CODE'
        search_params = { 'specialty' => invalid_specialty }

        fhir_search(:organization, params: search_params)

        assert_response_status([400, 404, 422].to_set)
        
        if response[:code] == 400 || response[:code] == 422
          assert_resource_type(:operationoutcome)
          assert resource.issue&.any? { |issue| issue.severity == 'error' },
                 'OperationOutcome should contain error severity issues'
        end
      end
    end

  end
end