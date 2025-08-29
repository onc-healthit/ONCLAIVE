module Test5Gpt
  class IndividualSearchParameterSupportTestGroup < Inferno::TestGroup
    id :req_19_individual_search_parameter_support
    title 'Individual Search Parameter Support'
    description %(
      This test group verifies that the Health Plan API supports the searchParameters
      on each profile individually as required by REQ-19.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :individual_search_parameter_support_test
      title 'Support for individual search parameters'
      description %(
        Verify that the server supports individual search parameters for the specified
        FHIR resource type and profile.
      )
      input :resource_type, :search_parameter, :search_value

      run do
        search_params = { search_parameter => search_value }
        reply = fhir_search(resource_type.to_sym, params: search_params)

        assert_response_status(200)
        assert_valid_resource

        resources = reply.resource.entry.map(&:resource)
        assert resources.any?, "No resources found for #{resource_type} with #{search_parameter}=#{search_value}"

        resources.each do |resource|
          assert resource.is_a?(FHIR.const_get(resource_type)), "Expected resource type #{resource_type}, but found #{resource.resourceType}"
        end
      end
    end
  end
end