module Test5_gemini
  class NetworkProfileNpiHandlingTest < Inferno::TestGroup
    id :req_29_network_profile_npi_handling
    title 'Network Profile NPI Handling'
    description %(
      Verify that NPI and CLIA identifiers are not populated for organization types other than provider organizations.
    )

    test do
      id :req_29_npi_clia_population
      title 'NPI and CLIA identifiers are not populated for non-provider organizations'
      description %(
        Search for Organization resources and check if NPI and CLIA identifiers are populated for non-provider organization types.
      )

      run do
        fhir_read(:organization, '123')
        assert_response_status(200)
        assert_resource_type(:organization)
        assert_valid_resource

        # Add logic to iterate through Organization resources and check for NPI and CLIA identifiers
        # based on organization type. Assert that NPI and CLIA are not populated for non-provider
        # organizations.
      end
    end
  end
end