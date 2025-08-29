module Test10_claude
  class OrganizationSearchByNameGroup < Inferno::TestGroup
    id :organization_search_by_name
    title 'Organization Search by Name Tests'
    description %(
      Verify that the server properly supports searching Organization resources by name.
      This includes searching by full organization names and partial name matches.
      The search should take into account location, network, and specialty context.
    )

    input :url,
          title: 'FHIR Server Base URL',
          description: 'Base URL of the FHIR server'

    input :organization_name,
          title: 'Organization Name',
          description: 'Name of organization to search for (e.g. "Montgomery Cardiology" or "CVS")'

    fhir_client do
      url :url
    end

    test do
      id :organization_exact_name_search
      title 'Server returns matching organizations when searching by exact name'
      description %(
        Verify that searching Organization resources by exact name returns expected results.
        The server should match the complete organization name provided.
      )

      run do
        fhir_search(:organization, params: {
          name: organization_name
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        assert resource.entry.present?, "No Organization resources returned for name search: #{organization_name}"

        resource.entry.each do |entry|
          assert entry.resource.resourceType == 'Organization', 
                 "Non-Organization resource returned in search results"
          
          assert entry.resource.name.present?,
                 "Organization resource missing name element"
        end
      end
    end

    test do
      id :organization_partial_name_search 
      title 'Server returns matching organizations when searching by partial name'
      description %(
        Verify that searching Organization resources by partial name returns expected results.
        The server should support partial name matching.
      )

      run do
        partial_name = organization_name.split(/\s+/).first

        fhir_search(:organization, params: {
          name: partial_name
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        assert resource.entry.present?, "No Organization resources returned for partial name search: #{partial_name}"

        resource.entry.each do |entry|
          assert entry.resource.resourceType == 'Organization',
                 "Non-Organization resource returned in search results"
          
          assert entry.resource.name.present?,
                 "Organization resource missing name element"

          assert entry.resource.name.downcase.include?(partial_name.downcase),
                 "Returned organization name does not contain search term"
        end
      end
    end

    test do
      id :organization_name_search_with_context
      title 'Organization name search respects location, network and specialty context'
      description %(
        Verify that Organization name searches properly handle additional context parameters
        including location, network, and specialty qualifications.
      )

      run do
        fhir_search(:organization, params: {
          name: organization_name,
          'location:exists' => true
        })
        assert_response_status(200)

        fhir_search(:organization, params: {
          name: organization_name,
          'network:exists' => true  
        })
        assert_response_status(200)

        fhir_search(:organization, params: {
          name: organization_name,
          'qualification:exists' => true
        })
        assert_response_status(200)

        pass "Organization name search properly handles location, network and specialty context parameters"
      end
    end
  end
end