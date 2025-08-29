module Test5_claude
  class ActivePractitionerSearchGroup < Inferno::TestGroup
    id :active_practitioner_org_search
    title 'Search for Active Practitioners and Organizations'
    description %(
      This test verifies the server's ability to search for currently active Practitioners 
      and Organizations using date-based queries. It validates both:
      
      1. PractitionerRole search with date filters and _include
      2. OrganizationAffiliation search with date filters and _include
    )

    fhir_client do
      url :url
    end

    test do
      id :active_practitioner_search
      title 'Search for active PractitionerRoles'
      description %(
        Verify server can search for active PractitionerRoles using date criteria
      )

      run do
        current_date = Date.today.strftime('%Y-%m-%d')
        
        fhir_search(:practitionerrole, params: {
          date: "ge#{current_date}",
          _include: 'PractitionerRole:practitioner'
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length.positive?, 
          'No PractitionerRole resources returned'

        bundle.entry.each do |entry|
          if entry.resource.resourceType == 'PractitionerRole'
            assert entry.resource.period.nil? || 
                   entry.resource.period.end.nil? ||
                   DateTime.parse(entry.resource.period.end) >= DateTime.now,
              "Found PractitionerRole that is not currently active"
          end
        end

        # Verify _include worked
        assert bundle.entry.any? { |e| e.resource.resourceType == 'Practitioner' },
          'No Practitioner resources were included in response'
      end
    end

    test do
      id :active_organization_search  
      title 'Search for active OrganizationAffiliations'
      description %(
        Verify server can search for active OrganizationAffiliations using date criteria
      )

      run do
        current_date = Date.today.strftime('%Y-%m-%d')

        fhir_search(:organizationaffiliation, params: {
          date: "ge#{current_date}",
          _include: 'OrganizationAffiliation:organization'
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length.positive?,
          'No OrganizationAffiliation resources returned'

        bundle.entry.each do |entry|
          if entry.resource.resourceType == 'OrganizationAffiliation'
            assert entry.resource.period.nil? ||
                   entry.resource.period.end.nil? ||
                   DateTime.parse(entry.resource.period.end) >= DateTime.now,
              "Found OrganizationAffiliation that is not currently active"
          end
        end

        # Verify _include worked
        assert bundle.entry.any? { |e| e.resource.resourceType == 'Organization' },
          'No Organization resources were included in response'
      end
    end
  end
end