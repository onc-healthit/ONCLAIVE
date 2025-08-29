module Test5Gemini
  class ProviderSearchBySpecialtyTest < Inferno::TestGroup
    id :req_35_provider_search_by_specialty
    title 'REQ-35: Provider Search by Specialty'
    description %(
      Verify that the server supports searching for PractitionerRole resources by specialty.
    )

    test do
      id :search_practitioner_role_by_specialty
      title 'Server returns PractitionerRole resources matching search by specialty'
      description %(
        Search for PractitionerRole resources with a specific specialty and validate the search response.
      )
      input :search_specialty

      run do
        skip_if search_specialty.blank?, 'No specialty provided for search.'

        search_params = {
          specialty: search_specialty
        }

        response = fhir_search(:practitioner_role, params: search_params)

        assert_response_status(200)
        assert_bundle_response(response)

        resources = response.resource.entry.map(&:resource)

        assert !resources.empty?, 'No PractitionerRole resources found matching the search criteria.'

        invalid_resources = resources.reject do |resource|
          resource.specialty.any? { |specialty| specialty.coding.any? { |coding| coding.code == search_specialty } }
        end

        assert_empty invalid_resources, 'All returned PractitionerRole resources should have the searched specialty.'
      end
    end
  end
end
