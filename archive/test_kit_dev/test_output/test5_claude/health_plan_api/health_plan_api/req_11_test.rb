module Test5_claude
  class RestfulBehaviorTest < Inferno::TestGroup
    id :restful_behavior
    title 'RESTful Behavior Implementation'
    description %(
      Verify that the Health Plan API implements RESTful behavior according to the FHIR specification.
      
      This includes testing:
      - Proper handling of HTTP verbs (GET, POST, PUT, DELETE)
      - Correct response codes
      - Content negotiation
      - Resource validation
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :read_interaction
      title 'Server supports read interactions'
      description 'Verify that the server properly implements RESTful read operations'
      input :known_patient_id
      
      run do
        fhir_read(:patient, known_patient_id)
        
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource
      end
    end

    test do
      id :search_interaction 
      title 'Server supports search interactions'
      description 'Verify that the server properly implements RESTful search operations'

      run do
        fhir_search(:patient)
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
      end
    end

    test do
      id :create_interaction
      title 'Server supports create interactions' 
      description 'Verify that the server properly implements RESTful create operations'

      run do
        patient = FHIR::Patient.new(
          name: [{ given: ['Test'], family: 'Patient' }]
        )
        
        fhir_create(patient)
        
        assert_response_status(201)
        assert_resource_type(:patient)
        assert_valid_resource
        assert response.headers['Location'].present?, 'Location header missing from create response'
      end
    end

    test do
      id :update_interaction
      title 'Server supports update interactions'
      description 'Verify that the server properly implements RESTful update operations'
      input :known_patient_id
      
      run do
        patient = fhir_read(:patient, known_patient_id).resource
        patient.gender = 'female'
        
        fhir_update(patient, known_patient_id)
        
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource
      end
    end

    test do
      id :delete_interaction
      title 'Server supports delete interactions'
      description 'Verify that the server properly implements RESTful delete operations'
      input :deletable_patient_id
      
      run do
        fhir_delete(:patient, deletable_patient_id)
        assert_response_status(204)
        
        fhir_read(:patient, deletable_patient_id)
        assert_response_status(410)
      end
    end

    test do
      id :content_types
      title 'Server supports proper content negotiation'
      description 'Verify that the server handles content types correctly'
      input :known_patient_id
      
      run do
        headers = { 'Accept' => 'application/fhir+json' }
        fhir_read(:patient, known_patient_id, headers: headers)
        
        assert_response_status(200)
        assert_response_content_type('application/fhir+json')
      end
    end

    def assert_valid_bundle_entries
      assert resource.is_a?(FHIR::Bundle), 'Expected response to be a Bundle'
      assert resource.entry.present?, 'Bundle must contain entries'
      resource.entry.each do |entry|
        assert entry.resource.present?, 'Bundle entry must contain resource'
        assert_valid_resource(resource: entry.resource)
      end
    end

    def assert_response_content_type(expected_type)
      actual_type = response.headers['Content-Type']
      assert actual_type&.start_with?(expected_type), 
        "Expected Content-Type '#{expected_type}' but got '#{actual_type}'"
    end
  end
end