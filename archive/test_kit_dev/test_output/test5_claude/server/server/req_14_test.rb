module Test5_claude
  class InsufficientScopeResponseGroup < Inferno::TestGroup
    id :insufficient_scope_response
    title 'REQ-14: Insufficient Scope Response'
    description %(
      Verify that the server returns a 403 Forbidden status code when
      the request is made with insufficient scope.
      
      The server SHALL return a 403 status code in this scenario.
    )

    test do
      id :insufficient_scope_test
      title 'Server returns 403 for insufficient scope'
      description %(
        This test verifies that the server properly returns a 403 Forbidden
        response when a request is made with insufficient authorization scope.
      )

      input :server_url
      input :patient_id
      input :limited_scope_token, 
            title: 'Limited Scope Token',
            description: 'An access token with deliberately insufficient scope'

      run do
        fhir_client.set_bearer_token(limited_scope_token)

        fhir_operation = ->() do
          fhir_read(:patient, patient_id)
        end

        result = run_request(fhir_operation)

        assert_response_status(403)
        
        assert_resource_type(:operationoutcome)
        
        outcome = resource

        assert outcome.issue&.any? { |issue| 
          issue.code == 'forbidden' && 
          issue.severity == 'error'
        }, 'OperationOutcome should indicate forbidden access due to insufficient scope'

        # Reset client token
        fhir_client.set_bearer_token(nil)
      end
    end
  end
end