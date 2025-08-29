module Test5_claude
  class PractitionerQualificationGroup < Inferno::TestGroup
    id :practitioner_qualification_coding
    title 'Practitioner Qualification Coding'
    description %(
      Validates that when the value set for coded concepts in qualification is 
      insufficient, the qualification can be provided in the text field of the 
      codeableConcept.

      This test verifies REQ-40 by:
      - Creating a Practitioner with qualification using text field
      - Reading back the created Practitioner
      - Validating the qualification text is preserved
    )

    test do
      id :practitioner_qualification_text_test
      title 'Server allows qualification text when code insufficient'
      description %(
        Tests that a Practitioner resource can be created with qualification text
        when standard codes are insufficient.
      )

      input :server_url
      
      fhir_client do
        url :server_url
      end

      run do
        # Create test Practitioner with qualification text
        qualification = FHIR::Practitioner::Qualification.new(
          code: FHIR::CodeableConcept.new(
            text: 'Special Advanced Certification in Pediatric Emergency Medicine'
          )
        )

        practitioner = FHIR::Practitioner.new(
          name: [FHIR::HumanName.new(family: 'Smith')],
          qualification: [qualification]
        )

        create_response = fhir_create(practitioner)
        assert_response_status(201)

        # Read back created Practitioner
        practitioner_id = create_response.resource.id
        read_response = fhir_read(:practitioner, practitioner_id)
        assert_response_status(200)
        assert_resource_type(:practitioner)

        created_practitioner = read_response.resource
        saved_qualification = created_practitioner.qualification&.first
        
        assert saved_qualification.present?, 
          'Created Practitioner should have qualification'
        
        assert saved_qualification.code&.text == 'Special Advanced Certification in Pediatric Emergency Medicine',
          'Qualification text should be preserved'

        # Cleanup
        fhir_delete(:practitioner, practitioner_id)
      end
    end
  end
end