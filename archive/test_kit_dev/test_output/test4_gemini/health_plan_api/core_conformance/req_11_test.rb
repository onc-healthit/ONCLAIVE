# frozen_string_literal: true

module Test4_gemini
  class Req11NetworkDocumentationForOrganizationsTest < Inferno::TestGroup
    id :req_11_network_documentation_for_organizations
    title 'REQ-11: Network documentation for organizations'
    description %(
      Health Plan API SHALL document organization network participation using OrganizationAffiliation instances linked to Networks
    )

    test do
      id :req_11_organization_affiliation_references_network
      title 'OrganizationAffiliation resources reference Networks'
      description %(
        Verify that OrganizationAffiliation resources correctly reference Network resources.
      )

      run do
        skip_if_not_supported(:OrganizationAffiliation)

        fhir_read(:organization_affiliation, params: { '_profile' => 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation' })

        assert_response_status(200)
        assert_bundle_response
        assert_valid_resource_paths(:OrganizationAffiliation)

        resources = response[:resource].entry.map(&:resource)

        skip_if resources.empty?, 'No OrganizationAffiliation resources found to test.'

        resources.each do |resource|
          network_references = resource.network.map(&:reference)
          assert !network_references.empty?, 'OrganizationAffiliation resource does not reference any Network resources.'

          network_references.each do |reference|
            assert_valid_reference(reference, :Network)
          end
        end

        pass
      end
    end
  end
end
