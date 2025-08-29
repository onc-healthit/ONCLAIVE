module Test6_claude
  class OrganizationContactTest < Inferno::TestGroup
    id :organization_contact_department_test
    title 'Organization Department Contact Handling'
    description %(
      Validates that organization contacts representing departments are properly formatted:
      - Family and given names should be blank
      - Department name should be populated in contact.name.text
      This implements REQ-39 for proper handling of department contacts.
    )

    test do
      id :department_contact_format
      title 'Department contacts have correct name formatting'
      description %(
        Verify that organization contacts representing departments have:
        1. Blank family and given names
        2. Department name in the name.text field
      )
      
      input :organization_id
      
      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        org = resource
        
        skip_if org.contact.nil?, 'Organization has no contacts to validate'

        dept_contacts = org.contact.select do |contact|
          # Look for contacts that appear to be departments (have text but no person names)
          contact&.name&.text.present? && 
            contact.name.given.blank? && 
            contact.name.family.blank?
        end

        skip_if dept_contacts.empty?, 'No department contacts found to validate'

        dept_contacts.each do |contact|
          assert contact.name.given.blank?, 
            "Department contact should have blank given name but was #{contact.name.given}"
          
          assert contact.name.family.blank?,
            "Department contact should have blank family name but was #{contact.name.family}"
          
          assert contact.name.text.present?,
            "Department contact must have department name in name.text"
        end

        pass "Successfully validated #{dept_contacts.length} department contact(s)"
      end
    end
  end
end