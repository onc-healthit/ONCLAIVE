module Test5_claude
  class RevincludesSupportGroup < Inferno::TestGroup
    id :revincludes_support
    title 'Support for _revincludes Parameter'
    description %(
      Verify that the server supports the _revinclude parameter for resource searches
      as specified in REQ-28: "A Server SHALL be capable of supporting _revincludes"
    )

    test do
      id :patient_revinclude_test
      title 'Server handles _revinclude with Patient resource'
      description %(
        Verify that the server properly processes a Patient search with _revinclude parameter.
        This tests that referenced resources are included in the search results.
      )
      
      input :patient_id
      
      run do
        # Search for patient and include referencing Observations
        search_params = {
          _id: patient_id,
          _revinclude: 'Observation:subject'
        }
        
        fhir_search(:patient, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length > 0, 'No resources returned in Bundle'
        
        # Verify Bundle contains both Patient and referenced Observations
        patient_entries = bundle.entry.select { |e| e.resource.resourceType == 'Patient' }
        observation_entries = bundle.entry.select { |e| e.resource.resourceType == 'Observation' }
        
        assert patient_entries.length > 0, 'No Patient resources found in Bundle'
        assert observation_entries.length > 0, 'No Observation resources found in Bundle'
        
        # Verify Observations reference the Patient
        observation_entries.each do |entry|
          observation = entry.resource
          assert observation.subject&.reference&.include?(patient_id),
                "Observation #{observation.id} does not reference Patient #{patient_id}"
        end
      end
    end

    test do
      id :multiple_revincludes_test  
      title 'Server handles multiple _revinclude parameters'
      description %(
        Verify that the server properly handles multiple _revinclude parameters
        to include multiple types of referencing resources.
      )

      input :patient_id
      
      run do
        search_params = {
          _id: patient_id,
          _revinclude: ['Observation:subject', 'Condition:patient']
        }

        fhir_search(:patient, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource
        
        assert bundle.entry.length > 0, 'No resources returned in Bundle'

        patient_entries = bundle.entry.select { |e| e.resource.resourceType == 'Patient' }
        observation_entries = bundle.entry.select { |e| e.resource.resourceType == 'Observation' }
        condition_entries = bundle.entry.select { |e| e.resource.resourceType == 'Condition' }

        assert patient_entries.length > 0, 'No Patient resources found in Bundle'
        assert observation_entries.length + condition_entries.length > 0,
               'No referencing resources (Observations or Conditions) found in Bundle'

        # Verify references for each resource type
        observation_entries.each do |entry|
          observation = entry.resource
          assert observation.subject&.reference&.include?(patient_id),
                "Observation #{observation.id} does not reference Patient #{patient_id}"
        end

        condition_entries.each do |entry|
          condition = entry.resource
          assert condition.patient&.reference&.include?(patient_id),
                "Condition #{condition.id} does not reference Patient #{patient_id}"
        end
      end
    end

    test do
      id :invalid_revinclude_test
      title 'Server handles invalid _revinclude parameter'
      description %(
        Verify that the server returns an appropriate error for invalid _revinclude parameters.
      )

      input :patient_id
      
      run do
        search_params = {
          _id: patient_id,
          _revinclude: 'InvalidResource:patient'
        }

        fhir_search(:patient, params: search_params) rescue nil

        assert_response_status([400, 404])
        assert_resource_type(:operationoutcome)
      end
    end
  end
end