require 'date' # Required for Date.today.iso8601

module Test10_gemini
  class Req37SearchActivePractitionersOrganizationsTestGroup < Inferno::TestGroup
    id :req_37_search_active_practitioners_organizations
    title 'REQ-37: Search for active Practitioners and Organizations'
    description %(
      This test group verifies the ability of the FHIR server to search for currently active
      PractitionerRole and OrganizationAffiliation resources.

      The test implements the logic described in REQ-37, which involves searching
      for resources active on or after the current date.

      **Note on Sample Query Interpretation:**
      The provided sample queries in the specification (`_include=PractitionerRole:date=ge2021-10-25`
      and `_include=OrganizationAffiliation:date=ge2021-10-25`) appear to misuse the `_include`
      parameter. `_include` is intended for including referenced resources, not for filtering
      the primary resource by a direct parameter like `date`.

      This implementation interprets the intent as searching for `PractitionerRole` and
      `OrganizationAffiliation` resources directly using the `date` search parameter
      (e.g., `PractitionerRole?date=ge<current_date>`). This is the standard and correct
      FHIR search pattern for filtering by date.
    )

    # Declare inputs required for the tests in this group
    input :url,
          title: 'FHIR Server Base URL',
          description: 'The base URL for the FHIR server (e.g., http://davinci-plan-net-ri.logicahealth.org/fhir)',
          type: 'text'

    # Configure the FHIR client for this group. All tests within this group will
    # inherit this client configuration.
    fhir_client do
      url :url
    end

    test do
      id :req_37_search_active_practitioner_roles
      title 'Search for active PractitionerRole resources by date'
      description %(
        This test performs a FHIR search on the `PractitionerRole` resource type
        to find active roles based on the current date. It uses the `date` search
        parameter with the `ge` (greater than or equal) prefix.

        The test verifies:
        1. The server responds with a 200 OK status.
        2. The response body is a FHIR Bundle resource.
        3. The Bundle contains at least one PractitionerRole entry.
      )

      run do
        # Get the current date in YYYY-MM-DD format for the 'date' search parameter.
        current_date = Date.today.iso8601

        # Perform the FHIR search for PractitionerRole resources.
        # The 'date' parameter is used to filter for resources active on or after the current date.
        fhir_search(:practitioner_role, params: { date: "ge#{current_date}" })

        # Assertions to validate the response
        assert_response_status(200), "Expected HTTP 200 OK, but received #{response[:status]}." \
                                     "Response body: #{response[:body]}"
        assert_resource_type(:bundle), "Expected a FHIR Bundle resource, but received '#{resource.resourceType}'." \
                                      "Response body: #{response[:body]}"

        # Check if the bundle contains any entries. An empty bundle would indicate no active
        # PractitionerRoles found, which might be a valid scenario for some servers, but for
        # a test of search capability, we expect results.
        assert resource.entry.present?,
               "No PractitionerRole resources found for date >= #{current_date}. " \
               "This may indicate no active PractitionerRoles in the server's data or an issue with the search."

        # Further validation: Ensure that all entries in the bundle are indeed PractitionerRole resources.
        resource.entry.each_with_index do |entry, index|
          assert entry.resource.resourceType == 'PractitionerRole',
                 "Bundle entry #{index + 1} expected resource type 'PractitionerRole', but found '#{entry.resource.resourceType}'."
        end

        info "Successfully searched for active PractitionerRole resources. Found #{resource.entry.length} entries."
      end
    end

    test do
      id :req_37_search_active_organization_affiliations
      title 'Search for active OrganizationAffiliation resources by date'
      description %(
        This test performs a FHIR search on the `OrganizationAffiliation` resource type
        to find active affiliations based on the current date. It uses the `date` search
        parameter with the `ge` (greater than or equal) prefix.

        The test verifies:
        1. The server responds with a 200 OK status.
        2. The response body is a FHIR Bundle resource.
        3. The Bundle contains at least one OrganizationAffiliation entry.
      )

      run do
        # Get the current date in YYYY-MM-DD format for the 'date' search parameter.
        current_date = Date.today.iso8601

        # Perform the FHIR search for OrganizationAffiliation resources.
        # The 'date' parameter is used to filter for resources active on or after the current date.
        fhir_search(:organization_affiliation, params: { date: "ge#{current_date}" })

        # Assertions to validate the response
        assert_response_status(200), "Expected HTTP 200 OK, but received #{response[:status]}." \
                                     "Response body: #{response[:body]}"
        assert_resource_type(:bundle), "Expected a FHIR Bundle resource, but received '#{resource.resourceType}'." \
                                      "Response body: #{response[:body]}"

        # Check if the bundle contains any entries.
        assert resource.entry.present?,
               "No OrganizationAffiliation resources found for date >= #{current_date}. " \
               "This may indicate no active OrganizationAffiliations in the server's data or an issue with the search."

        # Further validation: Ensure that all entries in the bundle are indeed OrganizationAffiliation resources.
        resource.entry.each_with_index do |entry, index|
          assert entry.resource.resourceType == 'OrganizationAffiliation',
                 "Bundle entry #{index + 1} expected resource type 'OrganizationAffiliation', but found '#{entry.resource.resourceType}'."
        end

        info "Successfully searched for active OrganizationAffiliation resources. Found #{resource.entry.length} entries."
      end
    end
  end
end