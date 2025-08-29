module Test5Gpt
  class NetworkContactHandlingTestGroup < Inferno::TestGroup
    id :req_38_network_contact_handling
    title 'Network Contact Handling for Departments'
    description %(
      This test group verifies that when the contact is a department name,
      rather than a human (e.g., patient help line), the FHIR resource
      includes a blank family and given name, and provides the department
      name in contact.name.text.
    )

    test do
      id :req_38_department_contact_name_test
      title 'Department Contact Name Handling'
      description %(
        Verify that the contact resource correctly handles department names
        by ensuring the family and given names are blank and the department
        name is present in contact.name.text.
      )
      input :organization_id, title: 'Organization ID', description: 'The ID of the Organization resource to test'

      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        assert_resource_type(:organization)
        assert_valid_resource

        organization = resource

        skip_if organization.contact.blank?, 'No contact information available in the Organization resource.'

        department_contact = organization.contact.find do |contact|
          contact.name&.text.present? && contact.name&.family.blank? && contact.name&.given.blank?
        end

        assert department_contact.present?, 'No department contact found with a blank family and given name, and a department name in contact.name.text.'

        pass 'Department contact is correctly handled with a blank family and given name, and department name in contact.name.text.'
      end
    end
  end
end