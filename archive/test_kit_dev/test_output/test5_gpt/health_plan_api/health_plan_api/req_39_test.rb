module Test5Gpt
  class OrganizationContactHandlingTestGroup < Inferno::TestGroup
    id :req_39_organization_contact_handling
    title 'Organization Contact Handling for Departments'
    description %(
      This test group verifies that when the contact is a department name, rather than a human,
      the Organization resource includes a blank family and given name, and provides the department
      name in contact.name.text as per REQ-39.
    )

    test do
      id :req_39_organization_contact_handling_test
      title 'Verify Organization contact handling for department names'
      description %(
        This test checks that the Organization resource correctly handles department contacts
        by ensuring that the family and given names are blank and the department name is present
        in contact.name.text.
      )
      input :organization_id, title: 'Organization ID', description: 'ID of the Organization resource to test'

      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        assert_resource_type(:organization)
        assert_valid_resource

        organization = resource
        assert organization.contact.present?, 'Organization contact is not present'
        
        department_contact = organization.contact.find do |contact|
          contact.name&.text.present? && contact.name&.family.blank? && contact.name&.given.blank?
        end

        assert department_contact.present?, 'No department contact found with the required structure'
        assert department_contact.name.text.present?, 'Department name is not present in contact.name.text'
      end
    end
  end
end