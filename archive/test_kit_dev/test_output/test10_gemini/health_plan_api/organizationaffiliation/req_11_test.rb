module Test10Gemini
  class Req11OrganizationNetworkDocumentationGroup < Inferno::TestGroup
    id :req_11_organization_network_documentation
    title 'REQ-11: Network Documentation for Organizations'
    description %(
      This test group verifies that the Health Plan API documents organization
      network participation using OrganizationAffiliation instances linked to
      Networks, as specified in REQ-11.

      The tests will:
      1. Search for OrganizationAffiliation resources.
      2. Validate that these resources contain references to network Organizations.
      3. Verify that the referenced network Organizations are accessible.
    )
    # Conformance: SHALL
    # Actor: Health Plan API

    # Test 1: Search for OrganizationAffiliation resources
    test do
      id :req_11_search_for_organization_affiliation
      title 'Search for OrganizationAffiliation resources'
      description %(
        Verifies that the API returns OrganizationAffiliation resources.
        REQ-11 states: "Health Plan API SHALL document organization network
        participation using OrganizationAffiliation instances...". This implies
        such resources should be discoverable via search. The test expects at
        least one OrganizationAffiliation resource to be found.
      )
      makes_request :organization_affiliation_search

      run do
        fhir_search(:organization_affiliation, name: :organization_affiliation_search)

        assert_response_status(200)
        assert_resource_type(:bundle, resource: resource)

        org_aff_resources = resource.entry&.map(&:resource)&.compact&.select do |res|
          res.resourceType == 'OrganizationAffiliation'
        end

        assert org_aff_resources.present?, 'No OrganizationAffiliation resources found. The API SHALL document network participation using these resources.'

        scratch[:organization_affiliation_resources] = org_aff_resources
        info "Found #{org_aff_resources.length} OrganizationAffiliation resource(s)."
      end
    end

    # Test 2: Validate OrganizationAffiliation network linkage
    test do
      id :req_11_validate_organization_affiliation_network_linkage
      title 'Validate OrganizationAffiliation network linkage to Networks'
      description %(
        Verifies that found OrganizationAffiliation resources have a populated
        'network' element, and that each entry in 'network' correctly
        references an Organization resource (representing the Network).
      )
      # This test uses data prepared in the previous test (via scratch)
      # and does not make new HTTP requests itself, but analyzes prior results.

      run do
        org_aff_resources = scratch[:organization_affiliation_resources]
        skip_if org_aff_resources.blank?, 'No OrganizationAffiliation resources available from previous step to validate network linkage.'

        all_network_references = []
        found_valid_link = false

        org_aff_resources.each_with_index do |org_aff, index|
          assert org_aff.resourceType == 'OrganizationAffiliation', "Resource at index #{index} is not an OrganizationAffiliation."

          networks = org_aff.network
          assert networks.present? && networks.is_a?(Array) && networks.any?,
                 "OrganizationAffiliation/#{org_aff.id} must have a non-empty 'network' array."

          networks.each_with_index do |network_reference, net_idx|
            assert network_reference.present?,
                   "OrganizationAffiliation/#{org_aff.id} 'network' array item at index #{net_idx} is nil."
            assert network_reference.reference.is_a?(String) && network_reference.reference.present?,
                   "OrganizationAffiliation/#{org_aff.id} 'network.reference' at index #{net_idx} must be a non-empty string."

            reference_string = network_reference.reference
            assert reference_string.start_with?('Organization/'),
                   "OrganizationAffiliation/#{org_aff.id} 'network.reference' ('#{reference_string}') at index #{net_idx} must be a relative reference to an Organization resource (e.g., 'Organization/id')."

            # Basic validation of FHIR ID format
            org_id = reference_string.split('/').last
            assert org_id.match?(/^[A-Za-z0-9\-\.]{1,64}$/),
                   "OrganizationAffiliation/#{org_aff.id} 'network.reference' ('#{reference_string}') at index #{net_idx} contains an invalid Organization ID format."

            all_network_references << reference_string
            found_valid_link = true
          end
        end

        assert found_valid_link, 'No OrganizationAffiliation resources found with valid network links to Organization resources.'

        unique_network_references = all_network_references.uniq
        scratch[:network_organization_references] = unique_network_references
        info "Found #{unique_network_references.length} unique network Organization references to verify."
      end
    end

    # Test 3: Verify linked Network Organizations are resolvable
    test do
      id :req_11_verify_linked_network_organizations_exist
      title 'Verify linked Network Organizations are resolvable'
      description %(
        Verifies that each unique Organization resource referenced in
        OrganizationAffiliation.network (as a Network) can be successfully
        fetched from the server and is indeed an Organization resource.
      )
      # makes_request :network_organization_read (dynamically named in loop)

      run do
        network_references = scratch[:network_organization_references]
        skip_if network_references.blank?, 'No network Organization references available from previous step to verify.'

        assert network_references.any?, 'No network Organization references were collected to verify.'
        pass_count = 0

        network_references.each_with_index do |ref_string, index|
          org_id = ref_string.split('/').last
          # Each read request needs a unique name if we were to use `uses_request` later for specific ones.
          # For now, just ensuring they are made.
          fhir_read(:organization, org_id, name: "network_organization_read_#{index}")

          assert_response_status(200)
          assert_resource_type(:organization, resource: resource)
          assert resource.id == org_id, "Requested Organization with ID '#{org_id}' but received resource with ID '#{resource.id}'."
          pass_count += 1
        end

        if network_references.empty? && pass_count == 0
          # This case should be caught by skip_if or the assert network_references.any?
          # but as a safeguard:
          info 'No network references to check.'
        else
          pass "Successfully resolved and validated #{pass_count} out of #{network_references.length} unique network Organization references."
        end
      end
    end
  end
end