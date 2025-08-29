require 'fhir_models' # Ensure fhir_models is available for FHIRPath evaluation

module Plannet
  # Test Group for REQ-07: Must Support elements processing
  # This group verifies that the server can provide resources containing
  # Must Support elements, which is a prerequisite for the Application Actor
  # (client) to process them according to the requirement.
  class MustSupportElementsGroup < Inferno::TestGroup
    id :plannet_must_support_elements_group
    title 'REQ-07: Must Support Elements Processing'
    description %(
      **Requirement ID**: REQ-07

      **Description**: "Application Actor SHALL process resource instances containing Must Support data elements without errors or application failure"

      **Actor**: Application Actor

      **Conformance**: SHALL

      **Test Description**:
      This test verifies that the FHIR server can return resource instances
      containing data elements designated as "Must Support" by the relevant
      Implementation Guide(s). While this test executes against the server,
      it checks the prerequisite condition for the Application Actor (client)
      to fulfill the requirement. The test attempts to read a specific resource
      instance known or expected to contain Must Support elements and verifies
      their presence in the response.

      *Note*: This test requires the ID of a resource instance (e.g., Organization)
      that exists on the target server and is expected to contain the specified
      Must Support elements. The specific Must Support elements to check should
      be configured based on the profiles relevant to the Plannet use case.
    )
    run_as_group

    # Define inputs required for the tests within this group
    input :organization_id,
          title: 'Sample Organization Resource ID',
          description: 'Enter the ID of an Organization resource expected to contain Must Support elements.',
          optional: false # This ID is necessary to perform the read check

    # Define the list of Must Support elements for Organization as an example.
    # In a production test kit, this list might be derived from profile metadata.
    input :organization_must_support_elements,
          title: 'Organization Must Support Elements (FHIRPath)',
          description: 'Comma-separated list of FHIRPath expressions for Must Support elements on the Organization resource (e.g., name, active, address.line)',
          default: 'name, active, identifier, address' # Example defaults based on common requirements

    # FHIR Client configuration (if not already configured globally or in a parent group)
    # fhir_client do
    #   url :server_url # Assuming :server_url is defined elsewhere
    #   bearer_token :access_token # Assuming :access_token is defined elsewhere, if needed
    # end

    # Test implementation for REQ-07
    test do
      id :plannet_req_07_must_support_processing
      title 'Server returns resource with specified Must Support elements'
      description %(
        Verifies that the FHIR server returns a resource instance containing
        the specified Must Support elements when queried. It reads a specific
        Organization resource by ID and checks for the presence of data in
        elements identified as Must Support using FHIRPath.
      )
      # Make inputs available to this test
      uses_request :organization_read_for_must_support

      run do
        # Ensure an organization ID was provided
        assert organization_id.present?, 'Organization ID not provided; cannot perform Must Support check.'

        # Parse the comma-separated list of Must Support element paths
        must_support_element_paths = organization_must_support_elements.split(',').map(&:strip).reject(&:empty?)
        skip_if must_support_element_paths.empty?, 'No Must Support elements specified for Organization resource.'

        info "Attempting to read Organization/#{organization_id} to check for Must Support elements: #{must_support_element_paths.join(', ')}"

        # Perform the FHIR read operation
        fhir_read(:organization, organization_id, name: :organization_read_for_must_support)

        # Assert successful response
        assert_response_status(200)
        assert_resource_type(:organization)

        # Assert the resource is valid according to the base FHIR specification
        # Optionally, validate against a specific Plannet profile if available:
        # assert_valid_resource(profile_url: 'http://your-ig.org/StructureDefinition/plannet-organization')
        assert_valid_resource

        retrieved_resource = resource

        missing_elements = []
        present_elements = []

        # Check each Must Support element using FHIRPath
        must_support_element_paths.each do |element_path|
          # Use FHIRPath.evaluate to check if the element has data.
          # It returns an array of matching values/nodes. An empty array means the element
          # is absent or the path doesn't resolve to any node with content.
          begin
            evaluation_result = FHIRPath.evaluate(retrieved_resource, element_path)

            # Check if the result is truly empty or contains only empty elements (more complex check needed for full robustness)
            # For this test, we consider an empty array result as the element being 'missing' or 'empty'.
            if evaluation_result.empty?
              missing_elements << element_path
            else
              # Basic check for non-nil/non-empty values in the result array
              # FHIRPath can return complex objects; a more robust check might be needed
              # depending on the specific elements and profiles.
              has_content = evaluation_result.any? { |v| !v.nil? && (!v.respond_to?(:empty?) || !v.empty?) }
              if has_content
                present_elements << element_path
              else
                # Element exists but might be empty (e.g., an empty list or string)
                # Depending on IG definition of Must Support, this might still be a failure.
                # For simplicity here, we treat it as missing content.
                missing_elements << "#{element_path} (present but empty)"
              end
            end
          rescue => e
            # Handle potential errors during FHIRPath evaluation (e.g., invalid path)
            warning "Error evaluating FHIRPath expression '#{element_path}' on Organization/#{organization_id}: #{e.message}"
            missing_elements << "#{element_path} (evaluation error)"
          end
        end

        # Assert that no Must Support elements were found missing
        assert missing_elements.empty?, "The following Must Support elements were missing or empty in the retrieved Organization resource (ID: #{organization_id}): #{missing_elements.join(', ')}"

        # If the assertion passes, all specified elements were found
        pass "Successfully retrieved Organization/#{organization_id} and verified the presence of all specified Must Support elements: #{present_elements.join(', ')}."
      end
    end
  end
end