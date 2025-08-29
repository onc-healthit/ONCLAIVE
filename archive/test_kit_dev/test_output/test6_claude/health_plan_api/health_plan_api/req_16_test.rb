module Test6_claude
  class UnknownResourceResponseGroup < Inferno::TestGroup
    id :unknown_resource_response
    title 'Unknown Resource Response Test'
    description %(
      This test verifies that the Health Plan API returns a 404 status code
      when attempting to access an unknown/non-existent resource.
      
      Requirement: Return the following response classes: (Status 404): unknown resource.
    )

    test do
      id :unknown_resource_404_test
      title 'Server returns 404 for unknown resource'
      description %(
        Verify that the server returns HTTP 404 when attempting to read
        a resource that does not exist.
      )

      input :server_url
      
      fhir_client do
        url :server_url
      end

      run do
        # Generate a random UUID that (almost certainly) won't exist
        unknown_id = SecureRandom.uuid

        # Attempt to read a non-existent Patient resource
        get("#{server_url}/Patient/#{unknown_id}")

        assert_response_status(404)
        
        # Validate error OperationOutcome if returned
        if resource.present? && resource.resourceType == 'OperationOutcome'
          assert_valid_resource
        end

      rescue Inferno::AssertionException => e
        fail("Expected 404 response for unknown resource but got: #{response&.status}\n#{e.message}")
      end
    end
  end
end