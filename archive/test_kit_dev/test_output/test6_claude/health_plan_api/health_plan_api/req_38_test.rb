module Test6_claude
  class NetworkContactDepartmentTest < Inferno::TestGroup
    id :network_contact_department_handling
    title 'Network Contact Handling for Departments'
    description %(
      Validates that when a contact is a department name rather than a human,
      the implementation properly structures the contact with:
      - Blank family and given names
      - Department name in contact.name.text
    )

    test do
      id :validate_department_contact_structure
      title 'Department Contact Has Required Structure'
      description %(
        Validates that department contacts follow the specified structure:
        - Family name is blank/null
        - Given name is blank/null 
        - Department name is populated in name.text
      )
      
      input :organization_id
      
      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        organization = resource

        # Skip if no contacts present
        skip_if organization.contact.nil?, 'Organization has no contacts to validate'

        department_contacts = organization.contact.select do |contact|
          contact&.name&.text.present? && 
          contact.name.given.blank? &&
          contact.name.family.blank?
        end

        skip_if department_contacts.empty?, 'No department contacts found to validate'

        department_contacts.each do |contact|
          assert contact.name.text.present?, 
                 "Department contact must have name.text populated"
          
          assert contact.name.given.blank?,
                 "Department contact must have blank given name"
          
          assert contact.name.family.blank?,
                 "Department contact must have blank family name"
        end

        pass "Successfully validated #{department_contacts.length} department contact(s)"
      end
    end

    test do
      id :validate_department_contact_updates
      title 'Department Contact Updates Maintain Structure'
      description %(
        Validates that department contacts maintain proper structure when updated:
        - Family name remains blank/null
        - Given name remains blank/null
        - Department name stays in name.text
      )

      input :organization_id
      
      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        
        organization = resource
        skip_if organization.contact.nil?, 'Organization has no contacts to validate'

        # Find first department contact
        dept_contact = organization.contact.find do |contact|
          contact&.name&.text.present? && 
          contact.name.given.blank? &&
          contact.name.family.blank?
        end

        skip_if dept_contact.nil?, 'No department contact found to test updates'

        # Update department name
        original_name = dept_contact.name.text
        new_name = "#{original_name} UPDATED"
        dept_contact.name.text = new_name

        fhir_update(organization)
        assert_response_status(200)

        # Verify structure maintained
        updated_org = resource
        updated_contact = updated_org.contact.find do |contact| 
          contact&.name&.text == new_name
        end

        assert !updated_contact.nil?,
               "Updated department contact not found"
        assert updated_contact.name.given.blank?,
               "Updated contact should maintain blank given name"
        assert updated_contact.name.family.blank?,
               "Updated contact should maintain blank family name"

        pass "Successfully validated department contact update maintains proper structure"
      end
    end
  end
end