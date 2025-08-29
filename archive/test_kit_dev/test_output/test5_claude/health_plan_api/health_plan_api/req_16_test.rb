module Test5_claude
  class UnknownResourceResponseGroup < Inferno::TestGroup
    id :unknown_resource_response
    title 'Unknown Resource Response Test'
    description %(
      Verify that the server returns appropriate 404 status code when 
      requesting an unknown/non-existent resource.

      Requirement: Return the following response classes: (Status 404): unknown resource.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :test_unknown_resource_response
      title 'Server returns 404 for unknown resource'
      description %(
        This test verifies that the server returns a 404 Not Found status
        when attempting to read a resource that does not exist.
      )

      input :url,
            title: 'FHIR Server URL',
            description: 'URL of the FHIR server'
            
      input :bearer_token,
            title: 'Bearer Token',
            description: 'Bearer token for server authentication'

      run do
        # Attempt to read non-existent resource
        fhir_operation do
          options(
            resource: :patient,
            operation: :read,
            id: 'non-existent-id-123456789'
          )
        end

        assert_response_status(404)
        
        assert_resource_type('OperationOutcome')
        
        outcome = resource

        assert outcome.issue&.any? { |issue| issue.severity == 'error' },
               'Expected OperationOutcome to contain error severity issue'

        assert outcome.issue&.any? { |issue| issue.code == 'not-found' },
               'Expected OperationOutcome to contain not-found issue code'
      end
    end
  end
end