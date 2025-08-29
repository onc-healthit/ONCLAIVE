module Test6_claude
  class RevIncludesSupportTest < Inferno::TestGroup
    id :rev_includes_support_test
    title 'Support for _revincludes Parameters'
    description %(
      This test verifies that the server supports the _revinclude parameter
      for supported resource types as required by REQ-28.
      
      The server SHALL be capable of supporting _revinclude parameters to include
      resources that reference the returned resources.
    )

    test do
      id :patient_revinclude_test
      title 'Server handles Patient _revinclude parameter'
      description %(
        Verify that the server properly processes a Patient search with _revinclude
        parameter and returns the referenced resources.
      )
      
      input :patient_id

      run do
        # Search for patient with _revinclude for Condition resources
        search_params = {
          _id: patient_id,
          _revinclude: 'Condition:subject'
        }

        fhir_search(:patient, params: search_params)

        assert_response_status(200)
        assert_resource_type(:searchset)

        bundle = resource

        # Verify bundle contains both Patient and referenced Conditions
        assert bundle.entry.length > 0, 'No resources returned in searchset'
        
        patient_entries = bundle.entry.select { |e| e.resource.resourceType == 'Patient' }
        condition_entries = bundle.entry.select { |e| e.resource.resourceType == 'Condition' }

        assert patient_entries.length > 0, 'No Patient resources found in response'
        assert condition_entries.length > 0, 'No referenced Condition resources included in response'

        # Verify Conditions reference the Patient
        condition_entries.each do |entry|
          condition = entry.resource
          assert condition.subject&.reference&.include?(patient_id),
                 "Condition #{condition.id} does not reference patient #{patient_id}"
        end
      end
    end

    test do
      id :encounter_revinclude_test 
      title 'Server handles Encounter _revinclude parameter'
      description %(
        Verify that the server properly processes an Encounter search with _revinclude
        parameter and returns the referenced resources.
      )

      input :encounter_id

      run do
        search_params = {
          _id: encounter_id,
          _revinclude: 'Observation:encounter'
        }

        fhir_search(:encounter, params: search_params)

        assert_response_status(200)
        assert_resource_type(:searchset)

        bundle = resource

        assert bundle.entry.length > 0, 'No resources returned in searchset'

        encounter_entries = bundle.entry.select { |e| e.resource.resourceType == 'Encounter' }
        observation_entries = bundle.entry.select { |e| e.resource.resourceType == 'Observation' }

        assert encounter_entries.length > 0, 'No Encounter resources found in response'
        assert observation_entries.length > 0, 'No referenced Observation resources included in response'

        observation_entries.each do |entry|
          observation = entry.resource
          assert observation.encounter&.reference&.include?(encounter_id),
                 "Observation #{observation.id} does not reference encounter #{encounter_id}"
        end
      end
    end
  end
end