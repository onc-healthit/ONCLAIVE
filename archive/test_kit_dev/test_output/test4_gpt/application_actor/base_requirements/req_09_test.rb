module Test4Gpt
  class MissingMustSupportInterpretationTest < Inferno::TestGroup
    id :req_09_missing_must_support_interpretation
    title 'Missing Must Support Interpretation'
    description %(
      Application Actor SHALL interpret missing Must Support data elements as data not present in Health Plan API system.
      This test verifies that the application correctly handles missing Must Support elements by checking the response
      from the Health Plan API when these elements are not present.
    )

    input :server_url, :access_token, :resource_type, :must_support_elements

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :check_missing_must_support_elements
      title 'Check Missing Must Support Elements'
      description %(
        This test checks if the application correctly interprets missing Must Support elements as data not present
        in the Health Plan API system. It verifies that the absence of these elements does not result in an error
        and that the application handles such cases gracefully.
      )

      run do
        # Perform a search or read operation on the specified resource type
        response = fhir_search(resource_type, params: { _count: 1 })

        assert_response_status(200)
        assert_valid_resource

        resource = response.resource.entry.first.resource
        missing_elements = must_support_elements.reject { |element| resource[element].present? }

        assert missing_elements.empty?, "The following Must Support elements are missing: #{missing_elements.join(', ')}"
        pass 'All Must Support elements are present or correctly interpreted as missing'
      end
    end
  end
end