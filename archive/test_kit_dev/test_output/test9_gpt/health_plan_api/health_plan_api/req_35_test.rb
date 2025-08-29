module Test9Gpt
  class ProviderSearchBySpecialtyGroup < Inferno::TestGroup
    id :req_35_provider_search_by_specialty
    title 'Provider Search by Specialty'
    description %(
      This test group verifies that the Health Plan API supports searching for providers by specialty.
      The focal resource and field for this search is PractitionerRole.specialty.
      The search can be qualified by location, network, and name.
    )

    input :provider_specialty,
          title: 'Provider Specialty',
          description: 'The specialty to search for, e.g., Cardiologist',
          type: 'text'

    fhir_client do
      url :server_url
    end

    test do
      id :provider_search_by_specialty
      title 'Search for providers by specialty'
      description %(
        This test performs a search for providers based on the specified specialty.
        It verifies that the server returns a valid Bundle of PractitionerRole resources
        with the specified specialty.
      )

      input :server_url

      run do
        fhir_search(:practitioner_role, params: { specialty: provider_specialty })

        assert_response_status(200)
        assert_resource_type(:bundle)

        entries = resource.entry || []
        assert entries.any?, "No PractitionerRole resources returned for specialty: #{provider_specialty}"

        entries.each do |entry|
          practitioner_role = entry.resource
          assert practitioner_role.is_a?(FHIR::PractitionerRole), 'Resource is not a PractitionerRole'
          assert practitioner_role.specialty.any? { |s| s.text == provider_specialty },
                 "PractitionerRole does not have the specialty: #{provider_specialty}"
        end
      end
    end
  end
end