module Test5_claude
  class PharmacySearchTestGroup < Inferno::TestGroup
    id :pharmacy_general_search
    title 'General Search for Pharmacy'
    description %(
      Verify that the server supports general pharmacy search functionality based on:
      - HealthcareService.category
      - HealthcareService.specialty
      With qualifying parameters for Location and network.
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
          description: 'Bearer token for authorization'

    test do
      id :pharmacy_category_search
      title 'Search HealthcareService by category'
      description 'Verify search functionality using HealthcareService.category'
      
      run do
        search_params = { 
          'category' => 'pharm'
        }
        
        fhir_search(:healthcareservice, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert bundle.entry.length.positive?, 'No pharmacy services returned'
        
        bundle.entry.each do |entry|
          assert entry.resource.is_a?(FHIR::HealthcareService), 
                'Bundle contains non-HealthcareService resources'
          assert entry.resource.category.any? { |c| c.coding.any? { |coding| coding.code == 'pharm' } },
                'HealthcareService resource missing pharmacy category'
        end
      end
    end

    test do
      id :pharmacy_specialty_search  
      title 'Search HealthcareService by specialty'
      description 'Verify search functionality using HealthcareService.specialty'
      
      run do
        search_params = {
          'specialty' => 'pharmacy'
        }
        
        fhir_search(:healthcareservice, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert bundle.entry.length.positive?, 'No pharmacy specialty services returned'
        
        bundle.entry.each do |entry|
          assert entry.resource.is_a?(FHIR::HealthcareService),
                'Bundle contains non-HealthcareService resources'
          assert entry.resource.specialty.any? { |s| s.coding.any? { |coding| coding.code == 'pharmacy' } },
                'HealthcareService resource missing pharmacy specialty'
        end
      end
    end

    test do
      id :pharmacy_location_search
      title 'Search Pharmacy by Location'
      description 'Verify pharmacy search with Location qualification'
      
      run do
        search_params = {
          'category' => 'pharm',
          'location' => 'Location/123' # Example location reference
        }
        
        fhir_search(:healthcareservice, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle.entry.each do |entry|
          assert entry.resource.is_a?(FHIR::HealthcareService),
                'Bundle contains non-HealthcareService resources'
          assert entry.resource.location.any?,
                'HealthcareService missing location reference'
        end
      end
    end

    test do
      id :pharmacy_network_search
      title 'Search Pharmacy by Network'
      description 'Verify pharmacy search with network qualification'
      
      run do
        search_params = {
          'category' => 'pharm',
          'network' => 'Organization/123' # Example network reference
        }
        
        fhir_search(:healthcareservice, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle.entry.each do |entry|
          assert entry.resource.is_a?(FHIR::HealthcareService),
                'Bundle contains non-HealthcareService resources'
          assert entry.resource.providedBy&.reference&.start_with?('Organization/'),
                'HealthcareService missing network organization reference'
        end
      end
    end
  end
end