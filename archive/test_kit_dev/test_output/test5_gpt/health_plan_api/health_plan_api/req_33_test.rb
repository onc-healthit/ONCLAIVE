module Test5Gpt
  class ProviderSearchByNameTestGroup < Inferno::TestGroup
    id :req_33_provider_search_by_name
    title 'Provider Search by Name'
    description %(
      This test group verifies that the Health Plan API supports searching for providers by name.
      Specifically, it tests the ability to search for a Practitioner resource using the `name` parameter.
    )

    input :server_url, :access_token, :practitioner_name

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :provider_search_by_name
      title 'Search Practitioner by Name'
      description %(
        Verify that the server can search for a Practitioner resource using the `name` parameter.
        The test will pass if a Practitioner with the specified name can be found.
      )

      run do
        search_params = { name: practitioner_name }
        reply = fhir_search(:practitioner, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        assert_valid_resource

        practitioners = reply.resource.entry.map(&:resource)
        assert practitioners.any?, "No Practitioner resources found with the name '#{practitioner_name}'."

        practitioners.each do |practitioner|
          names = practitioner.name.map { |n| "#{n.given.join(' ')} #{n.family}" }
          assert names.any? { |n| n.include?(practitioner_name) }, 
                 "Practitioner names do not match the search name '#{practitioner_name}'."
        end
      end
    end
  end
end