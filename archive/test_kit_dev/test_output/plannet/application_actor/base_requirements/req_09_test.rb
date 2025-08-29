require_relative '../../utils/assertions'

module Plannet
  # Test Group for REQ-09: Missing Must Support Interpretation
  # Description: "Application Actor SHALL interpret missing Must Support data elements
  # as data not present in Health Plan API system"
  # Conformance: SHALL
  # Actor: Application Actor
  class MissingMustSupportInterpretationGroup < Inferno::TestGroup
    include Plannet::Assertions

    id :plannet_missing_must_support_interpretation_group
    title 'REQ-09: Missing Must Support Interpretation'
    description %(
      This test group addresses requirement [REQ-09](https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/behavior.html#application-actor):
      Application Actor SHALL interpret missing Must Support data elements as data not present in Health Plan API system.

      Since this requirement pertains to the behavior of the *client* application (Application Actor),
      this test requires **manual attestation**.

      The test will attempt to retrieve a `plannet-Organization` resource from the
      server to provide a concrete example. It will then display the resource (if found)
      and list the Must Support elements defined for the profile.

      The user must then manually review the resource, identify any missing Must Support elements,
      and confirm whether their application correctly interprets this absence as
      "data not present".
    )
    run_as_group

    # Define Must Support elements for plannet-Organization profile based on
    # http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition-plannet-Organization.html
    # This list serves as a reference for the manual check.
    # Using simplified element names for clarity in the instructions.
    MUST_SUPPORT_ORGANIZATION_ELEMENTS = [
      'identifier',
      'active',
      'type',
      'name',
      'telecom',
      'address',
      'partOf',
      'contact',
      'endpoint'
    ].freeze

    # Inputs required for fetching a resource instance
    input :url,
          title: 'Plan Net FHIR API Endpoint',
          description: 'The base URL for the Plan Net FHIR API server.'

    input :organization_id,
          title: 'Plan-Net Organization ID',
          description: 'The ID of a known Plan-Net Organization resource to use for the test.',
          optional: true # Allow test to proceed by searching if ID is not provided

    # Optional input from a previous search test, if available
    input :first_organization_resource_json,
          title: 'First Plan-Net Organization Resource JSON from Search',
          description: 'JSON representation of the first Organization found in a previous search test.',
          optional: true

    # FHIR Client configuration
    fhir_client do
      url :url
      # Add headers/authentication if required by the server
      # Example: bearer_token :bearer_token
    end

    # Manual Test REQ-09
    test do
      id :plannet_req_09_missing_must_support_interpretation
      title 'Application interprets missing Must Support data correctly (Manual)'
      description %(
        **Manual Test:** This test requires the user (representing the Application Actor)
        to confirm compliance with requirement REQ-09.

        **Requirement:** Application Actor SHALL interpret missing Must Support data elements
        as data not present in Health Plan API system.

        **Test Steps:**

        1.  **Resource Retrieval:** The test attempts to fetch a `plannet-Organization` resource.
            It will use the `organization_id` input if provided, then check for the
            `first_organization_resource_json` input, or finally attempt a basic search.
        2.  **Resource Display:** If an Organization resource is successfully retrieved, its ID
            and JSON representation will be available in the test outputs and request details.
        3.  **Must Support Elements:** The Must Support elements for the `plannet-Organization`
            profile are listed below for reference:
            *   `#{MUST_SUPPORT_ORGANIZATION_ELEMENTS.join(', ')}`
        4.  **Manual Review & Confirmation:**
            *   Examine the retrieved Organization resource instance (view JSON in outputs/requests).
            *   Identify if any of the Must Support elements listed above are **missing** from this specific resource instance.
            *   **Attest** whether your application, when processing this resource (or a similar one with missing Must Support data), correctly interprets the absence of these elements as "data not present in the Health Plan API system".
        5.  **Record Result:** Select **Pass** if your application meets the requirement. Select **Fail** otherwise.

        *If no Organization resource can be retrieved, this test will be skipped.*
      )
      # Mark this test as potentially making an HTTP request
      makes_request :organization_read_or_search

      # Define outputs for context
      output :retrieved_organization_id, :retrieved_organization_json

      run do
        organization_resource = nil
        resource_source_description = ''

        # --- Step 1: Resource Retrieval ---
        if organization_id.present?
          # Option A: Use provided ID
          resource_source_description = "using provided ID: #{organization_id}"
          fhir_read(:organization, organization_id, name: :organization_read_or_search)

          if response[:status] == 200 && resource.is_a?(FHIR::Model)
            organization_resource = resource
            assert_resource_type(:organization, resource: organization_resource)
            info "Successfully retrieved Organization/#{organization_resource.id}."
          else
            warning "Failed to retrieve Organization with ID '#{organization_id}'. Status: #{response[:status]}. Body: #{response[:body]}"
            # Continue to try other methods if configured
          end

        elsif first_organization_resource_json.present? && organization_resource.nil?
          # Option B: Use resource from previous search output
          resource_source_description = "using resource from previous search test output"
          begin
            organization_resource = FHIR.from_contents(first_organization_resource_json)
            assert_resource_type(:organization, resource: organization_resource)
            info "Using Organization resource with ID #{organization_resource&.id || 'N/A'} from previous search result."
            # No new FHIR request made in this branch if we trust the input JSON
            request = nil # Clear request if we didn't make one here
          rescue => e
            error "Failed to parse Organization resource from input 'first_organization_resource_json': #{e.message}"
            organization_resource = nil # Ensure it's nil if parsing failed
          end

        end

        # Option C: Try searching if no resource obtained yet
        if organization_resource.nil? && !organization_id.present? # Avoid search if specific ID failed
          resource_source_description = "attempting basic search"
          info "No Organization ID provided or previous resource available. Attempting a search..."
          fhir_search(:organization, params: { _count: 1 }, name: :organization_read_or_search)

          if response[:status] == 200 && resource.is_a?(FHIR::Bundle)
            entry = resource.entry&.first
            if entry&.resource.present?
              organization_resource = entry.resource
              assert_resource_type(:organization, resource: organization_resource)
              info "Found Organization/#{organization_resource.id} via search."
            else
              info "Search successful, but no Organization resources found on the server."
            end
          else
            warning "Organization search failed. Status: #{response[:status]}. Body: #{response[:body]}"
          end
        end

        # --- Step 2 & 3: Prepare for Manual Check ---
        skip_if organization_resource.nil?, "Could not retrieve or find an Organization resource to perform the manual check (#{resource_source_description}). Skipping manual attestation for REQ-09."

        # Output the resource details for the user
        output retrieved_organization_id: organization_resource.id
        output retrieved_organization_json: organization_resource.to_json

        # --- Step 4 & 5: Prompt for Manual Confirmation ---
        # Use warning to display instructions prominently in the UI.
        # The user must manually set the test result (Pass/Fail) based on their application's behavior.
        warning %(
          **Manual Conformance Check Required for REQ-09**

          **Context:** An `Organization` resource (ID: `#{organization_resource.id}`) was retrieved
          (see `retrieved_organization_json` output or the request details for the full resource).

          **Reference - Must Support Elements for `plannet-Organization`:**
          *   `#{MUST_SUPPORT_ORGANIZATION_ELEMENTS.join(', ')}`

          **Action Required:**
          1. Review the retrieved `Organization/#{organization_resource.id}` resource.
          2. Identify any Must Support elements listed above that are **missing** from the instance.
          3. Confirm if your application correctly interprets such missing elements as "data not present".
          4. **Manually select Pass or Fail** for this test based on your application's behavior regarding REQ-09.
        )

        # The test run concludes here. The final result (Pass/Fail) is determined by the user's manual input in the Inferno UI.
        # There is no programmatic assertion for the manual step itself.
      end
    end
  end
end