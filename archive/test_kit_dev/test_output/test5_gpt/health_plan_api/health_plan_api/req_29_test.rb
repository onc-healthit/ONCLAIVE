module Test5Gpt
  class NetworkProfileNpiHandlingGroup < Inferno::TestGroup
    id :req_29_network_profile_npi_handling
    title 'Network Profile NPI Handling'
    description %(
      Verify that the NPI and CLIA identifier types, which are Must-Support, 
      are only populated for provider organizations and not for other organization types.
    )

    test do
      id :req_29_npi_clia_identifier_test
      title 'NPI and CLIA identifiers are only populated for provider organizations'
      description %(
        This test checks that the NPI and CLIA identifiers are populated only 
        for organizations that are provider organizations. Other organization 
        types should not have these identifiers populated.
      )
      input :organization_id

      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        assert_resource_type(:organization)
        assert_valid_resource

        organization = resource
        identifiers = organization.identifier || []

        npi_clia_identifiers = identifiers.select do |identifier|
          identifier.system == 'http://hl7.org/fhir/sid/us-npi' || 
          identifier.system == 'http://hl7.org/fhir/sid/us-clia'
        end

        if organization.type.any? { |type| type.coding.any? { |coding| coding.code == 'prov' } }
          assert npi_clia_identifiers.any?, 'Provider organizations must have NPI or CLIA identifiers.'
        else
          assert npi_clia_identifiers.empty?, 'Non-provider organizations should not have NPI or CLIA identifiers.'
        end
      end
    end
  end
end