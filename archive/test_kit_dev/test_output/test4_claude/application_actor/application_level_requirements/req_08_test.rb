module Test4_claude
  class MustSupportElementsDisplayGroup < Inferno::TestGroup
    id :must_support_elements_display
    title 'Must Support Elements Display'
    description %(
      Verify that the Application Actor properly handles Must Support data elements
      by displaying them for human use or storing them for other purposes.
      
      This test focuses on REQ-08 which specifies that the Application Actor SHOULD
      display Must Support data elements for human use or store for other purposes.
    )

    test do
      id :must_support_patient_elements
      title 'Must Support elements are properly handled for Patient resources'
      description %(
        Verify that Must Support elements in Patient resources are properly 
        handled by the application.
      )
      
      input :patient_id
      input :server_url
      
      run do
        # Read patient resource
        fhir_client do
          url :server_url
        end
        
        patient_request = fhir_read(:patient, patient_id)
        assert_response_status(200)
        
        patient = patient_request.resource
        assert_resource_type(:patient)
        
        # Check for presence of common Must Support elements
        must_support_elements = [
          patient&.name,
          patient&.gender,
          patient&.birthDate,
          patient&.address
        ]
        
        missing_elements = must_support_elements.select { |elem| elem.nil? }
        
        if missing_elements.empty?
          pass 'All Must Support elements are present in the Patient resource'
        else
          warning %(
            The following Must Support elements were not found:
            #{missing_elements.join(', ')}
            
            While these elements SHOULD be displayed/stored, their absence does not
            constitute a failure as this is a SHOULD requirement.
          )
        end
      end
    end

    test do
      id :must_support_observation_elements  
      title 'Must Support elements are properly handled for Observation resources'
      description %(
        Verify that Must Support elements in Observation resources are properly
        handled by the application.
      )
      
      input :patient_id
      input :server_url
      
      run do
        fhir_client do
          url :server_url
        end
        
        search_params = {
          'patient': patient_id,
          '_count': 1
        }
        
        observation_request = fhir_search(:observation, params: search_params)
        assert_response_status(200)
        
        skip_if observation_request.resource.entry.empty?, 
                'No Observation resources found for testing'
        
        observation = observation_request.resource.entry.first.resource
        assert_resource_type(:observation)
        
        # Check for presence of common Must Support elements
        must_support_elements = [
          observation&.status,
          observation&.code,
          observation&.subject,
          observation&.effectiveDateTime
        ]
        
        missing_elements = must_support_elements.select { |elem| elem.nil? }
        
        if missing_elements.empty?
          pass 'All Must Support elements are present in the Observation resource'
        else
          warning %(
            The following Must Support elements were not found:
            #{missing_elements.join(', ')}
            
            While these elements SHOULD be displayed/stored, their absence does not
            constitute a failure as this is a SHOULD requirement.
          )
        end
      end
    end
  end
end