module Test6_claude
  class NetworkProfileNPIHandling < Inferno::TestGroup
    id :network_profile_npi_handling
    title 'Network Profile NPI and CLIA Identifier Handling'
    description %(
      Validates that NPI and CLIA identifiers, which are Must-Support elements,
      are only populated for provider organizations and not for other organization types.
      
      The test verifies:
      * NPI and CLIA identifiers are present for provider organizations
      * NPI and CLIA identifiers are not present for non-provider organizations
    )

    test do
      id :provider_org_identifiers
      title 'Provider Organizations Have NPI and CLIA Identifiers'
      description %(
        Verifies that provider organizations have NPI and CLIA identifiers properly populated.
      )
      
      input :provider_org_id
      
      run do
        fhir_read(:organization, provider_org_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        org = resource

        # Verify organization is a provider
        assert org.type&.any? { |t| t.coding&.any? { |c| c.code == 'prov' } }, 
          'Organization must be typed as a provider'

        identifiers = org.identifier
        
        # Check for NPI
        npi = identifiers&.find { |id| id.system == 'http://hl7.org/fhir/sid/us-npi' }
        assert !npi.nil?, 'Provider organization must have an NPI identifier'
        
        # Check for CLIA
        clia = identifiers&.find { |id| id.system == 'urn:oid:2.16.840.1.113883.4.7' }
        assert !clia.nil?, 'Provider organization must have a CLIA identifier'
      end
    end

    test do
      id :non_provider_org_identifiers
      title 'Non-Provider Organizations Do Not Have NPI/CLIA Identifiers'
      description %(
        Verifies that non-provider organizations do not have NPI or CLIA identifiers populated.
      )
      
      input :non_provider_org_id
      
      run do
        fhir_read(:organization, non_provider_org_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        org = resource

        # Verify organization is not a provider
        assert !org.type&.any? { |t| t.coding&.any? { |c| c.code == 'prov' } },
          'Organization must not be typed as a provider'

        identifiers = org.identifier || []
        
        # Check no NPI exists
        npi = identifiers.find { |id| id.system == 'http://hl7.org/fhir/sid/us-npi' }
        assert npi.nil?, 'Non-provider organization should not have an NPI identifier'
        
        # Check no CLIA exists
        clia = identifiers.find { |id| id.system == 'urn:oid:2.16.840.1.113883.4.7' }
        assert clia.nil?, 'Non-provider organization should not have a CLIA identifier'
      end
    end
  end
end