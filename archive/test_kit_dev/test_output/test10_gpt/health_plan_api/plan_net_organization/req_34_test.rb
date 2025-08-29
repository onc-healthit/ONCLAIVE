module Test10Gpt
  class OrganizationSearchByNameGroup < Inferno::TestGroup
    id :req_34_organization_search_by_name
    title 'Organization Search by Name'
    description %(
      This test group verifies that the Health Plan API supports searching for
      Organization resources by name. The test will attempt to search for
      organizations using example names such as "Montgomery Cardiology" or "CVS"
      and validate that the search results are consistent with the search
      parameters.
    )

    input :organization_name,
          title: 'Organization Name',
          description: 'The name of the organization to search for',
          type: 'text'

    fhir_client do
      url :server_url
    end

    test do
      id :organization_search_by_name
      title 'Search for Organization by Name'
      description %(
        This test performs a search for Organization resources using the
        provided name. It verifies that the server returns a valid Bundle
        of Organization resources and that the resources match the search
        criteria.
      )

      input :server_url

      run do
        fhir_search(:organization, params: { name: organization_name })
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, "No Organization resources returned for name search: #{organization_name}"

        resource.entry.each do |entry|
          organization = entry.resource
          assert organization.name.downcase.include?(organization_name.downcase), 
                 "Organization name '#{organization.name}' does not include search term '#{organization_name}'"
        end
      end
    end
  end
end