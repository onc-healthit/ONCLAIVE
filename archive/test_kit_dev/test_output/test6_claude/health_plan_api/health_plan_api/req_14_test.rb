module Test6_claude
  class InsufficientScopeResponseGroup < Inferno::TestGroup
    id :insufficient_scope_response
    title 'REQ-14: Insufficient Scope Response'
    description %(
      Verify that the server returns a 403 Forbidden status code when the request
      is made with insufficient OAuth scopes. This tests the server's ability to
      properly handle and respond to requests with inadequate authorization.
    )

    test do
      id :insufficient_scope_test
      title 'Server returns 403 response for insufficient scope'
      description %(
        This test verifies that the server returns a 403 Forbidden status code
        when a request is made with insufficient OAuth scopes.
      )
      
      input :patient_id
      input :bearer_token_insufficient_scope, 
            title: 'Bearer Token with Insufficient Scope',
            description: 'Access token that has insufficient scopes'

      fhir_client do
        url :url
        bearer_token :bearer_token_insufficient_scope
      end

      run do
        fhir_operation = fhir_read(:patient, patient_id)

        assert_response_status(403)

        assert_resource_type(:operationoutcome)
        
        outcome = fhir_operation.resource

        assert outcome.issue&.any? { |issue| 
          issue.severity == 'error' && 
          issue.code == 'forbidden'
        }, 'Expected OperationOutcome to contain error issue with forbidden code'

        pass "Server correctly returned 403 Forbidden status for insufficient scope"
      end
    end
  end
end