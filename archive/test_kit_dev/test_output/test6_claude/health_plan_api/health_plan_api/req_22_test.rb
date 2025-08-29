module Test6_claude
  class ReverseChainingSupportTest < Inferno::TestGroup
    id :reverse_chaining_support
    title 'REQ-22: Reverse Chaining Support'
    description %(
      This test verifies that the server supports reverse chaining for search parameters 
      that specify the 'chain' property. Reverse chaining allows finding resources based
      on properties of resources that refer to them.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :reverse_chain_patient_observation
      title 'Server supports reverse chaining from Patient to Observation'
      description %(
        Verify that the server properly handles a reverse chain search from Patient 
        to Observation using the subject reference.
      )
      
      input :patient_id
      
      run do
        # Create test observation linked to patient
        observation = FHIR::Observation.new(
          status: 'final',
          subject: { reference: "Patient/#{patient_id}" }
        )
        
        fhir_create(observation)
        assert_response_status(201)
        observation_id = resource.id

        # Test reverse chain search
        search_params = {
          '_has:Observation:subject:code': 'final'
        }
        
        fhir_search(:patient, params: search_params)
        assert_response_status(200)
        assert_resource_type(:patient)
        
        patient_bundle = resource
        assert patient_bundle.entry.length.positive?, 
          'No Patient resources returned from reverse chain search'
          
        matching_patient = patient_bundle.entry.find do |entry|
          entry.resource.id == patient_id
        end
        
        assert !matching_patient.nil?,
          "Patient/#{patient_id} not found in reverse chain search results"

        # Cleanup
        fhir_delete(:observation, observation_id)
      end
    end

    test do
      id :reverse_chain_patient_condition 
      title 'Server supports reverse chaining from Patient to Condition'
      description %(
        Verify that the server properly handles a reverse chain search from Patient
        to Condition using the subject reference.
      )
      
      input :patient_id
      
      run do
        # Create test condition linked to patient
        condition = FHIR::Condition.new(
          clinicalStatus: {
            coding: [{
              system: 'http://terminology.hl7.org/CodeSystem/condition-clinical',
              code: 'active'
            }]
          },
          subject: { reference: "Patient/#{patient_id}" }
        )
        
        fhir_create(condition)
        assert_response_status(201)
        condition_id = resource.id

        # Test reverse chain search
        search_params = {
          '_has:Condition:subject:clinical-status': 'active'
        }
        
        fhir_search(:patient, params: search_params)
        assert_response_status(200)
        assert_resource_type(:patient)
        
        patient_bundle = resource
        assert patient_bundle.entry.length.positive?,
          'No Patient resources returned from reverse chain search'
          
        matching_patient = patient_bundle.entry.find do |entry|
          entry.resource.id == patient_id
        end
        
        assert !matching_patient.nil?,
          "Patient/#{patient_id} not found in reverse chain search results"

        # Cleanup
        fhir_delete(:condition, condition_id)
      end
    end

    test do
      id :reverse_chain_invalid_param
      title 'Server returns error for invalid reverse chain parameter'
      description %(
        Verify that the server returns an appropriate error when an invalid
        reverse chain parameter is specified.
      )
      
      run do
        search_params = {
          '_has:Invalid:subject:code': 'test'
        }
        
        fhir_search(:patient, params: search_params)
        
        assert_response_status([400, 404, 422])
        assert_resource_type(:operationoutcome)
      end
    end
  end
end