module Test5Gemini
  class OrganizationSearchBySpecialtyTest < Inferno::Test
    id :req_36_organization_search_by_specialty
    title 'Organization search by specialty'
    description %(
      Verify that the server supports searching for Organizations by specialty.
    )

    input :search_specialty,
          title: 'Specialty Code',
          description: 'The code for the specialty to search for',
          optional: false

    run do
      skip_if search_specialty.blank?, 'No specialty code provided.'

      search_params = {
        specialty: search_specialty
      }

      reply = fhir_search(:organization, search_params)

      assert_response_status(200)
      assert_bundle_response(reply)

      # Additional assertions can be added here to validate
      # the content of the returned Organization resources,
      # such as checking for the presence of the specified specialty
      # in the OrganizationAffiliation.specialty field.
    end
  end
end
