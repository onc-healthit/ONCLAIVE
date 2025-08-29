# test9_gemini.rb

# Import all test files.
# These paths are relative to this main module file (test9_gemini.rb),
# assuming test9_gemini.rb is at the root of the 'Test9_gemini' test suite directory.
require_relative 'health_plan_api/health_plan_api/req_34_test'
require_relative 'health_plan_api/health_plan_api/req_35_test'
require_relative 'health_plan_api/health_plan_api/req_36_test'
require_relative 'health_plan_api/health_plan_api/req_37_test'
require_relative 'health_plan_api/health_plan_api/req_38_test'

module Test9Gemini
  class Test9GeminiSuite < Inferno::TestSuite
    id :test9_gemini # Snake_case name of the test suite as ID
    title 'Test9 Gemini' # Human-readable title for the test suite

    # Configure the FHIR client for the entire suite.
    # This provides a common configuration point for the FHIR server URL.
    fhir_client do
      url :fhir_server_url,
          title: 'FHIR Server URL',
          description: 'Enter the base URL of the FHIR server to be tested.',
          default: 'http://example.com/fhir' # An optional default value
    end

    # Define the hierarchy of test groups.
    # This structure reflects the directory structure: health_plan_api/health_plan_api/
    group do
      id :health_plan_api_outer_group # Unique ID for the top-level directory group
      title 'Health Plan API' # Title reflecting the 'health_plan_api' directory

      # Nested group for the inner 'health_plan_api' directory
      group do
        id :health_plan_api_inner_group # Unique ID for the nested directory group
        title 'Health Plan API Core' # Title reflecting the inner 'health_plan_api' directory

        # Include test groups from imported files using their defined IDs.
        # From req_35_test.rb (ID: req_35_provider_specialty_search_group)
        group from: :req_35_provider_specialty_search_group

        # From req_36_test.rb (ID: req_36_org_search_by_specialty)
        group from: :req_36_org_search_by_specialty

        # Note:
        # - req_34_test.rb defines a TestSuite (ID: example_test_suite).
        #   TestSuites are not typically embedded as groups within another TestSuite.
        #   They are loaded via 'require_relative' and can be run independently.
        # - req_37_test.rb is of 'Unknown' type and has no ID.
        #   It's imported via 'require_relative'. If it contains tests, they would need to be
        #   part of a group with an ID to be included via 'group from:'.
        # - req_38_test.rb defines a TestSuite (ID: sample_error_suite), similar to req_34_test.rb.
      end
    end
  end
end