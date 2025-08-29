module Test5_claude
  class OrganizationSearchByNameTest < Inferno::TestGroup
    id :organization_search_by_name
    title 'Organization Search by Name'
    description %(
      Verify that the server supports searching Organization resources by name.
      This test focuses on searching Organizations using the name parameter to find matching
      organizations like "Montgomery Cardiology" or "CVS".

      The test verifies:
      * Searching organizations using exact name matches
      * Proper handling of the name search parameter
      * Return of valid Organization resources
    )

    test do
      id :organization_name_search
      title 'Server returns matching organizations when searching by name'
      description %(
        This test verifies that the server properly handles Organization searches
        using the name parameter and returns matching Organization resources.
      )

      # Define test inputs
      input :organization_name,
            title: 'Organization Name',
            description: 'Name of organization to search for (e.g. "Montgomery Cardiology")'

      # Define FHIR client
      fhir_client do
        url :url
        bearer_token :bearer_token
      end

      run do
        # Perform search by name
        fhir_search(:organization, params: {name: organization_name})

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource

        assert bundle.entry.present?, 'No Organization resources returned in Bundle'
        
        # Verify each returned resource
        bundle.entry.each do |entry|
          org = entry.resource
          assert org.is_a?(FHIR::Organization), 'Non-Organization resource returned'
          assert_valid_resource(resource: org)
          
          # Verify name matches search parameter
          assert org.name.present?, 'Organization resource missing name element'
          assert org.name.downcase.include?(organization_name.downcase), 
                 "Organization name '#{org.name}' does not match search parameter '#{organization_name}'"
        end

        pass "Successfully searched for and validated Organizations with name '#{organization_name}'"
      end
    end

    test do
      id :organization_name_no_matches
      title 'Server handles Organization name search with no matches'
      description %(
        This test verifies the server properly handles Organization name
        searches that should return no results.
      )

      fhir_client do
        url :url
        bearer_token :bearer_token
      end

      run do
        search_name = 'NONEXISTENT_ORGANIZATION_NAME_123'
        fhir_search(:organization, params: {name: search_name})

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource
        
        assert bundle.entry.blank?, 
               "Expected no results for nonexistent organization name but got #{bundle.entry.length} entries"

        pass "Server correctly returned empty results for nonexistent organization name"
      end
    end
  end
end