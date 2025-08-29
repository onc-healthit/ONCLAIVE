module Test5Gemini
  class Req37ActivePractitionersOrganizationsTest < Inferno::TestGroup
    id :req_37_active_practitioners_organizations
    title 'REQ-37: Search for Active Practitioners and Organizations'
    description %(
      Sample query to search for currently active Practitioners (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/PractitionerRole?_include=PractitionerRole:date=ge2021-10-25. Sample query to search for currently active Organizations (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/OrganizationAffiliation?_include=OrganizationAffiliation:date=ge2021-10-25.
    )

    test do
      id :req_37_search_active_practitioners
      title 'Server returns active PractitionerRole resources'
      description 'Search for PractitionerRole resources with a date parameter greater than or equal to the current date.'

      run do
        current_date = Date.today.strftime('%Y-%m-%d')
        search_params = { '_include' => 'PractitionerRole:date', 'date' => "ge#{current_date}" }
        response = fhir_search(:practitioner_role, search_params)

        assert_response_status(200)
        assert_bundle_response(response)

        # Additional assertions can be added here to validate the response content,
        # such as checking for the presence of active PractitionerRole resources.
      end
    end

    test do
      id :req_37_search_active_organizations
      title 'Server returns active OrganizationAffiliation resources'
      description 'Search for OrganizationAffiliation resources with a date parameter greater than or equal to the current date.'

      run do
        current_date = Date.today.strftime('%Y-%m-%d')
        search_params = { '_include' => 'OrganizationAffiliation:date', 'date' => "ge#{current_date}" }
        response = fhir_search(:organization_affiliation, search_params)

        assert_response_status(200)
        assert_bundle_response(response)

        # Additional assertions can be added here to validate the response content,
        # such as checking for the presence of active OrganizationAffiliation resources.
      end
    end
  end
end