module Test5_claude
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_group
    title 'Must Support Data Elements Population'
    description %(
      Verify that Health Plan API actors are capable of populating all Must Support 
      data elements as part of query results.
      
      This test validates that responses include all required Must Support elements
      defined in the applicable FHIR profiles.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :must_support_patient_elements
      title 'Patient Must Support Elements Present'
      description %(
        Verify that all Must Support elements are populated in Patient resources
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
            "Must Support element '#{element}' is missing from Patient resource"
        end
      end
    end

    test do
      id :must_support_coverage_elements  
      title 'Coverage Must Support Elements Present'
      description %(
        Verify that all Must Support elements are populated in Coverage resources
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
            "Must Support element '#{element}' is missing from Coverage resource"
        end
      end
    end

    test do
      id :must_support_explanation_of_benefit_elements
      title 'ExplanationOfBenefit Must Support Elements Present' 
      description %(
        Verify that all Must Support elements are populated in ExplanationOfBenefit resources
      )

      input :explanation_of_benefit_id

      run do
        fhir_read(:explanation_of_benefit, explanation_of_benefit_id)
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
            "Must Support element '#{element}' is missing from ExplanationOfBenefit resource"
        end
      end
    end
  end
end