module Test6_claude
  class ProviderSearchByNameGroup < Inferno::TestGroup
    id :provider_search_by_name
    title 'Provider Search by Name'
    description %(
      Verify that the server supports searching for providers by name, including:
      - Basic name search on Practitioner.name
      - Search refinements by location, network, specialty, and role/privileges
      - Proper handling of search parameters and results
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :basic_name_search
      title 'Basic Provider Name Search'
      description 'Verify basic name search functionality on Practitioner.name'
      input :practitioner_name
      
      run do
        fhir_search(:practitioner, params: {name: practitioner_name})
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert bundle.entry.length.positive?, 'No practitioners returned in search results'
        
        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Practitioner', 
                 "Expected Practitioner resources but found #{entry.resource.resourceType}"
          
          assert entry.resource.name.any? { |name| 
            name.text&.downcase&.include?(practitioner_name.downcase) ||
            name.given&.any? { |given| given.downcase.include?(practitioner_name.downcase) } ||
            name.family&.downcase&.include?(practitioner_name.downcase)
          }, "Practitioner name does not match search criteria"
        end
      end
    end

    test do
      id :refined_name_search 
      title 'Provider Name Search with Refinements'
      description 'Verify name search with location, network, specialty and role refinements'
      input :practitioner_name
      input :location_id, optional: true
      input :network_id, optional: true
      input :specialty_code, optional: true
      input :role_code, optional: true

      run do
        search_params = {name: practitioner_name}
        
        search_params[:location] = location_id if location_id.present?
        search_params['network'] = network_id if network_id.present?
        search_params['specialty'] = specialty_code if specialty_code.present?
        search_params['role'] = role_code if role_code.present?

        fhir_search(:practitioner, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        skip_if bundle.entry.empty?, 'No practitioners found matching refined criteria'

        bundle.entry.each do |entry|
          practitioner = entry.resource
          assert practitioner.resourceType == 'Practitioner'

          # Verify name matches
          assert practitioner.name.any? { |name| 
            name.text&.downcase&.include?(practitioner_name.downcase) ||
            name.given&.any? { |given| given.downcase.include?(practitioner_name.downcase) } ||
            name.family&.downcase&.include?(practitioner_name.downcase)
          }, "Practitioner name does not match search criteria"

          # Verify location if specified
          if location_id.present?
            assert practitioner.location&.any? { |loc| loc.reference.end_with?(location_id) },
                   "Practitioner not associated with specified location"
          end

          # Verify network if specified  
          if network_id.present?
            assert practitioner.qualification&.any? { |qual| 
              qual.extension&.any? { |ext| 
                ext.url == 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/network' &&
                ext.valueReference.reference.end_with?(network_id)
              }
            }, "Practitioner not in specified network"
          end

          # Verify specialty if specified
          if specialty_code.present?
            assert practitioner.qualification&.any? { |qual|
              qual.code.coding&.any? { |coding| coding.code == specialty_code }
            }, "Practitioner does not have specified specialty"
          end

          # Verify role if specified
          if role_code.present?
            assert practitioner.qualification&.any? { |qual|
              qual.code.coding&.any? { |coding| coding.code == role_code }
            }, "Practitioner does not have specified role"
          end
        end
      end
    end
  end
end