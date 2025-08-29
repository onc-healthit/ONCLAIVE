module Test5Gpt
  class UnknownResourceResponseTestGroup < Inferno::TestGroup
    id :req_16_unknown_resource_response
    title 'Unknown Resource Response'
    description %(
      This test group verifies that the Health Plan API returns a 404 status code
      when an unknown resource is requested, as required by REQ-16.
    )

    test do
      id :req_16_unknown_resource_response_test
      title 'Server returns 404 for unknown resource'
      description %(
        This test checks that the server returns a 404 status code when an
        unknown resource is requested. This is to ensure that the server
        correctly handles requests for resources that do not exist.
      )
      input :server_url

      run do
        # Attempt to read a non-existent resource
        fhir_read(:unknown_resource, 'nonexistent-id')

        # Assert that the response status is 404
        assert_response_status(404)
      end
    end
  end
end