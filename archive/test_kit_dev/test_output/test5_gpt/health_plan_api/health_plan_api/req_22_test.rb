module Test5Gpt
  class ReverseChainingSupportTestGroup < Inferno::TestGroup
    id :req_22_reverse_chaining_support
    title 'Reverse Chaining Support'
    description %(
      This test group verifies that the Health Plan API supports reverse chaining
      on all search parameters that specify the 'chain' property, as required by REQ-22.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :reverse_chaining_support_test
      title 'Server supports reverse chaining on search parameters'
      description %(
        This test checks if the server supports reverse chaining on search parameters
        that specify the 'chain' property. It performs a search using a reverse chaining
        parameter and verifies the response.
      )
      input :resource_type, :search_parameter, :chain_value

      run do
        # Perform a search using reverse chaining
        search_params = { "_has:#{resource_type}:#{search_parameter}:#{chain_value}" => 'value' }
        reply = fhir_search(resource_type.to_sym, params: search_params)

        # Assert that the response is successful and contains the expected resource type
        assert_response_status(200)
        assert_resource_type(resource_type.to_sym)

        # Validate the resources in the response
        resources = reply.resource.entry.map(&:resource)
        resources.each do |resource|
          assert resource.is_a?(FHIR.const_get(resource_type)), "Expected resource to be of type #{resource_type}, but found #{resource.class.name}"
        end

        pass "Server supports reverse chaining on search parameters for #{resource_type}."
      end
    end
  end
end