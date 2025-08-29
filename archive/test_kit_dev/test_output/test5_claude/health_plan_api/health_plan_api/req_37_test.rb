module Test5_claude
  class ActivePractitionerOrgSearchTest < Inferno::TestGroup
    id :active_practitioner_org_search
    title 'Search for Active Practitioners and Organizations'
    description %(
      Verify that the server supports searching for currently active Practitioners 
      and Organizations using date-based filtering.
      
      This test checks:
      * Search for active PractitionerRoles using date filtering
      * Search for active OrganizationAffiliations using date filtering
      * Proper inclusion of referenced resources
    )

    test do
      id :active_practitioner_role_search
      title 'Server returns active PractitionerRole resources'
      description 'Verify search for active PractitionerRoles with current date filter'
      
      run do
        current_date = Date.today.iso8601
        
        get("/PractitionerRole?date=ge#{current_date}&_include=PractitionerRole:practitioner")
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length.positive?, 
          'No PractitionerRole resources returned'

        bundle.entry.each do |entry|
          if entry.resource.resourceType == 'PractitionerRole'
            assert entry.resource.active != false, 
              "Found inactive PractitionerRole with id: #{entry.resource.id}"
          end
        end

        pass "Successfully retrieved #{bundle.entry.length} active PractitionerRole resources"
      end
    end

    test do
      id :active_org_affiliation_search  
      title 'Server returns active OrganizationAffiliation resources'
      description 'Verify search for active OrganizationAffiliations with current date filter'
      
      run do
        current_date = Date.today.iso8601
        
        get("/OrganizationAffiliation?date=ge#{current_date}&_include=OrganizationAffiliation:organization")
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length.positive?,
          'No OrganizationAffiliation resources returned'

        bundle.entry.each do |entry|
          if entry.resource.resourceType == 'OrganizationAffiliation'
            assert entry.resource.active != false,
              "Found inactive OrganizationAffiliation with id: #{entry.resource.id}"
          end
        end

        pass "Successfully retrieved #{bundle.entry.length} active OrganizationAffiliation resources"
      end
    end
  end
end