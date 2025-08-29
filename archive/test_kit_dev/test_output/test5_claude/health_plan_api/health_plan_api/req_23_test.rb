module Test5_claude
  class XmlFormatSupportGroup < Inferno::TestGroup
    id :xml_format_support
    title 'XML Format Support'
    description %(
      Verify that the server supports XML source formats for all Plan-Net interactions.
      The server SHOULD accept and return XML formatted resources.
    )

    fhir_client do
      url :url
    end

    test do
      id :xml_read_support
      title 'Server supports reading resources in XML format'
      description %(
        Verify that the server can return resources in XML format when requested
        with an Accept header of application/fhir+xml
      )
      input :known_resource_id
      
      run do
        fhir_client.set_headers('Accept' => 'application/fhir+xml')
        fhir_read(:organization, known_resource_id)

        assert_response_status(200)
        assert_valid_resource
        
        content_type = reply.response[:headers]['content-type']
        assert content_type.include?('application/fhir+xml'), 
          "Expected XML content type but got #{content_type}"
      end
    end

    test do
      id :xml_search_support  
      title 'Server supports searching resources in XML format'
      description %(
        Verify that the server can return search results in XML format when requested
        with an Accept header of application/fhir+xml
      )

      run do
        fhir_client.set_headers('Accept' => 'application/fhir+xml')
        fhir_search(:organization)

        assert_response_status(200)
        assert_valid_resource
        
        content_type = reply.response[:headers]['content-type']
        assert content_type.include?('application/fhir+xml'),
          "Expected XML content type but got #{content_type}"

        assert_resource_type('Bundle')
      end
    end

    test do
      id :xml_create_support
      title 'Server supports creating resources in XML format'
      description %(
        Verify that the server can accept resources in XML format when sent
        with a Content-Type header of application/fhir+xml
      )

      run do
        org = FHIR::Organization.new(
          name: 'Test Organization'
        )
        
        fhir_client.set_headers({
          'Content-Type' => 'application/fhir+xml',
          'Accept' => 'application/fhir+xml'
        })

        fhir_create(org, format: :xml)

        assert_response_status(201)
        assert_valid_resource
        
        content_type = reply.response[:headers]['content-type']
        assert content_type.include?('application/fhir+xml'),
          "Expected XML content type but got #{content_type}"
      end
    end

    test do
      id :xml_update_support
      title 'Server supports updating resources in XML format'
      description %(
        Verify that the server can accept resource updates in XML format when sent
        with a Content-Type header of application/fhir+xml
      )
      input :known_resource_id

      run do
        fhir_client.set_headers('Accept' => 'application/fhir+xml')
        resource = fhir_read(:organization, known_resource_id).resource
        
        resource.name = "Updated #{resource.name}"

        fhir_client.set_headers({
          'Content-Type' => 'application/fhir+xml',
          'Accept' => 'application/fhir+xml'
        })

        fhir_update(resource, format: :xml)

        assert_response_status(200)
        assert_valid_resource
        
        content_type = reply.response[:headers]['content-type']
        assert content_type.include?('application/fhir+xml'),
          "Expected XML content type but got #{content_type}"
      end
    end
  end
end