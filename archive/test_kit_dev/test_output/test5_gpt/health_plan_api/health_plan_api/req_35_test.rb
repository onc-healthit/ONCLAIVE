module Test5Gpt
  class ProviderSearchBySpecialtyTestGroup < Inferno::TestGroup
    id :req_35_provider_search_by_specialty
    title 'Provider Search by Specialty'
    description %(
      This test group verifies that the Health Plan API supports searching for providers by specialty.
      It specifically tests the ability to search for a provider with the specialty of 'Cardiologist'
      using the PractitionerRole.specialty field, with optional search parameters such as location, network, and name.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :provider_search_by_specialty_test
      title 'Search for providers by specialty'
      description %(
        This test searches for providers with the specialty 'Cardiologist' using the PractitionerRole resource.
        It checks that the search returns valid results and that the PractitionerRole.specialty field is correctly populated.
      )
      input :server_url, :access_token, :specialty_code, :location, :network, :name

      run do
        params = {
          specialty: specialty_code,
          location: location,
          network: network,
          name: name
        }.compact

        reply = fhir_search(:PractitionerRole, params: params)

        assert_response_status(200)
        assert_bundle_response

        entries = reply.resource.entry
        assert entries.any?, 'No PractitionerRole resources were returned'

        entries.each do |entry|
          practitioner_role = entry.resource
          assert practitioner_role.resourceType == 'PractitionerRole', 'Expected resource type to be PractitionerRole'
          assert practitioner_role.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } }, 
                 "PractitionerRole does not have the expected specialty code #{specialty_code}"
        end
      end
    end
  end
end