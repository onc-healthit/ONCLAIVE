# frozen_string_literal: true

require_relative './shared/resource_validation' # Assuming validation helpers are in this shared module

module Plannet
  # Test Group for REQ-04: Must Support Element Population
  # Description: "Health Plan API SHALL populate all Must Support data elements in query results"
  # Actor: Health Plan API
  # Conformance: SHALL
  class MustSupportPopulationGroup < Inferno::TestGroup
    include Plannet::ResourceValidation # Include shared validation methods

    id :plannet_req_04_must_support_population
    title 'REQ-04: Must Support Element Population'
    description %(
      **Description**: "Health Plan API SHALL populate all Must Support data elements in query results"

      **Actor**: Health Plan API

      **Conformance**: SHALL

      This test group verifies that all data elements marked as "Must Support"
      in the relevant Plan Net FHIR profiles are populated in the resources
      returned by the server in response to queries.

      It checks resources retrieved in previous tests (e.g., search results).
      Each test within this group focuses on a specific resource type defined
      in the Plan Net Implementation Guide, validating that instances of that
      resource type include all Must Support elements defined by their corresponding
      Plan Net profile.
    )

    # Define inputs for resources gathered in previous tests.
    # These inputs are expected to be JSON strings representing arrays of FHIR resources.
    input :retrieved_organizations_json,
          title: 'Retrieved Organization Resources',
          description: 'JSON array of Organization resources retrieved in previous tests.',
          type: 'textarea',
          optional: true
    input :retrieved_practitioners_json,
          title: 'Retrieved Practitioner Resources',
          description: 'JSON array of Practitioner resources retrieved in previous tests.',
          type: 'textarea',
          optional: true
    input :retrieved_locations_json,
          title: 'Retrieved Location Resources',
          description: 'JSON array of Location resources retrieved in previous tests.',
          type: 'textarea',
          optional: true
    input :retrieved_healthcare_services_json,
          title: 'Retrieved HealthcareService Resources',
          description: 'JSON array of HealthcareService resources retrieved in previous tests.',
          type: 'textarea',
          optional: true
    input :retrieved_organization_affiliations_json,
          title: 'Retrieved OrganizationAffiliation Resources',
          description: 'JSON array of OrganizationAffiliation resources retrieved in previous tests.',
          type: 'textarea',
          optional: true
    input :retrieved_practitioner_roles_json,
          title: 'Retrieved PractitionerRole Resources',
          description: 'JSON array of PractitionerRole resources retrieved in previous tests.',
          type: 'textarea',
          optional: true
    input :retrieved_endpoints_json,
          title: 'Retrieved Endpoint Resources',
          description: 'JSON array of Endpoint resources retrieved in previous tests.',
          type: 'textarea',
          optional: true

    # Define outputs to store the IDs of resources that passed validation.
    output :validated_organization_ids_json,
           :validated_practitioner_ids_json,
           :validated_location_ids_json,
           :validated_healthcare_service_ids_json,
           :validated_organization_affiliation_ids_json,
           :validated_practitioner_role_ids_json,
           :validated_endpoint_ids_json

    # Define the canonical URLs for the Plan Net profiles.
    # TODO: Replace these placeholder URLs with the actual canonical URLs from the Plan Net IG.
    ORGANIZATION_PROFILE_URL = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization'.freeze
    PRACTITIONER_PROFILE_URL = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Practitioner'.freeze
    LOCATION_PROFILE_URL = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location'.freeze
    HEALTHCARE_SERVICE_PROFILE_URL = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService'.freeze
    ORGANIZATION_AFFILIATION_PROFILE_URL = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation'.freeze
    PRACTITIONER_ROLE_PROFILE_URL = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole'.freeze
    ENDPOINT_PROFILE_URL = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Endpoint'.freeze

    # --- Tests for Must Support Population ---

    test :plannet_req_04_organization_must_support do
      id :plannet_req_04_organization_must_support
      title 'Organization resources include Must Support elements'
      description %(
        Verifies that all retrieved Organization resources contain Must Support
        elements as defined in the Plan Net Organization profile:
        `#{ORGANIZATION_PROFILE_URL}`.
        Skipped if no Organization resources were retrieved in previous tests.
      )
      input :retrieved_organizations_json
      output :validated_organization_ids_json

      run do
        skip_if retrieved_organizations_json.blank?, 'No Organization resources found to validate.'
        # Use the shared validation method which includes Must Support checks
        results = check_must_support_for_list(retrieved_organizations_json, ORGANIZATION_PROFILE_URL, 'Organization')

        # Process messages (errors/warnings)
        results[:messages].each do |msg|
          # Use send to call warning() or error() based on msg[:type]
          # Prepend resource reference for context
          message_text = msg[:resource] ? "[#{msg[:resource]}] #{msg[:message]}" : msg[:message]
          send(msg[:type], message_text)
        end

        # Assert that no errors were found (which implies Must Support elements were present)
        assert results[:messages].none? { |msg| msg[:type] == 'error' }, 'Found validation errors impacting Must Support requirements. Check messages for details.'

        # Pass if no errors
        pass "Successfully validated Must Support elements for #{results[:validated_ids].length} Organization resource(s)."
        output validated_organization_ids_json: results[:validated_ids].to_json
      end
    end

    test :plannet_req_04_practitioner_must_support do
      id :plannet_req_04_practitioner_must_support
      title 'Practitioner resources include Must Support elements'
      description %(
        Verifies that all retrieved Practitioner resources contain Must Support
        elements as defined in the Plan Net Practitioner profile:
        `#{PRACTITIONER_PROFILE_URL}`.
        Skipped if no Practitioner resources were retrieved in previous tests.
      )
      input :retrieved_practitioners_json
      output :validated_practitioner_ids_json

      run do
        skip_if retrieved_practitioners_json.blank?, 'No Practitioner resources found to validate.'
        results = check_must_support_for_list(retrieved_practitioners_json, PRACTITIONER_PROFILE_URL, 'Practitioner')

        results[:messages].each do |msg|
          message_text = msg[:resource] ? "[#{msg[:resource]}] #{msg[:message]}" : msg[:message]
          send(msg[:type], message_text)
        end
        assert results[:messages].none? { |msg| msg[:type] == 'error' }, 'Found validation errors impacting Must Support requirements. Check messages for details.'

        pass "Successfully validated Must Support elements for #{results[:validated_ids].length} Practitioner resource(s)."
        output validated_practitioner_ids_json: results[:validated_ids].to_json
      end
    end

    test :plannet_req_04_location_must_support