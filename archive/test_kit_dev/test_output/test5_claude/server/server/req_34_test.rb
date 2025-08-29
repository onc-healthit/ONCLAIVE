module Test5_claude
  class OrganizationSearchByNameGroup < Inferno::TestGroup
    id :organization_search_by_name
    title 'Organization Search by Name'
    description %(
      Verify that the server supports searching Organization resources by name.
      
      The Plan-Net design requires Organization resources to be searchable by:
      * Organization.name (Example: "Montgomery Cardiology" or "CVS")
      * Results should reflect Location, network, and specialty qualifications
    )

    test do
      id :organization_name_search
      title 'Server returns matching organizations when searching by name'
      description %(
        Perform a search for Organizations using the name parameter and validate
        that matching organizations are returned correctly.
      )
      
      input :organization_name,
            title: 'Organization Name',
            description: 'Name of organization to search for'

      run do
        fhir_search(:organization, params: {name: organization_name})

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.present?, 'No Organizations returned in search Bundle'
        
        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Organization', 
                "Expected resource type to be Organization but found #{entry.resource.resourceType}"
          
          org = entry.resource
          assert org.name.present?, 'Organization resource must have a name'
          
          name_matches = org.name.downcase.include?(organization_name.downcase)
          assert name_matches, "Organization name '#{org.name}' does not match search criteria '#{organization_name}'"
        end

        pass "Successfully searched Organizations by name '#{organization_name}' and validated #{bundle.entry.length} matching results"
      end
    end

    test do
      id :organization_name_no_match 
      title 'Server handles Organization name search with no matches appropriately'
      description %(
        Verify server returns appropriate empty results when searching for
        an Organization name that should not exist.
      )

      run do
        search_name = "NOTAREALORG#{rand(1000000)}"
        fhir_search(:organization, params: {name: search_name})

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource
        assert bundle.entry.blank?, 
              "Expected no results for non-existent organization name but found #{bundle.entry.length} entries"

        pass "Server correctly returned empty results for non-matching organization name search"
      end
    end
  end
end