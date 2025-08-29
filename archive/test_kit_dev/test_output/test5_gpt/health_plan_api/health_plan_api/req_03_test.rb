module Test5Gpt
  class MustSupportDataElementsTestGroup < Inferno::TestGroup
    id :req_03_must_support_data_elements
    title 'Population of Must Support Data Elements'
    description %(
      Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results.
      This test verifies that the server can populate these elements in the returned resources.
    )

    input :server_url, :access_token, :resource_type, :resource_id

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :must_support_data_elements_test
      title 'Verify Must Support Data Elements are Populated'
      description %(
        This test checks that all Must Support data elements are populated in the resource returned by the server.
      )

      run do
        # Read the resource from the server
        response = fhir_read(resource_type.to_sym, resource_id)
        
        # Assert the response status is 200
        assert_response_status(200)
        
        # Assert the resource type matches the expected type
        assert_resource_type(resource_type.to_sym)
        
        # Validate the resource against the base FHIR specification
        assert_valid_resource

        # Retrieve the resource from the response
        resource = response.resource

        # Define the must support elements for the given resource type
        must_support_elements = {
          'Patient' => ['name', 'gender', 'birthDate'],
          'Coverage' => ['status', 'subscriberId', 'beneficiary']
          # Add more resource types and their must support elements as needed
        }

        # Ensure the resource type is supported
        skip_if must_support_elements[resource_type].nil?, "Must support elements not defined for resource type #{resource_type}"

        # Check each must support element is present
        must_support_elements[resource_type].each do |element|
          assert resource[element].present?, "Must support element #{element} is missing"
        end

        pass "All must support elements are populated for #{resource_type} with ID #{resource_id}"
      end
    end
  end
end