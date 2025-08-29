require_relative '../../inferno_base_test'

module Plannet
  # Test Group for REQ-01: No Authentication Requirement
  # Description: "Health Plan API SHALL NOT require authentication for Plan-Net service access"
  # Actor: Health Plan API
  # Conformance: SHALL NOT
  class NoAuthRequiredGroup < Inferno::TestGroup
    id :plannet_no_auth_required
    title 'REQ-01: No Authentication Required'
    description %(
      # Background

      The [Plan-Net IG Requirement REQ-01](https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/requirements.html#req-01-no-authentication-requirement)
      states that the Health Plan API **SHALL NOT** require authentication for
      Plan-Net service access. This test verifies that requests made to a
      Plan-Net endpoint without authentication credentials are successful.

      # Test Methodology

      This test attempts to perform a FHIR search operation on a common
      Plan-Net resource type (HealthcareService) without providing an
      Authorization header or any other authentication mechanism.

      * **Success**: The server responds with a 2xx status code (e.g., 200 OK),
        indicating the request was processed successfully without authentication.
      * **Failure**: The server responds with a 401 Unauthorized or 403 Forbidden
        status code, indicating that authentication is required, which violates
        the requirement.
    )
    input :url,
          title: 'Plan-Net FHIR API Endpoint',
          description: 'The base URL for the Plan-Net FHIR API.'

    # Configure a dedicated FHIR client for this group that explicitly
    # does not use any authentication. This overrides any potential
    # authentication configured at a higher level (e.g., Test Suite).
    fhir_client :plan_net_unauthenticated_client do
      url :url
      # No access_token or other auth mechanism specified
    end

    # Test REQ-01: Verify no authentication is required for a basic search
    test do
      id :plannet_req_01_no_auth_test
      title 'Plan-Net endpoint allows access without authentication'
      description %(
        This test verifies that the Plan-Net FHIR API endpoint allows access
        to resources without requiring authentication. It attempts to search
        for HealthcareService resources without providing an access token.

        A successful response (HTTP 200 OK) indicates that the server does not
        require authentication for this type of request, conforming to the
        requirement. A 401 Unauthorized or 403 Forbidden response indicates
        failure.
      )

      run do
        # Perform a FHIR search for HealthcareService resources using the
        # unauthenticated client.
        # We don't need any specific search parameters, just checking accessibility.
        fhir_search(:healthcare_service, client: :plan_net_unauthenticated_client)

        # Assert that the response status code is 200 OK.
        # According to REQ-01, the server SHALL NOT require authentication.
        # Therefore, a successful response (200) is expected.
        # A 401 or 403 status code would mean authentication is required,
        # thus failing the test.
        assert_response_status(200)

        # If the assertion passes, explicitly state the success reason.
        pass 'Successfully accessed the Plan-Net endpoint without authentication, as required.'
      end
    end
  end
end