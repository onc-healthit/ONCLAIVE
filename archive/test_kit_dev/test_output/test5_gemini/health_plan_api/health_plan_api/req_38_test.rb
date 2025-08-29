module Test5_gemini
  class NetworkContactHandlingTest < Inferno::TestGroup
    id :req_38_network_contact_handling
    title 'REQ-38: Network Contact Handling for Departments'
    description %(
      Verify that when the contact is a department name, the Organization resource
      includes a blank family and given name, and provides the department name in
      contact.name.text.
    )

    test do
      id :req_38_department_contact_format
      title 'Organization contact for department has correct format'
      description %(
        Read an Organization resource that represents a department and ensure
        the contact information is formatted correctly.
      )
      input :organization_id

      run do
        fhir_read(:organization, organization_id)

        assert_response_status(200)
        assert_resource_type(:organization)

        organization = resource

        department_contact = organization.contact.find do |contact|
          contact.purpose&.coding&.any? { |coding| coding.code == 'DEPT' }
        end

        skip_if department_contact.blank?, 'No contact with purpose "DEPT" found in the Organization resource.'

        assert department_contact.name&.text.present?, 'Department contact must have a name in contact.name.text.'
        assert department_contact.name&.family.blank?, 'Department contact must have a blank family name.'
        assert department_contact.name&.given.blank?, 'Department contact must have a blank given name.'
      end
    end
  end
end