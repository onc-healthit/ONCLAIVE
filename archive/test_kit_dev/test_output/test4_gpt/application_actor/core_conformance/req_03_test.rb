module Test4Gpt
  class NoConsumerInformationInQueriesTestGroup < Inferno::TestGroup
    id :req_03_no_consumer_information_in_queries
    title 'REQ-03: No Consumer Information in Queries'
    description %(
      Application Actor SHALL NOT send consumer identifiable information when querying a Plan-Net service.
      This test ensures that no consumer identifiable information is included in the query parameters or headers.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :no_consumer_information_in_queries_test
      title 'Application Actor does not send consumer identifiable information in queries'
      description %(
        This test verifies that the Application Actor does not include any consumer identifiable information
        in the query parameters or headers when querying a Plan-Net service.
      )

      run do
        # Perform a FHIR search without consumer identifiable information
        response = fhir_search(:practitioner, params: { name: 'Smith' })

        # Assert that the request was successful
        assert_response_status(200)

        # Check headers and parameters for consumer identifiable information
        consumer_identifiable_keys = ['patient', 'patient_id', 'identifier', 'name', 'birthdate']
        headers_and_params = response.request.headers.merge(response.request.params)

        consumer_identifiable_keys.each do |key|
          assert headers_and_params[key].nil?, "Query contains consumer identifiable information: #{key}"
        end

        pass 'No consumer identifiable information was sent in the query.'
      end
    end
  end
end