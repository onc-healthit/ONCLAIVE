module Test5_claude
  class NetworkContactHandlingTest < Inferno::TestGroup
    id :network_contact_department_handling
    title 'Network Contact Handling for Departments'
    description %(
      Validates that department contacts in Organization resources are properly formatted
      with blank family/given names and department name in contact.name.text.
      
      Requirement: When the contact is a department name, rather than a human 
      (e.g., patient help line), include a blank family and given name, and 
      provide the department name in contact.name.text.
    )

    test do
      id :validate_department_contact
      title 'Department contact includes blank name components and text'
      description %(
        Verifies that department contacts in Organization resources have:
        * Blank family name
        * Blank given name
        * Department name properly populated in name.text
      )
      
      input :organization_id
      
      run do
        fhir_read(:organization, organization_id)
        
        assert_response_status(200)
        assert_resource_type(:organization)

        org = resource
        
        assert org.contact.present?, 'Organization must have contact information'
        
        department_contacts = org.contact.select do |contact|
          contact&.purpose&.coding&.any? do |coding|
            coding.code == 'DEPT'
          end
        end
        
        assert department_contacts.present?, 'No department contacts found in Organization'
        
        department_contacts.each do |contact|
          if contact.name
            # Verify blank family/given names
            assert contact.name.family.blank?, 
              "Department contact family name should be blank but was: #{contact.name.family}"
            
            assert contact.name.given.blank? || contact.name.given.empty?,
              "Department contact given name should be blank but was: #{contact.name.given}"
              
            # Verify text component exists and is populated
            assert contact.name.text.present?, 
              'Department contact name.text must contain the department name'
            
            assert contact.name.text.length > 0,
              'Department contact name.text cannot be empty'
          end
        end
      end
    end
  end
end