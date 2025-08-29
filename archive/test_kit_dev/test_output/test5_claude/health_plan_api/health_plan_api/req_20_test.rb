module Test5_claude
  class CombinationSearchGroup < Inferno::TestGroup
    id :combination_search_parameters
    title 'Combination Search Parameter Support'
    description %(
      This test group verifies that the Health Plan API properly supports 
      combination searches using multiple search parameters for each profile.
      
      The server SHALL support searching by combinations of search parameters
      as defined in the profiles.
    )

    test do
      id :patient_combination_search
      title 'Patient combination search parameters'
      description %(
        Verify that Patient resource supports combination searches with
        multiple parameters.
      )
      
      run do
        # Search with name + birthdate combination
        search_params = {
          'name': 'Smith',
          'birthdate': '1970-01-01'
        }
        
        fhir_search(:patient, params: search_params)
        
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_bundle_entries
        
        # Verify search results match both criteria
        bundle = resource
        bundle.entry.each do |entry|
          patient = entry.resource
          assert patient.name.any? { |name| name.text&.include?('Smith') }, 
            "Patient name does not match search criteria"
          assert patient.birthDate.to_s == '1970-01-01',
            "Patient birthdate does not match search criteria"
        end
      end
    end

    test do
      id :coverage_combination_search  
      title 'Coverage combination search parameters'
      description %(
        Verify that Coverage resource supports combination searches with
        multiple parameters.
      )

      run do
        # Search with beneficiary + status combination
        search_params = {
          'beneficiary': 'Patient/123',
          'status': 'active'
        }

        fhir_search(:coverage, params: search_params)

        assert_response_status(200)
        assert_resource_type(:coverage) 
        assert_valid_bundle_entries

        # Verify search results match both criteria
        bundle = resource
        bundle.entry.each do |entry|
          coverage = entry.resource
          assert coverage.beneficiary.reference == 'Patient/123',
            "Coverage beneficiary does not match search criteria"
          assert coverage.status == 'active',
            "Coverage status does not match search criteria"
        end
      end
    end

    test do
      id :organization_combination_search
      title 'Organization combination search parameters' 
      description %(
        Verify that Organization resource supports combination searches with
        multiple parameters.
      )

      run do
        # Search with name + address combination
        search_params = {
          'name': 'Health',
          'address': 'Seattle'
        }

        fhir_search(:organization, params: search_params)

        assert_response_status(200)
        assert_resource_type(:organization)
        assert_valid_bundle_entries

        # Verify search results match both criteria  
        bundle = resource
        bundle.entry.each do |entry|
          org = entry.resource
          assert org.name.include?('Health'),
            "Organization name does not match search criteria"
          assert org.address.any? { |addr| addr.city == 'Seattle' },
            "Organization address does not match search criteria"
        end
      end
    end

    def assert_valid_bundle_entries
      bundle = resource
      assert bundle.is_a?(FHIR::Bundle), 'Expected FHIR Bundle resource'
      assert !bundle.entry.empty?, 'Bundle contains no entries'
      bundle.entry.each do |entry|
        assert entry.resource.present?, 'Bundle entry has no resource'
        assert_valid_resource(resource: entry.resource)
      end
    end

  end
end