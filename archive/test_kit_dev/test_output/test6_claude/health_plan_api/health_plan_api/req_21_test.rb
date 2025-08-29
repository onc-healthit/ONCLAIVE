module Test6_claude
  class ForwardChainingTestGroup < Inferno::TestGroup
    id :forward_chaining_support
    title 'Forward Chaining Support Tests'
    description %(
      Verify that the server supports forward chaining on all search parameters 
      that specify the 'chain' property, as required by REQ-21.
      
      The server SHALL support forward chaining to allow traversing relationships
      between resources using dot notation in search parameters.
    )

    test do
      id :patient_organization_chain
      title 'Support chaining from Patient to Organization'
      description %(
        Verify that the server supports forward chaining from Patient to Organization
        using the organization search parameter.
      )
      
      input :patient_id
      
      run do
        # Search for patients linking to their managing organization
        search_params = {
          'organization.name': 'Hospital'
        }
        
        fhir_search(:patient, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_bundle_response
        
        skip_if search_results.empty?, 'No Patient resources found with organization chain'
        
        search_results.each do |patient|
          assert patient&.managingOrganization&.reference.present?, 
            'Patient resource missing required organization reference for chaining'
        end
      end
    end

    test do
      id :condition_patient_chain
      title 'Support chaining from Condition to Patient' 
      description %(
        Verify that the server supports forward chaining from Condition to Patient
        using the patient search parameter.
      )

      run do
        search_params = {
          'patient.gender': 'female'
        }
        
        fhir_search(:condition, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:condition) 
        assert_valid_bundle_response
        
        skip_if search_results.empty?, 'No Condition resources found with patient chain'
        
        search_results.each do |condition|
          assert condition&.subject&.reference.present?,
            'Condition resource missing required patient reference for chaining'
        end
      end
    end

    test do
      id :observation_patient_chain
      title 'Support chaining from Observation to Patient'
      description %(
        Verify that the server supports forward chaining from Observation to Patient
        using the patient search parameter.
      )

      run do
        search_params = {
          'patient.birthdate': 'gt2000-01-01'
        }
        
        fhir_search(:observation, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:observation)
        assert_valid_bundle_response
        
        skip_if search_results.empty?, 'No Observation resources found with patient chain'
        
        search_results.each do |observation|
          assert observation&.subject&.reference.present?,
            'Observation resource missing required patient reference for chaining'
        end
      end
    end
  end
end