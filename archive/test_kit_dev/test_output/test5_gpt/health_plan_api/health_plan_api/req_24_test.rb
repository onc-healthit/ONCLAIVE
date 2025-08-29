module Test5Gpt
  class UnauthorizedRequestRejectionTestGroup < Inferno::TestGroup
    id :req_24_unauthorized_request_rejection
    title 'Unauthorized Request Rejection'
    description %(
      This test group verifies that the Health Plan API server rejects any unauthorized requests by returning an HTTP 401 unauthorized response code, as required by REQ-24.
    )

    test do
      id :req_24_unauthorized_request_rejection_test
      title 'Server rejects unauthorized requests with HTTP 401'
      description %(
        This test sends a request to the Health Plan API server without authorization and expects an HTTP 401 unauthorized response code.
      )
      input :server_url

      run do
        # Making a request to the server without authorization
        response = get("#{server_url}/Patient")

        # Asserting that the response status is 401
        assert_response_status(401, 'Expected HTTP 401 Unauthorized response for unauthorized request')
      end
    end
  end
end