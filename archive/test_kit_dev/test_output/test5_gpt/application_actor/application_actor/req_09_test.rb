module Test5Gpt
  class ClientProcessingOfMissingInformationIndicatorsTestGroup < Inferno::TestGroup
    id :req_09_client_processing_of_missing_information
    title 'Client Processing of Missing Information Indicators'
    description %(
      Consumer App actors SHALL be able to process resource instances containing Must Support data elements asserting missing information.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :process_missing_information_indicators
      title 'Process resource instances with missing information indicators'
      description %(
        This test verifies that the application can process resources with Must Support elements indicating missing information.
      )
      input :resource_type, :resource_id

      run do
        skip_if resource_type.blank? || resource_id.blank?, 'Resource type and ID must be provided'

        resource = fhir_read(resource_type, resource_id).resource

        assert_response_status(200)
        assert_valid_resource

        # Check for Must Support elements with missing information indicators
        missing_info_elements = resource.to_hash.select do |key, value|
          value == { 'extension' => [{ 'url' => 'http://hl7.org/fhir/StructureDefinition/data-absent-reason', 'valueCode' => 'unknown' }] }
        end

        assert missing_info_elements.present?, 'No Must Support elements with missing information indicators found'
        pass "Resource contains Must Support elements with missing information indicators"
      end
    end
  end
end