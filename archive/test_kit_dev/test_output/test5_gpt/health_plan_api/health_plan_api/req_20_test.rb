module Test5Gpt
  class CombinationSearchParameterSupportTestGroup < Inferno::TestGroup
    id :req_20_combination_search_parameter_support
    title 'Combination Search Parameter Support'
    description %(
      This test group verifies that the Health Plan API supports the combination
      of search parameters on each profile as required by REQ-20.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :combination_search_parameter_support_test
      title 'Server supports combination of search parameters'
      description %(
        Verify that the server supports searching with a combination of search
        parameters for a specific resource type.
      )
      input :resource_type, :search_params

      run do
        skip_if search_params.blank?, 'No search parameters provided'
        
        response = fhir_search(resource_type, params: search_params)
        
        assert_response_status(200)
        assert_valid_resource

        resources = response.resource.entry.map(&:resource)
        assert resources.any?, 'No resources were returned from the search'

        # Additional assertions can be added here to validate specific search parameter behavior
      end
    end
  end
end