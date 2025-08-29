require 'fhir_models'
require 'fhir_client'

module Plannet
  # Test Group for REQ-05: Optional Must Support Elements Handling
  # Description: "Health Plan API SHALL NOT include Must Support data elements
  # in resource instances when information is not present and minimum cardinality is 0"
  class OptionalMustSupportHandlingGroup < Inferno::TestGroup
    id :plannet_req_05_optional_must_support_handling
    title 'REQ-05: Optional Must Support Elements Handling'
    description %(
      This test group verifies that the Health Plan API conforms to REQ-05.
      REQ-05 states: "Health Plan API SHALL NOT include Must Support data elements
      in resource instances when information is not present and minimum cardinality is 0".

      The test fetches instances of relevant Plan Net resource types and checks
      if any Must Support elements with a minimum cardinality of 0 are present
      in the resource with null values or as empty arrays. According to the requirement,
      these elements should be entirely absent if the information is not available.
    )

    # Define the resource types relevant to the Plan Net IG that might contain optional MS elements
    # This list should be adjusted based on the specific profiles and MS elements defined in the IG.
    PLANNET_RESOURCE_TYPES = [
      'Organization', 'OrganizationAffiliation', 'Location', 'HealthcareService',
      'Endpoint', 'Practitioner', 'PractitionerRole'
    ].freeze

    # This group assumes a FHIR client is configured, potentially in an ancestor group or the Test Suite.
    # Example configuration (if needed):
    # fhir_client do
    #   url :server_url # Input variable for the FHIR server URL
    #   bearer_token :access_token # Input variable for the bearer token, if required
    # end

    # -----------------------------------------------------------------------------
    # Test REQ-05-01: Check for absent optional Must Support elements
    # -----------------------------------------------------------------------------
    test do
      id :plannet_req_05_optional_must_support_test
      title 'Must Support elements with min cardinality 0 are absent when data is missing'
      description %(
        Verifies that resources returned by the API do not contain Must Support elements
        with a minimum cardinality of 0 if the element has no data (i.e., the element
        should be omitted, not present with a null value or empty array).
        It checks this by fetching resources and examining their structure against their
        declared profiles' Must Support requirements.
      )
      # This test assumes the necessary Implementation Guide resources (StructureDefinitions)
      # are available via `ig_resources` or a similar mechanism provided by the testing environment.
      # If not available, this test might need to be skipped or adapted.
      uses_request :search # Declares that this test performs FHIR search operations

      run do
        resources_checked_count = 0
        resources_failed_count = 0
        failed_instance_details = []

        # Check if IG resources are loaded, otherwise skip
        unless defined?(ig_resources) && ig_resources
           skip("Implementation Guide resources (StructureDefinitions) not loaded. Cannot determine Must Support elements.")
        end

        PLANNET_RESOURCE_TYPES.each do |resource_type|
          # Search for a small sample of resources of this type to check
          # Using _count=10 to limit the number of resources fetched per type
          fhir_search(resource_type, params: { _count: 10 })

          # Handle potential server errors or unsupported resource types
          if response[:status] == 400 || response[:status] == 404
             warning "Server returned #{response[:status]} for search on #{resource_type}. This resource type might not be supported or the search failed. Skipping checks for this type."
             next # Move to the next resource type
          end

          # Assert that the search was successful
          # Allow 201 only if the interaction could potentially be a create-on-search
          assert_response_status(200)

          # Get the bundle from the response
          bundle = resource
          unless bundle.is_a?(FHIR::Bundle)
            assert false, "Expected FHIR Bundle but received #{resource.class.name}"
          end

          # Skip checks for this type if no resources were returned
          unless bundle&.entry&.any?
            info "No #{resource_type} resources found on the server. Skipping checks for this type."
            next
          end

          # Extract resources from the bundle entries
          resources_in_bundle = bundle.entry.map { |e| e.resource }.compact

          resources_in_bundle.each do |instance|
            # Basic validation: Ensure it's a FHIR resource model instance
            unless instance.is_a?(FHIR::Model)
              warning "Found non-FHIR model instance in bundle for #{resource_type}. Skipping this entry."
              next
            end

            resources_checked_count += 1
            instance_id_info = "#{instance.resourceType}/#{instance.id}"
            instance_profiles = instance.meta&.profile

            # If a resource doesn't claim conformance to any profile, we cannot check MS elements
            unless instance_profiles&.any?
              info "Resource #{instance_id_info} does not declare conformance to any profiles. Skipping Must Support checks for this instance."
              next
            end

            instance_failed_checks = [] # Collect failures for this specific instance

            instance_profiles.each do |profile_url|
              # Attempt to find the profile definition using the loaded IG resources
              profile_definition = ig_resources.profile_by_url(profile_url)

              unless profile_definition
                # Log a warning if a declared profile cannot be found in the loaded IG
                warning "Could not find StructureDefinition for profile #{profile_url} referenced by #{instance_id_info}. Skipping Must Support checks for this profile."
                next
              end

              # Find Must Support elements with min cardinality 0 in this profile's snapshot view
              optional_must_support_elements = profile_definition.snapshot&.element&.select do |el|
                el.mustSupport == true && el.min == 0
              end || []

              # If no optional MS elements are defined for this profile, move to the next profile
              next if optional_must_support_elements.empty?

              optional_must_support_elements.each do |element_definition|
                # The path is typically like 'ResourceType.element.nestedElement'
                element_path = element_definition.path
                # Remove the ResourceType prefix to get the path within the resource instance
                path_parts = element_path.split('.').slice(1..-1)

                # Skip if the path is just the resource type itself (should not happen for elements)
                next if path_parts.empty?

                # Perform the check using the helper method
                check_result = check_element_absence(instance.source_hash, path_parts, instance_id_info, element_path)

                # If the check failed, record the failure message
                if check_result[:failed]
                  instance_failed_checks << check_result[:message]
                end
              end # End loop through optional MS elements
            end # End loop through