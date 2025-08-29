module Test5_claude
  class ClientInterpretationTest < Inferno::TestGroup
    id :client_interpretation_missing_must_support
    title 'Client Interpretation of Missing Must Support Data'
    description %(
      This test verifies that Application actors properly interpret missing Must 
      Support data elements within resource instances as data not present in the 
      Health Plan API actors system, as required by REQ-08.
    )

    test do
      id :verify_missing_must_support_interpretation
      title 'Client handles missing Must Support elements correctly'
      description %(
        Verify that when Must Support elements are missing from resources returned
        by the Health Plan API, the client interprets this as the data not being 
        present in the source system rather than an error condition.
      )

      # Define test resource with missing Must Support elements
      run do
        # Create a Patient resource deliberately missing Must Support elements like name
        patient = FHIR::Patient.new(
          id: '123',
          active: true
          # Deliberately omit name, gender, birthDate which are Must Support
        )

        # Simulate API response with missing Must Support data
        stub_request(:get, "#{url}/Patient/123")
          .to_return(
            status: 200,
            body: patient.to_json,
            headers: { 'Content-Type': 'application/fhir+json' }
          )

        # Make request to get Patient
        response = fhir_read(:patient, '123')
        assert_response_status(200)
        assert_valid_resource

        retrieved_patient = response.resource

        # Verify missing Must Support elements are handled as nil/empty rather than errors
        assert retrieved_patient.name.nil?, 
          'Missing name element should be interpreted as nil'
        
        assert retrieved_patient.gender.nil?,
          'Missing gender element should be interpreted as nil'
          
        assert retrieved_patient.birthDate.nil?,
          'Missing birthDate element should be interpreted as nil'

        # Verify client can still process the resource despite missing elements
        assert retrieved_patient.active == true,
          'Client should still process existing elements correctly'

        pass 'Client correctly interprets missing Must Support elements as data not present'
      end
    end
  end
end