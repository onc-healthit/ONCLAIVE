module Test9_gemini
  class Req35ProviderSpecialtySearchGroup < Inferno::TestGroup
    id :req_35_provider_specialty_search_group
    title 'REQ-35: Provider search by specialty'
    description %(
      This test group implements REQ-35: Provider search by specialty.
      It verifies that the Health Plan API can search for PractitionerRole
      resources based on their specialty. The focal resource and field is
      PractitionerRole.specialty. The search can be further qualified by
      location, network, and practitioner name as per the design requirement.
    )

    test do
      id :req_35_practitioner_role_search_by_specialty_and_qualifiers
      title 'Search PractitionerRole by specialty with optional qualifiers'
      description %(
        This test performs a search for PractitionerRole resources using the `specialty`
        search parameter. It allows for optional qualification of the search by
        `location` (PractitionerRole.location), `network` (PractitionerRole.network),
        and `practitioner.name` (name of the Practitioner referenced by PractitionerRole.practitioner).

        The test asserts that the server returns a 200 OK status and a FHIR Bundle.
        If the Bundle contains entries, each entry must:
        1. Be a PractitionerRole resource.
        2. Be a valid FHIR resource.
        3. Have a `specialty` that matches the searched specialty code and system (if provided).
      )

      input :search_specialty_code,
            title: 'Specialty Code',
            description: 'The code for the specialty to search for (e.g., "394579002" for Cardiologist).',
            default: '394579002' # SNOMED CT code for Cardiologist

      input :search_specialty_system,
            title: 'Specialty System (Optional)',
            description: 'The system for the specialty code (e.g., "http://snomed.info/sct").',
            optional: true,
            default: 'http://snomed.info/sct'

      input :search_location_reference,
            title: 'Location Reference (Optional)',
            description: 'Reference to a Location to qualify the search (e.g., "Location/123"). This will be used with the "location" search parameter.',
            optional: true

      input :search_network_reference,
            title: 'Network Reference (Optional)',
            description: 'Reference to an Organization representing a network to qualify the search (e.g., "Organization/abc"). This will be used with the "network" search parameter. Note: "network" is not a standard FHIR search parameter for PractitionerRole and implies Plan-Net specific support.',
            optional: true

      input :search_practitioner_name,
            title: 'Practitioner Name (Optional)',
            description: 'Name of the practitioner to qualify the search (e.g., "Smith"). This will be used with the "practitioner.name" chained search parameter.',
            optional: true

      makes_request :practitioner_role_specialty_search

      run do
        assert search_specialty_code.present?, "Input `search_specialty_code` must be provided."

        search_params = {}

        specialty_param_value =
          if search_specialty_system.present?
            "#{search_specialty_system}|#{search_specialty_code}"
          else
            search_specialty_code
          end
        search_params[:specialty] = specialty_param_value

        search_params[:location] = search_location_reference if search_location_reference.present?
        search_params[:network] = search_network_reference if search_network_reference.present?
        search_params['practitioner.name'] = search_practitioner_name if search_practitioner_name.present?

        fhir_search(:practitioner_role, params: search_params, name: :practitioner_role_specialty_search)

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource

        if bundle.entry.present?
          info "Found #{bundle.entry.length} PractitionerRole(s) matching the search criteria."
          bundle.entry.each_with_index do |entry, index|
            entry_resource = entry.resource
            assert entry_resource.is_a?(FHIR::PractitionerRole),
                   "Bundle entry ##{index + 1} is not a PractitionerRole. Found: #{entry_resource.resourceType}"

            # Validate against base FHIR. If a Plan-Net profile URL for PractitionerRole is known,
            # it could be specified here using:
            # assert_valid_resource(resource: entry_resource, profile_url: 'PLAN_NET_PRACTITIONERROLE_PROFILE_URL')
            assert_valid_resource(resource: entry_resource)

            specialty_match_found = entry_resource.specialty&.any? do |specialty_concept|
              specialty_concept.coding&.any? do |coding|
                coding.code == search_specialty_code &&
                (search_specialty_system.blank? || coding.system == search_specialty_system)
              end
            end

            found_specialties_display = entry_resource.specialty&.map do |sp|
              sp.coding&.map { |c| "#{c.system}|#{c.code}" }&.join('; ') || sp.text
            end&.join(', ') || "none"

            assert specialty_match_found,
                   "PractitionerRole/#{entry_resource.id || "(no id)"} (Bundle entry ##{index + 1}) does not have the searched specialty. " +
                   "Searched for: Code=#{search_specialty_code}, System=#{search_specialty_system.presence || 'any'}. " +
                   "Found specialties: [#{found_specialties_display}]."
          end
        else
          info "No PractitionerRole resources found matching the search criteria. This may be an acceptable outcome depending on the server's data."
        end
      end
    end
  end
end