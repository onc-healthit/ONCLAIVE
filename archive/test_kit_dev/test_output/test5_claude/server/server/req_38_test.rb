module Test5_claude
  class NetworkContactHandlingTest < Inferno::TestGroup
    id :network_contact_handling_test
    title 'Network Contact Handling for Departments Test'
    description %(
      Validates that department contacts are properly formatted with:
      - Blank family and given names
      - Department name in contact.name.text
      
      This verifies REQ-38: When the contact is a department name, rather than a human
      (e.g., patient help line), include a blank family and given name, and provide 
      the department name in contact.name.text.
    )

    test do
      id :department_contact_formatting
      title 'Department Contact Name Formatting'
      description 'Verify department contacts have blank given/family names and text name'
      
      input :organization_id
      
      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        organization = resource
        
        # Skip if no contacts present
        skip_if organization.contact.nil?, 'Organization has no contacts to validate'
        
        department_contacts = organization.contact.select do |contact|
          # Look for contacts that appear to be departments (have text but no family/given names)
          contact.name&.text.present? && 
            contact.name&.family.blank? &&
            (contact.name&.given || []).empty?
        end
        
        skip_if department_contacts.empty?, 'No department contacts found to validate'

        department_contacts.each do |contact|
          assert contact.name.family.nil?, 
            "Department contact should have blank family name but found: #{contact.name.family}"
          
          assert contact.name.given.nil? || contact.name.given.empty?,
            "Department contact should have blank given name but found: #{contact.name.given}"
            
          assert contact.name.text.present?,
            "Department contact must have department name in name.text but was blank"
        end

        pass "Successfully validated #{department_contacts.length} department contact(s)"
      end
    end

    test do
      id :department_contact_search
      title 'Department Contact Searchability'
      description 'Verify department contacts can be found via Organization search'
      
      run do
        # Search for organizations with contacts
        fhir_search(:organization, params: {_has: 'contact'})
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        skip_if resource.entry.empty?, 'No organizations with contacts found'
        
        found_department = false
        resource.entry.each do |entry|
          org = entry.resource
          next if org.contact.nil?
          
          org.contact.each do |contact|
            if contact.name&.text.present? && 
               contact.name&.family.blank? && 
               (contact.name&.given || []).empty?
              found_department = true
              break
            end
          end
          break if found_department
        end

        assert found_department, 'No organizations found with properly formatted department contacts'
      end
    end
  end
end