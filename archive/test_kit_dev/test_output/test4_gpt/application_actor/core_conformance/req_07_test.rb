module Test4Gpt
  class MustSupportElementsProcessingTestGroup < Inferno::TestGroup
    id :req_07_must_support_elements_processing
    title 'Must Support Elements Processing'
    description %(
      Application Actor SHALL process resource instances containing Must Support data elements without errors or application failure.
      This test verifies that the application can handle resources with Must Support elements correctly.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :must_support_elements_processing_test
      title 'Process Must Support elements without errors'
      description %(
        This test checks that the application processes resources with Must Support elements without errors or failures.
      )
      input :resource_type, :resource_id

      run do
        fhir_read(resource_type.to_sym, resource_id)
        
        assert_response_status(200)
        assert_valid_resource

        # Additional logic to verify Must Support elements
        must_support_elements = resource.meta&.profile&.flat_map do |profile_url|
          profile = fhir_client.read(FHIR::StructureDefinition, profile_url.split('/').last).resource
          profile&.snapshot&.element&.select { |el| el.mustSupport }
        end.compact

        must_support_elements.each do |element|
          assert resource.to_hash.dig(*element.path.split('.')), "Must Support element #{element.path} is missing"
        end

        pass 'The application processes Must Support elements correctly.'
      end
    end
  end
end