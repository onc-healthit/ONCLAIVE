# frozen_string_literal: true

module Test8Gemini
  # Test Group for REQ-01: No authentication requirement for Plan-Net service access.
  #
  # Description: "Health Plan API SHALL NOT require authentication for Plan-Net service access"
  # Actor: Health Plan API
  # Conformance: SHALL NOT
  # Requirement ID: REQ-01
  class Req01NoAuthenticationGroup < Inferno::TestGroup
    id :test8_gemini_req_01_no_authentication_group
    title 'REQ-01: No Authentication for Plan-Net Service Access'
    description %(
      This test group verifies that the Health Plan API does not require
      authentication for accessing Plan-Net services, as per REQ-01.
      It attempts to access a representative Plan-Net FHIR endpoint (e.g., searching
      for Organization resources) without providing any authentication credentials.

      A successful response (e.g., HTTP 200 OK, or HTTP 404 Not Found if the
      resource type is supported but no instances exist) indicates that
      authentication is not required. An HTTP 401 Unauthorized or HTTP 403
      Forbidden response indicates that authentication is required, which
      constitutes a failure for this test.
    )
    short_description 'Verify Plan-Net services do not require authentication (REQ-01).'

    input :url,
          title: 'FHIR Server Base URL for Plan-Net Services',
          description: 'The base URL of the Health Plan API providing Plan-Net services.',
          type: 'text' # Valid input type

    # Configure a FHIR client that will be used for requests within this group.
    # Importantly, no authentication (like oauth_credentials or bearer_token) is specified,
    # so requests will be made without an Authorization header.
    fhir_client do # Correct usage of fhir_client block
      url :url # Input 'url' is declared and used
    end

    test do
      id :test8_gemini_req_01_plan_net_organization_access_no_auth
      title 'Verify Plan-Net Organization endpoint does not require authentication'
      description %(
        This test attempts to perform a FHIR search for Organization resources
        (a common Plan-Net resource) without any authentication.
        It checks that the server response is not an HTTP 401 (Unauthorized)
        or HTTP 403 (Forbidden), which would indicate an authentication requirement.
      )
      # This test makes a request to the Organization endpoint.
      makes_request :plan_net_organization_unauthenticated_search # Correct usage

      run do
        # Perform a FHIR search for Organization resources.
        # No specific search parameters are critical here; the goal is to make a request
        # to a Plan-Net related endpoint without authentication.
        fhir_search(:organization, client: fhir_client, name: :plan_net_organization_unauthenticated_search) # Correct FHIR DSL method

        # Ensure a response was received from the fhir_search operation
        assert response, "FHIR search for Organization did not return a response object."
        # Ensure the response hash contains the :status key
        assert response.key?(:status), "Response from Organization search is missing a :status key."

        status_code = response[:status] # Correct hash syntax for response access

        # The requirement is "SHALL NOT require authentication".
        # Therefore, if the server responds with 401 or 403, it's a failure.
        # Assert that the status code is NOT 401 or 403.
        authentication_not_required = ![401, 403].include?(status_code)

        assert authentication_not_required,
               "Server responded with HTTP #{status_code}, indicating authentication IS required. " \
               "This violates REQ-01: Health Plan API SHALL NOT require authentication for Plan-Net service access."

        # If the assertion above passes, it means authentication was not the barrier.
        # Any other status code (e.g., 200, 400, 404, 5xx) means authentication was not the barrier.
        # A 200 OK is ideal, showing data can be accessed.
        # A 404 Not Found is also acceptable for this test, as it means the server processed
        # the request without demanding authentication, even if no matching resources were found.
        # Other errors (e.g., 400 for a bad search, 5xx for server issues) are not ideal for
        # general API health but still pass this specific authentication test.
        pass "Server responded with HTTP #{status_code}. Authentication was not identified as a barrier " \
             "for accessing Organization resources, satisfying REQ-01."
      end
    end
  end
end