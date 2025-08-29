module Test8_claude
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_processing
    title 'Must Support Elements Processing Tests'
    description %(
      Verify that the Application Actor properly processes Must Support data elements 
      without errors or application failure as required by REQ-07.
    )

    fhir_client do
      url :url
      oauth_credentials :credentials 
    end

    test do
      id :must_support_element_read
      title 'Process resource with Must Support elements'
      description %(
        Verify that the Application Actor can successfully process a resource 
        containing all defined Must Support elements without error.
      )

      input :patient_id,
            title: 'Patient ID',
            description: 'ID of a Patient resource containing Must Support elements'
      
      input :url,
            title: 'FHIR Server URL',
            description: 'Base URL of FHIR server'

      input :credentials,
            title: 'OAuth Credentials',
            type: :oauth_credentials,
            optional: true

      makes_request :must_support_patient

      run do
        fhir_read(:patient, patient_id, name: :must_support_patient)

        assert_response_status(200)
        assert_resource_type(:patient)

        assert resource[:name].present?, 
          'Application failed to process Must Support name element'
        assert resource[:gender].present?,
          'Application failed to process Must Support gender element' 
        assert resource[:birthDate].present?,
          'Application failed to process Must Support birthDate element'

        pass 'Successfully processed resource containing Must Support elements'
      end
    end

    test do
      id :must_support_element_search
      title 'Search using Must Support elements'
      description %(
        Verify that the Application Actor can successfully process search results
        containing Must Support elements without error.
      )

      uses_request :must_support_patient

      run do
        patient = request[:resource]
        
        search_params = {
          name: patient[:name]&.first&.family,
          gender: patient[:gender],
          birthdate: patient[:birthDate]
        }

        fhir_search(:patient, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        assert resource[:entry].present?,
          'No resources returned when searching with Must Support elements'

        pass 'Successfully processed search using Must Support elements'
      end
    end
  end
end