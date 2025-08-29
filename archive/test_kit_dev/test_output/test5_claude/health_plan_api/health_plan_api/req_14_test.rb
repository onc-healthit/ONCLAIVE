module Test5_claude
  class InsufficientScopeResponseGroup < Inferno::TestGroup
    id :insufficient_scope_response_test
    title 'REQ-14: Insufficient Scope Response'
    description %(
      Verify that the server returns a 403 Forbidden response when 
      a request is made with insufficient scope.
      
      The Health Plan API SHALL return a 403 status code when the 
      provided access token does not have sufficient scope to 
      access the requested resource.
    )

    test do
      id :verify_insufficient_scope_response
      title 'Server returns 403 for insufficient scope'
      description %(
        This test verifies that the server returns a 403 Forbidden response
        when making a request with an access token that has insufficient scope.
      )

      input :patient_id
      input :insufficient_scope_token, 
            title: 'Access Token with Insufficient Scope',
            description: 'An access token that does not have sufficient scope'

      run do
        fhir_client.set_bearer_token(insufficient_scope_token)

        fhir_operation = fhir_read(:patient, patient_id)

        assert_response_status(403)

        assert_valid_json(fhir_operation.response[:body])
        
        error_response = JSON.parse(fhir_operation.response[:body])
        
        assert error_response['resourceType'] == 'OperationOutcome', 
               'Response body should be an OperationOutcome resource'

        assert error_response['issue']&.any? { |issue| 
          issue['code'] == 'forbidden' 
        }, 'OperationOutcome should contain issue with code "forbidden"'
      end
    end
  end
end