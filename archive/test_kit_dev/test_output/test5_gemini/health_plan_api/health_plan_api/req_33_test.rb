module Test5Gemini
  class ProviderSearchByNameTest < Inferno::TestGroup
    id :req_33_provider_search_by_name
    title 'REQ-33: Provider Search by Name'
    description %(
      Verify that the Plan-Net server supports searching for Practitioner resources by name.
    )

    test do
      id :provider_search_by_name
      title 'Server returns results for Practitioner search by name'
      description %(
        The Plan-Net design requires support for searching Practitioner resources by name.
        This test searches for Practitioners named 'Joe Smith' and validates the response.
      )
      input :server_url

      run do
        fhir_client = FHIR::Client.new(server_url)

        search_params = {
          _summary: 'true',
          name: 'Joe Smith'
        }

        response = fhir_client.search('Practitioner', search: { parameters: search_params })

        assert_response_status(200)
        assert_resource_type('Bundle', response.resource)
        assert_valid_resource(resource: response.resource)

        # Further assertions can be added to validate:
        # - Presence of search parameters in the response Bundle
        # - Number of returned entries based on test data
        # - Content of returned Practitioner resources
      end
    end
  end
end