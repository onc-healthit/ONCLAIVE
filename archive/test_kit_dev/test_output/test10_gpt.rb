module Test10Gpt
  class TestSuite < Inferno::TestSuite
    id :test10_gpt
    title 'Test10 GPT Suite'
    
    input :url, title: 'FHIR Server URL', description: 'URL of the FHIR server'

    fhir_client do
      url :url
    end

    group do
      title 'Health Plan API'

      group do
        title 'Plan Net Organization'
        
        group from: :req_34_organization_search_by_name
        group from: :req_38_network_contact_handling
      end

      group do
        title 'Plan Net OrganizationAffiliation'
        
        group from: :req_36_organization_search_by_specialty
      end

      group do
        title 'Plan Net PractitionerRole'
        
        group from: :req_35_provider_search_by_specialty
        group from: :req_37_test_group
      end
    end
  end
end

require_relative 'health_plan_api/plan_net_organization/req_34_test'
require_relative 'health_plan_api/plan_net_organization/req_38_test'
require_relative 'health_plan_api/plan_net_organizationaffiliation/req_36_test'
require_relative 'health_plan_api/plan_net_practitionerrole/req_35_test'
require_relative 'health_plan_api/plan_net_practitionerrole/req_37_test'