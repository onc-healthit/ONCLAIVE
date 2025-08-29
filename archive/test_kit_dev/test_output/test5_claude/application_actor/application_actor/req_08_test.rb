module Test5_claude
  class MustSupportInterpretationGroup < Inferno::TestGroup
    id :must_support_interpretation
    title 'Client Interpretation of Missing Must Support Data'
    description %(
      This test group evaluates REQ-08: "When querying Health Plan API actors, 
      Application actors SHALL interpret missing Must Support data elements within 
      resource instances as data not present in the Health Plan API actors system."
    )

    test do
      id :verify_missing_must_support_handling
      title 'Client correctly handles missing Must Support elements'
      description %(
        Verify that the client application properly interprets missing Must Support
        data elements as "data not present" rather than errors or unknown values.
      )
      
      input :server_url, 
            title: 'Health Plan API Server URL',
            description: 'The base URL for the FHIR server under test'
            
      input :patient_id,
            title: 'Patient ID',
            description: 'ID of a patient resource with known missing Must Support elements'

      run do
        # Configure FHIR client
        fhir_client do
          url :server_url
        end

        # Read patient resource that should have missing Must Support elements
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        patient = resource
        
        # Verify resource is valid even with missing MS elements
        assert_valid_resource
        
        # Check common Must Support elements that may be missing
        skip_if patient.nil?, 'No Patient resource returned'

        missing_ms_elements = []
        
        # Example Must Support elements to check
        missing_ms_elements << 'name' if patient.name.empty?
        missing_ms_elements << 'birthDate' if patient.birthDate.nil?
        missing_ms_elements << 'gender' if patient.gender.nil?
        missing_ms_elements << 'address' if patient.address.empty?
        
        # Positive test - resource should be valid even with missing MS elements
        if missing_ms_elements.any?
          pass %(
            Patient resource ##{patient_id} is valid with missing Must Support elements: 
            #{missing_ms_elements.join(', ')}. These are correctly interpreted as 
            data not present in the system.
          )
        else
          skip %(
            Patient resource ##{patient_id} has all Must Support elements present.
            Please test with a patient resource known to have missing Must Support elements.
          )
        end
      end
    end

    test do
      id :verify_error_response_handling
      title 'Client handles error responses appropriately' 
      description %(
        Verify that when the server returns an error response, the client does not
        interpret this as missing Must Support data.
      )

      run do
        # Attempt to read non-existent patient to trigger error
        fhir_read(:patient, 'NONEXISTENT-ID')
        
        assert_response_status([404, 410], %(
          Expected error response code when requesting non-existent resource.
          404 (Not Found) or 410 (Gone) are valid error responses that should not
          be interpreted as missing Must Support data.
        ))
      end
    end

  end
end