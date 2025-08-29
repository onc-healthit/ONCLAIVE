module Test6_claude
  class ActivePractitionersAndOrgsGroup < Inferno::TestGroup
    id :active_practitioners_and_orgs
    title 'Search for Active Practitioners and Organizations'
    description %(
      Verify that the server supports searching for currently active Practitioners and Organizations.
      
      Two search scenarios are tested:
      1. Search for active PractitionerRole resources using date parameter
      2. Search for active OrganizationAffiliation resources using date parameter
    )

    fhir_client do
      url :url
    end

    test do
      id :active_practitioner_role_search
      title 'Server returns active PractitionerRole resources'
      description %(
        Search for currently active PractitionerRole resources using a date parameter.
        The date parameter should filter for resources active on or after the current date.
      )

      run do
        current_date = Date.today.strftime('%Y-%m-%d')
        
        get "/PractitionerRole?date=ge#{current_date}&_include=PractitionerRole:practitioner"

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource

        assert bundle.entry.present?, 'No PractitionerRole resources returned'
        
        bundle.entry.each do |entry|
          if entry.resource.resourceType == 'PractitionerRole'
            assert entry.resource.active != false, 
              "PractitionerRole #{entry.resource.id} is not active"
          end
        end

        pass "Successfully retrieved #{bundle.entry.length} active PractitionerRole resources"
      end
    end

    test do
      id :active_org_affiliation_search  
      title 'Server returns active OrganizationAffiliation resources'
      description %(
        Search for currently active OrganizationAffiliation resources using a date parameter.
        The date parameter should filter for resources active on or after the current date.
      )

      run do
        current_date = Date.today.strftime('%Y-%m-%d')

        get "/OrganizationAffiliation?date=ge#{current_date}&_include=OrganizationAffiliation:organization"

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource

        assert bundle.entry.present?, 'No OrganizationAffiliation resources returned'

        bundle.entry.each do |entry|
          if entry.resource.resourceType == 'OrganizationAffiliation'
            assert entry.resource.active != false,
              "OrganizationAffiliation #{entry.resource.id} is not active"
          end
        end

        pass "Successfully retrieved #{bundle.entry.length} active OrganizationAffiliation resources"
      end
    end
  end
end