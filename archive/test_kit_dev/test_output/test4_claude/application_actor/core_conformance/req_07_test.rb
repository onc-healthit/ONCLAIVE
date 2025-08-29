module Test4_claude
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_processing
    title 'Must Support Elements Processing'
    description %(
      Verify that the Application Actor can process resource instances containing Must Support 
      data elements without errors or application failure.
      
      This test group validates REQ-07: Application Actor SHALL process resource instances 
      containing Must Support data elements without errors or application failure.
    )

    test do
      id :must_support_patient_elements
      title 'Process Patient resource with Must Support elements'
      description %(
        Verify that a Patient resource containing all Must Support elements 
        can be processed without errors.
      )
      
      input :patient_id
      
      run do
        # Create test patient with must support elements
        patient = FHIR::Patient.new(
          id: patient_id,
          name: [{
            given: ['Test'],
            family: 'Patient'
          }],
          gender: 'female',
          birthDate: '1970-01-01',
          address: [{
            line: ['123 Test St'],
            city: 'Test City',
            state: 'TS',
            postalCode: '12345'
          }]
        )

        # Submit patient and verify processing
        fhir_create(patient)
        assert_response_status(201)
        
        # Read back and validate
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource

        # Verify must support elements preserved
        returned_patient = resource
        
        assert returned_patient.name.present?, 
          'Must Support element "name" not found in processed resource'
        assert returned_patient.gender.present?,
          'Must Support element "gender" not found in processed resource'
        assert returned_patient.birthDate.present?,
          'Must Support element "birthDate" not found in processed resource'
        assert returned_patient.address.present?,
          'Must Support element "address" not found in processed resource'

        # Clean up
        fhir_delete(:patient, patient_id)
      end
    end

    test do
      id :must_support_observation_elements  
      title 'Process Observation resource with Must Support elements'
      description %(
        Verify that an Observation resource containing all Must Support elements
        can be processed without errors.
      )

      input :patient_id

      run do
        # Create test observation with must support elements
        observation = FHIR::Observation.new(
          status: 'final',
          code: {
            coding: [{
              system: 'http://loinc.org',
              code: '8867-4',
              display: 'Heart rate'
            }]
          },
          subject: {
            reference: "Patient/#{patient_id}"
          },
          effectiveDateTime: Time.now.iso8601,
          valueQuantity: {
            value: 80,
            unit: 'beats/minute',
            system: 'http://unitsofmeasure.org',
            code: '/min'
          }
        )

        # Submit observation and verify processing
        fhir_create(observation)
        assert_response_status(201)
        created_id = resource.id

        # Read back and validate
        fhir_read(:observation, created_id)
        assert_response_status(200)
        assert_resource_type(:observation)
        assert_valid_resource

        # Verify must support elements preserved
        returned_obs = resource
        
        assert returned_obs.status.present?,
          'Must Support element "status" not found in processed resource'
        assert returned_obs.code.present?,
          'Must Support element "code" not found in processed resource'  
        assert returned_obs.subject.present?,
          'Must Support element "subject" not found in processed resource'
        assert returned_obs.effectiveDateTime.present?,
          'Must Support element "effectiveDateTime" not found in processed resource'
        assert returned_obs.valueQuantity.present?,
          'Must Support element "valueQuantity" not found in processed resource'

        # Clean up
        fhir_delete(:observation, created_id)
      end
    end
  end
end