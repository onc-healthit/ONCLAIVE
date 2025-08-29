module Test5_claude
  class IncludesTestGroup < Inferno::TestGroup
    id :includes_support_test_group
    title 'Support for _includes'
    description %(
      This test group validates that the server properly supports the _includes parameter
      as required by REQ-27: "For each resource] A Server SHALL be capable of supporting
      the following _includes [list]."
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :patient_includes_test
      title 'Server supports _include for Patient resources'
      description %(
        Verify that the server properly handles _include parameters when 
        searching Patient resources.
      )
      
      input :patient_id
      
      run do
        # Test include of Patient.organization
        search_params = {
          _id: patient_id,
          _include: 'Patient:organization'
        }
        
        fhir_search(:patient, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length > 1, 
          'Bundle should contain both Patient and included Organization resources'
          
        patient = bundle.entry.find { |e| e.resource.resourceType == 'Patient' }
        org = bundle.entry.find { |e| e.resource.resourceType == 'Organization' }
        
        assert !patient.nil?, 'Bundle should contain Patient resource'
        assert !org.nil?, 'Bundle should contain included Organization resource'
        
        # Verify proper linking between resources
        assert patient.resource.organization&.reference&.include?(org.resource.id),
          'Patient organization reference should match included Organization'
      end
    end

    test do
      id :encounter_includes_test 
      title 'Server supports _include for Encounter resources'
      description %(
        Verify that the server properly handles _include parameters when
        searching Encounter resources.
      )

      input :encounter_id
      
      run do
        search_params = {
          _id: encounter_id,
          _include: ['Encounter:patient', 'Encounter:practitioner']
        }
        
        fhir_search(:encounter, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource
        
        assert bundle.entry.length > 2,
          'Bundle should contain Encounter and included resources'
          
        encounter = bundle.entry.find { |e| e.resource.resourceType == 'Encounter' }
        patient = bundle.entry.find { |e| e.resource.resourceType == 'Patient' }
        practitioner = bundle.entry.find { |e| e.resource.resourceType == 'Practitioner' }
        
        assert !encounter.nil?, 'Bundle should contain Encounter resource'
        assert !patient.nil?, 'Bundle should contain included Patient resource'
        assert !practitioner.nil?, 'Bundle should contain included Practitioner resource'
        
        # Verify proper linking
        assert encounter.resource.subject&.reference&.include?(patient.resource.id),
          'Encounter patient reference should match included Patient'
          
        assert encounter.resource.participant&.any? { |p| 
          p.individual&.reference&.include?(practitioner.resource.id)
        }, 'Encounter practitioner reference should match included Practitioner'
      end
    end

  end
end