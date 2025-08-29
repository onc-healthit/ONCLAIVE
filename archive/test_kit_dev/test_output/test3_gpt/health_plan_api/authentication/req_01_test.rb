module Test4Gpt
  class NoAuthenticationRequirementTest < Inferno::TestGroup
    id :req_01_no_authentication_requirement
    title 'No Authentication Requirement'
    description %(
      Health Plan API SHALL NOT require authentication for Plan-Net service access.
      This test verifies that the server does not require authentication by attempting
      to access a public endpoint without providing any authentication credentials.
    )

    test do
      id :req_01_no_authentication_test
      title 'Server does not require authentication for access'
      description %(
        Verify that the server does not require authentication by accessing a public
        endpoint without authentication credentials and expecting a successful response.
      )
      input :server_url, title: 'FHIR Server URL', description: 'The base URL for the FHIR server'

      run do
        # Attempt to access the server without authentication
        response = get("#{server_url}/metadata")

        # Assert that the response is successful and does not require authentication
        assert_response_status(200)
        assert !response.headers['www-authenticate'], 'Expected no authentication challenge in response headers'
      end
    end
  end
end