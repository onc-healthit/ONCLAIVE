module Test6_claude
  class OrganizationNameSearchTest < Inferno::TestGroup
    id :organization_name_search
    title 'Organization Search by Name'
    description %(
      Verify that the server supports searching Organization resources by name.
      This test focuses on validating the Organization.name search parameter 
      functionality as specified in Plan-Net.

      The search should support partial matches of organization names like
      "Montgomery Cardiology" or "CVS" and return appropriate Organization resources.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :organization_name_exact_match
      title 'Server returns matching organizations when searching by exact name'
      description %(
        This test verifies that the server properly handles Organization searches
        using an exact organization name.
      )
      
      input :known_organization_name,
            title: 'Known Organization Name',
            description: 'Enter the exact name of an organization known to exist on the server'

      run do
        fhir_search(:organization, params: {name: known_organization_name})
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert bundle.entry.length.positive?, 'No Organizations returned for exact name search'
        
        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Organization', 
                 "Non-Organization resource returned: #{entry.resource.resourceType}"
          assert entry.resource.name&.downcase&.include?(known_organization_name.downcase),
                 "Returned organization name '#{entry.resource.name}' does not match search '#{known_organization_name}'"
        end
      end
    end

    test do
      id :organization_name_partial_match
      title 'Server returns matching organizations when searching by partial name'
      description %(
        This test verifies that the server properly handles Organization searches
        using a partial organization name.
      )

      input :partial_org_name,
            title: 'Partial Organization Name',
            description: 'Enter a partial name to search for (e.g., "card" for cardiology practices)'

      run do
        fhir_search(:organization, params: {name: partial_org_name})
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        skip_if bundle.entry.empty?, 'No Organizations returned for partial name search'
        
        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Organization',
                 "Non-Organization resource returned: #{entry.resource.resourceType}"
          assert entry.resource.name&.downcase&.include?(partial_org_name.downcase),
                 "Returned organization name '#{entry.resource.name}' does not contain search term '#{partial_org_name}'"
        end
      end
    end

    test do
      id :organization_name_no_match
      title 'Server returns appropriate response for non-matching organization name'
      description %(
        This test verifies that the server returns an empty Bundle when searching
        for an organization name that should not exist.
      )

      run do
        random_name = "NonExistentOrg#{rand(1000000)}"
        fhir_search(:organization, params: {name: random_name})
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert bundle.entry.empty?, 
               "Expected empty Bundle for non-existent organization name, but found #{bundle.entry.length} entries"
      end
    end
  end
end