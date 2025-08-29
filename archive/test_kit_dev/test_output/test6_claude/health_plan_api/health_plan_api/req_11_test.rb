module Test6_claude
  class RestfulBehaviorTest < Inferno::TestGroup
    id :restful_behavior_test
    title 'RESTful Behavior Implementation'
    description %(
      Verify that the Health Plan API implements RESTful behavior according to the FHIR specification.
      This includes testing:
      * Standard CRUD operations
      * Proper response codes
      * Content types and formats
      * Resource validation
    )

    test do
      id :resource_read_test
      title 'Server supports basic read interactions'
      description 'Verify that the server properly implements GET requests for resource read operations'
      
      fhir_client do
        url :url
      end

      run do
        skip_if !resources_found?, 'No resources available to test read operation'

        resource_type = available_resources.first
        resource_id = get_first_resource_id(resource_type)

        fhir_read(resource_type, resource_id)

        assert_response_status(200)
        assert_valid_resource
        assert_resource_type(resource_type)
        assert resource.id == resource_id, "Resource ID #{resource_id} does not match returned resource"
      end
    end

    test do
      id :resource_search_test 
      title 'Server supports search operations'
      description 'Verify that the server properly implements search operations'

      run do
        skip_if !resources_found?, 'No resources available to test search'

        resource_type = available_resources.first
        
        fhir_search(resource_type)
        
        assert_response_status(200)
        assert_resource_type('Bundle')
        assert resource.resourceType == 'Bundle', 'Expected Bundle but got ' + resource.resourceType
        assert ['searchset'].include?(resource.type), 'Expected searchset Bundle but got ' + resource.type
      end
    end

    test do
      id :content_type_test
      title 'Server supports appropriate content types'
      description 'Verify that the server handles content type headers correctly'

      run do
        skip_if !resources_found?, 'No resources available to test content types'

        resource_type = available_resources.first
        resource_id = get_first_resource_id(resource_type)

        # Test JSON
        fhir_client.set_headers({'Accept': 'application/fhir+json'})
        fhir_read(resource_type, resource_id)
        
        assert_response_status(200)
        assert_valid_json
        
        # Test XML
        fhir_client.set_headers({'Accept': 'application/fhir+xml'})
        fhir_read(resource_type, resource_id)
        
        assert_response_status(200)
        assert_valid_xml
      end
    end

    test do
      id :error_handling_test
      title 'Server implements proper error responses'
      description 'Verify that the server returns appropriate error responses'

      run do
        # Test 404 Not Found
        fhir_read(:Patient, 'NONEXISTENT-ID')
        assert_response_status(404)
        
        # Test 400 Bad Request
        fhir_search(:Patient, params: {invalid: 'parameter'})
        assert_response_status(400)
      end
    end

    def resources_found?
      !available_resources.empty?
    end

    def available_resources
      @available_resources ||= fhir_client.capability_statement.rest.first.resource.map(&:type)
    end

    def get_first_resource_id(resource_type)
      search_response = fhir_client.search(resource_type)
      return unless search_response.resource.entry&.first
      search_response.resource.entry.first.resource.id
    end

    def assert_valid_json
      assert_response_content_type('application/fhir+json')
      JSON.parse(response[:body])
    rescue JSON::ParserError
      assert false, 'Response body is not valid JSON'
    end

    def assert_valid_xml
      assert_response_content_type('application/fhir+xml')
      REXML::Document.new(response[:body])
    rescue REXML::ParseException
      assert false, 'Response body is not valid XML'
    end
  end
end