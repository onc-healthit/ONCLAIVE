module Test5_claude
  class InvalidParameterResponseGroup < Inferno::TestGroup
    id :invalid_parameter_response
    title 'Invalid Parameter Response Test'
    description %(
      Validates that the server returns a HTTP 400 status code when an invalid
      parameter is provided in the request.

      Requirement: Server SHALL return a status code of 400 when an invalid
      parameter is included in the request.
    )

    fhir_client do
      url :url
    end

    test do
      id :test_invalid_parameter_response
      title 'Server returns 400 status for invalid parameter'
      description %(
        This test verifies that the server returns a HTTP 400 status code
        when an invalid parameter is included in the request.
      )

      run do
        # Make request with invalid parameter
        fhir_search(:patient, params: {
          'invalid_param': 'invalid_value'
        })

        assert_response_status(400)

        assert_valid_json(response[:body])
        
        # Verify OperationOutcome is returned
        assert_resource_type(:operation_outcome)
        
        operation_outcome = FHIR.from_contents(response[:body])
        assert operation_outcome.issue&.any? { |issue| issue.severity == 'error' },
          'OperationOutcome should contain at least one error issue'
      end
    end
  end
end