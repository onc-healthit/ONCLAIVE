module Test5Gpt
  class JsonFormatSupportTestGroup < Inferno::TestGroup
    id :req_10_json_format_support
    title 'JSON Format Support'
    description %(
      Verify that the Health Plan API supports JSON format for all Plan-Net interactions.
      This test ensures that the server can handle requests and responses in JSON format
      as required by the specification.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :json_format_support_test
      title 'Health Plan API supports JSON format'
      description %(
        This test sends a request to the Health Plan API and verifies that the response
        is in JSON format, ensuring compliance with the requirement that JSON is supported
        for all Plan-Net interactions.
      )
      input :resource_type, :resource_id

      run do
        fhir_read(resource_type.to_sym, resource_id, headers: { 'Accept' => 'application/fhir+json' })
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+json')
        
        assert_valid_resource
      end
    end
  end
end