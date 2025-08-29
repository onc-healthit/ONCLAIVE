module Test6_claude
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_group
    title 'Population of Must Support Data Elements'
    description %(
      This test group verifies that the Health Plan API actor is capable of 
      populating all Must Support data elements as part of query results.
      
      Requirement: Health Plan API actors SHALL be capable of populating all 
      Must Support data elements as part of the query results.
    )

    test do
      id :must_support_patient_elements
      title 'Patient Must Support Elements Population Test'
      description %(
        Verify that all Must Support elements are populated in Patient resources
        returned by the server.
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
          'telecom',
          'gender',
          'birthDate',
          'address'
        ]

        must_support_elements.each do |element|
          assert patient.send(element).present?, 
            "Must Support element '#{element}' is not populated"
        end
      end
    end

    test do
      id :must_support_coverage_elements  
      title 'Coverage Must Support Elements Population Test'
      description %(
        Verify that all Must Support elements are populated in Coverage resources
        returned by the server.
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
            "Must Support element '#{element}' is not populated"
        end
      end
    end

    test do
      id :must_support_explanation_of_benefit_elements
      title 'ExplanationOfBenefit Must Support Elements Population Test' 
      description %(
        Verify that all Must Support elements are populated in ExplanationOfBenefit
        resources returned by the server.
      )

      input :eob_id
      
      run do
        fhir_read(:explanation_of_benefit, eob_id)
        assert_response_status(200)
        assert_resource_type(:explanation_of_benefit)

        eob = resource

        must_support_elements = [
          'status',
          'type',
          'patient',
          'created',
          'insurer',
          'provider',
          'payee',
          'outcome',
          'insurance',
          'item'
        ]

        must_support_elements.each do |element|
          assert eob.send(element).present?,
            "Must Support element '#{element}' is not populated"
        end
      end
    end
  end
end