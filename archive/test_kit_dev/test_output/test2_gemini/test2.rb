# Test2 Inferno Test Suite
# Generated on: 2025-04-24 10:05:27

require 'inferno/dsl/test_suite'

# Health Plan API - Authentication tests
require_relative 'health_plan_api/authentication/req_req_01_test'

module Test2
  class Test2TestSuite < Inferno::TestSuite
    id :test2_suite
    title 'Test2 Test Suite'
    description 'Test suite for validating Test2 Implementation Guide conformance'

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

    # Application tests
    group do
      id :application_group
      title 'Application Tests'

    end

  end
end
