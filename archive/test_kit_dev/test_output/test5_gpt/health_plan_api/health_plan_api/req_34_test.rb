module Test5Gpt
  class OrganizationSearchByNameTest < Inferno::TestGroup
    id :req_34_organization_search_by_name
    title 'Organization Search by Name'
    description %(
      This test verifies that the Health Plan API supports searching for 
      organizations by name. It checks that the search functionality is 
      implemented correctly for the Organization resource using the 
      Organization.name field.
    )

    input :server_url, :access_token, :organization_name

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :organization_search_by_name
      title 'Search Organization by Name'
      description %(
        The server should support searching for organizations by name. 
        This test performs a search on the Organization resource using 
        the name parameter and verifies the response.
      )

      run do
        fhir_search(:organization, params: { name: organization_name })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_resource

        organizations = resource.entry.map(&:resource)
        assert organizations.any?, 'No organizations were returned from the search'

        organizations.each do |organization|
          assert organization.name.downcase.include?(organization_name.downcase),
                 "Expected organization name to include '#{organization_name}', but found '#{organization.name}'"
        end
      end
    end
  end
end