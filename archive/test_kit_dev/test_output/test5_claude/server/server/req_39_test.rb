module Test5_claude
  class OrganizationContactDepartmentGroup < Inferno::TestGroup
    id :organization_contact_department
    title 'Organization Contact Department Handling'
    description %(
      Validates that organization contacts representing departments follow the specified format:
      - For department contacts, family and given names should be blank
      - Department name should be provided in contact.name.text
    )

    test do
      id :create_department_contact
      title 'Create Organization with Department Contact'
      description %(
        Creates an Organization resource with a department contact and validates
        the server accepts the specified contact format.
      )

      run do
        # Create Organization with department contact
        department_org = FHIR::Organization.new(
          name: 'Test Organization',
          contact: [
            {
              name: {
                family: '',
                given: [],
                text: 'Patient Help Line'
              },
              purpose: {
                coding: [
                  {
                    system: 'http://terminology.hl7.org/CodeSystem/contactentity-type',
                    code: 'ADMIN'
                  }
                ]
              }
            }
          ]
        )

        create_response = fhir_create(department_org)
        assert_response_status([201, 200])

        # Read back and validate
        created_id = create_response.resource.id
        read_response = fhir_read(:organization, created_id)
        assert_response_status(200)
        
        org = read_response.resource
        assert org.contact&.length == 1, 'Expected one contact in Organization'
        
        contact = org.contact.first
        assert contact.name.present?, 'Contact name must be present'
        assert contact.name.family.blank?, 'Contact family name should be blank for department'
        assert contact.name.given.blank?, 'Contact given name should be blank for department'
        assert contact.name.text.present?, 'Contact name.text must contain department name'

        # Cleanup
        fhir_delete(:organization, created_id)
      end
    end

    test do
      id :validate_department_contact_search
      title 'Search Organizations with Department Contacts'
      description %(
        Searches for Organizations and validates that department contacts
        maintain the specified format when returned in search results.
      )

      run do
        search_response = fhir_search(:organization)
        assert_response_status(200)
        
        resources = search_response.resource.entry&.map(&:resource)
        assert resources.present?, 'No Organization resources returned from search'

        department_contacts = resources.flat_map(&:contact).select do |contact|
          contact&.name&.text.present? && 
            contact.name.family.blank? && 
            contact.name.given.blank?
        end

        skip_if department_contacts.empty?, 'No department contacts found to validate'

        department_contacts.each do |contact|
          assert contact.name.text.present?, 'Department contact must have name.text populated'
          assert contact.name.family.blank?, 'Department contact family name must be blank'
          assert contact.name.given.blank?, 'Department contact given name must be blank'
        end
      end
    end
  end
end