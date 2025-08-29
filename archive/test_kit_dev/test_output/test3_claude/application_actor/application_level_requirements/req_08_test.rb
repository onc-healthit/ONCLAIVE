module Test3_claude
  class MustSupportDisplayGroup < Inferno::TestGroup
    id :must_support_display_test
    title 'Must Support Elements Display'
    description %(
      Validates that the Application Actor can properly display or store Must Support 
      data elements as specified in REQ-08.
      
      The test verifies that Must Support elements are:
      * Retrieved from test resources
      * Made available for display or storage
      * Handled appropriately by the application
    )

    test do
      id :must_support_patient_elements
      title 'Must Support elements in Patient resource can be displayed'
      description %(
        Verify that Must Support elements from a Patient resource are available
        for display or other processing by the application.
      )
      
      input :patient_id
      input :supported_elements, 
            title: 'Must Support Elements',
            description: 'Comma-separated list of must support elements that were displayed'

      run do
        skip_if patient_id.blank?, 'No patient ID provided'
        skip_if supported_elements.blank?, 'No must support elements provided'

        # Get patient resource
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        
        patient = resource
        must_support_elements = supported_elements.split(',').map(&:strip)

        # Verify each must support element is present
        must_support_elements.each do |element|
          assert patient.respond_to?(element), 
                 "Patient resource does not contain must support element: #{element}"
          
          element_value = patient.send(element)
          assert !element_value.nil? && element_value != '',
                 "Must support element #{element} has no value"
        end

        pass "Successfully verified #{must_support_elements.length} must support elements: #{must_support_elements.join(', ')}"
      end
    end

    test do
      id :must_support_observation_elements  
      title 'Must Support elements in Observation resource can be displayed'
      description %(
        Verify that Must Support elements from an Observation resource are available
        for display or other processing by the application.
      )

      input :observation_id
      input :supported_elements,
            title: 'Must Support Elements',
            description: 'Comma-separated list of must support elements that were displayed'

      run do
        skip_if observation_id.blank?, 'No observation ID provided'
        skip_if supported_elements.blank?, 'No must support elements provided'

        # Get observation resource
        fhir_read(:observation, observation_id)
        assert_response_status(200)
        assert_resource_type(:observation)

        observation = resource
        must_support_elements = supported_elements.split(',').map(&:strip)

        # Verify each must support element is present
        must_support_elements.each do |element|
          assert observation.respond_to?(element),
                 "Observation resource does not contain must support element: #{element}"
          
          element_value = observation.send(element)
          assert !element_value.nil? && element_value != '',
                 "Must support element #{element} has no value"
        end

        pass "Successfully verified #{must_support_elements.length} must support elements: #{must_support_elements.join(', ')}"
      end
    end
  end
end