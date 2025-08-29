require 'inferno/dsl'

module PlannetTestKit
  class PlanNetUnauthenticatedAccessGroup < Inferno::TestGroup
    id :plan_net_req_01_unauthenticated_access
    title 'REQ-01: Unauthenticated Plan-Net Access'
    description %(
      **Requirement:** Health Plan API SHALL NOT require authentication for Plan-Net service access (REQ-01).

      **Description:** This test group verifies that the Plan-Net endpoints provided by the
      Health Plan API do not require authentication for access. It attempts to perform
      FHIR search operations on various Plan-Net resource types without providing any
      authentication credentials (e.g., no `Authorization` header).

      **Validation:**
      - Each request should return an HTTP status code that is *not* 401 (Unauthorized) or 403 (Forbidden).
        Successful searches typically return 200 (OK), even if the result set is empty.
      - The response headers should *not* contain the `WWW-Authenticate` header, which typically
        indicates that authentication is required.
    )

    input :url,
          title: 'Health Plan API Base URL',
          description: 'The base URL of the Health Plan FHIR API endpoint.'

    # Configure a FHIR client specific to this group that *does not* use authentication.
    # This overrides any potential authentication configured at a higher level (TestSuite).
    fhir_client :plan_net_client do
      url :url
      # No access token or other authentication mechanism is provided.
    end

    # List of Plan-Net resource types to test based on TC-01
    PLAN_NET_RESOURCE_TYPES = [
      'Organization',
      'Practitioner',
      'PractitionerRole',
      'HealthcareService',
      'Location',
      'Network'
      # Add other relevant Plan-Net resources if needed
    ].freeze

    # Dynamically create a test for each resource type
    PLAN_NET_RESOURCE_TYPES.each do |resource_type|
      test do
        id :"plan_net_req_01_unauthenticated_#{resource_type.downcase}_search"
        title "Unauthenticated Search for #{resource_type}"
        description "Verify that searching for #{resource_type} resources does not require authentication."

        run do
          # Perform a FHIR search for the resource type without authentication
          # Use the specially configured :plan_net_client
          fhir_search(resource_type, client: :plan_net_client)

          # Assert that the response status is NOT 401 or 403
          assert_response_status_does_not_equal([401, 403])

          # Assert that the WWW-Authenticate header is not present
          assert response[:headers].fetch('www-authenticate', nil).blank?,
                 'WWW-Authenticate header should not be present for unauthenticated access.'

          # Optional: Could add checks for 200 OK specifically if desired,
          # but the core requirement is just the *absence* of auth requirement.
          # A 404 might be acceptable if the resource type isn't supported *at all*,
          # though that might indicate a different conformance issue.
          # The primary failure condition for *this* test is 401/403.
          pass "Successfully accessed #{resource_type} endpoint without authentication (HTTP Status: #{response[:status]})."
        end
      end
    end

    # TC-02: XML Format Testing (SHOULD Support) - Focus on Authentication Aspect
    test do
      id :plan_net_req_01_unauthenticated_organization_search_xml
      title 'Unauthenticated Organization Search Requesting XML Format'
      description %(
        Verify that searching for Organization resources while requesting the XML format
        (`Accept: application/fhir+xml`) does not require authentication.
        This also implicitly tests if the server correctly handles the Accept header
        without demanding authentication.
      )

      run do
        # Perform a FHIR search for Organization, requesting XML format
        fhir_search('Organization', client: :plan_net_client, headers: { 'Accept' => 'application/fhir+xml' })

        # Assert that the response status is NOT 401 or 403
        assert_response_status_does_not_equal([401, 403])

        # Assert that the WWW-Authenticate header is not present
        assert response[:headers].fetch('www-authenticate', nil).blank?,
               'WWW-Authenticate header should not be present for unauthenticated access, even when requesting XML.'

        # Optional: Check if the Content-Type is indeed XML if the status was successful (e.g., 200)
        # This verifies the "SHOULD" part of TC-02 regarding XML support.
        if response[:status] == 200
          content_type = response[:headers].fetch('content-type', '')
          assert content_type.include?('application/fhir+xml'),
                 "Expected Content-Type header to indicate 'application/fhir+xml', but received '#{content_type}'. " \
                 "Note: While XML support might be optional (SHOULD), requiring authentication based on the Accept header is non-conformant."
        end

        pass "Successfully accessed Organization endpoint requesting XML without authentication (HTTP Status: #{response[:status]})."
      end
    end

    # Note: The specification mentions READ operations and instance-level operations.
    # These tests currently focus on the SEARCH operations listed in TC-01.
    # Additional tests could be added here to cover unauthenticated READs if
    # sample resource IDs were provided as inputs. For example:
    #
    # input :sample_organization_id, optional: true, title: 'Sample Organization ID'
    #
    # test do
    #   id :plan_net_req_01_unauthenticated_organization_read
    #   title 'Unauthenticated Read for Organization'
    #   description 'Verify reading an Organization resource by ID does not require authentication.'
    #   skip_if_blank :sample_organization_id
    #
    #   run do
    #     fhir_read(:organization, sample_organization_id, client: :plan_net_client)
    #     assert_response_status_does_not_equal([401, 403])
    #     assert response[:headers].fetch('www-authenticate', nil).blank?, 'WWW-Authenticate header should not be present.'
    #     # Allow 404 Not Found as a valid non-authenticated response for READ
    #     pass "Attempted read for Organization/#{sample_organization_id} without authentication (HTTP Status: #{response[:status]})."
    #   end
    # end
  end
end