module Test5Gpt
  class MissingMustSupportDataTestGroup < Inferno::TestGroup
    id :req_08_missing_must_support_data
    title 'REQ-08: Client Interpretation of Missing Must Support Data'
    description %(
      This test group verifies that when querying Health Plan API actors,
      Application actors interpret missing Must Support data elements within
      resource instances as data not present in the Health Plan API actor's system.
    )

    input :server_url, :access_token, :resource_type, :resource_id

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :interpret_missing_must_support_data
      title 'Interpret Missing Must Support Data'
      description %(
        This test checks that the application actor correctly interprets missing
        Must Support data elements in a resource instance as data not present
        in the Health Plan API actor's system.
      )

      run do
        fhir_read(resource_type, resource_id)

        assert_response_status(200)
        assert_valid_resource

        resource = resource()

        # Assuming Must Support elements are defined in a profile or specification
        must_support_elements = ['element1', 'element2'] # Example elements

        missing_elements = must_support_elements.select do |element|
          !resource.respond_to?(element) || resource.send(element).nil?
        end

        assert missing_elements.empty?, "The following Must Support elements are missing or nil: #{missing_elements.join(', ')}"
      end
    end
  end
end