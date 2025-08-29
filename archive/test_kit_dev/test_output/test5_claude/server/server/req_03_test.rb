module Test5_claude
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_group
    title 'Must Support Data Elements Population'
    description %(
      Verify that the Health Plan API server is capable of populating all Must Support 
      data elements as part of query results.

      The server SHALL be capable of including all Must Support data elements defined
      in applicable profiles when returning resources in response to queries.
    )

    test do
      id :must_support_elements_patient
      title 'Patient Must Support elements are populated'
      description %(
        Verify that all Must Support elements in Patient resources are populated
        in query results when available.
      )
      
      input :patient_id
      
      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        patient = resource
        
        must_support_elements = [
          'identifier',
          'name',
          'gender',
          'birthDate',
          'address',
          'telecom'
        ]

        must_support_elements.each do |element|
          assert patient.send(element).present?, 
            "Must Support element '#{element}' is not populated in Patient resource"
        end

        pass "All required Must Support elements are populated in Patient resource"
      end
    end

    test do 
      id :must_support_elements_coverage
      title 'Coverage Must Support elements are populated'
      description %(
        Verify that all Must Support elements in Coverage resources are populated
        in query results when available.
      )

      input :coverage_id
      
      run do
        fhir_read(:coverage, coverage_id)
        assert_response_status(200)
        assert_resource_type(:coverage)

        coverage = resource

        must_support_elements = [
          'status',
          'beneficiary',
          'payor',
          'class',
          'period'
        ]

        must_support_elements.each do |element|
          assert coverage.send(element).present?,
            "Must Support element '#{element}' is not populated in Coverage resource"
        end

        pass "All required Must Support elements are populated in Coverage resource"
      end
    end

    test do
      id :must_support_elements_search
      title 'Must Support elements are populated in search results'
      description %(
        Verify that Must Support elements are populated when retrieving resources
        via search operations.
      )

      run do
        fhir_search(:patient)
        assert_response_status(200)
        assert_resource_type(:patient)
        
        bundle = resource
        assert bundle.entry.length > 0, 'No Patient resources returned in search'

        must_support_elements = [
          'identifier',
          'name', 
          'gender',
          'birthDate'
        ]

        bundle.entry.each do |entry|
          patient = entry.resource
          must_support_elements.each do |element|
            assert patient.send(element).present?,
              "Must Support element '#{element}' missing in search results"
          end
        end

        pass "Must Support elements are populated in search results"
      end
    end
  end
end