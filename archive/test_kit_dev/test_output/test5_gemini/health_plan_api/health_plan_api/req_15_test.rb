module Test5_gemini
  class InvalidParameterResponseTest < Inferno::Test
    id :req_15_invalid_parameter_response
    title 'Server returns an HTTP 400 status code for invalid parameters'
    description %(
      This test verifies that the server returns the correct HTTP status code (400)
      when an invalid parameter is provided in the request.
    )

    run do
      skip_if_known_not_supported(:Patient, [:read])

      invalid_parameter_name = 'invalid_parameter'
      fhir_read(:Patient, 'example', params: { invalid_parameter_name => 'invalid_value' })

      assert_response_status(400)
    end
  end
end
