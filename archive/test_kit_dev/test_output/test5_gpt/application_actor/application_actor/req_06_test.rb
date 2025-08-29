module Test5Gpt
  class MustSupportDataElementsTestGroup < Inferno::TestGroup
    id :req_06_must_support_data_elements
    title 'Must Support Data Elements Handling'
    description %(
      Application actors SHALL be capable of processing resource instances
      containing the Must Support data elements without generating an error
      or causing the application to fail.
    )

    input :server_url, :access_token, :resource_type, :resource_id

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :must_support_data_elements_test
      title 'Process Must Support Data Elements'
      description %(
        Verify that the application actor can process resource instances
        containing Must Support data elements without errors.
      )

      run do
        skip_if resource_type.nil? || resource_id.nil?, 'Resource type and ID must be provided'

        response = fhir_read(resource_type.to_sym, resource_id)
        assert_response_status(200)
        assert_valid_resource

        resource = response.resource
        must_support_elements = resource.meta.extension.select { |ext| ext.url.include?('must-support') }

        assert must_support_elements.any?, 'No Must Support elements found in the resource'

        must_support_elements.each do |element|
          assert resource.respond_to?(element.url.split('/').last), "Resource does not support #{element.url}"
        end

        pass 'Resource processed Must Support elements successfully'
      end
    end
  end
end