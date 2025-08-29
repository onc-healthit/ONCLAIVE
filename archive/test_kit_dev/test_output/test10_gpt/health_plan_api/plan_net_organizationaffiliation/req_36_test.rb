module Test10Gpt
  class OrganizationSearchBySpecialtyGroup < Inferno::TestGroup
    id :req_36_organization_search_by_specialty
    title 'Organization Search by Specialty'
    description %(
      This test group verifies that the Health Plan API supports searching for 
      organizations by specialty, specifically focusing on the 
      OrganizationAffiliation.specialty field. The test will ensure that 
      organizations with a specified specialty, such as "Compounding Pharmacy," 
      can be retrieved and that the search can be qualified by location, network, 
      and name.
    )

    input :server_url, 
          title: 'FHIR Server URL',
          description: 'The base URL for the FHIR server'
    input :specialty_code,
          title: 'Specialty Code',
          description: 'The code representing the specialty to search for',
          default: 'compounding-pharmacy'
    input :location, :network, :name

    fhir_client do
      url :server_url
    end

    test do
      id :organization_search_by_specialty
      title 'Search for Organizations by Specialty'
      description %(
        This test performs a search for organizations by the specialty code 
        provided. It verifies that the server returns a valid Bundle of 
        OrganizationAffiliation resources with the specified specialty. The search 
        may also be qualified by location, network, and name if provided.
      )

      run do
        search_params = { specialty: specialty_code }
        search_params[:location] = location if location.present?
        search_params[:network] = network if network.present?
        search_params[:name] = name if name.present?

        fhir_search(:organization_affiliation, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert resource.entry.present?, 'No OrganizationAffiliation resources returned for the specified specialty search.'

        resource.entry.each do |entry|
          affiliation = entry.resource
          assert affiliation.specialty.any? { |s| s.coding.any? { |c| c.code == specialty_code } },
                 "OrganizationAffiliation does not have the expected specialty code: #{specialty_code}"
        end
      end
    end
  end
end