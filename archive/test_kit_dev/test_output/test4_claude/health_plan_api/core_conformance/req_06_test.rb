module Test4_claude
  class RequiredMustSupportTest < Inferno::TestGroup
    id :required_must_support_handling
    title 'Required Must Support Elements Handling'
    description %(
      Verify that the Health Plan API properly handles Must Support elements
      by providing reason for missing information using nullFlavors or 
      dataAbsentReason extension when a Must Support element is absent and
      minimum cardinality is >0.
    )

    test do
      id :must_support_reason_check
      title 'Check reason provided for missing Must Support elements'
      description %(
        This test verifies that when a Must Support element with minimum 
        cardinality >0 is absent, the server provides an appropriate reason
        using either nullFlavor or dataAbsentReason extension.
      )

      # Define inputs needed for the test
      input :patient_id
      input :resource_type

      run do
        # Get the resource
        fhir_read(resource_type.to_sym, patient_id)
        assert_response_status(200)
        resource = resource_under_test

        # Get definition of resource type to identify Must Support elements
        definition = resource.class::METADATA

        must_support_elements = definition.select do |element| 
          element.mustSupport == true && element.min > 0
        end

        must_support_elements.each do |element|
          # Check if element is present
          element_value = resource.send(element.local_name)
          
          if element_value.nil? || element_value.empty?
            # Element is missing, verify reason exists
            has_reason = false

            # Check for nullFlavor
            null_flavor = resource.extension.find do |ext|
              ext.url == 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor'
            end
            has_reason = true if null_flavor.present?

            # Check for dataAbsentReason
            absent_reason = resource.extension.find do |ext|
              ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
            end
            has_reason = true if absent_reason.present?

            assert has_reason, %(
              Must Support element #{element.local_name} is missing but no reason
              was provided via nullFlavor or dataAbsentReason extension
            )
          end
        end

        pass "All missing Must Support elements have valid reasons provided"
      end
    end
  end
end