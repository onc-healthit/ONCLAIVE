module Test4Gpt
  class RequiredMustSupportElementsHandlingTestGroup < Inferno::TestGroup
    id :req_06_required_must_support_elements_handling
    title 'Required Must Support Elements Handling'
    description %(
      Health Plan API SHALL provide reason for missing information using nullFlavors
      or dataAbsentReason extension when Must Support element is absent and minimum
      cardinality is >0.
    )

    input :resource_type, :resource_id

    test do
      id :check_missing_must_support_elements
      title 'Check for missing Must Support elements'
      description %(
        Verify that the Health Plan API provides a reason for missing Must Support
        elements using nullFlavors or dataAbsentReason extension when the element
        is absent and has a minimum cardinality greater than 0.
      )

      run do
        fhir_read(resource_type.to_sym, resource_id)

        assert_response_status(200)
        assert_valid_resource

        must_support_elements = resource.meta&.profile&.flat_map do |profile_url|
          # Fetch the StructureDefinition for the profile
          profile_definition = fhir_client.read(FHIR::StructureDefinition, profile_url).resource
          profile_definition&.snapshot&.element&.select do |element|
            element.mustSupport && element.min > 0
          end
        end.compact

        missing_elements = must_support_elements.select do |element|
          element_path = element.path.split('.').drop(1).join('.')
          FHIRPath.evaluate(element_path, resource).empty?
        end

        missing_elements.each do |element|
          element_path = element.path.split('.').drop(1).join('.')
          data_absent_reason = FHIRPath.evaluate("#{element_path}.extension('http://hl7.org/fhir/StructureDefinition/data-absent-reason')", resource)
          null_flavor = FHIRPath.evaluate("#{element_path}.nullFlavor", resource)

          assert(
            data_absent_reason.present? || null_flavor.present?,
            "Missing Must Support element '#{element.path}' does not have a dataAbsentReason or nullFlavor."
          )
        end

        pass "All missing Must Support elements have a dataAbsentReason or nullFlavor."
      end
    end
  end
end