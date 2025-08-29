module Test5_claude
  class ReverseChainingSupportGroup < Inferno::TestGroup
    id :reverse_chaining_support
    title 'Reverse Chaining Support'
    description %(
      Verify that the server supports reverse chaining on all search parameters 
      that specify the 'chain' property. This test validates REQ-22 which requires
      servers to support reverse chaining capabilities.
    )

    SEARCH_PARAMS_WITH_CHAIN = {
      'Observation': ['subject'],
      'Condition': ['subject'],
      'Procedure': ['subject']
    }

    test do
      id :reverse_chain_capability_statement
      title 'Server capability statement declares reverse chain support'
      description 'Verify server capability statement includes reverse chain support'
      
      run do
        fhir_get_capability_statement

        assert_response_status(200)
        capability_statement = FHIR.from_contents(response[:body])
        
        SEARCH_PARAMS_WITH_CHAIN.each do |resource_type, chain_params|
          resource = capability_statement.rest.first.resource
            .find { |r| r.type == resource_type.to_s }

          assert resource.present?, 
            "Capability statement must declare support for #{resource_type}"

          chain_params.each do |param|
            search_param = resource.searchParam
              .find { |sp| sp.name == param }
            
            assert search_param&.chain.present?,
              "#{resource_type} search parameter '#{param}' must declare chain support"
          end
        end
      end
    end

    test do
      id :reverse_chain_search
      title 'Server supports reverse chain searches'
      description 'Verify server can execute reverse chain searches'
      
      run do
        SEARCH_PARAMS_WITH_CHAIN.each do |resource_type, chain_params|
          chain_params.each do |param|
            # Example reverse chain: /Patient?_has:Observation:subject:code=123
            search_params = {
              '_has': "#{resource_type}:#{param}:code=unknown-test-code"
            }
            
            fhir_search(:patient, params: search_params)
            
            assert_response_status([200, 404]),
              "Server returned unexpected status #{response.status} for reverse chain search"

            if response.status == 200
              assert_resource_type(:bundle)
              assert_valid_bundle_entries
            end
          end
        end
      end
    end

    test do
      id :reverse_chain_error_handling
      title 'Server handles invalid reverse chain parameters appropriately' 
      description 'Verify server returns appropriate errors for invalid reverse chain queries'

      run do
        # Test with invalid resource type
        search_params = {
          '_has': 'InvalidResource:subject:code=123'
        }
        fhir_search(:patient, params: search_params)
        assert_response_status(400)

        # Test with invalid chain parameter
        search_params = {
          '_has': 'Observation:invalid:code=123'  
        }
        fhir_search(:patient, params: search_params)
        assert_response_status(400)

        # Test with invalid format
        search_params = {
          '_has': 'invalid_format'
        }
        fhir_search(:patient, params: search_params)
        assert_response_status(400)
      end
    end

    def assert_valid_bundle_entries
      bundle = FHIR.from_contents(response[:body])
      assert bundle.entry.present?, 'Bundle must contain entries'
      bundle.entry.each do |entry|
        assert entry.resource.present?, 'Bundle entry must contain resource'
        assert_valid_resource(resource: entry.resource)
      end
    end

  end
end