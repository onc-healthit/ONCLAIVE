module Test5_claude
  class ProviderSpecialtySearchTest < Inferno::TestGroup
    id :provider_specialty_search
    title 'Provider Search by Specialty'
    description %(
      Verify that the server supports searching for providers by specialty via 
      PractitionerRole.specialty, including optional qualification parameters for
      location, network, and name.
    )

    fhir_client do
      url :url
    end

    test do
      id :specialty_basic_search
      title 'Server returns valid results for PractitionerRole specialty search'
      description %(
        Test will perform a search for PractitionerRole resources using specialty
        and validate the returned results.
      )
      
      input :specialty_code,
            title: 'Specialty Code',
            description: 'The specialty code to search for (e.g. cardio)',
            default: '394579002' # Example SNOMED code for Cardiology

      run do
        fhir_search(:practitionerrole, params: {
          specialty: specialty_code
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:practitionerrole)

        skip_if search_results.empty?, 'No PractitionerRole resources found for the given specialty'

        search_results.each do |resource|
          assert resource.specialty&.any? { |s| s.coding&.any? { |c| c.code == specialty_code } },
                "PractitionerRole #{resource.id} does not have the specified specialty code"
        end
      end
    end

    test do
      id :specialty_qualified_search
      title 'Server handles qualified specialty search parameters'
      description %(
        Test will perform searches for PractitionerRole resources using specialty
        combined with location, network, and name qualifiers.
      )
      
      input :specialty_code,
            title: 'Specialty Code',
            description: 'The specialty code to search for',
            default: '394579002'
            
      input :location_id,
            title: 'Location ID',
            description: 'A valid Location resource ID',
            optional: true
            
      input :network_id,
            title: 'Network ID', 
            description: 'A valid Network resource ID',
            optional: true
            
      input :provider_name,
            title: 'Provider Name',
            description: 'Name to search for',
            optional: true

      run do
        search_params = {
          specialty: specialty_code
        }

        search_params[:location] = location_id if location_id.present?
        search_params[:network] = network_id if network_id.present?
        search_params[:name] = provider_name if provider_name.present?

        fhir_search(:practitionerrole, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_bundle_entries(:practitionerrole)

        skip_if search_results.empty?, 'No PractitionerRole resources found matching search criteria'

        search_results.each do |resource|
          assert resource.specialty&.any? { |s| s.coding&.any? { |c| c.code == specialty_code } },
                "PractitionerRole #{resource.id} does not have the specified specialty code"

          if location_id.present?
            assert resource.location&.any? { |loc| loc.reference.include?(location_id) },
                  "PractitionerRole #{resource.id} is not associated with the specified location"
          end

          if network_id.present?
            assert resource.network&.any? { |net| net.reference.include?(network_id) },
                  "PractitionerRole #{resource.id} is not associated with the specified network"
          end
        end
      end
    end
  end
end