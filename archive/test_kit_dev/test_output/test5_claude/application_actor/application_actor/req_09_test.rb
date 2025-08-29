module Test5_claude
  class MissingInformationProcessingGroup < Inferno::TestGroup
    id :missing_information_processing
    title 'Client Processing of Missing Information Indicators'
    description %(
      Verify that Consumer App actors can process resource instances containing 
      Must Support data elements asserting missing information.
      
      This group tests the requirement REQ-09:
      "Consumer App actors SHALL be able to process resource instances containing 
      Must Support data elements asserting missing information."
    )

    test do
      id :missing_data_null_value
      title 'Process resource with null Must Support element'
      description %(
        Verify client can process a resource where a Must Support element 
        is present but set to null with appropriate nullFlavor coding.
      )
      
      input :patient_id
      
      run do
        # Create test patient with null must support element
        patient = FHIR::Patient.new(
          id: patient_id,
          meta: {
            profile: ['http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient']
          },
          name: [{
            given: ['Test'],
            family: 'Patient'
          }],
          birthDate: nil, # Must Support element set to null
          _birthDate: {
            extension: [{
              url: 'http://hl7.org/fhir/StructureDefinition/data-absent-reason',
              valueCode: 'unknown'
            }]
          }
        )

        fhir_create(patient)
        assert_response_status(201)

        # Verify client can read and process the resource
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        patient = resource
        assert patient.birthDate.nil?, 'Expected birthDate to be null'
        assert patient._birthDate&.extension&.first&.valueCode == 'unknown',
               'Expected data-absent-reason extension with code "unknown"'
      end
    end

    test do
      id :missing_data_extension
      title 'Process resource with data absent reason extension'
      description %(
        Verify client can process a resource where a Must Support element
        uses the data-absent-reason extension to indicate missing information.
      )

      input :patient_id
      
      run do
        # Create test patient with data absent reason
        patient = FHIR::Patient.new(
          id: patient_id,
          meta: {
            profile: ['http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient']
          },
          name: [{
            given: ['Test'],
            family: 'Patient'  
          }],
          extension: [{
            url: 'http://hl7.org/fhir/StructureDefinition/data-absent-reason',
            valueCode: 'masked'
          }]
        )

        fhir_create(patient)
        assert_response_status(201)

        # Verify client can read and process the resource
        fhir_read(:patient, patient_id) 
        assert_response_status(200)
        assert_resource_type(:patient)

        patient = resource
        absent_reason = patient.extension.find do |ext|
          ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
        end

        assert absent_reason.present?, 
               'Expected data-absent-reason extension to be present'
        assert absent_reason.valueCode == 'masked',
               'Expected data-absent-reason code to be "masked"'
      end
    end
  end
end