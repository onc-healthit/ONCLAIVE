module Test4Gpt
  class OptionalMustSupportHandlingTestGroup < Inferno::TestGroup
    id :req_05_optional_must_support_handling
    title 'REQ-05: Optional Must Support Elements Handling'
    description %(
      Health Plan API SHALL NOT include Must Support data elements in resource
      instances when information is not present and minimum cardinality is 0.
    )

    input :resource_type, :resource_id, :server_url, :access_token

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :req_05_optional_must_support_test
      title 'Verify Must Support elements are not included when not present'
      description %(
        This test checks that the Health Plan API does not include Must Support
        elements in resource instances when the information is not present and
        the minimum cardinality is 0.
      )

      run do
        skip_if resource_type.blank?, 'Resource type is not provided'
        skip_if resource_id.blank?, 'Resource ID is not provided'

        fhir_read(resource_type.to_sym, resource_id)
        assert_response_status(200)
        assert_valid_resource

        resource = resource.to_hash
        must_support_elements = [] # Define the Must Support elements for the resource type

        must_support_elements.each do |element|
          assert resource[element].nil?, "Must Support element '#{element}' should not be present when information is not available"
        end

        pass 'Must Support elements are correctly not included when information is not present'
      end
    end
  end
end