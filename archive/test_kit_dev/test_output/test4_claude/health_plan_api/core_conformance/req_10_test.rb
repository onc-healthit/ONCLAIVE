module Test4_claude
  class PractitionerNetworkTest < Inferno::TestGroup
    id :practitioner_network_documentation
    title 'Practitioner Network Documentation'
    description %(
      Validates that the Health Plan API properly documents practitioner network 
      participation using PractitionerRole instances that are linked to Networks.
      
      Requirement: Health Plan API SHALL document practitioner network participation 
      using PractitionerRole instances linked to Networks.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    input :url,
          title: 'Health Plan API URL',
          description: 'The base URL for the Health Plan API'

    input :bearer_token,
          title: 'Bearer Token',
          description: 'Bearer token for accessing the Health Plan API'

    test do
      id :practitioner_role_network_links
      title 'PractitionerRole resources are linked to Networks'
      description %(
        Verify that PractitionerRole resources contain valid references to Network resources.
      )

      run do
        # Search for PractitionerRole resources
        fhir_search(:practitionerrole)
        assert_response_status(200)
        assert_resource_type(:bundle)

        practitioner_roles = resource.entry.map(&:resource)
        assert practitioner_roles.present?, 'No PractitionerRole resources found'

        practitioner_roles.each do |role|
          # Verify network references exist
          network_refs = role.network
          assert network_refs.present?, 
                 "PractitionerRole #{role.id} has no network references"

          # Verify each network reference
          network_refs.each do |network_ref|
            assert network_ref.reference.present?,
                   "PractitionerRole #{role.id} has network reference without reference element"

            # Resolve and validate network reference
            fhir_read(:organization, network_ref.reference.split('/').last)
            assert_response_status(200)
            assert_resource_type(:organization)
            
            network = resource
            assert network.type&.any? { |t| t.coding&.any? { |c| c.code == 'ntwk' } },
                   "Referenced Organization #{network.id} is not typed as a network"
          end
        end
      end
    end

    test do
      id :network_practitioner_role_validation
      title 'Networks have valid PractitionerRole references'
      description %(
        Verify that Network resources can be found via PractitionerRole references.
      )

      run do
        # Search for Networks (Organizations with type=ntwk)
        fhir_search(:organization, params: {
          type: 'ntwk'
        })
        assert_response_status(200)
        assert_resource_type(:bundle)

        networks = resource.entry.map(&:resource)
        assert networks.present?, 'No Network resources found'

        networks.each do |network|
          # Search for PractitionerRoles referencing this network
          fhir_search(:practitionerrole, params: {
            network: "Organization/#{network.id}"
          })
          assert_response_status(200)
          assert_resource_type(:bundle)

          roles = resource.entry.map(&:resource)
          assert roles.present?,
                 "No PractitionerRole resources found referencing Network #{network.id}"

          # Validate each PractitionerRole
          roles.each do |role|
            assert_valid_resource(resource: role)
            assert role.practitioner.present?,
                   "PractitionerRole #{role.id} missing practitioner reference"
          end
        end
      end
    end
  end
end