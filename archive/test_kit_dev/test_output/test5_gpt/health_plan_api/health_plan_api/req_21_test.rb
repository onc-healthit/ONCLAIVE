module Test5Gpt
  class ForwardChainingSupportTestGroup < Inferno::TestGroup
    id :req_21_forward_chaining_support
    title 'Forward Chaining Support'
    description %(
      This test group verifies that the Health Plan API supports forward chaining
      on all search parameters that specify the 'chain' property, as required by REQ-21.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :forward_chaining_support_test
      title 'Support forward chaining on search parameters'
      description %(
        Verify that the server supports forward chaining on search parameters
        that specify the 'chain' property. This involves performing a search
        that utilizes chaining and ensuring the response is valid and correct.
      )
      input :resource_type, :search_param, :chain_param, :chain_value

      run do
        # Construct the search query with chaining
        search_params = { "#{search_param}.#{chain_param}": chain_value }
        
        # Perform the search
        reply = fhir_search(resource_type, params: search_params)

        # Assert the response is successful
        assert_response_status(200)
        assert_bundle_response

        # Validate that the resources in the response match the expected criteria
        resources = reply.resource.entry.map(&:resource)
        assert resources.any?, 'No resources returned from the search'

        resources.each do |resource|
          # Validate the chained parameter in each resource
          related_resource = resource.send(search_param)
          assert related_resource.present?, "Expected resource to have #{search_param} but it was not found"
          
          # Check if the chained parameter matches the expected value
          assert related_resource.any? { |rel| rel.send(chain_param) == chain_value },
                 "Expected at least one related resource to have #{chain_param} equal to #{chain_value}"
        end
      end
    end
  end
end