module Test6_claude
  class DataAbsentReasonGroup < Inferno::TestGroup
    id :data_absent_reason_test_group
    title 'Data Absent Reason Extension Tests'
    description %(
      Verify that when required data elements (minimum cardinality >0) are missing,
      the server includes appropriate dataAbsentReason extensions to explain why
      the data is not present.
    )

    test do
      id :verify_data_absent_reason
      title 'Server includes dataAbsentReason for missing required elements'
      description %(
        This test verifies that when required data elements are missing,
        the server properly includes the dataAbsentReason extension with
        appropriate values from the valueSet.
      )

      input :patient_id
      
      run do
        # Create a minimal Patient resource missing required elements
        patient = FHIR::Patient.new(
          id: patient_id,
          name: [] # Name is required but intentionally empty
        )

        # Attempt to create/update the patient
        fhir_update(patient, patient_id)

        # Verify response contains dataAbsentReason extension
        patient_response = resource

        assert_response_status([200, 201])
        assert_resource_type(:patient)

        # Check for dataAbsentReason extension on name element
        name_extension = patient_response.name&.first&.extension&.find do |ext| 
          ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
        end

        assert !name_extension.nil?, 
          'Server response must include dataAbsentReason extension for missing name element'

        # Verify extension has valid code from valueSet
        valid_codes = ['unknown', 'asked-unknown', 'temp-unknown', 'not-asked', 
                      'asked-declined', 'masked', 'not-applicable', 'unsupported', 
                      'as-text', 'error', 'not-a-number', 'negative-infinity',
                      'positive-infinity', 'not-performed', 'not-permitted']

        assert valid_codes.include?(name_extension.valueCode),
          "dataAbsentReason code '#{name_extension.valueCode}' must be from standard valueSet"

        pass "Server properly included dataAbsentReason extension for missing required element"
      end
    end

    test do
      id :verify_multiple_missing_elements
      title 'Server handles multiple missing required elements'
      description %(
        Verify server properly includes dataAbsentReason extensions when
        multiple required elements are missing from a resource.
      )

      input :patient_id
      
      run do
        patient = FHIR::Patient.new(
          id: patient_id,
          name: [], # Required
          gender: nil # Required
        )

        fhir_update(patient, patient_id)
        
        assert_response_status([200, 201])
        assert_resource_type(:patient)

        patient_response = resource

        # Check both name and gender have extensions
        has_name_extension = patient_response.name&.first&.extension&.any? do |ext|
          ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
        end

        has_gender_extension = patient_response.gender&.extension&.any? do |ext|
          ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason' 
        end

        assert has_name_extension, 
          'Missing dataAbsentReason extension for required name element'
        assert has_gender_extension,
          'Missing dataAbsentReason extension for required gender element'

        pass "Server properly handled multiple missing required elements"
      end
    end
  end
end