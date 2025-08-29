module Test5_claude
  class CombinationSearchParameterGroup < Inferno::TestGroup
    id :combination_search_parameter_support
    title 'Combination Search Parameter Support'
    description %(
      Verify that the server supports combination searches using multiple search parameters
      on each profile as required by REQ-20.
      
      The server SHALL support using multiple search parameters in combination when searching
      resources of each profile type.
    )

    test do
      id :patient_combination_search
      title 'Server supports combination search parameters for Patient'
      description %(
        Verify that the server properly handles a search with multiple parameters
        for Patient resources.
      )
      
      input :patient_family_name
      input :patient_given_name
      
      run do
        search_params = {
          family: patient_family_name,
          given: patient_given_name
        }
        
        fhir_search(:patient, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
        
        bundle = resource

        assert bundle.entry.present?, 'No Patient resources were returned'
        
        bundle.entry.each do |entry|
          patient = entry.resource
          assert_resource_type(patient, 'Patient')
          assert patient.name.any? { |name| name.family == patient_family_name }, 
                 "Patient family name #{patient.name&.first&.family} does not match search parameter #{patient_family_name}"
          assert patient.name.any? { |name| name.given.include?(patient_given_name) },
                 "Patient given name #{patient.name&.first&.given&.first} does not match search parameter #{patient_given_name}"
        end
      end
    end

    test do
      id :observation_combination_search  
      title 'Server supports combination search parameters for Observation'
      description %(
        Verify that the server properly handles a search with multiple parameters
        for Observation resources.
      )

      input :patient_id
      input :observation_code
      
      run do
        search_params = {
          patient: patient_id,
          code: observation_code,
          _sort: '-date'
        }

        fhir_search(:observation, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
        
        bundle = resource

        assert bundle.entry.present?, 'No Observation resources were returned'
        
        bundle.entry.each do |entry|
          obs = entry.resource
          assert_resource_type(obs, 'Observation')
          assert obs.subject&.reference&.include?(patient_id),
                 "Observation subject #{obs.subject&.reference} does not reference patient #{patient_id}"
          assert obs.code.coding.any? { |coding| coding.code == observation_code },
                 "Observation code #{obs.code&.coding&.first&.code} does not match search parameter #{observation_code}"
        end
      end
    end

    test do
      id :condition_combination_search
      title 'Server supports combination search parameters for Condition'
      description %(
        Verify that the server properly handles a search with multiple parameters
        for Condition resources.
      )

      input :patient_id
      input :condition_code
      input :clinical_status
      
      run do
        search_params = {
          patient: patient_id,
          code: condition_code,
          clinical_status: clinical_status
        }

        fhir_search(:condition, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
        
        bundle = resource
        
        assert bundle.entry.present?, 'No Condition resources were returned'
        
        bundle.entry.each do |entry|
          condition = entry.resource
          assert_resource_type(condition, 'Condition')
          assert condition.subject&.reference&.include?(patient_id),
                 "Condition subject #{condition.subject&.reference} does not reference patient #{patient_id}"
          assert condition.code.coding.any? { |coding| coding.code == condition_code },
                 "Condition code #{condition.code&.coding&.first&.code} does not match search parameter #{condition_code}"
          assert condition.clinicalStatus.coding.any? { |coding| coding.code == clinical_status },
                 "Condition clinical status #{condition.clinicalStatus&.coding&.first&.code} does not match search parameter #{clinical_status}"
        end
      end
    end
  end
end