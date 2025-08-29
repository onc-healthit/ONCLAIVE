require_relative 'application_actor/application_level_requirements/req_08_test'
require_relative 'application_actor/core_conformance/req_07_test'
require_relative 'health_plan_api/authentication/req_01_test'
require_relative 'health_plan_api/organizationaffiliation/req_11_test'
require_relative 'health_plan_api/plan_net_network/req_37_test'
require_relative 'health_plan_api/plan_net_organization/req_34_test'
require_relative 'health_plan_api/plan_net_organization/req_38_test'
require_relative 'health_plan_api/plan_net_organizationaffiliation/req_36_test'
require_relative 'health_plan_api/plan_net_practitionerrole/req_35_test'

module Test10Gemini
  class TestSuite < Inferno::TestSuite
    id :test10_gemini
    title 'Test10_gemini'
    description 'Inferno test suite for Test10_gemini'

    fhir_client do
      url :url
    end

    input :url,
          title: 'FHIR Endpoint',
          description: 'URL of the FHIR endpoint'

    group do
      title 'Application Actor'
      id :application_actor_group

      group do
        title 'Application Level Requirements'
        id :application_level_requirements_group
        group from: :test10_gemini_req_08_must_support_display_group
      end

      group do
        title 'Core Conformance'
        id :core_conformance_group
        group from: :req_07_must_support_elements_processing_group
      end
    end

    group do
      title 'Health Plan API'
      id :health_plan_api_group

      group do
        title 'Authentication'
        id :authentication_group
        group from: :req_01_no_authentication_group
      end

      group do
        title 'Organization Affiliation'
        id :organizationaffiliation_group
        group from: :req_11_organization_network_documentation
      end

      group do
        title 'Plan Net Network'
        id :plan_net_network_group
        group from: :req_37_search_active_practitioners_organizations
      end

      group do
        title 'Plan Net Organization'
        id :plan_net_organization_group
        group from: :req_34_organization_search_group
        group from: :req_38_department_contact_group
      end

      group do
        title 'Plan Net Organization Affiliation'
        id :plan_net_organization_affiliation_group
        group from: :req_36_organization_specialty_search
      end

      group do
        title 'Plan Net Practitioner Role'
        id :plan_net_practitioner_role_group
        group from: :req_35_provider_search_by_specialty_group
      end
    end
  end
end