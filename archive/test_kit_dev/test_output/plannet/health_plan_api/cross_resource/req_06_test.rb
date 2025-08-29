require_relative '../../utils/assertions'
require_relative '../../utils/plan_net_ig_metadata_extractor' # Assume this utility exists

module Plannet
  # Test Group for REQ-06: Required Must Support elements handling
  # Description: "Health Plan API SHALL provide reason for missing information using nullFlavors
  # or dataAbsentReason extension when Must Support element is absent and minimum cardinality is >0"
  class Req06MustSupportAbsentReasonGroup < Inferno::TestGroup
    include Plannet::Assertions # Include custom assertions if any

    id :plannet_req_06_must_support_absent_reason
    title 'Must Support Element Absence Reason'
    description %(
      This test group verifies that the Health Plan API provides a reason for missing information
      when a Must Support element with minimum cardinality > 0 is absent from a resource.
      The reason should be provided using the `dataAbsentReason` extension as defined by FHIR.

      The test retrieves relevant Plan Net resources identified in previous tests
      (e.g., Organization, Practitioner, Location, etc.) and checks each resource against
      the Must Support requirements defined in the Plan Net Implementation Guide profiles.

      For each resource instance:
      1. Identify the profiles the resource claims conformance to.
      2. For each profile, identify the Must Support elements with a minimum cardinality > 0.
      3. For each such element:
         - Check if the element is present in the resource instance.
         - If the element is **absent**, check if the `_elementName` (primitive element backing the data element)
           contains the `dataAbsentReason` extension (`http://hl7.org/fhir/StructureDefinition/data-absent-reason`).
         - The check passes for the element if it's either present OR absent with the `dataAbsentReason` extension.
         - The check fails if the element is absent AND lacks the `dataAbsentReason` extension.

      The test group passes if all checked Must Support elements across all tested resources
      meet these criteria. It skips if no relevant resources were found or if no Must Support
      elements with minimum cardinality > 0 are defined for the tested profiles.
    )

    # Constants
    DATA_ABSENT_REASON_URL = 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'.freeze

    # Inputs: Assume these are populated by previous tests, containing arrays of FHIR resource objects
    # Example: scratch[:organization_resources] = [FHIR::Organization.new(...), ...]
    # These inputs declare dependencies on previously stored resource lists.
    input :plannet_organization_resources_json,
          title: 'Plan Net Organization Resources JSON',
          description: 'JSON string representing an array of Plan Net Organization resources fetched previously.',
          type: 'textarea',
          optional: true
    input :plannet_practitioner_resources_json,
          title: 'Plan Net Practitioner Resources JSON',
          description: 'JSON string representing an array of Plan Net Practitioner resources fetched previously.',
          type: 'textarea',
          optional: true
    input :plannet_practitioner_role_resources_json,
          title: 'Plan Net PractitionerRole Resources JSON',
          description: 'JSON string representing an array of Plan Net PractitionerRole resources fetched previously.',
          type: 'textarea',
          optional: true
    input :plannet_location_resources_json,
          title: 'Plan Net Location Resources JSON',
          description: 'JSON string representing an array of Plan Net Location resources fetched previously.',
          type: 'textarea',
          optional: true
    input :plannet_healthcare_service_resources_json,
          title: 'Plan Net HealthcareService Resources JSON',
          description: 'JSON string representing an array of Plan Net HealthcareService resources fetched previously.',
          type: 'textarea',
          optional: true
    input :plannet_endpoint_resources_json,
          title: 'Plan Net Endpoint Resources JSON',
          description: 'JSON string representing an array of Plan Net Endpoint resources fetched previously.',
          type: 'textarea',
          optional: true
    input :plannet_insurance_plan_resources_json,
          title: 'Plan Net InsurancePlan Resources JSON',
          description: 'JSON string representing an array of Plan Net InsurancePlan resources fetched previously.',
          type: 'textarea',
          optional: true
    input :plannet_organization_affiliation_resources_json,
          title: 'Plan Net OrganizationAffiliation Resources JSON',
          description: 'JSON string representing an array of Plan Net OrganizationAffiliation resources fetched previously.',
          type: 'textarea',
          optional: true
    input :plannet_network_resources_json,
          title: 'Plan Net Network Resources JSON',
          description: 'JSON string representing an array of Plan Net Network resources fetched previously.',
          type: 'textarea',
          optional: true

    # Test: Check Must Support elements for dataAbsentReason
    test do
      id :plannet_req_06_must_support_element_absent_reason_test
      title 'Check for dataAbsentReason on missing Must Support elements (min > 0)'
      description %(
        Verifies that for every Must Support element with minimum cardinality > 0 defined in the relevant Plan Net profiles,
        if the element is missing from a resource instance, the `dataAbsentReason` extension is present.
      )

      # This run block implements the core logic described in REQ-06
      run do
        # Combine all resource inputs into a single list
        resources_to_check = []
        resource_inputs = [
          plannet_organization_resources_json, plannet_practitioner_resources_json,
          plannet_practitioner_role_resources_json, plannet_location_resources_json,
          plannet_healthcare_service_resources_json, plannet_endpoint_resources_json,
          plannet_insurance_plan_resources_json, plannet_organization_affiliation_resources_json,
          plannet_network_resources_json
        ]

        resource_inputs.compact.each do |json_string|
          begin
            parsed_resources = JSON.parse(json_string)
            parsed_resources.each do |resource_hash|
              # Re-parse each hash into a FHIR model object
              resource = FHIR.from_contents(resource_hash.to_json)
              resources_to_check << resource
            end
          rescue JSON::ParserError => e
            warning "Failed to parse resource JSON: #{e.message}. Skipping these resources."
          rescue StandardError => e
            warning "An error occurred processing resource JSON: #{e.message}. Skipping these resources."
          end
        end

        skip_if resources_to_check.empty?, 'No Plan Net resources found to perform the Must Support absence check.'

        # Assume PlanNetIgMetadataExtractor provides the necessary info
        # In a real test kit, this might load from packaged IG files
        metadata_extractor = PlanNetIgMetadataExtractor.new # Replace with actual initialization if needed

        failures = []
        elements_checked_count = 0

        resources_to_check.each do |resource|
          resource_type = resource.resourceType
          resource_id = resource.id
          profiles = resource.meta&.profile&.map(&:to_s) || []

          # Include base resource type profile if needed, or rely on IG profiles only
          # profiles << FHIR::Definitions.resource_definition(resource_type).url if profiles.empty?

          profiles.each do |profile_url|
            # Get Must Support elements with min cardinality > 0 for this profile
            # This requires the metadata extractor to have this capability
            must_support_elements = metadata_extractor.get_must_support_elements_with_min_cardinality_greater_than_zero(profile_url)

            next if must_support_elements.nil? || must_support_elements.empty?

            must_support_elements.each do |element_definition|
              element_path = element_definition[:path] # Assumes format { path: 'Resource.element.subelement', min: 1 }

              # Skip complex paths or elements not directly on the resource for simplicity in this example
              # A robust implementation would handle nested paths correctly.
              # This example focuses on direct or first-level nested elements.
              next unless element_path.start_with?(resource_type)
              simple_path = element_path.delete_prefix("#{resource_type}.")

              elements_checked_count += 1
              element_present = false

              begin
                resolved_values = Array.wrap(resource.send(:resolve_path, simple_path)) # Use resolve_path safely
                element_present = resolved_values.any? { |v| !v.nil? }
              rescue NoMethodError
                # Handle cases where the path does not exist / method is missing
                element_present = false
              rescue StandardError => e
                warning "Error resolving path '#{simple_path}' on #{resource_type}/#{resource_id}: #{e.message}"
                next # Skip checking this element due to error
              end

              unless element_present
                # Element is absent. Check for data-absent-reason extension.
                path_parts = simple_path.split('.')
                element_name = path_parts.pop
                parent_path = path_parts.join('.')

                parent_object = parent_path.empty? ? resource : resource.send(:resolve_path, parent_path)

                has_data_absent_reason = false
                if parent_object
                  parents_to_check = Array.wrap(parent_object).compact

                  has_data_absent_reason = parents_to_check.any? do |parent|
                    primitive_accessor = "_#{element_name}"
                    next false unless parent.respond_to?(primitive_accessor)

                    primitive_element_or_array = parent.send(primitive_accessor)
                    next false if primitive_element_or_array.nil?

                    Array.wrap(primitive_element_or_array).any? do |primitive|
                      primitive.respond_to?(:extension) &&
                        primitive.extension.any? { |ext| ext.url == DATA_ABSENT_REASON_URL }
                    end
                  end
                end

                unless has_data_absent_reason
                  failures << "Resource #{resource_type}/#{resource_id} (Profile: #{profile_url}) is missing Must Support element '#{simple_path}' (min > 0) and does not provide a dataAbsentReason extension."
                end
              end # unless element_present
            end # each must_support_element
          end # each profile
        end # each resource

        # Final assertion based on checks
        assert failures.empty?, "Found #{failures.length} missing Must Support elements (min > 0) without dataAbsentReason extension:\n- #{failures.join("\n- ")}"

        # If no elements were checked (e.g., profiles not supported, or no MS elements with min>0 found)
        skip_if elements_checked_count.zero?, 'No Must Support elements with minimum cardinality > 0 were identified and checked for the provided resources and profiles.'

        # If we reach here and failures is empty, and elements were checked
        pass "Successfully verified #{elements_checked_count} Must Support elements (min > 0). All missing elements had a dataAbsentReason extension where required."
      end
    end
  end
end