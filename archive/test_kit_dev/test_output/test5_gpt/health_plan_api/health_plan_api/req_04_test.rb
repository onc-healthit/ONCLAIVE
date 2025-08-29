module Test5Gpt
  class NotIncludingAbsentDataElementsTestGroup < Inferno::TestGroup
    id :req_04_not_including_absent_data_elements
    title 'REQ-04: Not Including Absent Data Elements'
    description %(
      This test group verifies that Health Plan API actors do not include data elements
      in the resource instance when information on a particular Must Support data element
      is not present and the minimum cardinality is 0, as per REQ-04.
    )

    input :resource_type, :resource_id

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :check_absent_data_elements
      title 'Verify absent Must Support data elements are not included'
      description %(
        This test checks that when a Must Support data element is absent and its minimum
        cardinality is 0, it is not included in the resource instance returned by the
        Health Plan API.
      )

      run do
        fhir_read(resource_type.to_sym, resource_id)
        
        assert_response_status(200)
        assert_valid_resource

        resource = resource()

        # Assuming 'must_support_elements' is a predefined list of Must Support elements
        # with minimum cardinality 0 for the given resource type
        must_support_elements = [] # Define this list based on the resource type

        must_support_elements.each do |element|
          assert !resource[element].present?, "Resource should not include #{element} when it is absent and cardinality is 0"
        end
      end
    end
  end
end