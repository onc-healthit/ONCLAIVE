module Test5_claude
  class AbsentDataElementsGroup < Inferno::TestGroup
    id :absent_data_elements
    title 'Absent Data Elements Not Included'
    description %(
      Validates that when information for a Must Support data element is not present
      and has minimum cardinality of 0, the server does not include the data element
      in the resource instance returned.
    )
    
    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :absent_element_not_included
      title 'Must Support elements with cardinality 0 are not included when absent'
      description %(
        This test verifies that Must Support elements with minimum cardinality of 0
        are not included in the resource when the data is not present.
      )
      
      input :patient_id
      
      run do
        # Get base Patient resource
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        patient = resource

        # Check common Must Support elements with min 0 cardinality
        optional_elements = [
          'Patient.birthDate',
          'Patient.telecom',
          'Patient.address',
          'Patient.communication'
        ]

        optional_elements.each do |element_path|
          element = patient.send(element_path.split('.').last)
          if element.nil? || (element.respond_to?(:empty?) && element.empty?)
            assert !resource.to_hash.key?(element_path.split('.').last), 
              "#{element_path} should not be included in resource when data is absent"
          end
        end

        pass "Optional Must Support elements are correctly omitted when absent"
      end
    end

    test do
      id :required_elements_present
      title 'Required elements are always included'
      description %(
        This test verifies that elements with minimum cardinality > 0 
        are always included, even when empty.
      )
      
      input :patient_id
      
      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        patient = resource

        # Check required elements
        required_elements = [
          'Patient.name',
          'Patient.gender'
        ]

        required_elements.each do |element_path|
          element_name = element_path.split('.').last
          assert resource.to_hash.key?(element_name),
            "Required element #{element_path} must always be included"
        end

        pass "Required elements are properly included"
      end
    end

  end
end