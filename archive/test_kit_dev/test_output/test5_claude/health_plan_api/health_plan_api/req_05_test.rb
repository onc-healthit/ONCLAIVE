module Test5_claude
  class DataAbsentReasonGroup < Inferno::TestGroup
    id :data_absent_reason_validation
    title 'Data Absent Reason Validation'
    description %(
      Validates that required elements with missing information properly use 
      dataAbsentReason extension or appropriate null values from value sets.

      Systems SHALL send the reason for missing information when minimum 
      cardinality is >0 using either:
      - Values from applicable valuesets where they exist
      - The dataAbsentReason extension
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :validate_data_absent_reason
      title 'Required elements use dataAbsentReason when data is missing'
      description %(
        This test verifies that when required elements (min > 0) are missing,
        the reason is properly communicated using dataAbsentReason extension
        or appropriate null values.
      )
      
      input :patient_id
      
      run do
        # Create Patient with missing required field (name)
        patient = FHIR::Patient.new(
          id: patient_id,
          active: true
        )

        # Add dataAbsentReason extension
        extension = FHIR::Extension.new(
          url: 'http://hl7.org/fhir/StructureDefinition/data-absent-reason',
          valueCode: 'unknown'
        )
        
        patient.name = [
          FHIR::HumanName.new(
            extension: [extension]
          )
        ]

        # Create the patient and validate response
        fhir_create(patient)
        assert_response_status(201)
        assert_resource_type(:patient)
        
        created_patient = resource
        assert_valid_resource

        # Verify dataAbsentReason extension exists
        name = created_patient.name.first
        absent_reason = name.extension.find do |ext| 
          ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
        end

        assert !absent_reason.nil?, 
          'dataAbsentReason extension not found for missing required name'
        
        assert absent_reason.valueCode == 'unknown',
          'incorrect dataAbsentReason code'

        # Clean up
        fhir_delete(:patient, created_patient.id)
      end
    end

    test do
      id :validate_missing_required_field
      title 'Server rejects resources missing required fields without reason'
      description %(
        This test verifies that the server rejects resources that have missing
        required fields without a dataAbsentReason or null value specified.
      )

      run do
        # Create invalid Patient missing required name field
        patient = FHIR::Patient.new(
          active: true
        )

        # Attempt to create - should be rejected
        fhir_create(patient)
        
        assert_response_status([400, 422])
        assert_resource_type(:operationoutcome)

        outcome = resource
        assert !outcome.issue.empty?, 'OperationOutcome should contain validation issues'
        
        error = outcome.issue.any? do |issue|
          issue.severity == 'error' && 
          issue.diagnostics&.match(/missing required/i)
        end

        assert error, 'OperationOutcome should indicate missing required field'
      end
    end
  end
end