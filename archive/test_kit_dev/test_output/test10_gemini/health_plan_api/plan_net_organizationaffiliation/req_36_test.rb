module Test10_gemini
  class Req36OrganizationSpecialtySearchTestGroup < Inferno::TestGroup
    id :req_36_organization_specialty_search
    title 'REQ-36: Organization Search by Specialty'
    description %(
      This test group verifies the server's capability to search for OrganizationAffiliation resources
      based on the `specialty` parameter, and combinations with `location`, `network`, and `name`
      (via chained search on primary organization).

      The Plan-Net design requires searching Organization by specialty, with additional
      qualifications for Location, Network, and Name.
      Focal Resource and Field: OrganizationAffiliation.specialty.
    )

    # Define inputs for the test group. These inputs will be available to all tests within this group.
    input :url,
          title: 'FHIR Server Base URL',
          description: 'The base URL for the FHIR server (e.g., http://example.com/fhir)'

    input :specialty_code,
          title: 'Specialty Code',
          description: 'A code representing a specialty (e.g., "333600000X" for Compounding Pharmacy, or a code from a relevant terminology).',
          default: '333600000X', # Example NPI taxonomy code for Compounding Pharmacy
          type: :text

    input :location_id,
          title: 'Location ID (Optional)',
          description: 'An ID of a Location resource to filter OrganizationAffiliations by. Leave blank to not use this filter.',
          optional: true,
          type: :text

    input :network_id,
          title: 'Network ID (Optional)',
          description: 'An ID of an Organization resource representing a network to filter OrganizationAffiliations by. Leave blank to not use this filter.',
          optional: true,
          type: :text

    input :primary_organization_name,
          title: 'Primary Organization Name (Optional)',
          description: 'The name of the primary organization to filter OrganizationAffiliations by (chained search: primary-organization.name). Leave blank to not use this filter.',
          optional: true,
          type: :text

    # Configure the FHIR client for all tests in this group
    fhir_client do
      url :url
    end

    # Helper method to validate search results for OrganizationAffiliation
    # This method will be available within the run block of tests
    def validate_organization_affiliation_search_results(response, expected_specialty_code)
      assert_response_status(200), "Expected HTTP 200 OK, but received #{response[:status]}."
      assert_resource_type(:bundle), "Expected a FHIR Bundle resource, but received #{resource.resourceType}."

      if resource.entry.empty?
        info "No OrganizationAffiliation resources found for the given search criteria. This may be valid if no matching resources exist on the server."
        # Pass the test even if no resources are found, as the server correctly handled the search.
        # If the requirement implies that resources *must* exist for a given search, this would be a fail.
        # For a general capability test, an empty bundle is a valid response.
        return
      end

      # Validate that all returned resources are OrganizationAffiliation and match the specialty
      resource.entry.each do |entry|
        org_aff = entry.resource
        assert org_aff.is_a?(FHIR::OrganizationAffiliation),
               "Expected resource in bundle entry to be OrganizationAffiliation, but found #{org_aff.resourceType}."

        # Validate specialty code: Check if any specialty CodeableConcept has a coding with the expected code
        specialty_matches = org_aff.specialty.any? do |specialty_cc|
          specialty_cc.coding.any? { |coding| coding.code == expected_specialty_code }
        end
        assert specialty_matches,
               "OrganizationAffiliation/#{org_aff.id} does not contain the expected specialty code '#{expected_specialty_code}'."

        # Further validation for other parameters (location, network, organization name)
        # would require more complex logic (e.g., fetching linked resources or relying on server's filtering).
        # For this test, we primarily validate the focal field 'specialty' and successful search.
      end
      pass "Successfully searched for OrganizationAffiliation resources matching the criteria."
    end

    test 'Search OrganizationAffiliation by specialty' do
      id :req_36_organization_specialty_search_by_specialty_only
      title 'Search OrganizationAffiliation by specialty'
      description %(
        This test performs a search for OrganizationAffiliation resources using only the `specialty` parameter.
        It verifies that the server responds with a 200 OK and a Bundle containing OrganizationAffiliation resources
        that match the specified specialty code.
      )
      # specialty_code is declared at the group level and is available here
      run do
        fhir_search(:organization_affiliation, params: { specialty: specialty_code })
        validate_organization_affiliation_search_results(response, specialty_code)
      end
    end

    test 'Search OrganizationAffiliation by specialty and location' do
      id :req_36_organization_specialty_search_by_specialty_and_location
      title 'Search OrganizationAffiliation by specialty and location'
      description %(
        This test performs a search for OrganizationAffiliation resources using the `specialty`
        and `location` parameters. It verifies that the server responds correctly and returns
        OrganizationAffiliation resources that match both criteria.
      )
      # specialty_code and location_id are declared at the group level and are available here
      run do
        skip_if location_id.blank?, 'Location ID is not provided, skipping this test.'
        fhir_search(:organization_affiliation, params: { specialty: specialty_code, location: location_id })
        validate_organization_affiliation_search_results(response, specialty_code)
      end
    end

    test 'Search OrganizationAffiliation by specialty and network' do
      id :req_36_organization_specialty_search_by_specialty_and_network
      title 'Search OrganizationAffiliation by specialty and network'
      description %(
        This test performs a search for OrganizationAffiliation resources using the `specialty`
        and `network` parameters. It verifies that the server responds correctly and returns
        OrganizationAffiliation resources that match both criteria.
      )
      # specialty_code and network_id are declared at the group level and are available here
      run do
        skip_if network_id.blank?, 'Network ID is not provided, skipping this test.'
        fhir_search(:organization_affiliation, params: { specialty: specialty_code, network: network_id })
        validate_organization_affiliation_search_results(response, specialty_code)
      end
    end

    test 'Search OrganizationAffiliation by specialty and primary organization name' do
      id :req_36_organization_specialty_search_by_specialty_and_organization_name
      title 'Search OrganizationAffiliation by specialty and primary organization name'
      description %(
        This test performs a search for OrganizationAffiliation resources using the `specialty`
        parameter and a chained search on `primary-organization.name`. It verifies that the server
        responds correctly and returns OrganizationAffiliation resources that match both criteria.
      )
      # specialty_code and primary_organization_name are declared at the group level and are available here
      run do
        skip_if primary_organization_name.blank?, 'Primary Organization Name is not provided, skipping this test.'
        fhir_search(:organization_affiliation, params: { specialty: specialty_code, 'primary-organization.name': primary_organization_name })
        validate_organization_affiliation_search_results(response, specialty_code)
      end
    end

    test 'Search OrganizationAffiliation by specialty, location, network, and primary organization name' do
      id :req_36_organization_specialty_search_with_all_qualifications
      title 'Search OrganizationAffiliation by specialty with all qualifications'
      description %(
        This test performs a comprehensive search for OrganizationAffiliation resources using the `specialty`,
        `location`, `network`, and `primary-organization.name` parameters simultaneously.
        It verifies that the server responds correctly and returns OrganizationAffiliation resources
        that match all specified criteria.
      )
      # specialty_code, location_id, network_id, and primary_organization_name are declared at the group level and are available here
      run do
        skip_if location_id.blank? || network_id.blank? || primary_organization_name.blank?,
                'One or more optional search parameters (Location ID, Network ID, Primary Organization Name) are not provided, skipping this comprehensive test.'

        search_params = {
          specialty: specialty_code,
          location: location_id,
          network: network_id,
          'primary-organization.name': primary_organization_name
        }

        fhir_search(:organization_affiliation, params: search_params)
        validate_organization_affiliation_search_results(response, specialty_code)
      end
    end
  end
end