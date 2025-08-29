module Test5Gemini
  class PractitionerQualificationCodingTest < Inferno::Test
    id :req_40_practitioner_qualification_coding
    title 'Practitioner qualification can be provided in text field when value set is insufficient'
    description %(
      When the value set for the coded concept in Practitioner.qualification is insufficient, 
      the qualification can be provided in the text field of the codeableConcept.
    )

    input :practitioner_id
    
    run do
      skip_if_not_supported(:Practitioner, [:read])
      skip_if resource.blank?, 'No Practitioner resources appear to be available. Please use patients with more information.'

      practitioner = resource

      practitioner.qualification.each do |qualification|
        if qualification.code.coding.any? && qualification.text.present?
          pass 'Practitioner qualification includes both coding and text'
          break
        elsif !qualification.code.coding.any? && qualification.text.present?
          warning 'Practitioner qualification relies solely on text field due to insufficient value set'
          break
        end
      end

      warning 'No Practitioner qualifications found with both coding and text or text only'
    end
  end
end
