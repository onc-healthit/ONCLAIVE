module Test5Gpt
  class NoPiiSendingTestGroup < Inferno::TestGroup
    id :req_02_no_pii_sending
    title 'No PII Sending by Clients'
    description %(
      A directory mobile application SHALL NOT send consumer identifiable information 
      when querying a Plan-Net service. This test verifies that no personally identifiable 
      information (PII) is sent in the request payloads when the application queries the service.
    )

    test do
      id :no_pii_in_request_test
      title 'Verify no PII is sent in requests'
      description %(
        This test checks that requests made to the Plan-Net service do not contain any 
        personally identifiable information (PII). The test will inspect the request payload 
        to ensure compliance with the requirement.
      )
      input :server_url, :access_token

      run do
        fhir_client do
          url :server_url
          bearer_token :access_token
        end

        # Perform a sample query to the Plan-Net service
        response = fhir_search(:organization)

        # Assert that the request does not contain PII
        request_payload = response.request[:payload]
        pii_patterns = [/name/i, /address/i, /phone/i, /email/i]

        pii_found = pii_patterns.any? { |pattern| request_payload.match?(pattern) }

        assert !pii_found, 'Request payload contains PII, which is not allowed.'
        pass 'No PII found in the request payload.'
      end
    end
  end
end