require_relative '../../../service_base_url_inputs'

module Test9Gemini
  class Req36OrganizationSearchBySpecialtyGroup < Inferno::TestGroup
    id :req_36_org_search_by_specialty
    title 'REQ-36: Organization Search by Specialty'
    description %(
      **Description**: "The Plan-Net design is based around the following types of searches:
      Organization by specialty - Example: Compounding Pharmacy
      - Focal Resource and Field: OrganizationAffiliation.specialty
      - Qualifications of Search: Location, network, name."

      This test group verifies the Health Plan API's capability to search for
      OrganizationAffiliation resources by specialty, with optional qualifications
      for location, network, and organization name.
    )

    input_order :url,
                :specialty_code,
                :specialty_system,
                :location_id,
                :network_id,
                :organization_name

    # Include the common inputs for service base URL
    include ServiceBaseURLInputs

    input :specialty_code,
          title: 'Specialty Code',
          description: 'The code for the specialty to search for (e.g., "compoundingpharm"). This input is required.',
          default: 'compoundingpharm'

    input :specialty_system,
          title: 'Specialty System (Optional)',
          description: 'The URI for the CodeSystem of the specialty code (e.g., "http://terminology.hl7.org/CodeSystem/organization-type").',
          optional: true

    input :location_id,
          title: 'Location ID (Optional)',
          description: 'ID of a Location resource to filter OrganizationAffiliations (e.g., "Location/example-location-id").',
          optional: true

    input :network_id,
          title: 'Network ID (Optional)',
          description: 'ID of an Organization resource representing the network to filter OrganizationAffiliations (e.g., "Organization/example-network-id").',
          optional: true

    input :organization_name,
          title: 'Primary Organization Name (Optional)',
          description: 'Name of the primary organization (OrganizationAffiliation.organization) to filter results (e.g., "Good Health Clinic").',
          optional: true

    fhir_client do
      url :url
    end

    test do
      id :req_36_org_aff_specialty_search
      title 'Search OrganizationAffiliation by specialty with optional qualifiers'
      description %(
        This test searches for OrganizationAffiliation resources based on the `specialty`
        parameter. It also includes `location`, `network`, and `primary-organization.name`
        as search qualifiers if their respective input values are provided.

        The test verifies that the server responds successfully (HTTP 200 OK) to such
        queries and returns a Bundle resource. If any OrganizationAffiliation resources
        are returned, the test checks if they match the specified `specialty`. If
        `location` or `network` qualifiers were used, it also checks if the returned
        resources reference the correct location or network. Direct validation of
        `primary-organization.name` within the returned resources is not performed due
        to the complexity of resolving referenced resources, but the server is expected
        to have applied this filter if the parameter was provided.
      )
      makes_request :organization_affiliation_search_by_specialty

      run do
        assert specialty_code.present?, "Specialty Code input must be provided."

        search_params = {}

        # Construct specialty parameter
        if specialty_system.present?
          search_params[:specialty] = "#{specialty_system}|#{specialty_code}"
        else
          search_params[:specialty] = specialty_code
        end

        # Add optional qualifiers
        search_params[:location] = location_id if location_id.present?
        search_params[:network] = network_id if network_id.present?
        search_params['primary-organization.name'] = organization_name if organization_name.present?

        fhir_search(:organization_affiliation, params: search_params, name: :organization_affiliation_search_by_specialty)

        assert_response_status(200)
        assert_resource_type(:bundle)

        if resource.present? && resource.entry.present?
          resource.entry.each do |entry|
            assert entry.resource.resourceType == 'OrganizationAffiliation',
                   "Expected resource type OrganizationAffiliation, but found #{entry.resource.resourceType}"

            # Validate specialty
            specialty_match_found = entry.resource.specialty&.any? do |spec|
              spec.coding&.any? do |coding|
                coding.code == specialty_code &&
                (specialty_system.blank? || coding.system == specialty_system)
              end
            end
            assert specialty_match_found,
                   "Returned OrganizationAffiliation #{entry.resource.id} does not match specialty code '#{specialty_code}'" \
                   "#{specialty_system.present? ? " and system '#{specialty_system}'" : ''}."

            # Validate location if provided
            if location_id.present?
              location_reference_found = entry.resource.location&.any? do |loc_ref|
                loc_ref.reference.include?(location_id)
              end
              assert location_reference_found,
                     "Returned OrganizationAffiliation #{entry.resource.id} does not reference location ID '#{location_id}' when 'location' parameter was used."
            end

            # Validate network if provided
            if network_id.present?
              network_reference_found = entry.resource.network&.any? do |net_ref|
                net_ref.reference.include?(network_id)
              end
              assert network_reference_found,
                     "Returned OrganizationAffiliation #{entry.resource.id} does not reference network ID '#{network_id}' when 'network' parameter was used."
            end
          end
        else
          info "No OrganizationAffiliation resources found for the given search criteria. This is a valid response if no data matches."
        end

        if organization_name.present?
          info "Search included 'primary-organization.name=#{organization_name}'. Direct validation of the organization name within returned resources is not performed by this test. The server is expected to have filtered based on this parameter."
        end

        pass "Successfully performed OrganizationAffiliation search with specialty '#{search_params[:specialty]}' and other provided qualifiers."
      end
    end
  end
end