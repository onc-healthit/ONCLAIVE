module Test6_claude
  class MustSupportDataElementsGroup < Inferno::TestGroup
    id :must_support_data_elements
    title 'Must Support Data Elements Handling'
    description %(
      Validates that the application can process resource instances containing 
      Must Support data elements without generating errors or application failure.
      
      Requirement: Applications SHALL be capable of processing resource instances 
      containing Must Support data elements without generating an error or causing
      the application to fail.
    )

    test do
      id :must_support_patient_elements
      title 'Process Patient with Must Support elements'
      description %(
        Verify application can process a Patient resource containing
        all Must Support elements without error.
      )
      
      input :patient_id
      
      run do
        # Create test patient with Must Support elements
        patient = FHIR::Patient.new(
          name: [{
            given: ['Test'],
            family: 'Patient'
          }],
          gender: 'male',
          birthDate: '1970-01-01',
          address: [{
            line: ['123 Test St'],
            city: 'Test City',
            state: 'TS',
            postalCode: '12345'
          }]
        )

        # Attempt to process the patient
        begin
          fhir_create(patient)
          assert_response_status(201)
          assert_resource_type(:patient)
          created_id = resource.id
          
          # Verify we can read it back
          fhir_read(:patient, created_id)
          assert_response_status(200)
          assert_resource_type(:patient)
          
          # Clean up
          fhir_delete(:patient, created_id)
          assert_response_status(200)
          
          pass 'Successfully processed Patient with Must Support elements'
          
        rescue StandardError => e
          fail "Error processing Must Support elements: #{e.message}"
        end
      end
    end

    test do
      id :must_support_observation_elements  
      title 'Process Observation with Must Support elements'
      description %(
        Verify application can process an Observation resource containing
        all Must Support elements without error.
      )

      input :patient_id
      
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
          subject: {
            reference: "Patient/#{patient_id}"
          },
          effectiveDateTime: Time.now.iso8601,
          valueQuantity: {
            value: 120,
            unit: 'mmHg',
            system: 'http://unitsofmeasure.org',
            code: 'mm[Hg]'
          }
        )

        begin
          fhir_create(observation)
          assert_response_status(201)
          assert_resource_type(:observation)
          created_id = resource.id
          
          # Verify we can read it back
          fhir_read(:observation, created_id)
          assert_response_status(200)
          assert_resource_type(:observation)
          
          # Clean up
          fhir_delete(:observation, created_id)
          assert_response_status(200)
          
          pass 'Successfully processed Observation with Must Support elements'
          
        rescue StandardError => e
          fail "Error processing Must Support elements: #{e.message}"
        end
      end
    end
  end
end