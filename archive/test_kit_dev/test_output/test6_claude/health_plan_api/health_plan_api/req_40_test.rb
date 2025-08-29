module Test6_claude
  class PractitionerQualificationCodingGroup < Inferno::TestGroup
    id :practitioner_qualification_coding
    title 'REQ-40: Practitioner Qualification Coding'
    description %(
      Validates that when a value set for coded concepts in qualifications is 
      insufficient, the qualification can be provided in the text field of the 
      codeableConcept element.

      This test verifies that:
      * A Practitioner resource can be created with qualification.code.text 
      * The text field contains the qualification when standard codes are insufficient
      * The server accepts and stores the text-based qualification properly
    )

    test do
      id :practitioner_qualification_text
      title 'Server supports text-based qualifications'
      description %(
        Verify that the server accepts a Practitioner resource with qualification 
        details provided in the text field of a codeableConcept.
      )

      input :practitioner_id
      
      run do
        # Create test qualification with text
        qualification = FHIR::Practitioner::Qualification.new(
          code: FHIR::CodeableConcept.new(
            text: 'Specialized Certification in Advanced Procedures'
          )
        )

        # Create practitioner with qualification
        practitioner = FHIR::Practitioner.new(
          id: practitioner_id,
          qualification: [qualification]
        )

        # Create/update the practitioner
        fhir_operation("Practitioner/#{practitioner_id}", body: practitioner)

        # Verify the practitioner was saved
        assert_response_status([200, 201])

        # Read back the practitioner
        fhir_read(:practitioner, practitioner_id)
        assert_response_status(200)
        saved_practitioner = resource

        # Verify qualification text was preserved
        assert saved_practitioner.qualification.present?, 
          'Expected practitioner to have qualifications'
        
        qual = saved_practitioner.qualification.first
        assert qual.code&.text == 'Specialized Certification in Advanced Procedures',
          'Expected qualification text to be preserved'
      end
    end

    test do
      id :practitioner_qualification_text_search
      title 'Server supports searching practitioners by qualification text'
      description %(
        Verify that practitioners can be found by searching qualification text.
      )
      
      run do
        # Search for practitioners with qualification text
        search_params = {
          'qualification-text': 'Specialized Certification'
        }
        fhir_search(:practitioner, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource
        assert bundle.entry.present?, 
          'Expected to find practitioners with matching qualification text'

        # Verify at least one result has matching text
        matching_qual = bundle.entry.any? do |entry|
          entry.resource.qualification&.any? do |qual|
            qual.code&.text&.include?('Specialized Certification')
          end
        end

        assert matching_qual, 
          'Expected to find practitioner with matching qualification text'
      end
    end
  end
end