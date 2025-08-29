module Test6_claude
  class JsonFormatSupportGroup < Inferno::TestGroup
    id :json_format_support
    title 'JSON Format Support'
    description %(
      Verify that the server supports JSON source formats for all Plan-Net interactions.
      
      The server SHALL support JSON format for request and response payloads.
    )

    test do
      id :json_format_read_test
      title 'Server supports JSON format for read interactions'
      description %(
        Verify that the server can handle a read request with JSON format 
        and returns a JSON response.
      )
      
      input :test_resource_id
      
      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_JSON
        
        fhir_read(:organization, test_resource_id)
        
        assert_response_status(200)
        assert_content_type('application/fhir+json')
        assert_valid_json(response[:body])
      end
    end

    test do 
      id :json_format_search_test
      title 'Server supports JSON format for search interactions'
      description %(
        Verify that the server can handle a search request with JSON format
        and returns a JSON response bundle.
      )

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_JSON
        
        fhir_search(:organization)
        
        assert_response_status(200)
        assert_content_type('application/fhir+json')
        assert_valid_json(response[:body])
        assert_resource_type(:bundle)
      end
    end

    test do
      id :json_format_create_test  
      title 'Server supports JSON format for create interactions'
      description %(
        Verify that the server can handle a create request with JSON payload
        and returns a JSON response.
      )

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_JSON
        
        organization = FHIR::Organization.new(
          name: 'Test Organization',
          active: true
        )
        
        fhir_create(organization)
        
        assert_response_status(201)
        assert_content_type('application/fhir+json')
        assert_valid_json(response[:body])
      end
    end

    def assert_content_type(expected_type)
      content_type = response[:headers]['content-type']
      assert content_type&.include?(expected_type), 
        "Expected content-type to be #{expected_type} but found #{content_type}"
    end

    def assert_valid_json(body)
      assert JSON.parse(body).is_a?(Hash), 
        'Response body is not valid JSON'
    rescue JSON::ParserError => e
      assert false, "Response body is not valid JSON: #{e.message}"
    end
  end
end