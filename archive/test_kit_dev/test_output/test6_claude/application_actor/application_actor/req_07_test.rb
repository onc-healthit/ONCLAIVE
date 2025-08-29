module Test6_claude
  class DataElementDisplayTest < Inferno::TestGroup
    id :data_element_display_test
    title 'Client Display of Data Elements'
    description %(
      Tests that an Application Actor is capable of displaying or storing FHIR data elements.
      
      Requirement REQ-07: Application actors SHOULD be capable of displaying the data elements 
      for human use or storing the information for other purposes.
    )

    test do
      id :data_element_display_capability
      title 'Verify data element display/storage capability'
      description %(
        This test verifies that the application can retrieve and process 
        FHIR resources for display or storage purposes.
      )
      
      input :patient_id
      input :server_url
      
      run do
        # Setup FHIR client
        fhir_client do
          url :server_url
        end

        # Retrieve a Patient resource
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        
        patient = resource
        
        # Check key data elements are present and accessible
        assert !patient.name.empty?, 'Patient name element must be present'
        assert !patient.birthDate.nil?, 'Patient birthDate element must be present'
        
        # Verify resource can be serialized for storage
        begin
          stored_json = patient.to_json
          parsed_json = JSON.parse(stored_json)
          assert !parsed_json.empty?, 'Resource must be serializable for storage'
        rescue => e
          fail "Resource cannot be properly serialized: #{e.message}"
        end

        # Optional: Additional resource types could be tested here
        fhir_search(:observation, params: {patient: patient_id})
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        observations = resource.entry&.map(&:resource)
        assert !observations.nil? && !observations.empty?,
               'Must support retrieval of related Observations'
               
        observations.each do |obs|
          assert obs.status.present?, 'Observation status must be accessible'
          assert obs.code.present?, 'Observation code must be accessible'
          assert obs.value&.present?, 'Observation value should be accessible'
        end

        pass 'Application successfully demonstrated capability to access and process data elements'
      end
    end
  end
end