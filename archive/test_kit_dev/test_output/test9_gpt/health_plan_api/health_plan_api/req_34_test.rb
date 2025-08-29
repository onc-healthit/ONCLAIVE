module Test9Gpt
  class OrganizationSearchByNameGroup < Inferno::TestGroup
    id :organization_search_by_name_group
    title 'Organization Search by Name'
    description %(
      This test verifies that the Health Plan API supports searching for 
      Organization resources by name, as described in the Plan-Net design.
      The search should return relevant organizations such as "Montgomery Cardiology" or "CVS".
    )

    input :organization_name,
          title: 'Organization Name',
          description: 'The name of the organization to search for'

    fhir_client do
      url :url
    end

    test do
      id :organization_search_by_name
      title 'Search for Organization by Name'
      description %(
        The server should support searching for Organization resources by the name field.
        This test will search for organizations matching the provided name and verify the response.
      )

      run do
        fhir_search(:organization, params: { name: organization_name })

        assert_response_status(200)
        assert_resource_type(:bundle)

        assert resource.entry.present?, "No Organization resources returned for the search by name: #{organization_name}"

        organization_names = resource.entry.map { |entry| entry.resource.name }
        assert organization_names.any? { |name| name.include?(organization_name) },
               "No Organization resource found with name including: #{organization_name}"
      end
    end
  end
end