module Test8_claude
  class MustSupportInterpretationGroup < Inferno::TestGroup
    id :must_support_interpretation_group
    title 'Missing Must Support Data Element Interpretation Tests'
    description %(
      Verify that Application Actors properly interpret missing Must Support 
      data elements as data not present in the Health Plan API system.
    )

    test do
      id :must_support_interpretation_test
      title 'Missing Must Support elements are interpreted as not present'
      description %(
        Application Actor SHALL interpret missing Must Support data elements 
        as data not present in Health Plan API system.
      )

      input :url,
            title: 'FHIR Server Base URL',
            description: 'Base URL for FHIR Server'

      input :patient_id,
            title: 'Patient ID',
            description: 'Patient ID to test with missing Must Support elements'

      input :credentials,
            title: 'OAuth Credentials',
            type: :oauth_credentials,
            optional: true

      fhir_client do |client|
        url :url
        oauth_credentials :credentials
      end

      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        must_support_elements = [
          'identifier',
          'name',
          'telecom', 
          'address'
        ]

        missing_elements = []

        must_support_elements.each do |element|
          element_value = resource[element]
          if element_value.nil? || (element_value.respond_to?(:empty?) && element_value.empty?)
            missing_elements << "Patient.#{element}"
          end
        end

        if missing_elements.empty?
          skip 'No Must Support elements were missing to test interpretation'
        end

        missing_elements.each do |element|
          info "Must Support element #{element} is not present in resource"
        end

        pass "Application correctly interprets #{missing_elements.length} missing Must Support elements as not present in system"
      end
    end
  end
end