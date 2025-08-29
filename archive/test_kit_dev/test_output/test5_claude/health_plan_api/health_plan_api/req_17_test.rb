module Test5_claude
  class DeletedResourceResponseGroup < Inferno::TestGroup
    id :deleted_resource_response
    title 'Deleted Resource Response Tests'
    description %(
      Verify that the server returns appropriate response for deleted resources:
      - Status code 410 (Gone) for deleted resources
      - Proper response structure and headers
    )

    test do
      id :deleted_resource_response_test
      title 'Server returns 410 status for deleted resources'
      description %(
        This test verifies that when requesting a deleted resource, 
        the server responds with HTTP status code 410 (Gone).
      )
      
      input :patient_id
      
      run do
        # First create and then delete a test patient
        test_patient = FHIR::Patient.new(
          name: [{ given: ['Test'], family: 'Patient' }]
        )
        
        fhir_create(test_patient)
        created_id = resource.id
        
        fhir_delete(:patient, created_id)
        assert_response_status(200)
        
        # Now try to read the deleted patient
        fhir_read(:patient, created_id)
        
        assert_response_status(410), 
          'Server did not return 410 status code for deleted resource'
          
        assert_response_headers_include('content-type')
      end
    end

    test do
      id :deleted_resource_response_validation
      title 'Validate response content for deleted resources'
      description %(
        This test verifies that the response for a deleted resource
        contains appropriate headers and content.
      )
      
      input :patient_id
      
      run do
        fhir_read(:patient, patient_id)
        
        skip_unless response.status == 410,
          'This test requires a 410 Gone response'
          
        assert_response_headers_include('content-type'), 
          'Response must include content-type header'
          
        assert response.headers['content-type'].include?('application/fhir+json'),
          'Content-type header must indicate FHIR JSON response'
      end
    end
  end
end