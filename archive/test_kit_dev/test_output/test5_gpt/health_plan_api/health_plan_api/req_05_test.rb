module Test5Gpt
  class DataAbsentReasonTestGroup < Inferno::TestGroup
    id :req_05_data_absent_reason
    title 'Data Absent Reason for Missing Required Information'
    description %(
      This test group verifies that when information on a particular data element is not present and the minimum cardinality is greater than 0, the Health Plan API SHALL send the reason for the missing information using values from the dataAbsentReason extension or appropriate nullFlavors.
    )

    input :resource_type, :resource_id

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :check_data_absent_reason
      title 'Check dataAbsentReason for missing required information'
      description %(
        This test checks that the resource uses the dataAbsentReason extension or appropriate nullFlavors when required information is missing.
      )

      run do
        resource = fhir_read(resource_type.to_sym, resource_id).resource

        assert resource.present?, "Resource with ID #{resource_id} could not be found."

        missing_elements = resource.to_hash.select do |key, value|
          value.nil? && resource.class.element_definition(key).min > 0
        end.keys

        assert missing_elements.any?, 'No missing required elements found in the resource.'

        missing_elements.each do |element|
          extension = resource.try(:extension).find { |ext| ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason' }
          assert extension.present?, "Missing dataAbsentReason extension for element #{element}."
        end
      end
    end
  end
end