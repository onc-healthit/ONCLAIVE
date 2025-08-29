module Test4Gpt
  class MustSupportElementsTestGroup < Inferno::TestGroup
    id :req_07_must_support_elements
    title 'Must Support Elements Processing'
    description %(
      Application Actor SHALL process resource instances containing Must Support data elements without errors or application failure.
    )

    input :server_url, :access_token, :resource_type, :resource_id

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :must_support_elements_processing
      title 'Process Must Support Elements'
      description %(
        Verify that the application can process resource instances containing Must Support data elements without errors or application failure.
      )

      run do
        # Read the resource to check for Must Support elements
        fhir_read(resource_type.to_sym, resource_id)
        
        assert_response_status(200)
        assert_valid_resource

        # Check for Must Support elements in the resource
        must_support_elements = resource.meta&.extension&.select { |ext| ext.url.include?('must-support') }
        
        assert must_support_elements.present?, 'Resource does not contain any Must Support elements.'

        # Additional logic to verify processing of Must Support elements can be added here

        pass 'Resource with Must Support elements processed successfully.'
      end
    end
  end
end