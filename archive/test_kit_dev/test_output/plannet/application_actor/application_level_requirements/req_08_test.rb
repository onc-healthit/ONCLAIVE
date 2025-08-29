# frozen_string_literal: true

require_relative './req_08_must_support_display_test'

module Plannet
  # Test Group for REQ-08: Must Support Element Handling by Application Actor
  #
  # This group contains tests related to the requirement that an Application Actor
  # SHOULD display Must Support data elements for human use or store them for other purposes.
  # Due to the nature of testing application display and internal storage, this
  # relies on manual user attestation.
  class PlannetMustSupportDisplayGroup < Inferno::TestGroup
    id :plannet_req_08_must_support_display_group
    title 'REQ-08: Must Support Element Handling'
    description %(
      **Requirement REQ-08:** Application Actor SHOULD display Must Support data elements for human use or store for other purposes.

      **Actor:** Application Actor
      **Conformance:** SHOULD

      This set of tests verifies whether the application under test appropriately handles
      elements marked as 'Must Support' in the relevant Plan-Net Implementation Guide profiles.
      Handling includes displaying the element for human use or storing it for other purposes.

      **Note:** Verification of application display or internal storage logic typically
      requires manual confirmation from the user running the test suite.
    )

    # Mark the entire group as optional since it tests a SHOULD requirement and involves manual steps.
    optional

    run_as_group

    # Include the specific test implementation for REQ-08
    test from: :req_08_must_support_display_test
  end
end
```

```ruby
# frozen_string_literal: true

