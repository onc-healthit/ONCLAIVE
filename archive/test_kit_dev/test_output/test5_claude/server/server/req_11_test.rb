module Test5_claude
  class RestfulBehaviorGroup < Inferno::TestGroup
    id :restful_behavior_implementation
    title 'RESTful Behavior Implementation'
    description %(
      Verify that the server implements RESTful behavior according to the FHIR specification.
      This includes testing:
      * Proper implementation of HTTP verbs
      * Correct handling of content types
      * Appropriate status codes
      * Resource validation
    )

    test do
      id :restful_get_behavior
      title 'Server implements GET requests correctly'
      description 'Verify server handles GET requests according to FHIR RESTful specification'
      
      run do
        fhir_read(:patient, '123')
        assert_response_status([200, 404])
        assert_valid_json
        skip_if response.code == 404, 'No test patient found'
        
        assert_response_headers_contain('Content-Type', 'application/fhir+json')
        assert_response_headers_contain('ETag')
        assert_response_headers_contain('Last-Modified') 
      end
    end

    test do
      id :restful_post_behavior 
      title 'Server implements POST requests correctly'
      description 'Verify server handles POST requests according to FHIR RESTful specification'

      run do
        patient = FHIR::Patient.new(
          name: [{ given: ['Test'], family: 'Patient' }]
        )
        
        fhir_create(patient)
        assert_response_status(201)
        assert_response_headers_contain('Location')
        assert_response_headers_contain('Content-Location')
        assert_valid_resource
      end
    end

    test do
      id :restful_put_behavior
      title 'Server implements PUT requests correctly' 
      description 'Verify server handles PUT requests according to FHIR RESTful specification'

      run do
        patient = FHIR::Patient.new(
          id: '123',
          name: [{ given: ['Test'], family: 'Patient' }]
        )

        fhir_update(patient)
        assert_response_status([200, 201])
        assert_valid_resource
        
        if response.code == 200
          assert_response_headers_contain('Content-Location')
        end
      end
    end

    test do
      id :restful_delete_behavior
      title 'Server implements DELETE requests correctly'
      description 'Verify server handles DELETE requests according to FHIR RESTful specification'

      run do
        fhir_delete(:patient, '123')
        assert_response_status([200, 204])

        # Verify resource was actually deleted
        fhir_read(:patient, '123')
        assert_response_status(404)
      end
    end

    test do
      id :content_type_handling
      title 'Server handles content types correctly'
      description 'Verify server properly handles content type headers'

      run do
        # Test JSON support
        headers = { 'Accept' => 'application/fhir+json' }
        get('/metadata', headers: headers)
        assert_response_status(200)
        assert_response_headers_contain('Content-Type', 'application/fhir+json')

        # Test XML support
        headers = { 'Accept' => 'application/fhir+xml' }
        get('/metadata', headers: headers)
        assert_response_status([200, 406])
      end
    end

    test do
      id :error_handling
      title 'Server implements proper error handling'
      description 'Verify server returns appropriate error responses'

      run do
        # Test invalid resource
        bad_patient = FHIR::Patient.new
        fhir_create(bad_patient)
        assert_response_status(400)
        assert_response_headers_contain('Content-Type', 'application/fhir+json')
        
        # Test invalid resource ID
        get('/Patient/invalid_id')
        assert_response_status(404)
        assert_valid_json
      end
    end
  end
end