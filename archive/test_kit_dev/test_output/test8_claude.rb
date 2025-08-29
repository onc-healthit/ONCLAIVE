require_relative 'application_actor/application_level_requirements/req_08_test'
require_relative 'application_actor/base_requirements/req_09_test'
require_relative 'application_actor/core_conformance/req_07_test'
require_relative 'health_plan_api/authentication/req_01_test'

module Test8Claude
  class TestSuite < Inferno::TestSuite
    id :test8_claude
    title 'Test8 Claude Test Suite'
    description 'Test suite for FHIR requirements testing'

    # Configure FHIR Client
    config_option :url, title: 'FHIR Server URL', description: 'URL of the FHIR server'

    # Configure FHIR client
    fhir_client do
      url :url
    end

    # Health Plan API Groups
    group do
      id :health_plan_api
      title 'Health Plan API Requirements'
      description 'Tests for Health Plan API conformance'

      group from: :no_authentication_requirement
    end

    # Application Actor Groups  
    group do
      id :application_actor
      title 'Application Actor Requirements'
      description 'Tests for Application Actor conformance'

      group do
        id :application_level
        title 'Application Level Requirements'
        description 'Application level conformance tests'

        group from: :must_support_display_group
      end

      group do
        id :base_requirements
        title 'Base Requirements'
        description 'Base level conformance tests'

        group from: :must_support_interpretation_group
      end

      group do
        id :core_conformance
        title 'Core Conformance Requirements'
        description 'Core conformance tests'

        group from: :must_support_elements_processing
      end
    end
  end
end