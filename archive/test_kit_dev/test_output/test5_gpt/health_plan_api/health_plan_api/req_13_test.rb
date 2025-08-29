module Test5Gpt
  class UnauthorizedRequestResponseTestGroup < Inferno::TestGroup
    id :req_13_unauthorized_request_response
    title 'Unauthorized Request Response'
    description %(
      This test group verifies that the Health Plan API returns the appropriate
      HTTP status code for unauthorized requests as per the requirement REQ-13.
      Specifically, it checks for a 401 or other 4xx status code when an unauthorized
      request is made.
    )

    test do
      id :unauthorized_request_response_test
      title 'Health Plan API returns 401/4xx for unauthorized requests'
      description %(
        This test sends a request to the Health Plan API without authorization
        and verifies that the response status code is 401 or another 4xx code,
        indicating an unauthorized request.
      )
      input :server_url

      run do
        fhir_client do
          url server_url
        end

        response = get("#{server_url}/Patient")

        assert response.status >= 400 && response.status < 500,
               "Expected a 4xx status code, but received #{response.status}"

        assert response.status == 401,
               "Expected a 401 Unauthorized status code, but received #{response.status}"
      end
    end
  end
end