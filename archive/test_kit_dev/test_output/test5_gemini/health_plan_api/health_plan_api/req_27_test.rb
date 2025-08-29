module Test5_gemini
  class Req27SupportForIncludes < Inferno::TestGroup
    id :req_27_support_for_includes
    title 'REQ-27: Support for _includes'
    description %(
      Verify that the server supports the following _includes for each resource as specified by the Health Plan API requirements.
    )

    # TODO: Add tests for each resource and its supported _includes based on the specification.
    # Example test for Patient resource with _include=Patient:organization
    test do
      id :patient_includes_organization
      title 'Server supports _include=Patient:organization'
      description 'Verify that the server supports the _include=Patient:organization parameter.'
      input :patient_id

      run do
        fhir_read(:patient, patient_id, params: { '_include': 'Patient:organization' })
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_valid_resource

        patient = resource
        assert patient.organization.present?, 'Patient resource did not contain an organization reference.'
      end
    end

    # Add more tests for other resources and their supported _includes...
  end
end
