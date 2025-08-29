# Test6_claude Inferno Test Suite
# Generated on: 2025-04-29 14:29:29

require 'inferno/dsl/test_suite'

# Application Actor - Application Actor tests
require_relative 'application_actor/application_actor/req_req_02_test'
require_relative 'application_actor/application_actor/req_req_06_test'
require_relative 'application_actor/application_actor/req_req_07_test'
require_relative 'application_actor/application_actor/req_req_08_test'
require_relative 'application_actor/application_actor/req_req_09_test'
require_relative 'application_actor/application_actor/req_req_31_test'

# Health Plan API - Health Plan API tests
require_relative 'health_plan_api/health_plan_api/req_req_01_test'
require_relative 'health_plan_api/health_plan_api/req_req_03_test'
require_relative 'health_plan_api/health_plan_api/req_req_04_test'
require_relative 'health_plan_api/health_plan_api/req_req_05_test'
require_relative 'health_plan_api/health_plan_api/req_req_10_test'
require_relative 'health_plan_api/health_plan_api/req_req_11_test'
require_relative 'health_plan_api/health_plan_api/req_req_12_test'
require_relative 'health_plan_api/health_plan_api/req_req_13_test'
require_relative 'health_plan_api/health_plan_api/req_req_14_test'
require_relative 'health_plan_api/health_plan_api/req_req_15_test'
require_relative 'health_plan_api/health_plan_api/req_req_16_test'
require_relative 'health_plan_api/health_plan_api/req_req_17_test'
require_relative 'health_plan_api/health_plan_api/req_req_18_test'
require_relative 'health_plan_api/health_plan_api/req_req_19_test'
require_relative 'health_plan_api/health_plan_api/req_req_20_test'
require_relative 'health_plan_api/health_plan_api/req_req_21_test'
require_relative 'health_plan_api/health_plan_api/req_req_22_test'
require_relative 'health_plan_api/health_plan_api/req_req_23_test'
require_relative 'health_plan_api/health_plan_api/req_req_24_test'
require_relative 'health_plan_api/health_plan_api/req_req_25_test'
require_relative 'health_plan_api/health_plan_api/req_req_26_test'
require_relative 'health_plan_api/health_plan_api/req_req_27_test'
require_relative 'health_plan_api/health_plan_api/req_req_28_test'
require_relative 'health_plan_api/health_plan_api/req_req_29_test'
require_relative 'health_plan_api/health_plan_api/req_req_30_test'
require_relative 'health_plan_api/health_plan_api/req_req_32_test'
require_relative 'health_plan_api/health_plan_api/req_req_33_test'
require_relative 'health_plan_api/health_plan_api/req_req_34_test'
require_relative 'health_plan_api/health_plan_api/req_req_35_test'
require_relative 'health_plan_api/health_plan_api/req_req_36_test'
require_relative 'health_plan_api/health_plan_api/req_req_37_test'
require_relative 'health_plan_api/health_plan_api/req_req_38_test'
require_relative 'health_plan_api/health_plan_api/req_req_39_test'
require_relative 'health_plan_api/health_plan_api/req_req_40_test'

module Test6_claude
  class Test6_claudeTestSuite < Inferno::TestSuite
    id :test6_claude_suite
    title 'Test6_claude Test Suite'
    description 'Test suite for validating Test6_claude Implementation Guide conformance'

    # Application Actor tests
    group do
      id :application_actor_group
      title 'Application Actor Tests'

      # Application Actor tests
      group do
        id :application_actor_application_actor_group
        title 'Application Actor Tests'

        test from: :req_req_02_test
        test from: :req_req_06_test
        test from: :req_req_07_test
        test from: :req_req_08_test
        test from: :req_req_09_test
        test from: :req_req_31_test
      end

    end

    # Health Plan API tests
    group do
      id :health_plan_api_group
      title 'Health Plan API Tests'

      # Health Plan API tests
      group do
        id :health_plan_api_health_plan_api_group
        title 'Health Plan API Tests'

        test from: :req_req_01_test
        test from: :req_req_03_test
        test from: :req_req_04_test
        test from: :req_req_05_test
        test from: :req_req_10_test
        test from: :req_req_11_test
        test from: :req_req_12_test
        test from: :req_req_13_test
        test from: :req_req_14_test
        test from: :req_req_15_test
        test from: :req_req_16_test
        test from: :req_req_17_test
        test from: :req_req_18_test
        test from: :req_req_19_test
        test from: :req_req_20_test
        test from: :req_req_21_test
        test from: :req_req_22_test
        test from: :req_req_23_test
        test from: :req_req_24_test
        test from: :req_req_25_test
        test from: :req_req_26_test
        test from: :req_req_27_test
        test from: :req_req_28_test
        test from: :req_req_29_test
        test from: :req_req_30_test
        test from: :req_req_32_test
        test from: :req_req_33_test
        test from: :req_req_34_test
        test from: :req_req_35_test
        test from: :req_req_36_test
        test from: :req_req_37_test
        test from: :req_req_38_test
        test from: :req_req_39_test
        test from: :req_req_40_test
      end

    end

  end
end
