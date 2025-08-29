module Test9_claude
  class OrganizationSearchByNameGroup < Inferno::TestGroup
    id :organization_search_by_name
    title 'Organization Search by Name Tests'
    description %(
      Verify that the server supports searching Organization resources by name.
      
      The Plan-Net design requires the ability to search Organizations by name, 
      such as "Montgomery Cardiology" or "CVS", with optional qualifications 
      like location, network, and specialty.
    )

    fhir_client do
      url :url
      oauth_credentials :credentials
    end

    input :url,
          title: 'Server Base URL',
          description: 'Base URL for FHIR server'

    input :credentials,
          title: 'OAuth Credentials',
          type: :oauth_credentials,
          optional: true

    input :organization_name,
          title: 'Organization Name',
          description: 'Name of organization to search for (e.g. Montgomery Cardiology)'

    test do
      id :organization_name_exact_search
      title 'Server returns matching organizations when searching by exact name'
      description %(
        This test verifies that the server properly handles Organization searches
        using an exact name match.
      )
      
      makes_request :organization_name_search

      run do
        fhir_search(:organization, params: {name: organization_name}, name: :organization_name_search)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, "No Organizations returned for name search with: #{organization_name}"

        resource.entry.each do |entry|
          assert entry.resource.is_a?(FHIR::Organization), "Expected resource type Organization but found #{entry.resource.class}"
          assert entry.resource.name.present?, 'Organization resource is missing name element'
        end

        matches = resource.entry.any? do |entry|
          entry.resource.name.downcase == organization_name.downcase
        end
        
        assert matches, "No Organizations found with exact name match for: #{organization_name}"
      end
    end

    test do
      id :organization_name_partial_search 
      title 'Server returns matching organizations when searching by partial name'
      description %(
        This test verifies that the server properly handles Organization searches
        using partial name matching.
      )

      input :organization_name

      run do
        partial_name = organization_name.split(/\s+/).first
        fhir_search(:organization, params: {name: partial_name})

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, "No Organizations returned for partial name search with: #{partial_name}"

        resource.entry.each do |entry|
          assert entry.resource.is_a?(FHIR::Organization), "Expected resource type Organization but found #{entry.resource.class}"
          assert entry.resource.name.present?, 'Organization resource is missing name element'
          assert entry.resource.name.downcase.include?(partial_name.downcase), 
                 "Organization name '#{entry.resource.name}' does not contain search term '#{partial_name}'"
        end
      end
    end

    test do
      id :organization_name_validation
      title 'Server properly handles invalid organization name searches'
      description %(
        This test verifies that the server returns appropriate responses for
        invalid organization name searches.
      )

      run do
        invalid_name = 'Invalid*Organization$Name'
        fhir_search(:organization, params: {name: invalid_name})
        assert_response_status([200, 400, 404])

        fhir_search(:organization, params: {name: ''}) 
        assert_response_status([200, 400, 404])
      end
    end
  end
end