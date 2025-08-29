module Test6_claude
  class CombinationSearchParameterGroup < Inferno::TestGroup
    id :combination_search_parameter_support
    title 'Combination Search Parameter Support'
    description %(
      Verify that the server supports searching with combinations of search parameters
      defined in each profile as required by REQ-20.
    )

    test do
      id :patient_combination_search
      title 'Patient profile supports combination search parameters'
      description %(
        Verify server handles search with multiple parameters for Patient profile.
        Tests combination of name, birthdate, and gender parameters.
      )
      
      input :patient_family_name
      input :patient_birth_date
      input :patient_gender

      run do
        fhir_search(:patient, params: {
          family: patient_family_name,
          birthdate: patient_birth_date,
          gender: patient_gender
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
      end
    end

    test do
      id :coverage_combination_search  
      title 'Coverage profile supports combination search parameters'
      description %(
        Verify server handles search with multiple parameters for Coverage profile.
        Tests combination of beneficiary, payor, and status parameters.
      )

      input :coverage_beneficiary
      input :coverage_payor
      input :coverage_status

      run do
        fhir_search(:coverage, params: {
          beneficiary: coverage_beneficiary,
          payor: coverage_payor,
          status: coverage_status
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
      end
    end

    def assert_valid_bundle_entries
      bundle = resource
      
      assert bundle.entry.present?, 'Bundle must contain entries'
      
      bundle.entry.each do |entry|
        assert entry.resource.present?, 'All bundle entries must contain resources'
        assert_valid_resource(resource: entry.resource)
      end
    end
  end
end