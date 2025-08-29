module Test5_claude
  class PharmacyGeneralSearchTest < Inferno::TestGroup
    id :pharmacy_general_search
    title 'General Search for Pharmacy'
    description %(
      Verify that the server supports general pharmacy searches using:
      * HealthcareService.category
      * HealthcareService.specialty
      * With qualifications for Location and network
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :pharmacy_category_search
      title 'Server handles HealthcareService category search'
      description 'Verify search by category returns pharmacy services'
      
      run do
        fhir_search(:healthcareservice, params: {
          category: 'pharm'
        })
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_bundle_response_type(:searchset)
        
        resources = resource.entry&.map(&:resource)
        assert resources.present?, 'No HealthcareService resources returned'
        
        resources.each do |service|
          assert service.category.any? { |c| c.coding.any? { |code| code.code == 'pharm' } },
            'Returned HealthcareService does not have pharmacy category'
        end
      end
    end

    test do
      id :pharmacy_specialty_search 
      title 'Server handles HealthcareService specialty search'
      description 'Verify search by specialty returns pharmacy services'

      run do
        fhir_search(:healthcareservice, params: {
          specialty: 'pharmacy'
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_bundle_response_type(:searchset)

        resources = resource.entry&.map(&:resource)
        assert resources.present?, 'No HealthcareService resources returned'

        resources.each do |service|
          assert service.specialty.any? { |s| s.coding.any? { |code| code.code.include?('pharm') } },
            'Returned HealthcareService does not have pharmacy specialty'
        end
      end
    end

    test do
      id :pharmacy_location_search
      title 'Server handles pharmacy search with location qualification'
      description 'Verify pharmacy search qualified by location'
      input :location_id
      
      run do
        fhir_search(:healthcareservice, params: {
          category: 'pharm',
          location: location_id
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_bundle_response_type(:searchset)

        resources = resource.entry&.map(&:resource)
        assert resources.present?, 'No HealthcareService resources returned'

        resources.each do |service|
          assert service.location.any? { |loc| loc.reference.include?(location_id) },
            'Returned HealthcareService not associated with specified location'
        end
      end
    end

    test do
      id :pharmacy_network_search
      title 'Server handles pharmacy search with network qualification'
      description 'Verify pharmacy search qualified by network'
      input :network_id
      
      run do
        fhir_search(:healthcareservice, params: {
          category: 'pharm',
          network: network_id
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_bundle_response_type(:searchset)

        resources = resource.entry&.map(&:resource)
        assert resources.present?, 'No HealthcareService resources returned'

        resources.each do |service|
          assert service.network.any? { |net| net.reference.include?(network_id) },
            'Returned HealthcareService not associated with specified network'
        end
      end
    end
  end
end