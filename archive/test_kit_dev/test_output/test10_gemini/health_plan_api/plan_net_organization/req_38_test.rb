require_relative 'test10_gemini/req_38_department_contact_test'

module Test10_gemini
  class Req38DepartmentContactTestGroup < Inferno::TestGroup
    id :req_38_department_contact_group
    title 'REQ-38: Network Contact Handling for Departments'
    description %(
      This test group verifies the server's handling of network contacts that represent
      department names rather than human individuals, as specified in REQ-38.

      According to the guidance: "When the contact is a department name, rather than a human
      (e.g., patient help line), include a blank family and given name, and provide the
      department name in contact.name.text."

      This test will attempt to read an Organization resource identified by the provided
      `organization_id` input. It then iterates through the `contact` elements within
      the Organization. For any contact that has a `name` element with a `text` field
      (indicating a potential department name), it asserts that the `family` and `given`
      name parts are blank or absent, and that the `text` field is present.

      If the provided Organization resource does not contain any contacts with a `name.text`
      field, the test will be skipped as the condition for verification is not met.
    )

    input :url,
          title: 'FHIR Server Base URL',
          description: 'The base URL of the FHIR server being tested.',
          type: :text

    input :organization_id,
          title: 'Organization Resource ID with Department Contact',
          description: %(
            The ID of an Organization resource on the FHIR server that is expected to
            contain at least one `contact` entry representing a department name.
            This resource will be used to verify the structure of such contacts.
          ),
          type: :text

    input :credentials,
          title: 'OAuth Credentials',
          type: :oauth_credentials,
          optional: true

    fhir_client do
      url :url
      oauth_credentials :credentials
    end

    # This test is defined in a separate file for better organization
    # and referenced here by its ID.
    test from: :req_38_verify_department_contact_name
  end
end
```

```ruby
# req_38_department_contact_test.rb
module Test10_gemini
  class VerifyDepartmentContactNameTest < Inferno::Test
    id :req_38_verify_department_contact_name
    title 'Verify Department Name Contact Structure'
    description %(
      Verifies that when a contact represents a department name (e.g., patient help line),
      its `name` element includes blank `family` and `given` names, and the department
      name is provided in `contact.name.text`.

      This test reads the Organization resource specified by `organization_id`.
      It then checks all `contact` entries. If a `contact` has a `name` element
      and that `name` has a `text` field, it is considered a candidate for a
      department name contact. For such candidates, the test asserts that:
      - `contact.name.family` is blank or nil.
      - `contact.name.given` is blank or nil.
      - `contact.name.text` is present.

      If no contacts with a `name.text` field are found in the Organization,
      the test will be skipped.
    )

    # Inputs are inherited from the TestGroup, but explicitly listing them here
    # can improve readability for the individual test's context.
    # However, Inferno's DSL automatically makes group inputs available.
    # As per guidance "Ensure each test explicitly declares all inputs it uses",
    # organization_id is explicitly declared here as it is directly used.
    input :organization_id,
          title: 'Organization Resource ID with Department Contact',
          description: %(
            The ID of an Organization resource on the FHIR server that is expected to
            contain at least one `contact` entry representing a department name.
            This resource will be used to verify the structure of such contacts.
          ),
          type: :text

    run do
      # 1. Make appropriate FHIR API calls: Read the Organization resource
      fhir_read(:organization, organization_id)

      # Handle success and error cases appropriately: Assert response status
      assert_response_status(200)
      assert_resource_type(:organization)

      organization = resource
      department_contacts_found = false

      # 2. Implement the test logic described in the specification
      # 3. Implement test for all components outlined in the test specification
      organization.contact&.each_with_index do |contact, index|
        if contact.name.present? && contact.name.text.present?
          department_contacts_found = true
          # This contact is a candidate for a department name contact.
          # Now, verify its structure according to REQ-38.

          # Assert blank family name
          assert contact.name.family.blank?,
                 "Expected Organization.contact[#{index}].name.family to be blank for department contact, but found '#{contact.name.family}'."

          # Assert blank given name
          assert contact.name.given.blank?,
                 "Expected Organization.contact[#{index}].name.given to be blank for department contact, but found '#{contact.name.given}'."

          # Assert department name in text is present (already checked in if condition, but re-assert for clarity)
          assert contact.name.text.present?,
                 "Expected Organization.contact[#{index}].name.text to be present for department contact, but it was blank."

          info "Successfully verified department contact at Organization.contact[#{index}]: text='#{contact.name.text}', family='#{contact.name.family}', given='#{contact.name.given}'."
        end
      end

      # If no contacts with a name.text were found, skip the test.
      # This means the provided resource did not contain the necessary data
      # to verify the requirement.
      skip_if !department_contacts_found,
              "No Organization.contact entries with a 'name.text' field were found in Organization/#{organization_id}. " \
              "This test requires an Organization resource that contains at least one contact representing a department name " \
              "to verify REQ-38."

      pass 'All identified department name contacts conform to REQ-38.'
    end
  end
end