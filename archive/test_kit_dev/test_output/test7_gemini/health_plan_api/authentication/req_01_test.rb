module Test7Gemini
  class Req01NoAuthenticationGroup < Inferno::TestGroup
    id :test7_gemini_req_01_no_authentication_group
    title 'REQ-01: No Authentication for Plan-Net Services'
    description %(
      **Requirement REQ-01**: "Health Plan API SHALL NOT require authentication for Plan-Net service access."

      This test group verifies that the Health Plan API does not require authentication
      for accessing Plan-Net services. It attempts to perform a FHIR operation
      on a common Plan-Net resource (HealthcareService) without any authentication.
    )

    # This group uses a dedicated FHIR client that does not include any authentication,
    # regardless of the suite's main FHIR client configuration.
    # The :url input is expected to be provided by the containing TestSuite.
    fhir_client :unauthenticated do
      url :url
      # No oauth_credentials or bearer_token are specified, ensuring unauthenticated requests.
    end

    test do
      id :test7_gemini_req_01_plan_net_no_auth_check
      title 'Attempt to access Plan-Net HealthcareService without authentication'
      description %(
        This test performs a FHIR search for `HealthcareService` resources using an
        unauthenticated request.

        **Expected Behavior**:
        - The server SHALL NOT return an HTTP 401 Unauthorized or 403 Forbidden status.
        - A successful response (e.g., HTTP 200 OK, even with an empty Bundle) indicates
          that authentication was not required, and the test passes.
        - Other non-success statuses (e.g., HTTP 404 Not Found if `HealthcareService`
          is not supported or no records exist, or HTTP 5xx server errors)
          are also considered passing for this specific requirement, as they do not
          indicate an authentication *requirement*. However, such statuses might be
          flagged by other tests focusing on server capability or availability.
      )
      # This test makes a request that can be referenced by its name.
      makes_request :plan_net_unauthenticated_search

      run do
        # Perform a FHIR search for HealthcareService resources using the unauthenticated client.
        # Searching for a small number of resources (_count=1) is sufficient.
        fhir_search(:healthcare_service, client: :unauthenticated, params: { _count: 1 }, name: :plan_net_unauthenticated_search)

        status = response[:status]

        if [401, 403].include?(status)
          fail "Authentication was required for Plan-Net service access (HealthcareService search). Received HTTP status: #{status}. Per REQ-01, the API SHALL NOT require authentication."
        else
          # If the status is not 401 or 403, the "SHALL NOT require authentication" condition is met for this interaction.
          if status == 200
            pass "Successfully accessed Plan-Net service (HealthcareService search) without authentication. Received HTTP status: #{status}."
          else
            # For statuses other than 200 (e.g., 404, 500), authentication was not the explicit barrier.
            info "Received HTTP status #{status} when accessing Plan-Net service (HealthcareService search) without authentication. Since this is not an authentication error (401/403), this meets the REQ-01 requirement that authentication SHALL NOT be required for this interaction."
            pass "Plan-Net service access (HealthcareService search) did not result in an authentication error (401/403). Received HTTP status: #{status}."
          end
        end
      end
    end
  end
end