module Test6_claude
  class XmlFormatSupportGroup < Inferno::TestGroup
    id :xml_format_support
    title 'XML Format Support for Plan-Net Interactions'
    description %(
      Verify that the server supports XML source formats for all Plan-Net interactions.
      
      Server SHALL support receiving and returning XML formatted resources for read, 
      search and other interactions.
    )

    test do
      id :xml_format_read_test
      title 'XML format support for read interaction'
      description 'Verify server supports reading resources in XML format'
      
      input :resource_id
      
      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_XML
        fhir_client.set_header('Accept', 'application/fhir+xml')

        fhir_read(:organization, resource_id)
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+xml')
        assert_valid_resource
      end
    end

    test do
      id :xml_format_search_test  
      title 'XML format support for search interaction'
      description 'Verify server supports searching resources in XML format'

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_XML
        fhir_client.set_header('Accept', 'application/fhir+xml')

        fhir_search(:organization)
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+xml')
        assert_valid_bundle
        assert_bundle_response_type(:searchset)
      end
    end

    test do
      id :xml_format_create_test
      title 'XML format support for create interaction' 
      description 'Verify server supports creating resources in XML format'

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_XML
        fhir_client.set_header('Accept', 'application/fhir+xml')
        fhir_client.set_header('Content-Type', 'application/fhir+xml')

        organization = FHIR::Organization.new(
          name: 'Test Organization',
          active: true
        )
        
        fhir_create(organization)

        assert_response_status(201)
        assert_response_content_type('application/fhir+xml')
        assert_valid_resource
      end
    end

    test do
      id :xml_format_headers_test
      title 'XML format headers handled correctly'
      description 'Verify server handles XML format request/response headers appropriately'
      
      input :resource_id

      run do
        skip_if resource_id.nil?, 'No resource ID provided'

        # Test with XML Accept header
        fhir_client.set_header('Accept', 'application/fhir+xml')
        fhir_read(:organization, resource_id)
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+xml')

        # Test with XML Content-Type header
        fhir_client.set_header('Content-Type', 'application/fhir+xml')
        fhir_read(:organization, resource_id) 
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+xml')

        # Reset headers
        fhir_client.set_header('Accept', nil)
        fhir_client.set_header('Content-Type', nil)
      end
    end

  end
end