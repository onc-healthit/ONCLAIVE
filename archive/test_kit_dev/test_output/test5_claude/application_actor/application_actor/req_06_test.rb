module Test5_claude
  class MustSupportDataElementsGroup < Inferno::TestGroup
    id :must_support_data_elements
    title 'Must Support Data Elements Processing'
    description %(
      Verify that Application actors can process resource instances containing 
      Must Support data elements without generating errors or application failures.
      
      Requirement: Application actors SHALL be capable of processing resource instances 
      containing the Must Support data elements without generating an error or causing 
      the application to fail.
    )

    test do
      id :must_support_patient_elements
      title 'Process Patient with Must Support elements'
      description %(
        Verify application can process a Patient resource containing all Must Support elements.
      )
      
      input :patient_id
      
      run do
        # Create test patient with all Must Support elements populated
        patient = FHIR::Patient.new(
          id: patient_id,
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

        begin
          # Attempt to process the patient resource
          fhir_create(patient)
          assert_response_status(201)
          
          # Verify created patient can be retrieved
          fhir_read(:patient, resource.id)
          assert_response_status(200)
          assert_resource_type(:patient)
          
          retrieved = resource
          
          # Verify Must Support elements were preserved
          assert retrieved.name.present?, 'Must Support element "name" not found in processed resource'
          assert retrieved.gender.present?, 'Must Support element "gender" not found in processed resource'
          assert retrieved.birthDate.present?, 'Must Support element "birthDate" not found in processed resource'
          assert retrieved.address.present?, 'Must Support element "address" not found in processed resource'

          pass 'Successfully processed Patient resource with Must Support elements'

        rescue => e
          fail "Error processing Must Support elements: #{e.message}"
        ensure
          # Cleanup
          fhir_delete(:patient, resource.id) if resource&.id
        end
      end
    end

    test do
      id :must_support_observation_elements
      title 'Process Observation with Must Support elements' 
      description %(
        Verify application can process an Observation resource containing all Must Support elements.
      )

      input :patient_id
      
      run do
        # Create test observation with Must Support elements
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

        begin
          # Attempt to process the observation resource
          fhir_create(observation)
          assert_response_status(201)
          
          # Verify created observation can be retrieved
          fhir_read(:observation, resource.id)
          assert_response_status(200)
          assert_resource_type(:observation)
          
          retrieved = resource
          
          # Verify Must Support elements were preserved
          assert retrieved.status.present?, 'Must Support element "status" not found in processed resource'
          assert retrieved.code.present?, 'Must Support element "code" not found in processed resource'
          assert retrieved.subject.present?, 'Must Support element "subject" not found in processed resource'
          assert retrieved.effectiveDateTime.present?, 'Must Support element "effectiveDateTime" not found in processed resource'
          assert retrieved.valueQuantity.present?, 'Must Support element "valueQuantity" not found in processed resource'

          pass 'Successfully processed Observation resource with Must Support elements'

        rescue => e
          fail "Error processing Must Support elements: #{e.message}"
        ensure
          # Cleanup
          fhir_delete(:observation, resource.id) if resource&.id
        end
      end
    end
  end
end