module Test5Gpt
  class OrganizationSearchBySpecialtyTestGroup < Inferno::TestGroup
    id :req_36_organization_search_by_specialty
    title 'Organization Search by Specialty'
    description %(
      This test group verifies that the Health Plan API supports searching for 
      Organizations by specialty, such as Compounding Pharmacy, using the 
      OrganizationAffiliation.specialty field. The search should be qualified by 
      parameters like Location, network, and name.
    )

    input :server_url, :access_token, :specialty_code

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :organization_search_by_specialty
      title 'Search for Organizations by Specialty'
      description %(
        Verify that the server can perform a search for Organizations using the
        OrganizationAffiliation.specialty field. The test checks if the server 
        returns valid Organization resources when searched with a specific 
        specialty code.
      )

      run do
        skip_if specialty_code.blank?, 'Specialty code is required to perform the search.'

        search_params = { 'specialty' => specialty_code }
        reply = fhir_search(:Organization, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_resource

        organizations = reply.resource.entry.map(&:resource)
        assert organizations.any?, 'No Organizations were returned in the search results.'

        organizations.each do |organization|
          assert organization.is_a?(FHIR::Organization), 'Returned resource is not an Organization.'
          assert organization.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } },
                 "Organization does not have the expected specialty code: #{specialty_code}"
        end
      end
    end
  end
end