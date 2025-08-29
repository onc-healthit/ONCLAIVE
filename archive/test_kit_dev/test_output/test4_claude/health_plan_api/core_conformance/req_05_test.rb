module Test4_claude
  class OptionalMustSupportElementsGroup < Inferno::TestGroup
    id :optional_must_support_elements
    title 'Optional Must Support Elements Handling'
    description %(
      Validates that the Health Plan API does not include Must Support data elements 
      in resource instances when information is not present and minimum cardinality is 0.
      
      Requirement: REQ-05
    )

    test do
      id :optional_must_support_validation
      title 'Verify absence of optional Must Support elements when data not present'
      description %(
        This test verifies that Must Support elements with minimum cardinality of 0
        are not included in resources when the data is not available.
      )
      
      # Define inputs needed
      input :patient_id
      
      run do
        # Get patient resource to check
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_valid_resource
        
        patient = resource

        # List of optional Must Support elements to check
        optional_ms_elements = [
          'Patient.telecom',
          'Patient.communication',
          'Patient.generalPractitioner'
        ]

        # Check each optional MS element
        optional_ms_elements.each do |element_path|
          element = patient.send(element_path.split('.').last)
          
          if element.nil? || (element.respond_to?(:empty?) && element.empty?)
            pass "Optional Must Support element #{element_path} correctly omitted when no data present"
          else
            if element.respond_to?(:empty?) && !element.empty?
              fail "Optional Must Support element #{element_path} was included with data when it should be omitted if no data present"
            end
          end
        end

      rescue Inferno::AssertionException => e
        fail e.message
      rescue StandardError => e
        error "Unexpected error checking optional Must Support elements: #{e.message}"
      end
    end

    test do
      id :required_elements_present 
      title 'Verify required elements are still present'
      description %(
        This test verifies that required elements (minimum cardinality > 0)
        are still present in the resource.
      )

      input :patient_id

      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_valid_resource

        patient = resource

        # Check required elements are present
        assert !patient.name.empty?, 'Required element Patient.name is missing'
        assert patient.gender.present?, 'Required element Patient.gender is missing'

        pass 'All required elements are present in resource'

      rescue Inferno::AssertionException => e
        fail e.message
      rescue StandardError => e
        error "Unexpected error checking required elements: #{e.message}"
      end
    end

  end
end