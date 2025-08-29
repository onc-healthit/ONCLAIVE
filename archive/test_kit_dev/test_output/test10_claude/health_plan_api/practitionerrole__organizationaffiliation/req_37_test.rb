module Test10_claude
  class ActivePractitionerOrganizationSearchGroup < Inferno::TestGroup
    id :active_practitioner_org_search
    title 'Search for Active Practitioners and Organizations'
    description %(
      Validates server support for searching currently active Practitioners and Organizations.
      
      For Practitioners, tests searching PractitionerRole resources with date parameter.
      For Organizations, tests searching OrganizationAffiliation resources with date parameter.
    )

    input :url,
          title: 'FHIR Server Base URL',
          description: 'Base URL for the FHIR server under test'

    fhir_client do
      url :url
    end

    test do
      id :search_active_practitioners
      title 'Search for active PractitionerRole resources'
      description %(
        Search for currently active PractitionerRole resources using date parameter.
        Validates server handles date-based queries correctly.
      )

      run do
        current_date = Date.today.strftime('%Y-%m-%d')
        
        fhir_search(:practitioner_role, 
                   params: {
                     date: "ge#{current_date}",
                     _include: 'PractitionerRole:practitioner'
                   })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No PractitionerRole resources returned'

        resource.entry.each do |entry|
          next unless entry.resource.resourceType == 'PractitionerRole'
          assert entry.resource.active != false, 
                 "PractitionerRole #{entry.resource.id} is not active"
        end
      end
    end

    test do
      id :search_active_organizations  
      title 'Search for active OrganizationAffiliation resources'
      description %(
        Search for currently active OrganizationAffiliation resources using date parameter.
        Validates server handles date-based queries correctly.
      )

      run do
        current_date = Date.today.strftime('%Y-%m-%d')

        fhir_search(:organization_affiliation,
                   params: {
                     date: "ge#{current_date}",
                     _include: 'OrganizationAffiliation:organization'
                   })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No OrganizationAffiliation resources returned'

        resource.entry.each do |entry|
          next unless entry.resource.resourceType == 'OrganizationAffiliation'
          assert entry.resource.active != false,
                 "OrganizationAffiliation #{entry.resource.id} is not active"
        end
      end
    end
  end
end