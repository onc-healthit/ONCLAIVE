module Test5_claude
  class InvalidParameterResponseTest < Inferno::TestGroup
    id :invalid_parameter_response
    title 'Invalid Parameter Response Test'
    description %(
      Verify that the server returns an appropriate error response (Status 400)
      when invalid parameters are provided in the request.

      The server SHALL return a 400 Bad Request status code when request
      parameters are invalid.
    )

    test do
      id :invalid_parameter_test
      title 'Server returns 400 status for invalid parameter'
      description %(
        This test verifies that the server returns a HTTP 400 status code
        when an invalid parameter is included in the request.
      )

      # Base FHIR server URL needed for requests
      input :url
      
      run do
        # Make request with invalid parameter
        fhir_client.set_no_auth
        fhir_client.url = url

        # Use obviously invalid parameter value
        get_request = "#{url}/Patient?_invalid=xyz123"
        
        response = fhir_client.raw_client.get(get_request)

        assert_response_status(400)

        assert_valid_json(response.body)
        
        outcome = FHIR.from_contents(response.body)
        
        assert outcome.is_a?(FHIR::OperationOutcome), 
          'Server response body should be an OperationOutcome resource'

        assert outcome.issue&.any? { |issue| issue.severity == 'error' },
          'OperationOutcome should contain at least one error issue'

        assert outcome.issue&.any? { |issue| 
          issue.code == 'invalid' || 
          issue.code == 'structure' ||
          issue.code == 'required'
        }, 'OperationOutcome should indicate invalid parameter'
      end
    end
  end
end