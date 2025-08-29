module Test5Gemini
  class OrganizationSearchByNameTest < Inferno::TestGroup
    id :req_34_organization_search_by_name
    title 'REQ-34: Organization Search by Name'
    description %(
      Verify that the server supports searching for Organization resources by name.

      This test is based on the Plan-Net design requirement that specifies support for searching
      organizations by name, with optional qualifications for location, network, and specialty.

      This test does not enforce any specific conformance requirements but validates the design requirement.
    )

    test do
      id :organization_search_by_name
      title 'Server returns Organization resources matching search by name'
      description %(
        Search for Organization resources by name and validate that the server returns the appropriate resources.
      )
      input :search_name,
            title: 'Organization Name',
            description: 'The name of the organization to search for',
            optional: false

      run do
        fhir_search(:organization, params: { name: search_name })

        assert_response_status(200)
        assert_resource_type(:organization)
        assert_bundle_response

        # Additional assertions can be added here to validate:
        # - The presence of specific organizations in the search results
        # - The number of returned results
        # - The content of the returned Organization resources
      end
    end
  end
end