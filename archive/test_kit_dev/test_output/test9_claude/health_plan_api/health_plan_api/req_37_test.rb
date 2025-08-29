module Test9_claude
  class ActivePractitionersOrganizationsGroup < Inferno::TestGroup
    id :active_practitioners_organizations_search
    title 'Search for Active Practitioners and Organizations'
    description %(
      Verify the server properly handles search operations for currently active 
      Practitioners and Organizations using date-based queries.
    )

    input :url,
          title: 'FHIR Server Base URL',
          description: 'Base URL for the FHIR server under test'

    fhir_client do
      url :url
    end

    test do
      id :active_practitioners_search
      title 'Search for currently active Practitioners'
      description %(
        Test the PractitionerRole search operation to find currently active practitioners
        using date parameters.
      )

      run do
        current_date = Date.today.strftime('%Y-%m-%d')
        
        fhir_search(:practitionerrole, 
                   params: {
                     date: "ge#{current_date}",
                     _include: 'PractitionerRole:practitioner'
                   })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No PractitionerRole resources returned'

        resource.entry.each do |entry|
          if entry.resource.resourceType == 'PractitionerRole'
            assert entry.resource.period.nil? || 
                   entry.resource.period.end.nil? ||
                   Date.parse(entry.resource.period.end) >= Date.today,
                   'Returned PractitionerRole is not currently active'
          end
        end
      end
    end

    test do
      id :active_organizations_search
      title 'Search for currently active Organizations'
      description %(
        Test the OrganizationAffiliation search operation to find currently active
        organizations using date parameters.
      )

      run do
        current_date = Date.today.strftime('%Y-%m-%d')

        fhir_search(:organizationaffiliation,
                   params: {
                     date: "ge#{current_date}",
                     _include: 'OrganizationAffiliation:organization'
                   })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No OrganizationAffiliation resources returned'

        resource.entry.each do |entry|
          if entry.resource.resourceType == 'OrganizationAffiliation'
            assert entry.resource.period.nil? ||
                   entry.resource.period.end.nil? ||
                   Date.parse(entry.resource.period.end) >= Date.today,
                   'Returned OrganizationAffiliation is not currently active'
          end
        end
      end
    end
  end
end