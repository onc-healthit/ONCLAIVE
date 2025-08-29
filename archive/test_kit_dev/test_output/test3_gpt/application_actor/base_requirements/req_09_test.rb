module Test4Gpt
  class MissingMustSupportTestGroup < Inferno::TestGroup
    id :req_09_missing_must_support
    title 'REQ-09: Missing Must Support Interpretation'
    description %(
      Application Actor SHALL interpret missing Must Support data elements as data not present in Health Plan API system.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :missing_must_support_interpretation
      title 'Interpretation of Missing Must Support Data Elements'
      description %(
        Verify that the Application Actor correctly interprets missing Must Support data elements as data not present in the Health Plan API system.
      )
      input :resource_type, :must_support_elements

      run do
        skip_if must_support_elements.blank?, 'No Must Support elements provided for verification.'

        # Fetch a resource to check for Must Support elements
        fhir_search(resource_type, params: { _count: 1 })
        assert_response_status(200)
        assert_resource_type(resource_type)

        resource = resource&.entry&.first&.resource
        skip_if resource.blank?, "No #{resource_type} resources found to verify Must Support elements."

        missing_elements = must_support_elements.reject do |element|
          resource.dig(*element.split('.'))
        end

        assert missing_elements.empty?, "The following Must Support elements are missing: #{missing_elements.join(', ')}"
        pass "All Must Support elements are present or correctly interpreted as missing."
      end
    end
  end
end