module Plannet
  # Test implementation for REQ-08: Application displays or stores Must Support elements.
  # This test requires manual attestation from the user.
  class Req08MustSupportDisplayTest < Inferno::Test
    include Inferno::DSL::Assertions

    id :req_08_must_support_display_test
    title 'Application displays or stores Must Support elements (Manual Attestation)'
    description %(
      **Requirement:** REQ-08
      **Description:** Application Actor SHOULD display Must Support data elements for human use or store for other purposes.
      **Conformance:** SHOULD

      **Test Steps:**
      1. The test identifies elements marked as 'Must Support' in the relevant Plan-Net Implementation Guide profiles.
      2. The list of Must Support elements is presented to the user.
      3. The user manually confirms whether their application displays these elements for human use or stores them for other purposes.

      **Instructions:** Please review the list of Must Support elements presented below. Based on your knowledge
      of the application under test, confirm whether it meets the requirement REQ-08 for these elements.
    )
    # Making the test optional aligns with the SHOULD conformance level and manual nature.
    # A failure in this test indicates a deviation from the SHOULD but may not block overall conformance.
    optional

    # Define which Plan-Net profiles to check for Must Support elements.
    # Replace these with the actual canonical URLs of the profiles defined in the target Plan-Net IG.
    # This list should be comprehensive for the resources relevant to the application's scope.
    PLANNET_PROFILES_TO_CHECK = [
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Practitioner',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Endpoint',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-InsurancePlan'
      # Add or remove profiles as relevant to the specific Plan-Net IG version and scope
    ].freeze

    # Helper method to extract Must Support elements from a profile's StructureDefinition
    # This assumes the IG resources (StructureDefinitions) are loaded and accessible via `ig_resources`.
    # The mechanism for loading `ig_resources` depends on the overall test kit setup.
    def get_must_support_elements(profile_url)
      profile = ig_resources&.profile_by_url(profile_url)
      unless profile&.snapshot&.element
        warning "Could not find snapshot elements for StructureDefinition: #{profile_url}. " \
                'Ensure the Plan-Net IG is correctly loaded.'
        return []
      end

      must_support_elements = []
      profile.snapshot.element.each do |element|
        # Check if the element itself is marked as Must Support
        is_must_support = element.mustSupport == true

        # Also check if any extensions on the element are Must Support
        # This handles cases where the extension is MS but the base element might not be.
        element.extension.each do |ext|
          # Look for the official Must Support extension definition if used
          # (Though `element.mustSupport` is the primary mechanism)
          # Example check (adjust if IG uses a specific extension for MS):
          # is_must_support ||= (ext.url == 'http://example.org/fhir/StructureDefinition/must-support-flag' && ext.valueBoolean == true)
        end

        if is_must_support
          # Use element.id for a potentially more stable identifier, fallback to path
          path = element.id || element.path
          # Clean up the path for better readability (remove resource type prefix if present)
          path = path.gsub(/^#{profile.type}\./, '')
          must_support_elements << "#{profile.type}.#{path}"
        end
      end
      must_support_elements.uniq # Return unique element paths
    end

    run do
      # Ensure IG resources are available
      unless ig_resources
        skip 'Implementation Guide resources not loaded. Cannot identify Must Support elements.'
      end

      all_must_support_elements = []
      profiles_checked = []
      profiles_missing = []

      PLANNET_PROFILES_TO_CHECK.each do |profile_url|
        must_supports = get_must_support_elements(profile_url)
        if must_supports.any?
          all_must_support_elements.concat(must_supports)
          profiles_checked << profile_url
        elsif ig_resources.profile_by_url(profile_url)
          # Profile found, but no MS elements identified
          info "No Must Support elements identified in profile: #{profile_url}"
          profiles_checked << profile_url # Still counts as checked
        else
          # Profile itself was not found
          profiles_missing << profile_url
        end
      end

      # Report any profiles that could not be found
      unless profiles_missing.empty?
        warning "Could not find the following Plan-Net profiles: #{profiles_missing.join(', ')}. " \
                'Must Support checks for these profiles were skipped.'
      end

      # If no Must Support elements were found across all checked profiles, skip the attestation.
      if all_must_support_elements.empty? && profiles_checked.any?
        skip "No Must Support elements were identified in the checked Plan-Net profiles: " \
             "#{profiles_checked.join(', ')}. Manual attestation cannot proceed."
      elsif all_must_support_elements.empty? && profiles_checked.empty?
        # This case means no profiles were found or loaded correctly.
        skip 'Could not find or process any specified Plan-Net profiles. Cannot identify Must Support elements.'
      end

      # Format the list of Must Support elements for display in the prompt
      must_support_list_markdown = all_must_support_elements.uniq.sort.map { |el| "* `#{el}`" }.join("\n")

      # Prompt the user for manual confirmation
      prompt(
        title: 'Manual Attestation for REQ-08: Must Support Element Handling',
        inputs: {
          confirmation: {
            title: 'Confirmation',
            description: 'Does your application display the Must Support elements listed below for human use, ' \
                         'or store them for other purposes, as required by REQ-08?',
            type: 'radio',
            options: {
              # Default to 'true' assuming compliance, user must actively select 'false'
              default: 'true',
              list_options: [
                { label: 'Yes, the application meets this requirement for the listed elements.', value: 'true' },
                { label: 'No, the application does not meet this requirement for one or more listed elements.', value: 'false' }
              ]
            }
          }
        },
        description: %(
          **Requirement REQ-08:** Application Actor SHOULD display Must Support data elements for human use or store for other purposes.

          The following elements have been identified as 'Must Support' based on the Plan-Net profiles checked:
          *(Profiles checked: #{profiles_checked.join(', ')})*

          #{must_support_list_markdown}

          Please confirm whether your application under test handles these elements according to the requirement.
        )
      ) # The prompt call pauses execution until the user submits the form.

      # 'confirmation' input value is available after the prompt returns.
      # It will be either 'true' or 'false' as a string.
      user_confirmed = (confirmation == 'true')

      # Assert that the user confirmed compliance.
      # If the user selects 'No' (confirmation == 'false'), this assertion will fail.
      # Since the test is optional, this failure indicates non-conformance with the SHOULD
      # requirement but doesn't necessarily block overall test suite success.
      assert user_confirmed, 'User attested that the application does not display or store all required Must Support elements. This does not meet the SHOULD requirement REQ-08.'

      # If the assertion passes, the test implicitly passes.
      pass 'User attested that the application displays or stores Must Support elements as required by REQ-08.'
    end
  end
end