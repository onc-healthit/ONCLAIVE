module Test5_claude
  class JsonFormatSupportGroup < Inferno::TestGroup
    id :json_format_support
    title 'JSON Format Support Tests'
    description %(
      Tests for REQ-10: Support json source formats for all Plan-Net interactions.
      
      The server SHALL support JSON format for all Plan-Net API interactions.
      This test group verifies proper JSON format support through various operations.
    )

    test do
      id :json_format_read_test
      title 'Server supports JSON format for read operations'
      description %(
        Verify that the server properly handles JSON format when reading resources.
        The server should return valid JSON and accept JSON format request headers.
      )
      
      input :test_resource_id
      
      run do
        headers = { 'Accept': 'application/fhir+json' }
        
        fhir_read(:PractitionerRole, test_resource_id, headers: headers)
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+json')
        
        assert_valid_json(response[:body])
        assert resource.is_a?(FHIR::PractitionerRole), 'Response resource is not a valid FHIR PractitionerRole'
      end
    end

    test do
      id :json_format_search_test  
      title 'Server supports JSON format for search operations'
      description %(
        Verify that the server properly handles JSON format for search operations.
        Search responses should be returned as valid JSON bundles.
      )

      run do
        headers = { 'Accept': 'application/fhir+json' }
        
        fhir_search(:PractitionerRole, headers: headers)
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+json')
        
        assert_valid_json(response[:body])
        assert resource.is_a?(FHIR::Bundle), 'Response resource is not a valid FHIR Bundle'
        assert resource.entry.any? { |e| e.resource.is_a?(FHIR::PractitionerRole) }
      end
    end

    test do
      id :json_format_create_test
      title 'Server supports JSON format for create operations' 
      description %(
        Verify that the server properly handles JSON format when creating resources.
        The server should accept JSON-formatted resources and return JSON responses.
      )

      run do
        practitioner_role = FHIR::PractitionerRole.new(
          active: true,
          practitioner: { reference: 'Practitioner/example' }
        )

        headers = {
          'Accept': 'application/fhir+json',
          'Content-Type': 'application/fhir+json'
        }

        fhir_create(practitioner_role, headers: headers)
        
        assert_response_status(201)
        assert_response_content_type('application/fhir+json')
        
        assert_valid_json(response[:body])
        assert resource.is_a?(FHIR::PractitionerRole), 'Response resource is not a valid FHIR PractitionerRole'
      ensure
        fhir_delete(:PractitionerRole, resource.id) if resource&.id
      end
    end

    def assert_valid_json(json_string)
      error_message = 'Response body is not valid JSON'
      assert JSON.parse(json_string), error_message
    rescue JSON::ParserError
      assert false, error_message
    end
  end
end