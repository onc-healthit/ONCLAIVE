module Test6_claude
  class OrganizationSearchBySpecialtyGroup < Inferno::TestGroup
    id :organization_search_by_specialty
    title 'Organization Search by Specialty Tests'
    description %(
      Verify that the server supports searching Organizations by specialty via 
      OrganizationAffiliation.specialty, including support for optional qualifiers
      like location, network, and name.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :organization_search_specialty_basic
      title 'Server returns results when searching Organizations by specialty'
      description %(
        Verify that searching OrganizationAffiliation resources by specialty returns
        expected results. Tests basic specialty search without additional qualifiers.
      )
      
      input :specialty_code
      
      run do
        fhir_search(:organizationaffiliation, params: {
          specialty: specialty_code
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_bundle_response_type(:searchset)
        
        skip_if bundle.total == 0, 'No OrganizationAffiliation resources found for the given specialty'
        
        bundle.entry.each do |entry|
          resource = entry.resource
          assert resource.specialty&.any? { |s| s.coding&.any? { |c| c.code == specialty_code }},
            "Resource #{resource.id} does not have expected specialty code #{specialty_code}"
        end
      end
    end

    test do
      id :organization_search_specialty_qualified
      title 'Server supports qualified Organization specialty searches'
      description %(
        Verify that searching OrganizationAffiliation resources by specialty with
        additional qualifiers for location, network and name returns valid results.
      )
      
      input :specialty_code
      input :location_id, optional: true
      input :network_id, optional: true 
      input :org_name, optional: true
      
      run do
        search_params = {
          specialty: specialty_code
        }
        
        search_params[:location] = location_id if location_id.present?
        search_params[:network] = network_id if network_id.present?
        search_params[:organization_name] = org_name if org_name.present?

        fhir_search(:organizationaffiliation, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_bundle_response_type(:searchset)
        
        skip_if bundle.total == 0, 'No OrganizationAffiliation resources found matching search criteria'

        bundle.entry.each do |entry|
          resource = entry.resource
          
          assert resource.specialty&.any? { |s| s.coding&.any? { |c| c.code == specialty_code }},
            "Resource #{resource.id} does not have expected specialty code #{specialty_code}"

          if location_id.present?
            assert resource.location&.any? { |loc| loc.reference.include?(location_id) },
              "Resource #{resource.id} is not associated with location #{location_id}"
          end

          if network_id.present?
            assert resource.network&.any? { |net| net.reference.include?(network_id) },
              "Resource #{resource.id} is not associated with network #{network_id}"
          end

          if org_name.present?
            org_reference = resource.organization&.reference
            skip_unless org_reference.present?, 'Resource has no organization reference'
            
            org = fhir_read(:organization, org_reference.split('/').last).resource
            assert org.name&.downcase&.include?(org_name.downcase),
              "Organization name '#{org.name}' does not match search criteria '#{org_name}'"
          end
        end
      end
    end
  end
end