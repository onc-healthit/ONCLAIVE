module Test5_claude
  class UnauthorizedRequestsTest < Inferno::TestGroup
    id :unauthorized_requests_rejection
    title 'Rejection of Unauthorized Requests'
    description %(
      This test verifies that the server properly rejects unauthorized requests
      by returning an HTTP 401 unauthorized response code as required.
      
      Servers SHALL reject any unauthorized requests with a 401 response.
    )

    fhir_client do
      url :url
    end

    test do
      id :unauthorized_patient_read
      title 'Server rejects unauthorized Patient read request'
      description %(
        This test attempts to read a Patient resource without authorization
        and verifies that the server returns HTTP 401.
      )
      
      input :known_patient_id
      
      run do
        # Clear any existing authorization
        fhir_client.set_bearer_token(nil)
        
        # Attempt unauthorized read
        fhir_read(:patient, known_patient_id)
        
        assert_response_status(401)
        assert_response_header('WWW-Authenticate')
      end
    end

    test do
      id :unauthorized_patient_search 
      title 'Server rejects unauthorized Patient search request'
      description %(
        This test attempts to search for Patient resources without authorization
        and verifies that the server returns HTTP 401.
      )
      
      run do
        fhir_client.set_bearer_token(nil)
        
        get '/Patient'
        
        assert_response_status(401)
        assert_response_header('WWW-Authenticate')
      end
    end

    test do
      id :unauthorized_patient_create
      title 'Server rejects unauthorized Patient create request'
      description %(
        This test attempts to create a Patient resource without authorization
        and verifies that the server returns HTTP 401.
      )
      
      run do
        fhir_client.set_bearer_token(nil)
        
        patient = FHIR::Patient.new(
          name: [{ given: ['Test'], family: 'Patient' }]
        )
        
        fhir_create(patient)
        
        assert_response_status(401)
        assert_response_header('WWW-Authenticate')
      end
    end
  end
end