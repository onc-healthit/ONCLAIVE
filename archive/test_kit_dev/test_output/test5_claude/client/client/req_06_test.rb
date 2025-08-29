module Test5_claude
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_test
    title 'Must Support Data Elements Handling'
    description %(
      Validates that the client application can process resource instances containing
      Must Support data elements without generating errors or application failures.
      
      This test group verifies conformance with REQ-06:
      "Application actors SHALL be capable of processing resource instances containing 
      the Must Support data elements without generating an error or causing the 
      application to fail."
    )

    test do
      id :must_support_patient_elements
      title 'Process Patient with Must Support Elements'
      description %(
        Verify client can process a Patient resource containing all Must Support elements.
      )
      
      input :client_id
      uses_request :patient_with_must_support

      run do
        # Create test patient with all Must Support elements populated
        patient = FHIR::Patient.new(
          name: [{
            given: ['Test'],
            family: 'Patient'
          }],
          gender: 'female',
          birthDate: '1970-01-01',
          address: [{
            line: ['123 Test St'],
            city: 'TestCity',
            state: 'TS',
            postalCode: '12345'
          }]
        )

        # Send patient to client
        response = fhir_create(patient)
        assert_response_status(201)
        
        patient_id = response.resource.id
        
        # Verify client processed resource by requesting it back
        get_response = fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        
        retrieved = get_response.resource
        
        # Verify Must Support elements were processed
        assert retrieved.name.present?, 'Client failed to process name element'
        assert retrieved.gender.present?, 'Client failed to process gender element'
        assert retrieved.birthDate.present?, 'Client failed to process birthDate element'
        assert retrieved.address.present?, 'Client failed to process address element'

        # Clean up
        fhir_delete(:patient, patient_id)
      end
    end

    test do
      id :must_support_observation_elements  
      title 'Process Observation with Must Support Elements'
      description %(
        Verify client can process an Observation resource containing all Must Support elements.
      )

      input :client_id
      uses_request :observation_with_must_support

      run do
        # Create test observation with Must Support elements
        observation = FHIR::Observation.new(
          status: 'final',
          code: {
            coding: [{
              system: 'http://loinc.org',
              code: '8480-6',
              display: 'Systolic blood pressure'
            }]
          },
          subject: { reference: "Patient/#{client_id}" },
          effectiveDateTime: Time.now.iso8601,
          valueQuantity: {
            value: 120,
            unit: 'mmHg',
            system: 'http://unitsofmeasure.org',
            code: 'mm[Hg]'
          }
        )

        # Send to client
        response = fhir_create(observation)
        assert_response_status(201)
        
        observation_id = response.resource.id

        # Verify client processed resource
        get_response = fhir_read(:observation, observation_id)
        assert_response_status(200)
        assert_resource_type(:observation)

        retrieved = get_response.resource

        # Verify Must Support elements were processed
        assert retrieved.status.present?, 'Client failed to process status element'
        assert retrieved.code.present?, 'Client failed to process code element'
        assert retrieved.subject.present?, 'Client failed to process subject element'
        assert retrieved.effectiveDateTime.present?, 'Client failed to process effectiveDateTime element'
        assert retrieved.valueQuantity.present?, 'Client failed to process valueQuantity element'

        # Clean up
        fhir_delete(:observation, observation_id)
      end
    end
  end
end