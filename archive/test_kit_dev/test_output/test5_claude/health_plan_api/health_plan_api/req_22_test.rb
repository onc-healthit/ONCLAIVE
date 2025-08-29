module Test5_claude
  class ReverseChainingSupportTest < Inferno::TestGroup
    id :reverse_chaining_support
    title 'Reverse Chaining Support'
    description %(
      This test verifies that the server supports reverse chaining on all search 
      parameters that specify the 'chain' property, as required by REQ-22.
      
      The test will:
      1. Query the server's CapabilityStatement
      2. Identify search parameters that support chaining
      3. Test reverse chaining queries using those parameters
    )

    test do
      id :capability_statement_chain_parameters
      title 'CapabilityStatement indicates search parameters supporting chains'
      description %(
        Verify the server's CapabilityStatement includes search parameters
        that specify support for chaining.
      )

      run do
        fhir_get_capability_statement

        assert_response_status(200)
        capability_statement = resource

        search_params_with_chain = []
        
        capability_statement.rest.each do |rest|
          rest.resource.each do |resource|
            resource.searchParam&.each do |param|
              if param.chain.present?
                search_params_with_chain << {
                  resource: resource.type,
                  parameter: param.name,
                  chains: param.chain
                }
              end
            end
          end
        end

        assert search_params_with_chain.present?, 
          'No search parameters with chain support found in CapabilityStatement'

        output search_params_with_chain: search_params_with_chain
      end
    end

    test do
      id :reverse_chain_search_execution
      title 'Execute reverse chain searches'
      description %(
        Test reverse chaining functionality for each identified search parameter
        that supports chaining.
      )
      input :search_params_with_chain
      
      run do
        search_params = input[:search_params_with_chain]
        
        search_params.each do |param_def|
          resource_type = param_def[:resource] 
          param_name = param_def[:parameter]
          
          # Execute reverse chain search
          search_string = "_has:#{resource_type}:#{param_name}"
          fhir_search(resource_type, params: { search_string => 'test-value' })
          
          assert_response_status([200, 201])
          assert_resource_type(:bundle)
          assert_valid_bundle_entries
          
          bundle = resource
          
          if bundle.total == 0
            info "No results found for reverse chain search on #{resource_type}.#{param_name}"
          end
        end

        pass "Successfully tested reverse chaining on #{search_params.length} search parameters"
      end
    end

    def assert_valid_bundle_entries
      bundle = resource
      bundle.entry&.each do |entry|
        assert entry.resource.present?, "Bundle entry missing resource"
        assert entry.resource.resourceType.present?, "Resource missing resourceType"
      end
    end
  end
end