module Test5_claude
  class OrganizationSearchBySpecialtyTest < Inferno::TestGroup
    id :organization_search_by_specialty
    title 'Organization Search by Specialty'
    description %(
      Verify that the server supports searching for Organizations by specialty
      through OrganizationAffiliation.specialty, with optional qualifiers for
      location, network, and name.

      This test validates the Plan-Net requirement for searching Organizations
      by specialty (e.g. Compounding Pharmacy) using OrganizationAffiliation.specialty
      as the focal resource and field.
    )

    test do
      id :search_org_by_specialty_basic
      title 'Server returns results when searching Organizations by specialty'
      description %(
        Verify that a search for Organizations using specialty returns 
        appropriate results. Tests basic specialty search without qualifiers.
      )
      
      input :specialty_code
      
      run do
        fhir_search(:organizationaffiliation, params: {
          specialty: specialty_code
        })
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert bundle.entry.length.positive?, 'No OrganizationAffiliation resources found for the given specialty'
        
        bundle.entry.each do |entry|
          resource = entry.resource
          assert resource.specialty&.any? { |s| s.coding.any? { |c| c.code == specialty_code }},
                 "OrganizationAffiliation #{resource.id} does not have matching specialty code"
        end
      end
    end

    test do
      id :search_org_by_specialty_with_qualifiers 
      title 'Server handles qualified searches by specialty with location and network'
      description %(
        Verify that searching Organizations by specialty works with additional
        qualifiers for location and network.
      )

      input :specialty_code
      input :location_id
      input :network_id
      
      run do
        fhir_search(:organizationaffiliation, params: {
          specialty: specialty_code,
          location: location_id,
          network: network_id
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle.entry.each do |entry|
          resource = entry.resource
          assert resource.specialty&.any? { |s| s.coding.any? { |c| c.code == specialty_code }},
                 "OrganizationAffiliation #{resource.id} does not have matching specialty code"
          
          assert resource.location&.any? { |l| l.reference.include?(location_id) },
                 "OrganizationAffiliation #{resource.id} does not reference specified location"
          
          assert resource.network&.any? { |n| n.reference.include?(network_id) },
                 "OrganizationAffiliation #{resource.id} does not reference specified network"
        end
      end
    end

    test do
      id :search_org_by_specialty_with_name
      title 'Server handles qualified searches by specialty with organization name'
      description %(
        Verify that searching Organizations by specialty works with additional
        qualifier for organization name.
      )

      input :specialty_code
      input :org_name
      
      run do
        fhir_search(:organizationaffiliation, params: {
          specialty: specialty_code,
          'organization.name': org_name
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        skip_if bundle.entry.empty?, 'No matching OrganizationAffiliation resources found'
        
        bundle.entry.each do |entry|
          resource = entry.resource
          assert resource.specialty&.any? { |s| s.coding.any? { |c| c.code == specialty_code }},
                 "OrganizationAffiliation #{resource.id} does not have matching specialty code"
          
          org = fhir_read(:organization, resource.organization.reference.split('/').last).resource
          assert org.name&.downcase&.include?(org_name.downcase),
                 "Organization #{org.id} name does not match search criteria"
        end
      end
    end
  end
end