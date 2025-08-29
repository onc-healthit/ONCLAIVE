module Test5_gemini
  class AbsentDataElementTest < Inferno::Test
    id :req_04_absent_data_elements
    title 'Absent Must Support data elements are not included in resources'
    description %(
      Health Plan API actors SHALL NOT include Must Support data elements with a minimum cardinality of 0 when the data is not present.
    )

    run do
      skip_if_known_not_supported(:Patient, [:read])

      patient_id = resource_references(:Patient).first.try(:reference)
      skip_if patient_id.blank?, 'No Patient resources available for this test.'

      response = fhir_read(:Patient, patient_id)
      assert_response_status(200)
      assert_resource_type(:Patient)

      # Example: Check for the presence of 'Patient.communication'
      # Replace with actual Must Support elements relevant to the tested profile
      assert_empty resource.communication, 'Must Support element "communication" is present with no data.'
    end
  end
end