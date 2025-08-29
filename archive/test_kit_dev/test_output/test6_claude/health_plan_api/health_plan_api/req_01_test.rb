module Test6_claude
  class NoIdentifyingInfoRequiredGroup < Inferno::TestGroup
    id :no_pii_required_directory
    title 'No PII Required for Directory Queries'
    description %(
      Verify that the Plan-Net service does not require consumer identifying 
      information to perform directory queries.

      Requirement: A conformant Plan-Net service SHALL NOT require a directory
      mobile application to send consumer identifying information in order to
      query content.
    )

    test do
      id :directory_query_without_pii
      title 'Directory query succeeds without PII'
      description %(
        This test verifies that a basic directory query can be performed
        without providing any consumer identifying information.
      )

      input :directory_endpoint
      
      fhir_client do
        url :directory_endpoint
      end

      run do
        # Attempt basic practitioner search without any PII
        fhir_search(:practitioner)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
      end
    end

    test do
      id :directory_query_rejects_pii
      title 'Directory query with PII still succeeds'
      description %(
        This test verifies that when PII is provided, the server still processes
        the request normally rather than requiring/using the PII.
      )

      input :directory_endpoint

      fhir_client do
        url :directory_endpoint
      end

      run do
        # Attempt search with PII parameters that should be ignored
        params = {
          'patient.identifier': 'TEST-PAT-001',
          'patient.name': 'Test Patient',
          'patient.birthdate': '1970-01-01'
        }

        fhir_search(:practitioner, params: params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries

        # Verify same results returned as basic search
        basic_search = fhir_search(:practitioner)
        assert_response_status(200)
        
        basic_results = basic_search.resource.entry&.map(&:resource)&.map(&:id)
        pii_results = resource.entry&.map(&:resource)&.map(&:id)

        assert basic_results == pii_results,
          'Search results with PII parameters should match basic search results'
      end
    end

    def assert_valid_bundle_entries
      assert resource.entry&.length&.positive?,
        'Search response bundle must contain entries'
      
      resource.entry.each do |entry|
        assert entry.resource.present?, 'All bundle entries must contain resources'
      end
    end
  end
end