module Test5_claude
  class JsonFormatSupportGroup < Inferno::TestGroup
    id :json_format_support
    title 'JSON Format Support Tests'
    description %(
      Verify that the server supports JSON source formats for all Plan-Net interactions.
      The server SHALL support JSON for request and response payloads.
    )

    test do
      id :json_read_support
      title 'Server supports JSON format for read operations'
      description %(
        Verify that the server properly handles JSON format when reading resources
        by including JSON content-type headers and validating response formats.
      )
      
      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_JSON
        
        fhir_read(:organization, '123')
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+json')
        assert resource.is_a?(FHIR::Organization), 'Response resource is not valid JSON'
      end
    end

    test do
      id :json_search_support  
      title 'Server supports JSON format for search operations'
      description %(
        Verify that the server properly handles JSON format when searching for resources
        by including JSON content-type headers and validating response formats.
      )

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_JSON
        
        fhir_search(:organization)
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+json')
        assert_valid_bundle_resource
        assert resource.entry.first.resource.is_a?(FHIR::Organization), 'Bundle entries are not valid JSON'
      end
    end

    test do
      id :json_create_support
      title 'Server supports JSON format for create operations' 
      description %(
        Verify that the server properly handles JSON format when creating resources
        by including JSON content-type headers and validating response formats.
      )

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_JSON
        
        org = FHIR::Organization.new(name: 'Test Org')
        fhir_create(org)
        
        assert_response_status(201)
        assert_response_content_type('application/fhir+json')
        assert resource.is_a?(FHIR::Organization), 'Created resource is not valid JSON'
      end
    end

    test do
      id :json_update_support
      title 'Server supports JSON format for update operations'
      description %(
        Verify that the server properly handles JSON format when updating resources
        by including JSON content-type headers and validating response formats.
      )

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_JSON
        
        org = FHIR::Organization.new(id: '123', name: 'Updated Org')
        fhir_update(org)
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+json') 
        assert resource.is_a?(FHIR::Organization), 'Updated resource is not valid JSON'
      end
    end
  end
end