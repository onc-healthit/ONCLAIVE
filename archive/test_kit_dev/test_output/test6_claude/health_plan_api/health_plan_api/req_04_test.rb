module Test6_claude
  class AbsentDataElementsTestGroup < Inferno::TestGroup
    id :absent_data_elements
    title 'Not Including Absent Data Elements'
    description %(
      Verifies that health plan API actors do not include Must Support data elements 
      in resource instances when the information is not present and minimum cardinality is 0.
    )

    test do
      id :verify_absent_data_omission
      title 'Verify absent optional data elements are not included'
      description %(
        This test verifies that Must Support data elements with minimum cardinality of 0
        are not included in resources when the data is not present.
      )

      # Input parameters
      input :patient_id
      
      run do
        # Get patient resource
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_valid_resource
        
        patient = resource

        # Check commonly optional Must Support elements
        optional_elements = [
          'birthDate',
          'gender', 
          'address',
          'telecom'
        ]

        optional_elements.each do |element|
          # Only validate if element is not present
          next unless patient.send(element).nil?

          # Verify element is actually not included in raw response
          raw_response = request.response_body
          assert !raw_response.include?(element), 
                "#{element} was included in response despite being absent"
        end

        pass "Successfully verified absent optional elements are not included in response"

      rescue Inferno::AssertionException => e
        fail e.message
      end
    end

    test do
      id :verify_required_elements_present
      title 'Verify required elements are still included'
      description %(
        This test verifies that required elements (min cardinality > 0) 
        are still included in the resource.
      )

      input :patient_id

      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_valid_resource

        patient = resource

        # Check required elements are present
        required_elements = ['id', 'resourceType']

        required_elements.each do |element|
          assert !patient.send(element).nil?,
                "Required element #{element} was not included in response"
        end

        pass "Successfully verified required elements are included in response"
      end
    end

  end
end