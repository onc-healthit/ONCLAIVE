module Test9_claude
  class NetworkContactDepartmentGroup < Inferno::TestGroup
    id :network_contact_department_handling
    title 'Network Contact Handling for Departments'
    description %(
      Verify that department contacts are properly represented in Organization resources.
      When a contact is a department name rather than a human (e.g., patient help line),
      the implementation must include a blank family and given name, and provide the 
      department name in contact.name.text.
    )

    fhir_client do
      url :url
      oauth_credentials :credentials 
    end

    test do
      id :department_contact_name_structure
      title 'Department contacts have proper name structure'
      description %(
        Verify that department contacts have:
        * Blank family name
        * Blank given name
        * Department name in name.text
      )

      input :organization_id,
            title: 'Organization ID',
            description: 'ID of an Organization resource that has department contacts',
            type: 'text'
            
      input :url,
            title: 'FHIR Server URL',
            description: 'Base URL for FHIR server'

      input :credentials,
            title: 'OAuth Credentials',
            type: :oauth_credentials,
            optional: true

      makes_request :organization_read

      run do
        fhir_read(:organization, organization_id, name: :organization_read)

        assert_response_status(200)
        assert_resource_type(:organization)

        department_contacts = resource.contact&.select do |contact|
          contact&.purpose&.coding&.any? do |coding|
            coding.code == 'DEPT' || 
            coding.display&.downcase&.include?('department')
          end
        end

        assert department_contacts.present?,
               'No department contacts found in Organization resource'

        department_contacts.each do |contact|
          assert contact.name.present?, 
                 "Department contact missing name element"
          
          assert contact.name.family.blank?,
                 "Department contact should have blank family name"
          
          assert contact.name.given.blank? || contact.name.given.empty?,
                 "Department contact should have blank given name"
          
          assert contact.name.text.present?,
                 "Department contact missing required text element containing department name"
                 
          warning do
            "Department name found in text: #{contact.name.text}"
          end
        end
      end
    end

    test do
      id :department_contact_validation
      title 'Department contacts pass FHIR validation'
      description %(
        Verify that Organization resources with department contacts
        pass basic FHIR validation requirements.
      )

      input :organization_id,
            title: 'Organization ID'
            
      input :url
      input :credentials,
            type: :oauth_credentials,
            optional: true

      uses_request :organization_read

      run do
        assert_valid_resource
      end
    end
  end
end