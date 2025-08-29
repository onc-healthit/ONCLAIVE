module Test5Gemini
  class DataAbsentReasonTest < Inferno::Test
    id :req_05_data_absent_reason
    title 'Missing required information uses dataAbsentReason'
    description %(
      Verify that the server utilizes dataAbsentReason when required information is missing.
    )

    input :resource_type,
          :resource_id,
          :required_element

    run do
      fhir_read(resource_type, resource_id)

      assert_response_status(200)
      assert_resource_type(resource_type)

      resource = response[:resource]
      element_path = required_element.split('.')

      element_value = element_path.reduce(resource) do |obj, key|
        obj.respond_to?(:[]) ? obj[key] : nil
      end

      assert !element_value, "Element '#{required_element}' should be absent."

      data_absent_reason_present = element_path.any? do |key|
        !resource.send(key)&.extension&.any? { |ext| ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason' }
      end

      assert data_absent_reason_present, "dataAbsentReason extension not found for missing element '#{required_element}'."
    end
  end
end