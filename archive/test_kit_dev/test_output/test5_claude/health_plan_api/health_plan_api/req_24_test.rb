module Test5_claude
  class UnauthorizedRequestTest < Inferno::TestGroup
    id :unauthorized_request_rejection
    title 'Rejection of Unauthorized Requests'
    description %(
      Verify that the server rejects unauthorized requests by returning an HTTP 401
      unauthorized response code per REQ-24.

      The server SHALL reject any unauthorized requests by returning an HTTP 401
      unauthorized response code.
    )

    test do
      id :unauthorized_patient_read
      title 'Server rejects unauthorized Patient read request'
      description %(
        This test verifies that the server properly rejects an unauthorized
        request to read a Patient resource by returning a 401 response.
      )
      
      input :patient_id
      
      run do
        # Create FHIR client without authorization
        client = FHIR::Client.new(url)
        client.set_no_auth

        # Attempt unauthorized read of Patient
        response = client.read(FHIR::Patient, patient_id)
        
        assert_response_status(401)
        
        begin  
          assert response.response[:headers]['www-authenticate'].present?,
                 'Response should include WWW-Authenticate header'
        rescue NoMethodError
          assert false, 'Response headers should include WWW-Authenticate challenge'
        end
      end
    end

    test do
      id :unauthorized_search
      title 'Server rejects unauthorized search request' 
      description %(
        This test verifies that the server properly rejects an unauthorized
        search request by returning a 401 response.
      )

      run do
        # Create FHIR client without authorization
        client = FHIR::Client.new(url)
        client.set_no_auth

        # Attempt unauthorized search
        response = client.search(FHIR::Patient)
        
        assert_response_status(401)

        begin
          assert response.response[:headers]['www-authenticate'].present?,
                 'Response should include WWW-Authenticate header'
        rescue NoMethodError
          assert false, 'Response headers should include WWW-Authenticate challenge'
        end
      end
    end

    test do
      id :unauthorized_create
      title 'Server rejects unauthorized create request'
      description %(
        This test verifies that the server properly rejects an unauthorized
        attempt to create a resource by returning a 401 response.
      )

      run do
        # Create FHIR client without authorization
        client = FHIR::Client.new(url)
        client.set_no_auth

        # Create test patient resource
        patient = FHIR::Patient.new(
          name: [{ given: ['Test'], family: 'Patient' }]
        )

        # Attempt unauthorized create
        response = client.create(patient)
        
        assert_response_status(401)

        begin
          assert response.response[:headers]['www-authenticate'].present?,
                 'Response should include WWW-Authenticate header'
        rescue NoMethodError
          assert false, 'Response headers should include WWW-Authenticate challenge'
        end
      end
    end
  end
end