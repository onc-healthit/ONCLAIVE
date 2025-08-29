require 'inferno/dsl/oauth_credentials'
require 'inferno/ext/fhir_client'

module Test3
  # Test Group for REQ-01: No Authentication Requirement
  #
  # This test group verifies that the Health Plan API does not require
  # authentication for accessing Plan-Net service endpoints, as specified
  # in requirement REQ-01.
  class NoAuthenticationRequirementGroup < Inferno::TestGroup
    id :test3_no_authentication_requirement_group
    title 'REQ-01: No Authentication Requirement'
    description %(
      **Requirement REQ-01:** "Health Plan API SHALL NOT require authentication for Plan-Net service access"

      **Actor:** Health Plan API

      **Conformance:** SHALL NOT

      **Test Description:**
      This test verifies that the FHIR server endpoints related to the Plan-Net
      Implementation Guide can be accessed without requiring authentication
      credentials (e.g., an OAuth 2.0 bearer token).

      The test attempts to perform a FHIR search operation (e.g., for Organization
      resources) against the server's base FHIR endpoint without providing any
      `Authorization` header or token.

      **Success Criteria:**
      The test passes if the server responds with any HTTP status code other than
      `401 Unauthorized` or `403 Forbidden`. A successful response (e.g., `200 OK`)
      or other error responses (e.g., `404 Not Found`, `500 Internal Server Error`)
      are considered passing for this specific requirement, as they do not
      indicate that authentication *is* required.

      **Failure Criteria:**
      The test fails if the server responds with `401 Unauthorized` or `403 Forbidden`,
      as this indicates that authentication is required, violating the requirement.
    )

    input :url,
          title: 'FHIR Endpoint URL',
          description: 'The base URL of the FHIR server implementing the Plan-Net IG.',
          type: 'url'

    # Test Case: REQ-01 - Access Plan-Net without Authentication
    test do
      id :test3_req_01_plan_net_access_without_auth
      title 'Plan-Net service access does not require authentication'
      description %(
        Tests whether a request to a Plan-Net FHIR endpoint (specifically,
        searching for Organization resources) can be performed without providing
        an authentication token.

        It sends a GET request to the `/Organization` endpoint without an
        `Authorization` header. It asserts that the response status code is
        neither 401 (Unauthorized) nor 403 (Forbidden).
      )

      run do
        # Create a FHIR client specifically for this test, ensuring no authentication
        # token is configured or sent. We use the base URL provided as input.
        unauthenticated_client = FHIR::Client.new(url)

        # Set standard FHIR headers, explicitly avoiding the Authorization header.
        # Using 'application/fhir+json' for Accept header.
        unauthenticated_client.additional_headers = {
          'Accept' => 'application/fhir+json'
        }
        # Ensure the additional headers are used (some versions of fhir_client might need this)
        unauthenticated_client.use_additional_headers = true

        # Log the attempt
        info "Attempting to search for Organization resources at #{url} without authentication..."

        begin
          # Perform a FHIR search operation for a common Plan-Net resource type (Organization)
          # using the unauthenticated client.
          response = unauthenticated_client.search(FHIR::Organization)

          # Extract response details
          status_code = response.response[:code]
          response_body = response.response[:body]

          # Log the received status code
          info "Received response status code: #{status_code}"

          # Assert that the response status is NOT 401 Unauthorized
          assert status_code != 401, "Server returned 401 Unauthorized. Authentication SHALL NOT be required per REQ-01. Response Body: #{response_body}"

          # Assert that the response status is NOT 403 Forbidden
          assert status_code != 403, "Server returned 403 Forbidden. Authentication SHALL NOT be required per REQ-01. Response Body: #{response_body}"

          # If the assertions pass, the requirement is met.
          pass "Server responded with status code #{status_code}. Since it was not 401 or 403, authentication does not appear to be required for Plan-Net access, meeting REQ-01."

        rescue RestClient::ExceptionWithResponse => e
          # Handle HTTP errors captured by RestClient (covers 4xx/5xx errors not caught above)
          status_code = e.response.code
          response_body = e.response.body

          # Log the error status code
          error "Request failed with HTTP status code: #{status_code}. Response Body: #{response_body}"

          # Even in case of an error, check if it was specifically 401 or 403
          assert status_code != 401, "Server returned 401 Unauthorized. Authentication SHALL NOT be required per REQ-01. Response Body: #{response_body}"
          assert status_code != 403, "Server returned 403 Forbidden. Authentication SHALL NOT be required per REQ-01. Response Body: #{response_body}"

          # If it's another error (e.g., 404, 500), it still passes the 'no auth required' check.
          # Issue a warning for context, but pass the test based on the requirement.
          warning "Request failed with status code #{status_code} (not 401/403). While this indicates a server issue or resource unavailability, it meets the specific requirement REQ-01 that authentication is not enforced."
          pass "Server responded with status code #{status_code}. Since it was not 401 or 403, authentication does not appear to be required for Plan-Net access, meeting REQ-01."

        rescue StandardError => e
          # Catch any other unexpected errors during the client interaction or processing
          # (e.g., network issues, DNS resolution failures, invalid URL)
          error "An unexpected error occurred while attempting unauthenticated access: #{e.class.name} - #{e.message}. Could not verify REQ-01."
          # Fail the test because the condition could not be verified due to an unexpected error.
          fail "Test execution failed due to an unexpected error: #{e.message}"
        end
      end
    end
  end
end