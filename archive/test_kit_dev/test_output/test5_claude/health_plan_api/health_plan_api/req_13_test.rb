module Test5_claude
  class UnauthorizedRequestTest < Inferno::TestGroup
    id :unauthorized_request_test
    title 'Unauthorized Request Response Test'
    description %(
      Verify that the server returns appropriate 401/4xx response codes
      for unauthorized requests as required by REQ-13.
      
      The test attempts to access protected resources without valid
      authentication credentials and validates that a 401 Unauthorized
      or appropriate 4xx response is returned.
    )

    test do
      id :unauthorized_fhir_request
      title 'Server returns 401/4xx for unauthorized requests'
      description %(
        Make requests without authorization tokens and verify 401/4xx response.
      )
      
      # Define server URL input
      input :server_url

      run do
        # Create FHIR client without auth credentials
        fhir_client = FHIR::Client.new(server_url)
        fhir_client.use_r4

        # Make request that requires auth
        response = fhir_client.read(FHIR::Patient, 'example')

        assert_response_status([401, 403, 404])

        assert response.response[:code].start_with?('4'),
               'Expected 4xx status code for unauthorized request'

        # Validate error OperationOutcome if present
        if response.resource.is_a?(FHIR::OperationOutcome)
          assert response.resource.issue&.any? { |issue| issue.severity == 'error' },
                 'OperationOutcome should contain error severity issue'
        end

        pass "Server correctly returned #{response.response[:code]} status for unauthorized request"
      end
    end

    test do
      id :invalid_token_request  
      title 'Server returns 401 for invalid token'
      description %(
        Make requests with invalid authorization token and verify 401 response.
      )

      input :server_url

      run do
        fhir_client = FHIR::Client.new(server_url)
        fhir_client.use_r4
        fhir_client.set_bearer_token('INVALID_TOKEN')

        response = fhir_client.read(FHIR::Patient, 'example')

        assert_response_status(401)

        assert response.resource.is_a?(FHIR::OperationOutcome),
               'Response should contain OperationOutcome'

        pass 'Server correctly returned 401 status for invalid token'
      end
    end
  end
end