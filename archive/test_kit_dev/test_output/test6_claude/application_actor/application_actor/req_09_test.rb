module Test6_claude
  class MissingInformationProcessingGroup < Inferno::TestGroup
    id :missing_information_processing
    title 'Client Processing of Missing Information Indicators'
    description %(
      Verify that Consumer App actors can properly process resource instances 
      containing Must Support data elements that assert missing information.
      
      This includes handling of:
      * Data Absent Reason extensions
      * Null values
      * Empty arrays
      * Missing optional elements
    )

    test do
      id :process_data_absent_reason
      title 'Process Data Absent Reason Extensions'
      description %(
        Verify the client can process resources containing dataAbsentReason 
        extensions on Must Support elements.
      )

      fhir_client do
        url :url
        bearer_token :bearer_token
      end

      run do
        # Create test patient with data absent reason
        patient = FHIR::Patient.new(
          name: [
            {
              extension: [
                {
                  url: 'http://hl7.org/fhir/StructureDefinition/data-absent-reason',
                  valueCode: 'unknown'
                }
              ]
            }
          ]
        )

        begin
          response = fhir_create(patient)
          assert_response_status(201)
          patient_id = response.resource.id
          
          # Verify client can read and process the resource
          read_response = fhir_read(:patient, patient_id)
          assert_response_status(200)
          assert_resource_type(:patient)
          
          processed_patient = read_response.resource
          assert processed_patient.name.first.extension.any? { |ext| 
            ext.url == 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
          }, 'Client must preserve data absent reason extension'

        ensure
          fhir_delete(:patient, patient_id) if patient_id
        end
      end
    end

    test do
      id :process_null_values
      title 'Process Null Values'
      description %(
        Verify the client can process resources with null values 
        in Must Support elements.
      )

      run do
        patient = FHIR::Patient.new(
          birthDate: nil,
          deceased: nil
        )

        begin
          response = fhir_create(patient)
          assert_response_status(201)
          patient_id = response.resource.id

          read_response = fhir_read(:patient, patient_id)
          assert_response_status(200)
          assert_resource_type(:patient)

          processed_patient = read_response.resource
          assert processed_patient.birthDate.nil?, 'Client must preserve null birthDate'
          assert processed_patient.deceased.nil?, 'Client must preserve null deceased status'

        ensure
          fhir_delete(:patient, patient_id) if patient_id
        end
      end
    end

    test do
      id :process_empty_arrays
      title 'Process Empty Arrays'
      description %(
        Verify the client can process resources with empty arrays
        in Must Support elements.
      )

      run do
        patient = FHIR::Patient.new(
          name: [],
          telecom: [],
          address: []
        )

        begin
          response = fhir_create(patient)
          assert_response_status(201)
          patient_id = response.resource.id

          read_response = fhir_read(:patient, patient_id)
          assert_response_status(200)
          assert_resource_type(:patient)

          processed_patient = read_response.resource
          assert processed_patient.name.empty?, 'Client must preserve empty name array'
          assert processed_patient.telecom.empty?, 'Client must preserve empty telecom array'
          assert processed_patient.address.empty?, 'Client must preserve empty address array'

        ensure
          fhir_delete(:patient, patient_id) if patient_id
        end
      end
    end
  end
end