require_relative '../../plannet_base_group'

module Plannet
  # Test Group for REQ-02: No consumer identification requirement
  # Description: "Health Plan API SHALL NOT require directory mobile applications
  # to send consumer identifying information in queries"
  class PlannetNoConsumerIdentificationGroup < PlannetBaseGroup
    id :plannet_no_consumer_identification_group
    title 'No Consumer Identification Requirement (REQ-02)'
    description %(
      This test group verifies that the Health Plan API does not require
      consumer identifying information for directory queries, as specified in REQ-02.

      The test attempts to perform a basic search for a common Plan Net resource
      (e.g., Organization) without providing any authentication or consumer-specific
      identifiers. A successful response (HTTP 200 OK) indicates that the API
      allows queries without consumer identification. A failure (e.g., HTTP 401
      Unauthorized or 403 Forbidden) suggests that the API incorrectly requires
      such information for basic directory access.
    )

    # Test REQ-02
    test do
      id :plannet_req_02_no_consumer_identification
      title 'API allows queries without consumer identifying information'
      description %(
        Tests if the API successfully responds to a search query for Organization
        resources without any consumer identifying information or authentication.
        This verifies that the API conforms to the requirement not to mandate
        consumer identification for directory queries.
      )
      # No specific inputs required beyond the base URL configured for the FHIR client.

      run do
        # Perform a FHIR search for Organization resources without any parameters
        # or authentication headers that would identify a specific consumer.
        # The fhir_client used here should be configured without an access token
        # for this specific request, or the server must allow unauthenticated access
        # for this type of query.
        # Assuming the base fhir_client is configured for the test session,
        # we make a request without adding specific auth.
        fhir_search(:organization)

        # Assert that the response status is 200 OK.
        # A 401 or 403 status code would indicate that the server requires
        # authentication or specific identification, failing the test.
        assert_response_status(200)

        # Assert that the response body is a FHIR Bundle.
        # This confirms the search operation returned a valid response format.
        assert_resource_type(:bundle)

        # If the above assertions pass, it indicates the API allows queries
        # without requiring consumer-specific identification.
        pass("Successfully received a response without providing consumer identifying information.")
      end
    end
  end
end