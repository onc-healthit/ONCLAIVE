module Test5_gemini
  class NoPiiForDirectoryQueriesTest < Inferno::Test
    id :req_01_no_pii_for_directory_queries
    title 'Directory queries do not require consumer identifying information'
    description %(
      A conformant Plan-Net service SHALL NOT require a directory mobile application 
      to send consumer identifying information in order to query content.
    )

    run do
      skip_if_not_supported(:Location, [:search])

      # Search for locations without providing any patient-specific parameters
      response = fhir_search(:location)

      assert_response_status(200)
      assert_response_header('Content-Type', 'application/fhir+json')

      # Additional assertions can be added here to validate the response content
      # based on the specific requirements of the directory query. For example:
      # - Assert that the response bundle contains at least one entry
      # - Assert that the returned Location resources have the expected properties

      pass 'Directory query executed successfully without providing consumer identifying information.'
    end
  end
end
