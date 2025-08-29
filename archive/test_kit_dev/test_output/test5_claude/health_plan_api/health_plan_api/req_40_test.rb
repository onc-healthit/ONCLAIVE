module Test5_claude
  class PractitionerQualificationCodingGroup < Inferno::TestGroup
    id :practitioner_qualification_coding
    title 'REQ-40: Practitioner Qualification Coding'
    description %(
      Validates that when a value set for coded concepts in qualification is 
      insufficient, the qualification can be provided in the text field of 
      the codeableConcept.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :qualification_text_field_test
      title 'Practitioner qualification allows text when code insufficient'
      description %(
        This test verifies that a Practitioner resource can be created and 
        retrieved with qualification information stored in the text field
        when the value set is insufficient.
      )
      
      input :practitioner_id
      
      run do
        # Create test qualification with text but no coding
        qualification = FHIR::Practitioner::Qualification.new(
          code: FHIR::CodeableConcept.new(
            text: 'Special Advanced Certification in Pediatric Care'
          )
        )

        practitioner = FHIR::Practitioner.new(
          id: practitioner_id,
          qualification: [qualification]
        )

        # Create the Practitioner
        fhir_create(practitioner)
        assert_response_status([200, 201])

        # Read it back
        fhir_read(:practitioner, practitioner_id)
        assert_response_status(200)
        assert_resource_type(:practitioner)

        retrieved = resource
        
        # Verify qualification text was preserved
        qual = retrieved.qualification&.first
        assert qual.present?, 'Practitioner qualification not found in retrieved resource'
        
        qual_text = qual.code&.text
        assert qual_text.present?, 'Qualification code text field is empty'
        assert qual_text == 'Special Advanced Certification in Pediatric Care',
               'Retrieved qualification text does not match expected value'
      end
    end

    test do
      id :qualification_coding_and_text_test 
      title 'Practitioner qualification allows both coding and text'
      description %(
        This test verifies that a Practitioner resource can include both
        coded values and supplemental text in qualifications.
      )

      input :practitioner_id

      run do
        qualification = FHIR::Practitioner::Qualification.new(
          code: FHIR::CodeableConcept.new(
            coding: [{
              system: 'http://terminology.hl7.org/CodeSystem/v2-0360',
              code: 'MD',
              display: 'Doctor of Medicine'
            }],
            text: 'Board Certified in Internal Medicine with Special Focus in Geriatrics'
          )
        )

        practitioner = FHIR::Practitioner.new(
          id: practitioner_id, 
          qualification: [qualification]
        )

        # Create the Practitioner
        fhir_create(practitioner)
        assert_response_status([200, 201])

        # Read it back
        fhir_read(:practitioner, practitioner_id)
        assert_response_status(200)
        assert_resource_type(:practitioner)

        retrieved = resource
        qual = retrieved.qualification&.first
        
        assert qual.present?, 'Practitioner qualification not found in retrieved resource'
        
        coding = qual.code&.coding&.first
        assert coding.present?, 'Qualification coding not found'
        assert coding.code == 'MD', 'Unexpected qualification code'
        
        text = qual.code&.text
        assert text.present?, 'Qualification text not found'
        assert text == 'Board Certified in Internal Medicine with Special Focus in Geriatrics',
               'Retrieved qualification text does not match expected value'
      end
    end
  end
end