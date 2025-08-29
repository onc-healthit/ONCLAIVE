require_relative '../../validation_test'
require_relative '../../generator/group_metadata'

module Plannet
  class NetworkDocumentationGroup < Inferno::TestGroup
    include Plannet::ValidationTest

    id :plannet_req_11_network_documentation_group
    title 'REQ-11: Network Documentation for Organizations'
    short_title 'Network Documentation'
    description %(
      # Background
      The REQ-11 requirement states that the Health Plan API SHALL document
      organization network participation using OrganizationAffiliation instances
      linked to Networks. This test group verifies that the server makes
      OrganizationAffiliation resources available and that these resources
      correctly reference Network resources.

      # Test Methodology
      This test group performs a search for OrganizationAffiliation resources.
      It then checks if any resources were returned. If resources are found,
      it iterates through each OrganizationAffiliation resource returned and
      validates the following:
      1. The resource is a valid FHIR resource.
      2. The resource contains the `network` element.
      3. The `network` element is an array of References.
      4. Each Reference within the `network` array points to a `Network` resource
         (i.e., the `reference` string starts with "Network/").

      If no OrganizationAffiliation resources are found, the test fails as the
      server does not meet the requirement to document network participation
      using this resource type. If any found OrganizationAffiliation resource
      fails the validation checks, the test also fails.
    )
    input :url
    output :organization_affiliation_list

    # Ensure FHIR client setup for this group
    fhir_client do
      url :url
      # Assuming bearer token authentication, adjust if needed
      # bearer_token :access_token
    end

    test do
      id :plannet_req_11_organization_affiliation_search
      title 'Search for OrganizationAffiliation resources'
      description %(
        Verify that the server supports searching for OrganizationAffiliation resources.
        This test performs a search for OrganizationAffiliation resources and expects a 200 OK response.
      )
      # Makes a basic search request for OrganizationAffiliation resources
      run do
        fhir_search(:organization_affiliation)

        assert_response_status(200)
        assert_resource_type(:bundle)
        # Pass the list of found resource IDs for potential use in subsequent tests
        # output organization_affiliation_list: resource.entry.map { |e| e.resource.id }.join(',') if resource.entry.present?

      end
    end

    test do
      id :plannet_req_11_org_affiliation_links_network
      title 'OrganizationAffiliation resources link to Network resources'
      description %(
        Verify that OrganizationAffiliation resources returned by the server
        contain references to Network resources in the 'network' element,
        as required by REQ-11.
      )
      # No specific inputs needed beyond the FHIR client URL (inherited)
      # Output is implicitly the test result (pass/fail/skip)

      run do
        # Retrieve the Bundle from the previous search test if possible, or perform search again
        # This assumes the search test ran successfully and stored the result if needed,
        # otherwise, we re-run the search. A direct search is simpler here.
        fhir_search(:organization_affiliation)

        assert_response_status(200)
        assert_resource_type(:bundle)

        affiliations = resource.entry&.map(&:resource)&.select { |res| res.resourceType == 'OrganizationAffiliation' }

        # Requirement is SHALL document, so failure if none are found
        assert affiliations.present?, "No OrganizationAffiliation resources found. Server SHALL document network participation using OrganizationAffiliation instances."

        affiliations_validated = 0

        affiliations.each do |affiliation|
          # Basic FHIR validation for the resource itself
          assert_valid_resource(resource: affiliation, profile_url: nil) # No specific profile mentioned, validate against base FHIR

          network_references = affiliation.network
          assert network_references.present?, "OrganizationAffiliation/#{affiliation.id} is missing the required 'network' element."
          assert network_references.is_a?(Array), "OrganizationAffiliation/#{affiliation.id} 'network' element must be an Array, but found #{network_references.class}."

          # Ensure the array is not empty
          assert network_references.any?, "OrganizationAffiliation/#{affiliation.id} 'network' array is present but empty."

          current_affiliation_valid = false
          network_references.each_with_index do |network_ref, index|
            assert network_ref.present?, "OrganizationAffiliation/#{affiliation.id} contains a nil/empty entry at index #{index} in the 'network' array."
            assert network_ref.is_a?(FHIR::Reference), "OrganizationAffiliation/#{affiliation.id} 'network' element at index #{index} contains a non-Reference item: #{network_ref.class}"

            reference_string = network_ref.reference
            assert reference_string.present?, "OrganizationAffiliation/#{affiliation.id} 'network' reference at index #{index} is missing the 'reference' string."
            assert reference_string.start_with?('Network/'), "OrganizationAffiliation/#{affiliation.id} 'network' reference at index #{index} does not point to a Network resource (expected 'Network/...', found '#{reference_string}')"

            # If we reach here, this specific reference is valid
            current_affiliation_valid = true
          end

          # After checking all references for this affiliation, ensure at least one was valid (though the inner asserts handle this)
          # This assertion is slightly redundant if the inner loop asserts correctly, but confirms the overall structure per affiliation.
          assert current_affiliation_valid, "OrganizationAffiliation/#{affiliation.id} did not contain any valid references to a Network resource in its 'network' element."

          affiliations_validated += 1
        end

        # If the loop completes without assertion failures, the test passes.
        pass "Successfully validated #{affiliations_validated} OrganizationAffiliation resource(s). Each contains at least one valid reference to a Network resource in the 'network' element."
      end
    end
  end
end