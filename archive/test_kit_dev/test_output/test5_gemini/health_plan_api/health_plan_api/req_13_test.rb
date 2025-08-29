module Test5_gemini
  class Req13Test < Inferno::Test
    id :req_13_unauthorized_request_response
    title 'Server returns an HTTP 401 Unauthorized response for requests without proper authorization'
    description %(
      This test verifies that the server returns an HTTP 401 Unauthorized response code when a request is made without proper authorization.
    )

    run do
      skip_if_known_not_supported(:OAuth)

      fhir_client :no_auth do
        url config.fhir_server.url
      end

      response = fhir_read(:patient, 'example')

      assert_response_status(401)
    end
  end
end