module Test5_claude
  class ClientDataDisplayGroup < Inferno::TestGroup
    id :client_data_display
    title 'Client Display of Data Elements'
    description %(
      Validates that the client application is capable of displaying FHIR data 
      elements for human use or storing the information for other purposes.
      
      This test group verifies REQ-07 which specifies that application actors 
      SHOULD be capable of displaying or storing FHIR data elements.
    )

    test do
      id :verify_patient_display
      title 'Client can display Patient resource data elements'
      description %(
        Verify that the client can properly display key data elements from a 
        Patient resource for human viewing.
      )
      
      input :patient_id
      input :displayed_fields, 
            title: 'Displayed Patient Fields',
            description: 'Comma-separated list of Patient fields displayed to user'
      
      run do
        skip_if patient_id.blank?, 'No patient ID provided'
        skip_if displayed_fields.blank?, 'No display fields specified'

        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        patient = resource
        displayed_field_list = displayed_fields.split(',').map(&:strip)

        displayed_field_list.each do |field|
          assert patient.respond_to?(field.to_sym), 
                 "Patient resource does not contain field: #{field}"
          
          field_value = patient.send(field.to_sym)
          assert !field_value.nil?, 
                 "Required display field #{field} has no value"
        end

        pass "Successfully verified display of Patient fields: #{displayed_fields}"
      end
    end

    test do
      id :verify_observation_display
      title 'Client can display Observation resource data elements' 
      description %(
        Verify that the client can properly display key data elements from an
        Observation resource for human viewing.
      )

      input :patient_id
      input :displayed_fields,
            title: 'Displayed Observation Fields',
            description: 'Comma-separated list of Observation fields displayed to user'

      run do
        skip_if patient_id.blank?, 'No patient ID provided'
        skip_if displayed_fields.blank?, 'No display fields specified'

        search_params = {patient: patient_id}
        fhir_search(:observation, params: search_params)
        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource
        assert !bundle.entry.empty?, 'No Observations found for patient'

        observation = bundle.entry.first.resource
        displayed_field_list = displayed_fields.split(',').map(&:strip)

        displayed_field_list.each do |field|
          assert observation.respond_to?(field.to_sym),
                 "Observation resource does not contain field: #{field}"
          
          field_value = observation.send(field.to_sym)
          assert !field_value.nil?,
                 "Required display field #{field} has no value"
        end

        pass "Successfully verified display of Observation fields: #{displayed_fields}"
      end
    end
  end
end