module Test5Gpt
  class NoPiiRequirementTestGroup < Inferno::TestGroup
    id :req_01_no_pii_requirement
    title 'No PII Requirement for Directory Queries'
    description %(
      A conformant Plan-Net service SHALL NOT require a directory mobile application 
      to send consumer identifying information in order to query content. This test 
      verifies that the Health Plan API does not require any personally identifiable 
      information (PII) when querying the directory.
    )

    test do
      id :no_pii_requirement_test
      title 'Directory queries do not require PII'
      description %(
        This test checks that the Health Plan API can be queried without sending 
        any consumer identifying information. The server should respond successfully 
        to a query made without PII.
      )
      input :server_url

      run do
        fhir_client do
          url server_url
        end

        # Perform a basic query to the directory endpoint without any PII
        response = fhir_search(:organization)

        # Assert that the response is successful and does not require PII
        assert_response_status(200)
        assert_valid_resource
        assert response.resource.entry.any?, 'No entries were returned from the directory query'
      end
    end
  end
end