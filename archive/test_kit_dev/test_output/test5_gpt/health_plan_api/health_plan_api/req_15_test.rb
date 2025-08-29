module Test5Gpt
  class InvalidParameterResponseTestGroup < Inferno::TestGroup
    id :req_15_invalid_parameter_response
    title 'Invalid Parameter Response'
    description %(
      This test group verifies that the Health Plan API returns a 400 status code
      when an invalid parameter is provided, as required by REQ-15.
    )

    test do
      id :req_15_invalid_parameter_response_test
      title 'Health Plan API returns 400 status for invalid parameter'
      description %(
        This test checks that the Health Plan API returns a 400 status code
        when a request is made with an invalid parameter. This is to ensure
        that the API correctly handles invalid input as per the specification.
      )
      input :server_url, :access_token

      run do
        fhir_client do
          url :server_url
          bearer_token :access_token
        end

        # Attempt to search with an invalid parameter
        fhir_search(:patient, params: { invalid_param: 'invalid_value' })

        # Assert that the response status is 400
        assert_response_status(400)
      end
    end
  end
end