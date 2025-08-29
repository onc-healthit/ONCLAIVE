module Test5_claude
  class UnknownResourceResponseTest < Inferno::TestGroup
    id :unknown_resource_response
    title 'Unknown Resource Response Test'
    description %(
      Verify that the server returns an appropriate 404 status code
      when attempting to access an unknown/non-existent resource.
      
      The server SHALL return a 404 status code when a resource
      does not exist or cannot be found.
    )

    test do
      id :unknown_resource_404_test
      title 'Server returns 404 for unknown resource'
      description %(
        This test verifies that the server returns a 404 Not Found
        status code when attempting to read a non-existent resource.
      )
      
      input :server_url,
            title: 'FHIR Server Base URL',
            description: 'Base URL for the FHIR server'

      run do
        # Generate a random UUID that should not exist
        unknown_id = SecureRandom.uuid

        # Attempt to read a Patient resource with the unknown ID
        fhir_operation do
          fhir_read(:patient, unknown_id)
        end

        assert_response_status(404)
        
        # Validate OperationOutcome if present
        if resource.present? && resource.is_a?(FHIR::OperationOutcome)
          assert resource.issue&.any? { |issue| issue.severity == 'error' },
                 'OperationOutcome should contain an error issue'
        end

      rescue Inferno::AssertionException => e
        fail("Server did not return 404 status: #{e.message}")
      end
    end
  end
end