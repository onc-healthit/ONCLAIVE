module Test6_claude
  class UnauthorizedResponseTest < Inferno::TestGroup
    id :unauthorized_response_test
    title 'Unauthorized Request Response'
    description %(
      Verify that the server returns appropriate 401/4xx status codes for 
      unauthorized requests as required by REQ-13.
      
      The server SHALL return a 401 Unauthorized response when:
      * No authentication credentials are provided
      * Invalid authentication credentials are provided
    )

    test do
      id :no_auth_credentials_test
      title 'Server returns 401 when no auth credentials provided'
      description %(
        Verify that the server returns HTTP 401 when a request is made
        without any authentication credentials.
      )

      run do
        # Clear any existing auth to ensure clean test
        client.set_bearer_token(nil)
        
        # Make request without auth
        fhir_read(:patient, '123')

        assert_response_status(401)
        assert_response_content_type('application/fhir+json')
        
        error = JSON.parse(response[:body])
        assert error['resourceType'] == 'OperationOutcome', 
          'Response body should be an OperationOutcome resource'
      end
    end

    test do
      id :invalid_auth_credentials_test 
      title 'Server returns 401 when invalid auth credentials provided'
      description %(
        Verify that the server returns HTTP 401 when a request is made
        with invalid authentication credentials.
      )

      run do
        # Set invalid bearer token
        client.set_bearer_token('INVALID_TOKEN')
        
        # Make request with invalid auth
        fhir_read(:patient, '123')

        assert_response_status(401)
        assert_response_content_type('application/fhir+json')

        error = JSON.parse(response[:body])
        assert error['resourceType'] == 'OperationOutcome',
          'Response body should be an OperationOutcome resource'
      end
    end

  end
end