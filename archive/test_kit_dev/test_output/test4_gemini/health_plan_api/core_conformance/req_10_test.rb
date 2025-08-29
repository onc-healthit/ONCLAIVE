# frozen_string_literal: true

module Test4_gemini
  class PractitionerNetworkDocumentationTest < Inferno::TestGroup
    id :req_10_practitioner_network_documentation
    title 'REQ-10: Network Documentation for Practitioners'
    description %(
      Verify that the Health Plan API documents practitioner network participation using PractitionerRole instances linked to Networks.
    )

    test do
      id :req_10_practitioner_role_network_reference
        title 'PractitionerRole resources contain a reference to a Network resource'
        description %(
          Search for PractitionerRole resources and ensure each one includes a reference to a Network resource.
        )
        input :practitioner_role_search_params

        run do
          fhir_search(:practitioner_role, search: { parameters: practitioner_role_search_params })

          assert_response_status(200)
          assert_bundle_response

          resource_types = resources_in_bundle.map(&:resourceType).uniq
          assert resource_types.include?('PractitionerRole'), 'No PractitionerRole resources found in the bundle.'

          invalid_practitioner_roles = resources_in_bundle.select do |resource|
            resource.resourceType == 'PractitionerRole' && resource.telecom.blank?
          end

          assert invalid_practitioner_roles.empty?, "The following PractitionerRole resources do not contain a 'telecom' element: #{invalid_practitioner_roles.map(&:id).join(', ')}"
        end
      end
  end
end