module Test5_claude
  class DirectoryQueryPiiTest < Inferno::TestGroup
    id :directory_query_pii_test
    title 'Directory Query PII Requirements'
    description %(
      Validates that a Plan-Net server does not require consumer identifying 
      information (PII) to perform directory queries.

      Requirement: A conformant Plan-Net service SHALL NOT require a directory
      mobile application to send consumer identifying information in order to
      query content.
    )

    test do
      id :basic_practitioner_search
      title 'Basic Practitioner search without PII'
      description %(
        Verify that a basic Practitioner search succeeds without providing
        any consumer identifying information.
      )

      run do
        # Attempt basic practitioner search without any PII
        fhir_search(:practitioner)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length >= 0, 
          'Server should return a Bundle with 0 or more entries'
      end
    end

    test do
      id :advanced_practitioner_search
      title 'Advanced Practitioner search with multiple parameters'
      description %(
        Verify that a Practitioner search with multiple search parameters 
        succeeds without requiring PII.
      )

      run do
        search_params = {
          specialty: 'http://nucc.org/provider-taxonomy|207R00000X',
          location: '90210',
          organization: 'example-org-id'
        }

        fhir_search(:practitioner, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource
        
        assert bundle.entry.length >= 0,
          'Server should return a Bundle with 0 or more entries'
      end
    end

    test do
      id :error_response_check
      title 'Error responses do not indicate PII requirements'
      description %(
        Verify that error responses from invalid searches do not indicate
        missing PII requirements.
      )

      run do
        # Intentionally invalid search to trigger error
        fhir_search(:practitioner, params: {invalid: 'parameter'})

        assert_response_status([400, 404, 422])

        skip_if response[:status] == 404, 'Server returned 404 Not Found'

        if response[:status] == 400 || response[:status] == 422
          operation_outcome = FHIR.from_contents(response[:body])
          
          assert operation_outcome.issue.none? { |issue|
            issue.diagnostics&.match?(/identification|identity|pii|personal/i)
          }, 'Error message should not indicate missing PII requirements'
        end
      end
    end
  end
end