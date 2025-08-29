# frozen_string_literal: true

module Test4_gemini
  class MustSupportElementsProcessingTest < Inferno::TestGroup
    id :req_07_must_support_elements_processing
    title 'REQ-07: Must Support Elements Processing'
    description %(
      Verify that the application under test can process resource instances containing Must Support data elements without errors or application failure.
    )

    test do
      id :req_07_must_support_elements_processing_test
      title 'Application can process resources with Must Support elements'
      description %(
        This test verifies that the application can successfully process a resource containing Must Support data elements.
      )
      input :must_support_resource

      run do
        skip_if must_support_resource.blank?, 'No resource with Must Support elements provided.'

        fhir_create(must_support_resource)

        assert_response_status(201), 'Expected HTTP Status Code 201, but found: %{status}' % { status: response[:status] }
      end
    end
  end
end