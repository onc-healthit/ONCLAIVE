module Test
  class TestSuite < Inferno::TestSuite
    title 'Test Suite'
    description 'A test suite for testing FHIR implementations'

    # Configure FHIR client
    config do
      input :url,
            title: 'FHIR Server URL',
            description: 'URL of the FHIR server to test against'
    end

    # Load test files
    require_relative 'application_actor/application_level_requirements/req_08_test'
    require_relative 'application_actor/base_requirements/req_09_test'
    require_relative 'application_actor/core_conformance/req_07_test'
    require_relative 'health_plan_api/authentication/req_01_test'

    # Define test groups 
    group do
      id :application_actor_tests
      title 'Application Actor Tests'

      group do
        id :application_level_requirements
        title 'Application Level Requirements'
        
        group from: :must_support_display_group
      end

      group do
        id :base_requirements
        title 'Base Requirements'

        group from: :missing_must_support_interpretation
      end

      group do
        id :core_conformance
        title 'Core Conformance'

        group from: :must_support_elements_processing
      end
    end

    group do
      id :health_plan_api_tests
      title 'Health Plan API Tests'

      group do
        id :authentication
        title 'Authentication'

        group from: :no_auth_required
      end
    end
  end
end