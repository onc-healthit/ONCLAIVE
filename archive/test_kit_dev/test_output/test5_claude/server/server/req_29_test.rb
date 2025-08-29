module Test5_claude
  class NetworkProfileNPIHandlingGroup < Inferno::TestGroup
    id :network_profile_npi_handling
    title 'Network Profile NPI Handling'
    description %(
      This test group verifies that NPI and CLIA identifiers are only present
      on provider organization resources and not on other organization types.
      
      The NPI and CLIA identifier types are Must-Support elements intended
      specifically for provider organizations.
    )

    test do
      id :provider_org_identifiers
      title 'Provider organizations have NPI and CLIA identifiers'
      description %(
        Validates that provider organizations contain NPI and/or CLIA
        identifiers as appropriate.
      )
      
      run do
        # Search for provider organizations
        search_params = {
          'type': 'prov'
        }
        
        fhir_search(:organization, params: search_params)
        assert_response_status(200)
        assert_resource_type(:bundle)

        skip_if resource.entry.blank?, 'No provider organizations found'

        resource.entry.each do |entry|
          org = entry.resource
          identifiers = org.identifier&.map { |id| id.system }
          
          assert identifiers.present?, "Provider organization #{org.id} has no identifiers"
          
          has_npi = identifiers.include?('http://hl7.org/fhir/sid/us-npi')
          has_clia = identifiers.include?('urn:oid:2.16.840.1.113883.4.7')
          
          assert has_npi || has_clia,
            "Provider organization #{org.id} lacks both NPI and CLIA identifiers"
        end
      end
    end

    test do 
      id :non_provider_org_identifiers
      title 'Non-provider organizations do not have NPI/CLIA identifiers'
      description %(
        Validates that organizations not marked as providers do not contain
        NPI or CLIA identifiers.
      )

      run do
        # Search for non-provider organizations
        search_params = {
          'type:not': 'prov'  
        }

        fhir_search(:organization, params: search_params)
        assert_response_status(200)
        assert_resource_type(:bundle)

        skip_if resource.entry.blank?, 'No non-provider organizations found'

        resource.entry.each do |entry|
          org = entry.resource
          identifiers = org.identifier&.map { |id| id.system }
          next if identifiers.blank?

          has_npi = identifiers.include?('http://hl7.org/fhir/sid/us-npi') 
          has_clia = identifiers.include?('urn:oid:2.16.840.1.113883.4.7')

          assert !has_npi && !has_clia,
            "Non-provider organization #{org.id} contains NPI or CLIA identifiers"
        end
      end
    end

  end
end