module Test5_claude
  class UnauthorizedRequestResponseGroup < Inferno::TestGroup
    id :unauthorized_request_response
    title 'Unauthorized Request Response Test'
    description %(
      Verify that the server returns appropriate 401/4xx status codes for 
      unauthorized requests as specified in REQ-13.
      
      The server SHALL return a 401 or other 4xx status code when receiving
      an unauthorized request.
    )

    test do
      id :unauthorized_request_test
      title 'Server returns 401/4xx for unauthorized request'
      description %(
        This test verifies that the server properly handles unauthorized requests
        by returning an appropriate 401 or 4xx status code response.
      )

      input :server_url
      
      run do
        # Make request without authorization
        fhir_client.set_no_auth
        
        # Attempt to read Patient resource without auth
        get "#{server_url}/Patient"

        assert_response_status([401, 403, 404])

        assert_response_headers_include('WWW-Authenticate')

        # Verify response body contains OperationOutcome
        assert_resource_type(:operation_outcome)
        
        outcome = resource
        
        assert outcome.issue&.any? { |issue| issue.severity == 'error' },
          'OperationOutcome should contain error severity issue'

        assert outcome.issue&.any? { |issue| issue.code == 'security' },
          'OperationOutcome should contain security issue code'
      end
    end
  end
end