# frozen_string_literal: true

module Test5Gemini
  class Req39OrganizationContactHandlingForDepartmentsTest < Inferno::Test
    id :req_39_organization_contact_handling_for_departments
    title 'Organization contact handling for departments'
    description %(
      When the contact is a department name, rather than a human (e.g., patient help line),
      include a blank family and given name, and provide the department name in contact.name.text.
    )
    # TODO: Determine appropriate resource type for this test
    # input :resource_type
    # input :resource_id

    run do
      skip_if resource_id.blank?, 'No resource ID provided.'

      # TODO: Implement test logic based on provided resource type and ID
      # resource = fhir_read(resource_type, resource_id)
      # assert_response_status(200)
      # assert_resource_type(resource_type)

      # Example Assertion:
      # assert resource.contact.all? { |contact| contact.name&.text.present? ^ (contact.given.present? || contact.family.present?) },
      #        'Organization contact must have either a name or given/family but not both.'
    end
  end
end