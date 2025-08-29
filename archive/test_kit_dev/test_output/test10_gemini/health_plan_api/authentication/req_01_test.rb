module Test10Gemini
  class Req01NoAuthenticationGroup < Inferno::TestGroup
    id :req_01_no_authentication_group
    title 'REQ-01: No Authentication Requirement'
    description %(
      This test group verifies that the Health Plan API, specifically for
      Plan-Net services, SHALL NOT require authentication for access.
      The test attempts to access a common Plan-Net resource endpoint (HealthcareService)
      without any authentication credentials. A successful response (HTTP 200 OK)
      indicates compliance.
    )

    # Define the input for the FHIR server URL.
    # This is a standard input required by most Inferno tests.
    input :url,
          title: 'FHIR Server Base URL',
          description: 'The base URL of the FHIR server implementing the Health Plan API.',
          type: 'text'

    test do
      id :req_01_plan_net_service_access_without_authentication
      title 'Plan-Net Service Access Without Authentication'
      description %(
        **Test Description:**
        This test verifies REQ-01: "Health Plan API SHALL NOT require authentication for Plan-Net service access".

        **Actions:**
        1. The test attempts to perform a FHIR search operation on the `HealthcareService`
           resource, which is a common Plan-Net resource.
        2. This request is made *without* an OAuth 2.0 bearer token or any other
           authentication mechanism.

        **Expected Outcome:**
        - The server SHOULD respond with an HTTP 200 OK status. This indicates that the
          Plan-Net service endpoint was accessible and processed the request successfully
          without requiring authentication.
        - The response body SHOULD be a valid FHIR Bundle (even if empty).

        **Failure Conditions:**
        - An HTTP 401 Unauthorized or 403 Forbidden response indicates that the server
          is requiring authentication, thereby failing the test.
        - Any other non-200 HTTP status code also indicates a failure, as successful
          access to the service was not achieved.
      )

      # This test makes a request to the /HealthcareService endpoint.
      # The name :plan_net_no_auth_check can be used by other tests if needed,
      # though not strictly necessary for this single test.
      makes_request :plan_net_no_auth_check

      run do
        # Perform a FHIR search for HealthcareService resources.
        # By not providing an access_token to the fhir_client or this call,
        # Inferno's FHIR client will not include an Authorization header.
        fhir_search(:healthcare_service, name: :plan_net_no_auth_check)

        # Assert that the response status is 200 OK.
        # This is the primary validation for the requirement that authentication
        # is NOT required for Plan-Net service access.
        assert_response_status(200)

        # Additionally, assert that the response body, if present and the status was 200,
        # is a FHIR Bundle, which is the expected resource type for a search operation.
        # The `resource` variable here refers to the parsed FHIR resource from the response body.
        assert_resource_type(:bundle, resource: resource)

        # If all assertions pass, explicitly pass the test with a success message.
        pass "Successfully accessed the Plan-Net HealthcareService endpoint without authentication (HTTP 200 OK). Response was a valid FHIR Bundle."
      end
    end
  end
end