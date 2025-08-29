module Test10Gpt
  class Req37TestGroup < Inferno::TestGroup
    id :req_37_test_group
    title 'REQ-37: Search for Active Practitioners and Organizations'
    description %(
      This test group verifies the ability to search for currently active Practitioners and Organizations
      using the FHIR API. It includes tests for searching active PractitionerRole and OrganizationAffiliation
      resources with a date parameter.
    )

    input :server_url,
          title: 'FHIR Server URL',
          description: 'The base URL for the FHIR server'

    fhir_client do
      url :server_url
    end

    test do
      id :search_active_practitioner_role
      title 'Search for Active PractitionerRole'
      description %(
        This test searches for active PractitionerRole resources using the date parameter.
        It verifies that the server returns a valid Bundle of PractitionerRole resources.
      )
      input :current_date, title: 'Current Date', default: Date.today.to_s

      run do
        fhir_search(:PractitionerRole, params: { 'date' => "ge#{current_date}" })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No PractitionerRole resources returned for the active search.'
      end
    end

    test do
      id :search_active_organization_affiliation
      title 'Search for Active OrganizationAffiliation'
      description %(
        This test searches for active OrganizationAffiliation resources using the date parameter.
        It verifies that the server returns a valid Bundle of OrganizationAffiliation resources.
      )
      input :current_date, title: 'Current Date', default: Date.today.to_s

      run do
        fhir_search(:OrganizationAffiliation, params: { 'date' => "ge#{current_date}" })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No OrganizationAffiliation resources returned for the active search.'
      end
    end
  end
end