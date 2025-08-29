module Test4_gemini
  class RequiredMustSupportElementsHandlingTest < Inferno::Test
    id :req_06_required_must_support_elements_handling
    title 'Health Plan API provides reason for missing information when Must Support element is absent'
    description %(
      Health Plan API SHALL provide reason for missing information using nullFlavors or dataAbsentReason extension when Must Support element is absent and minimum cardinality is >0
    )

    input :resource_type,
          :resource_id,
          :must_support_element_path

    run do
      fhir_read(resource_type, resource_id)

      assert_response_status(200)
      assert_resource_type(resource_type)

      # Extract the element value using the provided path
      element_value = resource.dig(*must_support_element_path.split('.'))

      assert element_value.nil? || element_value.empty?,
             "Must Support element '#{must_support_element_path}' is present in resource."

      # Check for nullFlavor or dataAbsentReason extension
      if element_value.respond_to?(:extension)
        missing_info_extension = element_value.extension.find do |ext|
          ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
        end
        assert !missing_info_extension.nil?,
               "Must Support element '#{must_support_element_path}' is absent without a dataAbsentReason extension."
      else
        assert !element_value.nil? && element_value.respond_to?(:nullFlavor),
               "Must Support element '#{must_support_element_path}' is absent without a nullFlavor."
      end
    end
  end
end