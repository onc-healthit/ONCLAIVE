module Test5_gemini
  class RevIncludesSupportTest < Inferno::TestGroup
    id :req_28_rev_includes_support
    title 'REQ-28: Support for _revincludes'
    description %(
      Verify that the server supports the following _revincludes for each resource: [list].
      Reference: <a href='[link to specific location in specification]'>[Requirement ID]</a>
    )

    # Replace [resource_type] with actual resource types from the specification
    test do
      id :[resource_type]_rev_includes_test
      title 'Server supports _revincludes for [resource_type] resource'
      description %(
        Verify that the server supports the required _revincludes when retrieving a [resource_type] resource.
      )
      input :[resource_type]_id

      run do
        # Replace [revincludes] with actual values from the specification
        fhir_read(
          :[resource_type],
          "[resource_type]_id",
          params: { '_revincludes' => '[revincludes]' }
        )

        assert_response_status(200)
        assert_resource_type(:[resource_type])
        assert_valid_resource

        # Add assertions to validate the presence and correctness of reversed included resources
        # based on the specific _revincludes used and the expected response structure.
      end
    end
  end
end
