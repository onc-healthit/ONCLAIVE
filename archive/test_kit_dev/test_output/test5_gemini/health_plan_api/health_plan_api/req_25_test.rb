# frozen_string_literal: true

module Test5_gemini
  class ReadInteractionTest < Inferno::TestGroup
    id :req_25_read_interaction_support
    title 'REQ-25: Support for read interaction'
    description %(
      For each resource type and profile, a Plan Net server SHALL support the read interaction.
    )

    test do
      id :req_25_patient_read
      title 'Server supports Patient read interaction'
      description 'Verify that the server supports reading a Patient resource by its id.'
      input :patient_id

      run do
        fhir_read(:patient, patient_id)

        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource

        patient = resource
        assert patient.id == patient_id, "Expected Patient id to be #{patient_id} but was #{patient.id}"
      end
    end

    # Additional tests for other resource types and profiles can be added here
  end
end