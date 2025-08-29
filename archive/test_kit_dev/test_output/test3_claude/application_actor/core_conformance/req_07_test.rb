module Test3_claude
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_processing
    title 'Must Support Elements Processing'
    description %(
      Validates that the Application Actor can process resource instances 
      containing Must Support data elements without errors or application failure.
      
      The test verifies that resources with Must Support elements can be:
      * Retrieved successfully
      * Processed without errors
      * Validated against profiles
    )

    test do
      id :must_support_patient_test
      title 'Process Patient with Must Support elements'
      description %(
        Verify that a Patient resource containing all Must Support elements
        can be processed successfully.
      )
      
      input :patient_id
      
      run do
        fhir_read(:patient, patient_id)
        
        assert_response_status(200)
        assert_resource_type(:patient)
        
        patient = resource
        
        # Verify must support elements are present and processable
        must_support_elements = [
          'name',
          'gender', 
          'birthDate',
          'address'
        ]
        
        must_support_elements.each do |element|
          assert patient.respond_to?(element), 
            "Patient resource missing must support element: #{element}"
          
          assert !patient.send(element).nil?,
            "Must support element #{element} is present but null"
        end
        
        assert_valid_resource
      end
    end

    test do
      id :must_support_condition_test 
      title 'Process Condition with Must Support elements'
      description %(
        Verify that a Condition resource containing all Must Support elements
        can be processed successfully.
      )
      
      input :condition_id
      
      run do
        fhir_read(:condition, condition_id)
        
        assert_response_status(200)
        assert_resource_type(:condition)
        
        condition = resource
        
        must_support_elements = [
          'clinicalStatus',
          'code',
          'subject',
          'onsetDateTime'
        ]
        
        must_support_elements.each do |element|
          assert condition.respond_to?(element),
            "Condition resource missing must support element: #{element}"
            
          assert !condition.send(element).nil?,
            "Must support element #{element} is present but null"
        end
        
        assert_valid_resource
      end
    end

    test do
      id :must_support_error_handling
      title 'Handle missing Must Support elements appropriately' 
      description %(
        Verify that resources with missing Must Support elements
        are handled gracefully without application errors.
      )
      
      run do
        # Create patient missing must support elements
        patient = FHIR::Patient.new(
          id: 'test-patient',
          active: true
        )
        
        # Attempt to process
        begin
          fhir_create(patient)
          assert_response_status([201, 400])
          
          if response[:status] == 400
            assert_valid_resource
            warning do
              assert response&.body&.include?('Missing must support element'),
                'Server should indicate missing must support elements in error response'
            end
          end
          
        rescue => e
          fail "Application error when processing resource with missing must support elements: #{e.message}"
        end
      end
    end
  end
end