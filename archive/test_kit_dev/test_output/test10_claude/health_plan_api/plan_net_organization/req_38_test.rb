module Test10_claude
  class NetworkContactHandlingGroup < Inferno::TestGroup
    id :network_contact_handling_test
    title 'Network Contact Handling for Departments'
    description %(
      When a contact is a department name rather than a human (e.g., patient help line),
      the contact.name.text field should contain the department name while family and 
      given name elements should be blank.
    )

    fhir_client do
      url :url
      oauth_credentials :credentials
    end

    test do
      id :department_contact_name_test
      title 'Department contacts have appropriate name formatting'
      description %(
        This test verifies that department contacts:
        1. Have blank family and given names
        2. Include the department name in contact.name.text
      )

      input :url,
            title: 'FHIR Server URL',
            description: 'Base URL of FHIR server'
            
      input :credentials,
            title: 'OAuth Credentials',
            type: :oauth_credentials,
            optional: true

      input :org_id,
            title: 'Organization ID',
            description: 'ID of organization to test'
      
      run do
        fhir_read(:organization, org_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        dept_contacts = resource.contact&.select do |contact|
          contact.name&.text.present? && 
          contact.name.text.match?(/department|unit|division|service/i)
        end

        skip_if dept_contacts.blank?, 'No department contacts found to validate'

        dept_contacts.each do |contact|
          assert contact.name.family.blank?, 
            "Department contact '#{contact.name.text}' should have blank family name"
          
          assert contact.name.given.blank? || contact.name.given.empty?,
            "Department contact '#{contact.name.text}' should have blank given name"
          
          assert contact.name.text.present?,
            "Department contact must have name.text containing department name"
        end

        pass "Department contacts correctly formatted with blank names and text description"
      end
    end

    test do
      id :human_contact_name_test 
      title 'Human contacts have appropriate name formatting'
      description %(
        This test verifies that human contacts have proper name formatting
        with populated family/given names, as a comparison to department contacts
      )

      input :url
      input :credentials, 
            type: :oauth_credentials,
            optional: true
      input :org_id
      
      run do
        fhir_read(:organization, org_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        human_contacts = resource.contact&.reject do |contact|
          contact.name&.text&.match?(/department|unit|division|service/i)
        end

        skip_if human_contacts.blank?, 'No human contacts found to validate'

        human_contacts.each do |contact|
          assert contact.name.family.present? || contact.name.given.present?,
            "Human contact should have either family or given name populated"
        end

        pass "Human contacts correctly formatted with populated name components"
      end
    end
  end
end