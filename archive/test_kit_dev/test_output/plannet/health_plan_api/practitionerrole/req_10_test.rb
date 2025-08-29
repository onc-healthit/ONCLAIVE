# frozen_string_literal: true

module Plannet
  # Test group for REQ-10: Network documentation for practitioners
  # Description: "Health Plan API SHALL document practitioner network participation
  # using PractitionerRole instances linked to Networks"
  # Actor: Health Plan API
  # Conformance: SHALL
  class Req10PractitionerRoleNetworkTestGroup < Inferno::TestGroup
    id :plannet_req_10_practitioner_role_network
    title 'REQ-10: Network Documentation for Practitioners'
    description %(
      # Background
      The #{title} verifies that the Health Plan API documents practitioner
      network participation using `PractitionerRole` instances linked to `Network` resources,
      as required by REQ-10.

      # Test Methodology
      This test searches for `PractitionerRole` resources on the FHIR server.
      It then checks if at least one `PractitionerRole` resource exists and
      contains a valid reference to a `Network` resource in its `network` element.
      The test ensures that the server uses the specified structure for documenting
      network participation.

      - **SHALL** document practitioner network participation using PractitionerRole instances linked to Networks.

      # Conformance
      - Tested Resource: `PractitionerRole`
      - Interaction: `search-type`
      - Element: `PractitionerRole.network` (must contain a Reference to a Network)
    )

    # This assumes the fhir_client is configured externally,
    # typically in the parent suite or group.
    # Example:
    # fhir_client do
    #   url :server_url
    #   bearer_token :access_token # if applicable
    # end

    test do
      id :plannet_req_10_practitioner_role_references_network
      title 'PractitionerRole resources link to Network resources'
      description %(
        Verifies that the server provides at least one `PractitionerRole` resource
        that references a `Network` resource via the `PractitionerRole.network` element.
        This confirms that the API documents network participation as required.
      )
      # No specific inputs needed for this test beyond FHIR client configuration

      run do
        # Step 1: Search for PractitionerRole resources
        fhir_search(:practitioner_role)

        # Step 2: Validate the search response
        assert_response_status([200, 201])
        assert_resource_type(:bundle)
        info "Successfully received search response for PractitionerRole resources."

        # Step 3: Check if any PractitionerRole resources were returned
        bundle = resource
        practitioner_roles = bundle.entry&.map(&:resource)&.select { |res| res.resourceType == 'PractitionerRole' }

        # If no PractitionerRole resources are found, the server cannot demonstrate
        # conformance to this requirement.
        assert practitioner_roles.present?, "No PractitionerRole resources found on the server. " \
                                            "The server must provide PractitionerRole resources to document network participation as required by REQ-10."

        info "Found #{practitioner_roles.count} PractitionerRole resource(s) in the search response."

        # Step 4: Validate PractitionerRole resources and check for Network references
        found_network_reference = false
        practitioner_roles_checked = 0

        practitioner_roles.each do |pr_role|
          # Validate the resource structure against base FHIR specification.
          # This helps ensure the resource itself is well-formed.
          # Use `resource: pr_role` to validate a specific resource from the bundle.
          # `profile_url: nil` explicitly validates against the base FHIR spec.
          assert_valid_resource(resource: pr_role, profile_url: nil)
          practitioner_roles_checked += 1

          # Check if the 'network' element is present and contains at least one reference
          next unless pr_role.network.present? && pr_role.network.any?

          # Check if any of the references in the 'network' element point to a Network resource
          has_valid_network_ref = pr_role.network.any? do |network_ref|
            network_ref.is_a?(FHIR::Reference) &&
              network_ref.reference.present? &&
              network_ref.reference.start_with?('Network/')
          end

          if has_valid_network_ref
            found_network_reference = true
            # Optional: Could break here if only one example is needed,
            # but checking all returned resources provides more thorough validation.
            # break
          end
        end

        # Step 5: Assert that at least one PractitionerRole with a valid Network reference was found
        assert found_network_reference, "No PractitionerRole resources were found containing a valid reference " \
                                        "to a Network resource in the 'network' element. Checked #{practitioner_roles_checked} PractitionerRole(s)."

        # Step 6: Pass if the assertion holds
        pass "Successfully verified that at least one PractitionerRole resource exists and references a Network resource via the 'network' element."
      end
    end
  end
end