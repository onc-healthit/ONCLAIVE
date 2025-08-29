module Test5_gemini
  class InsufficientScopeResponseTest < Inferno::Test
    id :req_14_insufficient_scope_response
    title 'Health Plan API returns 403 Forbidden with insufficient scope error'
    description %(
      This test verifies that the Health Plan API returns a 403 Forbidden response with an "insufficient scope" error message when a request is made with insufficient OAuth2 scopes.
    )

    run do
      skip_if_not_supported(:OAuth)

      # Assuming the test setup provides a way to make a request with insufficient scopes
      # Replace with actual implementation based on the test environment
      response = make_request_with_insufficient_scopes

      assert_response_status(403)
      assert_response_body_contains('insufficient scope')
    end
  end
end