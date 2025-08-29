module Test6_claude
  class ProviderSpecialtySearchGroup < Inferno::TestGroup
    id :provider_specialty_search
    title 'Provider Search by Specialty'
    description %(
      Verify that the server supports searching for providers by specialty.
      This test focuses on searching PractitionerRole resources by specialty,
      optionally refined by location and network parameters.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :search_practitioner_role_by_specialty
      title 'Server returns valid results when searching PractitionerRole by specialty'
      description %(
        This test verifies that the server supports searching PractitionerRole 
        resources by specialty, returning appropriate matches.
      )
      
      input :specialty_code,
            title: 'Specialty Code',
            description: 'The specialty code to search for (e.g. "208D00000X" for General Practice)'

      run do
        fhir_search(:practitionerrole, params: {
          specialty: specialty_code
        })
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
        
        skip_if search_bundle.total.zero?, 'No PractitionerRole resources found for the given specialty'
        
        search_bundle.entry.each do |entry|
          assert entry.resource.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } },
                "Found PractitionerRole without matching specialty code #{specialty_code}"
        end
      end
    end

    test do
      id :search_practitioner_role_by_specialty_location
      title 'Server supports searching PractitionerRole by specialty and location'
      description %(
        This test verifies that the server supports searching PractitionerRole 
        resources by both specialty and location parameters.
      )
      
      input :specialty_code
      input :location_id,
            title: 'Location ID',
            description: 'A valid Location resource ID to filter results'

      run do
        fhir_search(:practitionerrole, params: {
          specialty: specialty_code,
          location: location_id
        })
        
        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries
        
        skip_if search_bundle.total.zero?, 'No PractitionerRole resources found matching both criteria'
        
        search_bundle.entry.each do |entry|
          resource = entry.resource
          assert resource.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } },
                "Found PractitionerRole without matching specialty code"
          assert resource.location.any? { |loc| loc.reference.include?(location_id) },
                "Found PractitionerRole not associated with specified location"
        end
      end
    end

    def assert_valid_bundle_entries
      assert search_bundle.present?, 'No Bundle returned from search'
      assert search_bundle.entry.present?, 'Bundle contains no entries'
      search_bundle.entry.each do |entry|
        assert entry.resource.present?, 'Bundle entry has no resource'
        assert_resource_type(:practitionerrole, entry.resource)
        assert_valid_resource(entry.resource)
      end
    end

    def search_bundle
      @search_bundle ||= resource
    end
  end
end