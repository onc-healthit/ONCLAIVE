module Test5_claude
  class NetworkProfileNPIHandlingGroup < Inferno::TestGroup
    id :network_profile_npi_handling
    title 'Network Profile NPI Handling'
    description %(
      Verify that NPI and CLIA identifiers are only populated for provider 
      organizations and not for other organization types.

      The NPI and CLIA identifier types are Must-Support elements that are
      intended only for provider organizations.
    )

    test do
      id :provider_org_identifiers
      title 'Provider Organizations have NPI and CLIA identifiers'
      description %(
        Verify that provider organizations properly include NPI and CLIA
        identifiers when appropriate.
      )
      
      run do
        # Search for provider organizations
        fhir_search(:organization, params: {
          type: 'prov'
        })
        assert_response_status(200)
        
        provider_orgs = resources.select do |org| 
          org.type&.any? { |t| t.coding&.any? { |c| c.code == 'prov' } }
        end
        
        skip_if provider_orgs.empty?, 'No provider organizations found to verify identifiers'

        provider_orgs.each do |org|
          has_npi = org.identifier&.any? do |id|
            id.system == 'http://hl7.org/fhir/sid/us-npi'
          end
          
          has_clia = org.identifier&.any? do |id|
            id.system == 'urn:oid:2.16.840.1.113883.4.7'
          end
          
          assert(has_npi || has_clia, 
            "Provider organization #{org.id} missing both NPI and CLIA identifiers")
        end
      end
    end

    test do
      id :non_provider_org_identifiers
      title 'Non-Provider Organizations do not have NPI/CLIA identifiers'
      description %(
        Verify that non-provider organizations do not include NPI or CLIA
        identifiers which are intended only for provider organizations.
      )
      
      run do
        # Search for non-provider organizations
        fhir_search(:organization, params: {
          'type:not' => 'prov'  
        })
        assert_response_status(200)
        
        non_provider_orgs = resources.select do |org|
          org.type&.none? { |t| t.coding&.any? { |c| c.code == 'prov' } }
        end
        
        skip_if non_provider_orgs.empty?, 'No non-provider organizations found to verify identifiers'

        non_provider_orgs.each do |org|
          has_npi = org.identifier&.any? do |id|
            id.system == 'http://hl7.org/fhir/sid/us-npi'
          end
          
          has_clia = org.identifier&.any? do |id|
            id.system == 'urn:oid:2.16.840.1.113883.4.7'
          end
          
          assert(!has_npi && !has_clia,
            "Non-provider organization #{org.id} should not have NPI or CLIA identifiers")
        end
      end
    end
  end
end