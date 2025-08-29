module Test4Gpt
  class NetworkDocumentationTestGroup < Inferno::TestGroup
    id :req_11_network_documentation
    title 'Network Documentation for Organizations'
    description %(
      This test group verifies that the Health Plan API documents organization network participation
      using OrganizationAffiliation instances linked to Networks, as required by REQ-11.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :organization_affiliation_network_documentation
      title 'OrganizationAffiliation instances link organizations to networks'
      description %(
        This test checks if the Health Plan API documents organization network participation
        by ensuring that OrganizationAffiliation resources are linked to Networks.
      )
      input :organization_id

      run do
        # Search for OrganizationAffiliation resources for the given organization
        reply = fhir_search(:organization_affiliation, params: { organization: organization_id })
        
        assert_response_status(200)
        assert_bundle_response

        affiliations = reply.resource.entry.map(&:resource)
        assert affiliations.any?, 'No OrganizationAffiliation resources found for the given organization.'

        affiliations.each do |affiliation|
          assert affiliation.network.present?, 'OrganizationAffiliation does not link to any Network.'
          assert affiliation.network.all? { |network| network.reference.start_with?('Network/') },
                 'OrganizationAffiliation network references are not correctly formatted.'
        end

        pass 'All OrganizationAffiliation instances correctly link organizations to networks.'
      end
    end
  end
end