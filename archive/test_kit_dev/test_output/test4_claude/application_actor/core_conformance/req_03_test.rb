module Test4_claude
  class NoConsumerInfoQueryGroup < Inferno::TestGroup
    id :no_consumer_info_query
    title 'No Consumer Information in Queries'
    description %(
      Requirement REQ-03: Application Actor SHALL NOT send consumer identifiable 
      information when querying a Plan-Net service.
      
      This test verifies that queries do not contain any consumer identifiable 
      information in the parameters or payloads.
    )

    test do
      id :search_with_consumer_info
      title 'Search should fail when consumer info included'
      description %(
        This test verifies that the client correctly rejects attempts to include
        consumer identifiable information in search parameters.
      )
      
      input :server_url

      run do
        # Test searching with consumer identifiable info
        search_params = {
          'patient' => 'Patient/123',
          'member' => '12345',
          'subscriber' => '98765'
        }

        search_params.each do |param, value|
          fhir_operation do
            operation_name :search
            resource_type :Organization
            client do
              url server_url
            end
            params { param => value }
          end

          assert_response_status([400, 422], "Server should reject search with #{param} parameter")
          
          # Verify error response indicates consumer info not allowed
          assert_resource_type(:OperationOutcome)
          assert resource.issue&.any? { |issue|
            issue.severity == 'error' && 
            issue.code == 'processing' &&
            issue.details&.text&.match(/consumer|patient|member|subscriber/i)
          }, "OperationOutcome should indicate consumer info not allowed in #{param} parameter"
        end

        pass "Server correctly rejected queries containing consumer identifiable information"
      end
    end

    test do
      id :valid_search_no_consumer_info  
      title 'Search succeeds without consumer info'
      description %(
        This test verifies that valid searches without consumer information
        are processed successfully.
      )

      input :server_url

      run do
        # Test valid search without consumer info
        fhir_operation do
          operation_name :search
          resource_type :Organization
          client do
            url server_url
          end
          params(
            'active' => 'true',
            'type' => 'prov'
          )
        end

        assert_response_status(200)
        assert_resource_type(:Bundle)
        assert_valid_resource

        pass "Server successfully processed query without consumer identifiable information"
      end
    end
  end
end