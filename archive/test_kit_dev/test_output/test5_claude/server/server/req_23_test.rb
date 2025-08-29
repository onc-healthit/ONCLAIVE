module Test5_claude
  class XmlFormatSupportGroup < Inferno::TestGroup
    id :xml_format_support
    title 'XML Format Support'
    description %(
      Verify that the server supports XML source formats for all Plan-Net interactions.
      
      Conformance: SHOULD support XML format
      
      The test will make requests with XML format specified and validate that:
      * The server accepts the XML format request
      * The server returns responses in XML format when requested
    )

    test do
      id :xml_read_interaction
      title 'Server supports XML format for read interactions'
      description 'Verify server handles XML format for resource read operations'
      
      input :practitioner_id
      
      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_XML
        fhir_client.set_headers({'Accept': 'application/fhir+xml'})
        
        get("/Practitioner/#{practitioner_id}")
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+xml')
        assert_valid_resource
      end
    end

    test do
      id :xml_search_interaction 
      title 'Server supports XML format for search interactions'
      description 'Verify server handles XML format for resource search operations'

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_XML
        fhir_client.set_headers({'Accept': 'application/fhir+xml'})

        get('/Practitioner?_count=1')

        assert_response_status(200)
        assert_response_content_type('application/fhir+xml')
        assert_valid_bundle_response
      end
    end

    test do
      id :xml_create_interaction
      title 'Server supports XML format for create interactions' 
      description 'Verify server handles XML format for resource creation'

      run do
        fhir_client.default_format = FHIR::Formats::ResourceFormat::RESOURCE_XML
        fhir_client.set_headers({
          'Accept': 'application/fhir+xml',
          'Content-Type': 'application/fhir+xml'
        })

        practitioner = FHIR::Practitioner.new(
          active: true,
          name: [{ family: 'Smith', given: ['John'] }]
        )

        post('/Practitioner', practitioner)

        assert_response_status([201, 200])
        assert_response_content_type('application/fhir+xml')
        assert_valid_resource
      end
    end

    def assert_response_content_type(expected_type)
      assert response.headers['content-type']&.include?(expected_type), 
        "Expected content-type to include #{expected_type} but got #{response.headers['content-type']}"
    end

    def assert_valid_bundle_response
      assert_resource_type('Bundle')
      bundle = FHIR.from_contents(response.body)
      assert bundle.is_a?(FHIR::Bundle), 'Expected response to be a Bundle'
      assert bundle.entry&.any?, 'Expected Bundle to contain at least one entry'
      assert_valid_resource(resource: bundle)
    end
  end
end