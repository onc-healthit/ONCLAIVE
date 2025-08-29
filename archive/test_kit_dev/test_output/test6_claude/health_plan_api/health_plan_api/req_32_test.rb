module Test6_claude
  class PharmacyGeneralSearchTest < Inferno::TestGroup
    id :plan_net_pharmacy_general_search
    title 'General Search for Pharmacy'
    description %(
      Verify that the server supports general pharmacy search functionality using:
      - HealthcareService.category
      - HealthcareService.specialty
      With optional qualifications for:
      - Location
      - Network
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :pharmacy_category_search
      title 'Search HealthcareService by category'
      description 'Verify search functionality using HealthcareService.category'
      
      run do
        search_params = { 'category': 'pharm' }
        fhir_search(:healthcareservice, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:healthcareservice)
        
        skip_if resources.empty?, 'No pharmacy HealthcareServices found'
        
        resources.each do |resource|
          assert resource.category.any? { |c| c.coding.any? { |code| code.code == 'pharm' } },
                 'Resource category must include pharmacy code'
        end
      end
    end

    test do
      id :pharmacy_specialty_search  
      title 'Search HealthcareService by specialty'
      description 'Verify search functionality using HealthcareService.specialty'

      run do
        search_params = { 'specialty': 'pharmacy' }
        fhir_search(:healthcareservice, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:healthcareservice)

        skip_if resources.empty?, 'No pharmacy specialty HealthcareServices found'

        resources.each do |resource|
          assert resource.specialty.any? { |s| s.coding.any? { |code| code.code.include?('pharm') } },
                 'Resource specialty must include pharmacy-related code'
        end
      end
    end

    test do
      id :pharmacy_location_qualified_search
      title 'Search HealthcareService with location qualification'
      description 'Verify search functionality with location qualification'
      
      run do
        search_params = {
          'category': 'pharm',
          'location': 'Location/123'
        }
        fhir_search(:healthcareservice, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:healthcareservice)
      end
    end

    test do
      id :pharmacy_network_qualified_search  
      title 'Search HealthcareService with network qualification'
      description 'Verify search functionality with network qualification'
      
      run do
        search_params = {
          'category': 'pharm',
          'network': 'Organization/123'
        }
        fhir_search(:healthcareservice, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:healthcareservice)
      end
    end

    def assert_valid_bundle_entries(resource_type)
      assert resources.present?, 'No resources returned'
      resources.each do |resource|
        assert resource.resourceType == resource_type.to_s.capitalize,
               "Resource type #{resource.resourceType} does not match expected type #{resource_type}"
        assert_valid_resource(resource: resource)
      end
    end
  end
end