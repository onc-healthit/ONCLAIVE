module Test9Gpt
  class NetworkContactHandlingGroup < Inferno::TestGroup
    id :req_38_network_contact_handling
    title 'REQ-38: Network Contact Handling for Departments'
    description %(
      This test group verifies that when the contact is a department name, rather than a human,
      the FHIR resource includes a blank family and given name, and provides the department name
      in contact.name.text.
    )

    input :organization_id, 
          title: 'Organization ID',
          description: 'The ID of the organization resource to test against'

    fhir_client do
      url :server_url
    end

    test do
      id :req_38_network_contact_handling_test
      title 'Verify department contact handling in Organization resource'
      description %(
        This test checks that when the contact is a department name, the Organization resource
        includes a blank family and given name, and provides the department name in contact.name.text.
      )

      input :server_url

      run do
        fhir_read(:organization, organization_id)

        assert_response_status(200)
        assert_resource_type(:organization)

        department_contact = resource.contact.find do |contact|
          contact.name&.text.present? && 
          contact.name&.family.blank? && 
          contact.name&.given.blank?
        end

        assert department_contact.present?, 'No department contact found with the expected structure'

        assert department_contact.name.text.present?, 'Department name text is missing'
        assert department_contact.name.family.blank?, 'Family name should be blank for department contact'
        assert department_contact.name.given.blank?, 'Given name should be blank for department contact'
      end
    end
  end
end