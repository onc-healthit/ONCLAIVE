# Test3_claude Inferno Test Suite
# Generated on: 2025-04-24 10:53:11

require 'inferno/dsl/test_suite'

# Application Actor - Application-Level Requirements tests
require_relative 'application_actor/application-level_requirements/req_req_08_test'

# Application Actor - Base Requirements tests
require_relative 'application_actor/base_requirements/req_req_09_test'

# Application Actor - CORE Conformance tests
require_relative 'application_actor/core_conformance/req_req_07_test'

# Health Plan API - Authentication tests
require_relative 'health_plan_api/authentication/req_req_01_test'

module Test3_claude
  class Test3_claudeTestSuite < Inferno::TestSuite
    id :test3_claude_suite
    title 'Test3_claude Test Suite'
    description 'Test suite for validating Test3_claude Implementation Guide conformance'

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

    end

  end
end
