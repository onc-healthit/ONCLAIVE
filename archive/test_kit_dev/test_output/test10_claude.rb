require_relative 'health_plan_api/organization/req_34_test'
require_relative 'health_plan_api/organizationaffiliation/req_36_test'
require_relative 'health_plan_api/plan_net_organization/req_38_test'
require_relative 'health_plan_api/practitionerrole/req_35_test'
require_relative 'health_plan_api/practitionerrole__organizationaffiliation/req_37_test'

module Test10Claude
  class TestSuite < Inferno::TestSuite
    title 'Test10 Claude Test Suite'
    description 'Test suite for health plan API endpoints'

    # Configure FHIR client
    config do
      input :url,
            title: 'FHIR Server URL',
            description: 'URL of the FHIR server to test'
    end

    # Organization Tests
    group from: :organization_search_by_name

    # OrganizationAffiliation Tests  
    group from: :organization_specialty_search

    # PlanNet Organization Tests
    group from: :network_contact_handling_test

    # PractitionerRole Tests
    group from: :provider_specialty_search

    # PractitionerRole & OrganizationAffiliation Tests
    group from: :active_practitioner_org_search
  end
end