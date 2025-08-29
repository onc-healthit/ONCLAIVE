module Test4_claude
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_population
    title 'Must Support Elements Population'
    description %(
      Verify that the Health Plan API properly populates all Must Support 
      data elements in query results as required by REQ-04.

      The test will:
      * Query for resources that should contain Must Support elements
      * Verify that all Must Support elements are populated with valid values
      * Check both required and optional Must Support elements
    )

    MUST_SUPPORT_ELEMENTS = {
      'Patient' => [
        'name', 'gender', 'birthDate', 'address', 'telecom'
      ],
      'Coverage' => [
        'status', 'beneficiary', 'payor', 'class', 'type'
      ],
      'Organization' => [
        'name', 'address', 'telecom', 'type'
      ]
    }

    test do
      id :must_support_patient_elements
      title 'Patient Must Support Elements Are Populated'
      description 'Verify Must Support elements are populated for Patient resources'
      
      run do
        fhir_search(:patient)
        assert_response_status(200)
        assert_resource_type(:patient)

        resources = resource.entry.map(&:resource)
        assert resources.present?, 'No Patient resources were returned'

        resources.each do |patient|
          MUST_SUPPORT_ELEMENTS['Patient'].each do |element|
            assert patient.send(element).present?, 
              "Must Support element '#{element}' is not populated for Patient/#{patient.id}"
          end
        end
      end
    end

    test do
      id :must_support_coverage_elements  
      title 'Coverage Must Support Elements Are Populated'
      description 'Verify Must Support elements are populated for Coverage resources'

      run do
        fhir_search(:coverage)
        assert_response_status(200)
        assert_resource_type(:coverage)

        resources = resource.entry.map(&:resource)
        assert resources.present?, 'No Coverage resources were returned'

        resources.each do |coverage|
          MUST_SUPPORT_ELEMENTS['Coverage'].each do |element|
            assert coverage.send(element).present?,
              "Must Support element '#{element}' is not populated for Coverage/#{coverage.id}"
          end
        end
      end
    end

    test do
      id :must_support_organization_elements
      title 'Organization Must Support Elements Are Populated'
      description 'Verify Must Support elements are populated for Organization resources'

      run do
        fhir_search(:organization)
        assert_response_status(200)
        assert_resource_type(:organization)

        resources = resource.entry.map(&:resource)
        assert resources.present?, 'No Organization resources were returned'

        resources.each do |org|
          MUST_SUPPORT_ELEMENTS['Organization'].each do |element|
            assert org.send(element).present?,
              "Must Support element '#{element}' is not populated for Organization/#{org.id}"
          end
        end
      end
    end
  end
end