module Test5Gpt
  class XmlFormatSupportTestGroup < Inferno::TestGroup
    id :req_23_xml_format_support
    title 'XML Format Support'
    description %(
      This test group verifies that the Health Plan API supports XML source formats
      for all Plan-Net interactions as per requirement REQ-23.
    )

    test do
      id :xml_format_support_test
      title 'Server supports XML format for Plan-Net interactions'
      description %(
        Verify that the server can handle requests and responses in XML format
        for Plan-Net interactions.
      )
      input :server_url, :access_token

      run do
        fhir_client do
          url :server_url
          bearer_token :access_token
          headers 'Accept' => 'application/fhir+xml'
        end

        # Example FHIR read operation in XML format
        response = fhir_read(:patient, 'example-patient-id')

        assert_response_status(200)
        assert response[:headers]['content-type'].include?('application/fhir+xml'), 
               'Response content-type is not application/fhir+xml'

        # Additional assertions can be added here to validate XML content if needed
      end
    end
  end
end