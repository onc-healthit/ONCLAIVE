require_relative '../../inferno_test_suite'
require 'inferno/dsl/oauth_credentials'
require 'inferno/utils/assertion_utils'

module Test3
  # Test Group for REQ-07: Must Support elements processing
  #
  # Description: "Application Actor SHALL process resource instances containing
  # Must Support data elements without errors or application failure"
  #
  # This group contains tests to verify that the application can successfully
  # process resources that include elements marked as 'Must Support' in their
  # defining StructureDefinition or Implementation Guide.
  #
  # The primary test involves creating a resource instance populated with
  # Must Support elements and verifying that the server accepts it without error.
  #
  # Note: This test assumes the user provides a valid resource instance
  # containing the necessary Must Support elements as input. It does not
  # dynamically determine Must Support elements from profiles.
  class MustSupportProcessingGroup < Inferno::TestGroup
    id :req_07_must_support_processing_group
    title 'REQ-07: Must Support Element Processing'
    description %(
      ### Background
      The [FHIR Specification](https://www.hl7.org/fhir/mustsupport.html) defines 'Must Support' elements
      as those that an application actor must be capable of processing. This requirement ensures that systems
      can handle essential data elements defined within relevant profiles or implementation guides.

      ### Test Methodology
      This test verifies that the Application Actor (Server) can process resource instances
      containing Must Support data elements without errors or application failure.

      1. **Input**: The test requires a JSON representation of a FHIR resource instance.
         This instance **must** be pre-populated with the relevant Must Support elements
         according to the specific profile or implementation guide being tested against.
         *(Providing this resource instance is the responsibility of the tester setup).*
      2. **Action**: The test attempts to `create` the provided resource instance on the server.
      3. **Validation**: The test asserts that the server responds with a successful status code
         (HTTP 201 Created), indicating that it processed and accepted the resource without error.

      This test focuses specifically on the server's ability to *accept* and *process* the resource
      containing Must Support elements, fulfilling the requirement REQ-07. It does not validate
      the specific content or structure beyond basic FHIR resource validity.
    )
    run_as_group

    # Define standard inputs used by tests in this group
    input :url,
          title: 'FHIR Endpoint URL',
          description: 'The base URL of the FHIR server.'

    # Input for the resource containing Must Support elements
    input :must_support_resource_json,
          title: 'Resource with Must Support Elements (JSON)',
          description: %(
            Provide a JSON representation of a FHIR resource instance.
            This resource instance **MUST** contain all relevant 'Must Support' elements
            as defined by the applicable profile or implementation guide being tested.
            The test will attempt to create this resource on the server.
            Example: A US Core Patient resource with all its Must Support fields populated.
          ),
          type: 'textarea',
          optional: false # This input is crucial for the test

    # FHIR Client configuration specific to this group
    fhir_client do
      url :url
      # Assuming OAuth 2.0 is used for authentication; adjust if needed
      oauth_credentials :oauth_token do
        token_url 'http://example.com/oauth/token' # Placeholder - Adjust or make input
        client_id 'CLIENT_ID'                     # Placeholder - Adjust or make input
        client_secret 'CLIENT_SECRET'               # Placeholder - Adjust or make input
      end
    end

    # -----------------------------------------------------------------------------
    # Test: REQ-07 Must Support Element Processing
    # -----------------------------------------------------------------------------
    test do
      id :req_07_must_support_element_processing
      title 'Application processes resources with Must Support elements'
      description %(
        Verifies that the server can successfully process (via FHIR `create`)
        a resource instance containing Must Support elements.

        **Steps:**
        1. Parse the provided JSON resource (`must_support_resource_json`).
        2. Validate that the input is valid JSON and represents a FHIR resource.
        3. Send a `POST` request (FHIR `create`) to the server with the resource.
        4. Assert that the server responds with HTTP status 201 (Created).

        **Success Criteria:**
        - The server returns a 201 Created status code.

        **Assumptions:**
        - The provided `must_support_resource_json` input contains a valid FHIR resource.
        - This resource instance has been correctly populated with the necessary Must Support elements
          according to the relevant profile or implementation guide.
      )

      # Make the input available within the test
      uses_request :create_must_support_resource

      run do
        # --- Step 1 & 2: Parse and Validate Input Resource ---
        assert must_support_resource_json.present?,
               'Input `must_support_resource_json` is required but was not provided.'

        resource = nil
        begin
          resource = FHIR.from_contents(must_support_resource_json)
          info "Successfully parsed provided resource of type: #{resource.resourceType}"
        rescue StandardError => e
          fail "Failed to parse `must_support_resource_json` as a FHIR resource. Error: #{e.message}"
        end

        # Basic validation - ensure it's a FHIR resource object
        assert resource.is_a?(FHIR::Model), 'Provided JSON does not represent a valid FHIR resource structure.'
        assert resource.resourceType.present?, 'Parsed resource is missing the required `resourceType` element.'

        # Optional: More rigorous validation against base FHIR spec
        # validation_errors = resource.validate
        # assert validation_errors.empty?, "Provided resource is not valid FHIR: #{validation_errors}"
        # info "Provided resource appears to be valid FHIR."

        # --- Step 3: Perform FHIR Create ---
        fhir_create(resource, name: :create_must_support_resource)

        # --- Step 4: Assert Success Response ---
        # According to FHIR spec, a successful CREATE should return 201 Created.
        # https://www.hl7.org/fhir/http.html#create
        assert_response_status(201)
        info "Server successfully created the resource (HTTP 201 Created), indicating it processed the resource with Must Support elements without error."

        # Optional: Check if a resource was returned in the body (servers MAY return representation)
        # assert resource.present?, "Server did not return a resource body in the create response."
        # assert_valid_resource(resource: resource) # Validate if returned

        pass "Server successfully processed and created the resource containing Must Support elements."
      end
    end # End of test
  end # End of class MustSupportProcessingGroup
end # End of module Test3