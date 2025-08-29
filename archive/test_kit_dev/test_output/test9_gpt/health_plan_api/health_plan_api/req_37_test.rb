module Test9Gpt
  class Req37TestGroup < Inferno::TestGroup
    id :req_37_test_group
    title 'REQ-37: Search for Active Practitioners and Organizations'
    description %(
      This group of tests verifies the ability to search for currently active Practitioners and Organizations
      using the specified FHIR search queries. The tests ensure that the server can handle these queries
      and return the expected results.
    )

    input :base_url,
          title: 'FHIR Server Base URL',
          description: 'The base URL for the FHIR server'

    fhir_client do
      url :base_url
    end

    test do
      id :search_active_practitioners
      title 'Search for Active Practitioners'
      description %(
        This test performs a search for currently active Practitioners using the PractitionerRole resource.
        The search query includes a date parameter to filter active roles.
      )

      run do
        current_date = Date.today.to_s
        fhir_search(:PractitionerRole, params: { 'date' => "ge#{current_date}" })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.any?, 'No active PractitionerRole resources were returned'
      end
    end

    test do
      id :search_active_organizations
      title 'Search for Active Organizations'
      description %(
        This test performs a search for currently active Organizations using the OrganizationAffiliation resource.
        The search query includes a date parameter to filter active affiliations.
      )

      run do
        current_date = Date.today.to_s
        fhir_search(:OrganizationAffiliation, params: { 'date' => "ge#{current_date}" })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.any?, 'No active OrganizationAffiliation resources were returned'
      end
    end
  end
end