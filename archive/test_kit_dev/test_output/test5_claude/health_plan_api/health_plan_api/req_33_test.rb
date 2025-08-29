module Test5_claude
  class ProviderSearchByNameGroup < Inferno::TestGroup
    id :provider_search_by_name
    title 'Provider Search by Name Tests'
    description %(
      Verify that the system supports searching for providers by name,
      including proper handling of search qualifications like location,
      network, specialty, and role/privileges.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :basic_practitioner_name_search
      title 'Search Practitioner by name'
      description %(
        Verify that the system supports searching for Practitioners by name
        using the name search parameter.
      )
      
      input :practitioner_name
      
      run do
        fhir_search(:practitioner, params: {name: practitioner_name})
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
        
        bundle = resource

        skip_if bundle.total == 0, "No Practitioners found matching name '#{practitioner_name}'"
        
        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Practitioner', 
                 "Expected Practitioner resources but found #{entry.resource.resourceType}"
          
          practitioner = entry.resource
          assert practitioner.name.any? { |name| 
            name.text&.downcase&.include?(practitioner_name.downcase) ||
            name.given&.any? { |given| given.downcase.include?(practitioner_name.downcase) } ||
            name.family&.downcase&.include?(practitioner_name.downcase)
          }, "Practitioner name does not match search criteria"
        end
      end
    end

    test do
      id :qualified_practitioner_name_search 
      title 'Search Practitioner by name with qualifications'
      description %(
        Verify that the system supports searching for Practitioners by name
        with additional qualification parameters (location, network, specialty, role).
      )

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
        assert_valid_bundle_entries

        bundle = resource

        skip_if bundle.total == 0, 'No Practitioners found matching search criteria'

        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Practitioner',
                 "Expected Practitioner resources but found #{entry.resource.resourceType}"
          
          practitioner = entry.resource
          
          # Verify name matches
          assert practitioner.name.any? { |name| 
            name.text&.downcase&.include?(practitioner_name.downcase) ||
            name.given&.any? { |given| given.downcase.include?(practitioner_name.downcase) } ||
            name.family&.downcase&.include?(practitioner_name.downcase)
          }, "Practitioner name does not match search criteria"

          # Additional qualification validations could be added here based on
          # specific implementation requirements for location, network, specialty
          # and role relationships
        end
      end
    end
  end
end