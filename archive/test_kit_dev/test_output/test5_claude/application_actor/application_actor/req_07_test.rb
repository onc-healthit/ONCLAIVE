module Test5_claude
  class ClientDisplayTest < Inferno::TestGroup
    id :client_display_elements_test
    title 'Client Display of Data Elements'
    description %(
      Validates that Application actors are capable of displaying data elements 
      for human use or storing the information for other purposes.
      
      This test verifies that a client can:
      * Successfully retrieve FHIR resources
      * Process the retrieved data elements
      * Display or store the key elements appropriately
    )

    test do
      id :retrieve_patient_data
      title 'Retrieve patient data elements'
      description 'Verify client can retrieve patient demographic data elements'
      
      input :patient_id
      input :expected_display_elements, 
            title: 'Expected display elements',
            description: 'Comma-separated list of patient elements that should be displayed'
      
      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        patient = resource
        assert_valid_resource(patient)

        required_elements = expected_display_elements.split(',').map(&:strip)
        
        required_elements.each do |element|
          assert !patient.send(element).nil?, 
                "Patient resource is missing required display element: #{element}"
        end

        # Store patient resource for subsequent display verification
        output patient_resource: patient.to_json
      end
    end

    test do
      id :verify_display_capability 
      title 'Verify display capability'
      description 'Verify client can process and prepare data elements for display'
      
      input :display_confirmation,
            title: 'Display confirmation',
            description: 'Confirmation that client successfully displayed all elements (true/false)'
            
      run do
        skip_if display_confirmation.nil?, 
                'No display confirmation provided'

        assert display_confirmation.downcase == 'true',
               'Client failed to display all required data elements'

        pass 'Client successfully demonstrated capability to display data elements'
      end
    end
  end
end