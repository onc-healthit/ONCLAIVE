module Test10Gpt
  class NetworkContactHandlingTestGroup < Inferno::TestGroup
    id :req_38_network_contact_handling
    title 'REQ-38: Network Contact Handling for Departments'
    description %(
      This test group verifies that when the contact is a department name, rather than a human
      (e.g., patient help line), the FHIR resource includes a blank family and given name, and
      provides the department name in contact.name.text.
    )

    input :organization_id, 
          title: 'Organization ID',
          description: 'The ID of the Organization resource to check for department contact handling.'

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
          contact.name&.text.present? && contact.name&.family.blank? && contact.name&.given.blank?
        end

        assert department_contact.present?, 'No department contact found with the expected structure.'

        pass 'Department contact handling is correctly implemented.'
      end
    end
  end
end