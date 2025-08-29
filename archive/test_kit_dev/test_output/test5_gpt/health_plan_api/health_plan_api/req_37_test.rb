module Test5Gpt
  class ActivePractitionersAndOrganizationsTestGroup < Inferno::TestGroup
    id :req_37_active_practitioners_and_organizations
    title 'REQ-37: Search for Active Practitioners and Organizations'
    description %(
      This test group verifies that the Health Plan API can search for currently active Practitioners and Organizations
      using the specified FHIR search queries. The test will replace the date in the query with the current date to ensure
      the search is for active entities.
    )

    fhir_client do
      url :server_url
    end

    test do
      id :active_practitioners_search_test
      title 'Search for Active Practitioners'
      description %(
        This test checks if the server can search for currently active Practitioners using the PractitionerRole resource.
        The date parameter in the query is replaced with the current date.
      )
      input :server_url

      run do
        current_date = Date.today.strftime('%Y-%m-%d')
        search_params = { '_include' => 'PractitionerRole:date', 'date' => "ge#{current_date}" }
        
        reply = fhir_search(:PractitionerRole, params: search_params)
        
        assert_response_status(200)
        assert_bundle_response
        assert reply.resource.entry.any?, 'No active Practitioners found'
      end
    end

    test do
      id :active_organizations_search_test
      title 'Search for Active Organizations'
      description %(
        This test checks if the server can search for currently active Organizations using the OrganizationAffiliation resource.
        The date parameter in the query is replaced with the current date.
      )
      input :server_url

      run do
        current_date = Date.today.strftime('%Y-%m-%d')
        search_params = { '_include' => 'OrganizationAffiliation:date', 'date' => "ge#{current_date}" }
        
        reply = fhir_search(:OrganizationAffiliation, params: search_params)
        
        assert_response_status(200)
        assert_bundle_response
        assert reply.resource.entry.any?, 'No active Organizations found'
      end
    end
  end
end