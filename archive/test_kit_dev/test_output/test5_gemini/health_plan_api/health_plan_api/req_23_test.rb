# frozen_string_literal: true

module Test5_gemini
  class Req23XmlFormatSupportTest < Inferno::TestGroup
    id :req_23_xml_format_support
    title 'REQ-23: XML Format Support'
    description %(
      Verify that the server supports XML source formats for all Plan-Net interactions.
    )

    test do
      id :req_23_patient_read_xml
      title 'Server supports Patient read interaction with XML'
      description %(
        Verify that the server can return a Patient resource in XML format.
      )
      input :patient_id
      makes_request :patient_xml

      run do
        fhir_read(:patient, patient_id, format: :xml)

        assert_response_status(200)
        assert_response_header('Content-Type', 'application/fhir+xml;charset=utf-8', 'The server did not respond with the correct content type.')
        assert_valid_resource(resource, format: :xml)
      end
    end

    # Add similar tests for other Plan-Net interactions (e.g., search, create, update, delete)
    # and resources as needed, following the same pattern as the Patient read test.
  end
end