module Test5Gpt
  class InsufficientScopeResponseTestGroup < Inferno::TestGroup
    id :req_14_insufficient_scope_response
    title 'Insufficient Scope Response'
    description %(
      This test group verifies that the Health Plan API returns a 403 status code
      with an "insufficient scope" error when the request is made with inadequate
      authorization scope.
    )

    test do
      id :insufficient_scope_response_test
      title 'Server returns 403 status for insufficient scope'
      description %(
        This test checks that the server returns a 403 Forbidden status code
        with an "insufficient scope" error when a request is made with a token
        that does not have the necessary permissions.
      )
      input :server_url, :access_token

      fhir_client do
        url :server_url
        bearer_token :access_token
      end

      run do
        # Attempt to read a resource with insufficient scope
        response = fhir_read(:patient, 'example-patient-id')

        # Assert that the response status is 403
        assert_response_status(403)

        # Assert that the response contains an "insufficient scope" error message
        assert response[:body].include?('insufficient scope'), 
               'Expected response to include "insufficient scope" error message'
      end
    end
  end
end