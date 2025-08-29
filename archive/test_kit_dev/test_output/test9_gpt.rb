require_relative 'health_plan_api/health_plan_api/req_34_test'
require_relative 'health_plan_api/health_plan_api/req_35_test'
require_relative 'health_plan_api/health_plan_api/req_36_test'
require_relative 'health_plan_api/health_plan_api/req_37_test'
require_relative 'health_plan_api/health_plan_api/req_38_test'

module Test9Gpt
  class TestSuite < Inferno::TestSuite
    id :test9_gpt
    title 'Test9 GPT'
    description 'A test suite for testing health plan API functionalities.'

    input :url, title: 'FHIR Server URL', description: 'URL of the FHIR server to test against'

    fhir_client do
      url :url
    end

    group do
      title 'Health Plan API Tests'

      group from: :organization_search_by_name_group
      group from: :req_35_provider_search_by_specialty
      group from: :organization_search_by_specialty_group
      group from: :req_37_test_group
      group from: :req_38_network_contact_handling
    end
  end
end