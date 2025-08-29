module Test
  class MissingMustSupportInterpretationGroup < Inferno::TestGroup
    id :missing_must_support_interpretation
    title 'Missing Must Support Data Element Interpretation'
    description %(
      Verify that Application Actors properly interpret missing Must Support 
      data elements as data not present in the Health Plan API system.
    )

    test do
      id :missing_must_support_elements_test 
      title 'Application handles missing Must Support elements correctly'
      description %(
        This test verifies that the Application Actor interprets missing Must Support 
        data elements as data that is not present in the Health Plan API system,
        rather than errors or unknown values.
      )

      input :url,
            title: 'FHIR Server URL',
            description: 'Base URL for FHIR Server'

      input :patient_id,
            title: 'Patient ID',
            description: 'ID of patient resource with known missing Must Support elements'

      fhir_client do
        url :url
      end

      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        must_support_elements = resource.class::METADATA.select do |element|
          element.must_support? && !resource[element.local_name].present?
        end

        assert must_support_elements.present?,
               'No missing Must Support elements found to test interpretation'

        must_support_elements.each do |element|
          element_name = element.local_name
          assert !resource[element_name].present?,
                 "Expected Must Support element #{element_name} to be missing"

          assert resource["#{element_name}_element"]&.nil?,
                 "Must Support element #{element_name} should be interpreted as not present"
        end

        pass "Application correctly interprets #{must_support_elements.size} missing Must Support elements as not present"
      end
    end
  end
end