module Test
  class MustSupportElementsGroup < Inferno::TestGroup
    id :must_support_elements_processing
    title 'Must Support Elements Processing'
    description %(
      Verify that the Application Actor can process resource instances containing 
      Must Support data elements without errors or application failure.
    )

    test do
      id :must_support_elements_test
      title 'Process resources with Must Support elements'
      description %(
        This test verifies that the Application Actor can successfully process
        resource instances that contain Must Support data elements without 
        generating errors or failing.
      )

      input :resource_type,
            title: 'Resource Type',
            description: 'The FHIR resource type to test',
            type: 'text'
      
      input :test_resource_id,
            title: 'Test Resource ID', 
            description: 'ID of a resource instance containing Must Support elements',
            type: 'text'

      makes_request :must_support_resource

      run do
        fhir_read(resource_type.to_sym, test_resource_id, name: :must_support_resource)

        assert_response_status(200)
        assert_resource_type(resource_type.to_sym)

        assert resource.present?, 'Resource could not be parsed after retrieval'

        must_support_elements = resource.class::METADATA.select do |element|
          element.try(:mustSupport) == true
        end

        must_support_elements.each do |element|
          assert resource.send(element.local_name).present?,
            "Must Support element '#{element.local_name}' is missing or empty"
        end

        pass "Successfully processed resource containing Must Support elements"
      end
    end
  end
end