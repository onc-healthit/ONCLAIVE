require_relative 'health_plan_api/req_34_test'
require_relative 'health_plan_api/req_35_test'
require_relative 'health_plan_api/req_36_test'
require_relative 'health_plan_api/req_37_test'
require_relative 'health_plan_api/req_38_test'

module Test9Claude
  class TestSuite < Inferno::TestSuite
    title 'Test9 Claude Test Suite'
    description 'Test suite for validating Health Plan API functionality'

    # Configure FHIR client
    config do
      input :url,
            title: 'Health Plan API URL',
            description: 'URL of the FHIR server'
    end
    
    # Define FHIR client
    fhir_client do
      url :url
    end

    # Group definitions
    group from: :organization_search_by_name
    group from: :provider_specialty_search  
    group from: :organization_specialty_search
    group from: :active_practitioners_organizations_search
    group from: :network_contact_department_handling
  end
end