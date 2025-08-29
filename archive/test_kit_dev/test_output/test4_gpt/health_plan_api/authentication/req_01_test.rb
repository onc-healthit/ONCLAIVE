module Test4Gpt
  class NoAuthenticationRequirementTestGroup < Inferno::TestGroup
    id :req_01_no_authentication_requirement
    title 'No Authentication Requirement'
    description %(
      Health Plan API SHALL NOT require authentication for Plan-Net service access.
      This test verifies that the API does not enforce authentication when accessing the service.
    )

    test do
      id :req_01_no_authentication_test
      title 'Health Plan API does not require authentication'
      description %(
        This test checks that the Health Plan API can be accessed without authentication.
        It sends a request to the API endpoint and expects a successful response without requiring authentication.
      )
      input :server_url, title: 'FHIR Server URL', description: 'The base URL for the FHIR server'

      run do
        # Attempt to access the server without authentication
        response = get("#{server_url}/metadata")

        # Assert that the server responds successfully without authentication
        assert_response_status(200, response: response)
        assert_valid_json(response.body)
        assert response.body.include?('CapabilityStatement'), 'Expected response to include a CapabilityStatement'
      end
    end
  end
end