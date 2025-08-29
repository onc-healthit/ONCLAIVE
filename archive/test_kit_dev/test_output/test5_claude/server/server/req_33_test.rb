module Test5_claude
  class ProviderSearchByNameGroup < Inferno::TestGroup
    id :provider_search_by_name
    title 'Provider Search by Name'
    description %(
      Verify that the server supports searching for providers by name, including:
      - Searching Practitioner resources by name
      - Optional qualification parameters (location, network, specialty, role/privileges)
      
      Based on REQ-33: Provider search by name requirement.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :basic_name_search
      title 'Server supports basic Practitioner name search'
      description %(
        Verify that the server properly handles searching for Practitioners by name
        using the name search parameter.
      )
      
      input :practitioner_name
      
      run do
        fhir_search(:practitioner, params: {name: practitioner_name})
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert bundle.entry.length.positive?, 'No Practitioners returned'
        
        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Practitioner', 
            "Non-Practitioner resource returned: #{entry.resource.resourceType}"
          
          practitioner = entry.resource
          name_matches = practitioner.name.any? do |name|
            full_name = [
              name.given&.join(' '),
              name.family
            ].compact.join(' ').downcase
            
            full_name.include?(practitioner_name.downcase)
          end
          
          assert name_matches, "Returned Practitioner name does not match search criteria"
        end
      end
    end

    test do
      id :qualified_name_search 
      title 'Server supports qualified Practitioner name search'
      description %(
        Verify that the server properly handles Practitioner name searches 
        with additional qualifying parameters.
      )
      
      input :practitioner_name
      input :location_id, optional: true
      input :network_id, optional: true
      input :specialty_code, optional: true
      
      run do
        skip_if location_id.nil? && network_id.nil? && specialty_code.nil?,
          'No qualifying parameters provided to test'
          
        search_params = {name: practitioner_name}
        search_params[:location] = location_id if location_id.present?
        search_params['primary-network'] = network_id if network_id.present?
        search_params[:specialty] = specialty_code if specialty_code.present?
        
        fhir_search(:practitioner, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        if bundle.entry.present?
          bundle.entry.each do |entry|
            assert entry.resource.resourceType == 'Practitioner',
              "Non-Practitioner resource returned: #{entry.resource.resourceType}"
              
            practitioner = entry.resource
            
            # Verify name match
            name_matches = practitioner.name.any? do |name|
              full_name = [
                name.given&.join(' '),
                name.family
              ].compact.join(' ').downcase
              
              full_name.include?(practitioner_name.downcase)
            end
            
            assert name_matches, "Returned Practitioner name does not match search criteria"
            
            # Verify qualifiers if provided
            if specialty_code.present?
              has_specialty = practitioner.qualification&.any? do |q|
                q.code&.coding&.any? { |c| c.code == specialty_code }
              end
              assert has_specialty, "Practitioner does not have specified specialty"
            end
          end
        else
          pass "No practitioners found matching all criteria (this is valid)"
        end
      end
    end
  end
end