module Test10Gpt
  class ProviderSearchBySpecialtyGroup < Inferno::TestGroup
    id :req_35_provider_search_by_specialty
    title 'REQ-35: Provider Search by Specialty'
    description %(
      This test group verifies that the Health Plan API supports searching for providers by specialty.
      The focal resource and field for this search is PractitionerRole.specialty.
      The search should be qualified by location, network, and name.
    )

    input :base_url, 
          title: 'FHIR Server Base URL',
          description: 'The base URL for the FHIR server'
    input :specialty, 
          title: 'Specialty',
          description: 'The specialty to search for'
    input :location, 
          title: 'Location',
          description: 'The location to search for'
    input :network, 
          title: 'Network',
          description: 'The network to search for'
    input :name, 
          title: 'Name',
          description: 'The name to search for'

    fhir_client do
      url :base_url
    end

    test do
      id :provider_search_by_specialty
      title 'Search for providers by specialty'
      description %(
        This test searches for providers by the specified specialty.
        It verifies that the server returns a valid response and that the PractitionerRole resources
        returned match the search criteria.
      )

      run do
        fhir_search(:practitioner_role, params: { specialty: specialty, location: location, network: network, name: name })

        assert_response_status(200)
        assert_resource_type(:bundle)

        entries = resource.entry || []
        assert entries.any?, 'No PractitionerRole resources returned for the specified search criteria.'

        entries.each do |entry|
          practitioner_role = entry.resource
          assert practitioner_role.resourceType == 'PractitionerRole', 'Returned resource is not a PractitionerRole.'
          assert practitioner_role.specialty.any? { |s| s.coding.any? { |c| c.code == specialty } }, 'PractitionerRole does not have the expected specialty.'
        end
      end
    end
  end
end