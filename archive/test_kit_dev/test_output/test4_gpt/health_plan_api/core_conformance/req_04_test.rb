module Test4Gpt
  class MustSupportElementsPopulationTestGroup < Inferno::TestGroup
    id :req_04_must_support_elements_population
    title 'Must Support Elements Population'
    description %(
      Health Plan API SHALL populate all Must Support data elements in query results.
      This test verifies that all Must Support elements are present in the resources returned
      by the Health Plan API.
    )

    input :server_url, :access_token, :resource_type, :query_params

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :must_support_elements_population_test
      title 'Verify Must Support elements are populated'
      description %(
        This test checks that all Must Support elements are populated in the resources
        returned by the Health Plan API for the specified resource type.
      )

      run do
        # Perform a FHIR search for the specified resource type with given query parameters
        reply = fhir_search(resource_type.to_sym, params: query_params)

        assert_response_status(200)
        assert_bundle_response

        must_support_elements = [
          # List of Must Support elements for the specified resource type
          # Example: 'name', 'identifier', 'telecom'
        ]

        resources = reply.resource.entry.map(&:resource)
        skip_if resources.empty?, "No resources of type #{resource_type} were returned."

        resources.each do |resource|
          must_support_elements.each do |element|
            assert resource[element].present?, "Must Support element '#{element}' is missing in the resource."
          end
        end

        pass "All Must Support elements are populated in the returned resources."
      end
    end
  end
end