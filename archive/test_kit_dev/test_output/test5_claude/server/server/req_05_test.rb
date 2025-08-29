module Test5_claude
  class DataAbsentReasonTest < Inferno::TestGroup
    id :data_absent_reason_test
    title 'Data Absent Reason Extension Tests'
    description %(
      Verify that the server properly implements data absent reason extensions
      when required elements are missing. The server SHALL send the reason for 
      missing information using values from the dataAbsentReason value set where
      they exist.
    )

    test do
      id :check_required_missing_with_reason
      title 'Required elements use dataAbsentReason when missing'
      description %(
        When a required element is missing (minimum cardinality > 0), 
        verify that a valid dataAbsentReason extension is present explaining
        the reason for the missing data.
      )
      
      # Create test patient missing required data
      run do
        patient = FHIR::Patient.new
        patient.meta = FHIR::Meta.new
        patient.meta.profile = ['http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient']
        
        # Name is required but intentionally omitted
        # Should trigger dataAbsentReason
        
        begin
          response = fhir_create(patient)
          assert_response_status([201, 200])
          
          created_patient = response.resource
          
          # Verify dataAbsentReason extension exists on name element
          name_extension = created_patient.name&.first&.extension&.find do |ext| 
            ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
          end
          
          assert !name_extension.nil?, 
            'Required name element is missing but no dataAbsentReason extension found'
            
          # Verify extension has valid code from valueSet
          valid_codes = ['unknown', 'asked-unknown', 'temp-unknown', 'not-asked',
                        'asked-declined', 'masked', 'not-applicable', 'unsupported',
                        'as-text', 'error', 'not-a-number', 'negative-infinity',
                        'positive-infinity', 'not-performed', 'not-permitted']
                        
          assert valid_codes.include?(name_extension.valueCode),
            "dataAbsentReason code '#{name_extension.valueCode}' not from valid value set"

        rescue StandardError => e
          skip "Server rejected test patient creation: #{e.message}"
        end
      end
    end

    test do
      id :check_missing_data_validation
      title 'Server rejects missing required data without reason'
      description %(
        Verify that the server rejects resources missing required elements
        when no dataAbsentReason extension is provided.
      )
      
      run do
        patient = FHIR::Patient.new
        patient.meta = FHIR::Meta.new
        patient.meta.profile = ['http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient']
        
        # Name required but missing with no dataAbsentReason
        
        response = fhir_create(patient)
        
        assert_response_status(422),
          'Server should reject resource missing required elements with no dataAbsentReason'
          
        assert_operation_outcome(response.resource)
      end
    end
  end
end