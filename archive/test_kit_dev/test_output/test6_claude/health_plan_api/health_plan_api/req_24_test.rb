module Test6_claude
  class UnauthorizedRequestsTest < Inferno::TestGroup
    id :unauthorized_requests_rejection
    title 'Rejection of Unauthorized Requests'
    description %(
      This test verifies that the server properly rejects unauthorized requests
      by returning an HTTP 401 unauthorized response code as required.
      
      Requirement: A server SHALL reject any unauthorized requests by returning
      an HTTP 401 unauthorized response code.
    )

    test do
      id :unauthorized_patient_read
      title 'Server rejects unauthorized Patient read request'
      description %(
        This test attempts to read a Patient resource without authorization
        and verifies that a 401 response is returned.
      )
      
      input :server_url

      run do
        # Create client without auth token
        client = FHIR::Client.new("#{server_url}")
        client.use_r4
        
        # Attempt unauthorized read of Patient resource
        response = client.read(FHIR::Patient, 'example')
        
        assert_response_status(401)
        
        assert_equal 'application/fhir+json', response.response[:headers]['content-type']
        
        error = FHIR.from_contents(response.body)
        assert error.is_a?(FHIR::OperationOutcome), 
          'Server response should include an OperationOutcome'
      end
    end

    test do
      id :unauthorized_search
      title 'Server rejects unauthorized search request' 
      description %(
        This test attempts to perform a search without authorization
        and verifies that a 401 response is returned.
      )

      input :server_url
      
      run do
        # Create client without auth token
        client = FHIR::Client.new("#{server_url}")
        client.use_r4
        
        # Attempt unauthorized search
        response = client.search(FHIR::Patient)
        
        assert_response_status(401)
        
        assert_equal 'application/fhir+json', response.response[:headers]['content-type']
        
        error = FHIR.from_contents(response.body)
        assert error.is_a?(FHIR::OperationOutcome),
          'Server response should include an OperationOutcome'
      end
    end

    test do
      id :unauthorized_create
      title 'Server rejects unauthorized create request'
      description %(
        This test attempts to create a resource without authorization 
        and verifies that a 401 response is returned.
      )

      input :server_url
      
      run do
        # Create client without auth token
        client = FHIR::Client.new("#{server_url}")
        client.use_r4
        
        # Create a test Patient resource
        patient = FHIR::Patient.new(
          name: [{ given: ['Test'], family: 'Patient' }]
        )
        
        # Attempt unauthorized create
        response = client.create(patient)
        
        assert_response_status(401)
        
        assert_equal 'application/fhir+json', response.response[:headers]['content-type']
        
        error = FHIR.from_contents(response.body)
        assert error.is_a?(FHIR::OperationOutcome),
          'Server response should include an OperationOutcome'
      end
    end
  end
end