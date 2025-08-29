module Test5Gpt
  class RevIncludesSupportTestGroup < Inferno::TestGroup
    id :req_28_revincludes_support
    title 'Support for _revincludes'
    description %(
      This test group verifies that the Health Plan API server supports the _revincludes
      functionality for specified resources as required by REQ-28.
    )

    input :server_url, :access_token, :resource_type, :resource_id

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :revincludes_support_test
      title 'Server supports _revincludes for specified resources'
      description %(
        Verify that the server supports the _revincludes functionality for the given resource type.
        The test will attempt to retrieve resources that reference the specified resource using the
        _revincludes parameter.
      )

      run do
        skip_if resource_type.blank?, 'Resource type not provided'
        skip_if resource_id.blank?, 'Resource ID not provided'

        # Example _revincludes parameter, replace with actual list as needed
        revincludes_param = '_revincludes=Observation:subject'

        fhir_search(resource_type, params: { _id: resource_id, _revincludes: revincludes_param })

        assert_response_status(200)
        assert_valid_resource

        resources = resource.entry.map(&:resource)
        assert resources.any?, "No resources returned with _revincludes for #{resource_type} with ID #{resource_id}"

        # Additional assertions can be added here to verify specific _revincludes behavior
      end
    end
  end
end