module Test4_claude
  class OrganizationNetworkDocumentationGroup < Inferno::TestGroup
    id :organization_network_documentation
    title 'Network Documentation for Organizations'
    description %(
      Verify that the Health Plan API documents organization network participation 
      using OrganizationAffiliation instances that are properly linked to Networks.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :organization_affiliation_network_links
      title 'OrganizationAffiliation resources link organizations to networks'
      description %(
        This test verifies that OrganizationAffiliation resources:
        - Exist in the system
        - Link to valid Organization resources
        - Reference Network resources properly
      )
      
      input :organization_id
      
      run do
        # Search for OrganizationAffiliations linked to the test organization
        fhir_search(:organizationaffiliation, params: {
          organization: organization_id,
          _include: ['OrganizationAffiliation:network']
        })
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_response

        skip_if bundle.total.zero?, 'No OrganizationAffiliation resources found for the organization'

        bundle.entry.each do |entry|
          next unless entry.resource.resourceType == 'OrganizationAffiliation'
          
          org_affiliation = entry.resource

          # Verify organization reference
          assert org_affiliation.organization&.reference&.include?(organization_id),
            "OrganizationAffiliation must reference the specified organization"

          # Verify network references exist
          assert org_affiliation.network&.any?, 
            "OrganizationAffiliation must have at least one network reference"

          org_affiliation.network.each do |network_ref|
            assert network_ref.reference&.start_with?('Organization/'),
              "Network references must be Organization resources"
          end

          # Validate included network resources
          included_networks = bundle.entry.select do |e| 
            e.resource.resourceType == 'Organization' &&
            org_affiliation.network.any? { |ref| ref.reference == "Organization/#{e.resource.id}" }
          end

          assert included_networks.any?,
            "Referenced networks must be included in the response"

          included_networks.each do |network|
            assert network.resource.resourceType == 'Organization',
              "Referenced networks must be Organization resources"
            assert_valid_resource(resource: network.resource)
          end
        end

        pass "Successfully validated OrganizationAffiliation network documentation"
      end
    end

    test do
      id :network_type_validation 
      title 'Networks are properly identified as network organizations'
      description %(
        Verify that referenced network Organizations are properly typed as networks
        through appropriate type coding.
      )

      depends_on :organization_affiliation_network_links

      run do
        network_orgs = resources_in_bundle.select { |r| r.resourceType == 'Organization' }
        
        assert network_orgs.any?, 
          "No network Organization resources found in previous response"

        network_orgs.each do |network|
          assert network.type&.any? { |t| t.coding&.any? { |c| c.code == 'ntwk' } },
            "Network Organization #{network.id} must have type code 'ntwk'"
        end

        pass "Successfully validated network organization types"
      end
    end
  end
end