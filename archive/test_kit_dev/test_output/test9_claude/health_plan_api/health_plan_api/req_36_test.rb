module Test9_claude
  class OrganizationSpecialtySearchGroup < Inferno::TestGroup
    id :organization_specialty_search
    title 'Organization Search by Specialty Tests'
    description %(
      Verify that the server supports searching OrganizationAffiliation resources by specialty,
      optionally including Location, network, and name parameters.
    )

    input :url,
          title: 'FHIR Server Base URL',
          description: 'Base URL for the FHIR server'

    input :specialty_code,
          title: 'Specialty Code',
          description: 'Code representing the specialty to search for (e.g. "compounding-pharmacy")'
    
    input :location_id,
          title: 'Location ID',
          description: 'Optional Location resource ID to filter results',
          optional: true

    input :network_id, 
          title: 'Network ID',
          description: 'Optional network resource ID to filter results',
          optional: true

    input :organization_name,
          title: 'Organization Name',
          description: 'Optional organization name to filter results',
          optional: true

    fhir_client do
      url :url
    end

    test do
      id :organization_specialty_basic_search
      title 'Server supports OrganizationAffiliation search by specialty'
      description %(
        Verify that the server supports searching OrganizationAffiliation resources 
        by specialty using the specialty search parameter.
      )
      
      makes_request :specialty_search
      
      run do
        fhir_search(:organizationaffiliation, params: {specialty: specialty_code}, name: :specialty_search)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No OrganizationAffiliation resources returned'
        
        resource.entry.each do |entry|
          assert entry.resource.specialty.present?, 
                 'Returned OrganizationAffiliation is missing specialty'
          assert entry.resource.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code }},
                 "Returned OrganizationAffiliation specialty does not match search criteria: #{specialty_code}"
        end
      end
    end

    test do
      id :organization_specialty_combined_search
      title 'Server supports combined OrganizationAffiliation search parameters'
      description %(
        Verify that the server supports searching OrganizationAffiliation resources
        by specialty combined with optional location, network and name parameters.
      )
      
      makes_request :combined_search
      
      run do
        search_params = {specialty: specialty_code}
        
        search_params[:location] = location_id if location_id.present?
        search_params[:network] = network_id if network_id.present?
        search_params['organization.name'] = organization_name if organization_name.present?

        fhir_search(:organizationaffiliation, params: search_params, name: :combined_search)
        
        assert_response_status(200)
        assert_resource_type(:bundle)

        if resource.entry.present?
          resource.entry.each do |entry|
            org = entry.resource
            
            assert org.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code }},
                   "Returned OrganizationAffiliation specialty does not match search criteria"

            if location_id.present?
              assert org.location.any? { |loc| loc.reference.include?(location_id) },
                     "Returned OrganizationAffiliation location does not match search criteria"
            end

            if network_id.present?
              assert org.network.any? { |net| net.reference.include?(network_id) },
                     "Returned OrganizationAffiliation network does not match search criteria"
            end

            if organization_name.present?
              org_ref = org.organization.reference
              fhir_read(:organization, org_ref.split('/').last)
              assert_response_status(200)
              assert resource.name&.downcase&.include?(organization_name.downcase),
                     "Referenced Organization name does not match search criteria"
            end
          end
        end
      end
    end
  end
end