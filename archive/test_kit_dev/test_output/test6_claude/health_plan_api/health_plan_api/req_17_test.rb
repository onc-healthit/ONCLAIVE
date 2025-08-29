module Test6_claude
  class DeletedResourceResponseGroup < Inferno::TestGroup
    id :deleted_resource_response
    title 'Deleted Resource Response Test'
    description %(
      Verify that the server returns the appropriate response (Status 410) 
      for a deleted resource.

      This test validates REQ-17 which states:
      The server SHALL return a 410 (Gone) status code when accessing a previously
      deleted resource.
    )

    test do
      id :deleted_resource_test
      title 'Server returns 410 status for deleted resource'
      description %(
        This test verifies that the server returns a 410 (Gone) status code
        when attempting to read a previously deleted resource.
      )

      input :patient_id,
            title: 'Patient ID',
            description: 'ID of a deleted patient resource'

      run do
        fhir_client.set_no_auth
        
        fhir_read(:patient, patient_id)

        assert_response_status(410)
        
        assert_valid_json(response[:body])
        
        operation_outcome = FHIR.from_contents(response[:body])
        assert operation_outcome.is_a?(FHIR::OperationOutcome), 
               'Server response body should be an OperationOutcome resource'

        assert operation_outcome.issue&.any? { |issue| issue.severity == 'error' },
               'OperationOutcome should contain an error issue'
      end
    end
  end
end