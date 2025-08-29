module Test10_gemini
  class Req35ProviderSearchBySpecialtyGroup < Inferno::TestGroup
    id :req_35_provider_search_by_specialty_group
    title 'REQ-35: Provider search by specialty'
    description %(
      This test group verifies the server's ability to search for PractitionerRole resources
      based on specialty and various qualifying parameters as described in REQ-35.

      The Plan-Net design requires searches for providers by specialty, with qualifications
      including location, network (organization), and practitioner name.
      The focal resource and field for specialty is PractitionerRole.specialty.
    )

    # Inputs for the tests within this group
    # These inputs are declared at the group level, making them available to all
    # tests within this group and its subgroups.
    input :url,
          title: 'FHIR Server Base URL',
          description: 'The base URL for the FHIR server being tested.',
          type: :text

    input :specialty_code,
          title: 'Specialty Code (e.g., SNOMED CT for Cardiologist)',
          description: 'A SNOMED CT code representing a specialty (e.g., 408443003 for Cardiologist). ' \
                       'Ensure this code exists for PractitionerRoles on the server.',
          type: :text,
          default: '408443003' # Example: SNOMED CT for Cardiologist

    input :known_location_id,
          title: 'Known Location ID',
          description: 'The ID of a Location resource that a PractitionerRole is associated with. ' \
                       'This is used for searching by specialty and location.',
          type: :text,
          optional: true # Mark as optional if not all servers support this combination or data is scarce
          # default: 'example-location-id' # Uncomment and set a default if you have a specific test location

    input :known_organization_id,
          title: 'Known Organization ID (Network)',
          description: 'The ID of an Organization resource that a PractitionerRole is associated with (representing a network). ' \
                       'This is used for searching by specialty and network.',
          type: :text,
          optional: true # Mark as optional
          # default: 'example-organization-id' # Uncomment and set a default

    input :known_practitioner_name,
          title: 'Known Practitioner Name',
          description: 'The full name or part of the name of a Practitioner associated with a PractitionerRole. ' \
                       'This is used for searching by specialty and practitioner name.',
          type: :text,
          optional: true # Mark as optional
          # default: 'John Doe' # Uncomment and set a default

    # Configure the FHIR client for this group
    fhir_client do
      url :url
      # If authentication is needed, add oauth_credentials here, e.g.:
      # oauth_credentials :credentials
    end

    test do
      id :req_35_search_by_specialty
      title 'Search PractitionerRole by Specialty'
      description %(
        Verifies that the server can successfully search for PractitionerRole resources
        using the `specialty` search parameter.
        The test performs a FHIR search on the `PractitionerRole` endpoint with a
        provided `specialty_code`.
        It asserts a 200 OK response, a Bundle resource type, and that the bundle
        contains at least one entry.
      )
      # Explicitly declare inputs used by this test
      input :specialty_code

      run do
        # Perform the FHIR search for PractitionerRole by specialty
        fhir_search(:practitioner_role, params: { specialty: specialty_code })

        # Assertions for a successful search
        assert_response_status(200)
        assert_resource_type(:bundle)

        # Assert that the bundle contains at least one entry
        assert resource.entry.present?,
               "No PractitionerRole resources found for specialty code: '#{specialty_code}'. " \
               "Ensure test data exists for this specialty, or provide a valid specialty code."

        # Optional: Further validation that returned resources actually match the specialty
        # This would involve iterating through the bundle entries and checking each PractitionerRole's specialty.
        # For simplicity and adherence to the core spec, we'll keep it at presence check.
      end
    end

    test do
      id :req_35_search_by_specialty_and_location
      title 'Search PractitionerRole by Specialty and Location'
      description %(
        Verifies that the server can successfully search for PractitionerRole resources
        using the `specialty` and `location` search parameters.
        The test performs a FHIR search on the `PractitionerRole` endpoint with a
        provided `specialty_code` and `known_location_id`.
        It asserts a 200 OK response, a Bundle resource type, and that the bundle
        contains at least one entry.
      )
      # Explicitly declare inputs used by this test
      input :specialty_code, :known_location_id

      run do
        skip_if known_location_id.blank?, 'No known_location_id provided, skipping test for specialty and location search.'

        # Perform the FHIR search for PractitionerRole by specialty and location
        fhir_search(:practitioner_role, params: { specialty: specialty_code, location: known_location_id })

        # Assertions for a successful search
        assert_response_status(200)
        assert_resource_type(:bundle)

        # Assert that the bundle contains at least one entry
        assert resource.entry.present?,
               "No PractitionerRole resources found for specialty '#{specialty_code}' and location '#{known_location_id}'. " \
               "Ensure test data exists for this combination."
      end
    end

    test do
      id :req_35_search_by_specialty_and_network
      title 'Search PractitionerRole by Specialty and Network (Organization)'
      description %(
        Verifies that the server can successfully search for PractitionerRole resources
        using the `specialty` and `organization` search parameters (representing a network).
        The test performs a FHIR search on the `PractitionerRole` endpoint with a
        provided `specialty_code` and `known_organization_id`.
        It asserts a 200 OK response, a Bundle resource type, and that the bundle
        contains at least one entry.
      )
      # Explicitly declare inputs used by this test
      input :specialty_code, :known_organization_id

      run do
        skip_if known_organization_id.blank?, 'No known_organization_id provided, skipping test for specialty and network search.'

        # Perform the FHIR search for PractitionerRole by specialty and organization
        fhir_search(:practitioner_role, params: { specialty: specialty_code, organization: known_organization_id })

        # Assertions for a successful search
        assert_response_status(200)
        assert_resource_type(:bundle)

        # Assert that the bundle contains at least one entry
        assert resource.entry.present?,
               "No PractitionerRole resources found for specialty '#{specialty_code}' and organization '#{known_organization_id}'. " \
               "Ensure test data exists for this combination."
      end
    end

    test do
      id :req_35_search_by_specialty_and_practitioner_name
      title 'Search PractitionerRole by Specialty and Practitioner Name'
      description %(
        Verifies that the server can successfully search for PractitionerRole resources
        using the `specialty` and chained `practitioner.name` search parameters.
        The test performs a FHIR search on the `PractitionerRole` endpoint with a
        provided `specialty_code` and `known_practitioner_name`.
        It asserts a 200 OK response, a Bundle resource type, and that the bundle
        contains at least one entry.
      )
      # Explicitly declare inputs used by this test
      input :specialty_code, :known_practitioner_name

      run do
        skip_if known_practitioner_name.blank?, 'No known_practitioner_name provided, skipping test for specialty and practitioner name search.'

        # Perform the FHIR search for PractitionerRole by specialty and practitioner.name
        # Note the chained parameter syntax: 'practitioner.name'
        fhir_search(:practitioner_role, params: { specialty: specialty_code, 'practitioner.name': known_practitioner_name })

        # Assertions for a successful search
        assert_response_status(200)
        assert_resource_type(:bundle)

        # Assert that the bundle contains at least one entry
        assert resource.entry.present?,
               "No PractitionerRole resources found for specialty '#{specialty_code}' and practitioner name '#{known_practitioner_name}'. " \
               "Ensure test data exists for this combination."
      end
    end
  end
end