# test8_gemini.rb

module Test8Gemini
  class TestSuite < Inferno::TestSuite
    id :test8_gemini
    title 'Test8 Gemini Suite'
    description 'A test suite for Test8 Gemini, focusing on Application Actor and Health Plan API requirements.'

    # Configure FHIR client:
    # All tests that interact with a FHIR server will use this client.
    # The FHIR server endpoint URL must be provided by the user running the tests.
    fhir_client do
      url :url,
          title: 'FHIR Server Endpoint URL',
          description: 'The base URL of the FHIR server to be tested (e.g., https://fhir.example.com/r4).'
    end

    # Require all test group files.
    # This makes their defined groups and tests available to the suite.

    # Application Actor related test files
    require_relative 'application_actor/application_level_requirements/req_08_test'
    require_relative 'application_actor/base_requirements/req_09_test'
    require_relative 'application_actor/core_conformance/req_07_test'

    # Health Plan API related test files
    require_relative 'health_plan_api/authentication/req_01_test'

    # Define the hierarchical structure of test groups.
    # This organization reflects the directory structure of the test files.

    group do
      id :test8_gemini_application_actor_group
      title 'Application Actor'
      description 'Contains test groups related to Application Actor requirements.'

      group do
        id :test8_gemini_application_level_requirements_group
        title 'Application Level Requirements'
        description 'Tests for application-level requirements concerning the Application Actor.'

        # Include the group defined in 'req_08_test.rb' by its ID.
        group from: :patient_tests_group
      end

      group do
        id :test8_gemini_base_requirements_group
        title 'Base Requirements'
        description 'Tests for fundamental base requirements for the Application Actor.'

        # Include the group defined in 'req_09_test.rb' by its ID.
        group from: :req_09_ms_interpretation_group
      end

      group do
        id :test8_gemini_core_conformance_group
        title 'Core Conformance'
        description 'Tests for core conformance capabilities of the Application Actor. Content from req_07_test.rb is loaded.'
        # The file 'application_actor/core_conformance/req_07_test.rb' is loaded via require_relative.
        # Any tests or groups defined within it are registered.
        # It is not referenced via 'group from:' as its ID was specified as 'None'.
      end
    end

    group do
      id :test8_gemini_health_plan_api_group
      title 'Health Plan API'
      description 'Contains test groups related to Health Plan API requirements.'

      group do
        id :test8_gemini_authentication_group
        title 'Authentication'
        description 'Tests for authentication mechanisms related to the Health Plan API.'

        # Include the group defined in 'req_01_test.rb' by its ID.
        group from: :test8_gemini_req_01_no_authentication_group
      end
    end
  end
end