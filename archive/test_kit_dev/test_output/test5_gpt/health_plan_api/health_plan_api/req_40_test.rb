module Test5Gpt
  class PractitionerQualificationCodingTestGroup < Inferno::TestGroup
    id :practitioner_qualification_coding_test_group
    title 'Practitioner Qualification Coding'
    description %(
      This test group verifies that when the value set for the coded concept in qualification is insufficient,
      the qualification can be provided in the text field of the CodeableConcept.
    )

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :practitioner_qualification_coding_test
      title 'Practitioner qualification coding allows text field usage'
      description %(
        This test checks if the Practitioner resource's qualification element allows the use of the text field
        in the CodeableConcept when the value set is insufficient.
      )
      input :practitioner_id

      run do
        fhir_read(:practitioner, practitioner_id)
        assert_response_status(200)
        assert_resource_type(:practitioner)
        assert_valid_resource

        practitioner = resource
        assert practitioner.qualification.any?, 'No qualifications found in Practitioner resource'

        qualification = practitioner.qualification.first
        assert qualification.code.present?, 'Qualification code is missing'
        assert qualification.code.text.present?, 'Qualification code text is missing'
        assert qualification.code.coding.none? || qualification.code.coding.all? { |coding| coding.code.blank? }, 
               'Expected qualification coding to be insufficient, requiring text field usage'
      end
    end
  end
end