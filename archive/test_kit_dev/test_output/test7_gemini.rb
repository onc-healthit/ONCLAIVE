# Test7_gemini Inferno Test Suite
# Generated on: 2025-05-14 12:13:28

# Application Actor - Application-Level Requirements tests
require_relative 'test7_gemini/application_actor/application_level_requirements/req_08_test'

# Application Actor - Base Requirements tests
require_relative 'test7_gemini/application_actor/base_requirements/req_09_test'

# Application Actor - CORE Conformance tests
require_relative 'test7_gemini/application_actor/core_conformance/req_07_test'

# Health Plan API - Authentication tests
require_relative 'test7_gemini/health_plan_api/authentication/req_01_test'

module Test7_gemini
  class Test7_geminiTestSuite < Inferno::TestSuite
    id :test7_gemini_suite
    title 'Test7_gemini Test Suite'
    description 'Test suite for validating Test7_gemini Implementation Guide conformance'

    input :url,
          title: 'FHIR Server Base Url'

    fhir_client do
      url :url
    end

    # Application Actor tests
    group do
      id :application_actor_group
      title 'Application Actor Tests'

      # Application-Level Requirements tests
      group do
        id :application_actor_application_level_requirements_group
        title 'Application-Level Requirements Tests'

        group from: :req_08_test
      end

      # Base Requirements tests
      group do
        id :application_actor_base_requirements_group
        title 'Base Requirements Tests'

        group from: :req_09_test
      end

      # CORE Conformance tests
      group do
        id :application_actor_core_conformance_group
        title 'CORE Conformance Tests'

        group from: :req_07_test
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

        group from: :req_01_test
      end

    end

  end
end
