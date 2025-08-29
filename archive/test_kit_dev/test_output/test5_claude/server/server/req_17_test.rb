module Test5_claude
  class DeletedResourceResponseGroup < Inferno::TestGroup
    id :deleted_resource_response
    title 'Deleted Resource Response Test'
    description %(
      Verify that the server returns a 410 (Gone) status code when 
      requesting a deleted resource.

      The server SHALL return a 410 status code to indicate that the
      requested resource has been deleted.
    )

    test do
      id :deleted_resource_status_410
      title 'Server returns 410 status for deleted resources'
      description %(
        This test verifies that the server properly returns a 410 (Gone) 
        status code when requesting a resource that has been deleted.
      )

      input :patient_id
      
      run do
        # First create and then delete a test patient
        test_patient = FHIR::Patient.new(
          name: [{ given: ['Test'], family: 'Patient' }]
        )
        
        fhir_create(test_patient)
        created_id = resource.id
        assert_response_status(201)

        fhir_delete(:patient, created_id)
        assert_response_status(200)

        # Now try to read the deleted patient
        fhir_read(:patient, created_id)
        
        assert_response_status(410), 
          'Expected 410 (Gone) status when requesting deleted resource'

        assert_response_headers_include('content-type'),
          'Response did not include Content-Type header'
      end
    end
  end
end