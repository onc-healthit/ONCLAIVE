module Test5_claude
  class OrganizationContactHandlingTest < Inferno::TestGroup
    id :organization_contact_department_handling
    title 'Organization Contact Handling for Departments'
    description %(
      Validates that when an Organization's contact is a department rather than a person,
      the contact is structured properly with:
      * Blank family and given names
      * Department name in contact.name.text
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :validate_department_contact_structure
      title 'Department contacts have proper name structure'
      description %(
        This test verifies that Organization resources with department contacts
        follow the implementation guidance for structuring contact names.
      )
      
      input :organization_id
      
      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        organization = resource

        skip_if organization.contact.nil?, 
          'Organization has no contacts to validate'

        organization.contact.each do |contact|
          next unless contact.name&.text.present? # Skip contacts without name text
          
          # For contacts with text (department names), verify name structure
          assert contact.name.family.nil?,
            "Contact with department name '#{contact.name.text}' should have blank family name"
          
          assert contact.name.given.nil? || contact.name.given.empty?,
            "Contact with department name '#{contact.name.text}' should have blank given name"
          
          assert contact.name.text.present?,
            'Department contact must have name.text populated'
        end

        pass "Organization's department contacts are properly structured"
      end
    end
  end
end