# Plannet Inferno Test Suite
# Generated on: 2025-04-30 12:44:33

require 'inferno/dsl/test_suite'

# Application Actor - Application-Level Requirements tests
require_relative 'application_actor/application-level_requirements/req_req_08_test'

# Application Actor - Base Requirements tests
require_relative 'application_actor/base_requirements/req_req_09_test'

# Application Actor - CORE Conformance tests
require_relative 'application_actor/core_conformance/req_req_07_test'

# Application Actor - Security tests
require_relative 'application_actor/security/req_req_03_test'

# Health Plan API - Authentication tests
require_relative 'health_plan_api/authentication/req_req_01_test'

# Health Plan API - Cross-Resource tests
require_relative 'health_plan_api/cross-resource/req_req_06_test'

# Health Plan API - General Requirements tests
require_relative 'health_plan_api/general_requirements/req_req_04_test'

# Health Plan API - Global tests
require_relative 'health_plan_api/global/req_req_05_test'

# Health Plan API - OrganizationAffiliation tests
require_relative 'health_plan_api/organizationaffiliation/req_req_11_test'

# Health Plan API - Plan-Net API Security tests
require_relative 'health_plan_api/plan-net_api_security/req_req_02_test'

# Health Plan API - PractitionerRole tests
require_relative 'health_plan_api/practitionerrole/req_req_10_test'

module Plannet
  class PlannetTestSuite < Inferno::TestSuite
    id :plannet_suite
    title 'Plannet Test Suite'
    description 'Test suite for validating Plannet Implementation Guide conformance'

    # Application Actor tests
    group do
      id :application_actor_group
      title 'Application Actor Tests'

      # Application-Level Requirements tests
      group do
        id :application_actor_application-level_requirements_group
        title 'Application-Level Requirements Tests'

        test from: :req_req_08_test
      end

      # Base Requirements tests
      group do
        id :application_actor_base_requirements_group
        title 'Base Requirements Tests'

        test from: :req_req_09_test
      end

      # CORE Conformance tests
      group do
        id :application_actor_core_conformance_group
        title 'CORE Conformance Tests'

        test from: :req_req_07_test
      end

      # Security tests
      group do
        id :application_actor_security_group
        title 'Security Tests'

        test from: :req_req_03_test
      end

    end

    # Health Plan API tests
    group do
      id :health_plan_api_group
      title 'Health Plan API Tests'

      # Authentication tests
      group do
        id :health_plan_api_authentication_group
        title 'Authentication Tests'

        test from: :req_req_01_test
      end

      # Cross-Resource tests
      group do
        id :health_plan_api_cross-resource_group
        title 'Cross-Resource Tests'

        test from: :req_req_06_test
      end

      # General Requirements tests
      group do
        id :health_plan_api_general_requirements_group
        title 'General Requirements Tests'

        test from: :req_req_04_test
      end

      # Global tests
      group do
        id :health_plan_api_global_group
        title 'Global Tests'

        test from: :req_req_05_test
      end

      # OrganizationAffiliation tests
      group do
        id :health_plan_api_organizationaffiliation_group
        title 'OrganizationAffiliation Tests'

        test from: :req_req_11_test
      end

      # Plan-Net API Security tests
      group do
        id :health_plan_api_plan-net_api_security_group
        title 'Plan-Net API Security Tests'

        test from: :req_req_02_test
      end

      # PractitionerRole tests
      group do
        id :health_plan_api_practitionerrole_group
        title 'PractitionerRole Tests'

        test from: :req_req_10_test
      end

    end

  end
end
