module Test6_claude
  class InvalidParameterResponseGroup < Inferno::TestGroup
    id :invalid_parameter_response
    title 'Invalid Parameter Response Test'
    description %(
      Verify that the Health Plan API returns a Status 400 response 
      when an invalid parameter is provided.

      Requirement: REQ-15
      Conformance: SHALL
    )

    test do
      id :invalid_parameter_test
      title 'Server returns 400 status for invalid parameter'
      description %(
        This test verifies that the server properly returns a 400 Bad Request
        status code when an invalid parameter is included in the request.
      )

      # Define test inputs
      input :base_url, 
        title: 'Health Plan API Endpoint',
        description: 'Base URL for the Health Plan API'

      run do
        # Make request with invalid parameter
        fhir_client.set_url("#{base_url}?invalid_param=test")

        get fhir_client.url
        
        assert_response_status(400)

        assert_valid_json(response[:body])
        
        # Verify error response has proper structure
        error = JSON.parse(response[:body])
        assert error['resourceType'] == 'OperationOutcome', 
          'Response body should be an OperationOutcome resource'

        assert error['issue'].present?, 
          'OperationOutcome should contain issue element'

        assert error['issue'].first['severity'] == 'error',
          'Issue severity should be error'

        assert error['issue'].first['code'] == 'invalid',
          'Issue code should indicate invalid parameter'
      end
    end
  end
end