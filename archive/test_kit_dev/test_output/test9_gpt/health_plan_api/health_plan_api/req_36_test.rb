module Test9Gpt
  class OrganizationSearchBySpecialtyGroup < Inferno::TestGroup
    id :organization_search_by_specialty_group
    title 'Organization Search by Specialty'
    description %(
      This group of tests verifies that the Health Plan API supports searching
      for organizations by specialty. Specifically, it checks that the API can
      return organizations with a given specialty, such as a Compounding Pharmacy,
      using the OrganizationAffiliation.specialty field.
    )

    input :organization_specialty,
          title: 'Organization Specialty',
          description: 'The specialty to search for in organizations, e.g., Compounding Pharmacy'

    fhir_client do
      url :url
    end

    test do
      id :organization_search_by_specialty
      title 'Search for organizations by specialty'
      description %(
        This test searches for organizations by the specified specialty using the
        OrganizationAffiliation.specialty field. It verifies that the server returns
        a bundle of OrganizationAffiliation resources that match the search criteria.
      )

      run do
        fhir_search(:organization_affiliation, params: { specialty: organization_specialty })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, "No OrganizationAffiliation resources returned for specialty: #{organization_specialty}"

        resource.entry.each do |entry|
          affiliation = entry.resource
          assert affiliation.specialty.any? { |s| s.coding.any? { |coding| coding.display == organization_specialty } },
                 "OrganizationAffiliation does not have the expected specialty: #{organization_specialty}"
        end
      end
    end
  end
end